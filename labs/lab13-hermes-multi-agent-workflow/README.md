# Lab 13 — Build a Multi-Agent Workflow

## Objective
LO5: Compose multiple agents into a coordinated workflow. You will design a multi-agent workflow in which several agents take on distinct roles and hand off tasks to one another to complete a larger goal, building on the subagents and delegation concepts from Lab 8.

## Prerequisites
- **Lab 1–12 complete** — especially Lab 8 (Subagents & Delegation), whose concepts this lab extends.
- An isolated backend configured (docker recommended) for the worker agents.

## Estimated Time
45–55 minutes

## 📺 Reference Video
[Build a Multi-Agent Workflow](https://www.youtube.com/watch?v=GzlbC75bYtU&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=19)

## Steps

### 1. Watch the reference video
See a full multi-agent workflow composed and run end-to-end, with hand-offs between roles:

[https://www.youtube.com/watch?v=GzlbC75bYtU&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=19](https://www.youtube.com/watch?v=GzlbC75bYtU&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=19)

### 2. Define the agents and their roles in the workflow
Design the workflow by naming each agent and its distinct responsibility.

> Conversational/design step. For a chief-of-staff use case, define roles such as: **Researcher** (gathers facts), **Writer** (drafts content), **Reviewer** (checks quality), with **Athena** as coordinator. Write the roles down before wiring anything.

### 3. Connect the agents so outputs hand off between them
Wire the agents so each one's output becomes the next one's input (Researcher → Writer → Reviewer).

> Use the subagent/delegation mechanism from Lab 8. Instruct Athena that the Researcher's findings feed the Writer, and the Writer's draft feeds the Reviewer. Verify the exact multi-agent wiring in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).

### 4. Run the workflow end-to-end on a sample goal
Give the workflow a real goal and run it start to finish:

> For example: *"Produce a one-page competitor brief on the top 3 AI agent platforms."* Watch Researcher → Writer → Reviewer hand off in sequence and produce the final brief.

### 5. Verify each stage completed and the final result is correct
Check that every stage ran, each hand-off delivered usable input to the next, and the final output is coherent and correct.

## Verification / Expected Output
- The multi-agent workflow **runs end-to-end**, with **each agent handing off to the next** and producing the final result.
- Each stage's contribution is visible in the final deliverable.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| A hand-off drops data | Make each stage explicitly pass its output to the next; check the coordinator's instructions. |
| Agents run in parallel instead of sequence | State the order explicitly (Researcher → Writer → Reviewer); a sequential workflow needs ordered hand-offs. |
| One agent fails and halts the workflow | Re-run that stage; ensure its backend (docker) is healthy and it has the tools it needs. |
| Final output is incoherent | The Reviewer stage isn't enforcing quality — strengthen its role instructions. |
| Unsure how to wire multi-agent flows | Wiring is version-specific — verify in the video / docs link above. |

## Exercise / Challenge
Add a fourth role — a **Publisher** agent that formats the final brief and (using a tool from Lab 6) posts it to a channel or saves it to a file. Run the full four-stage workflow and confirm the published artifact reflects every prior stage. This turns Athena into a small autonomous content team.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
