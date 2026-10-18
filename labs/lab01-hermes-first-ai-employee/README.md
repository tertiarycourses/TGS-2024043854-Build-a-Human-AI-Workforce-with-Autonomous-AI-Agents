# Lab 1 — Hire Your First AI Employee — Customer & Market Research Brief

**Day 1 · Topic 2 · 55 min · Single agent · LO1**

> Install Hermes, give it company context and long-term memory, and let one agent turn raw reviews and live web research into a brief you can act on.

## Goal
Install and configure an autonomous LLM agent, give it context and long-term memory, and analyse its perception → reasoning → action loop on a real research task (LO1).

## The business scenario
You are Kopi Kaki Co.'s Marketing Lead. The Gula Melaka Cold Brew launches on 1 Dec and you have 60 unread customer reviews, a competitor list and no analyst. You 'hire' Mia — a Hermes Agent marketing analyst — onboard her with the company context, and ask for a research brief that tells you which campaign angle to run.

## You will deliver
- outputs/lab01/review-insights.md — ratings, themes and evidence (review IDs)
- outputs/lab01/research-brief.md — trends, competitors, 3 campaign angles with evidence
- Mia's long-term memory holds the brand facts and YOUR chosen angle (recalled in a new session)

## Who does what
- **Agents:** 1 Hermes agent — 'Mia', AI marketing analyst
- **You (the human):** Set the goal, challenge the evidence, choose the campaign angle

## Before you start
- A laptop (macOS, Linux or Windows with WSL2) with admin rights and internet access
- An LLM provider sign-in or API key (Nous Portal, OpenRouter, OpenAI/Codex, Anthropic)
- This lab folder downloaded (course repo → Code → Download ZIP)

## Concepts in action
- Perception (files + web) → Brain (LLM reasoning, memory) → Action (write files)
- AGENTS.md = context the agent loads automatically (context engineering)
- Short-term memory (this session) vs long-term memory (MEMORY.md, recalled next session)
- Human-in-the-loop: the agent recommends, the human decides

## Lab files (`data/`)

| File | What it is |
|---|---|
| `AGENTS.md` | Company context Hermes loads automatically |
| `brand-guide.md` | Brand voice, colours, platform formats |
| `campaign-brief.md` | Gula Melaka Cold Brew campaign brief (offer, KPIs, timeline) |
| `compliance-rules.md` | C1–C10 brand-safety and escalation rules |
| `product-catalogue.csv` | 12 products and prices |
| `customer-reviews.csv` | 60 synthetic customer reviews |
| `competitors.csv` | 6 fictional competitors |
| `assets/brand-palette.png` | Brand image asset |
| `assets/cold-brew-product-card.png` | Brand image asset |
| `assets/kopi-kaki-logo.png` | Brand image asset |

_All company data in this lab (Kopi Kaki Co., people, reviews, comments, metrics, competitors) is fictional and generated for training._

Copy-ready prompts: [`COPY-PROMPTS.txt`](COPY-PROMPTS.txt) or the course [Lab Prompts page](../../prompts/index.html). Printable instructions: [`LAB-01-Instructions.pdf`](LAB-01-Instructions.pdf).

## Steps

