# Lab 23 — Security

## Objective
Harden the Nimbus Supplies deployment before it faces real customers: protect API keys, restrict **who** can DM the bot, sandbox dangerous tools, and keep an audit trail. You will apply **least privilege** — each channel gets only the tools it needs, and strangers cannot burn your quota.

## Prerequisites
- Labs 15–22 completed (a public-facing Telegram bot is ideal for this lab).
- Your own Telegram/WhatsApp user ID (get it with `/whoami` — Lab 20).

## Estimated Time
30 minutes

## 📺 Reference Video
[OpenClaw reference playlist](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J)

## Steps

1. **Secure API keys — never hardcode or commit them.** Store keys once as environment variables.

   **macOS / Linux** — append to `~/.zshrc` or `~/.bashrc`:

   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   export FIRECRAWL_API_KEY="fc-..."
   export AGENTMAIL_API_KEY="..."
   ```

   **Windows (PowerShell)** — permanent user variable:

   ```powershell
   [Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY","sk-ant-...","User")
   ```

   Confirm keys are **not** sitting in cleartext in the config:

   ```bash
   ls -la ~/.openclaw/
   cat ~/.openclaw/config.toml | grep -i key    # should show references, not raw keys
   ```

2. **Restrict who can DM the bot (allowlists).** By default anyone who finds your Telegram bot can message it. Lock it to known users:

   ```bash
   openclaw channel set telegram \
     --allow-users 12345678,87654321 \
     --pair-mode allowlist
   ```

   Or just ask the agent: "Only allow Telegram users 12345678 and 87654321 to message you; block everyone else"

   For WhatsApp, allow specific numbers:

   ```bash
   openclaw channel set whatsapp \
     --allow-numbers +6591234567,+6598765432
   ```

   In group chats, only respond when mentioned:

   ```bash
   openclaw channel set telegram --group-policy mention-only
   ```

3. **Apply tool deny lists (least privilege per channel).** A customer-facing channel has no business running shell commands or deleting files:

   ```bash
   openclaw channel set telegram --deny exec,fs.write,fs.delete
   openclaw channel set telegram --allow group:web
   openclaw channel set telegram --profile messaging
   openclaw channel show telegram | grep -E "(allow|deny|profile)"
   ```

   Or just ask the agent: "On Telegram, deny shell exec and any file writes or deletes"

4. **Tighten the code-execution sandbox.** The `exec` / Python tools run sandboxed — cap time, memory, and network:

   ```bash
   openclaw tools config exec \
     --timeout 10s \
     --memory 256mb \
     --network deny

   openclaw tools config python \
     --timeout 30s \
     --memory 512mb \
     --network deny
   ```

   Or just ask the agent: "Cap your exec sandbox at 10 seconds, 256MB memory and no network access"

   

5. **Review the audit log.** Every tool call, model call, and channel event is logged:

   ```bash
   openclaw gateway logs --tail 100
   openclaw gateway logs --filter tool=exec
   openclaw gateway logs --since 1h --filter level=warn
   openclaw gateway logs --export ~/openclaw-audit-$(date +%F).log
   ```

   Review weekly. Investigate anything unexpected — unknown user IDs, blocked tool attempts, repeated auth failures.

6. **Rotate provider keys on a schedule (e.g. every 90 days).**
   1. Generate a new key in the provider dashboard.
   2. Update the environment variable.
   3. Restart the gateway: `openclaw gateway restart`.
   4. Confirm `openclaw model test` still works.
   5. **Revoke** the old key in the provider dashboard.

## Verification / Expected Output
- `cat ~/.openclaw/config.toml` does **not** contain raw API keys.
- A user **not** on your Telegram allowlist gets a polite "not authorized" reply (or no reply, per policy).
- `openclaw channel show telegram` lists your `deny: exec, fs.write, fs.delete` and `profile: messaging`.
- `openclaw gateway logs --filter tool=exec` shows blocked attempts when someone tries to run shell exec on a locked channel.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| The allowlist blocks **you** | Add your own user ID first (from `/whoami`), then re-apply. |
| A tool deny does not take effect | `openclaw gateway restart` — channel config is cached. |
| Logs grow huge | Rotate them: `openclaw gateway logs rotate --keep 7`. |
| Key still visible in an old shell | It was exported earlier; open a fresh terminal after moving it to `~/.zshrc`. |
| Sandbox change ignored | Restart the gateway; confirm with `openclaw tools status exec`. |

## Exercise / Challenge
Write a one-page **threat model** for the Nimbus Supplies bot: who could abuse it, the worst-case outcome, and the mitigation you applied for each. Then write a small script `check-nimbus-security.sh` that (a) fails if any provider key appears in `~/.openclaw/config.toml`, (b) fails if any channel has `exec` enabled with no allowlist, and (c) prints the currently-allowed users per channel. You will re-run this check across all three agents in the Lab 24 capstone.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
