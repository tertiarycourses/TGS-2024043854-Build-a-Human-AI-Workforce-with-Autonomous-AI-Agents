# Lab 6 — MCP and Tools

## Objective
LO3: Give the agent real-world reach with MCP servers and the Tool Gateway. You will add a Model Context Protocol (MCP) server in the Hermes config and use the bundled Tool Gateway (web search, image generation, TTS) so **Athena** can act on the outside world.

## Prerequisites
- **Lab 1–5 complete** — Hermes installed, a provider/model connected.
- Node.js / `npx` available (for the GitHub MCP server).
- A GitHub account/token if the MCP server needs authenticated access.

## Estimated Time
35–45 minutes

## 📺 Reference Video
[MCP and Tools](https://www.youtube.com/watch?v=U140gP-1bEI&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=7)

## Steps

### 1. Watch the reference video
See how MCP servers are declared in config and how the Tool Gateway tools are called from chat:

[https://www.youtube.com/watch?v=U140gP-1bEI&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=7](https://www.youtube.com/watch?v=U140gP-1bEI&list=PLmpUb_PWAkDx-VWjh00tVCji794xAa_IX&index=7)

### 2. Open the Hermes config to add an MCP server
Edit your Hermes config file and locate (or create) the `mcp_servers:` section:

```bash
# edit ~/.hermes/config.yaml -> mcp_servers:
```

Open `~/.hermes/config.yaml` in your editor. MCP servers are declared under an `mcp_servers:` key.

### 3. Add a GitHub MCP server entry
Add an entry that launches the official GitHub MCP server via `npx`. A typical block looks like this:

```yaml
mcp_servers:
  github:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_your_token_here"
```

The core command Hermes will run is:

```bash
npx -y @modelcontextprotocol/server-github
```

Save the file. Supply a GitHub personal access token in `env` if the server needs authenticated access.

> If your Hermes build uses a slightly different config schema for MCP, verify the exact keys in the video / Hermes docs (https://hermes-agent.nousresearch.com/docs/).

### 4. Restart so the MCP server is picked up, then verify
Restart Hermes (close and reopen the TUI, or restart the gateway) so it reads the new config, then run the diagnostic:

```bash
hermes doctor
```

`hermes doctor` should now show the GitHub MCP server connected and its tools available. Confirm there are no red lines for the new server.

### 5. Use a Tool Gateway tool from a chat
Open the TUI and ask Athena to use a bundled Tool Gateway capability — web search, image generation, or text-to-speech:

> This step is conversational. For example: *"Search the web for today's top AI agent news and list 3 headlines,"* or *"Generate an image of a friendly robot assistant."* Confirm the agent invokes the tool and returns the result.

### 6. The natural-language way
You can skip the CLI entirely and simply ask the agent: *"Add the GitHub MCP server to your tools and list what it can do"*.

## Verification / Expected Output
- The agent **lists the new MCP server's tools** (e.g. GitHub repo/issue tools).
- The agent **completes a task using a Tool Gateway tool** (web search / image / TTS) — you get real output back.
- `hermes doctor` shows the MCP server healthy.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| MCP server not listed after edit | You didn't restart Hermes, or the YAML is malformed — validate indentation under `mcp_servers:` and restart. |
| GitHub MCP server fails to start | Ensure `npx`/Node is installed; run `npx -y @modelcontextprotocol/server-github` manually to see the error. |
| GitHub tools return 401/403 | Missing/invalid `GITHUB_PERSONAL_ACCESS_TOKEN` — add a valid token in the `env:` block. |
| Tool Gateway tool does nothing | Confirm the Tool Gateway is enabled and your provider allows tool calls; check `hermes doctor`. |
| Unsure of the config schema | Verify the exact `mcp_servers` keys in the video / docs link above. |

## Exercise / Challenge
Give Athena a task that combines an MCP server with a Tool Gateway tool: *"Find the latest open issue in <your-github-repo>, then draft a short reply and read it back to me with text-to-speech."* Confirm the agent uses the GitHub MCP tool to read the issue and the TTS tool to speak the draft — a genuine outside-world action chain.

<sub>Part of the WSQ course **Build a Human-AI Workforce with Autonomous AI Agents** (TGS-2024043854) · © 2026 Tertiary Infotech Academy Pte Ltd · www.tertiarycourses.com.sg</sub>
