# Lab 17 — Channels

## Objective
Give customers a way to reach the Nimbus Supplies agent. You will create a **Telegram bot** end-to-end via BotFather, pair a **WhatsApp** number by QR, and run **both channels at once** through a single OpenClaw gateway so the same agent answers on either platform.

## Prerequisites
- Labs 15–16 completed (OpenClaw running, a model connected and passing `openclaw model test`).
- A free **Telegram** account.
- A phone with **WhatsApp** installed (for QR pairing).

## Estimated Time
30–40 minutes

## 📺 Reference Video
[OpenClaw reference playlist](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J)

## Steps

1. **Create a Telegram bot with BotFather.**
   1. Open Telegram and search for **@BotFather**.
   2. Send `/newbot`.
   3. Enter a **display name** (e.g. `Nimbus Supplies Assistant`).
   4. Enter a **username** — must be unique and **end in `_bot`** (e.g. `nimbus_supplies_bot`).
   5. BotFather replies with an HTTP API **token** like `123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`. **Copy it.**

   

2. **Register and start the Telegram channel.**

   ```bash
   openclaw channel add telegram --token 123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
   openclaw channel start telegram
   ```

   Or just ask the agent: "Connect Telegram using the bot token I got from BotFather"

   Or just ask the agent: "Start the Telegram channel and confirm it is live"

3. **Test Telegram.** In Telegram, search for your bot's username and send:

   > Hi, do you supply recycled A4 paper for Nimbus Supplies?

   The agent should reply using the model you connected in Lab 16.

4. **Add and start the WhatsApp channel.**

   ```bash
   openclaw channel add whatsapp
   openclaw channel start whatsapp
   ```

   Or just ask the agent: "Add WhatsApp as a channel and show me the pairing QR code"

   Or just ask the agent: "Start the WhatsApp channel so I can scan the QR code"

   A QR code prints in your terminal.

5. **Pair WhatsApp by scanning the QR.** On your phone: **WhatsApp → Settings → Linked Devices → Link a Device**, then scan the QR code shown in the terminal. Wait for `whatsapp: connected` in the OpenClaw log.

   > WhatsApp keeps a stateful session on disk at `~/.openclaw/whatsapp/`. Do **not** delete that folder unless you intend to re-pair.

   

6. **Confirm both channels are running at the same time.** One gateway hosts many channels — the same Nimbus Supplies agent now answers on both.

   ```bash
   openclaw channel list
   openclaw gateway status
   ```

   Or just ask the agent: "Which channels are you listening on right now?"

7. **Inspect and manage a channel.** Useful day-to-day commands:

   ```bash
   openclaw channel show telegram
   openclaw channel restart whatsapp   # e.g. after the QR expires
   ```

## Verification / Expected Output
- `openclaw channel list` shows **telegram** and **whatsapp**, both `running`.
- A message to the **Telegram** bot gets an agent reply.
- A message to the **linked WhatsApp** account gets an agent reply.
- `openclaw gateway status` shows both channels connected.

  

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Telegram bot never replies | Re-check the token; confirm the model works with `openclaw model test`; ensure `openclaw channel start telegram` ran. |
| "409 Conflict" from Telegram | The same bot token is polling from another machine/instance. Stop the other one — one token, one gateway. |
| WhatsApp QR expired before scanning | `openclaw channel restart whatsapp` to print a fresh QR. |
| WhatsApp disconnects after a while | Your phone must stay online periodically. Re-pair only if `~/.openclaw/whatsapp/` was deleted. |
| Only one channel responds | `openclaw channel list` — start the missing one; check `openclaw gateway status`. |
| Bot replies but ignores context | Memory/persistence is covered in Lab 22; for now each channel shares the same model. |

## Exercise / Challenge
Add a **second** Telegram bot with a different username (e.g. a dedicated `nimbus_orders_bot`) and confirm both bots plus WhatsApp run simultaneously through the one OpenClaw gateway. Then send the same question — "What are your opening hours?" — on all three and confirm the same agent answers consistently. This multi-channel front door is exactly what the Sales agent will own in the Lab 24 capstone.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
