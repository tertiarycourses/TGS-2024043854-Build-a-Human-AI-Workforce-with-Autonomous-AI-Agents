# Hermes video studio — real profiles, dependencies and human gates

Preflight the installed version, provider/tool access and distinct profiles before class. Desktop Bot Mode displays named profiles as bots; Telegram messaging bots are a different concept. A single conversation role-playing five people does not count.

## 1. Inspect and prepare

```text
hermes --version
hermes profile list
hermes profile create --help
hermes kanban create --help
hermes kanban diagnostics
hermes gateway status
```

Trainer may create missing profiles with `hermes profile create researcher --description "Extract approved launch facts with source IDs"`, and similarly scriptwriter, producer, auditor and publisher. Configure each through its actual profile settings; do not put credentials in prompts. Do not clone personal memory/credentials into a shared learner profile. In Desktop Bot Mode add the approved profiles to the roster using the current UI. Keep one running worker per profile.

## 2. Disable automatic decomposition, then create human gates

In the selected training gateway, set the board’s Orchestration Auto/Manual control to **Manual**, or configure `kanban.auto_decompose: false` in the correct profile config. Inspect the actual saved value and restart the selected gateway if needed. With Auto enabled, triage cards can be automatically decomposed and routed to workers, so an unassigned triage card alone is not a passive gate. Verify human cards remain unassigned/triage across a dispatcher tick before adding dependent work. Do not use Specify/Decompose on a human gate. Manual mode disables only built-in decomposition; it is not access control and does not prohibit profile-created tasks or wake-ups.

The following commands are for the human operator. Agents use the corresponding Kanban tools. Replace all example IDs with actual returned IDs. Keep the explicit workspace in task bodies; inspect `--workspace` help if binding a task directory.

```text
hermes kanban create "HUMAN: approve exact storyboard" --triage --tenant kopi-video --body "Only the learner may complete this after inspecting the exact storyboard; workers must not modify this gate."
hermes kanban create "HUMAN: accept exact final MP4" --triage --tenant kopi-video --body "Only the learner may complete this after playback, PASS audit and exact file hash. No external posting."
hermes kanban list --tenant kopi-video
```

With Manual mode verified, unassigned triage cards remain pending human action; inspect their state rather than assuming a passive gate from their title. Add source and audit dependencies before proceeding. Human completing an unassigned gate is a supervised classroom convention; it is not an invented native role-based approval system. Withhold send/post tools from this workflow and inspect the gate after each hand-off.

## 3. Wire the graph before dispatch

Create the actual cards with owner, full source/workspace path, unique output and acceptance criteria. Add parent edges **at creation** with `--parent ACTUAL_ID` or the agent tool's `parents` field. Do not create a runnable child and link a prerequisite afterwards: it could already have started.

| Card | Assignee | Parent(s) | Unique output / acceptance |
|---|---|---|---|
| Research | researcher | none | outputs/team/research.md; real source IDs |
| Storyboard | scriptwriter | research | outputs/team/storyboard.md; three approved 5-second scenes |
| HUMAN storyboard gate | none | storyboard | learner checks exact scene text |
| Render | producer | HUMAN storyboard gate | outputs/team/video/final.mp4; playable 15s,1080x1920 |
| Audit | auditor | render | outputs/team/audit-report.md; independently checked frames+metadata |
| HUMAN final gate | none | audit | learner watches full video and accepts actual SHA256 |
| Local package | publisher | HUMAN final gate | outputs/team/release-package.md; no external send/post |

Example human creation syntax (replace IDs and workspace):

```text
hermes kanban create "Render approved video" --assignee producer --parent ACTUAL_STORYBOARD_GATE_ID --tenant kopi-video --body "Workspace FULL_LOCAL_PATH. Own only outputs/team/video/. Inspect approved storyboard and reviewed tools/render_launch_video.py. Produce actual MP4, command log and metadata. No external writes."
hermes kanban list --tenant kopi-video
hermes kanban show ACTUAL_RENDER_TASK_ID
hermes kanban runs ACTUAL_RENDER_TASK_ID
```

Link the finished storyboard task as a parent of the existing unassigned storyboard gate, and audit as a parent of the unassigned final gate. Those gates have no worker, so the human inspects their dependencies before completing them. If any installed-version behaviour differs, stop and consult current official documentation/help rather than assuming an unsupported flag.

## 4. Run, review and recover

Use the already running Desktop-managed gateway; never start a second process polling the same Telegram bot. Dispatcher workers use separate profiles. Inspect actual runs and saved outputs. A worker completes only its own verified task; a failed or missing artifact stays incomplete. Human completes an unassigned gate only after its prerequisites are done and the exact artifact is accepted. A revision creates a follow-up task with the prior result as context; the changed output requires fresh audit and final acceptance.

## 5. Evidence

Capture one actual board/video-task screenshot for PP Task 3 showing bot/profile owners, a parent dependency or human gate, and the render/output task. Retain MP4, logs, source references, independent audit and exact-version human decision as working evidence. Keep tokens and unrelated records out of screenshots.

Official documentation checked 29 October 2026:
- https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- https://hermes-agent.nousresearch.com/docs/user-guide/desktop
