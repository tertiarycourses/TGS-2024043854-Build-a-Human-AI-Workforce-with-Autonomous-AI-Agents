# Build a Human-AI Workforce with Autonomous AI Agents

**WSQ Course · TGS-2024043854 · Tertiary Infotech Academy Pte Ltd**

| Course detail | Information |
|---|---|
| Course code | `TGS-2024043854` |
| Programme | WSQ |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/wsq-build-a-human-ai-workforce-with-autonomous-ai-agents.html) |
| Funding | Up to 70% WSQ course-fee funding for eligible learners (up to 50% baseline). Eligibility and terms apply — see the course page. |

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

## Topics and labs

| Topic | Content | Labs |
|-------|---------|------|
| 1 · Foundations | History of AI · AI agents vs agentic AI · the agentic loop · harness engineering · perception–brain–action · short/long-term memory · world models · single → multi-agent → human–agent collaboration · the 2026 agent market (OpenClaw, Hermes, Paperclip, OpenAI Dots, Meta Muse, Block Buzz, Manus Cue …) · Singapore's AgentSea · human–AI use cases (science, maths, drug discovery, business) · governance | Activity: Human–AI Workforce Canvas |
| 2 · Hermes Agent | One AI employee → a supervised multi-agent team | 1 First AI employee (research brief) · 2 End-to-end social media campaign · 3 Human-in-the-loop publishing (Telegram + cron) · 4 Multi-agent video studio (research → script → production → audit → publish) · 5 Campaign command centre (swarm + dashboard) |
| 3 · Paperclip | The same work as a governed company of agents | 6 Found the AI company · 7 Hire the team (approval gate) · 8 Launch campaign project · 9 Weekly video routine · 10 Govern, measure & improve |

See the [labs index](labs/README.md) for durations and instruction PDFs.

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

<sub>© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W) · WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · www.tertiaryinfotech.com</sub>
