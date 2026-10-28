# Lab 9 — Automate the Weekly Video Pipeline with a Routine and a Board Gate

**Day 2 · Topic 3 · 30 min · Scheduled multi-agent workflow · LO3**

> Turn research → script → production → audit → publish-ready into a routine that fires every Monday at 10:00 — and still stops for your approval.

## Goal
Automate a recurring multi-agent workflow while keeping a human approval gate, and assess the trade-off between autonomy and control (LO3).

## The business scenario
Goal 2 is one approved short video every week. You do not want to create the task by hand every Monday, but you also never want a video to go out unseen. You create the 'Weekly Kopi Short' routine: the clock creates the task, Ava delegates the pipeline, and the finished package waits for a Board approval.

## You will deliver
- Routine 'Weekly Kopi Short' for Ava — schedule trigger every week, Monday 10:00, Asia/Singapore
- One manual Run that produced a complete package
- Publish package + video/storyboard + audit in the run's task
- A Board Approval request that you approved (or rejected) with a comment

## Who does what
- **Agents:** CEO + Researcher + Copywriter + Video Producer + Auditor
- **You (the human):** Approve each week's video before it is published

## Before you start
- Labs 7–8 complete: the team has delivered at least one reviewed package

## Concepts in action
- Routine = trigger + generated task (a cron for a company)
- Heartbeats: agents wake on schedule or on assignment
- Autonomy level L4 Approver — the agents ask only at the gate
- Same pipeline as Lab 4, now governed and repeatable

## Lab files (`data/`)

| File | What it is |
|---|---|
| `paperclip-routine-weekly-kopi-short.md` | Routine spec |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `video-qa-checklist.md` | V1–V9 video QA checks |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-09-Instructions.pdf`](LAB-09-Instructions.pdf).

## Steps

### 1. Create the routine
Work → Routines → Create routine. Title 'Weekly Kopi Short'; For: Ava; in: ShiokColdBrew Launch (or a new project 'Weekly Content'); Advanced delivery settings → concurrency 'skip_if_active'. Paste the instructions below, then Create routine. (Without a default agent the routine stays a paused draft.)

**Prompt** — paste into *Paperclip → Routines → Create routine → Instructions*:

```text
Produce this week's Kopi Short (research -> script -> production -> audit -> publish-ready).
Delegate: Market Researcher picks one fresh angle (cite 2 sources); Copywriter writes a 20-30 second script in the Kopi Kaki voice (kopi-brand-voice); Video Producer renders the video, or a 6-frame storyboard if rendering is unavailable; Compliance Auditor checks compliance-rules.md (C1-C10) and video-qa-checklist.md (V1-V9).
Deliver a publish package: title, description with AI disclosure, 3-5 hashtags incl. #ShiokColdBrew, thumbnail, captions.
Gate: before anything is published, file a Board approval request with the package attached. Do NOT publish. Stay within each agent's budget.
```

✅ **Expected:** The routine lands on its Triggers tab.

### 2. Add the weekly trigger
Triggers → Add trigger → 'On a schedule' → Repeat: Every week → Monday → Time 10:00 → Time zone Asia/Singapore → Add schedule. (The default repeat is Weekdays — change it.) CLI alternative:

```bash
npx paperclipai routine list -C <company-id>
npx paperclipai routine trigger:create <routine-id> --payload-json '{"kind":"schedule","cronExpression":"0 10 * * 1","timezone":"Asia/Singapore"}'
```

✅ **Expected:** Next run: Monday 10:00 SGT.

### 3. Test before you trust — Run it now
Click Run on the routine's header (or Run now in the list). A new task is created for Ava; follow her delegation in the task thread and in Audit → Runs.

```bash
npx paperclipai routine run <routine-id>
npx paperclipai routine runs <routine-id> --limit 5
```

### 4. Board gate — approve or send back
Two gates, two strengths. (1) The Board approval request is prompt-enforced — the agents file it because the routine's instructions say so. (2) Approvers on a task are runtime-enforced, but routine-generated tasks are not guaranteed to carry them, so open the generated task and set Properties → Execution → Approvers → Assign to me every week. Then Dashboard → Pending Approvals → 'Board Approval' card: watch the video (or storyboard), read the audit, Approve, Reject or Request revision — and say why in Comments.

### 5. Tune the autonomy
Decide what may run without you each week (research, script, audit) and what must stop for you (publishing, any price or promo change). Add it as a rule to Ava's AGENTS.md so next Monday's run follows it.

## Verification / checkpoint
- [ ] Routine active with a weekly Monday 10:00 Asia/Singapore trigger
- [ ] Manual run created a task and completed the pipeline
- [ ] The generated task shows you as Approver
- [ ] A Board Approval request decided by you with a comment

**Checkpoint:** A manual Run produced a full package and a Board Approval request; the routine shows a weekly Monday 10:00 Asia/Singapore trigger.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Routine is a paused draft | Set a default agent (For: Ava) — the automation toggle needs one. |
| Sub-tasks not created | Ava may be paused or over budget — check Audit → Budgets; raise the cap or wait. |
| No approval request appeared | Agents follow the instructions — make the 'file a Board approval request' line explicit, and set yourself as Approver on the task. |
| Wrong time | Edit the trigger's time zone to Asia/Singapore. |

## Stretch challenge
Add a second trigger: a webhook that starts the pipeline when a competitor launches a product. What new risks does an event-driven trigger add, and what gate would you add?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
