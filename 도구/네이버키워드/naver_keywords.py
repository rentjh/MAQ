"""네이버 검색광고 API로 키워드 검색량·클릭수·경쟁도·순위별 예상 입찰가를 조회해 CSV로 저장합니다.

필요한 환경 변수 (검색광고 관리자 > 도구 > API 사용 관리에서 발급):
  NAVER_SA_CUSTOMER_ID  고객 ID
  NAVER_SA_API_KEY      액세스 라이선스
  NAVER_SA_SECRET_KEY   비밀키

사용법:
  python naver_keywords.py                     # keywords.txt → 결과_키워드조회.csv
  python naver_keywords.py --related 10        # 키워드마다 연관 키워드 상위 10개도 함께 저장
  python naver_keywords.py -i 내목록.txt -o 결과.csv

광고비가 들지 않는 조회 전용 API입니다(입찰·광고 생성 없음).
"""
import argparse
import base64
import csv
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.parse
import urllib.request

BASE = "https://api.searchad.naver.com"
POSITIONS = [1, 2, 3, 4, 5]


def _headers(method, uri):
    ts = str(int(time.time() * 1000))
    secret = os.environ["NAVER_SA_SECRET_KEY"].encode()
    sig = base64.b64encode(hmac.new(secret, f"{ts}.{method}.{uri}".encode(), hashlib.sha256).digest()).decode()
    return {
        "X-Timestamp": ts,
        "X-API-KEY": os.environ["NAVER_SA_API_KEY"],
        "X-Customer": os.environ["NAVER_SA_CUSTOMER_ID"],
        "X-Signature": sig,
        "Content-Type": "application/json; charset=UTF-8",
    }


def _call(method, uri, query=None, body=None):
    url = BASE + uri + ("?" + urllib.parse.urlencode(query) if query else "")
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=_headers(method, uri))
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 3:
                time.sleep(2 ** attempt)
                req = urllib.request.Request(url, data=data, method=method, headers=_headers(method, uri))
                continue
            raise SystemExit(f"API 오류 {e.code} {uri}: {e.read().decode(errors='replace')}")


def _num(v):
    # 검색량이 10 미만이면 API가 "< 10" 문자열을 돌려줌
    if isinstance(v, str):
        return 5 if "<" in v else float(v or 0)
    return v or 0


def keyword_stats(keywords):
    """keywordstool: 한 번에 힌트 키워드 최대 5개."""
    rows = {}
    for i in range(0, len(keywords), 5):
        batch = keywords[i:i + 5]
        res = _call("GET", "/keywordstool", {"hintKeywords": ",".join(batch), "showDetail": "1"})
        for k in res.get("keywordList", []):
            rows[k["relKeyword"]] = k
        time.sleep(0.3)
    return rows


def position_bids(keywords, device):
    """순위별 평균 입찰가(예상). 한 번에 여러 키워드×순위 조회."""
    out = {}
    for i in range(0, len(keywords), 20):
        batch = keywords[i:i + 20]
        items = [{"key": k, "position": p} for k in batch for p in POSITIONS]
        res = _call("POST", "/estimate/average-position-bid/keyword", body={"device": device, "items": items})
        for e in res.get("estimate", []):
            out[(e["keyword"], e["position"])] = e.get("bid")
        time.sleep(0.3)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", default="keywords.txt")
    ap.add_argument("-o", "--output", default="결과_키워드조회.csv")
    ap.add_argument("--related", type=int, default=0, help="키워드마다 연관 키워드 상위 N개 추가 저장")
    args = ap.parse_args()

    missing = [v for v in ("NAVER_SA_CUSTOMER_ID", "NAVER_SA_API_KEY", "NAVER_SA_SECRET_KEY") if not os.environ.get(v)]
    if missing:
        sys.exit("환경 변수가 없습니다: " + ", ".join(missing))

    with open(args.input, encoding="utf-8") as f:
        seeds = [l.strip().replace(" ", "") for l in f if l.strip() and not l.startswith("#")]
    seeds = list(dict.fromkeys(seeds))

    stats = keyword_stats(seeds)
    targets = [k for k in seeds if k in stats]
    if args.related:
        rel = sorted((k for k in stats if k not in seeds),
                     key=lambda k: _num(stats[k]["monthlyMobileQcCnt"]) + _num(stats[k]["monthlyPcQcCnt"]), reverse=True)
        targets += rel[: args.related * len(seeds)]
    not_found = [k for k in seeds if k not in stats]

    bids_m = position_bids(targets, "MOBILE")
    bids_p = position_bids(targets, "PC")

    cols = ["구분", "키워드", "월검색수_PC", "월검색수_모바일", "월검색수_합계", "월평균클릭_PC", "월평균클릭_모바일",
            "클릭률_PC(%)", "클릭률_모바일(%)", "평균노출광고수", "경쟁정도"] + \
           [f"모바일_{p}위_예상입찰가" for p in POSITIONS] + [f"PC_{p}위_예상입찰가" for p in POSITIONS]
    with open(args.output, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for k in targets:
            s = stats[k]
            pc, mo = _num(s["monthlyPcQcCnt"]), _num(s["monthlyMobileQcCnt"])
            w.writerow(["입력" if k in seeds else "연관", k, s["monthlyPcQcCnt"], s["monthlyMobileQcCnt"], pc + mo,
                        s.get("monthlyAvePcClkCnt"), s.get("monthlyAveMobileClkCnt"),
                        s.get("monthlyAvePcCtr"), s.get("monthlyAveMobileCtr"), s.get("plAvgDepth"), s.get("compIdx")] +
                       [bids_m.get((k, p)) for p in POSITIONS] + [bids_p.get((k, p)) for p in POSITIONS])
    print(f"저장: {args.output} ({len(targets)}개)")
    if not_found:
        print("조회 결과 없음(검색량이 거의 없거나 표기 차이): " + ", ".join(not_found))


if __name__ == "__main__":
    main()
