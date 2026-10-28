---
name: brand-compliance-audit
description: Audit a draft post, script, video or publish package against Kopi Kaki's compliance-rules.md (C1–C10) and video-qa-checklist.md (V1–V9) and return a PASS/FAIL table with fixes. Use for any review, audit or QA step.
---

# Brand compliance audit

1. Load `compliance-rules.md` (and `video-qa-checklist.md` for video).
2. For every rule, quote the exact text that passes or fails and give a one-line reason.
3. Verdict: **PASS** only if every rule passes. Otherwise **FAIL** with a numbered fix list.
4. Never fix the work yourself — return it to its owner with the fix list (Kanban: `request-changes`).
5. Escalate to the human if a rule is ambiguous.

Output: `audit-report.md` with the table, the verdict and the fix list.
