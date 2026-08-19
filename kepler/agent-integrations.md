---
title: Agent Integrations
description: Kepler runs the coding agent you already have. Connect Claude Code, Codex, GitHub Copilot, Cursor, Auggie, or OpenCode, or point Kepler at your own ACP server.
product: Kepler
feature: Agent Integrations
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode]
hosted_variant: both
status: GA
last_verified: 2026-08
llms_include: true
tags: [agent-integrations, claude-code, codex, copilot, cursor, auggie, opencode, acp, setup, settings]
taxonomy:
  category: kepler
---
<kbd>Last updated: August 2026</kbd>

Kepler runs the coding agent you already have. You sign in with your own agent account, and Kepler adds no markup on the agents you bring.

Kepler ships support for six agents, and you can point it at any other agent that speaks the Agent Client Protocol (ACP).

All of it lives in **Settings → Agents**.

<!-- TODO(screenshot): Settings → Agents, showing the Default agent row and the six agent sections with their status badges. The existing _images/agents-view.png and _images/agent-settings.png predate this layout. -->

***

## The six supported agents

Each agent gets its own section in **Settings → Agents**, in this order:

| Agent | Name in Settings | How Kepler runs it | Multiple accounts |
|---|---|---|---|
| **Claude Code** | Claude Code | Your installed `claude` CLI, over ACP or in an embedded terminal | Yes |
| **Codex** | Codex | A bundled `codex-acp` engine — no separately installed CLI needed | Yes |
| **GitHub Copilot** | GitHub Copilot | Your installed `copilot` CLI in ACP mode (`--acp`) | Yes |
| **Cursor** | Cursor CLI | Your installed `cursor-agent` CLI in ACP mode (`acp`) | No |
| **Auggie** | Auggie | Your installed `auggie` CLI in ACP mode (`--acp`) | Yes |
| **OpenCode** | OpenCode | Your installed `opencode` CLI in ACP mode (`acp`) | No |

**Auggie** is Augment's coding agent. It runs over the same ACP path as the rest, and its model and mode pickers work like any other agent's. It is also one of the three agents that report plan usage back to Kepler, alongside Claude Code and Codex — Auggie reports a billing cycle and a credit balance rather than rolling windows. See [Agent Sessions](/kepler/agent-sessions) for the **Token usage** chip and the opt-in it needs.

**Codex is bundled.** Its section reads **Bundled** rather than **Installed**, and it has no binary picker — Codex sessions and local sign-in run on the engine Kepler ships, not on a `codex` CLI you install yourself.

Two agents need a recent enough build to be driven over ACP:

| Agent | Minimum |
|---|---|
| **GitHub Copilot** | CLI v1.0 or newer. Older builds reject `--acp` |
| **Cursor CLI** | A build that exposes the `acp` command, added in early 2026 |

Kepler checks both before it starts a session and tells you to update rather than failing with a protocol error.

***

## Install an agent

When an agent is not installed, its section reads **Not installed** and offers **Install**. Kepler runs the install command on your behalf and streams the output, so you can read a failure rather than guess at one.

Kepler declares install methods per operating system, so the list you see depends on the machine you're on:

| Agent | macOS | Linux | Windows |
|---|---|---|---|
| **Claude Code** | Native installer, Homebrew, npm (global) | Native installer, npm (global) | Native installer, winget, npm (global) |
| **Codex** | Bundled — nothing to install | Bundled — nothing to install | Bundled — nothing to install |
| **GitHub Copilot** | Native installer, Homebrew, npm (global) | Native installer, Homebrew, npm (global) | winget, npm (global) |
| **Cursor CLI** | Native installer, Homebrew | Native installer | Native installer |
| **Auggie** | npm (global) | npm (global) | npm (global) |
| **OpenCode** | Native installer, Homebrew, npm (global) | Native installer, Homebrew, npm (global), pacman | scoop, Chocolatey, npm (global) |

If an agent offers no install method for your OS, Kepler says so and points you at the custom binary path instead.

