# Build a Human-AI Workforce with Autonomous AI Agents

**WSQ Course · TGS-2024043854 · Tertiary Infotech Academy Pte Ltd**

Hands-on courseware for running a **company of autonomous AI agents** with
**[Paperclip](https://docs.paperclip.ing)** — "an operating system for running a company of
AI agents." Learners self-host Paperclip locally with **Docker Compose**, then act as the
**Board**: hire a **CEO agent**, approve its **strategy**, staff a **team** of specialists,
watch them produce real deliverables, and govern the whole operation with **budgets, safety
rails and a full audit trail**.

> You set the goal and the budget. A CEO agent proposes strategy; specialist agents do the
> work. Every important decision — hiring, strategy, budget — passes a **human approval
> gate**. Work flows across a board: `todo → in_progress → in_review → done`.

---

## What's in this repo

| Path | Contents |
|------|----------|
| [LEARNER_GUIDE.md](LEARNER_GUIDE.md) | Complete step-by-step guide: machine prep → Docker Compose install → all 5 labs → troubleshooting → command cheat-sheet |
| [labs/](labs/) | The 5 hands-on labs, one folder each, plus a lab [index](labs/README.md) |
| [labs/lab1-install-paperclip/](labs/lab1-install-paperclip/) | Install Paperclip via Docker Compose + create a company (ships a documented `docker-compose.yml`) |
| [.claude/](.claude/) | Imported WSQ courseware toolchain (skills, agents, hooks, commands) for regenerating the slide deck / Lesson Plan / Learner Guide / assessments |

---

## The 5 Labs

| # | Lab | You will… | Est. |
|---|-----|-----------|------|
| 1 | [Install Paperclip with Docker Compose & Create Your Company](labs/lab1-install-paperclip/README.md) | Self-host Paperclip locally, then set a goal + monthly budget | ~25 min |
| 2 | [Hire Your CEO Agent](labs/lab2-hire-ceo/README.md) | Connect a local agent adapter and approve your first hire | ~15 min |
| 3 | [Approve the Company Strategy](labs/lab3-approve-strategy/README.md) | Have the CEO draft a strategy; review and move it to `done` | ~15 min |
| 4 | [Build the Team & Execute Real Work](labs/lab4-hire-team-execute/README.md) | CEO hires specialists, delegates tasks, agents write real files | ~25 min |
| 5 | [Govern the Company: Budgets, Safety Rails & Audit](labs/lab5-govern-audit/README.md) | Set caps, trigger the 80%/100% rails, query the audit trail in Postgres | ~20 min |

Do the labs **in order** — each builds on the company created in the previous one.

---

## Quick start

```bash
# 1. Install Docker Desktop and an AI coding CLI (Claude Code / OpenCode / Codex / Gemini), then:
git clone https://github.com/paperclipai/paperclip.git
cd paperclip
docker compose -f docker-compose.quickstart.yml up --build
# 2. Open the dashboard:
#    http://localhost:3100
```

Full prerequisites and click-by-click steps are in **[LEARNER_GUIDE.md](LEARNER_GUIDE.md)**.

---

## Prerequisites

- **Docker Desktop** (running) — <https://www.docker.com/products/docker-desktop/>
- **Git**
- **One AI coding CLI**, installed and logged in — **Claude Code** (recommended), OpenCode,
  Codex, or Gemini CLI. Agents reuse this login, so **no extra API keys** are needed to start.
- ~90 minutes for all five labs.

---

## References

- Crash course: <https://agentfactory.panaversity.org/docs/workforce-with-paperclip-crash-course>
- Paperclip docs: <https://docs.paperclip.ing>
- Paperclip source: <https://github.com/paperclipai/paperclip>
- Course page: <https://www.tertiaryinfotech.com>

---

<sub>© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201526454M) · WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · www.tertiaryinfotech.com</sub>
