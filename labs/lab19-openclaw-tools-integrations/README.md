# Lab 19 — Tools & Integrations

## Objective
Extend the Nimbus Supplies agent with two real-world integrations — **Firecrawl** (reliable, JS-rendered web scraping) and **AgentMail** (its own inbox/outbox) — then run an end-to-end back-office task: research a supplier's website, then email a customer a quote. You will also learn tool profiles and allow/deny lists.

## Prerequisites
- Labs 15–18 completed (OpenClaw running, model connected, at least one channel live).
- Free accounts and API keys from:
  - <https://www.firecrawl.dev/> (key looks like `fc-...`)
  - <https://agentmail.to/> (key + an inbox address like `bot@yourname.agentmail.to`)

## Estimated Time
40–50 minutes

## 📺 Reference Video
[OpenClaw reference playlist](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J)

## Steps

1. **Inspect the built-in tools first.**

   ```bash
   openclaw tools list
   ```

   You should see categories such as `group:fs` (file read/write), `group:web` (`web_search`, `web_fetch`, `browser`), `group:runtime` (`exec`, sandboxed Python), and `group:media`.

   

2. **Enable Firecrawl.** Sign up at <https://www.firecrawl.dev/>, then Dashboard → API Keys → copy the `fc-...` key:

   ```bash
   export FIRECRAWL_API_KEY="fc-..."
   openclaw tools enable firecrawl --api-key "$FIRECRAWL_API_KEY"
   openclaw tools status firecrawl
   ```

3. **Smoke-test Firecrawl from chat.** In Telegram or WhatsApp:

   > Use Firecrawl to fetch the products page of a stationery supplier's website and list their A4 paper options with prices in 5 bullets.

4. **Enable AgentMail.** Create an inbox at <https://agentmail.to/>, copy the API key and inbox address:

   ```bash
   export AGENTMAIL_API_KEY="..."
   openclaw tools enable agentmail \
     --api-key "$AGENTMAIL_API_KEY" \
     --inbox bot@yourname.agentmail.to
   openclaw tools status agentmail
   ```

5. **Smoke-test AgentMail.** From chat:

   > Send an email from my AgentMail inbox to `<your-personal-email>` with subject "Hello from Nimbus Supplies" and a friendly one-paragraph body.

   Check your inbox, reply to it, then ask:

   > Check my AgentMail inbox and summarise the latest reply.

6. **Run the real end-to-end task (research → quote → email).** From a channel, send one instruction that chains both tools plus the skill from Lab 18:

   > A customer, Acme Cafe, wants 10 reams of recycled A4 paper and 5 boxes of black pens. Use Firecrawl to check current prices on our supplier's site, then use the `nimbus-quote` skill to draft an itemised quote, and email it from my AgentMail inbox to orders@acmecafe.example with subject "Your Nimbus Supplies quote".

   

7. **Scope tools per channel with profiles and allow/deny lists.** Public channels should not run shell exec. Apply the safe `messaging` preset and lock down a public channel:

   ```bash
   openclaw channel set telegram --profile messaging
   openclaw channel set telegram --deny exec
   openclaw channel set telegram --allow group:web
   openclaw channel show telegram
   ```

8. **(Optional) Add one more integration of your choice.** Pick one from <https://docs.openclaw.ai/tools> and enable it (exact name/flags per the docs), e.g.:

   ```bash
   openclaw tools enable <tool-name> --api-key <KEY>
   ```

## Verification / Expected Output
- `openclaw tools list --enabled` shows **firecrawl** and **agentmail**.
- The agent scrapes a supplier URL on demand and returns structured prices.
- The agent sends an email via AgentMail that arrives in a real inbox.
- The end-to-end task produces an itemised quote email combining scraped prices and the `nimbus-quote` skill.
- A channel set to `--deny exec` refuses shell-exec requests.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `tool 'firecrawl' not found` | Update OpenClaw: `npm install -g openclaw@latest`, then re-enable. |
| `401 Unauthorized` from Firecrawl | Re-copy the key; check for trailing whitespace in the `export`. |
| AgentMail send returns 403 | Confirm the inbox is verified in the AgentMail dashboard. |
| Agent scrapes but invents prices | Tell it to only report prices it actually retrieved and mark unknowns "TBC" (matches the Lab 18 skill rule). |
| Email drafts but never sends | Check `openclaw tools status agentmail`; confirm the `--inbox` address matches your verified inbox. |
| Tool works from CLI but not Telegram | The channel profile may deny it. `openclaw channel show telegram` and adjust allow/deny. |

## Exercise / Challenge
Build a "supplier compare" task: use Firecrawl to fetch the A4-paper price from **two** supplier sites, have the agent tabulate them, pick the cheaper in-stock option, and email yourself a one-paragraph recommendation via AgentMail. Then define a `research` posture on the Telegram channel that allows only `firecrawl`, `web_search`, and `browser` (no `exec`, no `fs.write`) so customer-facing research can never touch the filesystem — you will reuse this exact separation for the Research agent in Lab 24.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
