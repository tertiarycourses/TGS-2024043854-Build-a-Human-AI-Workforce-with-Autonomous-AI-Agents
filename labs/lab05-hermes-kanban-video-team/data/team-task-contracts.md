# Launch video team contracts

| Task | Owner | Input | Output | Blocked by | Acceptance |
|---|---|---|---|---|---|
| 1 Research | researcher | Approved office pack | research.md | none | Every fact has source |
| 2 Storyboard | scriptwriter | research.md + brand | storyboard.md | 1 | Human approves scene text |
| 3 Render | producer | approved storyboard | video/final.mp4 | 2 + human gate | playable 15s, 1080x1920 |
| 4 Audit | auditor | actual MP4 + sources | audit-report.md | 3 | metadata, facts, rights, readability |
| 5 Accept | Human owner | reviewed video | decision-log.md | 4 | exact file hash + decision |

Each worker owns separate output files. A task list describes coordination; inspect actual distinct Hermes profile runs to prove the team ran. Do not publish externally.
