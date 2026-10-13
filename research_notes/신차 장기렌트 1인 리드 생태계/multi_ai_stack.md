# Multi-AI Tool Stack for a Solo Korean 신차 장기렌트 Agency (as of 2026-10-13)

Research date: 2026-10-13. Exchange rate assumption for KRW conversions: about 1,400 KRW/USD (unverified, used only to estimate). The only price fetched from an official pricing page is Google Gemini/Veo (page updated 2026-10-09). All other prices come from third-party aggregators and are marked **[unverified]**. openai.com/api/pricing returned HTTP 403 and could not be read directly.

## Q1. Strengths of other models vs Claude, and task routing

### Takeaway
Keep Claude (Max) as the hub for Korean copy, reasoning, CRM summarization and agentic work over MCP. Add **Gemini** as the second model, because it has the cheapest image generation (Nano Banana), Veo video and video/YouTube understanding, and it fits Google Workspace. GPT, Perplexity and HyperCLOVA X are optional or situational, not core.

### Cited Findings
- Gemini API official pricing (updated 2026-10-09):
  - **Text:** Gemini 3.8/3.6 Flash costs $0.75 input and $3.75 output per 1M tokens, rising to $1.50/$7.50 on 2027-01-01. Gemini 3.1 Pro Preview costs $2.00/$12.00 for prompts of 200k tokens or less. Flash-Lite variants cost $0.10–0.30 input.
  - **Images:** Nano Banana 2.1 costs about $0.034 for a 1K image and $0.05 for 2K. Nano Banana Pro (Gemini 3 Pro Image) costs about $0.134 for 1K/2K. The original Nano Banana (2.5 Flash Image) is deprecated, with shutdown on 2026-10-02.
  - **Veo 3.1 (per second, with audio):** Standard is $0.40 at 1080p, Fast is $0.12 at 1080p, and Lite is $0.05 at 720p or $0.08 at 1080p. The free tier does not include Veo.
  - Source: [Google AI Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- OpenAI **[unverified]**: aggregators list GPT-5.5 at $5 input and $30 output per 1M tokens (as of 2026-08-25), with cached input at $0.50. GPT-5.5 Pro is listed at either $30/$180 or $60/$480; the sources conflict. — [anotherwrapper](https://anotherwrapper.com/llm-pricing/gpt-5.5); [morphllm](https://morphllm.com/openai-api-pricing)
- An April 2026 snapshot of OpenAI pricing lists GPT-5.4 at $2.50/$15, GPT-5.2 at $1.75/$14 and GPT-5.1 at $1.25/$10. OpenAI reportedly has no plans to deprecate GPT-5.1, GPT-5 or GPT-4.1. — [BenchLM](https://benchlm.ai/blog/posts/openai-api-pricing)
- OpenAI image models are listed as "gpt-image-1.5 / GPT-5 Image" at $5 input and $10 output per 1M tokens, token-based **[unverified]**. — [modelcompare.dev](https://modelcompare.dev/pricing/openai-api-pricing)
- Sora 2 API pricing **[unverified]**: standard is $0.10/s at 720p; Pro is $0.30–0.70/s. One source reports that OpenAI scheduled removal of the Sora 2 API and its snapshots for 2026-09-24 with no successor. Its live status as of October 2026 is unconfirmed. — [benchlm](https://benchlm.ai/media-pricing/sora); [apiframe](https://apiframe.ai/blog/ai-video-api-pricing-2026); [cometapi](https://www.cometapi.com/ai-video-api-pricing/)
- Perplexity **[unverified]**:
  - Sonar costs $1/$1 per 1M tokens and Sonar Pro costs $3/$15, plus a fee of $5–14 per 1,000 requests.
  - Sonar Chat Completions support reportedly ended 2026-09-27, and new builds are pointed to the Agent API, which charges per tool invocation.
  - Sources: [flexprice](https://flexprice.io/pricing-index/perplexity-sonar-api); [puter](https://developer.puter.com/tutorials/perplexity-api-pricing/)
- HyperCLOVA X:
  - HCX-007 is a hybrid reasoning model with text-only input, served through CLOVA Studio (Naver Cloud).
  - Function calling is unavailable while reasoning is on.
  - Billing uses its own tokenization. I did not find a 2026 per-token price.
  - Source: [ncloud CLOVA Studio model guide](https://guide.ncloud-docs.com/docs/clovastudio-model)

### Inferences
- Suggested routing for this business:
  - **Korean ad copy, blog posts, scripts, consultation summaries and quote explanations:** Claude, as the primary model, since it is already paid for under Max.
  - **Thumbnails and card-news images:** Gemini Nano Banana 2.1 or Pro. It is cheapest per image and strong at Korean text-in-image (the Korean text-in-image quality is from practitioner reputation, not verified).
  - **Short video b-roll:** Veo 3.1 Fast or Lite. An 8-second 1080p Fast clip costs about $0.96 (about 1,350 KRW).
  - **YouTube or competitor video analysis:** Gemini, because it accepts video input natively.
  - **Web research:** Claude's own web search is likely enough. Perplexity is only for heavy citation-style research.
- GPT is mainly a backup or second opinion, for example A/B variants of copy or gpt-image for specific styles. It is not essential.
- HyperCLOVA X has a weak cost-benefit case for a solo operator. Claude and Gemini Korean quality is adequate, and the Naver-ecosystem advantage comes through the Naver *APIs* (search ads, DataLab), not through the LLM.
- Avoid building on the Sora API because of the reported deprecation.

### Gaps
- I could not read OpenAI's official pricing page (403). The GPT-5.5 figures are aggregator-only.
- HyperCLOVA X per-token pricing for 2026 was not found.
- I found no independent 2026 benchmark comparing Korean copywriting quality across Claude, GPT, Gemini and HCX.

## Q2. Short-form video, image and voice tools (cost and licensing)

### Takeaway
A workable low-cost production line is: Claude script → Vrew or CapCut edit → Typecast or ElevenLabs Korean voice → Nano Banana thumbnails → occasional Veo or Kling b-roll. AI avatars carry a mandatory "가상인물" label in endorsement-style ads since the June 2026 KFTC guideline revision.

### Cited Findings
- **Vrew:**
  - Switched to unified credits on 2026-04-22. — [Vrew notice](https://docs.channel.io/vrew-kr/ko/articles/%EA%B3%B5%EC%A7%80-2026422-%ED%86%B5%ED%95%A9-%ED%81%AC%EB%A0%88%EB%94%A7-%EB%B0%A9%EC%8B%9D%EC%9C%BC%EB%A1%9C-%EB%B3%80%EA%B2%BD%EB%90%A9%EB%8B%88%EB%8B%A4-58dfc5fd)
  - Prices were raised in late November 2025. — [Vrew notice](https://docs.channel.io/vrew-kr/ko/articles/%EA%B3%B5%EC%A7%80-2025%EB%85%84-11%EC%9B%94-%EB%A7%90-%EB%B8%8C%EB%A3%A8-%EC%9A%94%EA%B8%88%EC%9D%B4-%EC%9D%B8%EC%83%81%EB%90%A9%EB%8B%88%EB%8B%A4-1126-%EB%B0%98%EC%98%81-%EC%99%84%EB%A3%8C-22808225)
  - Japan annual prices are listed as Light ¥15,200, Standard ¥23,900 and Business ¥43,000 per year, with 2,000, 10,000 and 12,000 credits per month. The KRW price was not found **[unverified]**. — [atsoho](https://atsoho.com/apps/p/vrew)
- **Typecast:** the Basic Studio plan costs $5/month for 30,000 credits and includes a commercial license. SSFM 3.0 adds automatic Korean emotional expression **[unverified]**. — [toolquestor](https://toolquestor.com/vs/elevenlabs-vs-typecast); [typecast.ai](https://typecast.ai/kr/learn/best-ai-voice-tools-2026/)
- **ElevenLabs:** commercial use requires at least the Starter plan, about $5–6/month. Plans go up to $990/month, and prices changed during 2026 **[unverified]**. — [smallest.ai](https://smallest.ai/blog/elevenlabs-pricing-plans-cost-what-you-get-in-2026); [happyrobot](https://www.happyrobot.ai/hub/elevenlabs-pricing)
- **Kling AI** (international site) **[unverified]**:
  - The free tier is watermarked and excludes commercial rights.
  - Standard costs about $10/month for 660 credits and is the cheapest commercial tier. Pro costs $37 for 3,000 credits.
  - Video 3.0 costs about 6–8 credits per second at 720p–1080p without audio.
  - Sources: [eesel](https://eesel.ai/blog/kling-ai-pricing); [diyai](https://diyai.io/ai-tools/video-generation/kling-ai-pricing/)
- **Runway:** reportedly retired its Unlimited plan in June 2026 in favor of Max at $95/month for 9,500 credits **[unverified]**. — [costbench](https://www.costbench.com/compare/runway-vs-kling/)
- **Veo 3.1 API prices:** see Q1. — [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)
- **AI labeling rules:**
  - **AI기본법 제31조** requires AI providers to notify users that AI is used and to label generated output. It took effect 2026-01-22, with a grace period of at least one year. The maximum fine is 30M KRW. It applies to *AI business operators*, so it does not automatically require every advertiser to label every AI ad. — [i-boss](https://www.i-boss.co.kr/ab-74668-5969); [digitalmarketer](https://www.digitalmarketer.co.kr/insights/ai-ad-labeling-korea-guide)
  - **KFTC 추천·보증 심사지침**, revised June 2026: when an AI virtual person recommends or endorses a product, the ad must say so.
    - Text posts: the title or opening line must say, for example, "AI를 기반으로 생성된 가상인물이 포함된 게시물입니다".
    - Images and video: a "가상인물" label must stay near the person while they appear on screen.
    - Violations are treated as unfair advertising under 표시광고법.
    - Sources: [ddaily 2026-04-08](https://www.ddaily.co.kr/page/view/2026040811563569528); [kmong guide](https://kmong.com/support/expert-center/posts/799)

### Inferences
- For a rental agency, a HeyGen-style AI avatar "상담사" that recommends deals clearly falls under the 가상인물 label rule. Burn the label into the video template, for example a Vrew or CapCut overlay.
- Sources say less about AI-generated car b-roll without people, but Meta and YouTube platform AI-disclosure toggles still apply. Labeling by default is the safer choice.
- AI-generated car imagery should not misrepresent the actual trim, color or options being offered. This is an inference from 표시광고법 principles; no specific citation found.
- Typecast or 클로바더빙 likely beat ElevenLabs for natural Korean narration, though this is reputational and unverified. ElevenLabs is better if voice cloning or multilingual output is needed.

### Gaps
- HeyGen 2026 pricing and terms were not found.
- CapCut commercial-use and licensing status in Korea for 2026 was not found.
- Canva, Midjourney and Ideogram 2026 prices were not checked within the research budget.
- 클로바더빙 pricing was not found.
- Vrew KRW pricing was not found.

## Q3. Orchestration: n8n vs Make vs Zapier (lead intake → 알림톡 → CRM/Sheets → Claude)

### Takeaway
n8n is the best fit: either Cloud Starter (about €20–24/month) or self-hosted Community Edition (free, plus a server). It handles webhook → Google Sheets → Solapi 알림톡 → LLM API calls in one workflow, and Claude can drive it over n8n's MCP server. Messaging cost is trivial, at about 13 KRW per 알림톡.

### Cited Findings
- **n8n Cloud** **[unverified; check n8n.io/pricing]**:
  - Starter: 2,500 executions per month, about €20 (annual) or €24 (monthly), 5 concurrent executions, reportedly 5 active workflows.
  - Pro: 10,000 executions per month, €50–60.
  - Community Edition: free with unlimited executions.
  - Sources: [jetadmin 2026-09-26](https://www.jetadmin.io/blog/n8n-pricing/); [toolradar](https://toolradar.com/blog/n8n-pricing-2026)
- **n8n MCP:**
  - The instance-level MCP (Settings → Instance-level MCP, owner/admin only) lets Claude discover and trigger workflows. One guide says it can also create and test workflows since April 2026 (single source). Version 2.18.4 or later is recommended.
  - The MCP Server Trigger node exposes a single workflow. The MCP Client node lets n8n call external MCP servers.
  - Sources: [uibakery](https://uibakery.io/blog/n8n-mcp-guide); [agence-scroll](https://agence-scroll.com/en/blog/mcp-n8n-connect-claude-to-your-workflows-and-go-into-production-without-surprises)
- **Solapi 알림톡:**
  - 13 KRW per message (VAT excluded) for 1–9,999 messages per month, with volume discounts above that.
  - 친구톡 ended 2025-12-31. Promotional messages now go out as 브랜드 메시지.
  - Other vendors charge 5–15 KRW.
  - Sources: [Solapi pricing](https://solapi.com/guides/pricing); [bizgo](https://blog.bizgo.io/inside/alimtalk-price-by-volume/)
- **Kakao 알림톡 policy from 2026-01-01:**
  - Coupon, point and mileage messages are restricted to transaction or contract-based information.
  - Promotional content must be sent as a brand message.
  - Consultation confirmations are not addressed in this notice.
  - Source: [Channel Talk notice](https://docs.channel.io/updates/ko/articles/%EA%B3%B5%EC%A7%80-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%95%8C%EB%A6%BC%ED%86%A1-%EB%B0%9C%EC%86%A1-%EA%B0%80%EB%8A%A5-%EA%B8%B0%EC%A4%80-%EB%B3%80%EA%B2%BD-%EC%95%88%EB%82%B42611-%EC%8B%9C%ED%96%89-f9f70118)

### Inferences
- **Reference flow:**
  1. A Meta Lead Ads, landing-page form or Naver form webhook triggers n8n.
  2. n8n normalizes the phone number, checks for duplicates and appends a row to Google Sheets.
  3. A Solapi node or HTTP call sends a "상담 접수 확인" 알림톡 template.
  4. n8n calls the Claude API (or Gemini Flash-Lite, which is cheaper) with **masked PII** to classify the lead, for example by vehicle, budget or urgency, and draft a first reply.
  5. A Slack or Kakao "나와의 채팅" notification goes to the operator.
- Calling multiple AI APIs in one workflow is native in n8n: use separate credential nodes for Anthropic, OpenAI and Gemini, or HTTP Request nodes. Route by task inside the workflow, for example with Switch nodes.
- At solo volume (say 300 leads per month at about 5 executions each, so about 1,500), Cloud Starter fits. Self-hosting on a small VPS (roughly 5,000–10,000 KRW/month, unverified) removes execution caps, but the operator then owns updates, backups and security for a server that holds customer PII.
- Make and Zapier usually cost more per operation for multi-step AI flows, but I gathered no 2026 pricing within budget.
- A Claude API key is separate from Claude Max. API usage is billed separately (inference from Anthropic's product structure; I did not verify current API rates here).

### Gaps
- Make and Zapier 2026 pricing was not collected.
- Whether a "상담 신청 접수 확인" message qualifies as 알림톡 under current Kakao template review is assumed (it is a common practice) but was not verified against Kakao's guideline text.

## Q4. MCP servers (2026): availability, maturity, security

### Takeaway
Official or first-party MCP servers exist for Gmail, Drive and Calendar (Google), Notion, Slack, n8n (built in), Google Ads (read-only) and Kakao PlayMCP. Sheets, Meta Ads, Instagram, YouTube and Naver mostly rely on community servers. Treat those as higher risk: limit OAuth scopes and avoid servers that hold ad-account write tokens without review.

### Cited Findings
- **Google Workspace:**
  - Google's May 2026 announcement lists official MCP servers for Gmail (draft, search, read/write), Drive (fetch, permissions, list, upload), Calendar, Chat and People.
  - It also introduces a tiering model for agent tool access.
  - No official Sheets MCP was listed.
  - Source: [Google Workspace Updates 2026-05](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html)
- **Community Google Workspace MCP:** taylorwilsdon/google_workspace_mcp is the most-starred. It covers Sheets with OAuth 2.1 and scoping, and its latest release is reportedly v1.22.0 (2026-06-22). — [glama](https://glama.ai/mcp/servers/@taylorwilsdon/google_workspace_mcp/blob/2b72c4508f822df31097000bff23bbbc4275478d/README.md)
- **Google Ads:** the official Google Ads API MCP server was open-sourced in late 2025 and is read-only (account discovery and GAQL). — [ppc.io](https://ppc.io/blog/ads-mcp-google-vs-meta); [adspirer](https://www.adspirer.com/blog/why-not-google-free-mcp-server)
- **Meta Ads:**
  - Sources conflict on whether Meta has an official read/write MCP.
  - Community or commercial servers (Pipeboard, GoMarble) are what people commonly install.
  - The sources are vendor blogs with commercial bias.
  - Sources: [syntermedia](https://syntermedia.ai/blog/best-ad-platform-mcp-servers); [adspirer](https://www.adspirer.com/blog/best-ad-mcp-servers-2026)
- **Kakao PlayMCP:**
  - Opened in beta in August 2025.
  - Includes Kakao services (카카오톡 나와의 채팅방, 톡캘린더, 카카오맵, 선물하기, 멜론) and about 200 external servers as of May 2026.
  - Added OpenClaw integration with 10-minute one-time tokens.
  - Sources: [byline](https://byline.network/2025/08/13_kakao-2/); [Kakao 2026-05](https://www.kakaocorp.com/page/detail/12012?lang=KOR)
- **Naver:** a community Claude Code skill for Naver ad performance exists (vibehackers). I found no official Naver MCP. — [vibehackers](https://vibehackers.io/claude-code/skills/naver-ad-performance)
- **n8n MCP:** see Q3.

### Inferences
- Practical MCP set for Claude Max:
  - Google Drive and Gmail (official).
  - Notion or Google Sheets for the CRM. For Sheets, use the community server or route writes through n8n.
  - The n8n MCP, as the "action layer" that hides credentials from Claude.
  - Google Ads (official read-only) if Google Ads is used.
  - Kakao PlayMCP's 나와의 채팅 for notifications.
- **Security pattern:** let Claude call n8n workflows that hold the Meta, Naver and Solapi API keys, instead of installing many community MCPs that each hold tokens. Restrict write actions such as budget changes and message sends to human-approved workflows.
- Notion and Slack official MCPs are widely known to exist (Notion's MCP is connected in this environment), but I did not separately verify their 2026 status.

### Gaps
- I found no evidence of an official Instagram, YouTube or Naver 검색광고/DataLab MCP; community implementations probably exist but were not verified.
- No verified official status for a Meta Ads MCP.

## Q5. APIs and legal automated posting

### Takeaway
Instagram Reels auto-publishing is officially allowed through the Graph API, for Business accounts with app review, up to 100 posts per 24 hours. YouTube uploads are allowed but stay private until the API project passes an audit. Naver's search-ad and DataLab APIs are for analytics and keywords, not content posting. 알림톡 sending is legal through official dealers (Solapi and others) within Kakao's template rules.

### Cited Findings
- **Instagram:**
  - API publishing is capped at 100 posts per rolling 24 hours, and carousels count as one post. Check the live cap with `GET /<IG_ID>/content_publishing_limit`.
  - Reels publishing needs an Instagram Business account (Creator accounts are not supported) and app review for `instagram_business_content_publish`.
  - Sources disagree on Reels duration (90 seconds vs 15 minutes).
  - Sources: [Meta docs](https://developers.facebook.com/documentation/instagram-platform/content-publishing); [postproxy](https://postproxy.dev/blog/instagram-reels-api-publishing-guide/); [bundle.social 2026-08](https://bundle.social/blog/instagram-api-rate-limits)
- **YouTube Data API:**
  - Projects created after 2020-07-28 that have not passed the compliance audit have every upload forced to private. The audit takes about 2–4 weeks.
  - Quota figures conflict: a dedicated 100 uploads per day bucket since June 2026, versus 1,600 units per upload against a 10,000-unit default.
  - Sources: [postproxy](https://postproxy.dev/blog/youtube-upload-api-guide/); [singhamandeep](https://singhamandeep.com/?p=1570)
- **Naver 검색광고 API:**
  - `/keywordstool` returns monthly search volume, competition and related keywords.
  - No published call-limit figure was found. Users have asked about missing detail data.
  - Sources: [GitHub naver/searchad-apidoc issue](https://github.com/naver/searchad-apidoc/issues/1060); [ampm](https://inside.ampm.co.kr/insight/637)
- **Naver DataLab:**
  - Legacy developer-center keys allow 1,000 calls per day.
  - New keys are issued through NAVER API HUB from 2026-07-31, with a monthly quota of 50,000 for search trends.
  - Legacy keys work until 2027-06-30.
  - Source: [digitalmarketer](https://www.digitalmarketer.co.kr/insights/naver-datalab-api-data-for-non-developers); see also [ncloud API HUB](https://guide.ncloud-docs.com/docs/apihub-overview)
- **Kakao messaging:** see Q3. Solapi charges 13 KRW per 알림톡, and promotions go out as 브랜드 메시지. — [Solapi](https://solapi.com/guides/pricing)

### Inferences
- **Legal automated posting:** Instagram (Business account, app review) and YouTube (after the audit, or use a scheduler such as Buffer or Metricool that already holds approved apps) are allowed.
- **Naver Blog has no official posting API** (inference from the absence of any found evidence). Automating blog posting through browser bots risks violating Naver's terms, so keep blog posts AI-drafted and human-posted.
- For a solo operator, using an approved third-party scheduler is often faster than getting your own Meta and YouTube app reviews.
- The Meta Marketing API (Lead Ads retrieval and reporting) is the standard way to pull leads into n8n. n8n has a Facebook Lead Ads trigger node (from general knowledge; not re-verified here).

### Gaps
- Naver 검색광고 API rate limits were not found.
- Meta Marketing API access tiers for small advertisers in 2026 were not verified.
- Kakao 브랜드 메시지 pricing was not collected.

## Q6. Recommended stack tiers and routing table

### Takeaway
- **Minimal tier:** about 350,000–420,000 KRW/month on top of the ad budget, mostly the Claude Max subscription.
- **Standard tier:** about 500,000–650,000 KRW/month.
- Usage-based API costs (Gemini images and Veo) stay in the tens of thousands of KRW at solo volumes.
- All totals are estimates built from the unverified prices above.

### Cited Findings (price inputs)
- Gemini, Nano Banana and Veo: [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing).
- n8n: [jetadmin](https://www.jetadmin.io/blog/n8n-pricing/).
- Solapi: [Solapi](https://solapi.com/guides/pricing).
- Typecast: [toolquestor](https://toolquestor.com/vs/elevenlabs-vs-typecast).
- Kling: [eesel](https://eesel.ai/blog/kling-ai-pricing).
- Vrew: [atsoho](https://atsoho.com/apps/p/vrew).
- Claude Max costs $100 or $200 per month; this is from general knowledge and was not re-verified in this research **[unverified]**.

### Inferences
**Minimal tier (monthly, estimated):**

| Item | Est. cost |
|---|---|
| Claude Max 5x ($100) | ~140,000 KRW |
| n8n Cloud Starter (€20–24) | ~33,000–38,000 KRW |
| Gemini API (≈300 Nano Banana 2.1 images ≈ $10–15; Flash classification minimal) | ~15,000–20,000 KRW |
| Solapi 알림톡 (500 msgs × 13 KRW + VAT) | ~7,000 KRW |
| Vrew Light/Standard (KRW unverified) | ~15,000–25,000 KRW |
| Typecast Basic ($5) | ~7,000 KRW |
| Google Workspace / Sheets (existing or free) | 0–10,000 KRW |
| **Total** | **≈220,000–250,000 KRW**, or ≈360,000–390,000 KRW with Max 20x ($200) |

**Standard tier adds:**
- Kling Standard or Pro: about 14,000–52,000 KRW.
- Veo 3.1 Fast b-roll budget: about 20 clips × 8 s × $0.12 ≈ $19 ≈ 27,000 KRW.
- Canva Pro (price not verified).
- n8n Pro (about 80,000 KRW) or a self-hosted VPS.
- A social scheduler (price not verified).
- Optional ChatGPT Plus or Perplexity Pro for second opinions (about 28,000 KRW each, unverified).
- **Estimated total:** about 450,000–650,000 KRW.

**Routing table (task → tool → human check):**

| Task | Primary tool | Secondary | Human check |
|---|---|---|---|
| Korean ad copy, hooks and blog drafts | Claude (Max) | GPT-5.x for A/B variants | Always: verify prices, conditions and 과장광고 terms (e.g., "최저가", "무심사") |
| Keyword and demand research | Naver 검색광고 API + DataLab, run by n8n → Claude analysis | Perplexity / Claude web search | Spot-check volumes |
| Competitor YouTube or Reels analysis | Gemini (video input) | — | Light |
| Thumbnails and card news | Nano Banana 2.1 / Pro (Gemini API or app) | gpt-image, Canva | Check car model and trim accuracy and Korean text typos |
| Short-form edit and subtitles | Vrew / CapCut | — | Full review before posting |
| B-roll video | Veo 3.1 Fast/Lite | Kling Standard | Check for distorted logos, wrong car shapes and brand trademark issues |
| Korean voiceover | Typecast / 클로바더빙 | ElevenLabs | Listen through |
| AI avatar spokesperson | HeyGen-type tool | — | **Mandatory "가상인물" label** (KFTC June 2026) |
| Lead intake → 알림톡 → Sheets | n8n + Solapi + Sheets | — | Monitor failures daily |
| Lead summary and scoring | Claude API via n8n (PII masked) | Gemini Flash-Lite for cheap classification | Operator reviews before calling |
| Quote and 견적 comparison explanations | Claude with a verified rate table supplied by the operator | — | **Always**: numbers must come from the lender or 캐피탈 quote, never AI-generated |
| Ad performance reports | Google Ads MCP (read-only), Meta via n8n/Marketing API → Claude | — | Weekly review; no auto budget changes |
| Posting | Meta Graph API / approved scheduler; YouTube after audit | — | Approve each post |

### Gaps
- Claude Max price was not re-verified for October 2026.
- No KRW prices were confirmed for Vrew, Canva or CapCut.

## Q7. Risks: privacy, cost sprawl, tool overload

### Takeaway
The biggest risk is customer PII (name, phone, income or credit-related info for 장기렌트 심사) moving across several AI vendors. Mask or tokenize PII in n8n before any LLM call, keep one system of record, and cap the stack at about five paid tools.

### Cited Findings
- Google is introducing tiered access controls for agent tools on Workspace data, which signals that vendors see agent data access as a security concern. — [Google Workspace Updates](https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html)
- Many ad-platform MCP comparisons come from vendors promoting their own servers, so neutrality is low. — [adspirer](https://www.adspirer.com/blog/best-ad-mcp-servers-2026); [syntermedia](https://syntermedia.ai/blog/synter-mcp-vs-google-ads-mcp-vs-meta-ads-mcp)
- Pricing volatility:
  - Gemini Flash prices double on 2027-01-01. — [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)
  - The Sora API and Perplexity Sonar chat endpoint were reportedly deprecated in September 2026, and Runway changed plans in June 2026. These are the deprecation and plan-change risks. — [apiframe](https://apiframe.ai/blog/ai-video-api-pricing-2026); [flexprice](https://flexprice.io/pricing-index/perplexity-sonar-api); [costbench](https://www.costbench.com/compare/runway-vs-kling/)
- The AI기본법 grace period of at least one year from 2026-01-22 means enforcement may tighten from 2027. — [i-boss](https://www.i-boss.co.kr/ab-74668-5969)

### Inferences
- **PII:**
  - Send only a lead ID, vehicle interest, budget band and a free-text need (with phone and name stripped) to LLMs.
  - Keep the phone number only in Sheets or the CRM and in Solapi.
  - Disclose overseas transfer to AI vendors in the 개인정보 처리방침 / 동의서 if any PII reaches US-based APIs. This is an inference from 개인정보보호법 cross-border transfer rules; not researched in depth here.
- **Cost sprawl:**
  - Prefer pay-per-use APIs (Gemini, Veo) over overlapping subscriptions (Runway, Kling, Midjourney and HeyGen all at once).
  - Set billing caps in Google Cloud and the other API consoles.
  - Review total spend monthly against the 1–3M KRW ad budget. AI tools should stay under about 20–30% of the ad spend.
- **Tool overload:**
  - One hub (Claude), one automation layer (n8n), one data store (Sheets or Notion), one image/video vendor (Google), and one editor (Vrew or CapCut).
  - Add tools only when a specific bottleneck appears.
  - Deprecations (Sora, Sonar) show why building on many niche APIs is fragile for a solo operator.

### Gaps
- No specific Korean regulatory guidance (PIPC) on sending lead PII to LLM APIs was researched.
- No data on what time a solo operator actually spends maintaining multi-tool stacks.