### 1. Install Hermes Agent (skip if your trainer pre-installed it)
macOS / Linux / WSL2 — run the one-line installer in Terminal. Windows — use the PowerShell installer (or install inside WSL2). The installer sets up Python, Node.js, ripgrep and ffmpeg for you.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
# Windows PowerShell:  iex (irm https://hermes-agent.nousresearch.com/install.ps1)
source ~/.zshrc    # or ~/.bashrc — puts 'hermes' on your PATH
```

✅ **Expected:** `hermes --version` prints a version number.

### 2. Connect a model and check health
Run the setup wizard and choose a provider (Nous Portal, OpenRouter, OpenAI/Codex, Anthropic …). Pick a model with a context window of at least 64,000 tokens. Then run the doctor.

```bash
hermes setup
hermes doctor
```

✅ **Expected:** `hermes doctor` shows green checks for the model and tools.

### 3. Create the Kopi Kaki workspace and add the lab data
Download this lab's folder (or the whole course repo) and copy everything in `data/` into a new folder `~/kopi-kaki`. Hermes automatically loads `AGENTS.md` from the folder you start it in — that is how Mia learns who the company is.

```bash
mkdir -p ~/kopi-kaki/outputs/lab01
cp -R data/* ~/kopi-kaki/
cd ~/kopi-kaki
hermes
```

✅ **Expected:** The Hermes chat opens. Type `/help` to see slash commands.

### 4. Onboard Mia — persona and long-term memory
**Prompt** — paste into *Hermes chat (started inside ~/kopi-kaki)*:

```text
You are Mia, Kopi Kaki Co.'s AI marketing analyst. Read AGENTS.md, brand-guide.md and campaign-brief.md in this folder.

Save these facts to your long-term memory:
- Kopi Kaki Co.: Singapore kopi chain, 12 outlets, positioning "Heritage kopi, modern craft".
- Launch: Gula Melaka Cold Brew, SGD 6.80, launches 1 Dec 2026, campaign #ShiokColdBrew 17 Nov - 14 Dec.
- Promo SHIOK20: 20% off the first Gula Melaka Cold Brew ordered in the app, valid 1-14 Dec 2026, one per customer.
- Never publish anything without my APPROVE. Never make health or halal claims.

Then summarise the company in 5 bullets and ask me the 3 questions a new analyst should ask on day one.
```

✅ **Expected:** Mia confirms the memory was saved and returns 5 bullets + 3 questions. Check the file itself: `cat ~/.hermes/memories/MEMORY.md` shows the facts.

### 5. Perceive the data — analyse 60 customer reviews
**Prompt** — paste into *Hermes chat*:

```text
Analyse customer-reviews.csv.
1. Rating distribution (count and % for 1-5 stars) and average rating per outlet.
2. The top 5 praise themes and top 5 complaint themes, each with a count and 2 example review_ids.
3. Anything relevant to a cold-brew launch (mentions of cold brew, sweetness, oat milk, app).
Show your calculation method. Save the result as outputs/lab01/review-insights.md.
```

✅ **Expected:** A Markdown report with a ratings table and themes that cite review IDs (e.g. R1012).

### 6. Perceive the world — live web research
**Prompt** — paste into *Hermes chat*:

```text
Use web search to research specialty coffee and cold-brew trends in Singapore in 2026 (consumer preferences, price points, social media formats that work). Combine this with competitors.csv (the competitors are fictional - treat them as our internal notes).
Rules: cite every web fact with its URL; mark anything you could not verify as UNVERIFIED; do not invent statistics.
```

✅ **Expected:** 5+ cited findings with URLs and a competitor comparison table.

### 7. Act — write the research brief
**Prompt** — paste into *Hermes chat*:

```text
Write outputs/lab01/research-brief.md for the Marketing Lead with:
1. Executive summary (5 lines).
2. What our customers say (from review-insights.md).
3. Market & competitor snapshot (cited).
4. Three campaign angles for #ShiokColdBrew. For each: the big idea, target audience, supporting evidence (review IDs or URLs), the KPI it drives, and one risk.
5. A final section "Decision needed" asking me to choose one angle.
Follow the brand guide and compliance rules.
```

✅ **Expected:** research-brief.md with three evidence-backed angles and a 'Decision needed' section.

### 8. Human checkpoint — challenge, then decide
Read the brief like a manager. Challenge at least one claim, then make the decision and tell Mia to remember it.

**Prompt** — paste into *Hermes chat*:

```text
Which review_ids support angle 2? Quote them. Then: I choose angle <1|2|3> because <your reason>. Save my decision and reason to long-term memory, and add a "Decision log" section to research-brief.md.
```

✅ **Expected:** Mia quotes the supporting reviews, updates the brief and confirms the memory write.

### 9. Test long-term memory in a brand-new session
First confirm the decision is in the memory file. Then exit with `/exit`, start a fresh session and ask Mia what she remembers. A new session has an empty short-term memory; memory files load at session start, so the answer should come from MEMORY.md (ask her where it came from — 'I'll remember' in a chat is not proof).

```bash
cat ~/.hermes/memories/MEMORY.md
hermes
```

**Prompt** — paste into *New Hermes chat*:

```text
Which campaign angle did I choose, and why? What is the promo code and its terms? Tell me whether you got this from your memory file or by searching past sessions.
```

✅ **Expected:** Mia answers correctly without re-reading the files.

## Verification / checkpoint
- [ ] outputs/lab01/review-insights.md and research-brief.md exist and cite review IDs / URLs
- [ ] The brief ends with a decision log naming the angle you chose
- [ ] MEMORY.md contains the brand facts and your decision
- [ ] A new session recalls the chosen angle and the SHIOK20 terms
- [ ] PP evidence: take ONE screenshot now of the research brief or the memory recall — Task 1 of the Practical Performance uses it

**Checkpoint:** Every insight cites review IDs or a URL; the angle you chose is recalled in a brand-new session.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `hermes: command not found` | Open a new terminal or run `source ~/.zshrc` (macOS) / `source ~/.bashrc` (Linux/WSL2). |
| Model errors / context too small | Re-run `hermes setup` (or `hermes model`) and choose a model with ≥ 64k context. |
| Web search not available | Run `hermes tools` and enable the web toolset. Keyless search works for light use; for reliability add a free key, e.g. `hermes config set TAVILY_API_KEY tvly-...` (you reuse it on Day 2). |
| Windows paths | On native Windows Hermes keeps its data in %LOCALAPPDATA%\hermes instead of ~/.hermes — or run the labs inside WSL2. |
| Mia ignores the brand rules | Make sure you started `hermes` inside ~/kopi-kaki so AGENTS.md is loaded. |

## Stretch challenge
Ask Mia: "Save the review-analysis procedure you just used as a reusable skill called review-insights." Then run `hermes skills list` — a self-improving agent turns experience into procedural memory.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
