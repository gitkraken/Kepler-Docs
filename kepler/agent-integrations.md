---
title: Agent Integrations
description: Kepler runs the coding agent you already have. Connect Claude Code, Codex, GitHub Copilot, Cursor, Auggie, OpenCode, Grok Build, Pi, or Google Antigravity, or add your own custom agent.
product: Kepler
feature: Agent Integrations
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode, grok, pi, antigravity]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [agent-integrations, claude-code, codex, copilot, cursor, auggie, opencode, grok, pi, antigravity, acp, terminal, custom-agents, setup, settings, mcp-servers]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Use **Settings → Agents** to install the coding agents you already use, sign in to them, and choose how they run in Kepler. You sign in with your own agent account, and Kepler adds no markup on the agents you bring.

Kepler supports 9 agents. You can also add any other agent that speaks the Agent Client Protocol (ACP), or whose command-line interface you want to run inside a task.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-settings-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-settings-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Agents: the page description, New tasks use Claude Code with Change in Tasks, the Ask Kepler uses row set to Claude Code CLI (alex.lee@example.com, Acme) with Options and Clear default and its help text, and Your agents with Update all and Re-scan above the Claude Code card, which shows its account (Default), New sessions start in set to Chat, Let artifact comments start turns (on), Artifacts in new sessions (off), and a collapsed Program and data folder.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings → Agents.</figcaption>
</figure>

***

## Supported agents

Each agent gets its own section in **Settings → Agents**, in this order:

| Agent | Name in Settings | How Kepler runs it | Run modes | Multiple accounts |
|---|---|---|---|---|
| **Claude Code** | Claude Code | Your installed `claude` CLI | Chat or Terminal | Yes |
| **Codex** | Codex | Your installed `codex` CLI | Chat or Terminal | Yes |
| **GitHub Copilot** | GitHub Copilot | Your installed `copilot` CLI in ACP mode (`--acp`) | Chat or Terminal | Yes |
| **OpenCode** | OpenCode | Your installed `opencode` CLI, v2, in ACP mode (`acp`) | Chat or Terminal | No |
| **Pi** | Pi | Your installed `pi` CLI, in its own terminal interface | Terminal only | No |
| **Auggie** | Auggie | Your installed `auggie` CLI in ACP mode (`--acp`) | Chat or Terminal | Yes |
| **Google Antigravity** | Antigravity | Your installed `agy` CLI in a terminal, or Google's separate Antigravity ACP server (`agy_acp_server`) for Chat | Terminal (default) or Chat | No |
| **Cursor** | Cursor | Your installed `cursor-agent` CLI in ACP mode (`acp`) | Chat or Terminal | No |
| **Grok Build** | Grok Build | Your installed `grok` CLI in ACP mode (`agent stdio`) | Chat or Terminal | Yes |

