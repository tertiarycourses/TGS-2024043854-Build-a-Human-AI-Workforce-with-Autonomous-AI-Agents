# Lab 8 — Subagents & Delegation

## Objective
LO5: Delegate work to isolated subagents across backends. You will turn **Athena** into a coordinator that delegates tasks to worker subagents running on isolated terminal backends (local, docker, ssh, modal), then aggregates their results.

## Prerequisites
- **Lab 1–7 complete** — Hermes running with a provider.
- Docker installed and running if you use the `docker` backend (recommended for isolation).

## Estimated Time
40–50 minutes

## 📺 Reference Video
[Subagents & Delegation](https://www.youtube.com/watch?v=KPsMThlFb8Y&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=10)

## Steps

### 1. Watch the reference video
See how a coordinator agent spawns worker subagents on isolated backends and combines their output:

[https://www.youtube.com/watch?v=KPsMThlFb8Y&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=10](https://www.youtube.com/watch?v=KPsMThlFb8Y&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=10)

### 2. Choose an isolated backend for worker agents
Set the terminal backend that worker subagents will run on. `docker` gives each worker an isolated container:

```bash
hermes config set terminal.backend docker
```

Other supported backends include `local`, `ssh`, and `modal`. Docker is recommended so worker agents can't touch your host directly.

> The exact backend flag/values are **version-specific** — if `docker` isn't accepted, verify the supported backend names in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).

### 3. Ask the coordinator to delegate a multi-part task
Open the TUI and give Athena (the coordinator) a task with clearly separable parts so it delegates each to a worker subagent:

> Conversational step. For example: *"Delegate this: subagent A researches competitor pricing, subagent B drafts a comparison table, subagent C writes a one-paragraph recommendation. Then combine their work."* Watch the coordinator spin up workers.

### 4. Observe each subagent run in isolation and report back
Watch each worker subagent execute on the isolated backend and return its portion of the result. Confirm they run **separately** (each in its own container/environment when using docker) rather than in the coordinator's session.

### 5. Review the coordinator's aggregated result
Confirm the coordinator **combines** the workers' outputs into one coherent deliverable — the research, the table, and the recommendation merged into a single response.

### 6. The natural-language way
You can skip the CLI entirely and simply ask the agent: *"Delegate three subagents to research MiniMax, Kimi and DeepSeek in parallel, then merge the findings"*.

## Verification / Expected Output
- The coordinator **delegates to worker subagents on an isolated backend** and returns a **combined result**.
- With docker, each worker runs in its own container (isolation is visible/logged).
- The final aggregated answer reflects all delegated parts.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `hermes config set terminal.backend docker` rejected | Docker may not be installed/running, or the backend name differs — start Docker and verify supported names in the docs. |
| Subagents run in the main session, not isolated | Confirm the backend is actually set to `docker`; restart Hermes so it takes effect. |
| Workers hang or time out | Container resources/pull may be slow; check Docker is healthy and the image pulled. |
| Coordinator doesn't delegate | Phrase the task with clearly separable parts and explicitly ask it to delegate to subagents. |
| Aggregated result missing a part | One worker failed silently — re-run and check per-subagent logs. |

## Exercise / Challenge
Give Athena a "board pack" task: delegate three subagents to (1) pull this week's metrics, (2) draft an executive summary, and (3) list risks. Have the coordinator assemble a single one-page pack. Then switch `terminal.backend` back to `local` and re-run — note the difference in isolation and any behaviour change.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
