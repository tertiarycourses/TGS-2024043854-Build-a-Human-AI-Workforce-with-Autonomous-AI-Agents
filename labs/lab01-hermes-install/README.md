# Lab 1 — Install and Setup Hermes

## Objective
LO1: Install and configure Hermes Agent on a local machine. By the end of this lab you will have a working Hermes Agent installation that passes `hermes doctor` and opens the TUI. This is the foundation for **Athena**, the always-on personal chief-of-staff agent you build across the whole track.

## Prerequisites
- A macOS, Linux, or Windows-with-WSL2 machine with a terminal.
- Administrator / sudo rights to install a CLI tool.
- A free [Nous Portal](https://hermes-agent.nousresearch.com/) account (you will create/sign in during the setup wizard).
- `curl` and a POSIX shell (`bash`/`zsh`) available on PATH.
- An internet connection.

## Estimated Time
30–40 minutes

## 📺 Reference Video
[Install and Setup Hermes — Hermes Agent playlist](https://www.youtube.com/watch?v=KtlY6ETPyKo&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=11)

## Steps

### 1. Watch the reference video
Before touching the terminal, watch the reference video end to end so you know what a healthy install looks like and can spot where the UI differs from these written steps:

[https://www.youtube.com/watch?v=KtlY6ETPyKo&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=11](https://www.youtube.com/watch?v=KtlY6ETPyKo&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=11)

### 2. Install Hermes (macOS / Linux / WSL2)
Run the official one-line installer. It downloads the Hermes binary, places it under your user directory, and wires up the `hermes` command:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

You should see the installer print progress, then a success message telling you the install location and, usually, a reminder to reload your shell.

### 3. Reload your shell so the `hermes` command is on PATH
The installer adds Hermes to your PATH via your shell profile, but your current terminal session hasn't re-read that file yet. Reload it:

```bash
source ~/.zshrc
```

> If you use bash instead of zsh, run `source ~/.bashrc` (or open a brand-new terminal window). Confirm the command resolves with `which hermes`.

### 4. Run the first-time setup wizard
Launch the interactive setup wizard and connect Hermes to your Nous Portal account. This is where you sign in, pick defaults, and let Hermes provision a model provider:

```bash
hermes setup --portal
```

Follow the prompts: authenticate in the browser window it opens (or paste the auth code), accept or adjust the default paths, and let it finish writing your configuration to `~/.hermes/`.

### 5. Check the install is healthy
Run the built-in diagnostic. It checks the binary, config, PATH, provider connectivity, and the local runtime:

```bash
hermes doctor
```

Read every line. You want all checks reporting **green / OK**. If anything is red, note it for the Troubleshooting table below before moving on.

### 6. Launch the agent and say hello
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
| Setup wizard can't reach Nous Portal | Ensure you're signed in at hermes-agent.nousresearch.com; re-run `hermes setup --portal` and complete the browser auth. |
| `hermes doctor` shows a red provider/model line | No provider connected yet — finish `hermes setup --portal`, or set one up in Lab 5 (Providers & Model). |
| TUI opens but agent never replies | Provider key missing or invalid; check `hermes doctor` output and re-run setup. |

## Exercise / Challenge
Give Athena an identity on day one: in the TUI, tell the agent *"Your name is Athena and you are my personal chief of staff."* Then run `hermes doctor` again and take a screenshot of the all-green output — you'll use this as the baseline "healthy install" reference for every later lab.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
