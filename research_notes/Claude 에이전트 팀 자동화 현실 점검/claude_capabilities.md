# Claude product capabilities for "AI agent teams" (multi-agent automation) — state as of October 2026

Research date: 2026-10-13. All sources fetched on that date unless noted. Several Anthropic pages are living docs with no publish date ("Updated this week"); dates are given where the page states them.

## 1. What Claude products are relevant to agent teams, what each does, and how they differ

### Takeaway
There are now four distinct layers: (a) **Claude Code** (CLI / Desktop / web) with subagents, an *experimental* "agent teams" mode, hooks, skills, plugins, headless `-p` mode and cloud sessions; (b) **Claude Agent SDK** (Python/TypeScript library = Claude Code's loop embedded in your own app, API-key billed); (c) **Claude Managed Agents** (Anthropic-hosted agent harness on the API, beta, with multiagent orchestration, scheduled deployments, vaults); (d) **Claude app / Cowork** (non-developer surface: tasks, connectors, skills, plugins, scheduled tasks, Claude in Chrome). Non-developers realistically use (d) and Routines; (b)/(c) require programming.

### Cited Findings

**Claude Code — agent teams (experimental)**
- Agent teams are "experimental and disabled by default"; enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings.json or environment. One session is the team lead; teammates are separate Claude Code instances with their own context windows, a shared task list, and a mailbox for direct teammate-to-teammate messaging — [Claude Code docs: agent teams](https://code.claude.com/docs/en/agent-teams)
- Spawning teammates "requires an interactive session"; in non-interactive `-p` mode, "including Agent SDK sessions, Claude doesn't spawn teammates" (named subagents run as ordinary subagents) — [agent teams](https://code.claude.com/docs/en/agent-teams)
- Subagents vs agent teams: subagents return results to the caller (lower token cost, "results summarized back to main context"); teammates are fully independent, self-coordinate via messages and shared task list (higher cost, "each teammate is a separate Claude instance") — [agent teams](https://code.claude.com/docs/en/agent-teams)
- Recommended size: "Start with 3-5 teammates for most workflows"; "5-6 tasks per teammate"; "Three focused teammates often outperform five scattered ones"; "Letting a team run unattended for too long increases the risk of wasted effort" — [agent teams](https://code.claude.com/docs/en/agent-teams)
- Documented limitations: no session resumption of in-process teammates (`/resume`, `/rewind` don't restore them); task status can lag and block dependent tasks; one team per session; no nested teams; lead fixed for lifetime; teammate permission prompts bubble up to lead; split panes need tmux or iTerm2 (not VS Code terminal, Windows Terminal, Ghostty) — [agent teams](https://code.claude.com/docs/en/agent-teams)
- Hooks for quality gates on teams: `TeammateIdle`, `TaskCreated`, `TaskCompleted` (exit code 2 blocks/feeds back) — [agent teams](https://code.claude.com/docs/en/agent-teams)
- Team state is local files: `~/.claude/teams/{team-name}/config.json`, tasks in `~/.claude/tasks/{team-name}/`, mailboxes as JSON files — [agent teams](https://code.claude.com/docs/en/agent-teams)
- Lighter alternatives named by the docs: subagents within one session, "cross-session messaging" between sessions you run, and git worktrees for manual parallel sessions — [agent teams](https://code.claude.com/docs/en/agent-teams)
- Claude Code also has "dynamic workflows" where agents spawned by a workflow each send their own requests — [Claude Code costs](https://code.claude.com/docs/en/costs); Anthropic blog on harness design: [A harness for every task: dynamic workflows in Claude Code](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code) (linked from Agent SDK docs; not fetched)

**Claude Agent SDK**
- "Build production AI agents with Claude Code as a library": same tools, agent loop and context management as Claude Code, in Python and TypeScript. Capabilities: built-in tools, hooks, subagents, MCP, permissions, sessions (resume/fork), skills/commands/memory, plugins — [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- Billing/auth: "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Use the API key authentication methods" — i.e., SDK products run on API-key (pay-per-token) billing — [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- Comparison table: Agent SDK = run the agent in a process you operate; Claude Code CLI = interactive terminal use; Client SDK = raw API, you write the loop; Managed Agents = Anthropic hosts the agent harness — [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- Governed by Anthropic Commercial Terms of Service — [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)

**Claude Managed Agents (API)**
- "Pre-built, configurable agent harness that runs in managed infrastructure. Best for long-running tasks and asynchronous work." Status: **beta**, requires header `managed-agents-2026-04-01`; enabled by default for all API accounts — [Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview)
- Concepts: Agent (model, system prompt, tools, MCP servers, skills), Environment (Anthropic cloud sandbox or self-hosted sandbox), Session, Events (SSE streaming; history persisted server-side). Built-in tools: Bash, file ops, web search/fetch, MCP — [overview](https://platform.claude.com/docs/en/managed-agents/overview)
- Not eligible for Zero Data Retention or HIPAA BAA coverage (stateful by design) — [overview](https://platform.claude.com/docs/en/managed-agents/overview)
- MCP tunnels and "dreaming" are in a more limited research preview requiring an access request — [overview](https://platform.claude.com/docs/en/managed-agents/overview)
- Multiagent orchestration (beta under same header): the session's agent can delegate to **subagents**, write **dynamic workflows** ("a program that runs many agents in phases and combines their results", run server-side in the background), or consult an **advisor** model. Up to 20 predefined agents per list; 25-child-thread limit referenced (advisor threads exempt); session budgets cap spend; docs warn "Keep runs to the tasks that need them, because every agent in a run uses tokens" — [Managed Agents multiagent orchestration](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)
- June 9, 2026: **scheduled deployments** (cron-scheduled agent runs, new session each fire, pause/resume/archive/on-demand) and **vaults** (credentials injected at network boundary for approved domains) launched in public beta — [Claude blog: What's new in Claude Managed Agents](https://claude.com/blog/whats-new-in-claude-managed-agents)
- Third-party report says multiagent orchestration, "outcomes" and "dreaming" were announced for Managed Agents (May 2026) — [SD Times](https://sdtimes.com/ai/new-in-claude-managed-agents-dreaming-outcomes-and-multiagent-orchestration/) (secondary source; official doc above confirms multiagent orchestration exists in beta)

**Claude app / Cowork (non-developer surface)**
- Pricing page: "Claude Cowork is now just Claude," rolling out to Pro and Max — [claude.com/pricing](https://claude.com/pricing); same wording on [support: Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- Cowork availability: desktop on paid plans; web and mobile on Pro and Max, Team in beta, Enterprise requires owner enablement; Team/Enterprise admins control access via a toggle — [support 13854387](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- Max plan support article: Cowork for "longer, multi-step tasks such as reports, spreadsheets, and presentations, which continue in the background" — [What is the Max plan](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)
- Team/Enterprise seat allowance is shared across Claude chat, Claude Code and Cowork — [Claude Code costs](https://code.claude.com/docs/en/costs)

**Claude in Chrome / computer use**
- Claude in Chrome listed for Pro, Max, Team, Enterprise (not Free) — [claude.com/pricing](https://claude.com/pricing)
- Support search results: Claude in Chrome on all paid plans; generally available in Cowork and Claude Code, beta in the Chrome browser side panel; on Max/Team the side panel runs as a Cowork session (rolling to Pro); Enterprise extension disabled by default, turning on by default from Sept 10, 2026 unless disabled — [support: Claude in Chrome](https://support.claude.com/en/articles/12012173-claude-in-chrome), [admin controls](https://support.claude.com/en/articles/13065128-claude-for-chrome-admin-controls) (obtained via search summaries, not full-page fetch)
- Claude Desktop also has a separate built-in browser pane, distinct from the user's own Chrome (no shared logins unless imported) — same search results (support article, summary only)

**Connectors (MCP) and Skills**
- Connectors and Skills are included on all plans including Free — [claude.com/pricing](https://claude.com/pricing)
- Connectors are claude.ai integrations managed at claude.ai/customize/connectors; routine connector traffic routes through Anthropic servers; examples named: Slack, Linear, Google Drive — [Routines docs](https://code.claude.com/docs/en/routines)
- Skills load on demand (vs CLAUDE.md always loaded) — [Claude Code costs](https://code.claude.com/docs/en/costs)

### Inferences
- For a non-developer, the "agent team" that is actually turnkey is Cowork/Claude app tasks + connectors + skills + scheduled tasks, plus Claude in Chrome. The literal "agent teams" feature is a developer-oriented, experimental, terminal feature that requires interactive supervision.
- Agent SDK and Managed Agents are the production routes for real multi-agent automation, but both are API-billed (per token) and require coding.

### Gaps
- I did not find an official, dated changelog entry for when Claude Code agent teams launched; only that it remains experimental.
- Full official Cowork product definition page (beyond the scheduled-tasks support article) was not fetched.
- Claude in Chrome details came from search-result summaries of support articles, not full fetches; GA vs beta status differs between official support (beta in Chrome side panel) and a third-party blog (GA since Aug 26, 2026).

## 2. Which features allow unattended / scheduled operation, and what are the constraints?

### Takeaway
Four real unattended options exist: **Claude Code Routines** (cloud, laptop can be off; min 1-hour interval; Pro/Max/Team/Enterprise; research preview), **Cowork scheduled tasks** (now mostly run remotely; paid plans), **Desktop local scheduled tasks** (machine must be awake and app open), and **Managed Agents scheduled deployments** (API, beta). `/loop` needs an open session. All subscription-based runs draw down the same 5-hour/weekly plan limits.

### Cited Findings
- **Routines**: "a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors", running on Anthropic-managed cloud "so they keep working when your laptop is closed". Triggers: Scheduled (hourly/daily/weekdays/weekly or one-off), API (HTTP POST with bearer token), GitHub (pull request / release events). Status: **research preview** — [Routines](https://code.claude.com/docs/en/routines)
- Routines availability: Pro, Max, Team, Enterprise; created at claude.ai/code/routines, Desktop app, or `/schedule` in CLI; requires claude.ai subscription login (not API key / Bedrock / Vertex / Foundry); Team/Enterprise owners can disable — [Routines](https://code.claude.com/docs/en/routines)
- Routines permissions: "run autonomously as full Claude Code cloud sessions: there is no permission-mode picker"; all connected connectors included by default and "Claude can use every tool from an included connector, including writes, without asking for permission during a run"; actions appear as the user (commits, Slack messages under the user's linked accounts) — [Routines](https://code.claude.com/docs/en/routines)
- Routines are tied to individual accounts: "not shared with teammates, and their runs count against your account's usage and limits" — [Routines](https://code.claude.com/docs/en/routines)
- Routine limits: minimum interval one hour; scheduled runs 100/hour per account; Run now + API fires 30/hour per routine; API fires 100/hour per account; GitHub events have per-routine/per-account hourly caps (excess dropped); "None of these hourly limits has overage" — [Routines](https://code.claude.com/docs/en/routines)
- Routines and usage: draw down subscription usage like interactive sessions; when hitting limit, runs rejected unless usage credits (metered overage) are on; paused subscription → routines on hold; GitHub disconnected >72 hours → routine turns off — [Routines](https://code.claude.com/docs/en/routines)
- Routines caveat: "A green status in the run list means the session started and exited without an infrastructure error. It does not mean the task in your prompt succeeded" — [Routines](https://code.claude.com/docs/en/routines)
- Default cloud network: "Trusted" allowlist only; other hosts fail with 403 unless environment network access is edited — [Routines](https://code.claude.com/docs/en/routines)
- **Desktop local scheduled tasks**: run on your machine with local file access; "only fires while the app is open and your computer is awake"; if asleep, run skipped; on wake, exactly one catch-up run for the most recent missed time within 7 days; min interval 1 minute; per-task permission mode, runs in Manual mode stall until approved — [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)
- Comparison table: Cloud (no machine needed, no local files, no permission prompts, min 1 hour) vs Desktop (machine on, local files, configurable prompts, min 1 min) vs `/loop` (requires open session, min 1 min) — [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)
- **Cowork scheduled tasks**: run saved prompt hourly/daily/weekly/weekdays/manual; "Most scheduled tasks run remotely, so they keep running when your computer is asleep or the Claude Desktop app is closed"; tasks needing local files/apps run only locally; Pro/Max tasks created before October 6 that run on your computer continue to run there; available on Pro, Max, Team, Enterprise — [support 13854387](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork). Note: older versions of this article said tasks ran only while the computer was awake and the app open — superseded (per search results of article variants).
- **Managed Agents scheduled deployments**: cron schedule, new session per fire, public beta since June 9, 2026 — [Claude blog](https://claude.com/blog/whats-new-in-claude-managed-agents)
- Background token drains: scheduled tasks fire even while the session is idle "sending your full context each time"; each active teammate "keeps consuming tokens until it exits" — [Claude Code costs](https://code.claude.com/docs/en/costs)
- Usage limits reset on a rolling five-hour window; paid plans add weekly limits — [claude.com/pricing](https://claude.com/pricing); Max weekly limit "applies across all models", and Anthropic "may also apply other caps" — [Max plan support](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)
- Claude Code v2.1.234+ can wait and auto-continue an interrupted task after a usage limit resets — [Claude Code costs](https://code.claude.com/docs/en/costs)

### Inferences
- "Runs while I sleep" is genuinely available on subscriptions via Routines and Cowork scheduled tasks, but each run is a fresh session (no persistent memory beyond what's in repo/files/connectors), the minimum cloud cadence is hourly, and plan limits — not hourly caps — are the practical constraint for a small business.
- Unattended runs act with the owner's identity and full connector write access with no approval step, so scoping connectors is the main safety control.

### Gaps
- No official numeric token/message quota per plan was found (Anthropic expresses limits as multiples: Pro ≥5x Free, Max 5x/20x Pro, Team Premium 5x Standard).
- No published cap on number of routines or Cowork scheduled tasks per account found.

## 3. Pricing: plans, usage limits, API token prices, typical multi-agent cost

### Takeaway
Pro $20/mo ($17/mo annual), Max 5x $100/mo, Max 20x $200/mo, Team Standard $25 ($20 annual)/seat, Team Premium $125 ($100 annual)/seat, Enterprise $20/seat + usage at API rates. API (per MTok input/output): Fable 5.1 $10/$50, Opus 5.5 $4/$20, Sonnet 5.5 $2/$10, Haiku 5.5 $0.10/$0.50 (≤100K prompt). Anthropic's own figures: multi-agent ≈15x chat tokens (2025 research post); Claude Code agent teams ≈7x a standard session in plan mode.

### Cited Findings
**Subscription plans** — [claude.com/pricing](https://claude.com/pricing)
- Free $0; Pro $17/mo annual ($200 up front) or $20 monthly, "at least 5x Free's usage per 5-hour session"; Max 5x from $100/mo (5x Pro per session); Max 20x (20x Pro per session); Team Standard $20/seat annual, $25 monthly; Team Premium $100/seat annual, $125 monthly, 5x Standard usage; Enterprise $20/seat/mo annual plus usage at API rates.
- Max 20x price: support article states **$200/month** (Max 5x $100/month; web, monthly only) — [Max plan support](https://support.claude.com/en/articles/11049741-what-is-the-max-plan). (The pricing-page fetch summary showed only "from $100" for Max; treat $200 for 20x as the confirmed figure.)
- Max plans include monthly API credits ($100 for 5x, $200 for 20x per pricing page summary); Team/Enterprise can get pooled API credits — [claude.com/pricing](https://claude.com/pricing) (from fetched summary; verify before quoting)
- Claude Code not on Free; included Pro and above — [claude.com/pricing](https://claude.com/pricing)
- Usage credits (metered overage beyond plan limits) can be turned on; Team/Enterprise admins set spend limits at org/group/member level — [Claude Code costs](https://code.claude.com/docs/en/costs)

**API token prices (USD per million tokens)** — [platform.claude.com pricing](https://platform.claude.com/docs/en/about-claude/pricing)
| Model | Input | 5m cache write | 1h cache write | Cache read | Output | Batch in/out |
|---|---|---|---|---|---|---|
| Claude Fable 5.1 | $10 | $12.50 | $20 | $0.25 | $50 | $5 / $25 |
| Claude Mythos 5.1 (limited availability) | $10 | $12.50 | $20 | $0.25 | $50 | $5 / $25 |
| Claude Opus 5.5 | $4 | $5 | $8 | $0.20 | $20 | $2 / $10 |
| Claude Opus 5 / 4.8 / 4.7 / 4.6 / 4.5 | $5 | $6.25 | $10 | $0.50 | $25 | $2.50 / $12.50 |
| Claude Sonnet 5.5 | $2 | $2.50 | $4 | $0.10 | $10 | $1 / $5 |
| Claude Sonnet 5 | $2 | $2.50 | $4 | $0.20 | $10 | $1 / $5 |
| Claude Sonnet 4.6 / 4.5 | $3 | $3.75 | $6 | $0.30 | $15 | $1.50 / $7.50 |
| Claude Haiku 5.5 (prompt ≤100K tokens) | $0.10 | $0.125 | $0.20 | $0.01 | $0.50 | $0.05 / $0.25 |
| Claude Haiku 5.5 (prompt >100K tokens) | $0.50 | $0.625 | $1 | $0.05 | $2.50 | $0.25 / $1.25 |
| Claude Haiku 4.5 | $1 | $1.25 | $2 | $0.10 | $5 | $0.50 / $2.50 |
- Sonnet 5 $2/$10 introductory price became standard; planned Sept 1, 2026 increase to $3/$15 "will not occur" — [pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- Claude 4.6+ models (except Haiku 5.5) include the full 1M token context at standard pricing — [pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- US-only inference (`inference_geo: "us"`) = 1.1x multiplier — [pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- Fast mode (research preview): Opus 5.5 $8/$40; Opus 5 / 4.8 $10/$50; first-party API only — [pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- Web search $10 per 1,000 searches; code execution free when used with web search/fetch, otherwise 1,550 free hours/month per org then $0.05/hour/container — [pricing](https://platform.claude.com/docs/en/about-claude/pricing) (pricing-page summary phrased it as "50 free hours daily" — roughly equivalent)
- **Managed Agents**: tokens at model rates plus **$0.08 per session-hour** of `running` status; replaces container-hour billing; web search $10/1,000 — [pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable models always use extended thinking (can't turn off); thinking tokens billed as output — [Claude Code costs](https://code.claude.com/docs/en/costs)
- Claude Mythos is "limited availability" — [pricing](https://platform.claude.com/docs/en/about-claude/pricing)

**Typical costs and multipliers (Anthropic figures)**
- Claude Code enterprise average: "around $13 per developer per active day and $150-250 per developer per month, with costs remaining below $30 per active day for 90% of users" — [Claude Code costs](https://code.claude.com/docs/en/costs)
- "Agent teams use approximately 7x more tokens than standard sessions when teammates run in plan mode" — [Claude Code costs](https://code.claude.com/docs/en/costs)
- Agent team cost advice: use Sonnet for teammates, keep teams small ("token usage is roughly proportional to team size"), shut down teammates when done — [Claude Code costs](https://code.claude.com/docs/en/costs)
- Research system (June 13, 2025, older/Claude 4 era): agents use ~4x chat tokens; multi-agent systems ~15x chat tokens — [Anthropic engineering: multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- Background usage under $0.04 per session — [Claude Code costs](https://code.claude.com/docs/en/costs)

### Inferences
- Illustrative arithmetic (not an Anthropic figure): a workflow consuming 2M input + 200K output tokens on Sonnet 5.5 costs ≈ $4 + $2 = $6 uncached; at 15x a single-agent run, multi-agent overhead dominates cost. For subscription users the cost shows up as faster exhaustion of 5-hour/weekly limits rather than dollars.
- Opus 5.5 is cheaper per token ($4/$20) than previous Opus generations ($5/$25; Opus 4.1 $15/$75), lowering the gap with Sonnet.

### Gaps
- No Anthropic-published per-workflow dollar estimate for Cowork or Routines.
- Exact Max monthly API credit amounts come from a summarized fetch of the pricing page; not cross-verified.
- The 15x figure is from 2025 (Claude Opus 4/Sonnet 4); no updated official multiplier for Claude 5-family found, other than the ~7x agent-team figure.

## 4. Anthropic's guidance on when multi-agent helps vs. hurts

### Takeaway
Anthropic consistently says: start with the simplest solution; multi-agent pays off for broad, parallelizable, high-value tasks (research, review, competing hypotheses) and hurts for tightly coupled, sequential, shared-context tasks (including most coding), due to ~4–15x token costs and coordination failures.

### Cited Findings
- "Building effective agents" (Dec 19, 2024; page notes tooling has changed since): "find the simplest solution possible, and only increasing complexity when needed"; workflows (predefined code paths) vs agents (LLM directs its own process); patterns: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer; agentic systems "often trade latency and cost for better task performance" with "potential for compounding errors"; three principles: simplicity, transparency (show planning), careful agent-computer interface/tool docs — [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- Multi-agent research system (June 13, 2025): Opus 4 lead + Sonnet 4 subagents outperformed single-agent Opus 4 by 90.2% on internal research eval; token usage explained 80% of BrowseComp performance variance (with tool calls and model choice, 95%) — [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- Not a good fit: value doesn't justify token cost; domains where all agents need same context or many inter-dependencies; "most coding tasks"; tasks requiring real-time coordination — [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- Observed failure modes: spawning 50 subagents for simple queries; endless searching for non-existent sources; subagents distracting each other with excessive updates; duplicated work from vague delegation — [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- Lessons: delegate in detail (objective, output format, tools, boundaries); scale effort to complexity (simple fact-finding = 1 agent, 3–10 tool calls); 3–5 parallel subagents cut research time up to 90%; start evals with ~20 queries; rewriting a flawed tool description cut task time 40% — [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- Claude Code docs (current): agent teams best for research/review, new modules, competing-hypothesis debugging, cross-layer work; "For sequential tasks, same-file edits, or work with many dependencies, a single session or subagents are more effective"; "For routine tasks, a single session is more cost-effective"; avoid file conflicts — [agent teams](https://code.claude.com/docs/en/agent-teams)
- Managed Agents docs link to a Claude blog "when to use multiagent systems (and when not to)" — [Managed Agents multiagent orchestration](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration) → [blog](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them) (not fetched)

### Inferences
- For a small business, the evidence favors a single well-instructed agent plus scheduled runs and connectors, using multi-agent only for genuinely parallel research/review work.

### Gaps
- The Claude blog "Building multi-agent systems: when and how to use them" was not fetched; its specific claims/date are not captured.

## 5. Korean-language support, availability in Korea, Korean-service connectors

### Takeaway
Korean is a supported UI language and performs near English; Anthropic opened a Seoul office June 17, 2026 with major Korean enterprise customers. No official Korean-service connectors (Kakao, Naver etc.) were found. An unverified press claim says US export controls restrict top models (Mythos/Fable) for some Korean institutions.

### Cited Findings
- Korean is listed among supported interface languages for Claude web and desktop apps — [support: using Claude in your preferred language](https://support.claude.com/en/articles/10769299-using-claude-in-your-preferred-language) (via search summary)
- Multilingual docs: Korean scores 96.7% on Claude Sonnet 4.5 and 93.3% on Claude Haiku 4.5 relative to English (older models; no Claude 5 figures captured) — [Multilingual support](https://platform.claude.com/docs/en/build-with-claude/multilingual-support) (via search summary)
- Seoul office opened June 17, 2026 (updated June 18); led by KiYoung Choi, Representative Director of Korea; MOU with Ministry of Science and ICT; Korean-language safety evaluation with the Korea AI Safety Institute — [Anthropic news](https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem)
- Korean customers: NAVER (Claude Code across engineering), LG CNS, Hanwha Solutions (via AWS Bedrock), Samsung SDS (to Samsung Electronics employees), Nexon, Law&Company, WRTN, Channel Corp (Channel Talk, 230,000+ companies); Korea is in the top dozen countries for Claude.ai use — [Anthropic news](https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem)
- Samsung SDS deploying Claude Cowork and Claude Code across Samsung Electronics — [Pulse 2.0](https://pulse2.com/anthropic-opens-seoul-office-and-announces-korean-ai-partnerships/) (secondary)
- The Anthropic announcement lists no Korean-service connectors/integrations — [Anthropic news](https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem)
- Unverified: outlets report US export controls bar some Korean institutions from Anthropic's most advanced models (described as Mythos 5 / Fable 5) — [Shopifreaks](https://www.shopifreaks.com/?p=19580), [Agenzia Nova](https://www.agenzianova.com/en/news/Anthropic-opens-office-in-Seoul-despite-US-restrictions-on/) (secondary; not confirmed by Anthropic)

### Inferences
- A Korean small business can use Claude in Korean; integrations with Korean services (KakaoTalk, Naver Works, Korean accounting/banking) would require custom MCP servers or browser automation (Claude in Chrome), not official connectors.

### Gaps
- No official list of connectors for Korean services found; the connector directory was not fetched.
- KRW pricing / local billing, VAT treatment in Korea not found.
- Whether Fable 5.1 is available to Korean individual subscribers is unconfirmed; only secondary reports about export restrictions exist.
