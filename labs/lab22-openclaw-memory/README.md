# Lab 22 — Memory & Context

## Objective
Give the Nimbus Supplies agent a memory so it recalls customer preferences across conversations instead of starting cold every time. You will use the in-chat `/memory` command, inspect where OpenClaw persists state under `~/.openclaw/`, and run a teach-and-recall test — tell the agent a customer's standing preference, then confirm it applies that preference in a later, separate conversation.

## Prerequisites
- Labs 15–21 completed (at least one live channel; `/whoami` working).

## Estimated Time
25–30 minutes

## Concept Recap
OpenClaw keeps two kinds of state you care about here:
- **Conversation context** — the recent messages in the current chat (cleared with `/clear`).
- **Persistent memory** — durable facts the agent remembers about a user across chats, viewed/edited with `/memory` and stored on disk under `~/.openclaw/`.

> The exact on-disk filenames for memory can change between versions. Treat the paths below as inspection targets, and confirm specifics at <https://docs.openclaw.ai/>. Do **not** hand-edit these files while the gateway is running.

## 📺 Reference Video
[OpenClaw reference playlist](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J)

## Steps

1. **See what OpenClaw stores on disk.**

   ```bash
   ls -la ~/.openclaw/
   ```

   Or just ask the agent: "Show me what you store in your ~/.openclaw state folder"

   You will see directories such as `auth/` (Lab 16 credentials), `whatsapp/` (Lab 17 session), `skills/` (Lab 18), and memory/state directories. Explore, but do not edit yet:

   ```bash
   du -sh ~/.openclaw/*
   ```

2. **Inspect your current memory from chat.** In your Telegram or WhatsApp bot:

   ```
   /memory
   ```

   On a fresh setup this is empty or minimal. It is scoped to **you** (your channel user ID from `/whoami`).

3. **Teach the agent a durable customer preference.** Still in chat, send a plain-language instruction:

   > Remember this for future chats: our customer Acme Cafe always wants **recycled** A4 paper (never standard), delivery on **Tuesdays only**, and quotes addressed to **Mei from Acme**.

   Then confirm it was captured:

   ```
   /memory
   ```

   The new facts should appear. If your version proposes a memory update for approval, approve it.

4. **Clear the conversation to prove it is real memory, not just context.**

   ```
   /clear
   ```

   `/clear` wipes the short-term conversation history but must **not** erase persistent memory.

5. **Recall in a fresh conversation.** In the now-cleared chat, ask something that requires the remembered facts:

   > Draft a quote for Acme Cafe: 10 reams of A4 paper and 5 boxes of black pens.

   A correct agent should automatically choose **recycled** A4, note **Tuesday** delivery, and address the quote to **Mei** — without you repeating any of it. (This pairs perfectly with the `nimbus-quote` skill from Lab 18.)

   

6. **Edit or correct a memory.** If a preference changes, update it in natural language and re-check:

   > Update your memory: Acme Cafe now accepts delivery on Tuesdays **or** Thursdays.

   ```
   /memory
   ```

7. **Back up memory before major changes** (memory lives under `~/.openclaw/`, so the Lab 15 backup habit applies):

   ```bash
   mkdir -p ~/openclaw-backup-$(date +%F)
   cp -R ~/.openclaw/ ~/openclaw-backup-$(date +%F)/openclaw-state 2>/dev/null || true
   ```

   Or just ask the agent: "Back up all your memory and state to a dated folder in my home directory"

## Verification / Expected Output
- `/memory` shows the customer preferences you taught after Step 3.
- After `/clear`, `/memory` still shows those preferences (short-term context cleared, long-term memory retained).
- A fresh quote request for Acme Cafe automatically applies recycled paper, Tuesday delivery, and the correct recipient name.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `/memory` is always empty | Confirm you are messaging from a real channel (memory is per user ID; check `/whoami`). |
| Agent forgets after `/clear` | It was only in conversation context, not saved. Re-teach and explicitly say "remember this for future chats". |
| Memory bleeds between customers | Memory is keyed to the chat user, not the customer. For per-customer facts, keep them explicit in the message or use a skill (Lab 18). |
| Edited a memory file by hand and things broke | Stop the gateway before touching files; restore from your backup: `openclaw gateway stop` then copy the folder back. |
| Not sure where memory is stored | Inspect `~/.openclaw/` and confirm the current layout at <https://docs.openclaw.ai/>. |

## Exercise / Challenge
Teach the agent preferences for **two** different customers, then run separate quote requests and confirm it applies the right preferences to each without mixing them up. Next, decide a memory-hygiene policy for Nimbus Supplies: what should the agent remember (delivery days, contact names) versus what it must **not** persist (payment details, personal data) — write it as three bullet rules and add them to your `nimbus-quote` skill prompt so memory and skills reinforce the same policy. This governance mindset carries straight into Lab 23.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
