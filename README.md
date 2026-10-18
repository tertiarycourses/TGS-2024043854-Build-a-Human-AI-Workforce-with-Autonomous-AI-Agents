# Build a Human-AI Workforce with Autonomous AI Agents

**WSQ Course · TGS-2024043854 · Tertiary Infotech Academy Pte Ltd**

| Course detail | Information |
|---|---|
| Course code | `TGS-2024043854` |
| Programme | WSQ |
| Duration | 2 days · 16 hours (14 h training + 2 h assessment), 9:30 am – 6:30 pm |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/wsq-build-a-human-ai-workforce-with-autonomous-ai-agents.html) |
| Funding | Up to 70% WSQ course-fee funding for eligible learners (up to 50% baseline). Eligibility and terms apply — see the course page. |

## About the course

Hands-on courseware for building a **human–AI workforce**: from a single autonomous AI agent to a
multi-agent team and a governed company of agents — with a human approving everything that matters.
Learners work for one fictional company, **Kopi Kaki Co.** (a Singapore kopi chain launching the
*Gula Melaka Cold Brew* with the **#ShiokColdBrew** campaign), across **ten connected use-case labs**
on **Hermes Agent** (Nous Research) and **Paperclip** — delivering the WSQ competency *Artificial
Intelligence Application in Product Development* (TSC ICT-TEM-4034-1.1).

> **v2.0 · 3 topics · 10 labs · 2 days.** Day 1: Topic 1 (Foundations) + Topic 2 (Hermes Agent, Labs 1–5).
> Day 2: Topic 3 (Paperclip, Labs 6–10) and the final assessment. **Copy-ready prompts:** open
> [`prompts/index.html`](prompts/index.html) in your browser (works offline).

---

## Learning outcomes

- **LO1** — Analyse AI (LLM-based) applications across a range of industries to identify their capabilities and limitations.
- **LO2** — Establish the relationship between AI algorithm/agent design and chatbot/agent efficiency.
- **LO3** — Evaluate and improve the effectiveness of AI (RAG and agent) applications in product development.

---

## What's in this repo

| Path | Contents |
|------|----------|
| [prompts/index.html](prompts/index.html) | **Lab Prompts page** — pick a lab, click **Copy**, paste. Works offline from the downloaded folder |
| [labs/](labs/) | **10 use-case labs** — each with `README.md`, `LAB-NN-Instructions.pdf`, `COPY-PROMPTS.txt` and `data/` (mock company data, skills, agent roles, brand assets) |
| [courseware/](courseware/) | Slide deck **v2.0** (`.pptx` + `.pdf`), Lesson Plan and Learner Guide (`.docx` + `.pdf`) |
| [LG-Human-AI Workforce with Autonomous AI Agents.md](LG-Human-AI%20Workforce%20with%20Autonomous%20AI%20Agents.md) | Markdown mirror of the Learner Guide |
| [.claude/](.claude/) | Single-source build pipeline (`courseware-build/build/`) — deck, LP, LG, labs, PDFs and prompts page from one data set |

Confidential material — `assessment/` (papers, answer keys, and in `assessment/fg-ap/` the Facilitator Guide
and Assessment Plan, which embed the answer keys and rubric) — is **git-ignored** and Drive-only.

---

## Topics covered

1. **Foundations of Autonomous AI Agents & the Human–AI Workforce** — history of AI · the range of AI applications · AI agents vs agentic AI · the agentic loop · harness engineering · perception–brain–action · short/long-term memory and RAG · world models · single → multi-agent → human–agent collaboration · levels of autonomy · the 2026 agent market (OpenClaw, Hermes, Paperclip, OpenAI Dots, Meta Muse, Block Buzz, Manus Cue …) · Singapore's AgentSea · human–AI use cases in science, maths, drug discovery and business · governance. Activity: Human–AI Workforce Canvas.
2. **Hermes Agent — from a single AI employee to a multi-agent team** (Labs 1–5).
3. **Paperclip — running and governing a company of AI agents** (Labs 6–10).

## Labs

Copy-ready prompts for every lab: [`prompts/index.html`](prompts/index.html) (open in a browser; works offline). Full index: [labs/README.md](labs/README.md).

| # | Day | Lab | Instructions |
|---|---|---|---|
| 1 | Day 1 | [Hire Your First AI Employee — Customer & Market Research Brief](labs/lab01-hermes-first-ai-employee/README.md) | [PDF](labs/lab01-hermes-first-ai-employee/LAB-01-Instructions.pdf) |
| 2 | Day 1 | [End-to-End Social Media Campaign with One Agent](labs/lab02-hermes-social-media-campaign/README.md) | [PDF](labs/lab02-hermes-social-media-campaign/LAB-02-Instructions.pdf) |
| 3 | Day 1 | [Human-in-the-Loop Publishing & Community Care (Telegram + Cron)](labs/lab03-hermes-human-in-the-loop/README.md) | [PDF](labs/lab03-hermes-human-in-the-loop/LAB-03-Instructions.pdf) |
| 4 | Day 1 | [Multi-Agent Video Studio — Research → Script → Production → Audit → Publish](labs/lab04-hermes-multi-agent-video-studio/README.md) | [PDF](labs/lab04-hermes-multi-agent-video-studio/LAB-04-Instructions.pdf) |
| 5 | Day 1 | [Multi-Agent Campaign Command Centre — Measure, Optimise & Report](labs/lab05-hermes-campaign-command-centre/README.md) | [PDF](labs/lab05-hermes-campaign-command-centre/LAB-05-Instructions.pdf) |
| 6 | Day 2 | [Found Kopi Kaki Growth Studio — an AI Company You Govern](labs/lab06-paperclip-found-ai-company/README.md) | [PDF](labs/lab06-paperclip-found-ai-company/LAB-06-Instructions.pdf) |
| 7 | Day 2 | [Hire the Marketing Team Through the Board Approval Gate](labs/lab07-paperclip-hire-marketing-team/README.md) | [PDF](labs/lab07-paperclip-hire-marketing-team/LAB-07-Instructions.pdf) |
| 8 | Day 2 | [Run the #ShiokColdBrew Launch as a Project — Review, Revise, Release](labs/lab08-paperclip-launch-campaign-project/README.md) | [PDF](labs/lab08-paperclip-launch-campaign-project/LAB-08-Instructions.pdf) |
| 9 | Day 2 | [Automate the Weekly Video Pipeline with a Routine and a Board Gate](labs/lab09-paperclip-weekly-video-routine/README.md) | [PDF](labs/lab09-paperclip-weekly-video-routine/LAB-09-Instructions.pdf) |
| 10 | Day 2 | [Govern, Measure & Improve Your Human–AI Workforce](labs/lab10-paperclip-govern-measure-improve/README.md) | [PDF](labs/lab10-paperclip-govern-measure-improve/LAB-10-Instructions.pdf) |

---

## Quick start

```bash
# Hermes Agent (macOS/Linux/WSL2)
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash && hermes setup && hermes doctor

# Paperclip (Node.js 24.11+)
npx paperclipai onboard --yes        # → http://localhost:3100
```

---

## Prerequisites

- A laptop (Windows 10/11, macOS 12+, or Ubuntu 22.04+) with admin/sudo rights.
- **Node.js 24.11+** (Paperclip; or Docker Desktop) and a terminal; Windows learners use WSL2.
- At least one LLM provider — Claude Code / OpenAI Codex / OpenRouter / MiniMax / DeepSeek login or API key.
- A free **Telegram** account (Labs 3–5) and a free **Tavily** API key (Labs 1 and 7).

---

## References

- Hermes Agent: <https://hermes-agent.nousresearch.com/docs/>
- Paperclip: <https://docs.paperclip.ing>
- Course page: <https://www.tertiaryinfotech.com>

---

Provided by **Tertiary Infotech Academy Pte Ltd** (UEN 201200696W).

<sub>© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W) · WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · www.tertiaryinfotech.com</sub>
