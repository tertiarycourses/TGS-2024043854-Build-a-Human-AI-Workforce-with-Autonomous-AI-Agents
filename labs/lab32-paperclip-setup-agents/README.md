# Lab 32 — Setup AI Agents

## Objective
Configure the agents you hired for **Nimbus Coffee, Inc.** — their **mandate**, the **tools** they may use, and a **per-agent budget cap** — so each specialist can safely carry out delegated work. By the end every agent will have a clear job, a bounded toolset, and a spend limit, and will be ready to receive tasks.

## Prerequisites
- **Lab 31 complete**: an active CEO and at least one approved specialist agent.
- Nimbus Coffee configured with a company budget and workspace (Lab 29).
- Codex adapter available (Lab 28).

## Estimated Time
25–35 minutes

## 📺 Reference Video
[Setup AI Agents](https://www.youtube.com/watch?v=JLnGSWK4bJY&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=7)

## Steps

1. **Watch the reference video for this lab.** It shows an agent's configuration screen — mandate, tools, and per-agent budget.

   [https://www.youtube.com/watch?v=JLnGSWK4bJY&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=7](https://www.youtube.com/watch?v=JLnGSWK4bJY&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=7)

2. **Open an agent's configuration.** On the Nimbus Coffee page, pick one specialist (e.g. the Marketer) and open its **configuration**. This is where you turn a generic hire into a purpose-built role.

3. **Set the agent's mandate and the tools it may use.** Write a crisp **mandate** — one or two sentences on exactly what this agent is responsible for (e.g. "Own Nimbus Coffee's brand voice and launch marketing copy"). Then grant only the **tools** it needs (e.g. file-write to the workspace, web research) and withhold the rest. Least privilege here prevents an agent from straying outside its lane.

   > Tool names and the mandate field are version-specific — verify in the video / docs (<https://docs.paperclip.ing>).

4. **Set a per-agent budget cap.** Give this agent its own spend ceiling, carved out of the company budget. Per-agent caps mean one runaway agent can't drain the whole company — a key safety rail you'll exercise in Lab 33.

5. **Save and confirm the agent is ready to receive tasks.** Save the configuration, reload, and confirm the mandate, tools, and budget persist and the agent's status shows it is ready for work. Repeat steps 2–5 for each specialist you approved.

## Verification / Expected Output
- **Each agent has a mandate, allowed tools, and a budget cap**, and is **ready to receive tasks**.
- The configuration persists after a reload.
- Tools not granted to an agent do not appear in its available set.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Can't open an agent's config | Confirm the agent was actually approved/active in Lab 31; reload the company page. |
| Tool list is empty | The company may expose tools at a higher level first — verify where tools are enabled in the video / docs (<https://docs.paperclip.ing>). |
| Per-agent budget rejected | It may need to be ≤ the remaining company budget. Lower it or raise the company cap (Lab 29). |
| Agent still "not ready" after save | A required field (mandate or tools) may be blank. Fill all required fields and re-save. |
| Field names differ from the video | UI wording is version-specific — match fields per the video / docs (<https://docs.paperclip.ing>). |

## Exercise / Challenge
Configure two specialists with **deliberately non-overlapping** mandates and toolsets (e.g. the Marketer can write files and research but not deploy; the Engineer can write and run code but doesn't own brand voice). Then predict, in one sentence each, which agent should receive the "build the landing page" task vs the "write the launch tagline" task in Lab 34 — proving your role design is unambiguous before you start delegating.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
