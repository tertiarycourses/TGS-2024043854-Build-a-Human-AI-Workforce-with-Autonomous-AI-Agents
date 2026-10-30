---
name: courseware-build
description: Single-source build pipeline for a WSQ course — one content module (course_data.py + data_domainN.py, or data_labs.py for use-case labs) drives ALL artifacts (the slide deck PPT — all-white house style or the Claude Code course design via ccdeck.py, the Lesson Plan LP, the Learner Guide LG + its Markdown mirror, and the labs/ index) so they stay 100% aligned. Generic and course-agnostic: it locates the course repo and derives every filename from course_data, so the same engine works for any WSQ course. Use to regenerate courseware after editing course content.
---

# courseware-build — single-source WSQ courseware pipeline

**Key principle:** the course material must be **100% aligned to the exam/skills domains so
students who take the course can pass the exam.** One content module drives every artifact, so
titles, lab numbering, learning outcomes, the schedule and the assessment can never drift apart.

## Layout

```
.claude/skills/courseware-build/
  SKILL.md
  assets/            brand assets (tertiary-infotech-logo.png + any course badge)
  build/
    course_data.example.py   TEMPLATE → copy to course_data.py and fill in (metadata, outcomes, topics, schedule)
    data_domain.example.py   TEMPLATE → copy to data_domain1.py … data_domainN.py (per-domain activities/labs)
    build_slides.py       generic engine → courseware/<TITLE>-<VER>.pptx  (all-white house style)
    build_lesson_plan.py  generic engine → courseware/LP-<TITLE>.docx
    build_learner_guide.py generic engine → LG-<TITLE>.md (repo root) + courseware/LG-<TITLE>.docx
    prodoc.py             shared DOCX helpers (cover page, version-control record, TOC, page numbers)
    inject_toc.py         page-numbered TOC injector (LibreOffice can't update TOC fields headless)
    build_courseware.sh   orchestrator: generate → render PDF → inject TOC → re-render
```

## How the pipeline stays generic (won't break when moved / installed elsewhere)

- Each builder finds the **course repo** by walking up from its own location for a directory that
  contains both `courseware/` and `labs/`. Override with the `COURSE_REPO` env var.
- `assets/` is resolved **relative to the skill** (co-located), never a hard-coded path.
- Output filenames are derived from `course_data.SHORT_TITLE` / `VERSION` — nothing is hard-coded to
  a specific course, so the same engine builds any WSQ course.

## Build

```bash
# one command: PPT + LP + LG as DOCX + PDF, with page-numbered TOCs
bash .claude/skills/courseware-build/build/build_courseware.sh

# or individually
python3 .claude/skills/courseware-build/build/build_slides.py
python3 .claude/skills/courseware-build/build/build_lesson_plan.py
python3 .claude/skills/courseware-build/build/build_learner_guide.py
```

Assessments (WA SAQ + PP) are built by the sibling **wsq-assessment** skill from the same course
content, so the assessment stays aligned with the slides/LG/LP.

## After a build (mandatory)

Bump `VERSION` in `course_data.py`, add a Document Version Control Record entry in the LG/LP builders,
delete superseded versioned files, then run the **courseware-qa** agent to visually audit the deck
against the WSQ hard rules before reporting completion.

## Reusing for a new course

Copy this skill into the new course's `.claude/skills/courseware-build/`, replace `course_data.py` and
`data_domainN.py` with the new course's content, drop the course badge into `assets/`, and run the
orchestrator. The engine files (build_*.py, prodoc.py, inject_toc.py, build_courseware.sh) are reused
unchanged.

## Use-case labs + Claude Code deck design (pattern proven on TGS-2024043854 v2.0, Oct 2026)

Use this pattern when a course should run **connected use-case labs** (learners see business value)
instead of feature tours (tools / memory / skills one by one). Reference implementation:
`build/reference-usecase-labs/` (user level) — copy it into the course's `build/` and replace the content.

