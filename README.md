# Build a Human-AI Workforce with Autonomous AI Agents

**WSQ Course · TGS-2024043854 · Tertiary Infotech Academy Pte Ltd**

Hands-on courseware for building and governing **autonomous AI agents** across **three
platforms** — **Hermes Agent** (Nous Research), **OpenClaw**, and **Paperclip**. Learners
install each platform, connect models, give agents memory, skills, tools, schedules and
security, and run them in **multi-agent mode** — delivering the WSQ competency *Artificial
Intelligence Application in Product Development* (TSC ICT-TEM-4034-1.1).

> **32 labs, 3 topics, 2 days.** Day 1 covers Topic 1 (Hermes Agent) and Topic 2 (OpenClaw);
> Day 2 covers Topic 3 (Paperclip) and the final assessment. Each lab follows a reference
> video.

---

## Learning outcomes

- **LO1** — Analyse AI (LLM-based) applications across a range of industries to identify their capabilities and limitations.
- **LO2** — Establish the relationship between AI algorithm/agent design and chatbot/agent efficiency.
- **LO3** — Evaluate and improve the effectiveness of AI (RAG and agent) applications in product development.

---

## What's in this repo

| Path | Contents |
|------|----------|
| [labs/](labs/) | **32 hands-on labs** across three platforms, with reference videos, plus the lab [index](labs/README.md) |
| [courseware/](courseware/) | Generated deck, Lesson Plan, Learner Guide (**v1.6**) — `Human-AI Workforce with Autonomous AI Agents-v1.6.pptx`, `LP-*.docx/pdf`, `LG-*.docx/pdf` |
| [LG-Human-AI Workforce with Autonomous AI Agents.md](LG-Human-AI%20Workforce%20with%20Autonomous%20AI%20Agents.md) | Markdown mirror of the Learner Guide (step-by-step for all 32 labs) |
| [.claude/](.claude/) | WSQ courseware toolchain (single-source build + assessment generators) |

The confidential `assessment/` folder (question papers + answer keys) is **git-ignored** and
Drive-only — never pushed to GitHub.

---

## The three topics (32 labs)

| Topic | Labs | Platform | Running use case |
|-------|------|----------|------------------|
| 1 | [01–14](labs/README.md#topic-1--hermes-agent-labs-0114) | **Hermes Agent** (Nous Research) | *Athena* — a personal chief-of-staff agent |
| 2 | [15–26](labs/README.md#topic-2--openclaw-labs-1526) | **OpenClaw** | *Nimbus Supplies* — automating a business back-office |
| 3 | [27–32](labs/README.md#topic-3--paperclip-labs-2732) | **Paperclip** | *Tertiary AI News Research* — a zero-human AI news desk you govern |

See the [labs index](labs/README.md) for the full per-lab list with video links. Do each
topic's labs **in order**.

---

## Quick start (per platform)

```bash
# Hermes Agent (macOS/Linux/WSL2)
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash && hermes setup --portal

# OpenClaw (needs Node.js 24)
npm install -g openclaw@latest && openclaw onboard

# Paperclip (needs Docker Desktop)
git clone https://github.com/paperclipai/paperclip.git && cd paperclip \
  && docker compose -f docker-compose.quickstart.yml up --build   # http://localhost:3100
```

---

## Prerequisites

- A laptop (Windows 10/11, macOS 12+, or Ubuntu 22.04+) with admin/sudo rights.
- **Node.js 24** (OpenClaw) and **Docker Desktop** (Paperclip); a terminal.
- At least one LLM provider — Claude Code / OpenAI Codex / OpenRouter / MiniMax / DeepSeek login or API key.
- A free **Telegram** account for the channel labs.

---

## References

- Hermes Agent: <https://hermes-agent.nousresearch.com/docs/>
- OpenClaw: <https://docs.openclaw.ai/>
- Paperclip: <https://docs.paperclip.ing>
- Course page: <https://www.tertiaryinfotech.com>

---

<sub>© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W) · WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · www.tertiaryinfotech.com</sub>