**Auggie** is Augment's coding agent. It runs over ACP like the other agents, and its model and mode pickers work like any other agent's. Auggie is also one of the 3 agents that report plan usage back to Kepler, with Claude Code and Codex. Auggie reports only its credit balance, with the credits your plan includes, rather than usage windows. To learn about the plan usage meter, see [Agent Sessions](/kepler/agent-sessions#usage-indicators).

Kepler asks each agent's provider for plan usage while **Check plan usage with each agent's provider** is on. This setting is in **Settings → Agents → Usage limits**, and it is on by default.

**Grok Build** is xAI's coding agent. It signs in through your browser, or you can supply an xAI API key. Grok Build keeps its data under `~/.grok`, and Kepler uses that folder to keep several accounts apart.

**Google Antigravity runs 2 separate binaries.** Terminal mode runs the `agy` CLI. Chat mode runs Google's Antigravity ACP server, which is a separate download with its own version. The agent's section in **Settings → Agents** lists both under **Components**: **Antigravity CLI** (*Needed for Terminal mode.*) and **ACP server** (*Rich-text (ACP) mode. Installed separately from the Antigravity CLI.*). Each has its own **Install** or **Update to {version}**. Either one alone is enough to use the agent in that mode. Sessions stay in Terminal until you pick **Chat** for Antigravity, because the ACP server signs in separately from the CLI.

**Pi is terminal-only.** Its CLI has no ACP mode, so Kepler runs Pi's own interface in a terminal inside the task instead of leaving Pi out. Kepler does not check Pi's sign-in. Pi uses its own sign-in (`/login`, or the provider API-key environment variables it reads directly).

With Pi 1.x, Kepler loads its own extension for each launch. The extension gives the session the task's context and Kepler's workspace tools, and leaves your `APPEND_SYSTEM.md` and `~/.pi/agent` untouched. With other Pi versions, Kepler pastes the task's context in instead. A Pi session resumes by its own session ID, and Pi does not ask again whether to trust a worktree of a repository you already trust.

**OpenCode needs version 2.** Kepler reads and resumes only OpenCode 2's sessions and will not start a session on an OpenCode 1 binary: its card warns *OpenCode {version} is not supported*. A conversation you started under OpenCode 1 resumes from OpenCode 2's copy of it.

**Inbox wake in Terminal mode.** Kepler can wake an idle **Terminal** session to read its inbox for Claude Code, Pi, and OpenCode 2.1.1 or newer. Pi gets the wake through Kepler's per-launch extension and OpenCode through a plugin Kepler loads for each launch, and neither touches your own config. Kepler delivers the wake as a queued follow-up prompt. Other agents in Terminal mode cannot use Kepler's workspace tools or inbox, and Kepler suggests **Continue in Chat** from the session menu instead.

**Claude Code folder trust.** Kepler reads folder trust where the Claude Code CLI records your answer. A worktree inherits the trust you already gave its repository, so a session does not stop at the trust prompt.

**Codex now runs your own CLI.** Earlier builds shipped a bundled `codex-acp` engine. Kepler now finds and starts the `codex` you have installed, like every other agent, so its section reads **Installed** and it has a binary picker.

You set the mode the same way for every agent that offers both. **Settings → Agents → *your agent* → New sessions start in** picks between **Chat** and **Terminal**, per agent. To start one session the other way, use **Start in** in the composer's **Agent settings**. See [Agent Sessions](/kepler/agent-sessions#how-a-session-runs).

These 2 agents need a recent build to run over ACP:

| Agent | Minimum |
|---|---|
| **GitHub Copilot** | CLI v1.0 or newer. Older builds reject `--acp` |
| **Cursor CLI** | A build that exposes the `acp` command, added in early 2026 |

Kepler checks both before it starts a session and tells you to update rather than failing with a protocol error.

***

## Install an agent

When an agent is not installed, its section reads **Not installed** and offers **Install**. Kepler runs the install command for you and shows the output as it runs, so you can read a failure rather than guess at one. **Cancel** stops an install in progress (*Install cancelled: {name}*). Installs and updates run one at a time. If you start a second one while one is running, it waits. An install or update that produces no result for 20 minutes stops on its own and says so in the output.

The install methods depend on the operating system of the machine you are on:

| Agent | macOS | Linux | Windows |
|---|---|---|---|
| **Claude Code** | Native installer, Homebrew, npm (global) | Native installer, npm (global) | Native installer, winget, npm (global) |
| **Codex** | Standalone installer, Homebrew, npm (global) | Standalone installer, npm (global) | npm (global) |
| **GitHub Copilot** | Native installer, Homebrew, npm (global) | Native installer, Homebrew, npm (global) | winget, npm (global) |
| **Cursor CLI** | Native installer, Homebrew | Native installer | Native installer |
| **Auggie** | npm (global) | npm (global) | npm (global) |
| **OpenCode** | Native installer, Homebrew, npm (global) | Native installer, Homebrew, npm (global), pacman | npm (global) |
| **Grok Build** | Native installer | Native installer | Native installer |
| **Pi** | npm (global) | npm (global) | npm (global) |
| **Google Antigravity** | Native installer, plus the ACP server component | Native installer, plus the ACP server component | Native installer, plus the ACP server component |

Every OpenCode method installs OpenCode 2. Windows offers only npm, because Scoop's and Chocolatey's `opencode` packages still install OpenCode 1.

If an agent offers no install method for your OS, Kepler says so and points you to the custom binary path instead.

Kepler does not close the install output pane automatically when the install finishes. Errors during the install, such as a permissions failure, a partial install, or a post-install warning, appear only in that pane, so read them before you dismiss it.

***

## Binary detection

Kepler resolves each agent's binary the way your shell does: the first match on your `PATH`, so it agrees with `which`. Beyond `PATH`, it also searches your login shell's environment and well-known install directories. This is how Kepler finds an agent installed by nvm or Homebrew, even when you did not launch Kepler from a terminal. Kepler reads your login shell again on **Restart agent**, **Re-scan**, or a retry, so an environment variable you add, change, or remove in your shell's startup files reaches the restarted agent without restarting Kepler.

Each agent's card in **Settings → Agents** shows what Kepler resolved. The version and **Install** are in the card's title line. **Binary**, **Components**, and **Data folder** are under **Program and data folder**:

| Control | What it does |
|---|---|
| Version | The installed version, or **Not installed** |
| **Install** | Runs one of the install methods above. Shown when the agent is not installed |
| **Binary** | The resolved absolute path, or **Not found**, with where it came from (**PATH**, **Shell**, or **Common**) and its version |
| **Re-scan** | Re-detects this agent's binary. Use it after installing or removing one outside Kepler |
| **Custom path…** | Pins an absolute path of your own. Kepler validates it and refuses a directory or a path that is not a file |
| **Clear custom** | Drops the pinned path and goes back to automatic resolution. Shown only while a custom path is set |
| **Installed versions** | A picker listing every install Kepler found, with an **Auto** row. Appears only when Kepler finds more than one |
| **Data folder** | Overrides the agent's own data and config directory. Leave it empty for the agent default |
| **Enabled** | Whether Kepler offers this agent when you start a session |

If Kepler cannot read an installed agent's version, its section shows a **Version unknown** badge rather than plain **Installed**: *Kepler was unable to read {name}'s version. Features that depend on the version stay off, such as sending a new session's first message automatically. Reinstalling or updating {name} usually fixes this.*

When an installed version has a known problem, the agent's card shows a warning note under its title line that names the version and what to do:

| Agent | Warning |
|---|---|
| **OpenCode** | *OpenCode {version} is not supported*. Sessions with it do not start, so install OpenCode 2 or pick an OpenCode 2 binary |
| **Auggie** | *Auggie {version} may not load your MCP servers in chat* |
| **Google Antigravity** | *ACP server {version} can fail to start on Linux*. Reinstall the ACP server under **Program and data folder** |
| **Codex** | *Codex {version} can show approval prompts that need no answer*. Update Codex to 0.163.0 or newer |

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-version-advisory-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-version-advisory-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Codex card in Settings › Agents, version 0.150.1 with Update and Enabled, and under its title a warning note: Codex 0.150.1 can show approval prompts that need no answer, advising to update Codex to 0.163.0 or newer. Below it are Accounts with Add account and the Codex CLI account (Not signed in, Sign in), New sessions start in with Chat selected beside Terminal, and Program and data folder.">
  </a>
  <figcaption style="text-align:center; color:#888">A version warning on the Codex card.</figcaption>
</figure>

If a pinned path later disappears (for example, when an auto-updater cleans up an old version), Kepler falls back to automatic resolution instead of reporting the agent as missing.

Above the agent cards in **Settings → Agents**, **Re-scan** re-detects every agent at once, and **Update all** runs each installed agent's own updater.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-maintenance-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-maintenance-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Update all and Re-scan beside the Your agents heading in Settings › Agents, above the title row of the Claude Code card: version 2.1.145, Update and Enabled.">
  </a>
  <figcaption style="text-align:center; color:#888">Update all and Re-scan, above the agent cards.</figcaption>
</figure>

***

## Sign in to an agent

An installed agent shows **Sign in** until it has a credential, and **Sign out** once it does. **Sign in** opens a modal listing the methods that agent supports on this machine, plus any methods Kepler provides itself:

| Agent | How you sign in |
|---|---|
| **Claude Code** | Browser sign-in. Kepler runs the sign-in for you and your browser opens; you paste a code back only if the browser callback cannot reach Kepler. **More sign-in options** adds **Amazon Bedrock**, **Google Vertex AI**, **Microsoft Foundry**, and **LLM gateway** |
| **Codex** | Sign in with a ChatGPT account through your browser, or enter an API key. On a remote, **ChatGPT (device code)** |
| **GitHub Copilot** | **Sign in with GitHub**: Kepler's own device flow. Open `github.com/login/device` and enter the one-time code |
| **Cursor CLI** | Cursor's own browser sign-in, driven from the modal, or **Paste an API key** from the Cursor dashboard. On a remote, only the API key works |
| **Auggie** | **Sign in with browser**, or **Paste session token** |
| **OpenCode** | **OpenCode account (Go or Console)**: sign in through your browser with a one-time code. OpenCode also resolves providers from its own config file and provider environment variables |
| **Grok Build** | Browser sign-in, or **Paste an API key** for a deployment with no local browser |
| **Google Antigravity** | **Google OAuth**, **Google Cloud project**, or **Google Cloud project (SSO)**, driven from the modal. The ACP server used for Chat keeps its own sign-in, so Kepler checks whichever one the mode you picked uses |
| **Pi** | Nothing to do in Kepler. Sign in inside the CLI itself, or set the provider environment variables it reads |

### Claude Code through a cloud provider or gateway

To run Claude Code through your cloud provider rather than a Claude account, click **More sign-in options** in the **Sign in to Claude Code** modal and pick a method:

| Method | What you enter |
|---|---|
| **Amazon Bedrock** | A Bedrock API key (`AWS_BEARER_TOKEN_BEDROCK`) and the AWS region (`AWS_REGION`) |
| **Google Vertex AI** | The project (`ANTHROPIC_VERTEX_PROJECT_ID`) and region (`CLOUD_ML_REGION`), and optionally a credentials file (`GOOGLE_APPLICATION_CREDENTIALS`). Leave the file empty to use application default credentials |
| **Microsoft Foundry** | The resource name only (`ANTHROPIC_FOUNDRY_RESOURCE`), and optionally an API key and your Opus, Sonnet, and Haiku deployment names. Without a key, it signs in with Microsoft Entra ID credentials on this machine |
| **LLM gateway** | The gateway's URL (`ANTHROPIC_BASE_URL`) and the token it issues (`ANTHROPIC_AUTH_TOKEN`), plus any other `NAME=value` variables your gateway needs |

<figure style="text-align:center">
  <a href="/wp-content/uploads/claude-provider-signin-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/claude-provider-signin-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Sign in to Claude Code dialog with More sign-in options expanded: Sign in with Claude.ai and Sign in with token (advanced), then Amazon Bedrock, Google Vertex AI, Microsoft Foundry and LLM gateway, each with a line on how it runs Claude.">
  </a>
  <figcaption style="text-align:center; color:#888">Claude Code's sign-in methods, with More sign-in options expanded.</figcaption>
</figure>

The account then reads as the provider and its region, project, or resource, or as the gateway's host. Kepler shows no plan usage for it, because the plan belongs to your cloud provider. Saving one method clears the values stored for the others, and **Sign out** clears the provider. You can set a gateway's extra variables only on the computer running Kepler, not from a paired device.

### OpenCode account

**OpenCode account (Go or Console)** signs OpenCode in to your OpenCode account:

1. Click **Sign in** on OpenCode's card and pick **OpenCode account (Go or Console)**.
2. Click **Open sign-in in browser** and enter the **One-time code** the modal shows.
3. Choose the workspace with your Go subscription.
4. Select a Go model to use your plan.

The agent's card then shows OpenCode as signed in.

<figure style="text-align:center">
  <a href="/wp-content/uploads/opencode-account-signin-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/opencode-account-signin-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Sign in to OpenCode dialog on the OpenCode account flow: Sign in to your OpenCode account in your browser, choosing the workspace with your Go subscription, then Open sign-in in browser, a One-time code box with KPLR-2468 and Copy code, Waiting for you to finish in the browser, and Back.">
  </a>
  <figcaption style="text-align:center; color:#888">Signing OpenCode in to an OpenCode account with a one-time code.</figcaption>
</figure>

### Browser sign-in, including on a remote

**Claude Code** and **Codex** both sign in through your browser, and neither needs a terminal to do it.

This also works on a [remote environment](/kepler/remote-environments):

- **Claude Code** on a remote offers **Sign in with browser**, which opens the sign-in page in your *local* browser and takes the code you paste back. Kepler saves the credential on the remote machine.
- **Codex** on a remote offers **ChatGPT (device code)**: *Sign in with a one-time code in your browser. Works on any remote.* Kepler shows the sign-in link and a **One-time code**. The remote CLI waits for you to finish and writes the token there. Some ChatGPT workspaces turn device sign-in off, and Kepler then points you to the alternatives.
- **Cursor CLI** on a remote offers only **Paste an API key**, because its browser sign-in cannot complete there.

Wherever Kepler opens a browser sign-in for Claude Code, Codex, or Antigravity, **Open sign-in in browser** appears beside a read-only **Sign-in link** field with **Copy link**. To open the link in another browser or profile, copy it. The field stays after the browser opens, because a browser can open somewhere you cannot see it. The field goes away if the sign-in attempt fails.

When a sign-in runs in a terminal on a remote and the browser page does not load after you sign in, paste that page's address into the box under the terminal (*Browser page won't load after you sign in? Paste its address here.*) and click **Send**. Kepler requests the address on the remote machine, and only when the sign-in itself printed it. You then finish in the terminal.

