# Bonus Lab — Paperclip: Run Kopi Kaki as a One-Person Company

**Day 2 · Bonus topic · 60 min · AI company with an org chart, governed by you · LO3**

> You are the only human. A CEO agent hires a Chief of Staff, the Chief of Staff hires the marketing team, and you approve every hire from the Board seat.

## Goal
Set up a governed AI company with an org chart, hiring approvals and budgets, and compare it with the Hermes Kanban team (LO3).

## The business scenario
You are the founder-CEO of Kopi Kaki Co., a fictional Singapore kopi startup. The Tiong Bahru flagship opens on 1 Dec 2026 with the Gula Melaka Cold Brew (SGD 6.80, #ShiokColdBrew); until then you sell at weekend pop-ups and take app pre-orders. Your team is two baristas — and the AI agents you set up in this course. You have proved that agents can do the work. Now you decide to run Kopi Kaki as a one-person company (OPC): you sit on the Board, and an AI CEO runs the day-to-day. You set up Paperclip, write the CEO's instructions, and let the CEO hire a Chief of Staff, who hires the marketing team. Then you give the team the same launch-video brief as Activity 5 and compare.

## You will deliver
- Paperclip running at http://localhost:3100 with the company 'Kopi Kaki Co.'
- CEO agent with written instructions; a Chief of Staff hired through Board approval
- Marketing team hired by the Chief of Staff (researcher, writers, image creator, video producer, reviewer)
- Org chart screenshot: Board → CEO → Chief of Staff → team
- The launch-video task delivered by the team, and comparison.md: Paperclip vs Hermes Kanban

## Who does what
- **Agents:** CEO → Chief of Staff → 6 marketing agents
- **You (the human):** You are the Board: write the mission, approve hires and budgets, accept the video

## Before you start
- Hermes Desktop with Mia working (Topic 2) — Mia installs and starts Paperclip for you
- Node.js 24.11+ on the laptop (Mia checks; the trainer installs it if missing)
- This lab's data/ dragged into Desktop/kopi-kaki

## Concepts in action
- OPC: one human founder, an AI workforce, governance by design
- Paperclip = the company; agents = employees; you = the Board
- Delegated hiring: managers propose, the Board approves
- Kanban organises tasks; Paperclip organises people, budgets and reporting lines

## Lab files (`data/`)

| File | What it is |
|---|---|
| `paperclip-company-setup.md` | Values for the Paperclip company set-up |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `video-qa-checklist.md` | V1–V9 video QA checks |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |
| `paperclip-opc-setup.md` | Values for the Kopi Kaki one-person company and the target org chart |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-B-Instructions.pdf`](LAB-B-Instructions.pdf).

## Steps

### 1. What Paperclip is (5 min)
Paperclip (open source, github.com/paperclipai/paperclip) runs a company of AI agents: an org chart, job titles, reporting lines, budgets, tasks and an approval inbox. You are the Board. Hermes Kanban organised tasks for your team; Paperclip organises the people — who reports to whom, who may hire, and what each agent may spend. Watch the overview first: https://www.youtube.com/watch?v=WNYe5mD4fY8

### 2. Ask Mia to install and start Paperclip (10 min)
No terminal for you: Mia runs the installer and keeps it running.

**Prompt** — paste into *Hermes Desktop — Mia, folder Desktop/kopi-kaki*:

```text
Install Paperclip for me with its one-line onboarder (npx paperclipai onboard --yes) and keep it running. Check first that Node.js is 24.11 or newer; if not, stop and tell me what the trainer must install. When it is up, give me the link to open.
```

✓ **Expected:** Mia reports 'Server running at http://localhost:3100' — open it in your browser.

### 3. Set up the company: Kopi Kaki Co. (5 min)
In the onboarding wizard name the organization Kopi Kaki Co. Create the first agent and name her Ava. Connect a model. Then open Company settings: put the mission in the description and set the monthly budget to USD 60. Leave the onboarding task waiting — hiring rules come first.

✓ **Expected:** Kopi Kaki Co. exists with a USD 60/month budget.

### 4. Make Ava the CEO and write her instructions (8 min)
Paperclip's screen has no Role field, so ask Mia to set it. Then paste the CEO instructions below into Agents → Ava → Instructions → AGENTS.md, upload brand-guide.md, campaign-brief.md and compliance-rules.md with + (Add agent file), and switch ON Settings → General → Hiring → 'Require board approval for new hires'.

**Prompt** — paste into *Paperclip → Agents → Ava → Instructions → AGENTS.md (after asking Mia: 'In Paperclip, set Ava's role to CEO and her title to CEO for me.')*:

```text
You are Ava, CEO of Kopi Kaki Co., a Singapore kopi startup run as a one-person company: the founder is the Board and the only human.
Mission: launch the Gula Melaka Cold Brew on 1 Dec 2026 - 2,500 app pre-orders, one approved short video every week, AI spend under USD 60/month, zero compliance breaches.
How you work:
- You do not do the marketing work yourself. You hire and manage.
- Your first hire is a Chief of Staff who runs the marketing team for you.
- Every hire needs a mandate, a reporting line and a monthly budget, and waits for Board approval.
- Every public item passes an independent reviewer and then the Board. Never publish anything yourself.
- Source of truth: brand-guide.md, campaign-brief.md, compliance-rules.md.
- Report weekly to the Board: progress, spend vs budget, risks, decisions needed.
```

✓ **Expected:** Ava's role is CEO, her instructions show the mandate and three files, and the hiring gate is ON.

### 5. CEO task: hire a Chief of Staff (5 min)
Give Ava her first task. She proposes the hire; it lands in your approval inbox.

**Prompt** — paste into *Paperclip → New Task (assign to Ava)*:

```text
Hire a Chief of Staff for Kopi Kaki Co.
Mandate (3 bullets): turn my goals into weekly plans, hire and manage the marketing team, report progress and risks to you every Friday.
Reports to: you (CEO). Monthly budget: USD 10. Use the same adapter as you.
Submit the hire for Board approval and tell me when it is waiting.
```

✓ **Expected:** A 'Hire Agent' card in Pending Approvals.

### 6. Approve the hire from the Board seat (3 min)
Dashboard → Pending Approvals → View details → See full request. Check mandate, budget and reporting line, then click Approve.

✓ **Expected:** The Chief of Staff is active and reports to Ava.

### 7. Chief of Staff task: hire the marketing team (8 min)
Now the Chief of Staff staffs the same team you built in Activities 4 and 5. In Pending Approvals approve the hires that fit; send one back with Request revision.

**Prompt** — paste into *Paperclip → New Task (assign to the Chief of Staff)*:

```text
Hire the Kopi Kaki marketing team. All report to you.
- Market Researcher (finds facts with sources)
- Social Copywriter (LinkedIn, Facebook and Instagram posts)
- Image Creator
- Video Producer (HyperFrames)
- Voice-over Artist
- Content Reviewer (independent: checks posts and videos against compliance-rules.md and video-qa-checklist.md; can block release)
Give each a 3-bullet mandate and a monthly budget. The whole company must stay under USD 60/month including Ava and you. Submit every hire for Board approval.
```

✓ **Expected:** Six hire requests; after your decisions the team is active.

### 8. Show the organization chart (3 min)
Open Agents → Org chart view (icon next to New Agent). Expected: Board (you) → Ava (CEO) → Chief of Staff → six marketing agents. Take a screenshot: this is your one-person company.

### 9. Get the team to produce the launch video (10 min)
Give the Chief of Staff the same brief as Activity 5 so you can compare like with like. Watch the tasks the Chief of Staff creates and assigns.

**Prompt** — paste into *Paperclip → New Task (assign to the Chief of Staff)*:

```text
Produce the Gula Melaka Cold Brew launch video: 20 seconds, 1080x1920, 4 scenes, narration, facts only from campaign-brief.md and product-catalogue.csv, SGD 6.80, launch 1 Dec 2026, no health or halal claims.
Split it into tasks for the team, with the Content Reviewer checking the final file against video-qa-checklist.md. Ask me to approve the script before rendering and the exact final file before anything is used. Never publish.
```

✓ **Expected:** Sub-tasks assigned across the team, a script approval request, then a final-file approval request.

### 10. Compare Paperclip with the Hermes Kanban team (8 min)
Write down what each approach gave you.

**Prompt** — paste into *Paperclip → New Task (assign to Ava)*:

```text
Write comparison.md for the Board: Paperclip company vs the Hermes Kanban team from Activity 5 for the same launch video.
Rows: set-up time, who decides the task breakdown, approvals and hiring control, budget control, visibility (org chart, audit), output quality, my review effort, cost.
End with a recommendation: when should a one-person company use a Kanban team, and when a Paperclip company?
```

✓ **Expected:** A table and a clear recommendation.

## Verification / checkpoint
- [ ] http://localhost:3100 shows Kopi Kaki Co.; the hiring gate is ON
- [ ] Ava is CEO with written instructions
- [ ] Chief of Staff and six marketing agents hired through Board approvals
- [ ] Org chart: Board → CEO → Chief of Staff → team
- [ ] The video task ran with script and final-file approvals; comparison.md written

**Checkpoint:** The org chart shows Board → CEO → Chief of Staff → marketing team, every hire has a Board approval, and comparison.md answers when to use Kanban and when to use Paperclip.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Node.js too old | Ask the trainer to install Node.js 24.11+ (nodejs.org), then ask Mia to try again. |
| Port 3100 busy | Paperclip picks another port — ask Mia for the link it printed. |
| Run test fails | The agent's model is not signed in: connect a model in the agent's Harness / Runtime page. |
| Hires joined without approval | The hiring gate was OFF — Settings → General → Hiring. Pause the agent and re-hire. |

## Stretch challenge
Add a weekly routine (Routines → Create) that asks the Chief of Staff for one new video every Monday at 10:00, still behind your approval. What would you need to trust it to run unattended?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
