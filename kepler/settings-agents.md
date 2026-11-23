---
title: Agent Settings
description: Choose how new Kepler sessions start, install and sign in to your coding agents, set up custom agents and agent presets, keep agents running through sleep, restarts, and usage limits, and put idle agents to sleep.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot, cursor, antigravity, opencode, pi, auggie, grok]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [settings, agents, custom-agents, keep-awake, idle-agents, usage-limits, artifacts]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Use **Settings → Agents** to choose how new sessions start, to install, update, and sign in to the coding agents that work on your tasks, to add custom agents and agent presets, to keep agents running, and to put idle agents to sleep. Your agents' MCP servers and built-in tools are on [Agent tools](/kepler/settings-agent-tools), and the rules that approve their actions for you are on [Approvals](/kepler/settings-approvals).

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-settings-oct-2026-v7@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-settings-oct-2026-v7@2x.png" class="help-center-img img-bordered" alt="Your agents in Settings › Agents, with Update all and Rescan beside the heading and one row per agent: Claude Code (marked Default), Codex, GitHub Copilot, Auggie and Grok Build with 1 account and Add account; OpenCode, Antigravity and Cursor Not signed in with Sign in; and Pi. Each row shows the agent's version, an Enabled switch that is on and a chevron, and the line below the list says to open an agent for its accounts, how its sessions start and where its program lives.">
  </a>
  <figcaption style="text-align:center; color:#888">Your agents in Settings → Agents, one row per agent.</figcaption>
</figure>

<a id="default-agent"></a>

## Defaults

**Defaults** sets how new sessions and Ask Kepler chats start:

