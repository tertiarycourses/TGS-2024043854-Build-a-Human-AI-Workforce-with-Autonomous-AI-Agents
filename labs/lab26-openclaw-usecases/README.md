# Lab 26 — Use Cases & Key Functions

## Objective
Tie the whole OpenClaw track together by building at least one **end-to-end back-office automation** for **Nimbus Supplies** — combining channels, skills, tools, memory, dreaming, and crons into a real workflow (customer Q&A, supplier research-to-quote, or nightly reporting). By the end you will have proven that OpenClaw's key functions work together, not just in isolation.

## Prerequisites
- Completed OpenClaw track Labs 15–25: a running gateway, a model provider, at least one channel, one or more skills, tools, memory, and (optionally) the multi-agent team from Lab 24.
- `openclaw gateway status` reports **running**.
- Access to whatever a chosen use case needs (e.g. a Telegram channel for customer Q&A, a Firecrawl/web-search tool for supplier research, AgentMail or similar for sending quotes).

## Estimated Time
30–40 minutes

## 📺 Reference Videos
Three concrete OpenClaw use cases — pick one (or more) to implement:
- **Google Workspace CLI assistant** — [watch](https://www.youtube.com/watch?v=_ssB1YXRRtk&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J&index=9)
- **Data Analytics agent** — [watch](https://www.youtube.com/watch?v=RLUa-j-MpgQ&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J&index=10)
- **Social Media Marketing agent** — [watch](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J&index=1)

## Steps

1. **Watch one of the use-case videos above** and study how the presenter composes several functions into one automation — which channel triggers the flow, which skills and tools it calls, and how memory and crons fit in. Good starting points: a **Google Workspace CLI** assistant (Docs/Sheets/Gmail), a **Data Analytics** agent, or a **Social Media Marketing** agent.

2. **Pick a back-office use case.** Choose one concrete Nimbus Supplies workflow to implement end-to-end. A strong default is **"research a supplier, then email a quote"**: a customer asks for a price, the agent looks up current supplier pricing, applies a margin, and emails a formatted quote. Other options: customer FAQ Q&A on Telegram, or an automated nightly orders-and-quotes report.

3. **Compose the channels, skills and tools needed for it.** Wire the pieces together for your chosen use case. For research-to-quote that means: the customer **channel** (e.g. Telegram) as the trigger, the **skill** that formats a quote (e.g. `nimbus-quote` from Lab 18), a research **tool** (Firecrawl / `web_search`) for live pricing, and a delivery **tool** (AgentMail) to send the email. Confirm the agent has permission to call each one.

4. **Run the automation end-to-end and verify the outcome.** Send a real trigger — e.g. message the agent "What's your price for 50 kg of arabica beans?" on the customer channel — and watch the full chain fire: the agent recalls context from **memory**, runs the price lookup **tool**, builds the quote with the **skill**, and delivers it via email. Confirm the actual deliverable (the sent quote email) is correct, not just that the logs look busy.

5. **Schedule it or hand it to the multi-agent team from Lab 24.** Make the automation ongoing. Either attach it to a **cron** (e.g. a nightly consolidation report) so it runs unattended, or delegate the use case to the Sales / Research / Ops agents you built in Lab 24 so the right specialist owns each step. This is what turns a one-off demo into part of an always-on Nimbus Supplies back office.

## Verification / Expected Output
- A real back-office use case runs **end-to-end** using OpenClaw's channels, skills, tools and crons.
- The trigger (a customer message, a schedule, or a manual run) produces a genuine deliverable — for research-to-quote, an actual quote email combining memory, the quote skill, a live price lookup, and email delivery.
- The activity is visible across the stack: the channel received the trigger, the tools were called, and the outcome was produced.
- If scheduled or delegated, the automation continues to run without you re-triggering it manually.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Agent replies but never calls the tool | The tool is not attached or is denied for this agent. Re-check the agent's allow-list (Lab 24) and re-run `openclaw doctor`. |
| Quote email never arrives | The delivery tool (AgentMail) is unconfigured or rate-limited. Test the mail tool in isolation, then re-run the flow. |
| Price lookup returns stale/empty data | The research tool (Firecrawl/`web_search`) failed or was blocked. Check the tool's credentials and target URL. |
| Cron does not fire | Verify the schedule with `openclaw cron list`; confirm the gateway is running and the timezone is what you expect. |
| Multi-agent handoff loops | Two agents each think the other owns the step. Give one agent a clear mandate and remove overlapping tools. |

## Exercise / Challenge
Implement the research-to-quote use case fully for Nimbus Supplies, then add a second, different use case (e.g. a nightly report cron that summarises the day's quotes and flags anything still waiting on Research). Prove they coexist: send a live quote request and, the same evening, confirm the nightly cron posts a summary that references that exact request. Write a short paragraph mapping each step of both flows to the OpenClaw function it uses (channel, skill, tool, memory, cron, dreaming).

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
