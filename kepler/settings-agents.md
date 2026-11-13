---
title: Agent Settings
description: Install, update, and sign in to your coding agents in Kepler, choose how their sessions start, and set up custom agents, MCP servers, agent tools, approval rules, and usage limits.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot, cursor, antigravity, opencode, pi, auggie, grok]
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [settings, agents, custom-agents, mcp-servers, agent-tools, approvals, usage-limits, artifacts]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "kepler-configuration"
    nav_label: "Agent Settings"
    nav_order: 10
    nav_parent: "kepler-behavior-and-integration-settings"
    page_type: "content"
    card_icon: "robot"
    card_color: "amber"
    card_description: "Install and sign in to agents, custom agents, MCP servers, approvals and usage limits"
---
<kbd>Last updated: November 2026</kbd>

Use **Settings → Agents** to install and update the coding agents that work on your tasks, sign in to them, choose how each one starts, and give them more tools.

At the top of the page, a line names the agent new sessions start with. To change it, click **Change in Tasks**, which opens [Default agent](/kepler/settings-tasks#default-agent).

To choose the agent Ask Kepler uses, set **New Ask Kepler chats start with**. It is separate from the default for tasks. Its agent-settings pill saves the agent, account, [agent preset](#agent-presets), model, and options as you pick them. Below it, **Start each chat on the agent you used last** is on by default: your first chat uses the pill's agent, and each later chat starts on your last pick. To always start on the pill's agent, clear it.

**New Ask Kepler chats start with** lists only the agents that run in **Chat**, because only they can answer in the Ask Kepler panel. See [Ask Kepler](/kepler/ask-kepler#which-agents-can-answer).

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-settings-oct-2026-v6@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-settings-oct-2026-v6@2x.png" class="help-center-img img-bordered" alt="Settings › Agents: the page description; New sessions start on your last pick, or Claude Code the first time, with Change in Tasks; then New Ask Kepler chats start with, its agent-settings pill showing the Claude Code mark and the Quick fix preset, the caption Your first chat uses this agent, and Start each chat on the agent you used last ticked. Your agents has Update all and Rescan above the Claude Code card (Update, Enabled), which shows Accounts with Add account and the Claude Code CLI account marked Default with Check usage, New sessions start in set to Chat, Let artifact comments start turns (on), Artifacts in new sessions (off), and a collapsed Program and data folder.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings → Agents.</figcaption>
</figure>

## Your agents

Kepler supports **Claude Code**, **Codex**, **GitHub Copilot**, **OpenCode**, **Pi**, **Auggie**, **Antigravity**, **Cursor**, and **Grok Build**. Settings lists the agents installed on this machine first.

In the section header, **Update all** runs each installed agent's own updater, and **Rescan** looks again for the agent CLIs installed on this machine. If you install or remove an agent outside Kepler, click **Rescan**.

Each agent has a card. The card's title line shows the agent's name and these controls:

| Control | What it does |
|---|---|
| Version | The installed version, **Not installed**, or **Version unknown** when Kepler could not read the version |
| **Update** | Runs the agent's updater and streams its output. Shown when Kepler has an updater for that agent |
| **Install** | Opens **Set up {name}** to pick an install method, then **Sign in to {name}** if the agent needs a sign-in. Shown when the agent is not installed and has an installer for your OS |
| **Enabled** | *Off keeps it installed but hidden when you start work.* |

If you installed the agent yourself, use **Already installed?** in the same dialog: enter or browse to the program, then click **Use this**.

When the version is unknown, Kepler turns off features that depend on the version, such as sending a new session's first message automatically. To fix it, reinstall or update the agent.

If the installed version of an agent has a known problem, a warning note on the card names the version and says what to do:

| Note | What it means |
|---|---|
| *OpenCode {version} is not supported* | Sessions with this version do not start. Install OpenCode 2, or choose an OpenCode 2 binary under **Program and data folder** |
| *Auggie {version} may not load your MCP servers in chat* | With this version, Chat sessions may skip the MCP servers in Auggie's own settings, and a server whose path contains spaces or parentheses may fail to start |
| *Codex {version} can show approval prompts that need no answer* | Update Codex to 0.163.0 or newer |

The card body holds the rest:

| Control | What it does |
|---|---|
| **Accounts** | Claude Code, Codex, GitHub Copilot, Auggie, and Grok Build: runs more than 1 login side by side. See [Use several accounts for one agent](#use-several-accounts-for-one-agent) |
| **Account** | On an agent with a single login: who is signed in, with **Sign in** or **Sign out**. Signing out deletes the stored credentials |
| **New sessions start in** | The default mode for new sessions. See below |
| **Artifacts in new sessions** | Claude Code only. See below |
| **Let artifact comments start turns** | Claude Code only. See below |
| **Program and data folder** | A disclosure holding **Binary** and **Data folder** |

Under **Program and data folder**:

| Setting | What it controls | Default |
|---|---|---|
| **Binary** | The agent program Kepler runs. **Auto** uses the first match on your `PATH`, the same one `which` finds. To override it, pick a specific install or **Custom path…**, or click **Rescan** to search again | Auto |
| **Data folder** | *Overrides the agent's default data and config folder.* | Empty, meaning the agent's own default |

**OpenCode needs version 2.** If you have both versions installed, point **Binary** at OpenCode 2. A conversation you started under OpenCode 1 resumes in OpenCode 2.

**Google Antigravity runs the `agy` CLI in both modes.** Chat needs Antigravity CLI 1.5.0 or newer. With an older CLI, click **Update** on its card. One sign-in, **Sign in in Terminal**, serves both Chat and Terminal. See [Agent Integrations](/kepler/agent-integrations#sign-in-to-an-agent).

### Use several accounts for one agent

With **Accounts**, you can run more than 1 login for an agent side by side. Each account has its own credentials and history, but shares your skills, agents, commands, and settings.

To add an account, click **Add account**. For Claude Code, Codex, and GitHub Copilot, also choose whether its conversations **Keep separate** or **Share with the CLI**. A new Copilot account starts on **Share with the CLI**, and its new conversations use your CLI settings. If you change a Copilot account's choice later, the conversations it already has stay where they are and still open in Kepler.

Each account row has the following controls:

- A color picker that tints the agent icon wherever that account runs. The default account starts with **No color**.
- **Sign in**.
- An account menu with **Rename**, **Share history with the CLI**, **Sign in another way**, **Sign out**, and **Remove account**. On a signed-in Claude Code account, the menu also has **Switch account…**, which signs that account in with a different Claude login. See [Switch the account a Claude Code login uses](#switch-the-account-a-claude-code-login-uses).

Removing an account stops its running sessions and deletes the sessions stored only in that account. To keep those sessions, click **Move to CLI account** first. See [Agent Sessions](/kepler/kepler-agent-accounts#several-accounts-for-one-agent).

### When an added account stops sharing your settings

An added account shares your own settings, instructions, skills, agents, commands, and other configuration. If the agent saves a change while signed in to that account, it can write its own copy, and the account stops following your file. Kepler then shows a message under the account's row. Expand it to see both files, and choose one of the following:

- **Ask Kepler to resolve** opens an Ask Kepler chat with a prompt you can edit, asking the agent to copy what is worth keeping into your shared copy.
- **Share your {item} again** links the account back to your file, and saves its own copy as a backup next to it.
- **Keep its own {item}** keeps the account's copy. You can still choose **Share your {item} again** later from the row's menu.

### Switch the account a Claude Code login uses

**Switch account…** opens a dialog that names the login now signed in, and how many running sessions use the account. Running sessions pick up the new login when they restart or on their next request. On the default account, the one the CLI uses, the switch also changes the account the `claude` command uses in your own terminals.

Click **Continue** to open the usual sign-in. If your browser is already signed in, choose a different account on the sign-in page.

### Default mode for new sessions

Every agent that can run in both Chat and Terminal has this setting:

| Setting | What it controls | Default |
|---|---|---|
| **New sessions start in** | **Chat** runs the agent inside Kepler; **Terminal** runs the agent's own command-line app | Chat. Google Antigravity starts on Terminal |

Kepler saves the choice per agent, so one agent can default to Terminal while another stays on Chat. The setting is only a default: you can pick the other mode when you start a session. A terminal-only agent shows **Terminal** with no switch. See [Agent Sessions](/kepler/agent-sessions#how-a-session-runs).

### Artifacts in new sessions

The following setting is on Claude Code's card:

| Setting | What it controls | Default |
|---|---|---|
| **Artifacts in new sessions** | Gives new sessions the Artifact tools, which publish pages and designs and add about 12k tokens to each session's context | Off |

A running Chat session has its own **Artifacts** switch in its agent settings. When you turn it on, Kepler asks first, then restarts the session and resumes the conversation. Once a conversation has artifacts on, they stay on for that conversation. See [Agent Sessions](/kepler/agent-sessions).

### Let artifact comments start turns

The following setting is on Claude Code's card:

| Setting | What it controls | Default |
|---|---|---|
| **Let artifact comments start turns** | Lets anyone with edit access to an artifact a Chat session publishes start a turn in that session by sending a comment to Claude | On |

Running sessions keep the value they started with. When you change the setting, the card lists the sessions still on the previous value. To apply the new value, click **Restart all**, or tick sessions and click **Restart selected**.

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

You can use a preset in these places:

- **A session's agent settings.** In the composer, pick it in the **Preset** row, which appears when the chosen agent has presets. See [Agent Sessions](/kepler/agent-sessions#agent-model-mode-and-effort).
- **The default agents.** The **New sessions start with** pill on [Default agent](/kepler/settings-tasks#default-agent), and the **New Ask Kepler chats start with** pill at the top of this page.
- **Actions.** Each Action's **Preset** list, in the Action's editor. See [Actions](/kepler/actions).
- **Automations.** An automation's agent settings can use a preset. See [Automations](/kepler/automations).

If Actions or automations use a preset you delete, Kepler lists them and asks you to choose a replacement. If you change a preset that automations use, Kepler names them and asks you to confirm, and they use the updated options from their next run.

When you change a preset, running sessions that use it keep the earlier version until you update them. To apply the change, click **Update all** below the list. Updating keeps each conversation, but a session that needs a restart interrupts any turn in progress.

## MCP servers

Use **MCP servers** to give your agents extra tools, like a database, a browser, or your issue tracker. The servers here are each agent's own defaults, and every repository inherits them.

To see the servers an agent loads, pick the agent with **Agent**. If that agent has more than 1 account, pick an account too. Kepler lists only the agents that expose their MCP servers to Kepler. In the list:

- Click a server to open its own page. There you can turn the server or a single tool off, sign in to a server that needs it, use **Also add to…** to copy the server to another agent, and **Remove server**.
- Click **Add server** in the section header to add one.

A server or tool you turn off here is off in every repository, unless a repository turns it back on for itself. A repository's own **MCP servers** section is on its [Edit repo](/kepler/settings-repositories#edit-a-repository) page. See [MCP Servers](/kepler/mcp-servers).

Below the list, one more setting applies across every agent:

| Setting | What it controls | Default |
|---|---|---|
| **Keep the GitKraken MCP server installed in every agent** | *Gives every command-line agent Git tools and your issues and pull requests through GitKraken. Turn off to manage it yourself.* | On |

Separately, every session Kepler starts gets Kepler's own workspace tools, which are always on and have no setting. They let the agent work with your tasks and their notes, links, files, and worktrees, with sessions, approvals, and [themes](/kepler/settings-app#theme), and rebase, merge, and compose commits when [Agent tools](#agent-tools) turns them on. An agent can name a repository by one of its [aliases](/kepler/settings-repositories#edit-a-repository). For the full list of tools, see [Tasks and Resources](/kepler/tasks-and-resources).

Workspace tools run without the agent's own permission prompt, in both Chat and Terminal. Instead, an action that needs your approval, such as deleting a worktree or changing another task, waits for you on an approval card. See [Approvals](#approvals).

## Agent tools

Use **Agent tools** to let your agents call Kepler's own tools for rebasing, merging, and cleaning up commits:

| Setting | What it does | Default |
|---|---|---|
| **AI Sync** | *Lets agents rebase or merge your branch and resolve conflicts for you. Every change can be undone.* | Off |
| **AI Compose** | *Lets agents turn messy changes into clean, focused commits. Every change can be undone.* | Off |

You need a paid GitKraken subscription to turn either one on. Without one, a setting that is off shows a lock in place of its checkbox. A setting that is already on keeps its checkbox, so you can still turn it off.

A change applies to new agent sessions. Sessions already running keep the tools they started with.

## Approvals

Some actions your agents take wait for your approval. Use **Approvals** to manage the rules that approve those actions for you. An action that no rule covers still asks.

When an agent uses Kepler's workspace tools to do something that needs your approval, Kepler pins an approval card above that session's message box. Examples include deleting a worktree, sending a prompt to another session, or rewriting a branch. The card's **Approve** menu offers **Always approve** for that kind of action. Kepler does not offer it for actions that can lose work, or for a setting change that Ask Kepler asks to make. See [Answering Your Agent](/kepler/kepler-agent-requests#approval-requests).

**Always approved** lists each rule you create this way, with when and where you added it and how often it has run. **Remove** deletes the rule, so that kind of action asks again.

## Usage limits

These settings control how Kepler handles your agent plans' usage limits:

| Setting | What it controls | Default |
|---|---|---|
| **Check plan usage with each agent's provider** | Asks each agent's provider for your plan usage, per-model limits, and extra usage, with the agent's own sign-in | On |
| **Resume after the usage limit resets** | When a usage limit cuts off a turn and nothing is queued, sends a "continue" message shortly after the limit resets | Off |

Kepler uses the agent's sign-in only to ask its provider, and never changes it. With **Check plan usage with each agent's provider** off, Kepler shows only what agents report, and sends a message queued at a usage limit automatically only if the agent says when the limit resets.

***

---
