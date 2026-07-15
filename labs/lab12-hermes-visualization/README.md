# Lab 12 — Visualization

## Objective
LO5: Visualize agent activity and workflow data. You will use Hermes' visualization capability to render **Athena's** workflow as a graph — nodes for tool calls, edges for their order — then read it, export it, and use it to explain exactly what the agent did.

## Prerequisites
- **Lab 1–11 complete** — Hermes running with real activity (sessions, tasks, automations) to visualize.
- The Desktop app is helpful for the visualization view.

## Estimated Time
25–35 minutes

## 📺 Reference Video
[Visualization](https://www.youtube.com/watch?v=JX2RYeKugrc&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=27)

## Steps

### 1. Watch the reference video
Watch how Hermes renders workflows and activity visually, and pay attention to two things: where the visualization view lives in the UI, and how the presenter reads the diagram (which shapes are tool calls, how ordering is shown). You will reproduce both.

[https://www.youtube.com/watch?v=JX2RYeKugrc&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=27](https://www.youtube.com/watch?v=JX2RYeKugrc&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=27)

### 2. Run a real multi-step session so there is something to visualize
A visualization of an empty agent is empty. Start a fresh session and give Athena a task that forces several tool calls in sequence — for example:

> *"Research the top 3 AI agent platforms, compare their pricing, and summarize in a table."*

Let it run to completion; the web searches, reads, and summarization steps it performs become the nodes of your graph.

### 3. List sessions and note the ID of the one to visualize
In a terminal, list your recent sessions and copy the ID (or title/timestamp) of the session you just ran. You will visualize this specific session rather than "everything", which keeps the diagram readable.

```bash
hermes sessions list
```
Or just ask the agent: "List my recent sessions so I can pick one to visualize"


### 4. Open the visualization view
In the Desktop app, open the **Visualization / Activity** view from the sidebar and select the session from step 3. You should see the session's activity surface — task flow, tool calls, and timing.

> The exact menu location and view name are version-specific — verify in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).

### 5. Generate a workflow graph of the session
Ask Athena (or use the view's generate button) to render the session as a workflow diagram:

> *"Visualize the steps you took in this session as a workflow diagram."*

A graph should render in which **each node is a tool call** (web search, file read, summarize…) and **edges show the order** the calls ran in. If nothing renders, confirm you selected a session that actually used tools.

### 6. Read the graph — nodes, sequence, and time
Walk the diagram from start to finish and name what each node did: which tool, with what input, producing what output. Check the sequence matches what you asked for, and look for where time was spent (long-running nodes) or where the agent looped/retried. This is the supervision skill: confirming from the graph that the agent did what you expected — nothing more, nothing less.

### 7. Export or screenshot the visualization
Save the diagram for your records — use the view's export button if your build has one, otherwise take a screenshot. Keep it with the lab evidence; you will reuse this technique whenever you need to audit an agent run.

```bash
# macOS: Cmd+Shift+4  (Windows: Win+Shift+S)
```

### 8. Use the graph to explain what the agent did
Turn to a classmate (or write three sentences) and explain the run **using only the graph**: what the goal was, which tools ran in what order, and where the result came from. If you can narrate the run from the diagram alone, the visualization has done its job of making Athena's behaviour transparent.

## Verification / Expected Output
- A **workflow graph of a real session renders**, with identifiable tool-call nodes in the order they ran.
- You have an **exported image/screenshot** of the visualization.
- You can **explain the agent's run from the graph alone** — every node named, sequence justified.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Visualization view is empty | There's no activity yet — run a multi-step task (step 2) first, then reopen the view. |
| Can't find the visualization panel | It's primarily in the Desktop app — install/open it (Lab 2); verify the location in the docs. |
| Diagram renders but is unreadable | Narrow the scope to a single session (step 3) so the graph isn't overloaded. |
| Graph has almost no nodes | The task didn't require tools — rerun with a research-style task that forces several tool calls. |
| Agent won't generate a chart | Phrase the request explicitly ("visualize/chart …") and ensure a capable model is active. |
| Unsure which visualization types exist | Types are version-specific — verify in the video / docs link above. |

## Exercise / Challenge
Generate two visualizations: one of a **single workflow** (the steps behind one briefing) and one of a **trend** (task completion over the week). Write a two-sentence "read" of each — what it tells you about how Athena is working and one thing you'd optimize.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
