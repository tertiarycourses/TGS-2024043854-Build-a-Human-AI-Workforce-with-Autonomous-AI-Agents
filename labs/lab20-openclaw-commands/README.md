# Lab 20 — Commands

## Objective
Become fluent in the two ways you drive OpenClaw every day: the **CLI commands** (`config`, `model`, `doctor`, `gateway`, `channel`, `tools`, `skills`, `cron`) and the **in-chat slash commands** customers and operators use inside a channel. You will build a personal quick-reference table for running the Nimbus Supplies back office.

## Prerequisites
- Labs 15–19 completed.

## Estimated Time
30 minutes

## 📺 Reference Video
[OpenClaw reference playlist](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J)

## Steps

1. **`openclaw config` — read and change settings.**

   ```bash
   openclaw config list                        # show all settings
   openclaw config get model                   # get one setting
   openclaw config set model anthropic/claude-opus-4-7
   openclaw config edit                         # open the config file in $EDITOR
   ```

2. **`openclaw model` — manage the brain.**

   ```bash
   openclaw model list
   openclaw model current
   openclaw model use deepseek/deepseek-v4
   openclaw model test
   ```

3. **`openclaw doctor` — health check (with auto-fix).**

   ```bash
   openclaw doctor
   openclaw doctor --fix
   ```

4. **`openclaw gateway` — control the daemon that runs everything.**

   ```bash
   openclaw gateway status
   openclaw gateway start
   openclaw gateway stop
   openclaw gateway restart
   openclaw gateway logs --tail 50
   openclaw gateway install     # install daemon (LaunchAgent / systemd / Task Scheduler)
   ```

5. **`openclaw channel` — manage the front doors.**

   ```bash
   openclaw channel list
   openclaw channel add telegram --token <TOKEN>
   openclaw channel start whatsapp
   openclaw channel show telegram
   openclaw channel restart whatsapp
   openclaw channel remove telegram
   ```

6. **`openclaw tools` and `openclaw skills` — capabilities.**

   ```bash
   openclaw tools list
   openclaw tools list --enabled
   openclaw tools status agentmail

   openclaw skills list
   openclaw skills add web-research --source skills.sh
   openclaw skills remove web-research
   ```

7. **In-chat slash commands.** These work inside any channel (Telegram, WhatsApp, CLI chat). Try each from your Nimbus Supplies bot:

   | Slash Command | Purpose |
   | --- | --- |
   | `/help` | List all available slash commands |
   | `/model <name>` | Switch model **for this conversation only** |
   | `/skill <name> [args]` | Run an installed skill (e.g. `/skill nimbus-quote "…"`) |
   | `/tools` | List tools the agent may use in this channel |
   | `/clear` | Clear the conversation history |
   | `/memory` | View / edit the agent's memory for this user |
   | `/whoami` | Show your user ID, channel, profile, and current model |
   | `/stop` | Cancel the current generation |

   

8. **Watch it work live.** In one terminal, follow the logs; in the channel, send a message and observe the corresponding lines:

   ```bash
   openclaw gateway logs --follow
   ```

## Verification / Expected Output
- You can switch the model both from chat (`/model deepseek/deepseek-v4`) **and** globally from the CLI (`openclaw model use …`), and you understand `/model` is per-conversation while the CLI sets the default.
- `/whoami` returns your Telegram/WhatsApp user ID (you will need it for the Lab 23 allowlist).
- `openclaw gateway logs --follow` streams live activity while you chat.
- `/help` lists at least the eight commands above.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `/skill foo` says "unknown skill" | `openclaw skills list` — install it if missing. |
| `/model` change does not persist to the next chat | Expected — `/model` is per-conversation. Use `openclaw model use …` for the global default. |
| Gateway logs are empty | Ensure the gateway is running: `openclaw gateway status`. |
| `openclaw config set` seems ignored | Some settings need a restart: `openclaw gateway restart`. |
| `/whoami` shows no user ID | Send it from the actual channel (not CLI) so the platform user ID is present. |

## Exercise / Challenge
Create a one-page markdown cheat sheet of the **ten** commands you would use most to run Nimbus Supplies day to day (mix CLI and slash), save it to `~/.openclaw/notes/cheatsheet.md`, and pin it somewhere visible. Then run a "morning routine": `openclaw doctor`, `openclaw gateway status`, `openclaw channel list`, and `/whoami` in each channel — this is the exact daily health check you will formalise into a heartbeat in Lab 21.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
