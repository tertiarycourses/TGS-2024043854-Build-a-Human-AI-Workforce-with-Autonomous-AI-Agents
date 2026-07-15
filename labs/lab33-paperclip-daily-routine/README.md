# Lab 33 — Routine & Trigger — Publish Daily at 3pm

## Objective
LO3: Automate the company with a scheduled routine and trigger. Put **Altera AI Blogs** on autopilot. You will create a **Routine** with a **daily 3:00pm trigger** that generates and runs the blog-publishing task automatically — the routine fires, creates the day's *'Produce and publish today's AI blog post'* task, the team executes the pipeline (**research → draft → edit → publish**), and the finished post lands in **in_review** for the Board. No human kicks it off.

## Prerequisites
- **Lab 32 complete** — the Board-approved team (research analyst, blog writer, editor/publisher, SEO/marketer) is hired and working the backlog.
- **Lab 31 complete** — the Tavily secret is bound so researchers can search live.
- Paperclip running at `http://localhost:3100` with an enabled adaptor (Lab 29).

## Estimated Time
20–30 minutes

## Steps

### 1. Open the Routines page from the sidebar (Work → Routines)
In the dashboard sidebar open **Work → Routines**. This page holds every scheduled automation the company runs — it is the equivalent of a cron board for your agent workforce.

### 2. Create a new routine: 'Daily AI blog publish'
Click **New routine** and name it:

> **Daily AI blog publish**

### 3. Set the trigger: schedule, daily at 3:00pm (15:00)
In the routine's trigger section choose **schedule** and set it to **daily at 3:00pm (15:00)**. The trigger is what fires the routine — from now on the clock, not a human, starts the day's publishing run.

### 4. Define what the routine generates: the task 'Produce and publish today's AI blog post'
Configure the routine to generate the task:

> **Produce and publish today's AI blog post**

Description:

> *Pull the top stories from the watchlist, verify against two sources, draft a cited post, publish for Board review* — assigned to the team.

Every time the trigger fires, a fresh copy of this task lands on the board and the team executes it end to end.

### 5. Save and enable the routine, then trigger it once manually to confirm it creates and runs the task
Save the routine and switch it to **enabled**, then use the manual **run/trigger now** control to fire it once. Confirm on the Tasks board that the task was created and the team started the pipeline: research → draft → edit → publish.

### 6. At the next 3:00pm, confirm the task was generated and executed automatically
Wait for the next 3:00pm tick and check: the task **'Produce and publish today's AI blog post'** was generated and executed **with no human action**, and the finished post is sitting in **in_review** for you, the Board.

## Verification / Expected Output
- The routine **'Daily AI blog publish' is enabled** with a **daily 15:00 trigger**.
- A **manual run creates and executes the publish task** through the full pipeline.
- The **next 3pm run happens without human action**, leaving the day's post in **in_review** for the Board.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| No Routines page in the sidebar | Look under **Work → Routines** and confirm you are in the right company (**Altera AI Blogs**) — routines are company-scoped. |
| Routine saved but never fires | It is not **enabled** — flip the enable switch after saving, then check the trigger reads daily at 15:00. |
| Fires at the wrong hour | The instance timezone differs from yours — check the server/container timezone and adjust the trigger time to match. |
| Task is generated but nobody works it | The generated task isn't assigned — edit the routine's task definition to assign the team (or the CEO to dispatch it). |
| Manual run works, scheduled run doesn't | The Paperclip stack was down at 15:00 — keep the Docker Compose stack running (detached) so the trigger can fire. |
| Post never reaches in_review | Watch the task's activity log for a failed step (e.g. Tavily key missing — recheck Lab 31's binding). |

## Exercise / Challenge
Add a second routine of your own design — e.g. a **weekly Monday 9:00am** routine that generates *'Publish the weekly AI roundup post'* summarizing the week's seven daily posts. Enable it, trigger it manually once, and then disable the daily routine and note in two sentences what stops happening — that difference is exactly what the trigger automates.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
