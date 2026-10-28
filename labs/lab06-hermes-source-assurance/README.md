# Lab 6 — Activity 6 — Source Assurance, RAG Comparison & Maintenance

**Day 2 · Topic 3 · 45 min · Multi-agent team + human oversight · LO3**

> Retrieve approved source passages, compare grounded and unsupported answers, and repair a stale source before it reaches the video.

## Goal
Compare a retrieval-grounded assistant with a standard LLM and assess implementation and maintenance feasibility using actual source tests (LO3; PP Task 3 written analysis).

## The business scenario
The first cut depends on price, date and promotion wording. Source quality must be checked before product claims are reused. Then transfer the design to a fictional financial-services advisory workflow.

## You will deliver
- outputs/source/source-register.md — file IDs, versions, passages and owners
- outputs/source/retrieval-test.md and verifier-report.md — supported, missing and conflicting cases
- outputs/source/rag-feasibility.md — standard LLM comparison, costs, access, upkeep and evaluation

## Who does what
- **Agents:** Distinct Hermes profiles: researcher, scriptwriter, producer, auditor and publisher
- **You (the human):** Own approval gates, inspect evidence and accept the exact version

## Before you start
- Activity 5 real Hermes video team is working
- Same approved launch workspace and original source files

## Concepts in action
- Separate agent state and output ownership
- Source provenance and independent verification
- Exact-version human decision and honest completion

## Lab files (`data/`)

| File | What it is |
|---|---|
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `video-qa-checklist.md` | V1–V9 video QA checks |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |
| `source-test-cases.csv` |  |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-06-Instructions.pdf`](LAB-06-Instructions.pdf).

## Steps

### 1. Register sources (10 min)
**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Assign the researcher a separate source-register.md task. Inspect campaign-brief.md, product-catalogue.csv and compliance-rules.md. Record actual filenames, human-readable source IDs, current version/date if present, owner and permitted use. Quote exact supporting passages for price, launch date and promotion. Missing version metadata is a gap; do not invent it.
```

✅ **Expected:** Actual passages and stable source IDs support video claims.

### 2. Run supported and unsupported retrieval tests (10 min)
**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Use only the approved local sources for three tests: product price; full promo terms; whether the drink has a certified health benefit. Quote the supporting passage and source ID for each supported answer; answer INSUFFICIENT EVIDENCE for the unsupported health claim. Save retrieval-test.md. This is a small file-retrieval grounding exercise, not proof of a deployed vector database or production RAG system.
```

✅ **Expected:** Supported answers cite real passages; unsupported claim is refused.

### 3. Verify independently and repair stale evidence (10 min)
**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Assign the independent auditor to check each answer against the original source, not the researcher summary. In a separate training test fixture copy one price line and change it to an intentionally conflicting value; preserve the original files. Mark the fixture SYNTHETIC STALE TEST, detect the conflict and keep downstream release gated until I choose the authoritative source. Save verifier-report.md and the resolution; do not let majority vote decide factual truth.
```

✅ **Expected:** Verifier detects the seeded conflict and downstream copy uses the human-confirmed source.

### 4. Transfer to financial services and assess feasibility (15 min)
**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Write rag-feasibility.md for a fictional financial-services client. Compare a standard LLM assistant with retrieval from a firm-approved corpus: strengths, limitations, provenance, latency, cost and access boundaries. Assess implementation feasibility: corpus owner, ingestion/chunking/indexing choice, permissions, source versioning and rollback, refresh/re-index routine, test questions, accuracy/relevance checks and human approval. Explain how this local passage test differs from a production RAG service. Give one condition under which the simpler standard assistant is adequate and one condition requiring retrieval.
```

✅ **Expected:** Balanced RAG-vs-standard comparison with realistic maintenance plan and product decision.

## Verification / checkpoint
- [ ] Every accepted claim has a checked source passage
- [ ] Auditor independently detects the stale test without changing approved originals
- [ ] Feasibility covers cost/access/upkeep/evaluation and limitations of the local exercise

**Checkpoint:** Source-backed and missing-evidence tests plus independent verification and a written maintenance decision.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Agent invents certification | Return to original passages; mark unsupported and block reuse. |
| Different source versions disagree | Human source owner decides; preserve old/new versions and retest affected artifacts. |

## Stretch challenge
Transfer the checks to a different product while preserving source and decision ownership.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
