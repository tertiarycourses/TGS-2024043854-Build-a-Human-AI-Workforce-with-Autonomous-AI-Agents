# Paperclip Labs — Build a Human-AI Workforce with Autonomous AI Agents

These five hands-on labs take you from an empty laptop to a running **AI company**
governed by you. You will self-host **Paperclip** — "an operating system for running a
company of AI agents" — with **Docker Compose**, then hire a CEO agent, approve its
strategy, staff a team of specialist agents, and finally govern the whole operation with
budgets, safety rails and a full audit trail.

> **What is Paperclip?** You set an objective and a monthly budget, hire AI agents to do
> the work, and stay in control through **approval gates**. You are *the Board*. A **CEO
> agent** reports to you and proposes strategy; **specialist agents** report to the CEO and
> execute tasks. Work flows across a board: `todo → in_progress → in_review → done`.

Reference crash course: <https://agentfactory.panaversity.org/docs/workforce-with-paperclip-crash-course>
Official docs: <https://docs.paperclip.ing>

---

## The 5 Labs

| # | Lab | You will… | Est. |
|---|-----|-----------|------|
| 1 | [Install Paperclip with Docker Compose & Create Your Company](lab1-install-paperclip/README.md) | Self-host Paperclip locally, then set a goal + monthly budget | ~25 min |
| 2 | [Hire Your CEO Agent](lab2-hire-ceo/README.md) | Connect a local agent adapter and approve your first hire | ~15 min |
| 3 | [Approve the Company Strategy](lab3-approve-strategy/README.md) | Have the CEO draft a strategy; review and move it to `done` | ~15 min |
| 4 | [Build the Team & Execute Real Work](lab4-hire-team-execute/README.md) | CEO hires specialists, delegates tasks, agents write real files | ~25 min |
| 5 | [Govern the Company: Budgets, Safety Rails & Audit](lab5-govern-audit/README.md) | Set caps, trigger the 80%/100% rails, and query the audit trail in Postgres | ~20 min |

---

## Prerequisites (all labs)

- **Docker Desktop** running — <https://www.docker.com/products/docker-desktop/>
- **Git** — to clone the Paperclip repository.
- At least **one AI coding CLI** installed and logged in for the agent adapter, e.g.
  **Claude Code**, **OpenCode**, **Codex**, or **Gemini CLI**. (Agents reuse your existing
  logins — no extra API keys needed to start.)
- A terminal, and about **90 minutes** total.

Do the labs **in order** — each one builds on the company you created in the previous lab.

---

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
