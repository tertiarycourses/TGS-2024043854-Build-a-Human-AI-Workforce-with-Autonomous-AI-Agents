---
description: Push the current WSQ courseware (slides PPT/PDF, LG, LP, assessments) to the user-provided Google Drive courseware folder, archiving old versions and setting anyone-with-link viewer
argument-hint: <google-drive-courseware-folder-link>
---

# GDrive Push

Push this course repo's current courseware to the user's Google Drive courseware folder.

**Folder link (required, user-supplied):** `$ARGUMENTS`

## Steps

1. **HARD RULE — never push without the user's folder link.** If `$ARGUMENTS` is empty or
   not a Google Drive folder link/ID, ASK the user for the courseware folder link
   (AskUserQuestion) and stop until provided. Never fall back to a default or remembered folder.
2. Locate the `gdrive-push` skill folder (project `.claude/skills/gdrive-push/`, else
   `~/.claude/skills/gdrive-push/`) and follow its SKILL.md. Run the pusher from the course
   repo root:
   ```bash
   python3 <skill-dir>/gdrive_push.py "<folder-link>" --dry-run   # preview first
   python3 <skill-dir>/gdrive_push.py "<folder-link>"             # real push
   ```
3. Show the user the dry-run plan (what gets archived and uploaded per folder:
   Master Trainer Slides / Learner Guide / Lesson Plan / Assessment / Activities). Old files always land in each folder's lowercase archive/ subfolder (created/renamed automatically), then do the real push.
4. Report per folder: files archived → `archive/`, files uploaded, and each file's
   **anyone-with-link view link** (printed by the script). Remind the user that assessment
   answer keys are among the shared files.
5. If rclone is missing or not authorised, follow the SKILL.md one-time setup
   (`rclone config create gdrive drive scope=drive`) and have the user complete the
   Google sign-in in the browser.

## HARD RULE — FG and AP are ALWAYS pushed (user rule, 18 Oct 2026)

Every `/gdrive-push` run MUST also push the **Facilitator Guide and Assessment Plan** (DOCX + PDF) to
the course folder's **`Facilitator Guide/`** and **`Assessment Plan/`** subfolders — a run that
leaves them off Drive is **not finished**.

1. **Source:** the private `assessment/fg-ap/` folder (`FG_<code>_<title>_vN`, `Assessment_Plan_<code>_<title>_vN`).
   If it is empty but the FG/AP sit in `courseware/` (a git-ignored copy beside the deck/LP/LG), copy
   them into `assessment/fg-ap/` first. If no FG/AP exists at all, build them with **`wsq-fg-ap`**
   before pushing — never skip.
2. **Push them FIRST, not last.** The main run reaches FG/AP only after the whole `labs/` sync, which
   can take a long time on large lab trees; run the FG/AP pusher up front so they are on Drive even if
   the long sync stalls:
   ```bash
   python3 ~/.claude/skills/wsq-fg-ap/scripts/push_fgap.py --dry-run --dir "<repo>/assessment/fg-ap" --code TGS-…
   python3 ~/.claude/skills/wsq-fg-ap/scripts/push_fgap.py          --dir "<repo>/assessment/fg-ap" --code TGS-…
   ```
   (The main run then finds them unchanged by MD5 and skips them.)
3. **Version continuity:** before pushing, compare with the FG/AP already on Drive — never push a
   lower version number than what is there; carry the existing Version Control rows forward.
4. **Verify on Drive** (`rclone lsjson "gdrive:Facilitator Guide" …` / `"gdrive:Assessment Plan"`) that
   the new vN `.docx` + `.pdf` are present, the PDFs kept their file ids (in-place update) and the old
   versions sit in `archive/`. Report the FG/AP links with the courseware links.
5. Hand over to **`/tms-push`**, which must set/verify the two trainer-only LMS links.