### Engine files
| File | Role |
|---|---|
| `ccdeck.py` | Slide components in the **"Agentic AI Applications with Claude Code" (TGS-2025052468) design**: ivory `FAF9F5` / charcoal `21201C`, terracotta `D97757`, Cambria headings, Calibri body, white shadowed cards with icon circles. Components: `cover(logo=)`, `section`, `cards`, `rows`, `timeline`, `loop`, `compare`, `table` (auto-grows font to fill rows), `image`, `statement`, `prompt` (copy-ready dark code panel), `lab_intro`, `lab_flow` (agent/human steps), `hub`, `trainer`, `flow`. Text is fit-to-box; arrow glyphs are forced to Calibri (Cambria/Caladea have no →). |
| `render_icons.js` | react-icons → PNG (needs global `react`, `react-dom`, `react-icons`, `sharp`); `ccdeck.icon_png()` caches into `build/icons/`. |
| `data_labs.py` | **Single source for every lab**: scenario, deliverables, agents vs human role, LO, `prereq`, `concepts`, `flow` (agent/human steps), `steps` (body / `cmd` / `prompt` / `where` / `expect`), `verify`, `trouble`, `challenge`. |
| `mock_data.py` | Synthetic company pack (brief, brand guide, compliance rules, CSVs, SKILL.md files, templates) — seeded, deterministic. |
| `build_labs.py` | Writes `labs/labNN-*/README.md`, `COPY-PROMPTS.txt`, `LAB-NN-Instructions.pdf` (headless Chrome print), `data/` (+ generated brand images), `labs/README.md`, and the offline **Lab Prompts page** `prompts/index.html` (Copy buttons; works from `file://`). Never deletes — it overwrites. |
| `build_slides.py` | Writes `slide_map.json` (first slide of each section/lab) — the LP reads it, so LP slide numbers always match the deck. |
| `version_history.py` | Document Version Control rows shared by LP and LG. |

### Rules learned
- **One company, one storyline**: every lab builds on the previous lab's outputs (`~/<workspace>/outputs/labNN/`); Day 2 imports Day 1 outputs instead of redoing them.
- **Each lab ships**: README, instructions PDF, COPY-PROMPTS.txt, mock data, assets, prerequisites, and a checkpoint. Prompts appear on slides as `prompt` panels and on the prompts page (pattern from TGS-2024043856 M365 Copilot repo).
- **Human-in-the-loop must be real**: say whether a gate is runtime-enforced (blocked task, Approvers, hiring gate) or prompt-enforced (agent rule). Cron/scheduled runs are fresh sessions — carry approval state in a file (e.g. `pending-approval` status), never in chat memory. Review the package before releasing a publish/post step; post exactly once.
- **Approved CP governs timing**: map the schedule to the CP learning units (e.g. LU1 5 h / LU2 5 h / LU3 4 h + 2 h assessment); `course_data.LUS` + an LU column per schedule row; the LP asserts each LU's minutes.
- **Verify platform commands against `--help` / local docs** before writing a lab (Hermes ships its docs in `~/.hermes/hermes-agent/website/docs`); flag anything unverified.
- **Never commit assessment content in builders**: course-specific assessment builders (questions + model answers) and FG/AP data files (rubric) are git-ignored; the generic `wsq-assessment/build_assessment.py` is driven by a private override module.
- `inject_toc.py` now writes the page-numbered entries as the cached result of a **real Word TOC field**; `prodoc.add_version_control` uses fixed column widths (`prodoc.set_widths`) so the record no longer spans pages.

## Copy style — vivid pitch, never a template (user rule, 30 Oct 2026)

Slide and LG copy must read like a strong pitch, not a filled-in form. See the WSQ projects `CLAUDE.md` for the full rules. In short:
- The title makes a claim, the subtitle is a one-line pitch, and the body leads with named real examples (products, companies, numbers, dates).
- **Do not repeat the same labelled rows across a series of slides** (e.g. "How it works / The human decides / Watch for" on every scenario). Vary the layout to suit the idea. Worked example: `slides_v23.scenario()` uses a hook paragraph plus "Where you see it today" with three named examples, instead of four fixed rows.
- Verify every fact against its source; mark unverified claims; blur third-party names in screenshots.


## YouTube videos: embed so they play on click in PowerPoint (user rule, 30 Oct 2026)

Use the **`pptx-youtube-video`** skill (`~/.claude/skills/pptx-youtube-video/`) for every YouTube or online video in a
deck: `add_online_video(slide, url, x, y, w, h)`. It writes PowerPoint's Online Film markup, verified with the
trainer, and adds a "▶ Open in YouTube" fallback link. Never use a screenshot plus a link. Trainers must click
**Enable Content** on PowerPoint's yellow "external media blocked" bar before videos play; say so in the trainer notes.
