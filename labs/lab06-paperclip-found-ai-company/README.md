# Lab 6 — Found Kopi Kaki Growth Studio — an AI Company You Govern

**Day 2 · Topic 3 · 45 min · Human-governed company of agents · LO2**

> Self-host Paperclip, become the Board, set the goals and hard budgets, switch on the hiring gate and make your first agent the CEO.

## Goal
Design a governed multi-agent platform — adapters, goals, budgets and approval gates — and explain how these design choices drive efficiency and control (LO2).

## The business scenario
Day 1 proved agents can do the marketing work. Kopi Kaki's owners now want it to run every week as a small 'AI growth studio' — with an org chart, budgets and an audit trail they can trust. You set up Paperclip, where you are the Board and every agent reports, ultimately, to you.

## You will deliver
- Paperclip running at http://localhost:3100
- Organization 'Kopi Kaki Growth Studio' with 3 company-level goals
- Ava — your first agent — set as CEO on an adapter you have (Claude Code, Codex, Gemini CLI or Hermes) and passing 'Run test'
- 'Require board approval for new hires' switched ON
- Company budget USD 60/month and CEO budget USD 15/month, visible under Audit → Budgets

## Who does what
- **Agents:** 1 CEO agent (Ava)
- **You (the human):** You are the Board: goals, budgets, the hiring gate

## Before you start
- Node.js 24.11+ (or Docker Desktop)
- One agent CLI signed in on this laptop: Claude Code, Codex, Gemini CLI, or Hermes Agent from Day 1
- This lab's data/ copied into ~/kopi-kaki

## Concepts in action
- Paperclip = the company; agents = employees; you = the Board
- Goal → project → task: every task traces to a company goal
- Adapters: bring your own agent runtime (Claude Code, Codex, Gemini, Hermes …)
- Budgets warn at 80% and auto-pause at 100%

## Lab files (`data/`)