Kepler doesn't close the install output pane automatically when the install finishes. Mid-run errors — a permissions failure, a partial install, a post-install warning — surface only in that pane, so read them before you dismiss it.

***

## Binary detection

Kepler resolves each agent's binary the way your shell does: the first match on your `PATH`, so it agrees with `which`. Beyond `PATH`, it also sweeps your login shell's environment and well-known install directories. That's how Kepler finds an agent installed by nvm or Homebrew, even when you didn't launch Kepler from a terminal.

Open **Configure** on an agent's section to see and change what it resolved:

| Control | What it does |
|---|---|
| Status | **Installed**, **Bundled** (Codex), or **Not installed** |
| **Install** | Runs one of the install methods above. Shown when the agent is not installed |
| **Binary** | The resolved absolute path, or **Not found**, with where it came from (**PATH**, **Shell**, or **Common**) and its version |
| **Re-scan** | Re-detects this agent's binary. Use it after installing or removing one outside Kepler |
| **Custom path…** | Pins an absolute path of your own. Kepler validates it and refuses a directory or a path that is not a file |
| **Clear custom** | Drops the pinned path and goes back to automatic resolution. Shown only while a custom path is set |
| **Installed versions** | A picker listing every install Kepler found, with an **Auto** row. Appears only when Kepler finds more than one |
| **Data directory** | Overrides the agent's own data and config directory. Leave it empty for the agent default |
| **Enabled** | Whether Kepler offers this agent when you start a session |

If a pinned path later disappears — for example, when an auto-updater cleans up an old version — Kepler falls back to automatic resolution instead of reporting the agent as missing.

**Settings → Agents → Agent options → Installed agents** carries a **Refresh** button that re-scans every agent at once.

<!-- TODO(screenshot): one expanded agent section showing the Binary group — resolved path, source and version, Re-scan, Custom path…, and the Data directory field. -->

***

## Sign in to an agent

An installed agent shows **Sign in** until it has a credential, and **Sign out** once it does. **Sign in** opens a modal listing the methods that agent supports on this machine, plus any methods Kepler owns itself:

| Agent | How you sign in |
|---|---|
| **Claude Code** | Browser sign-in. Kepler runs the sign-in for you and your browser opens; you paste a code back only if the browser callback cannot reach Kepler |
| **Codex** | Sign in with a ChatGPT account through your browser, or supply an API key |
| **GitHub Copilot** | **Sign in with GitHub** — Kepler's own device flow. Open `github.com/login/device` and enter the one-time code |
| **Cursor CLI** | Cursor's own browser sign-in, driven from the modal. You can instead set `CURSOR_API_KEY` |
| **Auggie** | **Sign in with browser**, or **Paste session token** |
| **OpenCode** | Nothing to do in Kepler. OpenCode resolves providers from its own config file and provider environment variables |

### Browser sign-in, including over SSH

**Claude Code** and **Codex** both sign in through your browser, and neither drops you into a terminal to do it.

That holds on a [remote environment](/kepler/remote-environments) too:

- **Claude Code** over SSH offers **Sign in with browser**, which opens the sign-in page in your *local* browser and takes the code you paste back. The credential lands on the remote machine.
- **Codex** over SSH opens ChatGPT sign-in in your local browser and bridges the callback over your SSH connection. The token is written on the remote machine and never passes through Kepler.

Codex's browser sign-in on a remote target is the one flow with a condition on it: it needs the desktop app driving a window bound to an **SSH** host. Every client operating system qualifies, and Kepler doesn't require an SSH ControlMaster — one is a fast path, not a prerequisite. It is not offered in a browser client, and it does not apply to a [WSL environment](/kepler/remote-environments), which has no SSH connection to bridge the callback over.

Where it does not apply, **Import local Codex login** does the job: it copies this machine's `~/.codex/auth.json` to the remote target. That entry appears on every remote binding in the desktop app, so it also sits alongside the browser flow when both are available. Treat this import as handing over a credential — anyone with access to that remote machine can send Codex requests on your account until you sign out.

### Auggie's two methods

Auggie supports two sign-in methods:

