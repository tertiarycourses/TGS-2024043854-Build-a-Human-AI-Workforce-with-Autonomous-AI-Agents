# Lab 1 — Activity 1 — Hermes Desktop, Telegram & the Launch Brief

**Day 1 · Topic 2 · 75 min · Single agent · LO1**

> Onboard one office assistant, verify a real Telegram connection and create the evidence brief used by the rest of the course.

## Goal
Configure one agent, inspect its tools and memory, analyse source data and test human control (LO1; PP Q1 preparation).

## The business scenario
You are Kopi Kaki Co.'s Marketing Lead. The Gula Melaka Cold Brew launches on 1 Dec and you have 60 unread customer reviews, a competitor list and no analyst. You 'hire' Mia — a Hermes Agent marketing analyst — onboard her with the company context, and ask for a research brief that tells you which campaign angle to run.

## You will deliver
- outputs/lab01/review-insights.md — ratings, themes and evidence (review IDs)
- outputs/lab01/research-brief.md — trends, competitors, 3 campaign angles with evidence
- Mia's long-term memory holds the brand facts and YOUR chosen angle (recalled in a new session)
- outputs/lab01/telegram-check.md — bot round-trip and local file evidence, without credentials
- ONE readable screenshot of your own Telegram request and substantive Hermes reply — PP Task 1; hide private identifiers and credentials

## Who does what
- **Agents:** 1 Hermes agent — 'Mia', AI marketing analyst
- **You (the human):** Set the goal, challenge the evidence, choose the campaign angle

## Before you start
- Download the official Hermes Desktop installer for your OS: https://hermes-agent.nousresearch.com/desktop
- Trainer-approved model access; use the same local Hermes profile for Desktop and Telegram
- Course ZIP downloaded and unzipped; no credentials in the shared course folder

## Concepts in action
- Perception (files + web) → Brain (LLM reasoning, memory) → Action (write files)
- AGENTS.md = context the agent loads automatically (context engineering)
- Short-term memory (this session) vs long-term memory (MEMORY.md, recalled next session)
- Human-in-the-loop: the agent recommends, the human decides

## Lab files (`data/`)

| File | What it is |
|---|---|
| `AGENTS.md` | Company context Hermes loads automatically |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `customer-reviews.csv` | 60 synthetic customer reviews |
| `competitors.csv` | 6 fictional competitors |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |
| `campaign-data.xlsx` |  |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-01-Instructions.pdf`](LAB-01-Instructions.pdf).

## Steps

### 1. Download and install Hermes Desktop (preferred)
Open https://hermes-agent.nousresearch.com/desktop in your browser. On macOS choose the Mac download and open the DMG, then install and launch Hermes. On Windows choose the Windows download, run Hermes-Setup.exe and launch Hermes. Follow normal OS installation prompts. Linux learners use the official terminal installation route linked on the page. Record the app/backend version shown by the installed app; do not install a second CLI checkout unless the trainer identifies a real need.

✅ **Expected:** The native Hermes Desktop app opens on the learner computer. The selected connection/profile is local and its version is recorded.

### 2. Connect a model in the desktop app
Use the Desktop provider/account configuration and the trainer-approved provider to complete sign-in. Choose the model provided for class and send a short test message. Verify a real model response and inspect visible tool activity. A free app download does not guarantee free model/API usage.

✅ **Expected:** The selected local profile gives a real model-backed reply; credentials stay in the app's configuration.

### 3. Open the launch workspace in Desktop
Create the kopi-kaki workspace in your own user folder and copy the lab data into it. Preserve any existing AGENTS.md. Use the Desktop file browser/workspace context or explicitly give the full folder path in chat, then ask Hermes to list the approved files before analysing them. On Windows stay in the native Desktop runtime; WSL has a different filesystem, PATH and credential store unless explicitly connected.

**Prompt** — paste into *Hermes Desktop chat*:

```text
Work in my kopi-kaki workspace at <replace with its full local path>. List campaign-brief.md, brand-guide.md and customer-reviews.csv. Confirm the workspace path and selected local profile before doing any analysis. Do not open or print credentials.
```

✅ **Expected:** The Desktop agent can actually read the three files in the intended local workspace.

### 4. Connect Telegram from Desktop (preferred QR route)
In Hermes Desktop open Messaging, select Telegram and use the Quick setup card's Create with QR. Scan the code or open its link in your own Telegram account. Review the detected numeric user ID/allowlist and selected local profile. Complete any Restart now banner and verify the gateway has restarted. If this option is unavailable on the installed version, the trainer uses the official BotFather plus hermes gateway setup fallback in the same local runtime. Never show a bot token in a screenshot.

✅ **Expected:** Messaging shows Telegram configured for the learner's own account and the local training profile, with no pending restart.

### 5. Run the gateway and prove a round trip
Use the already-running Desktop-managed gateway. Do not start another gateway process polling the same bot. In Telegram send /start, then send the prompt below using the full local workspace path. If the app reports a restart is needed, complete it first.

**Prompt** — paste into *Your private Telegram bot chat*:

```text
Use my ~/kopi-kaki workspace. Read campaign-brief.md. State the product name, approved price and launch date. Create outputs/lab01/telegram-check.md containing those three facts and the current timestamp. Do not send any email, create events or publish anything. Report the saved file path.
```

✅ **Expected:** A Telegram reply cites the correct product facts and the new local file exists. Check its timestamp locally. No token is visible in evidence.

### 6. Onboard Mia — persona and long-term memory
**Prompt** — paste into *Hermes Desktop chat in the launch workspace*:

```text
You are Mia, Kopi Kaki Co.'s AI marketing analyst. Read AGENTS.md, brand-guide.md and campaign-brief.md in this folder.