**Import local Codex login** is the other remote route, in the desktop app: it copies this machine's `~/.codex/auth.json` to the remote target, and asks you to confirm on this machine before it reads the file. The import copies a credential: anyone with access to that remote machine can send Codex requests on your account until you sign out.

A Codex API key works locally and on a remote: Kepler collects the key in the modal and passes it to Codex for that account. **Sign out** on Codex signs the CLI itself out, and Kepler follows a sign-in you do in the Codex CLI outside Kepler.

### Auggie's sign-in methods

Auggie supports 2 sign-in methods:

| Method | What it does | Where it works |
|---|---|---|
| **Sign in with browser** | Runs Auggie's sign-in and finishes it in your browser. Auggie stores the credential under `~/.augment` | Local, and over SSH: the remote variant opens the page in your local browser and takes a pasted JSON response |
| **Paste session token** | You paste the JSON from `auggie token print` into Kepler. Kepler stores it and supplies it on every session | Anywhere, including CI-style setups with no browser |

If you run Auggie's browser sign-in on this machine yourself, Kepler detects it and you can skip the token paste.

### Multiple accounts of one agent

**Claude Code**, **Codex**, **GitHub Copilot**, **Auggie**, and **Grok Build** support more than one signed-in account. To add one, open **Settings → Agents → *your agent* → Accounts** and click **Add account**. Each account keeps its own credentials and history.

