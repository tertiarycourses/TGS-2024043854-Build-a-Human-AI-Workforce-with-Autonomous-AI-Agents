# Lab 6 — Activity 6 — Crons Make Next Week's Posts and Video While You Sleep

**Day 2 · Topic 3 · 30 min · Scheduled jobs that start the team's work · LO3**

> Your team works when you tell it to. A cron makes it work on Monday at 9:00 without you: fresh posts, a new video draft, waiting for your approval.

## Goal
Automate recurring content work with scheduled jobs, keep a human approval gate on every output, and test, pause and measure the jobs (LO3).

## The business scenario
You are the founder-CEO of Kopi Kaki Co., a fictional Singapore kopi startup. The Tiong Bahru flagship opens on 1 Dec 2026 with the Gula Melaka Cold Brew (SGD 6.80, #ShiokColdBrew); until then you sell at weekend pop-ups and take app pre-orders. Your team is two baristas — and the AI agents you set up in this course. The launch campaign runs for four weeks. You do not want to brief the team from scratch every Monday, so you schedule the work: every Monday the social bots draft the week's three posts, and every Friday the video team starts a new 15-second clip. The schedule starts the work; you still approve everything before it is used.

## You will deliver
- A Monday 9:00 job: the social bots draft three posts into outputs/social/weekly/ and tell you on Telegram
- A Friday 10:00 job: Mia starts a Kanban video run with your two HUMAN gates
- Both jobs tested once with Trigger now, then left scheduled (or paused after class)
- outputs/automation/cron-log.md: job, schedule, what it produced, what you approved

## Who does what
- **Agents:** Mia and the Activity 4 and 5 teams, started by scheduled jobs
- **You (the human):** Choose the schedule, approve every post and video, pause a job that misbehaves

## Before you start
- Activities 4 and 5 done (bots, role files and the kopi-video board exist)
- Telegram connected with /sethome from the Topic 2 setup
- Hermes Desktop stays open while a job runs (on a laptop that sleeps, nothing runs)

## Concepts in action
- A cron is a schedule plus a prompt: it starts work without being asked
- Automate the start of the work, never the approval
- Test with Trigger now before you trust a schedule; pause what you cannot watch
- Measure what the automation saves: drafts per week, your review minutes, model cost

## Lab files (`data/`)

| File | What it is |
|---|---|
| `AGENTS.md` | Company context Hermes loads automatically |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-06-Instructions.pdf`](LAB-06-Instructions.pdf).

## Steps

### 1. Read a scheduled job like a recipe (3 min)
Open Scheduled jobs in the left sidebar and click your Morning email brief. Every job has the same parts: a name, a frequency, the next run, where it delivers, and the prompt it runs. Pause stops it; Trigger now runs it immediately. The Blueprints list shows ready-made jobs (Weekly review, Competitor news watch, Topic news digest …).

✓ **Expected:** You can point to the frequency, the delivery target, the prompt, Pause and Trigger now.

### 2. Monday 9:00: the week's social drafts (7 min)
The job starts the work; you still approve. It writes drafts into a dated folder and tells you on Telegram — it never posts.

**Prompt** — paste into *Hermes Desktop — Mia, folder Desktop/kopi-kaki*:

```text
Create a scheduled job called 'Weekly social drafts' that runs every Monday at 9:00 Asia/Singapore time and delivers to my Telegram.
Job: in Desktop/kopi-kaki, read campaign-brief.md, research.md and last week's approval-log.md. Following the rules in souls/lin.SOUL.md, souls/farah.SOUL.md and souls/ivy.SOUL.md, draft this week's LinkedIn, Facebook and Instagram posts into outputs/social/weekly/<date>/, make one image per post with tools/make_post_image.py and a gallery.html. Then message me: 'Drafts ready — reply APPROVE, EDIT or REJECT per post'. Never post or publish anything.
Show me the job when it is saved.
```

✓ **Expected:** 'Weekly social drafts' appears in Scheduled jobs: every Monday 9:00, delivered to Telegram.

### 3. Friday 10:00: a new video draft on the board (7 min)
This job does not make the video itself: it starts a new run on the Kanban board, so your two HUMAN gates still hold.

**Prompt** — paste into *Hermes Desktop — Mia, folder Desktop/kopi-kaki*:

```text
Create a scheduled job called 'Weekly video draft' that runs every Friday at 10:00 Asia/Singapore time and delivers to my Telegram.
Job: on the kopi-video Kanban board, create a new run for a 15-second clip about this week's best-performing angle from outputs/social/approval-log.md: the same seven cards as Activity 5 with both HUMAN gates (approve the script, approve the exact video). Message me when the script is waiting for my approval. Nothing is rendered before I approve the script; nothing is published.
Show me the job when it is saved.
```

✓ **Expected:** 'Weekly video draft' appears in Scheduled jobs: every Friday 10:00.

### 4. Test both now with Trigger now (8 min)
Do not wait until Monday. In Scheduled jobs open each job and click Trigger now. Check Telegram, the new dated folder in outputs/social/weekly/ and the new cards on the kopi-video board.

✓ **Expected:** Two Telegram messages; a dated drafts folder with three posts and a gallery; new kopi-video cards waiting at your HUMAN gate.

### 5. Log it and stay in control (5 min)
Automation you cannot see is automation you cannot trust. Record what each job does, then pause the video job after class so it does not spend model credits while nobody is watching.

**Prompt** — paste into *Hermes Desktop — Mia*:

```text
Write outputs/automation/cron-log.md: one row per scheduled job with name, schedule, what the test run produced, model time used, and what still needs my approval. Then list my scheduled jobs with their next run time.
```

✓ **Expected:** cron-log.md with three rows (morning brief, social drafts, video draft); you paused 'Weekly video draft' in Scheduled jobs.

## Verification / checkpoint
- [ ] Scheduled jobs lists 'Weekly social drafts' (Mon 9:00) and 'Weekly video draft' (Fri 10:00)
- [ ] Trigger now produced dated drafts, a gallery and new kopi-video cards
- [ ] Telegram received both notifications
- [ ] Nothing was posted or rendered without your approval
- [ ] cron-log.md records every job; the video job is paused after class

**Checkpoint:** Scheduled jobs lists both jobs with the right times, each test run produced drafts and a Telegram message, and nothing was published without your approval.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Job never runs | Hermes Desktop must be open and the laptop awake at that time. Use Trigger now to test. |
| No Telegram message | Send /sethome in your Telegram chat with Mia, then Trigger now again. |
| Wrong time | Ask Mia to set the job's timezone to Asia/Singapore, or edit the frequency in Scheduled jobs. |
| The job did more than asked | Pause it, then tell Mia exactly what to remove from its prompt. Approval steps never move into a cron. |

## Stretch challenge
Use the Competitor news watch blueprint for Kopi Kaki's six competitors. What should the job do when it finds a price cut: alert you, or draft a response for your approval?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
