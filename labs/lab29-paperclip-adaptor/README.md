# Lab 29 — Setup Adaptor

## Objective
LO2: Connect a model adaptor as the agents' engine. Give the company's agents a **brain**. Paperclip ships three built-in adaptors — **Claude Code** (`claude_local`), **Codex** (`codex_local`) and **Gemini CLI** (`gemini_local`) — and supports installable **external adaptors (alpha)**. You will confirm your adaptor is detected so every agent **Tertiary AI News Research** hires can reason and act with it.

## Prerequisites
- **Lab 28 complete** — the company exists with a mission, budget and an approved CEO.
- Paperclip running at `http://localhost:3100`.
- At least one adaptor CLI account (Claude Code, OpenAI Codex CLI, or Gemini CLI).

## Estimated Time
20–30 minutes

## 📺 Reference Video
[Setup Adaptor](https://www.youtube.com/watch?v=WItGcCiQRKw&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=4)

## Steps

### 1. Watch the reference video for this lab
[https://www.youtube.com/watch?v=WItGcCiQRKw&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=4](https://www.youtube.com/watch?v=WItGcCiQRKw&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=4)

### 2. Install / log in to the adaptor CLI on the host so Paperclip can detect it
Paperclip detects adaptor CLIs installed on the host machine. Install and authenticate at least one — e.g. **Claude Code** (`claude` and log in) or the **OpenAI Codex CLI** (`codex` and log in) — on the same machine that runs the Paperclip containers.

### 3. Open Settings → Instance settings → Adapters in the dashboard
In the dashboard go to **Settings → Instance settings → Adapters**. This page is the registry of every engine the instance can run agents on.

### 4. Confirm the built-in adaptors are listed and yours shows as available
You should see the three built-ins with their model counts:

- **Claude Code** (`claude_local`) — 9 models
- **Codex** (`codex_local`) — 10 models
- **Gemini CLI** (`gemini_local`) — 8 models

The adaptor whose CLI you installed in step 2 should show as **available/detected**.

### 5. Use the power icon to hide adaptors; 'Install Adapter' adds external adaptor packages (alpha)
Two controls on this page matter for governance:

- The **power icon** on each adaptor toggles it — hide adaptors you don't want agents to pick, so hires can only run on engines you have vetted.
- **Install Adapter** adds **external adaptor packages** beyond the three built-ins. This feature is **alpha** — expect rough edges.

### 6. Restart Paperclip if your adaptor is not detected
Detection happens at startup, so a CLI installed after Paperclip came up may not show until a restart:

```bash
docker compose -f docker-compose.quickstart.yml restart
```

Run it from the cloned `paperclip` folder, then reload the Adapters page.

## Verification / Expected Output
- **Settings → Instance settings → Adapters** lists the built-in adaptors — Claude Code (9 models), Codex (10 models), Gemini CLI (8 models).
- Your chosen adaptor is **detected and enabled** for agents.
- Adaptors you powered off no longer appear as options when hiring an agent.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Your adaptor shows "not detected" | The CLI isn't installed/authenticated on the host, or Paperclip started before it was — log in with the CLI, then restart with `docker compose -f docker-compose.quickstart.yml restart`. |
| Adapters page is empty | You are in Company settings, not **Instance settings** — switch to Settings → Instance settings → Adapters. |
| Adaptor detected but agents can't use it | It is powered off — click the power icon to re-enable it. |
| Install Adapter fails | External adaptor packages are **alpha** — check the package name and Paperclip release notes, or stay on the built-ins. |
| CLI works in your terminal but not for Paperclip | The container can't see your CLI login — ensure the CLI is installed/authenticated on the same host (and path) Paperclip inspects, then restart. |

## Exercise / Challenge
Power off every adaptor except the one you intend the company to use, then start a hire and confirm only that engine is offered. Note in one sentence why pinning a single vetted adaptor is a governance control (predictable cost and behaviour), then re-enable any adaptors you actually want available.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
