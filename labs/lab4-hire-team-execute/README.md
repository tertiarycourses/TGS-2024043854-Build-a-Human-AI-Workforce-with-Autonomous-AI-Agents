# Lab 4 — Build the Team & Execute Real Work

**Goal:** Watch the company come alive. The **CEO** hires **specialist agents** (each hire
gated by *your* approval), delegates tasks to them, and — with a **workspace folder**
connected — the agents produce **real files** on your machine.

**Time:** ~25 min · **Maps to:** Crash-course Scenarios 4 & 7

**Before you start:** Complete [Lab 3](../lab3-approve-strategy/README.md) — you need an
**approved strategy**.

---

## 1. Connect a workspace folder

So agents write real deliverables (not just chat), give the company a folder on disk.

1. Create an empty folder for the company's output, e.g.:

   ```bash
   mkdir -p ~/paperclip-workspace/nimbus-coffee
   ```

2. In the dashboard open the company's **Workspace** settings and point it at that folder
   (or the path exposed inside the container — the Lab 1 data mount already persists the
   agent workspace).
3. Anything the team creates — web pages, copy, CSVs — now lands in this folder.

> **Reminder:** In Lab 1 the single bind mount also stores the agent workspace, so files
> survive restarts.

---

## 2. CEO hires specialists (each needs your approval)

1. Open the **CEO agent**. Based on the approved strategy, it proposes **specialist hires**
   — for the Nimbus Coffee example, perhaps a *Web Developer* agent and a *Copywriter*
   agent.
2. Each proposed hire enters an **approval gate**, exactly like the CEO hire in Lab 2.
3. **Review and Approve** each specialist you want. Set a **per-agent budget cap** if
   prompted (you'll lean on caps in Lab 5).

> Every specialist reports to the **CEO**, not to you. Your job is approvals and oversight —
> the CEO does the day-to-day delegation.

---

## 3. Delegate & execute

1. The CEO breaks the strategy into tasks and assigns them to specialists. New cards appear
   on the board in **todo**.
2. On each **heartbeat**, the assigned agents pick up their tasks (`in_progress`), run their
   adapter, and produce output into the **workspace folder**.
3. Completed work moves to **in_review** for your acceptance — the same gate you used for
   the strategy.

Watch it happen from the terminal:

```bash
docker compose logs -f      # from your Lab 1 compose folder
```

---

## 4. Verify real files were created

Check the workspace folder on your machine:

```bash
ls -R ~/paperclip-workspace/nimbus-coffee
```

You should see actual artefacts — e.g. an `index.html`, a `copy.md`, or a `social-posts.md`.
Open them and confirm they reflect your company goal.

---

## 5. Review and accept deliverables

1. Open each task sitting in **in_review**.
2. Inspect the linked file(s). Good enough? **Approve** → **done**. Not yet? **Send back**
   with a note; the agent revises on the next heartbeat.
3. Keep going until the board is clear and the goal is met.

> **You just ran a company:** a goal became a strategy, the strategy became a team, and the
> team produced real deliverables — with a human approval at every decision that mattered.

---

## 6. Quick checklist

- [ ] A **workspace folder** is connected to the company.
- [ ] The CEO **proposed** one or more specialists; you **approved** them.
- [ ] Tasks flowed `todo → in_progress → in_review` for the specialists.
- [ ] **Real files** appear in the workspace folder and match the goal.
- [ ] You **reviewed and accepted** (or sent back) each deliverable.

✅ **Next:** [Lab 5 — Govern the Company: Budgets, Safety Rails & Audit](../lab5-govern-audit/README.md)

---

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
