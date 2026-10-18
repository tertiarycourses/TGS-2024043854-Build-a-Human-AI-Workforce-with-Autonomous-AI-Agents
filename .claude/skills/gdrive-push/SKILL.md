---
name: gdrive-push
description: Push the current WSQ courseware (slides PPT/PDF, Learner Guide, Lesson Plan, assessments) to the user's Google Drive courseware folder, auto-archiving old versions, then output a verified link block (Trainer Slide PPT / Learner Slide PDF / LG PDF / LP PDF / Assessment DOCX) for lms-tms.tertiaryinfotech.com. Use when the user runs /gdrive-push or asks to upload/push courseware to Google Drive. ALWAYS requires the user-supplied Drive folder link.
---

# GDrive Push — WSQ courseware to Google Drive

Uploads the course's current artifacts into the right subfolders of a Google Drive
courseware folder, moving all superseded files into an `archive` subfolder first.
**Upload-only: nothing on Drive is ever deleted.**

## HARD RULE — user input required

**NEVER push without the user-provided Google Drive folder link.** If the user did not
include the courseware folder link (e.g. `/gdrive-push <link>`), ASK for it first
(AskUserQuestion) and wait. Do not fall back to a remembered, default, or previously
used folder. Confirm the link before the first real (non-dry-run) push of a session.

## Routing

| Drive subfolder (created if missing) | Files pushed |
|---|---|
| Master Trainer Slides | slide deck `.pptx` + `.pdf` (current version only) |
| Learner Guide | `LG-*.docx` + `LG-*.pdf` + the slides `.pdf` |
| Lesson Plan | `LP-*.docx` + `LP-*.pdf` |
| Assessment | all `assessment/*.docx` (WA + PP papers and answer keys) |
| Activities | the whole `labs/` tree (structure preserved) |

**Change detection — only changed files are pushed.** Every file's MD5 is compared
with the Drive copy first; identical files are skipped (no re-upload, no archiving).
The labs sync uses `rclone sync --checksum --backup-dir Activities/archive`, so
unchanged lab files are skipped and replaced/removed ones are MOVED to the archive,
never deleted.

**Archiving — each courseware folder ends up holding ONLY the current files.**
Before uploading, EVERY pre-existing file that is not identical to a pushed file —
old versions, differently-named old decks, Google-native Docs/Slides — is MOVED
server-side into that folder's `archive/` subfolder. The archive folder is
**created if absent**, and any existing `Archive`/`archives` variant is **renamed
to the canonical lowercase `archive`** (case-only renames via a two-step move).
Any **"old versions"-style folder is MERGED into `archive/`** — its contents are
moved in server-side and the emptied folder is removed.
A file that cannot be moved is reported as a WARNING and skipped, never deleted.
Target subfolders are matched case-insensitively (an existing "Assessments" folder
is reused, not duplicated).

Every uploaded file is then set to **"anyone with the link can view"** (via
`rclone link`, which creates the reader permission) and its view link is printed —
include the links in the report to the user.

## How to run

```bash
python3 <this-skill-dir>/gdrive_push.py "<drive-folder-link>" --repo "<course repo>" --dry-run   # preview
python3 <this-skill-dir>/gdrive_push.py "<drive-folder-link>" --repo "<course repo>"             # real push
```

Always run `--dry-run` first and show the user the plan; then do the real push.
Report per-folder what was archived and uploaded.

## FINAL STEP — LMS-TMS link block + link check

After the real push, ALWAYS end with an LMS-ready link block for
`lms-tms.tertiaryinfotech.com`, in EXACTLY this format (one artifact per line,
its "anyone with the link" view link appended):

```
Trainer Slide — PPT: <link to the current slides .pptx in Master Trainer Slides>
Learner Slide - PDF (get from LG folder): <link to the slides .pdf inside the Learner Guide folder>
LG - PDF: <link to LG-*.pdf>
LP - PDF: <link to LP-*.pdf>
Assessment - DOCX: <link(s) to the assessment .docx question papers>
```

Note the **Learner Slide PDF is the copy in the Learner Guide folder** (not the
Master Trainer Slides one). These links are what gets pasted into the course page
on lms-tms.tertiaryinfotech.com.

Then do a **final link check** before reporting done — for every link in the block:

1. Verify it resolves (e.g. `rclone lsjson --drive-root-folder-id ... ` by file id,
   or fetch the link and confirm it is not a 404/permission page).
2. Confirm it points to the RIGHT file — correct file name, correct extension
   (PPT vs PDF vs DOCX), and the CURRENT version (not an archived one).
3. Confirm sharing is "anyone with the link can view".

Report the check result per link (✓/✗). If any link fails, fix it (re-share or
re-link the correct file) and re-check before finishing.

## Transport / prerequisites

The script talks to Google Drive **directly via rclone** (remote name `gdrive`,
override with env `GDRIVE_REMOTE`). All Drive operations are upload (`copyto`) or
server-side move to Archive (`moveto`) — there is no delete anywhere.

- One-time setup if the remote is missing: `brew install rclone` then
  `rclone config create gdrive drive scope=drive` and complete the Google sign-in
  in the browser (use the account that owns the courseware folder).
- The `--drive-root-folder-id` flag scopes every call to the user-supplied folder,
  so the script cannot touch anything outside it.

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