To give each added account its own color, pick one from the swatch at the left of its row: **Rose**, **Amber**, **Lime**, **Cyan**, **Blue**, or **Violet**. Kepler tints the agent icon with that color on session tabs, the task's context panel, and the terminal status bar, so you can tell sessions on different accounts apart. *The default account stays uncolored.* Accounts also appear on the agent's card in Settings.

For **Auggie**, you can only add a second account with **Paste session token**. Its browser sign-in writes to one fixed file, so it would sign the second account into the first account's identity.

***

## Run modes

Most agents run in 2 modes, and each agent keeps its own default. To pick the default for an agent, open **Settings → Agents**, expand the agent, and set **New sessions start in**:

| Mode | What you get |
|---|---|
| **Chat** | *{agent} built into Kepler, with replies, diffs and plans you can read, review and search.* Kepler drives the agent over ACP and renders the conversation itself. This is the default |
| **Terminal** | *{agent}'s own command-line app, with its commands, shortcuts and settings, just as you use it today.* It runs in an embedded terminal inside the task |

To start one session in the other mode without changing the default, set **Start in** in the composer's **Agent settings** before you send the first message. An agent that offers only one mode shows no switch at all. See [Agent Sessions](/kepler/agent-sessions#how-a-session-runs).

### Detecting sessions started outside Kepler

