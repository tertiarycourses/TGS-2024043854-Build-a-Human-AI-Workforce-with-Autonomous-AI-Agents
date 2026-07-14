# Lab 9 — Profile and Kanban

## Objective
LO5: Supervise the agent through its profile and Kanban board. You will configure **Athena's** profile and use the Hermes Kanban board to watch tasks move through **todo → in progress → done**, giving you human oversight of what the agent is working on.

## Prerequisites
- **Lab 1–8 complete** — Hermes running, subagents/delegation understood (this lab shares its reference video with Lab 8).
- The Desktop app (Lab 2) is helpful for the Kanban board's visual UI.

## Estimated Time
30–40 minutes

## 📺 Reference Video
[Profile and Kanban](https://www.youtube.com/watch?v=KPsMThlFb8Y&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=10)

## Steps

### 1. Watch the reference video
This lab shares the video with Lab 8. Focus on the portions covering the agent **profile** and the **Kanban board** view:

[https://www.youtube.com/watch?v=KPsMThlFb8Y&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=10](https://www.youtube.com/watch?v=KPsMThlFb8Y&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=10)

### 2. Set up the agent profile (identity, defaults, preferences)
Configure Athena's profile — its identity, default model/backend, and behavioural preferences.

> Open the profile settings in the Desktop app (or the profile section of `~/.hermes/config.yaml`). Set the name to **Athena**, role to *personal chief of staff*, and default preferences (concise bulleted output, timezone, working hours). The exact profile fields are version-specific — verify in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).

### 3. Open the Kanban board view
Open the Kanban board that visualizes the agent's tasks.

> In the Desktop app, open the **Kanban / Tasks** view. You should see columns such as **Todo**, **In Progress**, and **Done**.

### 4. Assign a task and watch it move todo → in progress → done
Give Athena a task and watch the corresponding card move across the board:

> Assign a task (e.g. *"Draft my weekly team update"*). A card appears in **Todo**, moves to **In Progress** as the agent works, and lands in **Done** when finished. This is your live oversight of what the agent is doing.

### 5. Use the board to review and accept completed work
When a card reaches **Done**, open it, review the agent's output, and accept (or send it back with feedback). This human-in-the-loop review is the point of the board.

## Verification / Expected Output
- The **profile is set** (Athena's identity/defaults are saved).
- The **Kanban board shows tasks progressing** across its columns (Todo → In Progress → Done).
- You can open a Done card and review/accept the completed work.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Can't find the Kanban view | It's primarily in the Desktop app — install/open it (Lab 2); verify location in the docs. |
| Cards don't move columns | The agent may not be running the task — confirm the gateway is up and the task was actually assigned. |
| Profile changes don't apply | Restart Hermes so the new profile config loads. |
| Unsure which profile fields exist | Profile schema is version-specific — verify in the video / docs link above. |
| Done card has no output to review | The task failed mid-run; re-assign and watch In Progress for errors. |

## Exercise / Challenge
Assign three tasks at once and use the board to **prioritize**: drag/reorder Todo cards, watch Athena work them, and reject one Done card with feedback so it returns for a revision. Capture a screenshot of the board with cards in all three columns — this is your evidence of human oversight.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