| Method | What it does | Where it works |
|---|---|---|
| **Sign in with browser** | Runs Auggie's sign-in and finishes it in your browser. Auggie stores the credential under `~/.augment` | Local, and over SSH — the remote variant opens the page in your local browser and takes a pasted JSON response |
| **Paste session token** | You paste the JSON from `auggie token print` into Kepler. Kepler stores it and supplies it on every session | Anywhere, including CI-style setups with no browser |

If you run Auggie's browser sign-in on this machine yourself, Kepler detects it and you can skip the token paste.

### Multiple accounts of one agent

**Claude Code**, **Codex**, **GitHub Copilot**, and **Auggie** support more than one signed-in account. **Configure → Accounts → Add account** adds one; each account keeps its own credentials and history.

For **Auggie**, you can only add a second account with **Paste session token**. Its browser sign-in writes to one fixed file, so it would sign the second account into the first account's identity.

<!-- TODO(verify): checked again at kepler 7c31af83e — settings.agents.accountsHelp in src/shared/i18n/locales/en.ts is STILL worded for Claude Code ("Run multiple Claude Code logins side by side…") while the Accounts group renders for Codex, GitHub Copilot and Auggie too. This page does not quote the string, so it is a product-copy bug to raise rather than a docs fix; drop this comment once the copy is generalized. -->

***

## Claude Code modes

Claude Code is the one agent you can run two ways. **Configure → Default mode for new sessions** picks which:

| Mode | What you get |
|---|---|
| **Rich chat** | The full visual experience — plans, model and effort controls, richer input. This is the default |
| **Terminal** | Claude as a command-line session in an embedded terminal, the same as the Claude Code CLI |

You can switch modes inside a running session without losing the conversation.

**Detect Claude Code sessions started outside Kepler** is a separate, off-by-default setting. Turning it on adds hooks to `~/.claude/settings.json` so sessions you start in your own terminal show up in Kepler. In **Terminal** mode, Claude Code runs as a plain terminal command, so leave detection on if you want Kepler to track those sessions.

***

## Your default agent

**Settings → Agents → Default agent** sets which agent is preselected when you start work, and supplies the model, mode, and thinking effort a new session starts with.

Kepler saves agent options **per account**. Picking a different account of the same agent brings up that account's own saved model and options, so a heavier model on your work account doesn't follow you onto your personal one.

Only agents that are installed and **Enabled** appear in the picker. If your saved default is no longer installed, Kepler says so and asks you to pick another.

An Action can override all of this. See [Actions](/kepler/actions) for how an Action pins a provider, account, model, mode, and options together, and which choice wins when they disagree.

***

## Custom ACP servers

If your agent speaks ACP, Kepler can run it without any Kepler-side change. Open **Settings → Agents → Custom agent servers → Add** and fill in these fields:

| Field | What it holds |
|---|---|
| **Name** | What the agent is called in Kepler's pickers |
| **Command** | The binary to run — an absolute path, or a name Kepler resolves on your `PATH` |
| **Args (one per line)** | Arguments that put your agent into ACP mode, for example `--acp` |
| **Environment variables (KEY=value, one per line)** | Variables merged into the agent's environment on every session |

Kepler treats environment values as secrets: it hides them after you save and never sends them to any client. When you edit a server, leaving a value empty (`KEY=`) keeps the stored secret, and typing a new value replaces it.

Custom servers appear alongside the built-in agents everywhere you can choose an agent.

***

## What Kepler tells the agent about itself

Agent CLIs report **Kepler** as the client name, so your sessions show up as Kepler in places like your Anthropic dashboard rather than as an unlabelled non-interactive run.

This labeling applies to the sessions Kepler drives over ACP. Claude Code's **Terminal** mode deliberately leaves the label alone, because overriding it there would break key handling in the embedded terminal.

***

## Sessions

Connecting an agent is the setup; running one is a **session** inside a task. [Agent Sessions](/kepler/agent-sessions) covers sessions — starting, resuming, queuing prompts, and reviewing what the agent produced.

A task holds resources and does not require a worktree. See [Tasks and Resources](/kepler/tasks-and-resources).

---
