# Lab 3 — Human-in-the-Loop Publishing & Community Care (Telegram + Cron)

**Day 1 · Topic 2 · 45 min · Human–agent collaboration · LO2**

> Put the agent on Telegram, make it ask for your APPROVE before anything goes public, schedule it every morning, and let it triage comments while escalating the risky ones to you.

## Goal
Design a human-in-the-loop workflow — approval gates, escalation rules and scheduled automation — and relate the design to operational efficiency and risk (LO2).

## The business scenario
The campaign is planned; now it must run every day without you babysitting it. Each morning Mia sends you the day's post and image on Telegram. Only when you reply APPROVE does she publish it to the brand's Telegram channel and log it. She also works through the comment inbox — answering simple questions, but escalating food-safety, allergy, legal, billing, media and halal questions to you with personal data masked.

## You will deliver
- A Telegram bot connected to Hermes (your private chat with Mia)
- A 'Kopi Kaki Feed (Training)' Telegram channel where approved posts are published
- outputs/lab03/approval-log.csv — every APPROVE / EDIT / REJECT decision
- A daily 09:00 cron job that sends the day's post for approval
- outputs/lab03/moderation-queue.csv + an escalation summary on Telegram

## Who does what
- **Agents:** 1 Hermes agent (Mia) on the messaging gateway + cron scheduler
- **You (the human):** Approve, edit or reject every post; decide every escalation

## Before you start
- Labs 1–2 complete: outputs/lab02/content-calendar-v2.csv exists
- A Telegram account on your phone or desktop

## Concepts in action
- Human-in-the-loop (approve before acting) vs human-on-the-loop (monitor and intervene)
- Escalation rules turn policy into agent behaviour
- Cron = proactive agent (it starts work without being asked)
- Approval modes (smart / manual / off) for risky terminal commands

## Lab files (`data/`)

