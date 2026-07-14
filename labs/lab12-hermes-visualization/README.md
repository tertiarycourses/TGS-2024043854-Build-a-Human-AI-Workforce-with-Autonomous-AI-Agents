# Lab 12 — Visualization

## Objective
LO5: Visualize agent activity and workflow data. You will use Hermes' visualization capability to see **Athena's** workflow, task flow, and data at a glance, making the agent's behaviour transparent and easier to supervise.

## Prerequisites
- **Lab 1–11 complete** — Hermes running with real activity (sessions, tasks, automations) to visualize.
- The Desktop app is helpful for the visualization view.

## Estimated Time
25–35 minutes

## 📺 Reference Video
[Visualization](https://www.youtube.com/watch?v=JX2RYeKugrc&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=27)

## Steps

### 1. Watch the reference video
See how Hermes renders workflows/activity visually and how to read the output:

[https://www.youtube.com/watch?v=JX2RYeKugrc&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=27](https://www.youtube.com/watch?v=JX2RYeKugrc&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=27)

### 2. Open the visualization view for the agent's activity
Open the visualization panel that shows Athena's activity.

> In the Desktop app, open the **Visualization / Activity** view. It surfaces the agent's task flow, tool calls, and data. Verify the exact location in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).

### 3. Generate a visualization of a workflow or dataset
Ask Athena to produce a visualization of a workflow or a dataset:

> Conversational step. For example: *"Visualize the steps you took to produce this morning's briefing,"* or *"Chart my task completion over the last week."* The agent generates a diagram/chart of the workflow or data.

### 4. Interpret the visualization to understand what the agent did
Read the visualization: which steps ran, in what order, which tools/subagents were involved, and where time was spent. Use it to confirm the agent did what you expected.

## Verification / Expected Output
- A **visualization of the agent's workflow/data renders** and clearly communicates the agent's activity.
- You can point to specific steps/tools in the visualization and explain what happened.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Visualization view is empty | There's no activity yet — run some tasks/automations first, then reopen the view. |
| Can't find the visualization panel | It's primarily in the Desktop app — install/open it (Lab 2); verify location in the docs. |
| Diagram renders but is unreadable | Narrow the scope (one workflow / one week) so the visualization isn't overloaded. |
| Agent won't generate a chart | Phrase the request explicitly ("visualize/chart …") and ensure a capable model is active. |
| Unsure which visualization types exist | Types are version-specific — verify in the video / docs link above. |

## Exercise / Challenge
Generate two visualizations: one of a **single workflow** (the steps behind one briefing) and one of a **trend** (task completion over the week). Write a two-sentence "read" of each — what it tells you about how Athena is working and one thing you'd optimize.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
