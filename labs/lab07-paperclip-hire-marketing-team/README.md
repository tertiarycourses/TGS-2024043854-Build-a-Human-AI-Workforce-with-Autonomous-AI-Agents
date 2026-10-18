# Lab 7 — Hire the Marketing Team Through the Board Approval Gate

**Day 2 · Topic 3 · 45 min · Multi-agent organisation · LO3**

> Let the CEO design the team, then approve, push back on or reshape every hire — with budgets, a Tavily web-search secret, a shared brand skill and an independent auditor.

## Goal
Improve the effectiveness of an AI-agent workforce through organisation design — roles, reporting lines, budgets, tools (live search) and shared skills (LO3).

## The business scenario
Ava needs a team to hit the goals. In a real company you would never let a manager hire without approval, and you would never let the person who writes the ads also approve them. You ask Ava for a hiring plan, approve the hires that make sense, push back on one, give the researcher live web search, share the brand-voice skill, and make sure the Compliance Auditor reports to the CEO — not to the content team it audits.

## You will deliver
- A plan document from Ava (roles, mandates, adapters, budgets, reporting lines)
- 5 specialists hired through Approvals: Market Researcher, Content Strategist, Copywriter, Video Producer, Compliance Auditor
- At least one hire sent back with 'Request revision' and resubmitted
- Organization secret tavily_api_key bound to the researcher as TAVILY_API_KEY
- kopi-brand-voice skill in the company library, attached to the Copywriter and Auditor

## Who does what
- **Agents:** CEO + 5 specialist agents
- **You (the human):** Approve, revise or reject each hire; enforce separation of duties

## Before you start
- Lab 6 complete: Ava is CEO, the hiring gate is ON, budgets are set
- Your Tavily key from Day 1 (or a new free key from tavily.com)
- This lab's data/ copied into ~/kopi-kaki

## Concepts in action
- Role specialisation + reporting lines = coordination
- Separation of duties: the auditor must not report to those it audits
- Secrets: tools without exposing keys in prompts
- Per-agent budgets = cost control by design

## Lab files (`data/`)

| File | What it is |
|---|---|
| `paperclip-org-plan.md` | Reference hiring plan |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `skills/kopi-brand-voice/SKILL.md` | Agent skill (SKILL.md) |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-07-Instructions.pdf`](LAB-07-Instructions.pdf).

## Steps

### 1. Store the Tavily key as an organization secret
Reuse the Tavily key you used on Day 1 (or get a free one at tavily.com). Avatar menu → Settings → Secrets → New secret → Name tavily_api_key, paste the value in the Value field (stored once, never shown again) → create. Do not paste keys into a terminal, a prompt or a task.

### 2. Ask the CEO for a hiring plan
**Prompt** — paste into *Paperclip → New Task (assign to Ava)*:

```text
Propose the team to hit our three company goals.
Propose the smallest team that can research, plan, write, produce video and audit our marketing every week. For each role give: name, mandate (3 bullets), reports to, adapter, monthly budget in USD, tools and skills it needs.
Rules: the Compliance Auditor must not report to anyone whose work it audits; the total team budget must fit our USD 60/month company budget with Ava's USD 15 included.
Save it as a plan, ask me to confirm, then submit each hire for Board approval with its budget.
```

✅ **Expected:** A plan document and a confirmation card; after you confirm, hire requests appear in Approvals.

### 3. Review the plan against a reference
Compare Ava's plan with paperclip-org-plan.md. A good plan has clear mandates, budgets that add up, and an independent auditor. Note one thing Ava did better than the reference and one thing to change. Then click Confirm on the plan's confirmation card (a checkbox card in the task thread).

### 4. Approve — and push back once
Dashboard → Pending Approvals (or /<PREFIX>/approvals) → each 'Hire Agent' card → View details → See full request (budget, reports to, adapter). Approve the hires that fit. For one, click Request revision and explain in Comments — e.g. 'Video Producer budget too high: cap at USD 10 and render drafts first'. CLI fallback:

```bash
npx paperclipai approval list -C <company-id> --status pending
npx paperclipai approval approve <approval-id> --decision-note "Approved"
npx paperclipai approval request-revision <approval-id> --decision-note "Cap Video Producer at USD 10/month"
```

✅ **Expected:** Approved agents become active; the revised hire comes back for a second decision.

### 5. Give the researcher live web search
Agents → Market Researcher → Harness / Runtime → Environment variables → Add variable: Name TAVILY_API_KEY → Value source 'Organization secret' → select tavily_api_key → Save changes. The key never appears in prompts or tasks.

### 6. Share the brand-voice skill
Create the company skill from the file in your workspace, then attach it to the Copywriter and the Compliance Auditor (check under Org → Skills and Agent → Skills).

```bash
npx paperclipai skills create -C <company-id> --name "Kopi brand voice" --slug kopi-brand-voice --body-file ~/kopi-kaki/skills/kopi-brand-voice/SKILL.md
npx paperclipai skills agent sync <copywriter-id> --skill kopi-brand-voice --mode add -C <company-id>
npx paperclipai skills agent sync <auditor-id> --skill kopi-brand-voice --mode add -C <company-id>
```

### 7. Check the reporting lines
Agents → Org chart view. Expected: Board → Ava → {Market Researcher, Content Strategist, Compliance Auditor}; Content Strategist → {Copywriter, Video Producer}. If the auditor reports to the strategist, change it in Harness / Runtime → Agent identity → Reports to — and write one sentence on why.

### 8. Smoke-test the researcher
**Prompt** — paste into *Paperclip → New Task (assign to Market Researcher)*:

```text
Smoke test - live search.
Use Tavily to find 3 news items from the last 60 days about coffee or cold-brew trends in Singapore or Southeast Asia. For each: headline, date, URL and a one-line takeaway for Kopi Kaki. Mark anything you could not verify.
```

✅ **Expected:** Three results with URLs in the task thread.

## Verification / checkpoint
- [ ] 5 specialists active, each with a budget
- [ ] At least one hire went through Request revision
- [ ] TAVILY_API_KEY bound to the researcher from an organization secret
- [ ] Auditor reports to Ava; smoke test has URLs
- [ ] PP evidence: take ONE screenshot now of the Agents org chart view (Ava + hired specialists) — Task 3 of the Practical Performance uses it

**Checkpoint:** Five specialists in the Org chart view; the auditor reports to Ava; the researcher's smoke test returns cited Tavily results.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Hires joined without approval | The hiring gate was OFF — Settings → General → Hiring. Pause the agent and re-hire. |
| No Approvals in the sidebar | Use the Dashboard 'Pending Approvals' card or /<PREFIX>/approvals. |
| Researcher can't search | A plain-text env row shadows the secret — switch its Value source to 'Organization secret' and Save. |
| Plan exceeds budget | Request revision with the numbers; Ava must fit the total inside USD 60. |

## Stretch challenge
Ask Ava to propose a sixth role — Community Manager — and decide whether the value justifies the extra budget. Record your Board decision as an approval comment.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
