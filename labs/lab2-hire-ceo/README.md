# Lab 2 — Hire Your CEO Agent

**Goal:** Connect a **local agent adapter** to Paperclip and make your first hire — a
**CEO agent** that reports to you (the Board). This is your first taste of an **approval
gate**: no agent is hired until *you* sign off.

**Time:** ~15 min · **Maps to:** Crash-course Scenario 2

**Before you start:** Complete [Lab 1](../lab1-install-paperclip/README.md) — you need a
running Paperclip with a company and budget.

---

## 1. Prerequisites

- Paperclip running at **http://localhost:3100** with your company from Lab 1.
- **At least one AI coding CLI installed and logged in**, which Paperclip uses as the
  agent's "brain" via a **local adapter**:
  - **Claude Code**, **OpenCode**, **Codex**, or **Gemini CLI**.
- Agents reuse your **existing CLI login**, so no extra API keys are required to begin.

> **Adapters, briefly:** Paperclip detects supported CLIs on your machine and maps each to
> a *local adapter*. A **heartbeat** then wakes agents on a schedule to pick up work. If you
> prefer cloud models, you can instead supply `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` /
> `GEMINI_API_KEY` (see Lab 1's compose file) — but local CLIs are enough for this course.

---

## 2. Verify your adapter is detected

1. In the dashboard, open **Settings → Agents / Adapters** (wording may vary by version).
2. Confirm at least one adapter shows as **available** (e.g. *Claude Code — detected*).
3. If none appear, open a terminal and confirm the CLI runs and is logged in, e.g.:

   ```bash
   claude --version        # Claude Code
   # or:  opencode --version   /   codex --version   /   gemini --version
   ```

   Then restart the Paperclip container so it re-scans:

   ```bash
   docker compose restart      # from your Lab 1 compose folder
   ```

---

## 3. Propose the CEO hire

1. From your company page, choose **Hire CEO** (or **Add agent → CEO**).
2. Pick the **adapter/model** the CEO should use (e.g. Claude Code).
3. Optionally give the CEO a short **mandate** that echoes your company goal, e.g.

   > *"You are the CEO. Deliver the company goal on time and under budget. Propose strategy
   > and delegate to specialists. Escalate anything requiring Board approval."*

4. Submit. Notice the hire enters an **approval gate** — it is *proposed*, not yet active.

---

## 4. Approve the hire (you are the Board)

1. Review the proposed CEO: adapter, mandate, and any per-agent budget cap.
2. Click **Approve**.
3. Paperclip writes a new row to the **activity log** with `actor_type = user` — this is a
   decision only a human can make. The CEO is now **active** and reporting to you.

> **Why the gate?** Hiring, strategy, and budgets are the three decisions Paperclip
> deliberately reserves for humans. Everything else the agents can do on their own.

---

## 5. Quick checklist

- [ ] An agent **adapter** (Claude Code / OpenCode / Codex / Gemini) is detected.
- [ ] A **CEO agent** was **proposed** (entered an approval gate).
- [ ] You **approved** the hire; the CEO is now **active**.
- [ ] The hire is recorded in the activity log as an `actor_type = user` action.

✅ **Next:** [Lab 3 — Approve the Company Strategy](../lab3-approve-strategy/README.md)

---

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
