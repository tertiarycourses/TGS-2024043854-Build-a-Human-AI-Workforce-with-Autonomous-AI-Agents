# Lab 10 — Security

## Objective
LO4: Secure the agent with isolation, secrets, and approvals. You will harden **Athena** with defense in depth: restrict who can message the agent (default deny), run risky work in an isolated terminal backend, manage secrets safely, and require approval before sensitive actions — applying least privilege throughout.

## Prerequisites
- **Lab 1–9 complete** — Hermes running; docker backend understood (Lab 8).
- Docker installed and running (for the sandboxed backend).

## Estimated Time
35–45 minutes

## 📺 Reference Video
[Security](https://www.youtube.com/watch?v=KtlY6ETPyKo&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=11)

## Steps

### 1. Watch the reference video
This lab shares the video with Lab 1. Focus on the sections covering isolation, secrets, and approvals:

[https://www.youtube.com/watch?v=KtlY6ETPyKo&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=11](https://www.youtube.com/watch?v=KtlY6ETPyKo&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=11)

### 2. Restrict who can message the agent — set the channel allowlist (default deny)
Decide who is allowed to talk to Athena. The gateway authorizes every inbound message with a six-check chain — per-platform allow-all, DM pairing, the platform allowlist, the global allowlist, global allow-all, then **default deny**. Nothing configured means **everyone is denied** (fails closed), with a startup warning telling you exactly that.

In the dashboard open **Channels → Configure** for your channel (e.g. Telegram) and set the allowlist to your own user ID:

- **Allowed user IDs** (`TELEGRAM_ALLOWED_USERS`) — comma-separated IDs that may use the bot (get yours from `@userinfobot`).
- **Allow all users** (`TELEGRAM_ALLOW_ALL_USERS`) — leave off; it opens the bot to anyone (dev only).
- Unknown DMs can also be admitted one-by-one via **pairing codes** you approve.

### 3. Isolate execution in a sandboxed backend
Set the terminal backend to a sandboxed container so risky commands never run directly on your host:

```bash
hermes config set terminal.backend docker
```
Or just ask the agent: "Run your risky work in the docker sandbox from now on"


With docker, the agent's shell/tool execution happens inside a disposable container, limiting the blast radius of any dangerous action.

### 4. Store provider/tool secrets via config rather than plain text
Store API keys through the Hermes config mechanism instead of pasting them into prompts or scripts:

```bash
hermes config set <PROVIDER>_API_KEY <value>
```
Or just ask the agent: "Store this <PROVIDER> API key securely in your config"


Replace `<PROVIDER>` and `<value>` with your real provider and key (e.g. `hermes config set OPENROUTER_API_KEY sk-or-...`). Config-managed secrets are kept out of your chat history and plain-text files.

### 5. Require approval before the agent runs risky actions — set the approval mode
Set the approval mode so the agent pauses and asks you before executing sensitive actions (shell commands, file deletions, external posts):

```bash
hermes config set approvals.mode manual
```
Or just ask the agent: "Ask me for approval before running any risky action"


There are **three modes** (not four):

- **manual** (default) — every risky command prompts you: allow **o**nce / this **s**ession / **a**lways / **d**eny, with a 60-second timeout that **fails closed**. On gateway channels you get buttons or reply `yes` / `approve` / `go`.
- **smart** — an auxiliary LLM assesses risk: obviously-safe commands auto-approve, dangerous ones auto-deny, uncertain cases escalate to manual.
- **off** — disables all approval checks; equivalent to running with `--yolo` permanently. Trusted environments only.

Alongside whichever mode is active, the **Tirith** content scanner (`security.tirith_*`) runs in parallel and can add an approval prompt of its own; it also scans context files (`AGENTS.md`, `SOUL.md`, `.cursorrules`) for prompt injection before they enter the system prompt. And below everything sits the **unrecoverable blocklist** — commands like `rm -rf /`, fork bombs, `mkfs` on a mounted root or `dd` to a raw disk are refused regardless of YOLO, `approvals.mode: off`, or any allowlist entry.

> Avoid `--yolo` / `/yolo` / `HERMES_YOLO_MODE=1` outside disposable, trusted environments — it bypasses every approval prompt.

### 6. Apply least privilege — grant only the tools/skills the task needs
Review the tools, skills, and MCP servers Athena has access to and disable anything not needed for the current work.

> Conversational/config step: trim the enabled skills (Lab 4) and MCP servers (Lab 6) to the minimum. Least privilege means the agent can only do what the task actually requires.

## Verification / Expected Output
- **Only allowlisted users reach the agent** — a message from a non-allowlisted account is dropped (default deny).
- **Risky actions run only in the sandbox** (docker backend) and **only after approval**.
- **Secrets are not stored in plain text** — they're set via `hermes config set` and don't appear in chat/scripts.
- Only the tools/skills needed for the task are enabled.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Nobody can message the bot | That's the default-deny floor — add your user ID to the channel allowlist (Channels → Configure). |
| Strangers can trigger the bot | An allow-all flag is on (`*_ALLOW_ALL_USERS`) — turn it off and use the allowlist / pairing instead. |
| Risky command ran without a prompt | Approval mode is `off` or YOLO is on — set `hermes config set approvals.mode manual` and restart Hermes. |
| Agent executes on host, not in a container | Backend isn't set to `docker`; re-set `terminal.backend docker` and confirm Docker is running. |
| Secret visible in logs/history | Never paste keys into prompts — set them with `hermes config set <PROVIDER>_API_KEY`. |
| Too many approval prompts | Use `approvals.mode smart` so an LLM auto-approves the obviously-safe commands. |

## Exercise / Challenge
Deliberately ask Athena to do something risky (e.g. *"Delete all files in this folder"*) and confirm it **pauses for approval** and would execute only inside the sandbox. Then message the bot from a non-allowlisted account and confirm it is denied. Finally, write a 3-bullet "least privilege" policy for Athena listing exactly which tools/skills it is allowed to use as your chief of staff.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
