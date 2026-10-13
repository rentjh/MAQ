# 1인 신차 장기렌트 에이전시: 영업 운영 용량과 Claude 자동화 설계 (기준 2026-10-13)

Research scope: lead handling, sales calls and follow-up for a solo 신차 장기렌트 agent working about 100 leads a month while also producing content, and which parts Claude (Max plan) can realistically automate.
Method note: I used 15 search and fetch calls. Several Korean-specific benchmarks (call length, 견적 time, 렌트 텔레마케팅 conversion) were **not found** in reliable sources. Those items appear under Inferences or Gaps and are clearly marked. Treat vendor-published statistics as indicative only.

---

## Q1. Speed-to-lead, contact rates, call attempts, best times

### Takeaway
Every study points the same way: contact the lead within minutes and keep calling for about six attempts over 1–2 weeks. Calling fast matters far more than calling at the "best" time of day. Most headline numbers are old (2007–2013) and come from vendors, so use them as direction rather than precise multipliers.

### Cited Findings
- **Lead Response Management Study (2007, James Oldroyd with InsideSales.com):** the odds of *contacting* a lead were about 100x higher within 5 minutes than at 30 minutes. The odds of *qualifying* the lead were about 21x higher. The data covered 3 years, 6 companies, 15,000+ leads and 100,000+ call attempts. It is vendor data analyzed by an academic, is not peer reviewed, and is often mislabeled as an "MIT study." — [Callingly summary](https://callingly.com/blog/state-of-speed-to-lead); [electronics-cooling (2011)](https://www.electronics-cooling.com/2011/06/increase-your-sales-effectiveness-by-21x-in-25-minutes/); [MIT-labeled PDF](https://www.mortech.com/hs-fs/hub/25649/file-13535879-pdf/docs/mit_study.pdf)
- **HBR (2011, Oldroyd, McElheran & Elkington, about 1.25M leads):** firms that responded within 1 hour were about 7x more likely to qualify the lead than firms that waited one hour longer, and about 60x more likely than firms that waited 24 hours or more. This uses a different time window from the 21x figure, so the two numbers should not be combined. — [Callingly](https://callingly.com/blog/state-of-speed-to-lead)
- Xant.ai (formerly InsideSales) reports that 35–50% of sales go to the vendor that responds first. — [Callingly](https://callingly.com/blog/state-of-speed-to-lead)
- **Recent data, auto vertical (vendor):** Clearline AI (2026, 53 dealerships) found an average first response of more than 9 hours. Only 13.2% of dealerships responded within 5 minutes, and nearly 1 in 3 had not responded after 5 days. McKinsey (Jan 2025) found that 56% of dealership leads arrive after hours and 37% of dealerships handle them within an hour. — [Callingly](https://callingly.com/blog/state-of-speed-to-lead)
- **Insurance and mortgage, comparable regulated verticals:** Invoca reports a 39% missed-call rate in insurance. IIABA reports that 78% of consumers call several agencies. In mortgage (Insellerate/MBA 2024), 40% of leads were never contacted and fewer than 2% were called within the first hour. Weekday 6–8 PM is the peak window for insurance inquiries. — [Callingly](https://callingly.com/blog/state-of-speed-to-lead)
- **Number of attempts (Velocify, about 3.5M leads, c. 2013):** 93% of *converted* leads were reached by the 6th call. Leads that needed more than 7 calls to reach were 45% less likely to convert. The widely quoted "391% higher conversion when called within 1 minute" also comes from Velocify, but Callingly flags it as hard to verify or possibly misattributed. — [NatLawReview](https://natlawreview.com/node/60555/printable/print); [mpamag](https://www.mpamag.com/us/mortgage-industry/business-growth/does-calling-at-certain-times-of-day-really-improve-customer-contact/34468); [Callingly caveat](https://callingly.com/blog/state-of-speed-to-lead)
- **Best time:** in the Velocify data, the best and worst times of day differed by only 2.6 percentage points in contact rate. Timing calls to when the prospect showed interest improved contact by 110%, while the "optimal time" approach improved it by only 7%. The older 2007 InsideSales data found Wednesday and Thursday best (+49.7% over the worst day) and 4–6 PM the best hours. — [mpamag](https://www.mpamag.com/au/news/general/does-calling-at-certain-times-of-day-really-improve-conversion/293837); [christopholivierconsulting](https://christopholivierconsulting.com/?p=5971)
- Many reps stop after 2 attempts, while the commonly cited claim is that 80% of conversions need 5 or more touches. Callingly calls this an "industry benchmark" but gives no source. — [Callingly](https://callingly.com/blog/state-of-speed-to-lead)

### Inferences
- In Korea, 장기렌트 leads usually come from a DB or 랜딩 form, and customers often submit to several agencies at once (비교견적 behavior). This is an inference from the Korean marketing articles in Q6 and the insurance "78% call multiple agencies" pattern. If so, the first-responder effect probably applies strongly. A solo operator should treat **first contact within 5 minutes during working hours** as the top-priority operational KPI. Because the operator cannot always answer the phone, an **instant 알림톡 acknowledgement** sent automatically when the form is submitted is a practical substitute for "contact" when they cannot call right away.
- Recommended cadence (inference that synthesizes Velocify and HBR; I found no Korea-specific study): 6 call attempts over about 10 days, for example D0 ×2 (immediately and 2–3 hours later), D1, D3, D6 and D10. Pair them with 알림톡 or SMS after missed calls. After that, move the lead to the long nurture track (monthly content and 프로모션 notices for those who gave 광고 동의).
- After-hours leads, which are likely a large share given the 56% figure for dealerships, should get an automatic message plus a call at 09:00 the next day.

### Gaps
- I found no Korean public data on contact rates or response times for 장기렌트 or 리스 leads.
- I could not verify the original Velocify report directly. The 93% and 2.6pp figures come from secondary summaries.

---

## Q2. Time budget and realistic capacity (100 leads/month plus content)

### Takeaway
I found **no published benchmark** for 장기렌트 call length, 견적 preparation time or decision cycle. The capacity model below is an inference built from the brief's assumptions (a 2–4 week 비교견적 decision, then 출고 대기) and the attempt counts above. It suggests that about 100 new leads a month is workable for one person (roughly 45–60 hours a month on sales work) only if first contact, quotes and follow-up messages are heavily templated. Content production then has to fit into about 40–60 hours a month.

### Cited Findings
- Korean 장기렌트 marketing commentary says that counting raw 상담 신청 (DB) volume is the wrong KPI because the 신차 장기렌트 market is saturated. It recommends tracking conversion by source, 상담 결과 and 조건 일치율. — [i-boss 493387](https://www.i-boss.co.kr/ab-2987-493387); [i-boss 500127](https://www.i-boss.co.kr/ab-2987-500127)
- A 3-stage pre-qualification (ad copy, landing page, pre-submit question) that screens for no 연체 and confirmed income reduces lead count but is claimed to raise the 상담→계약 conversion rate. This is a vendor or promotional article. — [i-boss 500127](https://www.i-boss.co.kr/ab-2987-500127)
- 6 call attempts reach 93% of the leads that eventually convert (Velocify). — [NatLawReview](https://natlawreview.com/node/60555/printable/print)

### Inferences (model; all numbers are assumptions, not sourced)
| Activity | Assumption | Per month at 100 leads |
|---|---|---|
| Call attempts | about 4 dials per lead on average (many reached early); about 1.5 min per unanswered dial including logging | about 10 h |
| First consult call (reached leads, assume about 60–70%) | 10–15 min | about 12–17 h |
| Quote prep (assume about 50% request a 견적), 2–3 options per customer across 캐피탈/렌트사 rate sheets | 15–25 min manual; 5–10 min with templated Claude comparison | 4–20 h |
| Follow-up calls and messages during the 2–4 week decision window (about 3 touches per quoted lead) | 5 min each | about 12 h |
| Contract, 서류, 심사, 출고 coordination (assume 5–10 contracts/month) | 2–3 h per contract across 출고 대기 | 10–30 h |
| **Total sales ops** | | **about 50–90 h/month** |
- With about 160 working hours a month, that leaves roughly 70–110 hours for content, ads, admin and existing-customer care. With automation (an instant 알림톡 response, Claude-drafted quotes and notes, and an auto-generated daily priority list), the sales block can plausibly drop toward the low end of the range (about 50 h).
- The binding constraint is **response latency rather than total hours**. A solo operator filming shorts or meeting a customer cannot call within 5 minutes. Recommended design: batch content in fixed blocks (for example mornings 08–10 and one half-day a week), keep "phone-on" windows when leads arrive (lunch and 18–21 for the evening peak, by inference from the insurance 6–8 PM peak), and rely on automated 알림톡 acknowledgement plus a callback-booking link outside those windows.
- Pipeline load: with a 2–4 week decision cycle plus 출고 대기 (often months for popular models), there will be roughly 150–250 open opportunities at any time (inference). That is too many to track mentally, so a CRM or a Sheets pipeline with "next action date" is mandatory.

### Gaps
- No Korean data on average 장기렌트 consult call length, 견적 request rate or lead-to-contract conversion. Industry chatter often mentions low single-digit to around 10% conversion for purchased DBs, but I found no reliable source, so this is unverified.
- No 보험·렌트 텔레마케팅 productivity benchmarks (calls per hour, talk time) were found in this search pass.

---

## Q3. Korean messaging, STT and automation tools, and costs

### Takeaway
알림톡 (information only, no consent needed, template pre-approval required) is the backbone for instant acknowledgement and quote delivery. Marketing follow-ups must use 브랜드메시지, which replaced 친구톡 on 2026-01-01, or SMS/LMS with 광고 동의. Per-message costs are low (tens of won). Exact current 알림톡 and SMS unit prices from 솔라피 and 알리고 could not be retrieved and must be checked on the vendors' pricing pages.

### Cited Findings
- 솔라피: 브랜드메시지 자유형 (text or image) costs **₩100 per message plus VAT**. The notice is dated 2025-12-04 and was revised 2026-02-06. — [Solapi notice](https://solapi.com/notices/notices-2025-12-04)
- **친구톡 ended 2025-12-31.** From 2026-01-01, 친구톡 requests are automatically sent as 브랜드메시지 (자유형). 브랜드메시지 pricing differs depending on whether the recipient is a 채널 friend (blog revised July 2026). — [Solapi notice](https://solapi.com/notices/notices-2025-12-04); [bizgo blog](https://blog.bizgo.io/howto/alimtalk-friendtalk-difference/)
- 알림톡 needs only a phone number and no receive consent. It is limited to informational content, and Kakao must review the template first. Any advertising content, even partial, makes it unsendable. 브랜드메시지 requires consent. — [bizgo](https://blog.bizgo.io/howto/alimtalk-friendtalk-difference/); [channel.io guide](https://docs.channel.io/macgai-guide/ko/articles/bc502668-광고-문자-보내기)
- Solapi charges per message from a prepaid balance, with prices that vary by message type. Integrations are billed separately. — [Solapi guide](https://solapi.com/guides/start)
- 알림톡 falls back to SMS when the recipient does not use KakaoTalk, has blocked the channel, or there is a Kakao failure. The SMS integration is needed for this fallback. — [Kakao Cloud guide](https://guide.centerflow.kakaocloud.com/undefined-1/console/kakaotalk/alim_sms)
- NHN Cloud and NCP SENS are alternative API providers for SMS, LMS and 알림톡. — [NCP SENS](https://m.ncloud.com/product/applicationService/sens)
- Advertising-message law (정보통신망법 제50조): 광고성 정보 needs prior explicit consent. Sending is banned after opt-out or withdrawal, opting out must be free (a 무료수신거부 number is required), and fines go up to ₩30M. — [channel.io](https://docs.channel.io/macgai-guide/ko/articles/bc502668-광고-문자-보내기); [Solapi policy guide](https://solapi.com/guides/policyguidelines)
- Apple's native iPhone call recording (iOS 18.1+) plays an audible announcement that recording has started, which cannot be disabled, and can produce AI transcription and summaries. — [iter.kr](https://iter.kr/%EC%95%84%EC%9D%B4%ED%8F%B0-%ED%86%B5%ED%99%94%EB%85%B9%EC%9D%8C-%EB%B0%A9%EB%B2%95); [damoang](https://damoang.net/applemoang/3445)

### Inferences
- Unverified from my own knowledge: 정보통신망법 제50조 also requires *separate* consent for 광고성 정보 sent from 21:00 to 08:00. This was not confirmed by search, so check the 국가법령정보센터 text. It matters for automated night follow-ups: 정보성 견적 알림톡 is fine, but promotions are not.
- A typical message volume of about 100 leads × about 6 messages is roughly 600 messages a month. At tens of won each for 알림톡 or SMS, plus ₩100 for any 브랜드메시지, the cost is likely under ₩50,000–100,000 a month (inference; unit prices not verified).
- Suggested stack (inference): landing form → webhook → n8n or Make (or Google Apps Script) → Google Sheets as a lightweight CRM → Solapi or Aligo API sends an instant 알림톡 ("접수 완료, 10분 내 연락") and alerts the operator by phone push or KakaoTalk to themselves. Call recordings from Android 통화녹음 (with an auto-summary such as 에이닷 on Galaxy or SKT) or iPhone native recording are exported as text and summarized into CRM notes by Claude.
- 클로바노트 and 다글로 are mainly for meetings and uploaded audio files, and need a recording file. 에이닷 통화요약 works on calls directly (inference; their pricing and policies were not verified in this pass).

### Gaps
- Exact 2026 unit prices for 솔라피 알림톡, SMS and LMS, 알리고, and NHN Cloud were not retrieved.
- Current pricing, retention and terms for 에이닷 통화요약, 클로바노트 and 다글로 were not verified.
- n8n and Make costs were not retrieved. n8n self-hosting is free, and the cloud version is a paid subscription (general knowledge; unverified for 2026).

---

## Q4. What Claude (Max plan) can realistically automate

### Takeaway
Claude handles the text-heavy middle of the funnel well: comparing quotes from rate-sheet exports, turning call transcripts into CRM notes, drafting follow-up messages, building a daily priority list from a Sheets or CSV export, writing content drafts, and producing weekly ad reports from 네이버 검색광고 and Meta CSV exports. Real-time first response (the 5-minute window) should **not** depend on Claude. It belongs to deterministic tools (webhook → 알림톡). Usage limits are shared across the Claude apps and Claude Code. Training on consumer chats is on unless the user opts out, which matters under 개인정보보호법.

### Cited Findings
- **Max plan limits:** there is a 5-hour session limit and a weekly limit, plus a separate weekly limit for the top model. "These limits are shared across Claude and Claude Code" (web, desktop, mobile, Claude Code and IDE). Max 5x users who hit limits can upgrade to 20x. Usage credits or API credits can extend usage. — [support.claude.com](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)
- **Cowork scheduled tasks:** released 2026-02-25. They run only while the computer is awake and the Claude Desktop app is open. Cowork and Claude Code draw from the same 5-hour window. A temporary doubling of Cowork 5-hour limits (June to July/August 2026) is reported, but sources conflict on the end date. — [fast.io guide](https://www.fast.io/resources/claude-max-plan-features.md); [letsdatascience](https://letsdatascience.com/news/anthropic-doubles-claude-cowork-usage-limits-db601c73) (secondary sources)
- **Claude Code Routines:** these are saved Claude Code configurations that run on Anthropic cloud infrastructure on a schedule, from an API call or on a GitHub event, without the user's computer being on. They are managed at claude.ai/code/routines, through `/schedule`, or from Desktop. They are a research preview on Pro, Max, Team and Enterprise, launched around April 2026. — [makerkit guide](https://makerkit.dev/blog/tutorials/claude-code-routines-guide); [agentsroom](https://agentsroom.dev/blog/claude-code-routines-cloud-vs-local-scheduled-tasks) (third-party; official docs not retrieved)
- **Claude in Chrome:** beta for all Max subscribers from 2025-11-24, later all paid plans. It supports scheduled shortcuts (daily, weekly, monthly). A June 2026 "GA" claim is unverified. — [Claude in Chrome release notes](https://support.claude.com/en/articles/12306336-claude-in-chrome-release-notes); [claude-manual](https://claude-manual.com/en/products/chrome/guide)
- **Data and privacy:** under the Consumer Terms update (Aug 2025, decision deadline 2025-09-28), Free, Pro and Max chats and Claude Code sessions may be used for training unless the user opts out (Settings → Privacy → "Improve Claude"). With training on, retention is up to 5 years; with it off, 30 days. Commercial products (Team, Enterprise, API) are excluded. Incognito chats are reportedly not used for training. — [implicator.ai](https://www.implicator.ai/anthropics-five-year-data-plan-for-claude-consumer-users.md); [businesstoday](https://www.businesstoday.in/amp/technology/news/story/anthropic-to-use-claude-conversations-for-ai-training-unless-users-opt-out-by-september-28-491530-2025-08-29) (secondary; confirm on Anthropic's privacy center)
- AI기본법 obligations target "AI 사업자" who provide AI products or services to users. **People who use AI as a tool for their own work or creation are excluded.** — [kbmaeil](https://kbmaeil.com/article/20260121500740); [i-boss](https://www.i-boss.co.kr/ab-74668-5969)

### Inferences: task-by-task feasibility
| Task | Feasible? | Inputs needed | How |
|---|---|---|---|
| 견적 비교표 from 캐피탈/렌트사 rate sheets | Yes, high value | Rate-sheet PDF or Excel exports (no public APIs; 견적 systems are partner portals) | Cowork or Claude Code reads the folder and outputs a comparison table plus a customer-friendly 알림톡/PDF text. Human must verify numbers (risk of misreading). |
| Call transcript → CRM note (needs, budget, 차종, 신용, next action) | Yes | Transcript text from 에이닷, iPhone or 클로바노트 | Paste or drop the file, Claude outputs structured fields, then Google Sheets (via Drive/Sheets connector or CSV) |
| Follow-up message drafts (정보성 vs 광고성 versions) | Yes | CRM row | Templates. The human sends or approves. 알림톡 templates must be Kakao-approved, so Claude fills variables rather than writing free text. |
| Daily lead priority list | Yes | Sheets/CSV export with lead date, attempts, last touch, stage | Cowork scheduled task (needs the PC on) or a Routine (cloud; needs a data source the Routine can reach, such as a GitHub repo or connector) |
| Content drafts (blog, shorts scripts, 출고 후기 posts) | Yes, strongest fit | Brand guide, past posts | Batch weekly. Note 표시광고법 and AI기본법 labeling questions are covered by a separate researcher. |
| Weekly ad report (네이버 검색광고, Meta) | Yes via CSV export; partly via Claude in Chrome | CSV from 광고 관리자 / 검색광고 시스템 | Exporting CSV and running Claude analysis is the most reliable path. Claude in Chrome can navigate dashboards, but logged-in ad accounts raise prompt-injection and mis-click risk. Prefer read-only report pages. |
| Instant first response (under 5 min) | **No; use deterministic automation** | Webhook | n8n/Make/Apps Script → 알림톡. Claude is not a real-time trigger engine, and Cowork tasks depend on the PC being on. |
- Usage: these workloads are mostly short text jobs, so Max 5x is likely enough. Heavy Claude Code or agentic browser use is what consumes limits (inference).
- **개인정보 risk:** customer names, phone numbers, 주민번호, income and 신용 info are personal data, and 신용정보 is sensitive in practice. Recommendations (inference): turn off the "Improve Claude" training setting; mask or pseudonymize phone numbers and 주민번호 before pasting (use a lead ID); never paste 신분증 or 소득 서류 images; reflect overseas transfer and 처리위탁 in the 개인정보 처리방침 if customer data is processed by Claude (an overseas processor). Consider a Team plan if the business grows (commercial terms, no training).
- **Prompt injection:** ad dashboards, emails and web pages read by Claude in Chrome or by connectors can contain hostile text. Keep agentic browsing on read-only tasks and do not let it send messages or change bids without confirmation (inference, consistent with Anthropic's Chrome safety guidance noted in the release notes).

### Gaps
- No official numeric message or token caps for Max 5x or 20x. Anthropic does not publish them.
- Official code.claude.com Routines documentation was not retrieved directly. Routine details come from third-party guides.
- No native Claude connector for 네이버 검색광고 or Meta Ads was confirmed. The 네이버 검색광고 API exists, but I did not verify an MCP server for it.

---

## Q5. AI voice agents and AI 콜봇 for first contact: legal issues, acceptance, recommendation

### Takeaway
Since 2026-01-22, the AI기본법 has required a business that offers a generative-AI service to users to tell them in advance. An AI 콜봇 calling customers would very likely fall under this (one law-firm or advisory interpretation applies it to AI 상담 챗봇). There is a 1-year-plus 계도기간 (grace period). Korean 대기업 insurers use AI 콜봇 only under sandbox approval and with prior 마케팅 동의. For a solo 장기렌트 agent, the evidence favors a human first call plus an automated 알림톡, not an AI outbound caller.

### Cited Findings
- The AI기본법 and its 시행령 took effect on **2026-01-22**. 제31조 sets three duties: (1) prior notice when providing a generative-AI-based product or service, (2) labeling of generated outputs, and (3) deepfake labeling. Overseas providers serving Korean users are included. — [kbmaeil](https://kbmaeil.com/article/20260121500740); [Shin & Kim newsletter](https://shinkim.com/kor/media/newsletter/3142)
- One advisory piece says an advertiser who exposes AI functions to visitors (for example an AI 상담 챗봇 on its site) becomes a "이용사업자" subject to 제31조① prior notice. By extension, the same likely applies to AI 콜봇 (interpretation). — [i-boss](https://www.i-boss.co.kr/ab-74668-5969)
- MSIT published "인공지능 투명성 확보 안내 지침" with the law and runs a **계도기간 of 1 year or more**. Guidance may change. — [kbmaeil](https://kbmaeil.com/article/20260121500740); [lawtimes](https://www.lawtimes.co.kr/news/217123)
- Insurance precedent: 라이나생명's "AI 텔레마케터 기반 보험 모집" was designated an 혁신금융서비스 (sandbox) and applies only to consumers who agreed to marketing. NH농협손보 automated about 400k 완전판매 모니터링 calls a year with an AI 음성봇 (from Jan 2026). 삼성생명, KB손보 and 교보 also use AI 콜봇. — [hankyung 2026-02](https://www.hankyung.com/article/2026021919531); [sateconomy](https://sateconomy.co.kr/news/view/1065607394200157)
- Consumer acceptance (US, not Korea): in a WordPress VIP survey of 1,200 US consumers, 60% said they feel aversion when "AI" appears in brand messaging. — [wikidocs summary](https://wikidocs.net/blog/@jaehong/20125/)
- Recording or bot notice duties abroad (for example US all-party-consent states) put responsibility on the host or business even when a vendor controls the bot. — [beancount](https://beancount.io/ko/blog/2026/08/17/ai-notetaker-wiretap-bipa-compliance-guide)

### Inferences
- In Korea, recording a call you take part in is generally not illegal under 통신비밀보호법 (general knowledge; not re-verified here). However, transcribing and summarizing the call is 개인정보 processing, and sending it to an AI vendor is 처리위탁 or overseas transfer, so the 처리방침 and a short spoken notice ("상담 품질을 위해 통화가 녹음·요약됩니다") are prudent. A proposed bill requiring notice before recording has been discussed in past sessions. Its status as of Oct 2026 was **not verified**.
- An outbound AI 콜봇 also triggers 정보통신망법 rules on 광고성 전화 (consent) and AI기본법 prior notice. Lead forms would therefore need explicit consent covering AI calls. Speaking to a bot on a high-trust, high-ticket product (₩500k–1M+/month for 3–5 years) risks hurting the trust advantage a 1인 agent has (inference).
- Recommendation for a solo operator (inference): do **not** deploy an outbound AI voice agent for first contact in 2026. Use (a) an instant 알림톡 plus a booking link, (b) human callback within the operator's phone-on windows, and (c) optionally an *inbound* after-hours AI answering or receptionist that collects name, car model and preferred callback time, clearly announced as AI. Revisit after the 계도기간 ends and MSIT guidance settles.

### Gaps
- No Korean survey on consumer acceptance of AI 콜봇 in car rental or leasing.
- No Korean AI voice vendor pricing (for example per-minute rates) was retrieved.
- Current 통화녹음 고지 법안 status was not found.

---

## Q6. Referral, retention, 재렌트 and 만기 customers as lead sources

### Takeaway
I found almost no sourced Korean material on referral or 만기 re-sales for 장기렌트 agents. Available Korean commentary focuses on paid DB quality. Logically, though, a solo agent's lowest-cost leads are existing customers nearing 만기 (3–5 year contracts) and their referrals. This is mostly inference.

### Cited Findings
- Korean 장기렌트 marketing articles focus on DB acquisition and filtering (no 연체, confirmed income) and on conversion tracking by channel. They do not cover referral or 만기 programs, and they are promotional. — [i-boss 500127](https://www.i-boss.co.kr/ab-2987-500127); [i-boss 493387](https://www.i-boss.co.kr/ab-2987-493387)
- Google Ads remarketing creatives should be rotated every 2–3 weeks because of ad fatigue. — [AMPM insight](https://inside.ampm.co.kr/insight/60491)
- 78% of homebuyers work with the first agent who responds (NAR 2025), which shows how much first contact matters in relationship sales. — [Callingly](https://callingly.com/blog/state-of-speed-to-lead)

### Inferences
- Build a "만기 캘린더" in the CRM: for each contract, store the start date, term and 만기, and schedule touches at 만기 −6 months (재렌트, 인수 or 반납 options explained), −3 months (new-model quote) and −1 month. A Claude scheduled task or Routine can generate a monthly "만기 도래 고객 list plus a personalized message draft."
- Referral: ask at the 출고 moment, when satisfaction peaks, and send a 정보성 알림톡 with a referral link. Any reward offer is 광고성, so it requires consent and the 표시광고 rules should be checked. Check whether 렌트사 or 캐피탈 contracts restrict referral payments (unverified).
- Repeat and referral leads likely need fewer call attempts and less 비교견적 time, which frees capacity. No data was found to quantify this.

### Gaps
- No data on 장기렌트 재계약 (re-rental) rates, referral share of sales, or agent commission structures for referrals.
- No Korean 영업인 community sources (for example Naver cafés) were accessible in this pass.
