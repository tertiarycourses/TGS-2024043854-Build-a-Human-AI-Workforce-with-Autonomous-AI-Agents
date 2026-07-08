# Lab 3 — Approve the Company Strategy

**Goal:** Let your **CEO agent** draft a strategy for reaching the company goal, then act as
the Board: **review** it and move it from `in_review` to `done`. You will see Paperclip's
**task board** and its four states in action for the first time.

**Time:** ~15 min · **Maps to:** Crash-course Scenario 3

**Before you start:** Complete [Lab 2](../lab2-hire-ceo/README.md) — you need an active CEO.

---

## 1. The task board & its four states

Every piece of work in Paperclip lives on a board and flows through four states:

```
todo  →  in_progress  →  in_review  →  done
```

- **todo** — created, not started.
- **in_progress** — an agent is actively working it.
- **in_review** — the agent finished; **waiting for a human** to accept.
- **done** — you approved it.

A **strategy** is just the first, most important task on this board — and it stops at
`in_review` until *you* advance it.

---

## 2. Ask the CEO to draft a strategy

1. Open your company and select the **CEO agent**.
2. Trigger the strategy work — either click **Draft strategy**, or send the CEO a short
   instruction such as:

   > *"Draft a strategy to achieve our company goal within budget. Break it into phases and
   > the specialist roles you'll need to hire."*

3. The CEO's task moves to **in_progress**. On the next **heartbeat** the CEO's adapter
   (Claude Code / OpenCode / etc.) runs and produces a strategy document. The task then
   moves itself to **in_review**.

> **Tip:** If nothing happens immediately, wait for the heartbeat or use **Run now / Nudge**
> if your version exposes it. Watch the logs with `docker compose logs -f`.

---

## 3. Review the strategy (Board decision)

1. Open the strategy task sitting in **in_review**.
2. Read what the CEO proposed — phases, the specialist roles it wants to hire, and rough
   effort. Ask yourself:
   - Does it actually serve the **company goal** from Lab 1?
   - Are the proposed hires reasonable for your **budget**?
3. Choose one:
   - **Approve** → the task moves to **done**. (Do this to continue the course.)
   - **Request changes / send back** → returns to the CEO for another pass. Iterate until
     you're happy, *then* approve.

4. On approval, Paperclip logs the decision with `actor_type = user`. The strategy is now
   the authorised plan the CEO will staff and execute in Lab 4.

> **Governance point:** Nothing downstream (hiring specialists, spending budget) proceeds on
> an *unapproved* strategy. The `in_review` gate is where you keep control.

---

## 4. Quick checklist

- [ ] The CEO's strategy task moved `todo → in_progress → in_review`.
- [ ] You **read** the proposed strategy and its intended hires.
- [ ] You **approved** it (or sent it back, iterated, then approved) → state is **done**.
- [ ] The approval is recorded in the activity log as a `user` action.

✅ **Next:** [Lab 4 — Build the Team & Execute Real Work](../lab4-hire-team-execute/README.md)

---

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
