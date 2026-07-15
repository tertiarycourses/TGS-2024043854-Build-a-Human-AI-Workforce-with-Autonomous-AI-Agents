# Lab 5 — Providers & Model

## Objective
LO2: Connect an LLM provider and switch models with no lock-in. You will connect a model provider (Nous Portal, OpenRouter, OpenAI, or any endpoint) and select a model that meets the **≥64,000-token context** requirement, then switch providers to compare speed and quality — keeping **Athena** provider-agnostic.

## Prerequisites
- **Lab 1–4 complete** — Hermes installed and running.
- At least one provider available: a Nous Portal account (from setup) and/or an API key for OpenRouter/OpenAI.

## Estimated Time
25–35 minutes

## 📺 Reference Video
[Providers & Model](https://www.youtube.com/watch?v=1oaaOWy7wSI&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=6)

## Steps

### 1. Watch the reference video
See how providers are connected and how to switch models on demand:

[https://www.youtube.com/watch?v=1oaaOWy7wSI&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=6](https://www.youtube.com/watch?v=1oaaOWy7wSI&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=6)

### 2. Open the interactive provider/model picker
Launch the interactive picker to see available providers and models and select one:

```bash
hermes model
```
Or just ask the agent: "Show me the available providers and models, and which one you're on"


Use the arrow keys to browse providers and their models. Pay attention to each model's context window — you need one that supports at least 64,000 tokens.

### 3. Set a model explicitly
Instead of (or in addition to) the picker, set the active model directly in config:

```bash
hermes config set model anthropic/claude-opus-4.6
```
Or just ask the agent: "Switch yourself to Claude Opus 4.6"


This writes the model choice to your Hermes config so every new session uses it. Substitute another `provider/model` string if you prefer a different model — the format stays `provider/model`.

### 4. Add a provider key if using a cloud endpoint
If your chosen model runs on a cloud endpoint (e.g. OpenRouter), store the API key in config so Hermes can authenticate:

```bash
hermes config set OPENROUTER_API_KEY sk-or-...
```
Or just ask the agent: "Add my OpenRouter API key to your provider config"


Replace `sk-or-...` with your real OpenRouter key. For other providers, set the matching `<PROVIDER>_API_KEY` variable.

### 5. Confirm the active model meets the ≥64k context rule
Reopen the picker to confirm the active model and its context window:

```bash
hermes model
```
Or just ask the agent: "Confirm your active model has at least a 64k context window"


Verify the selected model reports a context window of **≥64,000 tokens**. This is a hard requirement for the Athena workflows later in the track (long briefings, multi-document context).

## Verification / Expected Output
- The agent **starts on the selected model** (visible in `hermes model` / new sessions).
- You can **switch to another provider/model without reinstalling** Hermes — just re-run the picker or `hermes config set model ...`.
- The active model's context window is **≥64,000 tokens**.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `hermes model` shows no models for a provider | The provider isn't authenticated — add its key with `hermes config set <PROVIDER>_API_KEY <value>`. |
| Chosen model rejects requests (401/403) | Invalid or missing API key; re-set it and confirm no trailing spaces. |
| Selected model has < 64k context | Pick a larger-context model in `hermes model`; the track requires ≥64k. |
| Model set but sessions still use the old one | Restart the TUI/gateway so the new config is loaded; confirm with `hermes model`. |
| Want to compare speed/quality | Set one model, run a prompt, switch with `hermes config set model ...`, run the same prompt, and compare. |

## Exercise / Challenge
Run the **same** prompt (e.g. *"Draft a 200-word status update to my board"*) on two different providers/models. Record latency and note quality differences in a short table. Then set Athena back to your preferred ≥64k model. This demonstrates the "no lock-in" advantage in practice.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