| Setting | What it controls |
|---|---|
| **New sessions start with** | The agent that the **New task** composer, the Dashboard's composer, and a new draft session start with |
| **New Ask Kepler chats start with** | The agent that new [Ask Kepler](/kepler/ask-kepler) chats start with |
| **New sessions start in** | Whether new sessions run in **Chat** or **Terminal**, for every agent. See [Default mode for new sessions](#default-mode-for-new-sessions) |

Each of the first two is an agent-settings pill, like the one in the composer: pick the agent and account, and optionally an [agent preset](#agent-presets), a model, and other options. Kepler saves each pick as you make it. An [Action](/kepler/actions) uses **New sessions start with** unless it names an agent of its own.

Below each pill, **Start each session on the agent you used last** and **Start each chat on the agent you used last** are on by default. Your first session or chat uses the pill's agent, and each later one starts on your last pick. To always start on the pill's agent, clear the box.

**New Ask Kepler chats start with** lists only the agents that run in **Chat**, because only they can answer in the Ask Kepler panel. See [Ask Kepler](/kepler/ask-kepler#which-agents-can-answer).

### Default mode for new sessions

**New sessions start in** chooses where new sessions run. **Chat** runs your agents inside Kepler, and **Terminal** runs each agent's own command-line app. The default is **Chat**.

This setting applies to every agent that can run in both modes, including agents you add later. To give one agent its own mode, open the agent from [Your agents](#your-agents) and set **New sessions start in** on its page. Choosing a mode under **Defaults** again sets it for every agent.

The setting is only a default: you can pick the other mode when you start a session. A terminal-only agent always starts in Terminal. See [Agent Sessions](/kepler/agent-sessions#how-a-session-runs).

## Your agents

Kepler supports **Claude Code**, **Codex**, **GitHub Copilot**, **OpenCode**, **Pi**, **Auggie**, **Antigravity**, **Cursor**, and **Grok Build**. Settings lists the agents installed on this machine first.

In the section header, **Update all** runs each installed agent's own updater, and **Rescan** looks again for the agent CLIs installed on this machine. If you install or remove an agent outside Kepler, click **Rescan**.

Each agent has a row with its version, a **Default** badge on your default agent, and its accounts or sign-in state. A row also has these controls:

| Control | What it does |
|---|---|
| **Install** | Opens **Set up {name}** to pick an install method, then **Sign in to {name}** if the agent needs a sign-in. Shown when the agent is not installed and has an installer for your OS |
| **Add account** | Opens the agent's page and its add-account dialog |
| **Sign in** | Signs in to an agent that has a single login |
| **Enabled** switch | *Off keeps it installed but hidden when you start work.* |

If you installed the agent yourself, use **Already installed?** in the **Set up {name}** dialog: enter or browse to the program, then click **Use this**.

When a newer version of an installed agent is out, its row shows **Update available**. After an update, the row shows **Updated**: new sessions use the new version, and a running session switches when you restart it. To turn off the title-bar notice and the restart notice for agent updates, see [Settings → Updates](/kepler/settings-updates-help#updates).

When the version reads **Version unknown**, Kepler turns off features that depend on the version, such as sending a new session's first message automatically. To fix it, reinstall or update the agent.

### An agent's own page

To open an agent's page, click its row. The page holds the agent's own settings:

| Setting | What it controls |
|---|---|
| **New sessions start in** | This agent's own mode, instead of the [default for every agent](#default-mode-for-new-sessions) |
| **Update** | Runs the agent's updater and shows its output. Shown when Kepler has an updater for that agent |
| **Accounts** | Claude Code, Codex, GitHub Copilot, Auggie, and Grok Build: runs more than 1 login side by side. See [Use several accounts for one agent](#use-several-accounts-for-one-agent) |
| **Account** | On an agent with a single login: who is signed in, with **Sign in** or **Sign out**. Signing out deletes the stored credentials |
| **Artifacts in new sessions** | Claude Code only. See below |
| **Let artifact comments start turns** | Claude Code only. See below |
| **Which {name} Kepler runs** | The agent program Kepler runs. **Auto** uses the first match on your `PATH`, the same one `which` finds. To override it, pick a specific install or **Custom path…**, or click **Rescan** to search again |
| **Where {name} keeps its data** | *Set it only to keep the {name} Kepler runs apart from the one you run yourself.* Empty uses the agent's usual folder |

If the installed version of an agent has a known problem, a warning note on its page says what to do:

| Note | What it means |
|---|---|
| *OpenCode {version} is not supported* | Sessions with this version do not start. Install OpenCode 2, or choose an OpenCode 2 program under **Which OpenCode Kepler runs** |
| *Auggie integration is unverified* | Kepler could not verify the selected Auggie build. Before you rely on MCP tools in Chat, click **Rescan** or select a verified installation under **Which Auggie Kepler runs** |
| *Codex {version} can show approval prompts that need no answer* | Update Codex to 0.163.0 or newer |

**OpenCode needs version 2.** If you have both versions installed, point **Which OpenCode Kepler runs** at OpenCode 2. A conversation you started under OpenCode 1 resumes in OpenCode 2.

**Google Antigravity runs the `agy` CLI in both modes.** Chat needs Antigravity CLI 1.5.0 or newer. With an older CLI, click **Update** on its page. Chat and Terminal share one sign-in: **Sign in in Terminal**. See [Agent Integrations](/kepler/agent-integrations#sign-in-to-an-agent).

### Use several accounts for one agent

With **Accounts**, you can run more than 1 login for an agent side by side. Each account has its own credentials and history, but shares your skills, agents, commands, and settings.

To add an account, click **Add account**, on the agent's row or its page. For Claude Code, Codex, and GitHub Copilot, also choose whether its conversations **Keep separate** or **Share with the CLI**. A new Copilot account starts on **Share with the CLI**, and its new conversations use your CLI settings. If you change a Copilot account's choice later, the conversations it already has stay where they are and still open in Kepler.

Each account row has the following controls:

- A color picker that tints the agent icon wherever that account runs. The default account starts with **No color**.
- **Sign in**.
- An account menu with **Rename**, **Share history with the CLI**, **Sign in another way**, **Sign out**, and **Remove account**. On a signed-in Claude Code account, the menu also has **Switch account…**, which signs that account in with a different Claude login. See [Switch the account a Claude Code login uses](#switch-the-account-a-claude-code-login-uses).

Once an agent has 2 or more accounts, Kepler uses them in list order, top first:

- A new session you start without picking an account starts on the first account with usage left.
- When a session hits a usage limit, Kepler continues it on the first account with usage left, or suggests that account, depending on [When a usage limit is reached](#keep-agents-running).

To reorder the list, drag a row by its handle, or use **Move to top**, **Move up**, and **Move down** in the account menu. To keep an account out of the switch at a usage limit, clear **Use at a usage limit** in its menu. Its row then reads **Skipped at a usage limit**. An account that keeps its own history reads **New sessions only**, because a conversation can move to it only with **Share history with the CLI** on.

Removing an account stops its running sessions and deletes the sessions stored only in that account. To keep those sessions, click **Move to CLI account** first. See [Agent Sessions](/kepler/agent-sessions#several-accounts-for-one-agent).

### When an added account stops sharing your settings

An added account shares your own settings, instructions, skills, agents, commands, and other configuration. If the agent saves a change while signed in to that account, it can write its own copy, and the account stops following your file. Kepler then shows a message under the account's row. Expand it to see both files, and choose one of the following:

- **Ask Kepler to resolve** opens an Ask Kepler chat with a prompt you can edit, asking the agent to copy what is worth keeping into your shared copy.
- **Share your {item} again** links the account back to your file, and saves its own copy as a backup next to it.
- **Keep its own {item}** keeps the account's copy. You can still choose **Share your {item} again** later from the row's menu.

### Switch the account a Claude Code login uses

**Switch account…** opens a dialog that names the login now signed in, and how many running sessions use the account. Running sessions pick up the new login when they restart or on their next request. On the default account, the one the CLI uses, the switch also changes the account the `claude` command uses in your own terminals.

Click **Continue** to open the usual sign-in. If your browser is already signed in, choose a different account on the sign-in page.

### Artifacts in new sessions

The following setting is on Claude Code's page:

| Setting | What it controls | Default |
|---|---|---|
| **Artifacts in new sessions** | Gives new sessions the Artifact tools, which publish pages and designs and add about 12k tokens to each session's context | Off |

A running Chat session has its own **Artifacts** switch in its agent settings. When you turn it on, Kepler asks first, then restarts the session and resumes the conversation. Once a conversation has artifacts on, they stay on for that conversation. See [Agent Sessions](/kepler/agent-sessions).

### Let artifact comments start turns

The following setting is on Claude Code's page:

| Setting | What it controls | Default |
|---|---|---|
| **Let artifact comments start turns** | Lets anyone with edit access to an artifact a Chat session publishes start a turn in that session by sending a comment to Claude | On |

Running sessions keep the value they started with. When you change the setting, the page lists the sessions still on the previous value. To apply the new value, click **Restart all**, or tick sessions and click **Restart selected**.

Restarting keeps each conversation. It interrupts a turn in progress and stops background work, and a restarted session stops watching the artifacts it published before.

## Custom agents

To run an agent that Kepler does not list, add it as a custom agent by giving Kepler its command. To add one, click **New custom agent** in the section header. To edit one, click its row. Either way, the agent opens as a sub-page with these fields:

| Field | What it takes |
|---|---|
| **Name** | The name Kepler shows for the agent |
| **Command** | The program to run, for example `/usr/local/bin/my-agent` or `my-agent` |
| **Args (one per line)** | Arguments passed to the command |
| **Environment variables (KEY=value, one per line)** | Environment for the command |
| **Runs in** | **Chat**: *Kepler's chat. Needs a program that speaks ACP (the Agent Client Protocol).* **Terminal**: *The command's own app, in a terminal.* |

Custom agents appear with the built-in agents wherever you pick an agent.

Kepler encrypts environment values at rest and hides existing values when you edit an agent. To keep a stored secret, leave its value empty (`KEY=`). To replace it, type a new value.

**Delete** asks first, then deletes the agent and the environment values stored with it. You cannot undo a delete.

## Agent presets

An agent preset saves one agent's model, mode, and other options, such as effort, under a name, so you can pick them all at once whenever you pick that agent. The list groups your presets by agent, with the agent's badge beside each name:

- To add a preset, click **New preset** in the section header, or click **Save preset** in a session's agent settings.
- To edit a preset, click its row.
- To duplicate, reorder, or delete a preset, use its menu.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-presets-nov-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-presets-nov-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Agent presets section of Settings › Agents with New preset and its description: Quick fix and Careful review, each badged Claude Code, Quick fix badged Codex, and Docs pass badged OpenCode, each row with its options menu.">
  </a>
  <figcaption style="text-align:center; color:#888">Presets, each badged with the agent it belongs to.</figcaption>
</figure>

A preset opens as a sub-page with these fields:

| Field | What it takes |
|---|---|
| **Name** | A name no other preset uses |
| **Agent** | The agent the preset belongs to, with its **Model**, **Mode**, and other options |
| **MCP servers** | Claude Code, Codex, OpenCode, and GitHub Copilot: **On** or **Off** for each of the agent's MCP servers, with **Reset** |

A preset's MCP server choices apply to each session that uses it. A server that is off in the agent's own settings can only stay off. **Save preset** in a session's agent settings keeps the MCP servers you switched for that session. See [MCP Servers](/kepler/mcp-servers#per-session).

You can use a preset in these places:

- **A session's agent settings.** In the composer, pick it in the **Preset** row, which appears when the chosen agent has presets. See [Agent Sessions](/kepler/agent-sessions#agent-model-mode-and-effort).
- **The default agents.** The **New sessions start with** and **New Ask Kepler chats start with** pills in [Defaults](#defaults).
- **Actions.** Each Action's **Preset** list, in the Action's editor. See [Actions](/kepler/actions).
- **Automations.** An automation's agent settings can use a preset. See [Automations](/kepler/kepler-automations).

If Actions or automations use a preset you delete, Kepler lists them and asks you to choose a replacement. If you change a preset that automations use, Kepler names them and asks you to confirm, and they use the updated options from their next run.

When you change a preset, running sessions that use it keep the earlier version until you update them. To apply the change, click **Update all** below the list. Updating keeps each conversation, but a session that needs a restart interrupts any turn in progress.

<a id="usage-limits"></a>
<a id="usage-and-recovery"></a>

## Keep agents running

**Keep agents running** keeps your agents working when the machine would sleep or Kepler quits, and when an agent hits a usage limit or its model is overloaded. **Keep agents running** and [Idle agents](#idle-agents) apply to the machine the agents run on, so in a window connected to a remote machine, they apply to that machine.

| Setting | What it controls | Default |
|---|---|---|
| **Keep this machine awake while agents work** | Blocks sleep while an agent session is starting, running, or waiting for your input, and while Remote Access is on | On |
| **Keep agents and terminals running after Kepler quits or restarts** | *Agents and terminals stay alive while Kepler is closed or updating, and reconnect afterwards. When off, quitting or restarting Kepler ends them.* | On |
| **When a usage limit is reached** | What happens to a session that a usage limit cuts off, for every agent, in Chat and in Terminal. See the options below | Wait for the reset |
| **Retry automatically when the model is overloaded** | When the model is overloaded or the provider has a temporary server error, Kepler waits and asks the agent to continue, for up to 12 hours. It never resends your prompt | On |

**Keep this machine awake while agents work** also counts Claude Code sessions running outside Kepler. The screen can still turn off. If Kepler cannot keep the machine awake, the setting says why under it.

**Keep agents and terminals running after Kepler quits or restarts** applies from the next session you start. If agents and terminals cannot start on this machine, the setting says why.

**When a usage limit is reached** has these options:

- **Ask me**: the session stops, and its usage bar offers to switch accounts or wait for the reset.
- **Wait for the reset**: the session continues when the limit resets.
- **Switch accounts**: the session continues on the agent's next account with usage left, in [the order on its page](#use-several-accounts-for-one-agent), or after the reset if no account has any.

Kepler reads each account's plan usage from its provider, through the agent's own sign-in, and never changes that sign-in. If an account row on an agent's page shows **Turn on usage checks**, click it to turn those checks back on.

## Idle agents

**Idle agents** stops sessions you have left alone, once you are not looking at them:

| Setting | What it controls | Default |
|---|---|---|
| **Put idle task agents to sleep** | How long an agent in a task can stay quiet before Kepler stops it, from **After 5 minutes** to **After 24 hours**, or **Never** | After 1 hour |
| **Put idle Ask Kepler chats to sleep** | How long an Ask Kepler chat can stay quiet before Kepler stops it | After 15 minutes |
| **Wake idle terminal agents to read new reports** | Types a one-line note into a sleeping terminal agent's empty input when a report reaches it | On |

A sleeping session's status reads **Asleep**. Your next message wakes it, and the conversation carries on. Agents in a terminal sleep too, once nothing is typed into them and nothing they started is still running. Typing into the terminal wakes them. Agents that are working or waiting on you stay awake. See [Session status](/kepler/agent-sessions#session-status).

<figure style="text-align:center">
  <a href="/wp-content/uploads/agents-idle-sleep-nov-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agents-idle-sleep-nov-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Idle agents section of Settings › Agents: Put idle task agents to sleep set to After 1 hour, with help that says agents in a terminal sleep too, and Put idle Ask Kepler chats to sleep set to After 15 minutes. Below them, Wake idle terminal agents to read new reports is ticked, with its help text.">
  </a>
  <figcaption style="text-align:center; color:#888">The Idle agents settings, at their defaults.</figcaption>
</figure>

## Agent tools

MCP servers and Kepler's [built-in tools](/kepler/settings-agent-tools#built-in-tools) are on **Settings → Agent tools**: see [Agent Tool Settings](/kepler/settings-agent-tools).

### MCP servers

**MCP servers** is a section of **Settings → Agent tools**: see [MCP servers](/kepler/settings-agent-tools#mcp-servers).

## Approvals

The rules that approve your agents' actions for you are on **Settings → Approvals**: see [Approval Settings](/kepler/settings-approvals).

***

---
