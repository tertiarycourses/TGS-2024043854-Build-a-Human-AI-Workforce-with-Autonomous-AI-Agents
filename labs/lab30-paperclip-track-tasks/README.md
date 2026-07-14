# Lab 30 — Track AI Tasks

## Objective
Use Paperclip's **task board** to track AI work through its four states — **todo → in_progress → in_review → done** — giving you visibility and control over what the agents are doing for **Nimbus Coffee, Inc.** By the end you will be able to watch a task move across the board and inspect its activity log.

## Prerequisites
- **Lab 29 complete**: Nimbus Coffee configured with a budget and a connected workspace.
- The Codex adapter available (Lab 28) so tasks can actually be worked.
- Paperclip running at `http://localhost:3100`.

## Estimated Time
20–30 minutes

## 📺 Reference Video
[Track AI Tasks](https://www.youtube.com/watch?v=FrYvRd0KX_I&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=5)

## Steps

1. **Watch the reference video for this lab.** It shows the task board layout and how tasks flow through the four columns.

   [https://www.youtube.com/watch?v=FrYvRd0KX_I&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=5](https://www.youtube.com/watch?v=FrYvRd0KX_I&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=5)

2. **Open the task board for the company.** In the dashboard, open **Nimbus Coffee, Inc.** and go to its **task board**. You'll see four columns — **todo**, **in_progress**, **in_review**, **done** — the single source of truth for everything the company is working on.

3. **Create or observe a task in the "todo" column.** Either create a task yourself (e.g. "Draft the Nimbus Coffee brand tagline") or watch one the CEO/agents have already queued. A task in **todo** is committed work that has not started yet.

4. **Watch a task move todo → in_progress → in_review.** As an agent picks up the task, it moves to **in_progress**; when the agent finishes and produces a deliverable, it moves to **in_review**, waiting for your judgement. Observing this flow is how you supervise a company of agents without micromanaging each action.

5. **Open a shell to review the task activity log.** For a deeper view than the UI, open a shell inside the running Paperclip container:

   ```bash
   docker compose -f docker-compose.quickstart.yml exec paperclip sh
   ```

   From here you can inspect logs / data behind the board (the activity records that back each task's history). Exit with `exit` when done.

   > The service name (`paperclip`) and internal log locations are version-specific — verify in the video / docs (<https://docs.paperclip.ing>).

## Verification / Expected Output
- Tasks are **visible on the board** and move through **todo → in_progress → in_review → done**.
- At least one task demonstrably transitions between states while you watch.
- The container shell opens and lets you inspect the task/activity history behind the board.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Board is empty | No tasks yet. Create one manually, or hire the CEO (Lab 31) so agents begin queueing work. |
| Tasks stuck in `todo` | No agent/adapter is available to pick them up. Confirm Codex is available (Lab 28) and an agent exists. |
| `exec paperclip` — no such service | The service name differs in your compose file. Run `docker compose -f docker-compose.quickstart.yml ps` to find the real service name, then re-run `exec`. |
| Task moves to in_review but shows no output | The deliverable may be written to the workspace — check `~/paperclip-workspace/nimbus-coffee`. |
| Column names differ from the video | UI wording is version-specific — verify state names in the video / docs (<https://docs.paperclip.ing>). |

## Exercise / Challenge
Create three Nimbus Coffee tasks of different sizes (a quick tagline, a medium landing-page draft, a larger go-to-market note). Watch which ones flow fastest to **in_review** and note where they queue. Write one sentence on what the board tells you about the company's throughput — this is the operational visibility that lets you run a zero-human company responsibly.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