| File | What it is |
|---|---|
| `paperclip-company-setup.md` | Values for the Paperclip company set-up |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-06-Instructions.pdf`](LAB-06-Instructions.pdf).

## Steps

### 1. Check the prerequisites
Paperclip needs Node.js 24.11 or newer, run as your normal user (never sudo). Its agents run on an agent CLI that is already signed in on this machine — Claude Code, Codex, Gemini CLI, or the Hermes Agent you installed on Day 1. Copy this lab's data into your workspace.

```bash
node --version          # v24.11.0 or higher
claude --version        # or: codex --version / gemini --version / hermes --version
cp -Rn data/* ~/kopi-kaki/
```

✅ **Expected:** Node ≥ 24.11 and at least one agent CLI.

### 2. Install and start Paperclip
Option A (recommended): the one-line onboarder — local, trusted, no login. Option B: Docker Desktop (Windows: enable WSL2 first with `wsl --install`); the compose file needs two secrets, and you will create an account and 'Claim this instance' on first visit. Leave the terminal running. Later restarts: `npx paperclipai run`.

```bash
# Option A
npx paperclipai onboard --yes

# Option B (Docker)
git clone https://github.com/paperclipai/paperclip.git && cd paperclip
export BETTER_AUTH_SECRET="$(openssl rand -hex 32)"
export PAPERCLIP_TOOL_ACTION_SIGNING_SECRET="$(openssl rand -hex 32)"
export ANTHROPIC_API_KEY="sk-ant-..."     # and/or OPENAI_API_KEY
docker compose -f docker/docker-compose.quickstart.yml up --build
```

✅ **Expected:** 'Server running at http://localhost:3100' — open it in your browser.

### 3. Create the organization and your first agent
The onboarding wizard asks 'What is the name of your organization?' → Kopi Kaki Growth Studio → Continue. 'Create your first agent' → name it Ava. 'Connect a model' → sign in or paste a key (a typed key is stored as a secret) → finish. On the first task's card 'What would you like to do?' (a question card in the 'Paperclip onboarding' task) choose 'I have a task in mind' but DO NOT confirm any team yet — the hiring gate comes first. It is fine to leave that onboarding task waiting.

### 4. Make Ava the CEO and test her adapter
The wizard files the first agent with a general role, and the UI has no Role field — so set it with the CLI. Then open Agents → Ava → Harness / Runtime: check the adapter (claude_local, codex_local, gemini_local or hermes_local) and model, click 'Test your agent' → Run test.

```bash
npx paperclipai company list                 # copy the company id
npx paperclipai agent list -C <company-id>    # copy Ava's agent id
npx paperclipai agent update <ava-id> --payload-json '{"role":"ceo","title":"CEO"}'
```

✅ **Expected:** `agent list` shows Ava with role ceo, and Run test says 'Connection successful'.

### 5. Give Ava her mandate
Open Agents → Ava → Instructions → AGENTS.md. The wizard seeded a 'chief of staff' persona there — REPLACE it with this CEO mandate (changes apply on her next run). Also upload brand-guide.md, campaign-brief.md and compliance-rules.md from ~/kopi-kaki with the + (Add agent file) button.

**Prompt** — paste into *Paperclip → Agents → Ava → Instructions → AGENTS.md*:

```text
You are Ava, CEO of Kopi Kaki Growth Studio, a small AI marketing studio serving Kopi Kaki Co. (a Singapore kopi chain).
Goals: (1) 2,500 app pre-orders for the Gula Melaka Cold Brew by 30 Nov 2026, (2) one approved short video every week, (3) monthly AI spend under USD 60 with zero compliance breaches.
How you work:
- Break goals into projects and tasks; propose hires with a mandate, adapter, reporting line and monthly budget; never hire without Board approval.
- Every public-facing item must pass the Compliance Auditor and then wait for the Board. Never publish anything yourself.
- Before anything is published or any spend outside budget, file a Board approval request.
- Use brand-guide.md, campaign-brief.md and compliance-rules.md as the source of truth.
- Report weekly: goal status, spend vs budget, risks, decisions needed.
```

✅ **Expected:** Ava's Instructions show the mandate and the three files.

### 6. Switch on the hiring gate
Avatar menu (bottom-left) → Settings → General → Hiring → turn ON 'Require board approval for new hires'. It is OFF by default — without it, the CEO's hires would join immediately.

### 7. Set the goals
Goals are hidden from the sidebar by default: open http://localhost:3100/<PREFIX>/goals (PREFIX is the short code in your URL) → Add Goal, level 'company', one per goal in paperclip-company-setup.md.

### 8. Set hard budgets (CLI — the UI cannot create the first cap)
Budgets are in cents per month. Then check Audit → Budgets: 80% sends a warning; 100% pauses the agent automatically.

```bash
npx paperclipai budget company:update -C <company-id> --payload-json '{"budgetMonthlyCents":6000}'
npx paperclipai budget agent:update <ava-id> --payload-json '{"budgetMonthlyCents":1500}'
npx paperclipai budget overview -C <company-id>
```

✅ **Expected:** Organization USD 60 and Ava USD 15 under Audit → Budgets.

### 9. Confirm the structure
Agents → Org chart view (icon next to New Agent): Board (you) → Ava (CEO). Write down which decisions the system has now reserved for you.

## Verification / checkpoint
- [ ] http://localhost:3100 loads Kopi Kaki Growth Studio
- [ ] Ava's role is CEO and her Run test passes
- [ ] 'Require board approval for new hires' is ON
- [ ] 3 company goals; budgets visible under Audit → Budgets

**Checkpoint:** Agents → Org chart view shows Ava (CEO) under the Board; Audit → Budgets shows both caps; the hiring gate is ON.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `node` too old | Install Node.js 24.11+ (e.g. from nodejs.org or `nvm install 24`). |
| Docker: 'BETTER_AUTH_SECRET must be set' | Export both secrets (or put them in docker/.env) before `docker compose up`. |
| Port 3100 busy | Paperclip falls back to another port — read the URL it prints. |
| Run test fails | Sign in to the CLI first (e.g. `claude`, `codex login`, `hermes setup`) on the same machine, or paste an API key. |
| Goals page not in the sidebar | Open /<PREFIX>/goals directly, or Settings → Experimental → Goals Sidebar Link. |

## Stretch challenge
Compare your Paperclip company with the Hermes studio from Lab 4: which governance features (org chart, budgets, hiring gate, audit log) would you have had to build yourself in Hermes?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
