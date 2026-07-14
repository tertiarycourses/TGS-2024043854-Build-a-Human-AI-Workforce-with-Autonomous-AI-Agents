# Lab 1 — Install and Setup Hermes

## Objective
LO1: Install and configure Hermes Agent on a local machine. By the end of this lab you will have a working Hermes Agent installation that passes `hermes doctor` and opens the TUI. This is the foundation for **Athena**, the always-on personal chief-of-staff agent you build across the whole track.

## Prerequisites
- A macOS, Linux, or Windows (native or WSL2) machine with a terminal.
- Administrator / sudo rights to install software.
- **Git** installed (required on all platforms). On Linux also `curl` and `xz-utils`. The installer auto-handles Python 3.11, Node.js v22, ripgrep and ffmpeg.
- A free [Nous Portal](https://hermes-agent.nousresearch.com/) account (you will create/sign in during the setup wizard).
- An internet connection.

> Full, always-current install reference: <https://hermes-agent.nousresearch.com/docs/getting-started/installation>

## Estimated Time
30–40 minutes

## Steps

### 1. Choose your installation method
Hermes offers several official install paths — pick the ONE that matches your machine:

| Option | Platform | How |
| --- | --- | --- |
| **A. Hermes Desktop installer** (recommended) | macOS / Windows | Download from <https://hermes-agent.nousresearch.com/> and run the installer |
| **B. Install script** | Linux / macOS / WSL2 / Android (Termux) | One-line `curl … \| bash` (Step 2) |
| **C. PowerShell** | Windows (native) | One-line `iex (irm …)` (Step 3) |
| **D. From source** | Developers | Clone the repo — see the Development Setup in the Contributing guide |
| **E. Nix / NixOS** | Nix users | Nix flake + declarative NixOS module — see the Nix & NixOS Setup guide |

> If you install via the **Desktop** app (Option A), you can skip Steps 2–3. If you install via the CLI first, you can add the desktop app later with `hermes desktop`.

### 2. Option B — install script (Linux / macOS / WSL2 / Termux)
Run the official one-line installer. It downloads the Hermes runtime, places it under your user directory, and wires up the `hermes` command:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

You should see the installer print progress, then a success message telling you the install location and a reminder to reload your shell.

### 3. Option C — Windows PowerShell (native Windows)
On native Windows (no WSL2), run the PowerShell installer instead:

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

### 4. Install Hermes Desktop (macOS / Windows)
Hermes Desktop gives you a GUI over the same agent. Either download the installer from <https://hermes-agent.nousresearch.com/> and run it, or — if you already installed the CLI in Step 2/3 — launch it directly:

```bash
hermes desktop
```

Sign in with the same Nous Portal account so the Desktop app and the CLI drive one agent.

### 5. Reload your shell so the `hermes` command is on PATH
The installer adds Hermes to your PATH via your shell profile, but your current terminal session hasn't re-read that file yet. Reload it:

```bash
source ~/.zshrc
```

> If you use bash instead of zsh, run `source ~/.bashrc` (or open a brand-new terminal window). Confirm the command resolves with `which hermes`.

### 6. Run the first-time setup wizard
Launch the interactive setup wizard and connect Hermes to your Nous Portal account. This is where you sign in, pick defaults, and let Hermes provision a model provider:

```bash
hermes setup --portal
```

Follow the prompts: authenticate in the browser window it opens (or paste the auth code), accept or adjust the default paths, and let it finish writing your configuration to `~/.hermes/`.

### 7. Check the install is healthy
Run the built-in diagnostic. It checks the binary, config, PATH, provider connectivity, and the local runtime:

```bash
hermes doctor
```

Read every line. You want all checks reporting **green / OK**. If anything is red, note it for the Troubleshooting table below before moving on.

### 8. Launch the agent and say hello
Open the terminal UI (TUI) and start your first conversation with the agent — this is Athena's very first session:

```bash
hermes --tui
```

Type a greeting such as `Hello, are you working?` and confirm the agent replies. Press the documented quit key (commonly `Ctrl+C` or `q`) to exit when done.

## Verification / Expected Output
- `hermes doctor` reports **all green** — every diagnostic line shows OK/healthy.
- `hermes --tui` opens the terminal interface, you can send a message, and the agent replies coherently.
- `~/.hermes/` now contains your configuration (created by the setup wizard).

If both the doctor is green and the TUI replies, Lab 1 is complete and Athena's runtime is live.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `hermes: command not found` after install | You didn't reload the shell — run `source ~/.zshrc` (or open a new terminal). Confirm with `which hermes`. |
| `curl` install fails or hangs | Check your internet/proxy; re-run the one-line installer. Corporate proxies may block the download host. |
| Installer complains about missing Git / build tools | Install Git (all platforms); on Linux also `curl` + `xz-utils`; for the Desktop app, `g++` / `build-essential`. |
| Setup wizard can't reach Nous Portal | Ensure you're signed in at hermes-agent.nousresearch.com; re-run `hermes setup --portal` and complete the browser auth. |
| `hermes doctor` shows a red provider/model line | No provider connected yet — finish `hermes setup --portal`, or set one up in Lab 5 (Providers & Model). |
| TUI opens but agent never replies | Provider key missing or invalid; check `hermes doctor` output and re-run setup. |

## Exercise / Challenge
Give Athena an identity on day one: in the TUI, tell the agent *"Your name is Athena and you are my personal chief of staff."* Then run `hermes doctor` again and take a screenshot of the all-green output — you'll use this as the baseline "healthy install" reference for every later lab. Bonus: if you installed via the CLI, launch the desktop app with `hermes desktop` and confirm it drives the same agent.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
