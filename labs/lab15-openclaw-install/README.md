# Lab 15 — Install OpenClaw

## Objective
Install the **OpenClaw** agent platform on your own machine (Windows, macOS, or Linux) **or** on a cloud VPS, then verify the install with `openclaw doctor` and `openclaw gateway status`. By the end you will have a running OpenClaw gateway that will become the back-office brain of a small business we call **Nimbus Supplies** — the running example that threads through Labs 15–20.

## Prerequisites
- A laptop running Windows 10/11 (WSL2 recommended), macOS 12+, or Ubuntu 22.04+.
- Admin / sudo rights on the machine and a terminal you are comfortable with.
- **Node.js 24 LTS** (minimum supported is **22.16+**). We install it in Step 1.
- Internet access and roughly 2 GB free disk.
- Optional (for the cloud portion): a **Hostinger** VPS or an **[exe.dev](https://exe.dev/)** sandbox account.

## Estimated Time
30–40 minutes

## 📺 Reference Video
[OpenClaw reference playlist](https://www.youtube.com/watch?v=q5YFlpVlmkI&list=PLHutrxqbP1BwAQf6dROCLZqK0PLpGu35J)

## Steps

1. **Install Node.js 24 LTS (24 recommended; 22.16+ minimum).** OpenClaw runs on Node.

   **Windows** — download the **Node 24 LTS** installer from <https://nodejs.org/> and run the `.msi` (WSL2 is recommended for stability), then check:

   ```powershell
   node -v
   npm -v
   ```

   **macOS**:

   ```bash
   brew install node@24
   node -v && npm -v
   ```

   **Linux (Ubuntu / Debian)**:

   ```bash
   curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -
   sudo apt-get install -y nodejs
   node -v && npm -v
   ```

   

2. **Install OpenClaw — Option A (npm, recommended, cross-platform).** After Node is installed:

   ```bash
   npm install -g openclaw@latest
   openclaw onboard
   ```

   `openclaw onboard` launches an interactive wizard that creates `~/.openclaw/`, installs the background gateway, and offers to connect a model provider (we do providers properly in Lab 16 — you can skip the provider step here).

3. **Install OpenClaw — Option B (installer script, fallback if npm fails).**

   **macOS / Linux / WSL2:**

   ```bash
   curl -fsSL https://openclaw.ai/install.sh | bash
   ```

   **Windows (PowerShell, run as Administrator):**

   ```powershell
   iwr -useb https://openclaw.ai/install.ps1 | iex
   ```

   > Piping a remote script to a shell runs remote code. If your policy requires it, read it first (`curl -fsSL https://openclaw.ai/install.sh | less`). Confirm the current URL at <https://docs.openclaw.ai/install>.

4. **Install OpenClaw — Option C (from source, advanced).** Requires `git` and `pnpm`:

   ```bash
   git clone https://github.com/openclaw/openclaw.git
   cd openclaw
   pnpm install && pnpm build && pnpm ui:build
   pnpm link --global
   openclaw onboard --install-daemon
   ```

5. **(Optional) Install on a VPS so Nimbus Supplies runs 24/7.** The same three-step flow works on any Ubuntu host — a **Hostinger** KVM VPS or an **exe.dev** sandbox. SSH in first (`ssh root@<your-vps-ip>`), then run:

   ```bash
   # Step 1 — Node.js 24
   curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -
   sudo apt-get install -y nodejs
   node -v && npm -v

   # Step 2 — OpenClaw (note: sudo for a global install on a fresh VPS)
   sudo npm install -g openclaw@latest

   # Step 3 — onboarding wizard
   openclaw onboard
   ```

   > **Note:** exe.dev storage can be ephemeral — back up `~/.openclaw/` if you want agent state to survive rebuilds.

   

6. **Verify the installation.**

   ```bash
   openclaw --version
   openclaw doctor
   openclaw gateway status
   ```

   `openclaw doctor` runs a health check (Node version, gateway daemon, providers, channels). It is normal for the provider and channel checks to be "not configured" at this point — you wire those up in Labs 16 and 17.

7. **Confirm the gateway is running (and set to auto-start).** The gateway is the long-running daemon that will host every channel, tool, and cron for Nimbus Supplies:

   ```bash
   openclaw gateway status
   openclaw gateway start   # if it is not already running
   ```

## Verification / Expected Output
- `openclaw --version` prints a version number.
- `openclaw doctor` shows green checks for Node and the gateway. Example:

  ```text
  OpenClaw — Doctor
  ✔ Node.js v24.x (>= 22.16 required)
  ✔ gateway daemon installed
  ✔ config directory: ~/.openclaw
  – no model provider configured (connect one in Lab 16)
  – no channels configured (add one in Lab 17)
  ```

  

- `openclaw gateway status` reports **running**.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `openclaw: command not found` | Reopen your terminal, or add `~/.openclaw/bin` to your `PATH`. On zsh: `source ~/.zshrc`. |
| Node version too old error | You have < 22.16. Reinstall Node 24 LTS (Step 1) and re-run `node -v`. |
| `gateway not running` | `openclaw gateway start`, then re-check `openclaw gateway status`. |
| PowerShell: "running scripts is disabled" | `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then re-run the `iwr … | iex` line. |
| WSL2 not available on Windows | Run `wsl --install` in an elevated PowerShell, reboot, then use the macOS/Linux `curl` install inside WSL. |
| npm global install permission denied (VPS) | Use `sudo npm install -g openclaw@latest`, or configure an npm prefix you own. |

## Exercise / Challenge
Run `openclaw doctor` and copy its full output into a note. For every line that is **not** a green check, write one sentence naming the lab that will resolve it (model provider → Lab 16, channels → Lab 17, tools → Lab 19). Then, if you have a VPS or exe.dev sandbox, repeat the install there and confirm you can reach the same `openclaw gateway status` output over SSH — this is the deployment you will grow into an always-on Nimbus Supplies back office by Lab 24.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
