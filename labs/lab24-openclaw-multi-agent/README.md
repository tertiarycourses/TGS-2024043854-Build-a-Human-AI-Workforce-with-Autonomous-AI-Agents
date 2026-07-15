# Lab 24 — Multi-Agent Workforce

## Objective
Bring everything together. Split the single Nimbus Supplies agent into **three cooperating agents** — a **Sales** agent (customer-facing on Telegram/WhatsApp), a **Research** agent (supplier scouting with Firecrawl), and an **Ops** agent (email, quotes, nightly crons) — each with least-privilege tools, and run one end-to-end business scenario across all three. This is the graded capstone for the OpenClaw module.

## Prerequisites
- Labs 15–23 completed. You should have: a working model (Lab 16), Telegram + WhatsApp (Lab 17), the `nimbus-quote` skill (Lab 18), Firecrawl + AgentMail (Lab 19), crons + heartbeat (Lab 21), memory (Lab 22), and security lockdown (Lab 23).

## Estimated Time
50–60 minutes

## 📺 Reference Video
[OpenClaw Multi-Agent setup](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J&index=1)

## Design: three agents, three roles

| Agent | Front door | Tools it may use | Job |
| --- | --- | --- | --- |
| **Sales** | Telegram + WhatsApp | `group:web`, `nimbus-quote` skill (no `exec`, no `fs.write`) | Greet customers, answer questions, capture orders, hand quotes to Ops |
| **Research** | CLI + one private Telegram bot | `firecrawl`, `web_search`, `browser` only | Vet suppliers, compare prices, report findings |
| **Ops** | Cron-driven + AgentMail | `agentmail`, `fs` (write quotes/reports), crons | Send quotes/emails, run nightly reports, restock reminders |

> **Important — verify the multi-agent commands for your version.** OpenClaw's exact syntax for defining/running multiple named agents (e.g. an `openclaw agent …` command family) can differ by release. The steps below show the **intended structure**; confirm the precise sub-commands at <https://docs.openclaw.ai/> before running. Where native multi-agent commands are unavailable, use the **fallback** in Step 6 (separate config profiles / instances), which relies only on primitives verified in Labs 15–23.

## Steps

1. **Create three named agents.** Attempt the native multi-agent path first (confirm exact syntax in the docs):

   ```bash
   openclaw agent create sales
   openclaw agent create research
   openclaw agent create ops
   openclaw agent list
   ```

   If `openclaw agent` is not available in your build, skip to Step 6 for the verified fallback and treat "agent" as "profile/instance" throughout.

2. **Give each agent least-privilege tools** (mirrors Lab 19/23 allow-deny, applied per agent):

   ```bash
   # Sales — web + quoting only, no shell, no filesystem writes
   openclaw agent set sales --allow group:web --deny exec,fs.write,fs.delete

   # Research — scraping only
   openclaw agent set research --allow firecrawl,web_search,browser --deny exec,fs.write

   # Ops — email + files, no public channel exposure
   openclaw agent set ops --allow agentmail,group:fs
   ```

3. **Attach channels to the right agents.**

   ```bash
   # Customer traffic goes to Sales
   openclaw channel set telegram --agent sales
   openclaw channel set whatsapp --agent sales

   # A private research bot for the operator (see Lab 17 for creating a 2nd bot)
   openclaw channel add telegram --token <RESEARCH_BOT_TOKEN>
   openclaw channel set <research-bot> --agent research
   ```

4. **Give each agent the right skill/memory.** Sales uses `nimbus-quote` and the customer memory from Lab 22; Research uses `nimbus-supplier-brief` (Lab 18 exercise). Install/enable as needed:

   ```bash
   openclaw skills list
   ```

5. **Wire cooperation between agents.** The simplest, robust hand-off uses the tools you already have:
   - **Sales → Ops:** when Sales captures an order, it asks Ops (via a shared note file or an AgentMail message) to produce and send the quote.
   - **Ops → Research:** when a price is unknown ("TBC"), Ops asks Research to look it up with Firecrawl.
   - **Research → Ops:** Research replies with the price; Ops finalises the quote email.

   ```bash
   # Ops nightly consolidation cron (from Lab 21, now owned by Ops)
   openclaw cron create \
     --schedule "0 21 * * *" \
     --prompt "Compile today's Nimbus Supplies orders and quotes sent, and list anything waiting on Research." \
     --channel telegram \
     --name ops-nightly-report
   ```