**Settings → Integrations → Your terminal → Show sessions started outside Kepler** is a separate setting that applies to all agents, and it is **on by default**. It installs GitKraken hooks so sessions you start in your own terminal show up in Kepler. It covers every agent Kepler can track that way: **Claude Code**, **Codex**, **Cursor**, **GitHub Copilot**, **OpenCode**, **Auggie**, **Grok Build**, and **Pi**. Kepler does not track Google Antigravity this way. See [Agent Sessions](/kepler/agent-sessions#sessions-started-outside-kepler).

Kepler also follows its own **Terminal** sessions through those hooks. If a live terminal session keeps reporting status but its hook events stop arriving, Kepler warns *Agent sessions aren't reporting to Kepler*, because status and notifications may be out of date. **Repair** reinstalls the reporting configuration. Restart any session that still does not report afterward. A window that only views another computer's sessions gets the warning without **Repair**, because you repair reporting on the computer running the sessions.

### Programs that report their own status

Some terminal programs report their own status to Kepler (through the OSC 7501 escape sequence). When an agent's terminal program does this, Kepler shows the session as working, blocked, or done from what the program reports, without hooks. If hook events also arrive, the hooks take precedence. See [Agent Sessions](/kepler/agent-sessions#whats-different-in-terminal).

***

## Your default agent

**Settings → Tasks → New tasks → Default agent** sets which agent is preselected when you start work, and supplies the model, mode, and thinking effort a new session starts with.

Kepler saves agent options **per account**. Picking a different account of the same agent brings up that account's own saved model and options, so a larger model you chose on your work account does not carry over to your personal one.

Only agents that are installed and **Enabled** appear in the picker. If your saved default is no longer installed, Kepler says so and asks you to pick another.

An Action can override all of this. See [Actions](/kepler/actions) for how an Action pins a provider, account, model, mode, and options together, and which choice wins when they disagree.

***

## Custom agents

If your agent is not one of the 9 supported agents, you can add it by its command. To add one, open **Settings → Agents → Custom agents**, click **New custom agent**, and fill in these fields:

| Field | What it holds |
|---|---|
| **Name** | What the agent is called in Kepler's pickers |
| **Runs in** | **Chat**: *Kepler's chat. Needs a program that speaks ACP (the Agent Client Protocol).* **Terminal**: *The command's own app, in a terminal.* |
| **Command** | The binary to run: an absolute path, or a name Kepler resolves on your `PATH` |
| **Args (one per line)** | Arguments for the command. For a Chat agent, the arguments that put it into ACP mode, for example `--acp` |
| **Environment variables (KEY=value, one per line)** | Variables merged into the agent's environment on every session |

Kepler treats environment values as secrets: it encrypts them at rest, hides them after you save, and never sends them to any client. When you edit a custom agent, leaving a value empty (`KEY=`) keeps the stored secret, and typing a new value replaces it.

Custom agents appear alongside the built-in agents everywhere you can choose an agent. A custom agent that runs in **Terminal** works the same way: Kepler works out what terminal mode can offer from the command's own flags rather than from a list of agent names, so your own agent degrades exactly the way a built-in one does.

***

## MCP servers

Kepler lists the MCP servers each agent loads, and lets you add, remove, sign in to, and turn off servers or single tools, per repository from the composer's **Agent settings** pill or as defaults in **Settings → Agents → MCP servers**. See [MCP Servers](/kepler/mcp-servers).

***

## What Kepler tells the agent about itself

Agent CLIs report **Kepler** as the client name, so your sessions show up as Kepler in places like your Anthropic dashboard rather than as an unlabeled non-interactive run.

This labeling applies to the sessions Kepler drives over ACP. **Terminal** mode deliberately leaves the label alone, because overriding it there would break key handling in the embedded terminal.

***

## Sessions

After you connect an agent, you run it in a **session** inside a task. To learn how to start and resume sessions, queue prompts, and review what the agent produced, see [Agent Sessions](/kepler/agent-sessions).

A task holds resources and does not require a worktree, or even a repository. See [Tasks and Resources](/kepler/tasks-and-resources).

To follow conversations you started outside Kepler, see [Sessions started outside Kepler](/kepler/agent-sessions#sessions-started-outside-kepler).

---
