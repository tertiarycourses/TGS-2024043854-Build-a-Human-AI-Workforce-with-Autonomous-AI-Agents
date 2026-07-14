# Lab 34 — Assign Task

## Objective
Run **Nimbus Coffee, Inc.** end-to-end: **assign a real task** to a specialist agent, watch it **execute and write a deliverable** into the workspace, then **review and accept** the result to move it to **done** — completing a slice of the company goal. This is the payoff of the whole Paperclip track: a zero-human company producing real work under your governance.

## Prerequisites
- **Lab 33 complete**: budget rails and audit governance in place.
- Configured specialist agents with mandates, tools, and budgets (Lab 32).
- A connected workspace folder at `~/paperclip-workspace/nimbus-coffee` (Lab 29).
- Codex adapter available (Lab 28).

## Estimated Time
25–35 minutes

## 📺 Reference Video
[Assign Task](https://www.youtube.com/watch?v=kAGzMnQ3_Cs&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=9)

## Steps

1. **Watch the reference video for this lab.** It shows assigning a task, the agent executing it, and reviewing the deliverable.

   [https://www.youtube.com/watch?v=kAGzMnQ3_Cs&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=9](https://www.youtube.com/watch?v=kAGzMnQ3_Cs&list=PLZslvC3k6NibmbMzfuyc3UGXkIC5k6YvC&index=9)

2. **Assign a task to a specialist agent.** On the task board (Lab 30), create a concrete task and **assign it to the right specialist** — e.g. give the Engineer "Build a one-page Nimbus Coffee landing page in the workspace", or the Marketer "Write the launch tagline and hero copy". Match the task to the mandate you set in Lab 32.

3. **Watch the agent execute and write output to the workspace.** The task moves **todo → in_progress** as the agent works. When it finishes, check that a real file appeared in your workspace:

   ```bash
   ls -R ~/paperclip-workspace/nimbus-coffee
   ```

   You should see the deliverable the agent produced (e.g. `index.html`, `tagline.md`). This is the proof that the agent did real work, not just described it.

4. **Review the deliverable in the in_review state.** The task is now in **in_review**, waiting on you. Open the produced file and judge it against the task and the company goal. As the Board, you are the quality gate.

5. **Approve to move it to done, or send it back for revision.** If the deliverable is good, **approve** it — the task moves to **done** and that slice of the Nimbus Coffee goal is complete. If it falls short, **send it back for revision** with feedback, and the agent iterates. Either way, you stayed in control end-to-end.

## Verification / Expected Output
- An assigned task is **executed by an agent**, produces a **real file** in `~/paperclip-workspace/nimbus-coffee`, and is **reviewed and accepted to done**.
- `ls -R ~/paperclip-workspace/nimbus-coffee` lists the deliverable the agent wrote.
- The task's final state on the board is **done** (or back in progress if you sent it for revision).

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| No file appears in the workspace | The workspace isn't writable/mounted. Re-check the connection (Lab 29); if containerised, confirm the host folder is mounted into the container. |
| Task stuck in `in_progress` | The agent may lack the needed tool or hit its budget cap. Check the agent's tools/budget (Lab 32) and Codex status (Lab 28). |
| Agent produces the wrong kind of output | The task didn't match the agent's mandate. Reassign to the specialist whose mandate fits (Lab 32). |
| `ls: No such file or directory` | The workspace path is wrong or wasn't created. Re-run `mkdir -p ~/paperclip-workspace/nimbus-coffee` and re-check the config. |
| Can't approve / send back | The review action wording is version-specific — locate the approve/revise controls in the video / docs (<https://docs.paperclip.ing>). |

## Exercise / Challenge
Assign one task to each of your specialists in a sensible order (e.g. Marketer writes the tagline, then Engineer builds a landing page that uses it), and drive both to **done**. Then open the workspace and confirm the files reference each other correctly. Finally, cross-check the audit trail from Lab 33 to confirm each assignment and approval is attributed to the right actor — you have now run a complete zero-human company cycle for Nimbus Coffee, from goal to shipped deliverable, entirely under Board governance.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