6. **Fallback (fully verified) — run agents as separate profiles/instances.** If native multi-agent commands are not in your build, model each agent as its own OpenClaw configuration using only Lab 15–19 primitives:
   - **Sales** = your main instance with Telegram/WhatsApp, `--profile messaging`, deny `exec,fs.write` (Lab 23).
   - **Research** = a second instance pointed at a separate config dir with only Firecrawl/web tools enabled:

     ```bash
     OPENCLAW_HOME=~/.openclaw-research openclaw onboard
     OPENCLAW_HOME=~/.openclaw-research openclaw tools enable firecrawl --api-key "$FIRECRAWL_API_KEY"
     ```

     > `OPENCLAW_HOME` (or the equivalent config-dir flag) is the mechanism to run isolated instances — **confirm the exact variable/flag name at <https://docs.openclaw.ai/>**.
   - **Ops** = a third instance with AgentMail + filesystem + the crons from Lab 21.

   The three instances cooperate through **AgentMail** (email each other) and a **shared folder** (e.g. `~/nimbus-shared/`) that Ops can read/write.

7. **Run the end-to-end capstone scenario.** From a customer's Telegram, trigger the whole workflow:

   > Hi Nimbus Supplies — I'm Mei from Acme Cafe. I need 10 reams of recycled A4 paper and 5 boxes of black pens. What's your best price and when can you deliver?

   Expected chain:
   1. **Sales** greets Mei, recalls Acme's preferences from memory (recycled paper, Tuesday delivery — Lab 22), and captures the order.
   2. Sales hands the order to **Ops**, which starts the `nimbus-quote`. The pen price is unknown → marked **TBC**.
   3. Ops asks **Research** to fetch the current pen price via Firecrawl.
   4. Research replies with the price; **Ops** finalises the itemised quote (with GST) and emails it to Acme via AgentMail.
   5. That night, the **ops-nightly-report** cron summarises the day, including Mei's order.

   

### 8. The natural-language way
You can skip the CLI entirely and simply ask the agent: *"Spawn two sub-agents to research our top two competitors in parallel, then compare their pricing"*.

## Verification / Expected Output
- Three agents (or three isolated instances) exist and each has a **distinct, least-privilege** tool set — Sales cannot run `exec`, Research cannot write files, Ops is not exposed on a public channel.
- The customer message on Telegram produces a **real quote email** that combines: memory (recycled paper), a skill (`nimbus-quote`), a Research price lookup (Firecrawl), and AgentMail delivery.
- The nightly cron posts a summary that references the same order.
- `openclaw gateway logs` (per instance) shows the hand-offs and no blocked-tool surprises.

## Capstone Checklist
- [ ] Sales agent answers customers on **both** Telegram and WhatsApp.
- [ ] Research agent can scrape supplier prices but **cannot** write files or run shell.
- [ ] Ops agent sends email via AgentMail and owns the nightly cron; it is **not** on a public channel.
- [ ] Customer memory (Lab 22) is applied automatically in the quote.
- [ ] The `nimbus-quote` skill (Lab 18) produces the itemised, GST-inclusive quote.
- [ ] Heartbeat is healthy and the gateway auto-restarts (Lab 21).
- [ ] Security: allowlists on the customer channel, keys not in cleartext, deny lists enforced (Lab 23).
- [ ] One full customer request runs end-to-end across all three agents.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `openclaw agent` command not found | Your build may not have native multi-agent mode. Use the Step 6 fallback (isolated instances) and confirm at <https://docs.openclaw.ai/>. |
| Wrong agent answers a channel | Re-check `openclaw channel set <name> --agent <agent>` (or which instance owns which channel token). One token, one owner. |
| Agents don't hand off | The hand-off relies on a shared medium — confirm AgentMail works for all instances and the shared folder is readable/writable by Ops. |
| Research agent writes files anyway | Its deny list is not applied — re-run the `--deny fs.write` step and restart that instance. |
| Two instances fight over one channel | Each Telegram token must belong to exactly one agent/instance (409 Conflict otherwise). |
| Isolated instance ignores `OPENCLAW_HOME` | Confirm the correct config-dir variable/flag for your version in the docs. |

## Exercise / Challenge
Add a **fourth** agent — **Finance** — that reconciles the day's quotes into a simple CSV and emails a weekly revenue summary, with read-only access to the shared folder and no ability to message customers. Then run your `check-nimbus-security.sh` from Lab 23 against **every** agent/instance and confirm all pass. Finally, write a half-page reflection: which tasks genuinely benefited from splitting into multiple agents, and where a single agent would have been simpler? That trade-off judgement is the core skill this course is assessing.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
