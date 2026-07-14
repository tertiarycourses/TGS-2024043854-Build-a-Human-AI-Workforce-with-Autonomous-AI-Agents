# Lab 33 — Security

## Objective
Apply Paperclip's **governance** to **Nimbus Coffee, Inc.**: company-wide and per-agent **budget caps** that trigger an **80% warning** and a **100% pause**; **approvals** that gate risky decisions; and the **audit trail** that records everything. By the end you will have demonstrated the warning and pause rails, resumed the company, and audited who did what — human vs agent — in the embedded PostgreSQL.

## Prerequisites
- **Lab 32 complete**: agents configured with mandates, tools, and per-agent budget caps.
- A company budget set (Lab 29) and, ideally, a deliberately small cap so you can hit the thresholds.
- Paperclip running at `http://localhost:3100` with its embedded PostgreSQL up.
- Basic comfort running `psql`.

## Estimated Time
25–35 minutes

## 📺 Reference Video
[Security](https://www.youtube.com/watch?v=77uTzIqw8SQ&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=8)

## Steps

1. **Watch the reference video for this lab.** It demonstrates the budget rails (80% warning, 100% pause), resuming, and the audit trail.

   [https://www.youtube.com/watch?v=77uTzIqw8SQ&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=8](https://www.youtube.com/watch?v=77uTzIqw8SQ&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=8)

2. **Set a company and/or per-agent budget cap.** In the company settings (Lab 29) and/or an agent's config (Lab 32), set a **deliberately small cap** so ongoing agent work will approach it during this lab. This is what lets you observe the safety rails fire instead of waiting days.

3. **Trigger the 80% warning and 100% pause, then resume.** Let the agents keep working (assign a task or two). As spend crosses **80%** of the cap, Paperclip raises a **warning**; at **100%** it **pauses** the company/agent so nothing can overspend. Review the pause, then **resume** (e.g. by raising the cap or explicitly resuming) and confirm work continues. You have now seen both the soft and hard money rails in action.

4. **Audit actions and spend in the embedded PostgreSQL.** Connect to Paperclip's database to inspect the ground-truth record:

   ```bash
   psql "postgresql://postgres@localhost:5432/paperclip"
   ```

   This opens a SQL prompt against the `paperclip` database. From here you can query the activity/audit records directly rather than trusting the UI alone.

   > The database name and table names are version-specific — verify in the video / docs (<https://docs.paperclip.ing>).

5. **Separate human vs agent actions with `actor_type`.** Run the audit query to see how much of the company's activity was human decisions versus agent actions:

   ```sql
   SELECT actor_type, COUNT(*) FROM activity_log GROUP BY actor_type;
   ```

   You should see rows for `user` (your approvals and hires from Labs 31–34) and for the agents. This is the accountability core: every action is attributable, so you can always answer "who did this?" Exit `psql` with `\q`.

## Verification / Expected Output
- The **80% warning** and **100% pause** both fire as spend approaches the cap.
- **Resume works** — after you resume/raise the cap, agent work continues.
- The audit query returns a breakdown of activity **by `actor_type`** (human `user` vs agents), and you can see **total spend** in the audit data.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Warning/pause never fires | The cap is too high relative to spend. Lower the company or per-agent cap and generate more agent activity. |
| `psql: connection refused` | The database container isn't up/exposed. Check `docker compose -f docker-compose.quickstart.yml ps`; confirm Postgres maps to `localhost:5432`. |
| `relation "activity_log" does not exist` | The table name differs by version. List tables with `\dt` and verify the audit table name in the video / docs (<https://docs.paperclip.ing>). |
| `psql` asks for a password | Supply the configured credentials (or the value in the compose file); the connection string may need a password segment. |
| Company won't resume after pause | Raise the budget cap first, then resume; confirm no per-agent cap is still at 100%. |

## Exercise / Challenge
Deliberately drive Nimbus Coffee to a **100% pause**, screenshot the paused state, then run the `actor_type` audit query and record the human-vs-agent action counts. Write three sentences: what the 80% warning is for, what the 100% pause protects against, and how the `actor_type` audit lets you prove — to a real Board — that a zero-human company is still fully accountable.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
