# Lab 5 — Multi-Agent Campaign Command Centre — Measure, Optimise & Report

**Day 2 · Topic 2 · 35 min · Multi-agent (parallel swarm) · LO2**

> Run three analysts in parallel, have a verifier check their numbers, and get a dashboard plus an optimisation plan you approve — then schedule it every Monday.

## Goal
Relate a parallel multi-agent design (workers + verifier + synthesiser) to speed, accuracy and cost, using metrics to verify the output and decide improvements (LO2).

## The business scenario
Week 1 of #ShiokColdBrew is over. Leadership wants to know: are we on track for 2,500 pre-orders, which posts work, what customers are saying and what competitors are doing? You launch a Kanban swarm — three parallel workers, a verifier that re-checks their numbers, and a synthesiser that builds the dashboard and recommendations. You decide which optimisations to apply.

## You will deliver
- outputs/lab05/dashboard.html — KPI cards + charts (opens in a browser)
- outputs/lab05/optimisation-plan.md — 3 proposals with evidence, impact, risk
- outputs/lab05/verification.md — the verifier's re-calculation of the key numbers
- Your decision recorded on the swarm task
- A Monday 09:00 cron that delivers the weekly report to Telegram

## Who does what
- **Agents:** 3 parallel workers + verifier + synthesiser (Kanban swarm)
- **You (the human):** Spot-check one number yourself; approve which optimisations to run

## Before you start
- Labs 3–4 complete: gateway running; researcher and auditor profiles exist
- A spreadsheet app to spot-check numbers

## Concepts in action
- Parallel (swarm) vs ordered (pipeline) multi-agent patterns
- Verifier agent + human spot-check = two layers of verification
- KPIs: engagement rate, CTR, cost per pre-order, sentiment
- Human-on-the-loop reporting with a weekly cron

## Lab files (`data/`)

| File | What it is |
|---|---|
| `AGENTS.md` | Company context Hermes loads automatically |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `campaign-week1-metrics.csv` | Week-1 post metrics (12 posts) |
| `sales-by-outlet.csv` | Weekly sales for 12 outlets |
| `social-comments.csv` | 20 social comments incl. complaints, legal, PII, spam |
| `competitors.csv` | 6 fictional competitors |
| `tasks/swarm-definition-of-done.md` | Task brief (used with --body-file) |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-05-Instructions.pdf`](LAB-05-Instructions.pdf).

## Steps

### 1. Add the analyst and strategist profiles
Reuse the researcher (competitor watch) and auditor (verifier) from Lab 4, and add two roles.

```bash
cp -Rn data/* ~/kopi-kaki/
mkdir -p ~/kopi-kaki/outputs/lab05
hermes profile create analyst --clone --description "Computes marketing KPIs from CSV data with exact formulas and shows its working"
hermes profile create strategist --clone --description "Synthesises analyses into an HTML dashboard and an evidence-based optimisation plan"
hermes profile create listener --clone --description "Analyses customer comments for sentiment, themes and risks; masks personal data"
```

### 2. Launch the swarm
A swarm creates parallel worker cards, then a verifier card, then a synthesiser card — all on the board, and workers start at once. So the definition of done goes INTO the goal and worker titles: every card points to ~/kopi-kaki/tasks/swarm-definition-of-done.md (formulas, output paths, charting rule). Note: the campaign data covers its first six days (17–22 Nov); the scenario is set in late Nov 2026, so web research must use the most recent real sources and label their dates.

```bash
hermes kanban swarm "Week-1 #ShiokColdBrew review and optimisation plan. FIRST read ~/kopi-kaki/tasks/swarm-definition-of-done.md; data in ~/kopi-kaki; write outputs to ~/kopi-kaki/outputs/lab05/" \
  --worker "analyst:KPIs vs targets from ~/kopi-kaki/campaign-week1-metrics.csv and sales-by-outlet.csv per the definition of done" \
  --worker "listener:Sentiment and risk review of ~/kopi-kaki/social-comments.csv per the definition of done" \
  --worker "researcher:Competitor and cold-brew trend watch from the most recent real sources, dated and cited, per the definition of done" \
  --verifier auditor --synthesizer strategist
hermes kanban list            # copy the swarm root id
```

✅ **Expected:** 3 worker cards running in parallel, then verifier, then synthesiser.

### 3. Open the dashboard and plan
Read the KPI cards (pre-orders vs 2,500, engagement vs 8%, video views vs 40,000, cost per pre-order), the top and bottom posts and the three proposals.

```bash
open ~/kopi-kaki/outputs/lab05/dashboard.html
```

✅ **Expected:** A self-contained HTML dashboard with charts and an optimisation plan.

### 4. Human verification — check one number yourself
Open campaign-week1-metrics.csv in a spreadsheet. Sum app_preorders and paid_spend_sgd, and compute cost per pre-order = spend ÷ pre-orders. Compare with the dashboard and with verification.md. If they differ, comment on the analyst task and ask for a correction — never forward a number you have not checked.

✅ **Expected:** Your figure matches (or you have sent a correction back).

### 5. Decide and record
**Prompt** — paste into *Hermes chat in ~/kopi-kaki*:

```text
I approve proposals <1 and 3> from outputs/lab05/optimisation-plan.md and reject proposal <2> because <reason>. Comment this decision on the swarm root card <swarm_root_id>, then update outputs/lab05/office-action-plan.csv for 24-30 Nov to apply the approved changes (status stays "proposed" so each action still requires my explicit review).
```

✅ **Expected:** Decision comment on the board and an updated office-action-plan.csv with action, owner, source evidence, due date and approval status.

### 6. Make it weekly
```bash
hermes cron create "0 9 * * 1" "Weekly #ShiokColdBrew report: recompute KPIs vs targets from the latest CSVs in ~/kopi-kaki, list the top and bottom 3 posts, summarise sentiment and escalations, and recommend max 3 changes. Do not change any plan without my approval." --name weekly-campaign-report --deliver telegram
hermes cron list              # copy the job id
hermes cron run <job_id>
```

✅ **Expected:** A weekly report arrives on Telegram.

## Verification / checkpoint
- [ ] dashboard.html opens and shows the four KPIs vs target
- [ ] verification.md re-computes at least pre-orders, spend, engagement rate and cost per pre-order
- [ ] Your manual check matches (data covers 17–22 Nov)
- [ ] weekly-campaign-report is listed in `hermes cron list`

**Checkpoint:** Your own calculation of pre-orders and cost per pre-order matches the dashboard; the plan you approved is recorded on the task.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Swarm workers can't find the CSVs | Say the absolute path (~/kopi-kaki/...) in the worker titles, or comment it on the root card. |
| Dashboard is blank | Ask the strategist for a single self-contained HTML file with inline SVG charts (no external scripts or data files). |
| Numbers disagree | That's why the verifier and you exist — request changes on the analyst card with the correct figure. |

## Stretch challenge
Feed the result back into Lab 3: ask Mia to add the approved changes to tomorrow's approval message, so the loop runs plan → publish → measure → improve without leaving Telegram.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
