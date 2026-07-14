# Lab 7 — Cron Jobs & Automation

## Objective
LO4: Automate recurring agent work on a schedule. You will schedule **Athena** to run recurring jobs — for example an 8am daily briefing sent to your messaging app — and verify the scheduled run fires and produces output.

## Prerequisites
- **Lab 1–6 complete** — Hermes running with a provider, and ideally an MCP/Tool Gateway tool (from Lab 6) so the job can gather real content.
- A destination for the briefing (messaging app / channel) if you want delivery.

## Estimated Time
35–45 minutes

## 📺 Reference Video
[Cron Jobs & Automation](https://www.youtube.com/watch?v=grMNnzCv2gY&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=8)

## Steps

### 1. Watch the reference video
Watch how recurring jobs (crons/automations) are defined and triggered in Hermes. The exact syntax is version-specific, so follow the video closely:

[https://www.youtube.com/watch?v=grMNnzCv2gY&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=8](https://www.youtube.com/watch?v=grMNnzCv2gY&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=8)

### 2. Define a recurring job (daily 8am briefing)
Create a recurring automation in the Hermes automations/crons section — for example a daily 8am briefing:

```bash
# see the automations/crons section (verify exact syntax in docs)
```

Open the automations/crons configuration (Desktop app's automation UI or the crons section of `~/.hermes/config.yaml`). Define a job with:
- **Schedule:** daily at 08:00 (cron-style `0 8 * * *`).
- **Prompt/task:** e.g. *"Give me a concise bulleted briefing: my calendar today, top 3 industry headlines, and anything overdue."*
- **Delivery:** your messaging app/channel (optional).

> Cron syntax and the automation config keys are **version-specific** — verify the exact syntax in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/). Do not assume flags that aren't in your build.

### 3. Confirm the automation is registered
Run the diagnostic to confirm Hermes has picked up the new scheduled job:

```bash
hermes doctor
```

Look for the automation/scheduler being healthy and the job listed. If your build has a dedicated crons list command, use it too (check `hermes --help`).

### 4. Trigger the job once to confirm it produces output
Manually run the job once (rather than waiting for 8am) to confirm it produces the expected briefing.

> This is typically a "run now" action in the automations UI, or a trigger command shown in the docs. Confirm the briefing is generated and delivered to your chosen destination.

### 5. Confirm the next scheduled run is queued
Check that after the manual run, the **next** run is still scheduled for its normal time (08:00 tomorrow), so the automation keeps recurring.

## Verification / Expected Output
- The scheduled job **runs at its time (or on manual trigger)** and delivers the expected briefing.
- `hermes doctor` shows the scheduler/automation healthy and the job registered.
- After a manual run, the **next scheduled run is queued**.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Job not listed after saving | Restart Hermes/gateway so it re-reads the automation config; check YAML indentation. |
| Cron never fires at the set time | Confirm the schedule expression and your machine's timezone; the local deployment must be running at that time. |
| Manual trigger works but delivery fails | Re-check the messaging-app/channel integration and any required token. |
| Unsure of the exact cron syntax | Verify in the video / docs (https://hermes-agent.nousresearch.com/docs/) — syntax is version-specific. |
| Briefing content is empty | The prompt has nothing to pull from — connect the calendar/news tools from Lab 6 first. |

## Exercise / Challenge
Add a **second** automation: an end-of-day 6pm job that asks Athena to summarize what was completed today and list tomorrow's top 3 priorities. Trigger both jobs manually and confirm each delivers a distinct, correctly-formatted briefing. Bonus: make the morning job depend on your remembered "concise, bulleted" preference from Lab 3.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
