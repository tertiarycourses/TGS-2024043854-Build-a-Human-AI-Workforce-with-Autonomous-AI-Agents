# Lab 18 — Skills

## Objective
Learn what OpenClaw **skills** are, install and remove skills from the [skills.sh](https://skills.sh/) registry, invoke them from chat, and build a **custom skill** for Nimbus Supplies so the agent handles a recurring back-office task (drafting a customer quote) the same way every time.

## Prerequisites
- Labs 15–17 completed (OpenClaw running, a model connected, at least one live channel to test from).

## Estimated Time
30–40 minutes

## Concept Recap
A **skill** is a reusable, named capability: a prompt plus optional tools and examples that the agent can trigger by name. Think of skills as shortcuts that give consistent, repeatable behaviour — `web-research`, `code-review`, `self-improvement`, or a company-specific one like `nimbus-quote`.

## 📺 Reference Video
[OpenClaw reference playlist](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J)

## Steps

1. **List the skills currently installed.**

   ```bash
   openclaw skills list
   ```

   

2. **Install a few useful skills from the registry.** Skills come from <https://skills.sh/>:

   ```bash
   openclaw skills add web-research --source skills.sh
   openclaw skills add self-improvement --source skills.sh
   ```

   Confirm one installed correctly:

   ```bash
   openclaw skills show self-improvement
   ```

3. **Invoke a skill from chat.** In your Telegram or WhatsApp channel, send:

   ```
   /skill web-research "Who are the main office-supplies wholesalers in Singapore?"
   ```

   The agent runs the skill and returns a structured answer. The self-improvement skill (`/skill self-improvement`) asks the agent to reflect on recent conversations and propose a memory update — approve or reject it.

4. **Remove a skill you do not need** (keeps the agent focused and safe):

   ```bash
   openclaw skills remove self-improvement
   ```

5. **Refresh the registry index** if a skill you expect is missing:

   ```bash
   openclaw skills update
   ```

6. **Build a custom Nimbus Supplies skill.** Skills live under `~/.openclaw/skills/`. Create a folder and a skill definition. (File layout is shown here as a documented example — confirm the exact schema for your version at <https://docs.openclaw.ai/> before relying on advanced fields.)

   ```bash
   mkdir -p ~/.openclaw/skills/nimbus-quote
   ```

   Create `~/.openclaw/skills/nimbus-quote/skill.md` with your editor:

   ```markdown
   ---
   name: nimbus-quote
   description: Draft a polite, itemised price quote for a Nimbus Supplies customer.
   ---

   You are the Nimbus Supplies quoting assistant. When invoked, ask for (or read
   from the message) the customer name, the items requested, and quantities. Then
   produce a short, friendly quote with:
   - a one-line greeting addressed to the customer
   - an itemised table: item | qty | unit price (SGD) | line total
   - a subtotal, 9% GST line, and grand total
   - standard terms: "Prices valid 14 days. Delivery within 3 business days in SG."
   If a unit price is unknown, clearly mark it "TBC — confirm with supplier" rather
   than inventing a number.
   ```

7. **Register and test the custom skill.**

   ```bash
   openclaw skills list                 # confirm nimbus-quote appears
   openclaw gateway restart             # reload skills if it is not picked up
   ```

   Then from a channel:

   ```
   /skill nimbus-quote "Customer: Acme Cafe. 10 reams recycled A4 paper, 5 boxes black pens."
   ```

## Verification / Expected Output
- `openclaw skills list` shows the registry skills you added plus your custom **nimbus-quote**.
- `/skill web-research "…"` runs end-to-end and returns an answer in chat.
- `/skill nimbus-quote "…"` produces an itemised quote with a GST line and the standard terms, and marks any unknown price as "TBC" instead of guessing.

  

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `skill 'foo' not found` | `openclaw skills update` to refresh the registry index, then retry the add. |
| Skill installs but `/skill` does not trigger | Restart the gateway: `openclaw gateway restart`. |
| Custom skill not listed | Check the folder path `~/.openclaw/skills/nimbus-quote/` and the front-matter `name:`; restart the gateway. |
| Self-improvement loops endlessly | Cap it: `openclaw skills config self-improvement --max-iterations 3`. |
| Not sure about the skill file schema | Confirm the current format at <https://docs.openclaw.ai/> — schema fields can change between versions. |

## Exercise / Challenge
Build a second custom skill, `nimbus-supplier-brief`, that takes a supplier name and returns a 5-bullet vetting summary (product range, minimum order, lead time, payment terms, one risk flag). Install one more skill from skills.sh that you would genuinely use at work, and write two sentences on the task it saves you. Keep both skills — the Research agent will lean on `nimbus-supplier-brief` in the Lab 24 capstone.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
