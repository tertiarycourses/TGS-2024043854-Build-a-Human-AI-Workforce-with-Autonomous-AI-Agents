# Lab 16 — Models & Providers

## Objective
Connect a language model to OpenClaw so your Nimbus Supplies agent can actually think and reply. You will try all **five** supported provider options — two OAuth sign-ins (OpenAI Codex, MiniMax) and three API-key providers (Anthropic, DeepSeek, OpenRouter) — learn where credentials are stored, switch between models, and test the active model.

## Prerequisites
- Lab 15 completed (OpenClaw installed, `openclaw gateway status` shows **running**).
- At least **one** provider account: an OpenAI/ChatGPT subscription, a MiniMax account, or an API key for Anthropic, DeepSeek, or OpenRouter.

## Estimated Time
30–40 minutes

## 📺 Reference Video
[OpenClaw reference playlist](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J)

## Steps

1. **See what is available and what is currently selected.**

   ```bash
   openclaw models list
   openclaw model current
   ```

   Or just ask the agent: "Which models can you use, and which one is active right now?"

2. **Option A — OpenAI Codex (OAuth, GPT-5.5).** OAuth uses the `openai-codex` provider so you sign in with your **ChatGPT Plus / Pro** subscription instead of paying per token. Credentials are stored in `~/.openclaw/auth/` (profile at `~/.openclaw/auth-profiles/openai-codex.json`); refresh is automatic.

   ```bash
   openclaw models auth login --provider openai-codex
   ```

   The terminal prints an authorization URL. Copy it into a browser, sign in to your OpenAI/ChatGPT account, click **Authorize OpenClaw**, then copy the **entire callback URL** (including the `?code=…`) back into the terminal. Then select the model:

   ```bash
   openclaw models set openai-codex/gpt-5.5
   openclaw models auth status
   ```

3. **Option B — MiniMax (OAuth, MiniMax-M2.7).** Enable the OAuth plugin, restart the gateway, then log in and set it as default:

   ```bash
   openclaw plugins enable minimax-portal-auth
   openclaw gateway restart
   openclaw models auth login --provider minimax-portal --set-default
   ```

   The CLI prints a **user code** and a verification URL. Open the URL, paste the code, sign in to your MiniMax account, and click **Allow**. Then pick the model (use the `-highspeed` variant for faster, cheaper replies — good for high-volume customer chat):

   ```bash
   openclaw models set minimax-portal/MiniMax-M2.7
   # or: openclaw models set minimax-portal/MiniMax-M2.7-highspeed
   ```

4. **Option C — Anthropic (API key, Claude Opus 4.7).** Get a key from <https://console.anthropic.com/settings/keys>:

   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   openclaw config set provider anthropic
   openclaw config set model anthropic/claude-opus-4-7
   openclaw model test
   ```

   Or just ask the agent: "Switch your model to Anthropic's Claude Opus 4.7"

   Or just ask the agent: "Say hello so I can confirm your model connection works"

5. **Option D — DeepSeek (API key, V4).** Get a key from <https://platform.deepseek.com/api_keys>:

   ```bash
   export DEEPSEEK_API_KEY="sk-..."
   openclaw config set provider deepseek
   openclaw config set model deepseek/deepseek-v4
   openclaw model test
   ```

6. **Option E — OpenRouter (API key, routes to Claude Opus 4.7).** Get a key from <https://openrouter.ai/keys>:

   ```bash
   export OPENROUTER_API_KEY="sk-or-..."
   openclaw config set provider openrouter
   openclaw config set model openrouter/anthropic/claude-opus-4.7
   openclaw model test
   ```

7. **Persist API keys so they survive reboots.** For the API-key providers, add the `export` line to your shell profile (`~/.zshrc` on macOS, `~/.bashrc` on Linux). OAuth tokens are persisted automatically in `~/.openclaw/auth/` and do **not** need this.

   ```bash
   echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.zshrc
   source ~/.zshrc
   ```

   Windows (PowerShell, permanent user variable):

   ```powershell
   [Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY","sk-ant-...","User")
   ```

8. **Switch models and confirm the active one.** You can hot-swap the global default at any time:

   ```bash
   openclaw model use deepseek/deepseek-v4
   openclaw model current
   openclaw model test
   ```

   Or just ask the agent: "Make DeepSeek v4 your default model from now on"

9. **Give the agent a Nimbus Supplies smoke test.** With any model active, from the CLI chat (`openclaw`) ask:

   > You are the back-office assistant for Nimbus Supplies, a small office-supplies reseller. In two sentences, introduce yourself to a customer.

   A sensible reply confirms the model is wired up.

   Or just ask the agent: "Introduce yourself in two sentences as the Nimbus Supplies back-office assistant"

## Verification / Expected Output
- `openclaw models list` shows the models you connected; `openclaw model current` prints the active one.
- `openclaw model test` returns a short successful completion (no auth error).
- For OAuth providers, `openclaw models auth status` shows a valid, non-expired session.
- `ls ~/.openclaw/auth/` shows stored credential files for OAuth providers.

  

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `openclaw model test` returns 401 / unauthorized | Key is wrong or not exported. Run `echo $ANTHROPIC_API_KEY` (etc.) and re-export. |
| OAuth callback "code invalid/expired" | The code is single-use and short-lived. Re-run `openclaw models auth login --provider …` and paste the fresh callback quickly. |
| MiniMax login command not found | You skipped `openclaw plugins enable minimax-portal-auth` + `openclaw gateway restart`. |
| Model set but agent still uses the old one | `openclaw model current` to confirm; a per-chat `/model` override may be active — see Lab 20. |
| Key works in terminal but not after reboot | You did not persist it. Add the `export` to `~/.zshrc` (Step 7). |
| Rate-limited / out of credits | Switch providers: `openclaw model use minimax-portal/MiniMax-M2.7-highspeed`. |

## Exercise / Challenge
Pick two providers you have access to and run the **same** Nimbus Supplies prompt ("Draft a polite reply to a customer asking whether we stock recycled A4 paper") through each with `openclaw model use …`. Note differences in tone, speed, and cost. Then decide which model you will make the default for customer-facing chat and which (cheaper/faster) model you would use for high-volume tasks like cron reports in Lab 21. Record your choice in a note — you will reference it in the capstone.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
