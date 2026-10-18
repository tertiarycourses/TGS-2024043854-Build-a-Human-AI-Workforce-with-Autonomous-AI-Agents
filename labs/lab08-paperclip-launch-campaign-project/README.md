# Lab 8 — Run the #ShiokColdBrew Launch as a Project — Review, Revise, Release

**Day 2 · Topic 3 · 55 min · Multi-agent project with Board review · LO3**

> Turn the campaign into seven linked tasks, let the team execute research → plan → copy → video → audit, and use an approval gate to send work back until it is good enough to release.

## Goal
Run and evaluate an end-to-end multi-agent project, using review gates and revision cycles to improve output quality (LO3).

## The business scenario
Ava's team is hired. Now it must deliver the launch campaign pack the Marketing Lead asked for on Day 1 — but as a company: tracked tasks, dependencies, owners, costs and an audit trail. Your job is the Board review: the deliverables that go public stop with you, and you either approve them or send them back with specific comments.

## You will deliver
- Project 'ShiokColdBrew Launch' linked to goal 1, with 7 tasks and blocked-by links
- research-report, campaign plan + calendar, teaser captions, video script, video/storyboard + publish package
- Compliance audit (agent reviewer) before your approval on captions, video and release pack
- At least one task sent back with a comment and returned improved
- A retrospective with cycle time, revisions and spend

## Who does what
- **Agents:** CEO + 5 specialists
- **You (the human):** Approve or send back every public deliverable; release

## Before you start
- Lab 7 complete: five specialists hired and active
- Day 1 outputs in ~/kopi-kaki/outputs (research brief, content calendar) — the team builds on them

## Concepts in action
- Tasks + blocked-by = an ordered workflow with owners
- Execution policy: agent Reviewer, then human Approver
- Revision comments are feedback the agents act on
- Audit → Activity = the trail for every decision

## Lab files (`data/`)

| File | What it is |
|---|---|
| `paperclip-backlog.csv` | 7 launch issues with dependencies |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `video-qa-checklist.md` | V1–V9 video QA checks |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-08-Instructions.pdf`](LAB-08-Instructions.pdf).

## Steps

### 1. Create the project
Work → Projects → Add Project 'ShiokColdBrew Launch' → Configuration → link goal 1 (2,500 pre-orders). Paste campaign-brief.md into the description, and attach your Day 1 work so the team builds on it instead of starting again: ~/kopi-kaki/outputs/lab01/research-brief.md and ~/kopi-kaki/outputs/lab02/content-calendar-v2.csv.

### 2. Let the CEO build the backlog
**Prompt** — paste into *Paperclip → New Task (assign to Ava, project ShiokColdBrew Launch)*:

```text
Set up the ShiokColdBrew Launch backlog.
Create the 7 tasks in paperclip-backlog.csv inside project "ShiokColdBrew Launch" - same titles, assignees, priorities, blocked-by links and definitions of done (paste the definition of done into each task). Tasks 1 and 2 must start from the Day 1 research brief and content calendar attached to the project. Reply with the task keys.
```

✅ **Expected:** 7 tasks with owners and blocked-by relationships.

### 3. Put the gates on the public deliverables
Open tasks 3 (captions), 5 (video + publish package) and 7 (release pack). In Properties → Execution: Reviewers → Compliance Auditor (the agent review stage), and Approvers → Assign to me (the human gate). When the owner marks a task done, Paperclip moves it to in_review — first to the auditor, then to you.

### 4. Start the work and watch it flow
Assigning a task (or commenting on it) wakes its agent; if nothing starts, click Run now on the agent. Watch tasks move backlog → todo → in_progress → in_review → done, and blocked-by links release the next task. Audit → Runs shows every run and its cost.

### 5. Board review — send something back
When a task reaches 'Approval pending with you', read it against the brief. Send at least one back with specific, testable comments — in the task thread, or with the CLI (the comment must be in the same request):

```bash
npx paperclipai issue update <TASK-KEY> --status in_progress --comment "1) Only 3 TikTok posts - we need at least 6 for the 40,000-view KPI. 2) Caption 4 says 'healthier than soft drinks' - remove (rule C1). 3) Every post showing SHIOK20 must show its terms (rule C3)."
```

✅ **Expected:** The task returns to its owner, is revised and comes back to you.

### 6. Approve and release
Approve each gated task with a decision comment. For the release pack, check: what is ready, what is not, open risks, total spend. 'Released' means approved to publish — publishing itself stays a human action (or the Day 1 Telegram flow).

```bash
npx paperclipai issue update <TASK-KEY> --status done --comment "Approved for release - post via the Telegram approval flow"
```

### 7. Run the retrospective
**Prompt** — paste into *Paperclip → New Task (assign to Ava)*:

```text
Launch project retrospective for ShiokColdBrew Launch.
Report: cycle time per task, number of Board send-backs and auditor findings, spend per agent vs budget, and the three biggest quality problems we caught at review. Recommend two changes to agent instructions that would have prevented them.
```

✅ **Expected:** A retrospective with metrics and two instruction changes (you will apply them in Lab 10).

## Verification / checkpoint
- [ ] Project linked to goal 1 with 7 linked tasks, all done
- [ ] Reviewer = Compliance Auditor and Approver = you on tasks 3, 5, 7
- [ ] ≥ 1 send-back with comment visible in Audit → Activity
- [ ] Retrospective lists cycle time, revisions, spend

**Checkpoint:** All 7 tasks done; at least one went back from in_review with a comment and returned improved; the release pack was approved by you with a comment.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Task never starts | Check it is assigned, not blocked, and the agent is not paused or out of budget (Audit → Budgets); then Run now on the agent. |
| Task went straight to done | No Approver was set before the owner finished — set Properties → Execution → Approvers and reopen it. |
| Approving fails with 422 | Only the named approver can approve, and a comment is required in the same request. |
| Video not rendered | Accept a storyboard + script; rendering is optional on Day 2. |

## Stretch challenge
Add a dependency the plan missed (e.g. 'Legal check of SHIOK20 terms' before release). How does one new gate change cycle time and risk?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
