# Lab 21 — Cron Jobs & Heartbeat

## Objective
Make Nimbus Supplies run without you watching it. You will schedule recurring agent tasks with **cron** (a nightly sales report and a weekly supplier price-check) and monitor agent uptime with the **heartbeat** so the gateway self-checks, auto-restarts, and can page an external monitor if it dies.

## Prerequisites
- Labs 15–20 completed (channels live, Firecrawl + AgentMail enabled).
- The gateway daemon installed so crons fire while you are away (`openclaw gateway install` from Lab 15/16).

## Estimated Time
30 minutes

## 📺 Reference Video
[OpenClaw reference playlist](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J)

## Steps

1. **Create the nightly sales-report cron.** Cron syntax is `<min> <hour> <day> <month> <weekday>`.

   ```bash
   # Every day at 21:00 — post a Nimbus Supplies end-of-day summary to Telegram
   openclaw cron create \
     --schedule "0 21 * * *" \
     --prompt "Summarise today's Nimbus Supplies customer chats and any quotes sent. List open questions that still need a human." \
     --channel telegram \
     --name nightly-sales-report
   ```

2. **Create a weekly supplier price-check cron** (uses Firecrawl from Lab 19):

   ```bash
   # Every Monday at 08:00 — check supplier prices and email me
   openclaw cron create \
     --schedule "0 8 * * 1" \
     --prompt "Use Firecrawl to fetch our main supplier's A4 paper price and email me the current price via AgentMail with subject 'Weekly supplier price'." \
     --channel telegram \
     --name weekly-price-check
   ```

   

3. **List and inspect your crons.**

   ```bash
   openclaw cron list
   openclaw cron show nightly-sales-report
   openclaw cron logs nightly-sales-report --tail 20
   ```

4. **Fire a cron on demand to test it now** (ignores the schedule):

   ```bash
   openclaw cron run nightly-sales-report
   ```

   Check the target channel — you should receive the summary within a few seconds.

5. **Disable / enable / delete crons** as your needs change:

   ```bash
   openclaw cron disable weekly-price-check
   openclaw cron enable  weekly-price-check
   openclaw cron delete  weekly-price-check   # only if you no longer need it
   ```

6. **Enable the heartbeat.** The heartbeat is a periodic self-check that verifies the gateway is alive, the model responds, and channels are connected; on failure the daemon attempts auto-restart and logs the incident.

   ```bash
   openclaw gateway heartbeat enable --interval 60s
   openclaw gateway heartbeat status
   openclaw gateway heartbeat logs --tail 20
   ```

7. **(Optional) Push a heartbeat ping to an external monitor** so you are paged if Nimbus Supplies goes dark (e.g. a free <https://healthchecks.io/> check):

   ```bash
   openclaw gateway heartbeat webhook \
     --url https://hc-ping.com/<your-uuid> \
     --interval 5m
   ```

8. **Confirm auto-restart works.** Ensure the daemon is installed to auto-start, then simulate a crash:

   ```bash
   openclaw gateway status        # expect "running" + "auto-start: yes"
   openclaw gateway stop
   # wait ~60s for the service manager to restart it
   openclaw gateway status        # expect "running" again
   ```

### 9. The natural-language way
You can skip the CLI entirely and simply ask the agent: *"Add a heartbeat task: every 30 minutes, check my inbox and flag anything urgent"*.

## Verification / Expected Output
- `openclaw cron list` shows **nightly-sales-report** and **weekly-price-check**.
- `openclaw cron run nightly-sales-report` delivers a summary to Telegram immediately.
- `openclaw gateway heartbeat status` reports **healthy**.
- After `openclaw gateway stop`, the service manager restarts the gateway within about a minute (confirmed by `openclaw gateway status`).

  

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Cron created but never fires | Crons only run while the gateway is up. `openclaw gateway status`; install the daemon with `openclaw gateway install`. |
| Cron fires but no message arrives | `openclaw cron logs <name>` — usually a model or channel error. |
| Heartbeat says "unhealthy: provider" | API key expired or out of credits — revisit Lab 16. |
| Auto-restart not working | Re-run `openclaw gateway install`; verify the unit in your OS service manager. |
| Weekly price-check email empty | Confirm Firecrawl + AgentMail are enabled (`openclaw tools list --enabled`). |

## Exercise / Challenge
Add a third cron that every **weekday at 18:00** asks in Telegram "Any orders to fulfil before we close?" and, based on your reply, drafts (but does not send) a supplier restock email via AgentMail. Then wire the heartbeat to a real healthchecks.io check and confirm you get an alert within 5 minutes of stopping the gateway. By the capstone, the Ops agent will own crons like these.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
