# Implementation Patterns for Claude-Based Agent Teams (Solo Operators / Small Businesses), as of Oct 2026

Researcher notes. Research date: 2026-10-13. Sources are dated where possible. Many "2026 statistics" pages online are vendor or SEO content that cite each other. Those are flagged as such below.

## 1. Which workflows suit agents today, and how to pick one

### Takeaway
The workflows that suit agents are narrow, repeatable and reversible, and their output can be checked: research/summarization, drafting (content, email or customer replies), triage, report prep and coding. High-stakes, irreversible or ambiguous actions (paying, sending, publishing, long open-ended plans) work poorly unless a human approves them. Even Anthropic's SMB product keeps final send/post/pay steps behind human approval.

### Cited Findings
- **Anthropic's dividing line (Dec 19, 2024):** "Workflows" follow predefined code paths, while "agents" direct their own tool use. Anthropic advises starting with the simplest solution and adding agentic complexity only when it is justified, because agents trade latency and cost for performance. Agents fit open-ended problems where the number of steps can't be predicted, and only where you can trust the model's decisions. They "cost more and can compound errors." — [Anthropic, Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- **Where multi-agent setups pay off (June 13, 2025):** They work best for valuable, breadth-first tasks with heavy parallelization, information that exceeds one context window, and many tools (e.g., research). They are a poor fit for tasks where all agents need shared context or have many interdependencies, for most coding tasks, and for low-value tasks where the extra token cost isn't justified. — [Anthropic, How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- **Anthropic's own SMB workflow list (May 13, 2026):** Claude for Small Business ships 15 workflows and 15 skills across finance, ops, sales, marketing, HR and customer service. Examples: payroll planning, month-end close, a business "pulse" dashboard, campaign planning, invoice chasing, margin analysis, tax-season organizing, contract review, lead triage and content strategy. Connectors: PayPal, QuickBooks, HubSpot, Canva, Docusign, Google Workspace and Microsoft 365. — [Anthropic news](https://www.anthropic.com/news/claude-for-small-business); also [Axios, 2026-05-13](https://www.axios.com/2026/05/13/anthropic-claude-small-business-smb)
- **Practitioner view:** Agents work best on narrow, repeatable, reversible tasks such as inbox triage and lead enrichment. They fail on long multi-step planning, ambiguous goals, high-stakes actions without approval, and stale data feeding retrieval. This is a blog, not a study. — [Lilach Bullock, AI agents for small business: what they can and cannot do](https://www.lilachbullock.com/ai-agents-small-business-what-they-can-cannot-do/)
- **Low-risk targets named in an SMB guide:** drafting customer replies, summarizing long records, comparing documents and preparing CRM updates. Customer-facing or public actions should go through human approval. — [mo-cms.botica.it.com, Claude AI Agents for Business Operations](https://mo-cms.botica.it.com/blog/claude-ai-agents-for-business-operations) (secondary blog)
- **Bookkeeping caveat (vendor claim):** Claude Code or Desktop can query accounting data, categorise transactions and answer questions about the books only when connected to a real accounting backend via MCP. "On their own, they have no ledger, no bank feed, and no filing capability." — [AccountsOS blog](https://accounts-os.com/blog/bookkeeping-with-claude-code) (vendor)
- **Verification as the deciding criterion:** "Claude stops when the work looks done. Without a check it can run, 'looks done' is the only signal available, and you become the verification loop." Anthropic's guidance: "If you can't verify it, don't ship it." — [Claude Code docs, Best practices](https://code.claude.com/docs/en/best-practices)
- **Adoption data (SMB surveys, not agent-specific):**
  - Tech.co surveyed 300 US leaders at firms with fewer than 500 staff. 22% say AI saves them 6–10 hours a week, and 54% reported a productivity boost. — [IT Brief](https://itbrief.news/story/ai-saves-small-business-leaders-6-to-10-hours-a-week)
  - Bluehost surveyed 350 US small businesses in 2026. 78% save time weekly and 21% save 8+ hours, but only 16% have deployed an AI agent. — [Bluehost 2026 study](https://www.bluehost.com/state-of-small-business-ai-confidence)
- **Failure base rate (enterprise-focused):** Gartner (June 25, 2025) predicts that over 40% of agentic AI projects will be canceled by end-2027 due to escalating costs, unclear business value or inadequate risk controls. It warns of "agent washing" and estimates only about 130 of thousands of "agentic" vendors are genuine. The supporting poll covered 3,412 webinar attendees. — [Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)

### Inferences
- **Selection checklist for a solo operator:**
  1. The task repeats weekly or more.
  2. The output is a draft or file, not an external action.
  3. Mistakes are cheap and reversible.
  4. A pass/fail check or checklist exists.
  5. The inputs are mostly trusted (your own files) or the agent can't act after reading untrusted input.
  - Blog drafting, research briefs, meeting/report summaries and reply drafts meet all five.
  - Auto-sending email, payments, bookkeeping entries without a ledger backend, and auto-publishing fail one or more.
- Most SMB "time saved" comes from general chat-style AI use, not autonomous agents, according to the Bluehost data. Expectations for agent-specific savings should therefore be modest and measured per workflow.

### Gaps
- I found no rigorous 2026 study that measures agent success or failure rates by task type for small businesses. The evidence is anecdotal or vendor-sourced.
- An SBE Council 2026 figure (median 5 owner hours a week saved) is cited by blogs but could not be verified against the original.

## 2. Typical architectures and real "agent team" setups

### Takeaway
There are three practical tiers.
- **Claude Code / Cowork.** A single agent or orchestrator plus specialist subagents defined as Markdown files, with skills, hooks and MCP connectors. Best for file-based content and research work.
- **No-code orchestration (n8n, Make, Zapier) calling Claude.** Best for trigger-driven business workflows (email, form, CRM) with built-in approval steps.
- **Ready-made product layer.** Claude for Small Business inside Cowork.

Practitioners consistently report that splitting the work into researcher, writer and reviewer subagents with file handoffs beats one overloaded session.

### Cited Findings
- **Anthropic's composable patterns:**
  - Prompt chaining: sequential steps with programmatic checks between them.
  - Routing: send easy queries to a cheaper model.
  - Parallelization: sectioning or voting.
  - Orchestrator-workers: a lead model splits the task dynamically.
  - Evaluator-optimizer: a generate → critique loop, which works when clear criteria exist.
  - Anthropic also advises starting with direct API calls rather than frameworks, and treating tool design ("agent-computer interface") as seriously as prompts.
  - Source: [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- **Claude Code subagents: definition and scope.**
  - Subagents are Markdown files with YAML frontmatter. `.claude/agents/` is project scope (can be checked into git) and `~/.claude/agents/` is user scope.
  - Only `name` and `description` are required. Optional fields: `tools`, `disallowedTools`, `model` (sonnet/opus/haiku/inherit), `permissionMode`, `maxTurns`, `skills` (preload), `mcpServers`, `hooks`, `memory` (user/project/local) and `isolation: worktree`.
  - Each subagent runs in a fresh context and returns only a summary.
  - Defaults: nesting up to 3 levels and 20 concurrent subagents.
  - Source: [Claude Code docs, Subagents](https://code.claude.com/docs/en/sub-agents)
- **Subagent best practices from the docs:**
  - Write clear descriptions, because Claude delegates based on them.
  - Apply least privilege, e.g. read-only tools for reviewers.
  - Use subagents for high-volume output.
  - Chain subagents for multi-step flows.
  - Use `memory: project` for learning across sessions.
  - Use Stop/PreToolUse hooks for guardrails.
  - Source: [Subagents docs](https://code.claude.com/docs/en/sub-agents)
- **Extension mechanisms (Claude Code docs):**
  - CLAUDE.md holds persistent, short rules. Bloated files cause instructions to be ignored.
  - Skills (`.claude/skills/<name>/SKILL.md`) are loaded on demand. Use `disable-model-invocation: true` for side-effecting workflows you want to trigger manually.
  - Hooks are "deterministic and guarantee the action happens," unlike advisory CLAUDE.md instructions.
  - MCP is added via e.g. `claude mcp add --transport http notion https://mcp.notion.com/mcp`.
  - Plugins bundle skills, hooks, subagents and MCP.
  - Headless `claude -p` is for scripts and cron.
  - "Agent teams" (multi-session coordination) are listed as **experimental and disabled by default**.
  - Source: [Best practices](https://code.claude.com/docs/en/best-practices)
- **Writer/Reviewer pattern (official):** Run one session to write and another, with fresh context, to review. A fresh context "won't be biased toward code it just wrote." — [Best practices](https://code.claude.com/docs/en/best-practices)
- **Real setup 1 — GenAI Unplugged (Apr 17, 2026): 3-agent content team in Claude Code**
  - Researcher: WebSearch, WebFetch, Read, Glob, Grep, plus Perplexity and Firecrawl MCP; maxTurns 20; Sonnet.
  - Writer: Read, Write, Edit, Glob, Grep; no web tools; preloads an `seo-check` skill; reads brand-voice guide files; saves to `drafts/`.
  - Reviewer: read-only, with `disallowedTools: Write, Edit`.
  - All three use `memory: project` and Sonnet. Handoff is sequential via file paths. Independent research tasks run in parallel.
  - What worked: separate contexts, a read-only reviewer, and explicit checklists (forbidden-phrase lists, pass/fail criteria).
  - What failed: a reviewer with write access silently fixed issues, so the author never saw recurring problems. A vague "find problems" prompt produced 9/10 scores every time.
  - Model choice: Opus for the writer cost about 5x as much, was 2x slower, and gave only marginal quality gains.
  - Source: [GenAI Unplugged](https://genaiunplugged.substack.com/p/claude-code-agents-ai-research-team)
- **Real setup 2 — vegcale.com (Apr 25, 2026, Japanese): blog automation**
  - A `/generate-blog <topic>` orchestrator runs researcher (→ `drafts/work/research.md`), then writer (→ `draft.md`), then publisher (`scripts/wp-publish.sh` via the WordPress REST API, with an application password in `.env`).
  - Lessons:
    - Vague descriptions prevent auto-invocation.
    - Handoff paths must match between agents.
    - Separate agents reduce "context contamination."
    - Publishing as `status: draft` is recommended for safety.
  - Source: [vegcale.com](https://vegcale.com/2026/04/25/claude-code-subagent-blog-automation/)
- **Real setup 3 — GPTers (Korean community study, approx. 2025): Naver blog**
  - Revision: a `seo-reviewer.md` agent raised a test post's score from 45 to 85 to 98 and the author's own post from 62 to 92 (self-scored by the agent).
  - Auto-writing: five agents (Keyword-parser finds about 10 similar blogs, analyzer, morpheme strategy, blog-writer, orchestration). The auto-written post went from 75 to 99.
  - Naver publishing was manual: markdown → HTML → plain text via ChatGPT, then pasted.
  - Pain points: terminal and Claude Code installation was hard for non-developers, there was confusion between slash commands, agents and skills, and the result still needed manual touch-ups.
  - Source: [GPTers post](https://www.gpters.org/nocode/post/1-edit-naver-blog-lb1p2TAsVZHZwEK)
- **Six-agent SEO pipeline:** six agents plus an orchestrator, where each writes an output file the next one reads. — [thruuu blog](https://thruuu.com/blog/seo-content-agent-claude-code/) (search snippet only; not fetched in full)
- **Korean role-split example:** keyword-researcher → outline-planner → blog-writer → fact-checker → seo-editor, called in order by the main session. — [daleseo.com](https://daleseo.com/claude-code-sub-agents/) / [magicaiprompts](https://www.magicaiprompts.com/docs/claude/sub-agent/) (search snippets)
- **n8n + Claude pattern:**
  - Claude is the reasoning layer that decides which tools to call. Deterministic n8n nodes perform the actions.
  - The n8n AI Agent node can use remote MCP server tools.
  - A typical support-triage build posts a summary to Slack for human review before anything is sent.
  - Source: [aitraining2u tutorial](https://www.aitraining2u.com/blog/build-ai-agent-n8n-claude-tutorial.html) (secondary)
- **Claude for Small Business:** a toggle install inside Claude Cowork. Existing tool permissions carry over. — [Anthropic news](https://www.anthropic.com/news/claude-for-small-business)

### Inferences
- **For a semi-technical solo operator:**
  - Content and research work fits Claude Code or Cowork with 3–5 subagents and file handoffs.
  - Event-driven business ops (new email, form submission, invoice due) fit n8n/Make with Claude as one node plus an approval step, or Claude for Small Business if the tools match its connectors.
- **Recurring design rules across write-ups:**
  - One job per agent.
  - Least-privilege tools.
  - The reviewer is read-only and uses an explicit checklist.
  - Handoffs go through files in a shared `drafts/work/` folder.
  - Use Sonnet-class models by default and reserve Opus for orchestration or hard reasoning.

### Gaps
- No first-hand 2026 Hacker News or Simon Willison write-up on a non-coding "agent team" for small business was found within the search budget.
- No detailed Make or Zapier + Claude case study was retrieved.
- The Claude Agent SDK (programmatic agents) was not researched in depth. I have no sourced detail on it here.

## 3. Human-in-the-loop design, safety, logging, evaluation and cost controls

### Takeaway
Safety comes from three things: architecture (drafts not publish, least-privilege tools, never combining private data + untrusted input + outbound communication in one agent), deterministic gates (hooks, n8n human-review tools, permission modes) and evidence-based review. Prompt instructions alone are not a sufficient defense.

### Cited Findings
- **Lethal trifecta (Simon Willison, June 16, 2025):**
  - The risk arises when one agent has (1) private data, (2) exposure to untrusted content and (3) the ability to communicate externally. Together these allow data theft through prompt injection.
  - Mixing MCP tools from different sources can create the trifecta without you noticing.
  - Prompting the model to ignore injected instructions is unreliable. Guardrail products claiming "95%" are a failing grade.
  - Preferred designs: once an agent has read untrusted input, it should be structurally unable to take consequential actions (e.g., CaMeL).
  - Source: [Simon Willison](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- **Claude Code permission modes (2026):**
  - Modes: Manual (asks before writes, Bash and MCP), allowlists via `/permissions`, OS sandboxing via `/sandbox`, plan mode (read-only), `dontAsk` (denies anything not pre-approved, for unattended runs) and auto mode.
  - In auto mode a classifier model blocks scope escalation, unknown infrastructure and hostile-content-driven actions. Since v2.1.283 it is the default starting mode for interactive sessions.
  - Source: [Best practices](https://code.claude.com/docs/en/best-practices)
- **Hooks as hard gates:**
  - A PreToolUse hook can deny a tool call. For example, exit code 2 blocks an SQL UPDATE/DELETE.
  - A Stop hook can block a turn from ending until a check script passes.
  - Subagent-scoped hooks exist.
  - Sources: [Subagents docs](https://code.claude.com/docs/en/sub-agents); [Best practices](https://code.claude.com/docs/en/best-practices); [Claude Code hooks docs](https://docs.anthropic.com/en/docs/claude-code/hooks)
- **Recovery:** Checkpoints and `/rewind` restore files changed via Claude's edit tools. They don't cover Bash or external changes and are "not a replacement for git." — [Best practices](https://code.claude.com/docs/en/best-practices)
- **Adversarial review:**
  - Use a fresh-context reviewer subagent.
  - Ask it to "flag only gaps that affect correctness or the stated requirements," because reviewers told to find gaps will always report some.
  - Ask the working agent for evidence (command output, screenshots) rather than claims.
  - Source: [Best practices](https://code.claude.com/docs/en/best-practices)
- **n8n human-in-the-loop for tools (official docs):**
  - Tools attached to the AI Agent node's "Human review" step pause the workflow until a person approves or denies.
  - Channels: n8n chat, Slack, Discord, Telegram, Teams, Gmail, WhatsApp Business, Google Chat and Outlook.
  - Reviewers see the tool and its parameters via `$tool.name` / `$tool.parameters`. A denial cancels the action and the AI is told.
  - Source: [n8n docs](https://docs.n8n.io/advanced-ai/human-in-the-loop-tools)
- **Claude for Small Business approval model:** the user starts every task and approves before anything sends, posts or pays. The user can approve the plan up front or let a workflow run end to end. — [Anthropic news](https://www.anthropic.com/news/claude-for-small-business)
- **Evaluation:**
  - Start with about 20 real queries.
  - An LLM-as-judge with a single 0.0–1.0 score plus a pass/fail grade was most consistent with human judgment.
  - Human review still catches biases that evals miss.
  - Each subagent needs an objective, an output format, tool/source guidance and boundaries.
  - Source: [Anthropic multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system)
- **Cost controls:**
  - Multi-agent systems use about 15x the tokens of chat, and agents about 4x.
  - Use cheaper models via routing.
  - Use `maxTurns` limits per subagent.
  - Set `CLAUDE_CODE_SUBAGENT_MODEL` to force a cheaper subagent model.
  - Sources: [Anthropic multi-agent](https://www.anthropic.com/engineering/multi-agent-research-system); [Subagents docs](https://code.claude.com/docs/en/sub-agents); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- **Logging:** Subagent transcripts are stored separately. `claude -p --output-format json/stream-json` produces machine-parseable run logs. — [Subagents docs](https://code.claude.com/docs/en/sub-agents); [Best practices](https://code.claude.com/docs/en/best-practices)

### Inferences
- **Minimal safe blog setup:**
  - Researcher: web access but no write access outside `drafts/research/`, and no credentials.
  - Writer: no web access.
  - Reviewer: read-only.
  - Publisher: a separate, manually triggered skill (`disable-model-invocation: true`) that posts only as WordPress `status: draft`.
  - A PreToolUse hook restricts Write/Edit to `drafts/`.
  - Design inference. I found no published example of this exact hook, so it needs testing.
- **Email triage:** draft into a Gmail drafts folder or Slack approval. Never let the agent that reads inbound email also have outbound send rights without a human gate, because of the trifecta.

### Gaps
- No quantitative data on prompt-injection incident rates for SMB agent deployments was found.
- Details of Cowork's own permission and logging UI were not retrieved.

## 4. Concrete costs and time-to-build

### Takeaway
Subscription numbers are below. They come from claude.com/pricing as fetched 2026-10-13; check them, because the current model lineup differs from training data.
- Solo operators typically spend **$20/mo (Pro)** to **$100–200/mo (Max)**. Team Standard is $25/seat/mo.
- Per-article content pipeline costs reported by practitioners are under $2 on Sonnet-class models.
- n8n adds about $0–25/mo.
- Build time for a first working pipeline is reported in hours, not weeks. Non-developers report terminal setup as the main hurdle.

### Cited Findings
- **Claude plans (claude.com/pricing, fetched 2026-10-13):**
  - Free: no Claude Code or Cowork.
  - Pro: $20/mo or $17/mo annual; includes Claude Code.
  - Max: from $100/mo (5x or 20x Pro usage); reportedly includes $100 or $200/mo in API credits.
  - Team Standard: $25/seat monthly or $20 annual; includes Claude Code and Cowork; up to $500/mo pooled API credits.
  - Team Premium: $125/$100 per seat.
  - Usage limits reset on a rolling 5-hour window, with weekly limits on top. Overage can be billed at API rates.
  - Source: [Claude pricing](https://claude.com/pricing)
- **API prices per million tokens (input/output), same page:**

  | Model | Input | Output |
  |---|---|---|
  | Opus 5.5 | $4 | $20 |
  | Sonnet 5.5 | $2 | $10 |
  | Haiku 5.5 (≤100K prompt) | $0.10 | $0.50 |

  Batch processing is 50% off. Cache reads are about 5% of the input price. — [Claude pricing](https://claude.com/pricing)
- **Claude for Small Business:** no extra charge beyond Claude licenses and existing partner tools. — [Axios](https://www.axios.com/2026/05/13/anthropic-claude-small-business-smb)
- **Per-run costs (GenAI Unplugged, Sonnet, author estimates):**
  - Researcher $0.15–0.30, writer $0.20–0.40, reviewer $0.10–0.20, about $0.45–0.90 per pipeline run.
  - Time: about 15 minutes total (researcher 4–5, writer 6–8, reviewer 2–3) versus 2+ hours manually.
  - Parallel research cut about 12 minutes to about 5.
  - Source: [GenAI Unplugged](https://genaiunplugged.substack.com/p/claude-code-agents-ai-research-team)
- **Another pipeline write-up:** about $1.50 per article from research to publish (paid newsletter, unverified). — [GenAI Unplugged content system](https://genaiunplugged.substack.com/p/claude-code-content-system-full-ai-pipeline)
- **n8n (third-party summaries, mid/late 2026; sources disagree):**
  - Self-hosted Community Edition is free with unlimited executions; VPS costs about $4–7/mo.
  - Cloud Starter is about €20/mo annual (about €24 monthly) for 2,500 executions.
  - Pro is about €50/mo for 10,000 executions.
  - Figures on included AI credits conflict between sources.
  - Sources: [jetadmin, Sep 2026](https://www.jetadmin.io/blog/n8n-pricing/); [toolradar](https://toolradar.com/blog/n8n-pricing-2026)
- **Token multiplier warning:** multi-agent systems use about 15x the tokens of chat. — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- **Non-developer friction:** GPTers participants struggled with installation, the terminal and VS Code. Theanna's founder notes that most Claude Code tutorials "assume you know what a terminal is." — [GPTers](https://www.gpters.org/nocode/post/1-edit-naver-blog-lb1p2TAsVZHZwEK); [Theanna](https://theanna.io/building-theanna/how-to-set-up-claude-code-non-technical-founders)

### Inferences
- **Example solo budgets:**
  - Content creator: Claude Pro at $20 is likely enough for a few articles a week on Sonnet within subscription limits. Max at $100 suits daily pipelines or parallel subagents.
  - An API-only automation (n8n → Claude Sonnet) producing about 30 articles a month at about $1 each comes to roughly $30/mo plus n8n (€0–24).
  - Arithmetic from the cited per-run figures, not a measured case.
- **Build-time estimate:** First 3-agent pipeline is 1–3 hours for someone comfortable with a terminal, longer for non-developers. This is inferred from tutorial scope and reported friction, not measured.

### Gaps
- No independent, verified monthly-spend case studies for solo operators were found.
- How far subscription limits stretch for agent-heavy usage (e.g., runs per week on Pro) is not documented in sources I retrieved.

## 5. Example: AI-assisted blog content pipeline

### Takeaway
Proven blog pipelines share one shape: keyword/competitor research, then a research brief file, then an outline and draft using brand-voice files, then a read-only review or fact-check against a checklist. A human then reviews, and the post is saved as a draft (WordPress `status: draft`, or a manual paste for Naver) instead of being auto-published.

### Cited Findings
- **Stage → agent mapping from sources:**

  | Stage | Agents in sources |
  |---|---|
  | Keyword research | keyword-researcher / Keyword-parser (finds about 10 similar ranking blogs) |
  | Research | researcher (WebSearch/WebFetch, Perplexity/Firecrawl MCP, writes a brief with URLs); analyzer (success patterns) |
  | Draft | blog-writer / writer (brand voice guide + playbook files, no web) |
  | Fact-check/edit | fact-checker, seo-editor, read-only reviewer with forbidden-phrase list and pass/fail criteria; seo-reviewer scoring |
  | Publish | publisher via WordPress REST API with app password, recommended as draft; or MD → HTML conversion agent and manual Naver posting |

  Sources: [GenAI Unplugged](https://genaiunplugged.substack.com/p/claude-code-agents-ai-research-team); [vegcale](https://vegcale.com/2026/04/25/claude-code-subagent-blog-automation/); [GPTers](https://www.gpters.org/nocode/post/1-edit-naver-blog-lb1p2TAsVZHZwEK); [daleseo](https://daleseo.com/claude-code-sub-agents/)
- **Brand voice:** Defining your writing style in CLAUDE.md or a style file lets the agent write in your voice. — [brunch @parkkyunga](https://brunch.co.kr/@parkkyunga/137) (search snippet)
- **Notion as a storage/review surface:** connected via `claude mcp add --transport http notion https://mcp.notion.com/mcp`. — [Best practices](https://code.claude.com/docs/en/best-practices)
- **Caution on self-scoring:** GPTers' 45 → 98 and 62 → 92 scores came from the agent's own SEO rubric, not traffic outcomes. — [GPTers](https://www.gpters.org/nocode/post/1-edit-naver-blog-lb1p2TAsVZHZwEK)

### Inferences
- **Suggested concrete stack:**
  - `.claude/agents/{keyword-researcher, researcher, writer, fact-checker(read-only), seo-editor(read-only)}.md` and `.claude/skills/publish-draft/SKILL.md` (manual trigger).
  - `CLAUDE.md` holds voice and banned phrases.
  - Shared `drafts/work/` for handoffs.
  - Output saved to Notion, Google Docs or WordPress as a draft.
  - A human approves before the post goes public.
- **Fact-check design:** require the researcher to output claims with URLs, and have the fact-checker verify each draft claim against that brief. This follows the evidence-over-assertion guidance.
- **Korean bloggers on Naver Blog:** I didn't find a documented official write API for Naver in these sources, so "save draft + manual paste" is the realistic end step.

### Gaps
- No source measured SEO or traffic outcomes of agent-written posts.
- Naver Blog API publishing options were not verified.

## 6. Step-by-step adoption roadmap

### Takeaway
The sources converge on a sequence: start simple, with one workflow and one agent. Add a verification check, then measure time and quality on about 20 real cases. Split into subagents only when context overload or quality issues appear. Add automation (headless runs, n8n triggers) and connectors last, always keeping approval gates on external actions.

### Cited Findings
- **Start simple:** add complexity only when it's justified, and measure and iterate. — [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
- **Small evaluation samples:** start with about 20 real queries, because early changes have large effects. — [Anthropic multi-agent](https://www.anthropic.com/engineering/multi-agent-research-system)
- **Test small before scaling:** "Refine your prompt based on what goes wrong with the first 2–3 [items], then run on the full set," using `--allowedTools` and `dontAsk` for unattended runs. — [Best practices](https://code.claude.com/docs/en/best-practices)
- **Context discipline:** use `/clear` between tasks. After two failed corrections, restart with a better prompt. Prune CLAUDE.md regularly and convert repeated rules to hooks. — [Best practices](https://code.claude.com/docs/en/best-practices)
- **Iterate per agent:** check output quality and adjust each agent file's instructions based on the results. Use `memory: project` so agents accumulate lessons. — [GenAI Unplugged](https://genaiunplugged.substack.com/p/claude-code-agents-ai-research-team)
- **Why people split into agents:** one session overloaded with research, drafting and review ran out of context and lost track of the research by the quality-check stage. — [GenAI Unplugged content system](https://genaiunplugged.substack.com/p/claude-code-content-system-full-ai-pipeline) (search snippet)
- **Lower-friction on-ramp:** Claude for Small Business offers prebuilt workflows, plus a free training course with PayPal and a 10-city tour. — [Anthropic news](https://www.anthropic.com/news/claude-for-small-business); [tbreak](https://tbreak.com/claude-small-business-uae-smes/)

### Inferences
- **Suggested roadmap:**
  - **Week 0:** Log time spent on 3 candidate tasks and pick the one that best meets the checklist in section 1.
  - **Week 1:** Do the task with a single Claude session plus a written prompt or CLAUDE.md. Measure minutes saved and edits needed on 5–10 real runs.
  - **Week 2:** Turn the prompt into a skill and add a read-only reviewer subagent with an explicit checklist.
  - **Week 3–4:** Split into researcher, writer and reviewer subagents if context or quality problems appear. Add an MCP connector (Notion/Drive) for output storage, and add hooks for path restrictions.
  - **Month 2:** Schedule it (`claude -p`, cron or n8n trigger) with an approval step in Slack or email. Then expand to a second workflow only after the first shows sustained savings.
  - Track cost per run and the edit rate.

### Gaps
- No longitudinal case study of a solo operator's multi-month adoption with measured ROI was found.
