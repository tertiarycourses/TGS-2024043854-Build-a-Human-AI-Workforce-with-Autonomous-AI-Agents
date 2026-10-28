# Lab 7 — Activity 7 — OpenAI Dots: Supervised Launch Review

**Day 2 · Topic 3 · 35 min · Persistent assistant + human supervision · LO3**

> Give a dot a bounded launch-review task, inspect its evidence and practise steering or stopping it.

## Goal
Evaluate Dots and Hermes against the same evidence, access and human-control criteria (LO3).

## The business scenario
The launch manager wants a persistent assistant to check an approved meeting pack and surface gaps. The exercise compares human control, access and verification with the local Hermes workflow.

## You will deliver
- outputs/dots/dots-review.md — actual task, evidence, corrections and access status
- outputs/dots/comparison.csv — Hermes/Dots quality, time, review effort and limitations

## Who does what
- **Agents:** One OpenAI dot; compare with the existing Hermes team
- **You (the human):** Own approval gates, inspect evidence and accept the exact version

## Before you start
- Trainer verifies current Dots entitlement and workspace controls at https://chatgpt.com/dots
- Use only synthetic launch data and the learner’s own authorised training connections
- If learners lack entitlement, use a real trainer demonstration; record observed versus personally executed work accurately. PP does not require Dots access.

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

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-07-Instructions.pdf`](LAB-07-Instructions.pdf).

## Steps

### 1. Verify current access (5 min)
Open https://chatgpt.com/dots in your own approved account. Follow current onboarding if offered. Inspect the workspace’s connected apps, computer access and approval settings before the task. The trainer uses the current official getting-started guide. A consumer free subscription or SWDA redemption is not proof of Dots entitlement.

✅ **Expected:** Actual access state is recorded; unavailable access remains labelled unavailable.

### 2. Delegate the bounded review (10 min)
**Prompt** — paste into *Your OpenAI dot, or trainer’s real demonstration*:

```text
Review only the synthetic Kopi Kaki launch pack I explicitly provide. Identify the management decision, check price/date against the supplied catalogue and list three unresolved questions with source references. Save or present a review I can inspect. Do not access unrelated work, send messages, create events, share files, buy services or publish. Tell me which sources you actually accessed and what is unavailable. Pause if you need broader access.
```

✅ **Expected:** An actual source-linked review or a truthful access limitation; no invented connection.

### 3. Steer and inspect (10 min)
**Prompt** — paste into *Your OpenAI dot, or trainer’s real demonstration*:

```text
Show the evidence for the price and date and distinguish source facts from your suggestions. I choose the outlet-focused recommendation. Revise the review to that decision and explain the change. Stop this task after the revised review; do not treat approval as continuing authority.
```

✅ **Expected:** User steering changes the actual review; inspect current controls to pause/stop further work.

### 4. Compare and record (10 min)
Record personally executed or trainer-observed status, task/setup/run/review minutes, source coverage, defects and corrections. Compare with Hermes on the same scope. Do not claim a named multi-dot team, a connector or an approval control that was not observed.

**Prompt** — paste into *Hermes Desktop chat in the Kopi Kaki workspace*:

```text
Using only our observed results, prepare comparison.csv with platform, execution status, setup/run/review minutes, source coverage, defects, human corrections and remaining uncertainty. State where a local Hermes profile/team or a dot fits this launch workflow and why.
```

✅ **Expected:** Comparison reflects actual evidence rather than product promises.

## Verification / checkpoint
- [ ] Entitlement and exact source access are recorded
- [ ] Review distinguishes source evidence from suggested actions
- [ ] A human correction and stop/pause action are observed or explicitly marked unavailable
- [ ] No unverified team/connector claim or external publication

**Checkpoint:** Actual bounded Dots review, or accurately labelled trainer observation, compared with the Hermes baseline.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Dots unavailable | Observe a real trainer run if available; label observation. Otherwise do the bounded review in Hermes and mark Dots incomplete. |
| Requested broader access | Stop and reduce scope to supplied synthetic documents; do not connect personal work to complete the lab. |

## Stretch challenge
Transfer the checks to a different product while preserving source and decision ownership.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
