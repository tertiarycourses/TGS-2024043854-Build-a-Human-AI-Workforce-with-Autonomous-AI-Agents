# Lab 10 — Security

## Objective
LO4: Secure the agent with isolation, secrets, and approvals. You will harden **Athena**: run risky work in an isolated terminal backend, manage secrets safely, and require approval before sensitive actions — applying least privilege throughout.

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

### 2. Isolate execution in a sandboxed backend
Set the terminal backend to a sandboxed container so risky commands never run directly on your host:

```bash
hermes config set terminal.backend docker
```

With docker, the agent's shell/tool execution happens inside a disposable container, limiting the blast radius of any dangerous action.

### 3. Store provider/tool secrets via config rather than plain text
Store API keys through the Hermes config mechanism instead of pasting them into prompts or scripts:

```bash
hermes config set <PROVIDER>_API_KEY <value>
```

Replace `<PROVIDER>` and `<value>` with your real provider and key (e.g. `hermes config set OPENROUTER_API_KEY sk-or-...`). Config-managed secrets are kept out of your chat history and plain-text files.

### 4. Require approval before the agent runs risky actions
Enable approval prompts so the agent pauses and asks you before executing sensitive actions (shell commands, file deletions, external posts):

```bash
# enable approval prompts in the security settings
```

Open the security settings (Desktop app or the security section of `~/.hermes/config.yaml`) and turn on approval/confirmation for risky actions.

> The exact security-settings keys are version-specific — verify in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).

### 5. Apply least privilege — grant only the tools/skills the task needs
Review the tools, skills, and MCP servers Athena has access to and disable anything not needed for the current work.

> Conversational/config step: trim the enabled skills (Lab 4) and MCP servers (Lab 6) to the minimum. Least privilege means the agent can only do what the task actually requires.

## Verification / Expected Output
- **Risky actions run only in the sandbox** (docker backend) and **only after approval**.
- **Secrets are not stored in plain text** — they're set via `hermes config set` and don't appear in chat/scripts.
- Only the tools/skills needed for the task are enabled.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Risky command ran without a prompt | Approval prompts aren't enabled — turn them on in security settings and restart Hermes. |
| Agent executes on host, not in a container | Backend isn't set to `docker`; re-set `terminal.backend docker` and confirm Docker is running. |
| Secret visible in logs/history | Never paste keys into prompts — set them with `hermes config set <PROVIDER>_API_KEY`. |
| Too many approval prompts | Scope approvals to genuinely risky actions; keep read-only tools frictionless (see docs). |
| Unsure which security keys exist | Security settings are version-specific — verify in the video / docs link above. |

## Exercise / Challenge
Deliberately ask Athena to do something risky (e.g. *"Delete all files in this folder"*) and confirm it **pauses for approval** and would execute only inside the sandbox. Then write a 3-bullet "least privilege" policy for Athena listing exactly which tools/skills it is allowed to use as your chief of staff.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