| File | What it is |
|---|---|
| `AGENTS.md` | Company context Hermes loads automatically |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `social-comments.csv` | 20 social comments incl. complaints, legal, PII, spam |
| `templates/approval-log.csv` | Template |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-03-Instructions.pdf`](LAB-03-Instructions.pdf).

## Steps

### 1. Create your Telegram bot and find your user ID
In Telegram: open @BotFather → /newbot → choose a name (e.g. 'Mia Kopi Kaki') → copy the token. Open @userinfobot to get your numeric user ID. Keep the token secret. (Shortcut: the dashboard's Messaging → Telegram page has a 'Create with QR' button.)

### 2. Connect Telegram to Hermes and start the gateway
Run the messaging setup, choose Telegram, paste the token and your user ID as the only allowed user. Then run the gateway (leave this terminal open).

```bash
hermes gateway setup
hermes gateway run      # or: hermes gateway install && hermes gateway start
```

✅ **Expected:** Send 'hi' to your bot in Telegram — Mia replies.

### 3. Create the brand channel (the 'publish' destination)
In Telegram create a new channel 'Kopi Kaki Feed (Training)', add your bot as an administrator with permission to post. Then list targets to find its ID.

```bash
hermes send --list telegram
```

✅ **Expected:** Your channel appears as telegram:<channel_id>. Copy it.

### 4. Make risky commands ask first
Create this lab's output folder and approval log, and switch approvals to manual so every dangerous terminal command pauses for you. Be clear about what this does and does not cover: approval modes gate risky TERMINAL commands; the publishing gate in this lab is a rule the agent follows (prompt-enforced, written into AGENTS.md). Lab 4 shows a runtime-enforced gate (a blocked task only you can release).

```bash
cp -Rn data/* ~/kopi-kaki/
mkdir -p ~/kopi-kaki/outputs/lab03
cp ~/kopi-kaki/templates/approval-log.csv ~/kopi-kaki/outputs/lab03/approval-log.csv
hermes config set approvals.mode manual
```

### 5. Run one approval cycle by hand
**Prompt** — paste into *Telegram → your bot*:

```text
Approval workflow for #ShiokColdBrew (standing rule - add it to ~/kopi-kaki/AGENTS.md too):
1. Take the next post with status "draft" from ~/kopi-kaki/outputs/lab02/content-calendar-v2.csv, set its status to "pending-approval" and send it to me here with its post id, image, platform and date. End with: Reply APPROVE <post_id>, EDIT <post_id>: <changes> or REJECT <post_id>.
2. Whenever I reply APPROVE <post_id>, read that row from the CSV - it must say "pending-approval" - then post the caption and image to telegram:<channel_id>, set the status to "published" and append a row to ~/kopi-kaki/outputs/lab03/approval-log.csv.
3. EDIT: apply my changes, re-check with kopi-brand-voice, keep "pending-approval" and send it again. REJECT: set "rejected" and log it.
4. Never publish a row that is not "pending-approval" and never without my APPROVE.
```

✅ **Expected:** You receive the draft with its post id; after APPROVE <post_id> it appears in the channel, the CSV says published and approval-log.csv has a row.

### 6. Schedule it every morning at 09:00
Turn step 1 of the workflow into a proactive agent. A cron job runs in its own fresh session, so it must NOT try to publish: it only marks the next post 'pending-approval' and sends it to you. Your reply goes to your normal chat with Mia, which reads the CSV state (step 2 of the rule) and publishes. The state in the CSV is what connects the two sessions. Copy the job id from `hermes cron list`.

```bash
hermes cron create "0 9 * * *" "Proposal only - never publish. Take the next post with status draft from ~/kopi-kaki/outputs/lab02/content-calendar-v2.csv, set it to pending-approval and send me its post id, image, platform, date and caption, ending with: Reply APPROVE <post_id>, EDIT <post_id>: <changes> or REJECT <post_id>." --name daily-post-approval --deliver telegram
hermes cron list
hermes cron run <job_id>
```

✅ **Expected:** The job is listed; the test run sends you a draft; replying APPROVE <post_id> in your chat with Mia publishes it.

### 7. Triage the comment inbox with escalation rules
**Prompt** — paste into *Telegram → your bot (or Hermes chat in ~/kopi-kaki)*:

```text
Triage ~/kopi-kaki/social-comments.csv using compliance-rules.md.
For each comment decide: REPLY (safe FAQ), IGNORE (spam) or ESCALATE (food safety, allergy, legal threat, billing/refund, media enquiry, halal question, health claim question, anything uncertain).
- For REPLY: draft a reply in the kopi-brand-voice skill.
- For ESCALATE: do NOT draft a public reply. Mask all personal data (names, phone numbers) and recommend the next step.
Save outputs/lab03/moderation-queue.csv (comment_id, decision, reason, draft_reply) and send me an escalation summary here.
```

✅ **Expected:** 7 escalations summarised on Telegram with phone numbers masked; safe replies drafted.

### 8. Decide like a manager
Reply on Telegram with your decision for each escalation (e.g. 'C06: call the customer today, ops to inspect Bishan'). Approve the batch of FAQ replies. Discuss: which decisions must always stay human, and which could move to human-on-the-loop later?

## Verification / checkpoint
- [ ] Bot replies only to your allow-listed user ID
- [ ] Every published post has an APPROVE row in approval-log.csv and its CSV status went pending-approval → published
- [ ] `hermes cron list` shows daily-post-approval
- [ ] C03, C06, C09, C11, C15, C16, C18 are ESCALATE with personal data masked

**Checkpoint:** Nothing reaches the channel without an APPROVE in approval-log.csv; all 7 risky comments are escalated, none answered.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Bot silent | Is `hermes gateway run` still running? Check `hermes gateway status` and that your user ID is allowed. |
| Cannot post to channel | Make the bot an admin of the channel with 'Post messages' permission. |
| Cron never fires | The gateway (or `hermes gateway install`) must be running for the scheduler; check `hermes cron status`. |
| Agent published without asking | Tighten the prompt: 'Never publish without the literal reply APPROVE' and keep approvals.mode manual. |

## Stretch challenge
Add a second gate: a post that mentions a price or promo must be approved twice (you and a colleague's Telegram ID). How would you express that rule, and what does it cost in speed?

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
