# Labs — Build a Human-AI Workforce with Autonomous AI Agents

33 hands-on labs across **three** autonomous-agent platforms. Each lab follows a reference
video and builds toward one realistic use case. The course runs over **2 days**:

- **Day 1** — Topic 1 (Hermes Agent) + Topic 2 (OpenClaw)
- **Day 2** — Topic 3 (Paperclip) + Final Assessment

| Topic | Labs | Platform | Running use case |
|-------|------|----------|------------------|
| 1 | 01–14 | **Hermes Agent** (Nous Research) | *Athena* — an always-on personal chief-of-staff |
| 2 | 15–26 | **OpenClaw** | *Nimbus Supplies* — automating a business back-office |
| 3 | 27–33 | **Paperclip** | *Altera AI Blogs* — a zero-human AI blog company you govern |

Do each topic's labs **in order** — later labs build on what earlier ones set up.

---

## Topic 1 — Hermes Agent (Labs 01–14)

| # | Lab |
|---|-----|
| 1 | [Install and Setup Hermes](lab01-hermes-install/README.md) |
| 2 | [Deployment — Local Install & Hermes Desktop App](lab02-hermes-deployment/README.md) |
| 3 | [Memory and Plugins](lab03-hermes-memory-plugins/README.md) |
| 4 | [Skills](lab04-hermes-skills/README.md) |
| 5 | [Providers & Model](lab05-hermes-providers-models/README.md) |
| 6 | [MCP and Tools](lab06-hermes-mcp-tools/README.md) |
| 7 | [Cron Jobs & Automation](lab07-hermes-crons-automation/README.md) |
| 8 | [Subagents & Delegation](lab08-hermes-subagents-delegation/README.md) |
| 9 | [Profile and Kanban](lab09-hermes-profile-kanban/README.md) |
| 10 | [Security](lab10-hermes-security/README.md) |
| 11 | [Use Case — Make a Video with Hyperframe](lab11-hermes-usecase-video/README.md) |
| 12 | [Visualization](lab12-hermes-visualization/README.md) |
| 13 | [Build a Multi-Agent Video Team (Profiles + Kanban)](lab13-hermes-multi-agent-workflow/README.md) |
| 14 | [Webhook](lab14-hermes-webhook/README.md) |

## Topic 2 — OpenClaw (Labs 15–26)

| # | Lab |
|---|-----|
| 15 | [Install OpenClaw](lab15-openclaw-install/README.md) |
| 16 | [Models & Providers](lab16-openclaw-models-providers/README.md) |
| 17 | [Channels](lab17-openclaw-channels/README.md) |
| 18 | [Skills](lab18-openclaw-skills/README.md) |
| 19 | [Tools & Integrations](lab19-openclaw-tools-integrations/README.md) |
| 20 | [Commands](lab20-openclaw-commands/README.md) |
| 21 | [Cron Jobs & Heartbeat](lab21-openclaw-crons-heartbeat/README.md) |
| 22 | [Memory & Context](lab22-openclaw-memory/README.md) |
| 23 | [Security](lab23-openclaw-security/README.md) |
| 24 | [Multi-Agent Workforce](lab24-openclaw-multi-agent/README.md) |
| 25 | [Dreaming — Idle Reflection & Self-Improvement](lab25-openclaw-dreaming/README.md) |
| 26 | [Use Cases & Key Functions](lab26-openclaw-usecases/README.md) |

## Topic 3 — Paperclip (Labs 27–33)

Running use case: **Altera AI Blogs** — found and govern a zero-human company that researches the AI landscape daily and publishes AI-related blogs end to end, as the Board.

| # | Lab |
|---|-----|
| 27 | [Install Paperclip on Windows & Mac](lab27-paperclip-install/README.md) — self-host with Docker Compose (Docker Desktop / WSL2) and open the dashboard at localhost:3100 |
| 28 | [Setup Company, CEO & Mission](lab28-paperclip-company-ceo-mission/README.md) — found 'Altera AI Blogs': mission, budget and the Board-approved CEO agent |
| 29 | [Setup Adaptor](lab29-paperclip-adaptor/README.md) — enable a model adaptor (Claude Code / Codex / Gemini CLI) as the agents' engine |
| 30 | [Create the Task Backlog](lab30-paperclip-task-backlog/README.md) — six well-briefed tasks, with 'Hire the agents to publish the AI-related blogs end to end' as the core task assigned to the CEO |
| 31 | [Add the Tavily Search API](lab31-paperclip-tavily-search/README.md) — store the key as a company Secret and bind it to TAVILY_API_KEY for live web search |
| 32 | [Hire the Members Under the Hiring Task](lab32-paperclip-hire-team/README.md) — the CEO proposes the blog team (research analyst, blog writer, editor/publisher, SEO/marketer) under the core task; you approve each hire at the gate |
| 33 | [Routine & Trigger — Publish Daily at 3pm](lab33-paperclip-daily-routine/README.md) — a Routine with a daily 15:00 trigger generates and runs 'Produce and publish today's AI blog post' automatically |

---

## Lab convention

Every lab follows the same structure: **Objective → Prerequisites → Estimated Time →
📺 Reference Video → Steps (copy-pasteable) → Verification / Expected Output →
Troubleshooting → Exercise / Challenge**. Each lab links its reference video.

> **Note on commands:** commands are anchored on each platform's official docs
> ([Hermes](https://hermes-agent.nousresearch.com/docs/) ·
> [OpenClaw](https://docs.openclaw.ai/) · [Paperclip](https://docs.paperclip.ing)). These
> platforms move fast; a few version-specific commands are flagged in-lab with a "verify"
> note — always trust the reference video and `--help`/`doctor` output on your build.

---

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