Save these facts to your long-term memory:
- Kopi Kaki Co.: Singapore kopi chain, 12 outlets, positioning "Heritage kopi, modern craft".
- Launch: Gula Melaka Cold Brew, SGD 6.80, launches 1 Dec 2026, campaign #ShiokColdBrew 17 Nov - 14 Dec.
- Promo SHIOK20: 20% off the first Gula Melaka Cold Brew ordered in the app, valid 1-14 Dec 2026, one per customer.
- Never publish anything without my APPROVE. Never make health or halal claims.

Then summarise the company in 5 bullets and ask me the 3 questions a new analyst should ask on day one.
```

✅ **Expected:** Mia confirms the memory was saved and returns 5 bullets + 3 questions. Inspect the selected local profile’s memory entry to verify only the approved facts were saved.

### 7. Perceive the data — analyse 60 customer reviews
**Prompt** — paste into *Hermes Desktop chat in the launch workspace*:

```text
Analyse customer-reviews.csv.
1. Rating distribution (count and % for 1-5 stars) and average rating per outlet.
2. The top 5 praise themes and top 5 complaint themes, each with a count and 2 example review_ids.
3. Anything relevant to a cold-brew launch (mentions of cold brew, sweetness, oat milk, app).
Show your calculation method. Save the result as outputs/lab01/review-insights.md.
```

✅ **Expected:** A Markdown report with a ratings table and themes that cite review IDs (e.g. R1012).

### 8. Perceive the world — live web research
**Prompt** — paste into *Hermes Desktop chat in the launch workspace*:

```text
Use web search to research specialty coffee and cold-brew trends in Singapore in 2026 (consumer preferences, price points, social media formats that work). Combine this with competitors.csv (the competitors are fictional - treat them as our internal notes).
Rules: cite every web fact with its URL; mark anything you could not verify as UNVERIFIED; do not invent statistics.
```

✅ **Expected:** 5+ cited findings with URLs and a competitor comparison table.

### 9. Act — write the research brief
**Prompt** — paste into *Hermes Desktop chat in the launch workspace*:

```text
Write outputs/lab01/research-brief.md for the Marketing Lead with:
1. Executive summary (5 lines).
2. What our customers say (from review-insights.md).
3. Market & competitor snapshot (cited).
4. Three campaign angles for #ShiokColdBrew. For each: the big idea, target audience, supporting evidence (review IDs or URLs), the KPI it drives, and one risk.
5. A final section "Decision needed" asking me to choose one angle.
Follow the brand guide and compliance rules.
```

✅ **Expected:** research-brief.md with three evidence-backed angles and a 'Decision needed' section.

### 10. Human checkpoint — challenge, then decide
Read the brief like a manager. Challenge at least one claim, then make the decision and tell Mia to remember it.

**Prompt** — paste into *Hermes Desktop chat in the launch workspace*:

```text
Which review_ids support angle 2? Quote them. Then: I choose angle <1|2|3> because <your reason>. Save my decision and reason to long-term memory, and add a "Decision log" section to research-brief.md.
```

✅ **Expected:** Mia quotes the supporting reviews, updates the brief and confirms the memory write.

### 11. Test long-term memory in a brand-new session
Inspect only the approved decision entry through the Desktop file browser or ask the agent to quote that entry without unrelated memory. Start a new Desktop chat using the same local profile and workspace, then ask the prompt below. Explain whether the answer came from persisted memory or source/session search.

**Prompt** — paste into *New Hermes Desktop chat, same local profile*:

```text
Which campaign angle did I choose, and why? What is the promo code and its terms? Tell me whether you got this from your memory file or by searching past sessions.
```

✅ **Expected:** Mia answers correctly without re-reading the files.

### 12. Capture the Telegram evidence
Open your private training bot chat and ask it to explain the approved launch angle using source review IDs. Include your request and its substantive reply in ONE readable screenshot for PP Task 1. Crop unrelated chats and private identifiers; never include a bot token. Keep telegram-check.md and the source brief as working evidence.

✅ **Expected:** Own Telegram request/reply is visible; this is the channel screenshot, not a Desktop-only frame.

## Verification / checkpoint
- [ ] Telegram private chat reaches your local Hermes gateway and creates telegram-check.md
- [ ] outputs/lab01/review-insights.md and research-brief.md exist and cite review IDs / URLs
- [ ] The brief ends with a decision log naming the angle you chose
- [ ] MEMORY.md contains the brand facts and your decision
- [ ] A new session recalls the chosen angle and the SHIOK20 terms
- [ ] PP Task 1: ONE own Telegram request and substantive Hermes reply screenshot; no tokens

**Checkpoint:** Every insight cites review IDs or a URL; the angle you chose is recalled in a brand-new session.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `hermes: command not found` | Open a new terminal or run `source ~/.zshrc` (macOS) / `source ~/.bashrc` (Linux/WSL2). |
| Model errors / context too small | Re-run `hermes setup` (or `hermes model`) and choose a model with ≥ 64k context. |
| Web search not available | Run `hermes tools` and enable the web toolset. Keyless search works for light use; for reliability add a free key, e.g. `hermes config set TAVILY_API_KEY tvly-...` (you reuse it on Day 2). |
| Windows paths | On native Windows Hermes keeps its data in %LOCALAPPDATA%\hermes instead of ~/.hermes — or run the labs inside WSL2. |
| Mia ignores the brand rules | Make sure you started `hermes` inside ~/kopi-kaki so AGENTS.md is loaded. |
| Bot is silent | Check allowed numeric ID, bot token entry, gateway status and network. Ensure no second gateway is polling this bot. |
| Telegram cannot find files | Use the full ~/kopi-kaki workspace path; gateway session directory can differ from the CLI session. |
| Desktop, CLI and Telegram see different files | Check selected connection/profile, workspace and runtime. Native Windows and WSL do not automatically share tokens, skills or paths. |

## Stretch challenge
Ask Mia: "Save the review-analysis procedure you just used as a reusable skill called review-insights." Then run `hermes skills list` — a self-improving agent turns experience into procedural memory.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
