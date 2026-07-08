# Lab 5 — Govern the Company: Budgets, Safety Rails & Audit

**Goal:** Put on your CFO/Board hat. Set **budget caps**, trigger Paperclip's **safety
rails** (80% warning, 100% pause), and then **query the audit trail** directly in the
embedded PostgreSQL — the way a real finance owner would verify what the agents did.

**Time:** ~20 min · **Maps to:** Crash-course Scenarios 5 & 6

**Before you start:** Complete [Lab 4](../lab4-hire-team-execute/README.md) — you need a
company that has hired agents and done some work (so there's spend and history to inspect).

---

## 1. Budget caps & safety rails

Paperclip enforces spending limits at two levels:

- **Company-wide monthly cap** — the budget you set in Lab 1.
- **Per-agent caps** — an optional ceiling on each individual agent.

Two automatic **safety rails** protect you:

| Threshold | What happens |
|-----------|--------------|
| **80%** of a cap | **Warning** — you're notified spend is approaching the limit. |
| **100%** of a cap | **Pause** — work stops so nothing runs away. Only *you* can lift it. |

### Try it

1. Open **Settings → Budget** for the company (and/or a specific agent).
2. Temporarily set a **low cap** — e.g. lower it just above current spend — to force the
   rails to fire.
3. Nudge the team to do a little more work and watch for the **80% warning**, then the
   **100% pause**.
4. Restore a sensible cap and **resume** to lift the pause.

> **Cost tracking under the hood:** every spend is written to the **`cost_events`** table,
> and every action (hires, approvals, pauses) to **`activity_log`**. That's what makes the
> rails — and the audit below — possible.

---

## 2. Audit the company like a CFO (query PostgreSQL)

The company's entire history is queryable. Open a shell in the running container and connect
to the **embedded PostgreSQL**.

```bash
# from your Lab 1 compose folder — open a shell in the container
docker compose exec paperclip sh
```

Inside the container, connect with `psql` (the embedded DB is bundled). If `psql` isn't on
the path, the database files live under `PAPERCLIP_HOME` (`/paperclip`):

```bash
# adjust db name/user if your version differs; check docs.paperclip.ing
psql "postgresql://postgres@localhost:5432/paperclip"
```

### Useful audit queries

**Every decision and action, newest first:**

```sql
SELECT created_at, actor_type, action, detail
FROM activity_log
ORDER BY created_at DESC
LIMIT 50;
```

**Separate *your* decisions from the agents' actions** — the `actor_type` field is the key:

```sql
SELECT actor_type, COUNT(*)
FROM activity_log
GROUP BY actor_type;
-- 'user'  = decisions only you could make (hires, approvals, budgets)
-- 'agent' = work the agents did on their own
```

**Where did the money go?**

```sql
SELECT created_at, agent, amount, description
FROM cost_events
ORDER BY created_at DESC;

SELECT SUM(amount) AS total_spent FROM cost_events;
```

Exit with `\q`, then `exit` to leave the container.

> **What you're proving:** every dollar and every action is attributable. You can show
> exactly *who* (human vs. agent) did *what*, *when*, and *what it cost* — full accountability.

---

## 3. Establish a monthly governance review

Set up the recurring habit the crash course recommends. Ask your CEO agent (or note for
yourself) to run a monthly audit against a baseline:

> *"Walk through everything hired, configured, scheduled, approved, or paused since the last
> audit. Flag anything I did not explicitly sign off on."*

This catches **drift** without you having to hover over the company day to day.

---

## 4. Quick checklist

- [ ] A **company** and/or **per-agent** budget cap is set.
- [ ] You triggered the **80% warning** and the **100% pause**, then **resumed**.
- [ ] You connected to the embedded **PostgreSQL** and read `activity_log`.
- [ ] You used **`actor_type`** to separate human decisions from agent actions.
- [ ] You totalled spend from **`cost_events`**.
- [ ] You defined a **monthly audit** prompt to detect drift.

🎉 **You've completed the Paperclip labs** — you installed an AI company, staffed it, and
now govern it with budgets and a full audit trail.

**Where next:** the **Dynamic Workforce** crash course (scheduling recurring agent work) and
the cloud deployment guides at <https://docs.paperclip.ing>.

---

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
