# Lab 13 — Build a Multi-Agent Video Team (Profiles + Kanban)

## Objective
LO3: Orchestrate a team of profiles through the Kanban board to produce a video. You will build a three-profile video-production team — **researcher**, **scriptwriter**, and **video_producer** — then create a Kanban board task, decompose it into child tasks, and watch the orchestrator route each child task to the right profile by its description until the team delivers a rendered video.

## Prerequisites
- **Lab 1–12 complete** — especially Lab 9 (Profile and Kanban) and Lab 11 (video generation), whose concepts this lab combines.
- At least two models available (a long-context model, a cheap model, and a code/tool-capable model are ideal — one provider with several models is fine).
- The Desktop app / dashboard open for the Profiles and Kanban pages.

## Estimated Time
45–55 minutes

## 📺 Reference Video
[Build a Multi-Agent Video Team (Profiles + Kanban)](https://www.youtube.com/watch?v=GzlbC75bYtU&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=19)

## Steps

### 1. Watch the reference video
Watch a multi-profile workflow composed and run end-to-end. Pay attention to two mechanics you will reproduce: how a task's **assignee** is a *profile* (not a person), and how the orchestrator picks a profile for each child task by matching the task against the profile's `--description`.

[https://www.youtube.com/watch?v=GzlbC75bYtU&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=19](https://www.youtube.com/watch?v=GzlbC75bYtU&list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d&index=19)

### 2. Design the team on paper first
Before creating anything, write down the three roles, the kind of model each needs, and — most importantly — the one-line description the orchestrator will route by. The description is the routing contract: it must say exactly what the profile takes in and hands off.

| Profile | Model type | `--description` (the routing contract) |
| --- | --- | --- |
| `researcher` | Long-context model | Reads sources, writes the video brief + key points |
| `scriptwriter` | Cheap model | Turns the brief into a narrated script + scene list |
| `video_producer` | Code/tool model | Turns the script into a rendered video with TTS + slides |

Note the pipeline shape: brief → script → video. Each profile's output is the next profile's input.

### 3. Create the researcher profile
Create the first profile on a long-context model (it will read sources whole). The `--description` text is what the orchestrator matches child tasks against, so type it exactly as designed:

```bash
hermes profile create researcher --description "Reads sources, writes the video brief + key points"
```

> Profile-creation syntax (and how the model is attached — a `--model` flag or a follow-up config step) is version-specific — verify in the video / docs (https://hermes-agent.nousresearch.com/docs/).

### 4. Create the scriptwriter profile
Create the second profile on a **cheap** model — turning a brief into a script is high-volume, low-difficulty work, so this is where you save money:

```bash
hermes profile create scriptwriter --description "Turns the brief into a narrated script + scene list"
```

### 5. Create the video_producer profile
Create the third profile on a **code/tool-capable** model — it must drive TTS and slide-rendering tools reliably:

```bash
hermes profile create video_producer --description "Turns the script into a rendered video with TTS + slides"
```

### 6. Verify the team on the Profiles page
Open the dashboard and go to the **/profiles** page in the sidebar. You should see all three profiles listed, each showing its model and its description. Read each description back critically — a vague description here causes wrong routing later. Fix any typos now (edit the profile or recreate it).

### 7. Create the Kanban board task
Create the top-level task on the board and assign the first stage to the researcher. Pick a real topic you care about and keep the deliverable measurable ("60-second explainer video"):

```bash
hermes kanban create "Produce a 60-second explainer video on <topic>" --assignee researcher
```

Note the task ID printed on creation — you need it for the next step. The board is durable: it is a SQLite database at `~/.hermes/kanban.db`, so tasks survive restarts.

### 8. Decompose the task into child tasks
Ask Hermes to break the top-level task into child tasks:

```bash
hermes kanban decompose <id>
```

You should see child tasks appear — roughly "research + brief", "script + scene list", "render video with TTS + slides". Inspect each child's assignee: the orchestrator routes each child to the profile whose **description** best matches the work. This is why step 2's wording mattered.

### 9. Watch the lanes as the team works
Open the dashboard **/kanban** page and watch the board dispatch. Every task moves through the lifecycle **triage → todo → ready → running → blocked → done → archived**. The research child should enter `running` first (it runs on the researcher profile's model), then hand off so the script task becomes `ready`, and so on down the pipeline. A task sitting in `blocked` is asking for a human — open it and read why.

### 10. Review each task's workspace deliverables
Click into each completed child task. Every task gets its own **workspace** (a scratch directory / dedicated dir / git worktree, depending on configuration) where its outputs live. Open the researcher task's workspace and read the brief; open the scriptwriter's and read the script + scene list; open the video_producer's and play the rendered video. Confirm each stage's output actually fed the next — the script should quote the brief's key points, and the video should follow the scene list.

### 11. Accept the final video to done
If the video meets the brief, accept the top-level task so it moves to **done** (and later `archived`). If it doesn't, add a comment on the relevant child task with concrete feedback (e.g. "narration too fast in scene 2") and send that task back through the board rather than redoing everything — that is the point of decomposed work.

### 12. Reflect: why this beats one big agent
Look back at the run: the expensive long-context model only did research, the cheap model wrote the script, and the tool model rendered. One prompt to a single agent would have used the expensive model for everything. Note one sentence on cost and one on reviewability (you could inspect and reject *per stage*).

### 13. The natural-language way
You can skip the CLI entirely and simply ask the agent: *"Create a crew of profiles — researcher, scriptwriter, video producer — then decompose this board task and route each piece to the right profile"*.

## Verification / Expected Output
- Three profiles (**researcher**, **scriptwriter**, **video_producer**) visible on the dashboard **/profiles** page with correct descriptions.
- The decomposed Kanban tasks are **routed to the right profile by description**, and the **/kanban** lanes show tasks flowing triage → todo → ready → running → done.
- Each child task's **workspace contains its deliverable** (brief, script + scene list, rendered video), and the accepted top-level task sits in **done**.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| Task stuck in `blocked` | It's waiting on a human — open the task, read the blocker, add a comment answering it / unblock it, and it re-enters the flow. |
| Child task routed to the wrong profile | The routing signal is the profile `--description` — sharpen it (say exactly what the profile takes in and hands off) and re-decompose. |
| Nothing dispatches / board is dead | The gateway isn't running — check `hermes gateway status` and restart it, then reload the /kanban page. |
| Board looks empty after a restart | It shouldn't — the board is durable SQLite at `~/.hermes/kanban.db`. Check you're on the same machine/account and the gateway is up. |
| Video task fails at render | The `video_producer` profile's model must be tool-capable — attach a code/tool model and ensure the TTS/slides tools from Lab 6/11 are available. |
| Unsure of profile/kanban command syntax | Commands are version-specific — verify in the video / docs link above. |

## Exercise / Challenge
Add a fourth profile — `qa_reviewer` (cheap model, `--description "Watches the draft video, checks it against the brief, lists fixes"`) — recreate the board task and decompose again. Confirm the orchestrator now routes a review child task to `qa_reviewer` before final acceptance, and that one fix it raises gets applied. You have turned Athena into a supervised four-role production team.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
