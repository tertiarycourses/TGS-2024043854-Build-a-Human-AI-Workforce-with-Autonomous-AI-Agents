# Lab 10 — Govern, Measure & Improve Your Human–AI Workforce

**Day 2 · Topic 3 · 35 min · Workforce governance · LO3**

> Read the costs and the audit trail, score every agent, pause or re-budget one, fix the instructions that caused rework, and present a Board report on what the AI workforce delivered.

## Goal
Evaluate and improve an AI-agent workforce with metrics, audit evidence and governance controls, and recommend improvements to stakeholders (LO3).

## The business scenario
One month in, the owners ask the Board three questions: what did the AI workforce deliver, what did it cost, and is it safe? You use Paperclip's dashboard, Audit (Activity, Runs, Costs, Budgets) and your scorecard to answer — and you act: pause or re-budget the agent in the red, improve the instructions that caused rework, and decide what humans keep doing.

## You will deliver
- scorecard — per-agent output, quality, cost vs budget with a RAG status
- One agent paused or re-budgeted, with the reason in a comment
- Improved instructions for the agent with the most revisions and audit findings — the Copywriter in the mock data (a new Revision you can restore)
- board-report — value, cost, risk, human role, next-quarter decisions — approved by you

## Who does what
- **Agents:** Whole company (CEO + 5 specialists)
- **You (the human):** Evaluate, intervene, improve, report — and stay accountable

## Before you start
- Labs 6–9 complete (live data), plus agent-scorecard.csv for a month of mock history

## Concepts in action
- Evaluate on utility, quality, cost and safety
- Budget controls: 80% warning, 100% auto-pause
- Audit trail = accountability evidence (IMDA agentic AI framework)
- Improve the harness (instructions, gates), not just the model

## Lab files (`data/`)

| File | What it is |
|---|---|
| `agent-scorecard.csv` | Month-1 agent scorecard (mock) |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-10-Instructions.pdf`](LAB-10-Instructions.pdf).

## Steps

### 1. Read the money
Dashboard → Month Spend card; then Audit → Costs and Audit → Budgets. Which agents passed the 80% warning? Is any auto-paused at 100%? Compare with agent-scorecard.csv (a month of mock history) and your live numbers from Labs 6–9.

```bash
npx paperclipai cost summary -C <company-id>
npx paperclipai cost by-agent -C <company-id>
npx paperclipai budget overview -C <company-id>
```

### 2. Read the audit trail
Audit → Activity. Find one hire approval, one Request revision, one task send-back, one Board Approval decision and one budget event. This trail is your evidence of human accountability — the core of Singapore's Model AI Governance Framework for Agentic AI.

### 3. Build the scorecard with the CEO
**Prompt** — paste into *Paperclip → New Task (assign to Ava; Approvers → Assign to me)*:

```text
Monthly agent scorecard.
Using Paperclip's costs and activity data plus agent-scorecard.csv, produce a scorecard with one row per agent: tasks done, Board send-backs, audit findings, spend vs budget, cost per completed task, and a RAG status (green/amber/red) with a one-line reason. Show your calculations.
```

✅ **Expected:** A scorecard you can spot-check against Audit → Costs.

### 4. Intervene
Take the red agent (in the mock data: Video Producer — over budget, 2 revisions). As the Board either Pause it (agent header) or raise/lower its budget, and record why in a comment. Pause is reversible; Terminate is permanent.

```bash
npx paperclipai agent pause <video-producer-id>
# or re-budget (cents):
npx paperclipai budget agent:update <video-producer-id> --payload-json '{"budgetMonthlyCents":800}'
```

### 5. Improve the harness, not the blame
The agent that causes the most rework is the Copywriter (4 audit findings, 3 Board revisions in the mock data). Fix the instructions that let those mistakes through. (For the Video Producer you already acted on cost in the previous step.)

**Prompt** — paste into *Paperclip → Agents → Copywriter → Instructions (AGENTS.md)*:

```text
Add to your rules:
- Before submitting any caption, run the kopi-brand-voice self-check and fix every FAIL; attach the table to the task.
- Never write health or halal claims (C1, C4). Any post with SHIOK20 must show its exact terms (C3).
- If the same rule fails twice on one task, stop and ask the Content Strategist instead of resubmitting.
```

✅ **Expected:** Saved as a new Revision (Governance → Revisions → Restore is your undo). Resume the Video Producer if you paused it.

### 6. Write the Board report
**Prompt** — paste into *Paperclip → New Task (assign to Ava; Approvers → Assign to me)*:

```text
Board report - month 1 of the AI growth studio.
Write a one-page report for Kopi Kaki's owners: (1) value delivered vs the three goals, (2) total cost and cost per deliverable, (3) quality and safety - send-backs, audit findings, escalations, (4) what humans still do and why, (5) three decisions for next quarter.
```

✅ **Expected:** A one-page report waiting for your approval — approve it with a comment.

### 7. Wrap up the class company (optional)
Stop scheduled work so nothing runs after class. To restart later, open each routine (Work → Routines) and switch its automation back on.

```bash
npx paperclipai routines disable-all -C <company-id>
```

## Verification / checkpoint
- [ ] Scorecard values match Audit → Costs for ≥ 2 agents
- [ ] A pause or budget change with a written reason
- [ ] New Revision of the Copywriter's instructions
- [ ] Board report approved by you with a comment

**Checkpoint:** Scorecard numbers match Audit → Costs for at least two agents; one intervention and one instruction change are logged with reasons.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Costs show zero | Subscription-based adapters may report little or no billed cost — use the mock scorecard for the analysis. |
| Paused agent still running | A run in progress finishes; no new work starts until you Resume. |
| Budget-paused agent resumed by itself | Budgets reset on the 1st of the month (UTC) — pause manually to keep it stopped. |

## Stretch challenge
Decide the autonomy level (L1 Operator → L5 Observer) for each agent next quarter and justify it in one line each.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
