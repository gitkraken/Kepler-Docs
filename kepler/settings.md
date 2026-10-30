---
title: Settings
description: A reference for every setting in Kepler across the 15 Settings pages, plus folder locations, branch prefixes, the Variables menu, per-repository commands (including setup commands that run on every new worktree), worktrees and branches, themes, MCP server defaults, notifications, and the keyboard shortcut list.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, bitbucket-data-center, azure-devops, azure-devops-server]
integrations: [claude-code, codex, copilot, cursor, antigravity, opencode, pi, auggie, grok, github, gitlab, bitbucket, azure-devops, jira, jira-data-center, linear, trello]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [settings, configuration, keyboard-shortcuts, appearance, agents, tasks, notifications, updates, mcp-servers, actions, repositories, worktrees, terminal, voice-input, remote, remote-environments, remote-access, logs, gitkraken-dev, integrations, preferences]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Settings has 15 pages, each with its own sections. This page documents every one of them: what each setting controls, what it defaults to, and what changes when you change it.

Open Settings from the gear icon in the top bar, or with **⌘ ,** (**Ctrl ,** on Windows and Linux). The same shortcut closes Settings again, the way the gear button does.

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-general-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-general-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Settings open on Repositories. The left rail starts with Search settings and Setup, then lists Account; Agents, Tasks, Repositories, Integrations and Actions; General, Notifications, Appearance, Voice input and Keyboard shortcuts; Remote environments and Remote Access; and Updates and Help, with Repositories' section links expanded under it.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings, open on Repositories.</figcaption>
</figure>

***

## The Settings pages

The left rail starts with a **Search settings** field and **Setup**, a progress ring that reopens the first-run checklist. Below them, the rail lists the pages in five unlabeled groups, separated by thin lines. The following table lists the pages in rail order:

| Page | What it covers |
|---|---|
| **Account** | Who you're signed in as, your organization, what your plan unlocks, and GitKraken AI credits |
| **Agents** | Your agents, custom agents, MCP servers, agent tools, approvals, and usage limits |
| **Tasks** | How new tasks start, including the default agent and the agent new sessions start with, and how a task's page looks |
| **Repositories** | The repositories folder, your repos and folders, worktrees and branches, and Projects |
| **Integrations** | Issue tracker and Git host connections, and sessions started in your own terminal |
| **Actions** | Preferred Actions per item kind, and the Action list |
| **General** | Language, windows, the default editor, and keeping agents running |
| **Notifications** | Which agent events notify you, on the desktop and in Kepler |
| **Appearance** | Light or dark appearance and themes, the chat, the terminal font, code font size, and diff layout |
| **Voice input** | On-device speech-to-text, its transcription engine, and learned words |
| **Keyboard shortcuts** | Kepler's keyboard shortcuts |
| **Remote environments** | The machines your agents can run on, over SSH or WSL |
| **Remote Access** | Opening this Kepler from another device |
| **Updates** | The installed version and app updates |
| **Help** | The docs, release notes, onboarding guides, and Kepler's logs |

**Account** is first because it's the only page about the *person* rather than the app, and it's where the account menu hands off to.

### Find a setting

To find a setting by name, type in **Search settings**. Search matches section titles, control labels, help text, and common synonyms, so a word like *theme* or *notifications* finds the right section. With no match, the results read *No settings match "{query}"*.

Under the page you have open, the rail lists that page's main sections so you can jump to one. Under **Agents**, the rail also lists each supported agent below **Your agents**. A page with fewer than two listed sections shows no list.

### Sub-pages and unsaved changes

Item editors open as sub-pages inside their Settings page, with a breadcrumb back to the page. Examples include a repository, a project, a custom agent, an MCP server, and an Action.

If you leave a sub-page with unsaved changes, Kepler asks before it discards anything. It asks on every way out: **Escape**, **Back**, the form's own **Cancel**, a page in the Settings rail, or a link elsewhere in the app:

- A form that can save asks **Save your changes?**, with **Cancel**, **Don't save**, and **Save**.
- A form that has nothing to save yet, such as a step-by-step add flow, asks **Discard your changes?**, with **Keep editing** and **Discard**.

A form with a **Save** button keeps it in a footer with **Cancel**. While you have unsaved edits, the footer reads *Unsaved changes*. If a save fails, the footer shows why and keeps your edits on the form. A save that succeeds confirms with *Saved {name}*.

Most fields outside those forms save themselves. Each one shows its own status beside it: **Saving**, **Saved**, or **Unable to save** with the reason. A switch shows only **Saving** and a failure. If a save fails after you've left the page, Kepler tells you which setting it was: *Unable to save {label}*.

Moving between pages replaces a single history entry. As a result, **Back** returns you to whatever you were doing before you opened Settings, rather than walking back through every page you visited.

### Settings in a remote window

In a window connected to a remote environment, Settings shows that machine's settings, and its header names the machine. Each page states under its title where its settings are saved: **Saved on {machine}** or **Saved on this machine**. A section that saves somewhere other than its page carries its own badge. The **Saved on this machine** tooltip reads *Applies to every Kepler window on this machine, whichever machine it's connected to.* To change this machine's own settings from such a window, click **Open this machine's settings** in the header: it opens the same page in a local window.

### Deep links and section anchors

Every section has a stable anchor id. A link of the form `/settings/<page>#<section-id>` opens that page and scrolls to the section.

A bare `/settings` opens the last page that window had open, or **Agents** if there's none. Legacy links of the form `/settings#<section-id>` still work: Kepler resolves the id to the page that owns that section and keeps the hash. An id that no page owns anymore, such as `general`, `windows-and-notifications`, `keyboard-shortcuts`, or `features`, opens **Agents**.

The following table lists each page's path with its section anchors, in page order:

| Page path | Section anchors, in page order |
|---|---|
| `/settings/account` | `account`, `plan-features`, `ai-credits` |
| `/settings/agents` | `agents`, `custom-agents`, `mcp-servers`, `agent-git-tools`, `approvals`, `usage-limits` |
| `/settings/tasks` | `new-tasks`, `default-agent`, `task-page` |
| `/settings/repositories` | `repositories-root`, `repositories`, `worktrees`, `projects` |
| `/settings/integrations` | `provider-integrations`, `agent-options` |
| `/settings/actions` | `preferred-actions`, `action-list` |
| `/settings/general` | `language`, `windows`, `default-editor`, `keep-running` |
| `/settings/notifications` | `system-notifications` |
| `/settings/appearance` | `appearance`, `transcript`, `terminal`, `code`, `diff-view` |
| `/settings/voice` | `voice`, `voice-engine`, `voice-dictation`, `voice-learned` |
| `/settings/keyboard-shortcuts` | `shortcuts-general`, `shortcuts-navigation`, `shortcuts-dashboard`, `shortcuts-task-page`, `shortcuts-chat`, `shortcuts-changes` |
| `/settings/remote-environments` | `remote-environments`, `found-machines`, `remote-windows` |
| `/settings/remote-access` | `remote-access` |
| `/settings/updates` | `updates` |
| `/settings/help` | `onboarding-help`, `logs` |

`default-agent` sits inside **New tasks** rather than being a section of its own. From the rail or search, `worktrees` opens the **Worktrees and branches** sub-page instead of scrolling to its row. Each agent also gets its own anchor on the Agents page, `agent-<agent-id>`, for example `agent-claude-code`, and each custom agent gets `custom-agent-row-<id>`.

When search, or a pointer on another page, sends you to one setting, Kepler marks that setting as you arrive, then fades the mark, and moves focus to it.

***

## Account

The Account page has three sections: **Account**, **Unlock more with Kepler**, and **GitKraken AI credits**. The following table lists its controls:

| Control | What it does |
|---|---|
| **Account** | Who you're signed in as, with your name and email |
| Organization | Your active organization and its plan. When your GitKraken account belongs to more than one organization, this line becomes a switcher. What a feature costs, and whether it's unlocked at all, follows the organization you're acting as |
| **Refresh account status** | Re-reads your plan. Kepler also picks up a purchase or plan change made outside the app on its own, with no restart |
| **Manage account** / **Manage subscription** | Opens your GitKraken account or subscription on gitkraken.dev |
| **Unlock more with Kepler** | What this plan does and doesn't include. Shown only while something is left to unlock |
| **GitKraken AI credits** | Your credit balance, with **Buy credits**, and **Your usage by feature**. Shown only when there's a balance to show |

**Your usage by feature** shows where your AI credits went. A stacked bar splits your use between your three most-used AI features and everything else as **Other**. Below the bar, each feature has a row with its share of your use as a percentage, such as **Commit Message**, **Conflict Resolution**, **Compose Changes**, or **Task & branch names**. Hover a feature's help icon for what it does. The breakdown appears only once you've used an AI feature.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ai-usage-breakdown-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ai-usage-breakdown-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The GitKraken AI credits section of Settings › Account: Your weekly usage 412,500 / 3.2M (13%, resets Sun, Mar 8), Shared weekly credits 18.4M / 80M, and Your usage by feature, a stacked bar over Commit Message 38.3%, Conflict Resolution 27.2%, Compose Changes 18.5%, Task & branch names 9.9% and Pull Request 6.1%, each with a help icon, above Buy credits.">
  </a>
  <figcaption style="text-align:center; color:#888">GitKraken AI credits, with your usage by feature.</figcaption>
</figure>

When a feature is locked on the organization you're acting as but included on another one you belong to, Kepler says so and offers the switch rather than sending you to a paywall: *{organization} ({plan}) already includes this.*, with **Switch to organization**.

A paywall also asks **Already upgraded?** with **Check again**, for a plan you've just changed. If nothing has changed, it says so briefly: *Still on {plan}*. A paywall that covers the whole window also shows an account card: **Signed in as**, your **Current organization**, and a **Switch** button for each other organization whose plan includes the feature.

### Trials

When a trial starts, a dialog reads **You just opened up all of Kepler**, with a pill showing how many days are free (*{count} days free*). It lists what the trial unlocks: *Every feature below is yours until {date}.* When the trial ends, a dialog reads **Your trial has ended** and lists **What your trial included**. It offers an upgrade or, when your account can start the trial again, a way to pick up where you left off.

***

## Agents

*The coding agents that work on your tasks: install them, sign in, choose how you work with each, and give them more tools.* The page opens with a line that names your default agent, *New tasks use {agent}.*, and a **Change in Tasks** link to [Default agent](#default-agent).

The Agents page has six sections: **Your agents**, **Custom agents**, **MCP servers**, **Agent tools**, **Approvals**, and **Usage limits**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-settings-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-settings-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Settings › Agents: the page description, New tasks use Claude Code with Change in Tasks, and Your agents with Update all and Re-scan above the Claude Code card, which shows its account (alex.lee@example.com, Acme, Default), New sessions start in set to Chat, Let artifact comments start turns, and a collapsed Program and data folder.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings → Agents.</figcaption>
</figure>

### Your agents

Kepler ships adapters for **Claude Code**, **Codex**, **GitHub Copilot**, **OpenCode**, **Pi**, **Auggie**, **Antigravity**, **Cursor**, and **Grok Build**. Settings lists the agents installed on this machine first, then the rest, each group in that order.

Two buttons sit in the section header: **Update all** runs each installed agent's own updater, and **Re-scan** re-detects the agent CLIs installed on this system. Run **Re-scan** after you install or remove an agent outside Kepler.

Each card's title line carries the agent's name and these controls:

| Control | What it does |
|---|---|
| Version | The installed version. **Not installed** when Kepler can't find the CLI. A warning-toned **Version unknown** means Kepler was unable to read it, which turns off features that depend on the version, such as sending a new session's first message automatically. Reinstalling or updating the agent usually fixes it |
| **Update** | Runs the agent's updater and streams its output. Shown when Kepler has an updater for that agent |
| **Install** | Runs an install method on your behalf and streams the output. Shown on a not-installed agent that has an installer for your OS. **Cancel** stops an install in progress: *Install cancelled: {name}* |
| **Enabled** | *Off keeps it installed but hidden when you start work.* |

When the installed version of an agent, or of one of its components, is known to misbehave, a warning note sits on the card under the title line. The note names the version and says what to do. Kepler ships these notes:

| Note | What it means |
|---|---|
| *OpenCode {version} is not supported* | Sessions with this version won't start. Install OpenCode 2, or choose an OpenCode 2 binary under **Program and data folder** |
| *Auggie {version} may not load your MCP servers in chat* | Kepler's fix for how Auggie loads MCP servers covers only the Auggie versions it was built for |
| *ACP server {version} can fail to start on Linux* | Antigravity's Chat server can be killed at startup on some Linux systems. Reinstall it under **Program and data folder** |
| *Codex {version} can show approval prompts that need no answer* | Update Codex to 0.163.0 or newer |

The card body holds the rest:

| Control | What it does |
|---|---|
| **Accounts** | Runs multiple logins side by side, each with its own credentials and history but sharing your skills, agents, commands, and settings. **Add account** asks whether its conversations **Keep separate** or **Share with the CLI**. Each account row has a color picker that tints the agent icon wherever that account runs (the default account stays uncolored, so its picker shows the ⊘ **No color** mark), plus **Sign in** and an account menu with **Rename**, **Share history with the CLI**, **Sign in another way**, **Sign out**, and **Remove account**. On a signed-in Claude Code account, the menu also has **Switch account…**, which signs that account in with a different Claude login (see below). Removing an account stops its running sessions and deletes the sessions stored only in it, unless you first **Move to CLI account**; see [Agent Sessions](/kepler/agent-sessions#several-accounts-for-one-agent). Available for Claude Code, Codex, GitHub Copilot, Auggie, and Grok Build |
| **Account** | On an agent with a single login: who is signed in, with **Sign in** or **Sign out**. Signing out deletes the stored credentials |
| **New sessions start in** | The default mode for new sessions. See below |
| **Artifacts in new sessions** | Claude Code only. See below |
| **Let artifact comments start turns** | Claude Code only. See below |
| **Program and data folder** | A disclosure holding **Binary**, **Components**, and **Data folder** |

Under **Program and data folder**:

| Setting | What it controls | Default |
|---|---|---|
| **Binary** | The binary Kepler spawns. **Auto** resolves it the way your shell does (the first match on your `PATH`), so it matches `which`. Pick a specific install, or **Custom path…**, to override. **Re-scan** searches again | Auto |
| **Components** | Extra pieces an agent can need, such as its CLI for Terminal mode (*Needed for Terminal mode.*), each with **Install** or **Update to {version}** | None |
| **Data folder** | *Overrides the agent's default data and config folder.* | Empty, meaning the agent's own default |

**Codex runs your own CLI.** Kepler resolves and spawns the `codex` you have installed, like every other agent. Usage figures read the OAuth token from `~/.codex/auth.json`, or `CODEX_HOME/auth.json` when you have set a custom data folder.

**OpenCode needs version 2.** Kepler reads and resumes only OpenCode 2's sessions, and a session won't start on an OpenCode 1 binary: the card shows *OpenCode {version} is not supported*. If you have both installed, point **Binary** at OpenCode 2. A conversation you started under OpenCode 1 resumes from OpenCode 2's copy of it. **Antigravity** runs in Chat through its ACP server, a separate component from its `agy` terminal CLI. See [Agent Integrations](/kepler/agent-integrations).

#### When an added account stops sharing your settings

An added account shares your own settings, instructions, skills, agents, commands, and other configuration by linking to your files. If the agent saves a change while signed in to that account, it can write its own copy in place of the link, and the account stops following your file. Kepler flags this under the account's row: *This account stopped sharing your {items}*. Expand it to see both paths, **This account's copy** and **Your {item}**, and choose one of the following:

- **Share your {item} again** asks first, then links the account back to your file. *Its own copy is saved as a backup next to it, so nothing is lost.*
- **Keep its own {item}** keeps the account's copy. The row's menu then offers **Share your {item} again** if you change your mind.

#### Switch the account a Claude Code login uses

**Switch account…** opens **Switch the account for {name}?**, which names the login now signed in. *If your browser is already signed in, choose a different account on the sign-in page.* The dialog also warns you about the following:

- How many running sessions use the account, and when they pick up the new login: when they restart, or on their next request.
- On the default account, the one the CLI uses, the switch *also changes the account the claude command uses in your own terminals.*

**Continue** opens the usual sign-in. When it succeeds, Kepler confirms: *{name} is now signed in as {login}.*

#### Default mode for new sessions

Every agent that can run both ways carries this setting:

| Setting | What it controls | Default |
|---|---|---|
| **New sessions start in** | **Chat**: *{agent} built into Kepler, with replies, diffs and plans you can read, review and search.* **Terminal**: *{agent}'s own command-line app, with its commands, shortcuts and settings, just as you use it today.* | Chat. Google Antigravity starts on Terminal, because its Chat server signs in separately |

The choice is saved per agent, so one agent can default to Terminal while another stays on Chat. The help text reads *You can pick the other one when you start a session.*: a new session can start in the other mode without changing the setting. A terminal-only agent shows **Terminal** with no switch. See [Agent Sessions](/kepler/agent-sessions#how-a-session-runs).

#### Artifacts in new sessions

The following setting is on Claude Code's card:

| Setting | What it controls | Default |
|---|---|---|
| **Artifacts in new sessions** | *The Artifact tools let the agent publish pages and designs. They add about 12k tokens to the context of every session that has them. Each session can still turn them on or off from its session menu.* | Off |

A running Chat session has its own **Artifacts** switch in its agent settings. Turning it on restarts the session and resumes the conversation, after Kepler asks **Turn on Artifacts?**. Once a conversation has artifacts on, they stay on for it. See [Agent Sessions](/kepler/agent-sessions).

#### Let artifact comments start turns

The following setting is on Claude Code's card:

| Setting | What it controls | Default |
|---|---|---|
| **Let artifact comments start turns** | Anyone with edit access to an artifact a Chat session publishes can start a turn in that session by sending a comment to Claude. A reply is posted automatically | On |

Running sessions keep the value they started with. When you change it, the card lists the sessions still using the previous value, marking those that **Published an artifact** or have a **Turn in progress**, with **Restart all** and **Restart selected ({count})**. Restarting keeps each conversation. A turn in progress is interrupted, and a restarted session stops watching artifacts it published before.

### Custom agents

*Run an agent that isn't listed above by giving Kepler its command.* To add one, click **New custom agent** in the section header. To edit one, click its row. Either opens the agent as a sub-page with these fields:

| Field | What it takes |
|---|---|
| **Name** | The name Kepler shows for the agent |
| **Command** | The program to run, for example `/usr/local/bin/my-agent` or `my-agent` |
| **Args (one per line)** | Arguments passed to the command |
| **Environment variables (KEY=value, one per line)** | Environment for the command |
| **Runs in** | **Chat**: *Kepler's chat. Needs a program that speaks ACP (the Agent Client Protocol).* **Terminal**: *The command's own app, in a terminal.* |

Added agents appear with the built-in agents everywhere an agent can be picked. With none added, the section reads *No custom agents yet.*

Kepler encrypts environment values at rest and hides existing ones when you edit an agent. Leave a value empty (`KEY=`) to keep the stored secret, or type a new value to replace it.

**Save** waits until the agent is stored. If the save fails, the form stays open with the reason: *Unable to save {name}: {reason}*. **Delete** asks first, **Delete custom agent?**: it *Deletes {name} and the environment values stored with it.* and can't be undone.

### MCP servers

*Give your agents extra tools, like a database, a browser or your issue tracker.* This section shows each agent's own MCP server defaults, which every project inherits.

To see the servers an agent loads, pick it with **Agent**, and pick an account when that agent has more than one. Only agents that expose their MCP servers to Kepler are listed. In the list:

- Click a server to open its own page. There you can turn the server or a single tool off, sign in to a server that needs it, use **Also add to…** to copy the server to another agent, and **Remove server**.
- Click **Add server** in the section header to add one.

A server or tool you turn off here is off in every repository, unless a repository turns it back on for itself. A repository's own **MCP servers** section is on its [Edit repo](#edit-a-repository) page. See [MCP Servers](/kepler/mcp-servers).

Below the list, one more setting applies across every agent:

| Setting | What it controls | Default |
|---|---|---|
| **Keep the GitKraken MCP server installed in every agent** | *Gives every command-line agent Git tools and your issues and pull requests through GitKraken. Turn off to manage it yourself.* | On |

This setting is about the MCP clients on your machine. It differs from the workspace MCP server that Kepler attaches to every session it starts itself, which is always on and has no setting. That server's tools are named by what they act on, such as `task_get`, `session_start`, or `worktree_create`. They give the agent tools to:

- Read a task and its resources, find tasks, create a task, change its Progress stage, name, or hold, and archive it.
- Read, write, and delete the task's notes.
- Attach and detach issue, pull request, and URL links, and attach or detach files.
- List the agents, repositories, and folders in your workspace. An agent can name a repository by one of its [aliases](#edit-a-repository).
- Create, attach, detach, update, or delete one of the task's worktrees.
- List and read sessions, start a session with the agent it chooses, send follow-ups, rename or archive a session, and read the reports its own sessions send back.
- List pending approvals.
- Read and save themes. See [Theme](#theme).
- Rebase, merge, and compose commits, when [Agent tools](#agent-tools) turns them on.

Every workspace tool runs without the agent's own permission prompt, in Chat and Terminal alike. Instead, an action that needs your say, such as deleting a worktree or changing another task, waits for you on an approval card. See [Approvals](#approvals), and [Tasks and Resources](/kepler/tasks-and-resources) for the full list of tools.

### Agent tools

*Kepler's own tools your agents can call, starting with rebasing, merging and cleaning up commits.* The following table lists them:

| Setting | What it does | Default |
|---|---|---|
| **AI Sync** | *Lets agents rebase or merge your branch and resolve conflicts for you. Every change can be undone.* | Off |
| **AI Compose** | *Lets agents turn messy changes into clean, focused commits. Every change can be undone.* | Off |

**AI Sync** and **AI Compose** add their tools to the workspace MCP server. Both require a paid GitKraken subscription. On the Community plan, they show a lock: *Not available on the Community plan. Upgrade to unlock.* Turning either on confirms that *New agent sessions will pick up this change.* Sessions already running keep the tools they started with.

### Approvals

*Some actions your agents take wait for your approval. These rules approve them for you; anything not covered still asks.*

When an agent asks, through Kepler's workspace tools, to do something that needs your say, Kepler pins an approval card above that session's message box. Examples include deleting a worktree, sending a prompt to another session, or rewriting a branch. The card's **Approve** menu offers **Always approve** for that kind of action. Kepler doesn't offer it for actions that can lose work. See [Agent Sessions](/kepler/agent-sessions).

Each rule you create this way is listed under **Always approved**. A rule's row says when and where you added it, *Added {date} from {session} on {task}.*, and how often it has run, *Used {count} times, last {when}.* or *Not used yet.* **Remove** deletes the rule, so that kind of action asks again. With no rules, the section reads *No rules yet. When an agent asks, choose Always approve on its request to stop being asked about actions like it.*

### Usage limits

Two settings handle your agent plans' usage limits:

| Setting | What it controls | Default |
|---|---|---|
| **Check plan usage with each agent's provider** | *Kepler asks each agent's provider for your plan usage, per-model limits and extra usage, using the agent's own sign-in. The sign-in goes nowhere else and is never changed. When off, Kepler shows only what agents report, and a message queued at a usage limit is sent automatically only if the agent says when the limit resets.* | On |
| **Resume after the usage limit resets** | When a turn is cut off by your account usage limit and nothing is queued, Kepler queues a "continue" message that is sent shortly after the limit resets | Off |

***

## Tasks

*A task is one piece of work: its prompt, the agent sessions working on it, and the worktree or folder they work in. Set how new tasks start and how a task's page looks.*

The Tasks page has two sections: **New tasks** and **Task page**.

### New tasks

This section sets what Kepler preselects for every new task. Its values belong to the environment you're working on, so in a remote window they're that machine's.

#### Default agent

**Default agent** picks the agent, account, model, mode, and thinking effort that Kepler preselects for a new task. Its description reads *Used when new sessions start with the default agent, when Kepler has no earlier pick to go on, and whenever you choose Use default agent in the launcher.* The following table lists its controls:

| Control | What it does |
|---|---|
| **New tasks use** | Chooses the agent, and the account when that agent supports more than one |
| Options | Model, mode, and the agent's own configuration options. Available once an agent is picked |
| **Clear default** | Removes the saved default. Appears only once one is set |

Nothing is set out of the box, and the control is hidden entirely when no agent is installed. If the agent you saved is later uninstalled, the row warns you: *Your default agent, {name}, is no longer installed. Pick another.*

An [Action](/kepler/actions) inherits this configuration unless it names an agent of its own.

#### New sessions start with

Under **Default agent**, the following setting decides which agent the Task Composer, the Dashboard's composer, and a new draft session preselect:

| Option | What it does |
|---|---|
| **Last used agent** | *The agent, model and mode you last picked.* The default |
| **Default agent** | *Always the default agent above.* |

With **Last used agent**, a task an agent created that has no session yet starts with the agent that created it. An Action's own agent isn't remembered as your last pick. If you choose **Default agent** with no default set, Kepler points you at the **Default agent** picker.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-sessions-start-with-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-sessions-start-with-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The New tasks section of Settings › Tasks: New tasks use Claude Code CLI with Options and Clear default, its description, and New sessions start with offering Last used agent (The agent, model and mode you last picked) beside Default agent (Always the default agent above).">
  </a>
  <figcaption style="text-align:center; color:#888">Default agent and New sessions start with, in Settings → Tasks.</figcaption>
</figure>

#### Where new tasks make changes

The following setting chooses what a newly attached repository starts on:

| Setting | What it controls | Default |
|---|---|---|
| **Where new tasks make changes** | What a newly attached repository starts on, in the Task Composer | Isolated worktree |

The following table lists its options:

| Option | What it does |
|---|---|
| **Isolated worktree** | *Own folder, agents run side by side.* Forks a new branch into its own worktree |
| **New branch** | *Switches your repo to a new branch.* Forks a new branch directly in the repository's own checkout, with no worktree |
| **Current branch** | *Works on whatever is checked out.* Runs on the repository's own checkout, on whichever branch it currently has, with no new branch created |

This setting sets the default only. The repository chip's own **Base branch** and **Isolated worktree** controls still override it for any single Task. See [Create a Task](/kepler/create-task#configuring-a-repository).

**Commits made on the current branch land on whichever branch is checked out at the time.** That caveat applies to **New branch** and **Current branch** alike, since both run in the repository's own checkout rather than an isolated one. If another Task is already working in that checkout, Kepler says so and offers to switch that one repository to an isolated worktree instead.

Two settings sit under **Where new tasks make changes**, because they apply only when Kepler creates a branch or a worktree: **Branch prefix** and **Worktrees folder**.

#### Branch prefix

The following setting starts the name of every branch Kepler creates:

| Setting | What it controls | Default |
|---|---|---|
| **Branch prefix** | *Starts the name of every branch Kepler creates. A repo can set its own in its settings.* | `kepler/` |

The prefix applies to **automatic** names only. A branch name you type is used verbatim, which is how a repository with an enforced `feat/` or `fix/` push rule still works. A prefix you type without a trailing separator gains a `/`, so typing `team` stores `team/`. A personal `ea-` style prefix is kept as the literal lead-in it is. The prefix saves when you press **Enter** or **Escape**, or leave the field, and the field shows its save status.

Each repository can override the prefix on its [Edit repo](#edit-a-repository) page under **Settings → Repositories**. If a repository already has a branch literally named after the prefix, Kepler says which one and points you there: *Can't be used in {repo}: it has a branch named {branch}. Set a different prefix for that repository under Repositories.*

#### Folder locations

Three paths tell Kepler where to put things. Two of them are on this page, and the third is on the Repositories page:

| Setting | Where it is | What it controls | Default |
|---|---|---|---|
| **Worktrees folder** | Tasks → New tasks | *Where Kepler creates the worktree for each new task.* | `~/kepler/worktrees` |
| **Tasks folder** | Tasks → New tasks | *Each task gets a folder here for its attachments and files.* | `~/kepler/tasks` |
| **Repositories folder** | [Repositories](#repositories-folder) | Where Kepler clones repositories, and where it looks for repositories to add | `~/kepler/repositories` |

All three are unset out of the box. Kepler computes a fallback under your home folder without writing it, so an untouched setting still reads as untouched.

Type a path directly, or click **Choose a folder** beside the field to browse. Edits save when you leave the field, so no separate Save button exists, and the field shows its save status.

The fields also warn you about paths that won't work as you expect:

- If a **Worktrees folder** has text before `<REPOSITORY_PATH>`, Kepler adds each repository's full path after that text. The field says so, *Each repo's full path is added after this folder.*, shows where an example repository would land, and suggests a template for worktrees next to each repository and one for a subfolder per repository. On Windows, such a path is invalid, so Kepler refuses it: *Not saved: adding each repo's full path after this folder creates an invalid path.*
- If the **Repositories folder** doesn't exist yet, the field reads *This folder doesn't exist yet. Kepler creates it when you clone.*

#### The Variables menu

A folder field that can contain a dynamic variable has a **Variables** menu beside it. The menu shows each variable as a named tag, such as **REPOSITORY PATH**, beside its raw token. Pick a variable and Kepler inserts it at the cursor. Kepler fills it in when it creates the folder, so one pattern covers every repository. Each field offers only the variables it can actually resolve:

| Field | Variables offered |
|---|---|
| **Worktrees folder** | `<REPOSITORY_PATH>` (*Main repo folder*), `<REPOSITORY_NAME>` (*Repo name*) |
| **Repositories folder** | `<REPOSITORY_NAME>` |
| **Tasks folder** | None |

For example, `<REPOSITORY_PATH>/.worktrees/<REPOSITORY_NAME>` nests each worktree inside the repository it belongs to. Kepler collapses any `..` segments you write.

**Tasks folder** takes no variables. A task folder has no repository behind it, so nothing would ever fill one in. Kepler refuses the value rather than storing a path that can't resolve: *Dynamic variables cannot be used here. A task folder has no repository behind it, so nothing would ever fill one in. This value was not saved.*

Per-repository commands have a **Variables** menu of their own, with two more variables. See [Per-repository commands](#per-repository-commands).

<figure style="text-align:center">
  <a href="/wp-content/uploads/folder-fields-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/folder-fields-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Worktrees folder field in Settings › Tasks, set to /home/alex/kepler/worktrees, with its Variables menu open listing the REPOSITORY PATH tag (Main repo folder) and the REPOSITORY NAME tag (Repo name), each beside its raw token, and the Choose a folder button beside the field.">
  </a>
  <figcaption style="text-align:center; color:#888">The Worktrees folder field in Settings → Tasks, with the Variables menu open.</figcaption>
</figure>

#### Automatically name new tasks

The following setting names new tasks for you:

| Setting | What it controls | Default |
|---|---|---|
| **Automatically name new tasks** | *Names a new task with AI from its prompt and attached resources. A task created from a single issue or PR keeps that item's name.* | On |

This setting requires a paid GitKraken subscription. On the Community plan, it shows a lock. A change takes effect on the next task you create.

### Task page

This section sets how a task's page looks in this window. It's saved on this machine:

| Setting | What it controls | Default |
|---|---|---|
| **Show tabs on the task page** | Keeps sessions, worktrees, and resources open as tabs you can pin, drag between groups, and arrange side by side. With it off, each column of a task shows one thing at a time and you switch from the list on the left. See [The task view](/kepler/task-view) | Off |
| **Preview tabs** | *A single click opens a preview that the next click replaces. Double-click, or edit, to keep it open.* Sessions always open as permanent tabs. Needs tabs turned on | On |

***

## Repositories

The Repositories page has four sections: **Repositories folder**, **Your repos and folders**, **Worktrees and branches**, and **Projects**.

### Repositories folder

The following setting tells Kepler where to clone repositories:

| Setting | What it controls | Default |
|---|---|---|
| **Repositories folder** | *Kepler adds the repos it finds in this folder. It only looks when you change the folder or scan, so a repo you remove won't come back.* | `~/kepler/repositories` |

**Scan for repositories**, beside the field, registers every repository it finds there. It reports **Added {count} repositories.** or **No new repositories found.** in a notification. It runs only when you change the setting or press it, never on startup, so a repository you deliberately removed stays removed.

A scan that added repositories offers **Undo**, which removes them again. Undo keeps any repository you've started using or changed since the scan, and says which: *Kept {names}. You've used or changed them since the scan.* If nothing before a variable in the setting is a full folder path, the scan has nowhere to look and says so: *There is no folder to scan: nothing before the dynamic variable in this setting is a full folder path. Point it at one first.*

If the folder doesn't exist yet, the field says Kepler creates it when you clone. The field takes the `<REPOSITORY_NAME>` variable. See [The Variables menu](#the-variables-menu).

### Your repos and folders

This section lists every repository Kepler tracks and every folder you've attached to a task. Each row shows its name, its path on disk, and how many commands it has: **No commands**, **1 command**, or a count. The following table lists the section's controls:

| Control | What it does |
|---|---|
| **Filter repos and folders** | Narrows the list by name |
| **Row** | Click it to open the repository's **Edit repo** page, or the folder's page |
| **Add repo** | Opens the **Add repo** page. See below |
| **Add folder…** | Adds a plain folder |
| **Trash icon** | Untracks the repository or folder. The folder on disk is left untouched |

With nothing tracked, the section reads *Add a repository or folder to manage it here.*

#### Add a repository

**Add repo** opens a sub-page. You give a source, Kepler inspects it, and what it found becomes a card you can edit before you add it:

| Field | What it takes |
|---|---|
| **Folder or URL** | *Paste a URL to clone it, or pick a folder that already holds a repo.* You can also drop a folder onto the page, or **Create a new repo instead** |
| The card | The resolved repository (**{name} on {provider}**, its path, its branch count), plus the name, description, and branch prefix you can edit |

Kepler says what a source resolves to before you commit to it. For example, it reads **A new folder named {name} will be created here.**, *This folder already holds a clone of that repo. It will be added as is.*, or **This repo is already in Kepler.** A path that isn't a Git repository reads **That folder isn't a Git repo.**

While a clone runs, the page reads *Cloning {name} into {folder}* and *You can leave this page. Kepler tells you when the clone finishes.* Leaving doesn't stop the clone. If it fails later, a notification names the repository: *Unable to clone {name}: {reason}*.

#### Edit a repository

Click a repository's row to open its **Edit repo** page. The page shows the repository's path, its remote, and its branches, and has these parts:

| Part | What it holds |
|---|---|
| **Name** | The name Kepler shows wherever it names this repository. The field's placeholder is the folder name. Leave it empty to use the folder name. A repository you name this way keeps that name verbatim and stops competing with same-named folders for a disambiguating suffix |
| **Aliases** | *Short names for this repo when talking to agents, separated by commas.* An agent can name the repository by an alias wherever Kepler's workspace tools take a repository, and finds it by alias when it lists your repositories. An alias can't contain a colon or repeat another repository's alias or name |
| **Description** | Free text. Its placeholder reads *What this repo is for. Agents working in it read this.* Kepler appends it to the repository's line in the resource list it hands a session, so a full sentence is more useful here than a single label |
| **Branch prefix** | Overrides the prefix from **Settings → Tasks** for this repository alone. See below |
| **Commands** | Shell commands for this repository. See [Per-repository commands](#per-repository-commands) |
| **MCP servers** | *Extra tools your agents get in this repo, on top of their own lists. Changes here apply right away.* See [MCP Servers](/kepler/mcp-servers) |

**Name**, **Aliases**, and **Description** are optional. Kepler stores whitespace-only text as empty. The page has no **Save** button: each field saves on its own and shows its save status.

<figure style="text-align:center">
  <a href="/wp-content/uploads/edit-repo-dialog-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/edit-repo-dialog-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Edit repo page for acme-web in Settings › Repositories: its path and main · 2 branches, then Name, Aliases (empty, Short names for this repo when talking to agents, separated by commas), Description and Branch prefix on Default (kepler/) with the example kepler/fix-login-form; the Commands section with Add command, Install deps (Runs on creation) and Dev server; and MCP servers with Add server, Agent set to Claude Code CLI and acme-issues, docs-search and acme-analytics switched on.">
  </a>
  <figcaption style="text-align:center; color:#888">The Edit repo page.</figcaption>
</figure>

##### Branch prefix, per repository

The **Branch prefix** control has three options:

| Option | What it does |
|---|---|
| **Default ({value})** | Uses the prefix from **Settings → Tasks** |
| **None** | Creates task branches with no prefix |
| **Custom** | A prefix for this repository only |

**New task branches will look like** shows an example, so you can see what you're choosing before a branch exists.

**Default** and **None** save the moment you pick them. **Custom** saves its text when you press **Enter** or **Escape**, or leave the field. If the repository already has a local branch named like the prefix, Kepler refuses it rather than saving it: *Can't create {prefix} branches here: this repo already has a branch named {branch}. Rename that branch or choose another prefix.*

Removing a repository deletes its sessions, terminals, and configured commands, and terminates any live agent and terminal sessions tied to it. Kepler confirms before it does.

#### Per-repository commands

*Run your dev server, tests or build from a task's worktree in one click. A command can also run when Kepler creates a new worktree, like installing dependencies.* Commands are shell commands scoped to one repository.

To add a command, click **Add command** in the **Commands** section of the Edit repo page. With no commands, the section reads *No commands yet.* and suggests examples. Each command saves on its own: an open row has its own **Cancel** and a primary button, **Add command** for a new row or **Save** for a stored one. **Enter** in the name field, or **⌘ Enter** (**Ctrl + Enter** on Windows and Linux), also saves the row. Each command row has three fields:

| Field | What it does |
|---|---|
| Name | A label, for example *Install deps*. It's what you pick from the **Run** menu later |
| Command | The shell command, for example `pnpm install`. Its **Variables** menu inserts any of the variables below |
| **Run on worktree creation** | Runs this command automatically when Kepler creates a worktree for this repository. Off by default, which leaves it a command you run on demand. A row with it on shows a **Runs on creation** chip |

Commands accept four variables, which Kepler fills in when the command runs:

| Variable | Resolves to |
|---|---|
| `<REPOSITORY_PATH>` | Main repo folder |
| `<REPOSITORY_NAME>` | Repo name |
| `<SOURCE_PATH>` | Where files come from (the main repo, or the source worktree when forking) |
| `<WORKTREE_PATH>` | The new worktree folder |

Drag a row by its handle to reorder it, or move it from the keyboard with **Alt + ↑** and **Alt + ↓**. A new order saves at once. Order sets the **Run** menu order and the order that commands set to run on worktree creation run in.

A row missing its name or its command can't be saved: Kepler opens it on the missing field, with *Add a name to show in the Run menu.* or *Add the command to run.* **Cancel** discards a row you opened by accident. A closed row that isn't saved yet shows a **Not saved** chip. **Remove command** deletes a saved command at once, with a *Deleted command {name}* notification that offers **Undo**.

Commands flagged to run on worktree creation execute sequentially, in list order, and stop on the first failing command. Kepler skips the rest and reports them as skipped. Each one runs in the new worktree's folder through your login shell, so you don't need to `cd` into it, and tools configured in your shell profile (`nvm`, for instance) are available. Each has a ten-minute timeout.

A failed command does not undo the worktree. The worktree exists but may not be usable. To fix it:

1. Read the command output in the task.
2. Correct the command here.
3. Run it again from the **Run** menu.

To run a command from the task view, right-click a worktree row in the rail and use **Run command here**. It lists that repository's commands and runs the one you pick in that worktree, opening its terminal in place. A repository with none yet reads **No commands yet** and offers **Create command…**, which opens this page and returns you to the task when you leave it. A command that's running shows on the run button and its menus, where you can stop it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/repo-commands-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/repo-commands-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Commands section of the Edit repo page for acme-web: Add command, Install deps (pnpm install) with the Runs on creation chip, and Dev server open for editing with its name, Run on worktree creation, the command pnpm dev with Variables, and Cancel and Save, above the note that commands run in the worktree folder with your login shell.">
  </a>
  <figcaption style="text-align:center; color:#888">A repository's Commands, with one row open for editing.</figcaption>
</figure>

### Worktrees and branches

*Update, clean up and delete worktrees and local branches across your repositories.* On the Repositories page, this section is one row, **Manage worktrees and branches**. Click it to open the **Worktrees and branches** sub-page.

*See which worktrees and local branches of your repositories are stale, update the ones that can be brought up to date, and delete what is done.* The sub-page reads your repositories as soon as it opens, and deletes nothing on its own. It lists every worktree, and every local branch that no worktree holds, grouped by repository. A summary such as *{worktrees} and {branches} in {repos}.* says how many look safe to delete. A branch with no worktree reads **Not checked out** where a worktree shows its path. The base branch carries a **Base** badge and is never deleted.

The following table lists the sub-page's controls:

| Control | What it does |
|---|---|
| **Search branch, path or repo** | Narrows the list. Every word you type must match the branch, the path, or the repository name |
| **Show worktrees and branches** | Filters by status: **Safe to delete ({count})**, **Needs update ({count})**, **Conflicts ({count})**, **Stale ({count})**, or **All ({count})**. A count reads *checking…* until Kepler has compared each branch with its base |
| **Show worktrees, branches or both** | **All**, **Worktrees only**, or **Branches only** |
| **Stale after** *n* **days** | How many days without activity before a worktree or branch counts as stale. Defaults to 14 |
| **Re-check** | Fetches every repository's remotes, then inspects the list again. A repository whose fetch failed says so beside its name: *Unable to fetch: {reason}; numbers may be stale* |
| **Select all safe to delete** / **Select all that need an update** / **Select all with conflicts** / **Select all stale** / **Select all** | Selects the rows in the current view |
| Selection bar | Reads *{count} selected*, or *{count} selected · {hidden} hidden by filters*, with **Clear**, **Update**, and **Delete**. **Update** and **Delete** act only on the selected rows you can see |

Each row shows how it stands with its upstream: commits to push (↑) and pull (↓), **No upstream**, or **Upstream gone**. Badges then compare it with its base: **{count} behind {base}**, **Conflicts with {base}**, or **Up to date with {base}**, plus how many files are uncommitted. A row also says how long since it was touched and why it may be finished, such as being merged into its base. On the right, it shows the tasks using it, an **External** count for sessions started outside Kepler, and its pull request. A branch row shows the tasks, sessions, and pull requests tied to that branch.

A row counts as one or more of the following:

- **Safe to delete**: *Its work has landed: merged into the base or its pull request merged (a branch whose upstream is gone and whose pull request was closed counts too), and nothing is uncommitted, unpushed or in use.*
- **Needs update**: behind the base branch with no known conflict, so an update can bring it up to date.
- **Conflicts**: behind the base branch, and merging the base in would conflict, so you have to update it by hand.
- **Stale**: no activity for longer than the stale threshold, but nothing proves the work landed. It may still hold uncommitted or unpushed work, so deleting it can lose something.

**Needs update** and **Conflicts** leave out rows that are safe to delete. Activity includes what Kepler recorded on the branch, not only changes in the worktree.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-worktree-cleanup-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-worktree-cleanup-01-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Repositories › Worktrees and branches: 4 worktrees and 2 branches in 1 repo, 3 look safe to delete, with Stale after 14 days and Re-check; Search branch, path or repo, the Safe to delete (3), Needs update, Conflicts, Stale and All filters, and All / Worktrees only / Branches only. Under acme-web, kepler/old-banner and kepler/promo-page (worktrees tagged Spring sale banner) and kepler/summer-teaser (Not checked out) are each 3 behind main and merged into main; old-banner and summer-teaser are ticked, and the bar reads 2 selected with Clear, Update and Delete.">
  </a>
  <figcaption style="text-align:center; color:#888">The Worktrees and branches sub-page, filtered to what is safe to delete.</figcaption>
</figure>

#### Delete worktrees and branches

Select rows, then click **Delete**. The confirmation, **Delete {count} items?**, says what is lost:

- For worktrees: *The directories are removed from disk. Anything listed below is lost with them.* **Also delete the branches** deletes each worktree's branch too.
- For local branches: *The local branches are deleted. Commits that exist only on them are lost.* When every branch's work has landed, it reads *Their work is already in the base branch, so nothing is lost.* instead. Each branch that isn't merged is marked **not merged**. **Force delete branches that are not merged** deletes those too, and **Also delete the branches on the remote** deletes the remote branches.

<figure style="text-align:center">
  <a href="/wp-content/uploads/worktree-branch-delete-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/worktree-branch-delete-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Delete 2 items? dialog for two local branches: The local branches are deleted, with Force delete branches that are not merged and Also delete the branches on the remote unticked, kepler/size-guide marked not merged, and Cancel and Delete 2 items.">
  </a>
  <figcaption style="text-align:center; color:#888">Deleting two local branches, one of them not merged.</figcaption>
</figure>

Kepler keeps any branch it can't delete safely and says why, for example *Checked out in {path}. Remove that worktree first.* or *Its work is not in the base branch, so it was kept.*

A lock Kepler itself left on a worktree, for a task this install knows or a task since deleted, is cleared and the worktree deleted. Kepler never deletes a repository's main checkout. It keeps any worktree that still has uncommitted or unpushed work, other tasks, running agent sessions, or a lock from another tool, and says why for each. Where forcing can help, the result offers **Force delete**, which discards the listed work and ends the agent sessions running there.

#### Update worktrees

To bring several worktrees and local branches up to date with their base branch at once:

1. On the Worktrees and branches sub-page, select the worktrees and branches.
2. Click **Update**. The **Update worktrees** dialog opens: *Each branch is brought up to date with its base. Nothing changes until Update is pressed.*
3. Review the plan. Each row reads **Will update** with how many commits it's behind, **Up to date**, or **Skipped** with the reason, such as *an agent is working in it*, *uncommitted changes*, *checked out in a worktree*, *would conflict*, or *a sync result is waiting for review*.
4. Under **How to update**, choose **Rebase** or **Merge**.
5. To push each updated branch too, tick **Push after update**. Each row that will update then reads **Will push**, or **No upstream, update only** for a branch with no upstream.
6. Click **Update**.

Kepler updates a local branch that has no worktree in place, from the repository's main checkout, without checking it out. It skips such a branch when a worktree holds it, or when the main checkout has uncommitted changes. If an update was prepared but couldn't be applied on its own, Kepler keeps it for you to review instead of discarding it.

While the update runs, each row shows its status: **Waiting**, **Updating…**, **Updated**, **Up to date**, **Skipped**, **Conflict**, or **Failed**. When it finishes, you can undo one row with **Roll back**, or every row with **Roll back all**. If you didn't push during the update, **Push** and **Push all** push the updated branches that have an upstream. A branch that moved since the update isn't pushed. The finished report stays in every window until you click **Dismiss**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-worktree-batch-update-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-worktree-batch-update-01-v3@2x.png" class="help-center-img img-bordered" alt="The Update worktrees dialog with How to update set to Rebase and Push after update ticked: kepler/gift-card-ui is Up to date, kepler/old-banner Will update · 3 commits behind with No upstream, update only, kepler/wishlist is Skipped · uncommitted changes, and kepler/summer-teaser Will update · 3 commits behind with Will push. The footer reads 2 worktrees to update beside Cancel and Update.">
  </a>
  <figcaption style="text-align:center; color:#888">The Update worktrees plan, with Push after update ticked.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-worktree-batch-update-02-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-worktree-batch-update-02-v3@2x.png" class="help-center-img img-bordered" alt="The finished update on the Worktrees and branches page: Update finished, 2 updated · 1 pushed, with Roll back all and Dismiss; kepler/old-banner reads Not pushed: no upstream and Updated, kepler/summer-teaser Pushed and Updated, each with Roll back.">
  </a>
  <figcaption style="text-align:center; color:#888">The finished update, with Roll back on each row.</figcaption>
</figure>

### Projects

*Group repos that belong together under one name.* A **Project** groups repositories so they act as a unit, such as a frontend and a backend you change together. The following table lists the section's controls:

| Control | What it does |
|---|---|
| **Row** | Shows the project's name and its repository count. Click it to open the project's page |
| **New project** | Opens a page where you name a project and pick its repositories. **Add from folder** adds a repository without leaving the page |

A new project shows **Create** and **Cancel**, and **Create** refuses a blank name: *Give the project a name.* Once the project exists, its page has no **Save** button: its name saves as you edit it, and each repository you tick or untick saves at once. A folder's page saves its name and description the same way. A project's page also has **Delete project**. Deleting a project keeps its repositories in your repository list. With no projects, the section reads *No projects yet.*

***

## Integrations

*Bring your work into Kepler: start tasks from your issues and pull requests, and follow agent sessions you run in your own terminal.* The Integrations page has two sections: **Issues and pull requests** and **Your terminal**.

### Issues and pull requests

Connect your issue and pull request providers to see them in the Task Composer and in [the Kepler interface](/kepler/kepler-interface). Kepler lists every supported provider whether or not it is connected, in this order:

| Provider |
|---|
| Azure DevOps |
| Azure DevOps Server |
| Bitbucket |
| Bitbucket Data Center |
| GitHub |
| GitHub Enterprise |
| GitLab |
| GitLab Self-Hosted |
| Jira |
| Jira Server / Data Center |
| Linear |
| Trello |

Each provider row carries these controls and states:

| Control | What it does |
|---|---|
| **Connect** | Starts the connection flow for a provider you have not connected |
| **Connected** | Shown on a working connection |
| **Reconnect** | Refreshes an expired token. A **Sign-in expired** badge and the hint *Sign-in has expired. Click Reconnect to refresh this provider's token.* mark the rows that need it |
| **Cannot connect to server** | The provider's server didn't answer. The integration is still connected, and this clears on its own once the server responds. Check that it's reachable from your network or VPN. No reconnect needed |
| **Unexpected response** | The provider answered with data Kepler was unable to read, so some of its items may be missing. The integration is still connected and reconnecting won't fix it, so if it persists, check for a proxy or gateway between Kepler and the provider |
| **Disconnect** | Disconnects the provider from GitKraken everywhere: every GitKraken product and service that uses this connection loses access too. Other accounts for that provider stay connected, and you can reconnect at any time |
| **Refresh** | Re-checks every provider's connection status. It's in the section header |

Providers connect through your GitKraken account, so the section asks you to sign in before it shows anything to manage.

A self-hosted provider, such as GitHub Enterprise, Azure DevOps Server, Bitbucket Data Center, or Jira Server / Data Center, connects with a personal access token. **Connect** or **Reconnect** opens **Connect {name}**, with **Server URL** and **Personal access token**. **Save connection** checks the token against your server from this machine, saves the connection here, and syncs it to your GitKraken account. Until the sync finishes, the row shows **Cloud sync pending**. See [Pull Request Integrations](/kepler/pull-request-integrations) and [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

Every connected provider except Trello also has a line that reads **Everything visible** or **{count} hidden**, with **Choose what's visible…**. It opens **Choose what {name} brings in**, where you untick the organizations, repositories, or tracker projects you don't want. *Hidden items are left out of the dashboard, the launcher and pickers. Tasks and branches already linked to them keep resolving.* The choice is saved on your GitKraken account. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

When a provider has more than one account, an **Accounts** block lists them. **Set as primary** chooses which account Kepler acts as, and **Read from this account** chooses which one Kepler reads issues and pull requests from. They can be different accounts.

When an organization refuses a working connection (it blocks third-party OAuth apps, or hasn't approved GitKraken), the row names the organization and says its items aren't shown, with a link to fix it, such as **Request access on GitHub**.

Under the list, *Agents can use these through the GitKraken MCP server.* links to [MCP servers](#mcp-servers).

For per-provider setup, see [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

### Your terminal

The following setting covers agent sessions you start outside Kepler:

| Setting | What it controls | Default |
|---|---|---|
| **Show sessions started outside Kepler** | *Lists sessions you start in your own terminal, so you can follow and continue them here.* Kepler installs GitKraken hooks to do this. One switch covers every agent that reports through hooks, and the help text names them. See [Agent Sessions](/kepler/agent-sessions#sessions-started-outside-kepler) | On |

If Kepler stops receiving hook events from a running agent session, every window shows *Agent sessions aren't reporting to Kepler*, with a **Repair** button. **Repair** reinstalls the reporting configuration. Restart any session that still doesn't report, since a running CLI doesn't reload its hooks. A window that only views another computer's sessions gets the warning without **Repair**, and is told to repair reporting from the computer running those sessions.

***

## Actions

*Start agent work without retyping prompts: save the ones you use often and run them on a task, issue or pull request.* An **Action** is an editable named prompt. The Actions page has two sections:

| Section | What it holds |
|---|---|
| **Preferred Actions** | *Pick which Action runs when you press the Action button on a task, issue or pull request.* One picker per kind of item: **Tasks**, **Issues**, **Pull requests I authored**, and **Pull requests from others**. Any slot can be **None** |
| **All Actions** | The shipped Actions under **Built in** and yours under **Custom**. Click a row to edit it. A row also offers **Restore default** where you have edited it, and **Delete** on a custom row |

The **All Actions** section header has **New Action**, which creates an Action, and **Restore all defaults**, which discards every edit. An Action you create or edit opens as a sub-page.

Kepler ships four default Actions:

- **Tasks** default to **Implement**.
- **Issues** default to **Plan**.
- Pull requests you authored default to **Address Feedback**.
- Pull requests from others default to **Review**.

For what the built-in Actions ask an agent to do, how the editor's **Title**, **Prompt**, **Applies to**, and **Agent** fields behave, and how an Action picks the agent it runs on, see [Actions](/kepler/actions).

***

## General

The General page has four sections: **Language**, **Windows**, **Default editor**, and **Keep agents running**.

### Language

**Language** has one setting:

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Language** | The display language for Kepler's interface | English | English, Español |

The choice also applies to native dialogs, not only the in-app interface.

### Windows

This section holds this machine's window preferences:

| Setting | What it controls | Default |
|---|---|---|
| **Restore windows on launch** | *Reopens the windows you had open, with their size, page and connection. Turn off to start with one window.* | On |
| **Always use the custom folder picker** | Local windows open your system's folder dialog, and windows connected to another machine use Kepler's own folder picker, which can browse that machine. Turn this on to use Kepler's picker in every window | Off |

Kepler reads **Restore windows on launch** during cold start, so a change takes effect on the next launch.

### Default editor

**Default editor** has one setting:

| Setting | What it controls | Default |
|---|---|---|
| **Open files and folders in** | The app that **Open in** and **⌘ ⇧**-click (**Ctrl + Shift**-click on Windows and Linux) on a file link use. The options are **Last used app**, each editor Kepler finds on this machine, and your system's default app | Last used app |

With your system's default app, files open without line numbers, folders open in Finder, Explorer, or your file manager, and programs open in your last used editor. If no editor can be opened from the window you're in, the setting reads *No editors can be opened from this window*.

### Keep agents running

This section keeps agent work alive when the machine would otherwise stop it. It applies to the machine the agents run on, which on a remote connection is that machine:

| Setting | What it controls | Default |
|---|---|---|
| **Keep this machine awake while agents work** | Blocks sleep and standby while an agent session is starting, running, or waiting for your input, and while Remote Access is on, except while it's waiting to reconnect, because sleeping would drop the connection. The screen can still turn off | On |
| **Keep agents and terminals running across restarts and updates** | *Agent sessions and terminals stay alive while Kepler restarts or updates, and reconnect afterwards. Experimental.* | On |

Kepler holds the machine awake through the platform's own mechanism: `caffeinate` on macOS, an execution-state assertion on Windows, and `systemd-inhibit` on Linux. Where that isn't possible, the setting says so under the switch. For example, it reads *Can't stay awake: there is no sleep-blocking mechanism available on this platform.* On Linux, it can say that the system's polkit policy is refusing the request, with a rule an administrator can install. The setting counts Claude Code sessions detected outside Kepler alongside Kepler's own. Kepler releases the machine as soon as the last such session settles.

**Keep agents and terminals running across restarts and updates** applies from the next session you start. With it on, a ready update's popover says *Running agents and open terminals keep going through the restart.* On a build that doesn't include the runtime it needs, the switch shows off, is disabled, and says so: *This build can't keep agents running across restarts.*

***

## Notifications

*Choose how Kepler tells you what your agents are doing. Desktop notifications show while Kepler is in the background, In Kepler alerts while you're using it. Sessions started outside Kepler notify only once they're on a task.*

The Notifications page has one section, **What to notify you about**. Its settings are saved on this machine.

### What to notify you about

The section is a grid. Each row is an event, and each column is a place Kepler can notify you: **Desktop** or **In Kepler**. The following table lists the events and their defaults in the desktop app:

| Event | When it fires | Desktop | In Kepler |
|---|---|---|---|
| **Replies** | *An agent finished replying and it's your turn.* | Off | Off |
| **Questions** | *An agent asks you something and waits for your answer.* | On | On |
| **Permission requests** | *An agent wants permission to do something.* | On | On |
| **Approval requests** | *An agent asks to do something in Kepler only you can approve, like deleting a worktree or rewriting a branch.* See [Approvals](#approvals) | On | On |
| **Errors** | *A session stops because something went wrong.* | On | On |

In a browser connected to Kepler, every **Desktop** box starts off. **Replies** stays off on the desktop unless you turned on system notifications in an earlier version of Kepler. Until you set **Approval requests** yourself, it follows **Permission requests**. When you turn on the first **Desktop** box, Kepler sends a sample notification so your OS asks for permission.

After your first session starts, the desktop app sends one notification to say *Notifications are on*: *Kepler will notify you here when an agent needs you. Change this in Settings › Notifications.* Clicking it opens this page. Kepler skips it if every **Desktop** box is off.

Two more settings sit under the grid:

| Setting | What it controls | Default |
|---|---|---|
| **Play a sound with desktop notifications** | Whether a desktop notification makes the OS notification sound | On |
| **Notify even for the task you're looking at** | *Otherwise Kepler stays quiet about the task open in the window you're using.* | Off |

To silence desktop notifications from one remote machine only, use **Mute notifications from {host}** on that machine in [Remote environments](#remote-environments).

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-settings-notifications-01-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-settings-notifications-01-01-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Notifications, What to notify you about, at the desktop app's defaults: a grid of Replies, Questions, Permission requests, Approval requests and Errors against Desktop and In Kepler, with every box ticked except both Replies boxes; below it Play a sound with desktop notifications is ticked and Notify even for the task you're looking at is not.">
  </a>
  <figcaption style="text-align:center; color:#888">What to notify you about, at the desktop app's defaults.</figcaption>
</figure>

***

## Appearance

The Appearance page has five sections: **Theme**, **Chat**, **Terminal**, **Code**, and **Diff view**. Its settings are saved on this machine.

### Theme

The **Theme** section has two parts: **Appearance**, which picks whether Kepler looks light or dark, and **Theme**, which picks the colors for each. Themes color the whole app, including code views, diffs, syntax, chat code blocks, and terminals.

**Appearance** has three options:

| Option | What it does |
|---|---|
| **System** | *Follows your system.* Kepler uses your dark theme when your OS is dark and your light theme when it's light, and switches when the OS does. **The default** |
| **Light** | *Always uses a light theme* |
| **Dark** | *Always uses a dark theme* |

Under **Theme**, each theme is a tile. The **Kepler** group holds the built-in themes:

- **Kepler**, which has a dark and a light version. It's the theme a fresh install uses for both.
- **Midnight**, a near-black theme that has only a dark version.

How you pick a tile depends on **Appearance**:

- On **System**, each tile has a moon and a sun. Click the moon to *Use {name} when your system is dark*, or the sun to *Use {name} when your system is light*. Click the tile itself to *Use {name} for both dark and light*.
- On **Light** or **Dark**, click a tile to use it for that appearance.

The tile in use reads **In use now**. If you used **Midnight** in an earlier version of Kepler, Kepler switches **Appearance** to **Dark** and keeps **Midnight** as your dark theme.

<figure style="text-align:center">
  <a href="/wp-content/uploads/appearance-theme-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/appearance-theme-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Theme section of Settings › Appearance at its defaults: Appearance set to System (Follows your system), and under Theme the Kepler tile in use, its preview split between dark and light with a moon and a sun under it, Midnight with a moon, and Your themes with Browse gallery and Create a theme.">
  </a>
  <figcaption style="text-align:center; color:#888">Appearance and Theme, at their defaults.</figcaption>
</figure>

Terminals follow the theme too. A terminal program that asks, such as an agent's own command-line app, is told the terminal's background color as it starts, so it draws a palette that suits the theme you're on. One that asks to follow theme changes is redrawn when you switch, while it runs.

#### Your themes

**Your themes** lists the themes you've added, with two more tiles, **Browse gallery** and **Create a theme**. **Open themes folder**, beside the heading, opens the folder they live in, `~/.kepler/themes`.

A theme file is a `.json` or `.jsonc` file, so comments are allowed. One file can hold a family of up to 8 themes, such as a dark and a light version. Each theme has an id and a name, and `extends` one of Kepler's base themes, `midnight`, `dark`, or `light`. It then overrides that base's colors, and can add code colors and a `terminal` block. The `terminal` block sets the terminal's background, foreground, cursor, selection, and 16 ANSI colors. Kepler reads up to 64 theme files and reloads a file each time you save it.

A tile whose file Kepler can't fully read shows **Has problems** or **Has warnings**. Click the badge to see what's wrong. A file that isn't valid JSON shows *Line {line}, column {column}: {message}*; a problem with a theme's values names the setting it's in, such as *themes.1.extends*. Below the list, **Create a task to fix it** hands the file to an agent, and in the desktop app **Open file** opens it in your editor, at the error's line when there is one. *Changes apply when you save.* A file with warnings still works. A theme that has errors is left out, and the other themes in its file still load. A tile's **More actions for {name}** menu has **Show in folder** and **Move to Trash** (**Move to Recycle Bin** on Windows).

<figure style="text-align:center">
  <a href="/wp-content/uploads/theme-problems-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/theme-problems-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Your themes in Settings › Appearance with harbor.jsonc's problem badge open: Unable to load 1 theme from harbor.jsonc, because harbor-light has errors that must be fixed while the other themes in the file are not affected. It lists themes.1.extends: Invalid option and Unknown key &quot;accent&quot; was ignored, above Create a task to fix it.">
  </a>
  <figcaption style="text-align:center; color:#888">A theme file's problems, each named by the setting it's in.</figcaption>
</figure>

#### Theme gallery

**Browse gallery** opens the **Theme gallery**: *Themes from the community, each checked for contrast. Try one on Kepler before you install it.* The gallery needs an internet connection. It has the following controls:

- **Search themes**, which matches a theme's name, author, tags, or description.
- **Show**, which filters to **All**, **Dark**, or **Light** themes.
- **Sort:**, with **Featured**, **Newest**, or **Name**.

Click a theme to see its details card, drawn in the theme's own colors. The card shows its author, its dark and light variants, **Version**, **License**, and **Updated**, and any contrast warnings in your version of Kepler. Then choose one of the following:

- **Install** adds the theme to **Your themes** without changing the theme on screen. The button then reads **Use**, or **Use for dark and light** for a theme with both.
- **Try it** closes the gallery and paints the whole window in the theme, so you can open a diff or a terminal to judge it. A bar at the bottom reads **Trying {name}**, with **Use {name}** and **Done**, which returns you to the gallery.

If a theme you already have uses the same id, Kepler asks before it replaces that file, and moves the old file to the Trash. A gallery theme you installed and haven't edited offers **Update to {version}** on its tile when a newer version is published. The gallery's themes come from `gitkraken/kepler-themes` on GitHub, where you can also publish your own.

<figure style="text-align:center">
  <a href="/wp-content/uploads/theme-gallery-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/theme-gallery-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Theme gallery dialog: Search by name, author or color, the All / Dark / Light filter, Sort: Featured and 5 themes, and tiles for Amethyst, Blue Is the New Green, Third Impact, Quiet and Kepler Sky with their authors and a moon or sun for each variant. The selected Amethyst's details card shows Amethyst Dark by Eric Amodio with its description, Version, License and Updated, above Install and Try it.">
  </a>
  <figcaption style="text-align:center; color:#888">The Theme gallery, with one theme's details open.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/theme-gallery-try-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/theme-gallery-try-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Settings › Appearance painted in the Amethyst theme while trying it from the gallery, with the preview bar at the bottom: Trying Amethyst Dark, a Dark / Light switch, Use Amethyst and Done.">
  </a>
  <figcaption style="text-align:center; color:#888">Trying a gallery theme on the whole window before you use it.</figcaption>
</figure>

#### Create a theme

**Create a theme** opens the new task launcher with a prompt already written for an agent, ending in *The theme I want:* for you to describe it. The agent reads and saves themes through Kepler's `theme_get` and `theme_save` tools, so it doesn't need the themes folder attached. Before `theme_save` saves a theme, it checks the file's format and that its colors reach the minimum contrast Kepler requires, and reports any problem back to the agent. **Create a task to fix it**, on a broken theme file, starts the same kind of task with that file's problems listed.

<figure style="text-align:center">
  <a href="/wp-content/uploads/create-a-theme-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/create-a-theme-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The New task launcher opened from Create a theme, its prompt asking the agent to read theme_get, check a draft with theme_save using dryRun, then save it, and ending in The theme I want. Add issue, Add PR and Add context sit above the prompt, and the agent picker, Start and Add repo or folder below it.">
  </a>
  <figcaption style="text-align:center; color:#888">The launcher that Create a theme opens.</figcaption>
</figure>

#### Themes in a remote window

Themes belong to this computer, as your choice of theme does. Every window, including one connected to a remote environment, lists and installs themes in this computer's themes folder and gallery. In a window connected to another machine, the picker adds an **On {host}** group with that machine's themes that this computer doesn't have. Each one offers **Install {name} on this computer**, or **Update {name} from {host}** for a copy you installed from it earlier.

### Chat

This section sets how a session's conversation scrolls and how wide it grows:

| Setting | What it controls | Default |
|---|---|---|
| **Chat auto-scroll** | **Auto-scroll to the end** *keeps the newest output in view. Scroll up to stop.* **Stay on my message** *keeps your message in view. The transcript doesn't scroll on its own.* | Auto-scroll to the end |
| **Conversation width** | *How wide the conversation grows in a wide pane. The message box keeps its width.* **Narrow**, **Wide**, or **Full width** | Narrow |
| **Remember scroll position** | *Return to where you left off when you come back to a session.* | On |

Neither scrolling mode fights you: once you scroll up, the transcript stays where you put it. The conversation stays centered at every width, and an agent's answers span its full width.

<figure style="text-align:center">
  <a href="/wp-content/uploads/appearance-chat-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/appearance-chat-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Chat section of Settings › Appearance: Auto-scroll to the end, Conversation width with Narrow selected beside Wide and Full width, and Remember scroll position ticked.">
  </a>
  <figcaption style="text-align:center; color:#888">The Chat settings, at their defaults.</figcaption>
</figure>

### Terminal

This section controls Kepler's embedded terminals:

| Setting | What it controls | Default |
|---|---|---|
| **Font family** | *Separate fonts with commas. The terminal uses the first one installed on this machine.* | Empty, which falls back to your platform's monospace stack |
| **Font size** | Terminal font size in pixels. Values outside 8–32 are clamped | 13 |
| **Line height** | Vertical spacing between lines, to one decimal place. Values outside 1–2 are clamped | 1.2 |
| **Show the message box under terminal sessions** | *Adds Kepler's message box under an agent's terminal, for attachments and voice. You can also switch it from the terminal's status bar.* | Off |

The greyed text in the **Font family** field (`Fira Code, JetBrains Mono, Menlo`) is an example of the format, not the value in effect. If you name a font Kepler can't find on this machine, the field says so and keeps your text. The terminal falls through to the next name in your list. **Font family** and **Font size** save when you press **Enter** or **Escape**, or leave the field, and show their save status.

#### Embedded terminals

Kepler scopes its terminals to a worktree. Opening one starts a shell in that worktree's folder, so you don't need to `cd` into it, and the shell sources your profile the same way an interactive login shell would. Use **⌘ J** to show and hide the terminal panel, **New terminal** to open another, and **Close terminal** to end one.

Terminals are for the work that sits alongside an agent session: running tests while the agent writes code, checking Git state, or reproducing something the session didn't surface. A terminal starts in one worktree and stays there, so work that spans several repositories is usually easier in a standalone terminal.

### Code

**Code** has one setting:

| Setting | What it controls | Default |
|---|---|---|
| **Font size** | *Size of text in diffs and file views.* A value below 10 or above 24 is clamped, and the field says the size can be 10 to 24 | 13 |

### Diff view

**Diff view** has one setting:

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Diff view** | The layout diffs open in | Stacked | Stacked, Split |

This setting is what the layout starts on. A per-diff **Stacked** / **Split** toggle also sits on the Changes overlay's viewer header, so you can switch a single diff without changing the default. See [Review changes](/kepler/review-changes).

***

## Voice input

*Talk to your agents instead of typing. Speech is transcribed on this machine and never leaves it.* The Voice input page has four sections: **Voice input**, **Transcription engine**, **When you stop talking**, and **Learned words**. Its settings are saved on this machine.

### Voice input

The first section has one switch, **Use voice input in the chat prompt**, which shows the microphone in the chat prompt. *Turn this off to pause voice input. The downloaded models stay on this computer.* Installing a model turns it on.

### Transcription engine

*Every engine runs on this computer and nothing you say leaves it. Qwen3-ASR gives better results than Whisper: it reads what you are writing, so it gets developer terms like Jira, rebase or pull request right far more often.* The section offers three engines:

| Engine | What it's best at |
|---|---|
| **Qwen3-ASR 1.7B** | *The most accurate, especially with developer terms and mixed languages. Needs a recent graphics card.* |
| **Qwen3-ASR 0.6B** | *Better than Whisper with technical terms, and lighter on memory. For graphics cards with less memory.* |
| **Whisper** | *Works on any machine, including without a compatible graphics card. Less accurate with technical terms.* |

Both Qwen3-ASR engines need a graphics card with WebGPU. On a new device, Kepler selects the Qwen3-ASR size that suits its graphics card and marks it **Recommended**. It selects Whisper instead when the machine has no WebGPU, or when a Whisper model is already installed. Each card shows its approximate download size. **Download and set up ({size})** installs a Qwen3-ASR model, and the card then reads *Ready on this computer.* Until the engine you selected is downloaded, dictation keeps using one that is. **Remove Qwen3-ASR models** deletes every downloaded Qwen3-ASR model after a confirmation. If you use Whisper, a one-time card suggests **Switch to Qwen3-ASR ({size})**, with **Not now**.

When a newer version of an installed Qwen3-ASR model ships, the card says *A newer version of this model is available. Dictation keeps using the installed one until you update.*, with **Update ({size})**. Kepler also tells you once, in a notification with **Update**.

With a Qwen3-ASR engine, **Dictation language** sets *The language you speak.* **Auto-detect**, the default, picks among your system's preferred languages and the app language, or among all languages when those name fewer than two. Over time it leans toward the languages this device has reliably dictated in. Choose a language to always dictate in it. Whisper ignores this setting.

#### Whisper

With **Whisper** selected, the section continues as a guided sequence. It shows one step at a time, and each step appears only once it can do something:

| Step | What it is |
|---|---|
| **Set up voice input** | *Takes a minute: Kepler checks what this machine can run, then downloads a model.* **Get started** begins setup |
| Hardware check | A one-time measurement of how fast this machine transcribes: *Checking what this machine can run…* It runs once. Later quality changes skip it |
| **Choose transcription quality** | Picks a model, with the check's recommendation marked **Suggested**. **Download and set up** installs it |
| Ready | The installed model and its size on disk, with **Change quality**, **Remove Whisper**, and **Technical details** |

Whisper offers four quality levels:

| Option | What it's best at |
|---|---|
| **Fast** | Short prompts in a quiet room, transcribed almost instantly on any machine. The best place to start |
| **Balanced** | Longer sentences and technical words, still quick on most machines |
| **Accurate** | Accents, names, and background noise. Expect a short pause after speaking on machines without a modern graphics card |
| **Most accurate** | The best quality available, including for languages other than English. Worth it on Apple Silicon or a recent graphics card, and slow on anything older |

Each option shows its approximate download size, calculated for the runtime your hardware check measured, so the number you read before installing is the one you download. Downloads continue if you leave the page, and Kepler notifies you when the model is ready.

Once a Whisper model is installed, these controls manage it:

| Control | What it does |
|---|---|
| **Change quality** | Reopens the quality picker |
| **Remove Whisper** | Removes the Whisper model and frees up its local storage. If Whisper is what dictates, the chat microphone turns off |
| **Technical details** | Shows the model's revision, and the backend and data type it runs on |

### When you stop talking

This section appears once a model is installed. It chooses what happens when you stop recording:

| Option | What it does |
|---|---|
| **Insert the text so you can edit it** | Puts the transcript in the prompt for you to review. The default |
| **Send the prompt** | Sends the prompt automatically |
| **Keep listening, transcribing each phrase as you pause** | Keeps the microphone open and transcribes each phrase as you pause |

### Learned words

*Qwen3-ASR learns the spelling of words you fix in dictated text before sending, one word at a time. A word fixed in two sends is suggested, and used once you approve it. Only the words are stored, on this device only, and they are kept after sign-out.*

When a fix becomes a suggestion, a notification says *A dictated word fix is ready to review*, with **Review**, which opens this section. The section has two lists:

- **Suggested words**: *Fixes you made in two sends. Dictation uses a word only after you approve it.* Each word reads **Heard as {heard}**, with **Approve** and **Dismiss**. Kepler never suggests a dismissed fix again.
- **Learned words**: the words dictation uses, each marked **In use** or **Added by you**, with **Remove {term}**. While Qwen3-ASR dictates, **Add a word** adds one yourself.

**Forget learned words** removes every word Qwen3-ASR learned or suggested, and every word you added, on this device, after a confirmation.

Kepler downloads each model from the internet once. Transcription then runs entirely on your device, and your audio is never uploaded. See [Voice Input](/kepler/voice-input).

***

## Keyboard shortcuts

*These shortcuts can't be changed yet.* The Keyboard shortcuts page lists Kepler's shortcuts in six sections: **General**, **Navigation**, **Dashboard**, **Task page**, **Chat**, and **Changes and code views**. Kepler also shows each shortcut in the menu items and button tooltips it belongs to. A few tab shortcuts that Settings doesn't list, such as reopening a closed tab and jumping to a tab by position, are in [Task View](/kepler/task-view#keyboard).

Mac symbols are shown first. On Windows and Linux, **⌘** is **Ctrl** and **⌥** is **Alt**, and **⌃** is **Ctrl** on every platform.

### General

The **General** group holds app-wide shortcuts:

| Action | Mac | Windows / Linux |
|---|---|---|
| Open settings | ⌘ , | Ctrl + , |
| Toggle Ask Kepler chat | ⌘ L | Ctrl + L |
| Toggle Ask Kepler terminal | ⌃ ` | Ctrl + ` |
| New task | ⌘ N | Ctrl + N |
| Open quick launcher (global) | ⇧ ⌥ N | Shift + Alt + N |
| New window | ⌘ ⇧ N | Ctrl + Shift + N |
| Quit | None | Ctrl + Q |
| Zoom in | ⌘ = | Ctrl + = |
| Zoom out | ⌘ – | Ctrl + – |
| Reset zoom | ⌘ 0 | Ctrl + 0 |
| Copy the selection or the focused item | ⌘ C | Ctrl + C |
| Close window | ⌘ ⇧ W | Ctrl + Shift + W |
| New session | ⌘ T | Ctrl + T |
| Rename task | F2 | F2 |
| Manage remote environments | ⌘ ⇧ R | Ctrl + Shift + R |
| Open file | ⌘ O | Ctrl + O |
| Go to file | ⌘ P | Ctrl + P |
| Dismiss / Cancel | Escape | Escape |
| Back | ⌘ [ | Alt + ← |
| Forward | ⌘ ] | Alt + → |

### Navigation

The **Navigation** group moves you between tabs and regions:

| Action | Mac | Windows / Linux |
|---|---|---|
| Previous tab | ⌘ ⇧ [ | Ctrl + Shift + [ or Ctrl + PageUp |
| Next tab | ⌘ ⇧ ] | Ctrl + Shift + ] or Ctrl + PageDown |
| Move tab left | ⌘ ⌥ [ | Ctrl + Alt + [ or Ctrl + Shift + PageUp |
| Move tab right | ⌘ ⌥ ] | Ctrl + Alt + ] or Ctrl + Shift + PageDown |
| Close tab or panel | ⌘ W | Ctrl + W or Ctrl + F4 |
| Toggle terminal | ⌘ J | Ctrl + J |
| Next region | F6 | F6 |
| Previous region | ⇧ F6 | Shift + F6 |

### Dashboard

The **Dashboard** group works on the Dashboard's tasks and detail panels:

| Action | Mac | Windows / Linux |
|---|---|---|
| Move panel left | ⌘ ⌥ ⇧ ← | Ctrl + Alt + Shift + ← |
| Move panel right | ⌘ ⌥ ⇧ → | Ctrl + Alt + Shift + → |
| Move panel up | ⌘ ⌥ ⇧ ↑ | Ctrl + Alt + Shift + ↑ |
| Move panel down | ⌘ ⌥ ⇧ ↓ | Ctrl + Alt + Shift + ↓ |
| Move task to the previous Progress stage | ⌘ ⇧ ← | Ctrl + Shift + ← |
| Move task to the next Progress stage | ⌘ ⇧ → | Ctrl + Shift + → |
| Focus detail panel 1–8 | ⌘ 1–8 | Ctrl + 1–8 |
| Focus last detail panel | ⌘ 9 | Ctrl + 9 |
| Switch detail panels | ⌃ Tab | Ctrl + Tab |
| Switch detail panels, oldest first | ⌃ ⇧ Tab | Ctrl + Shift + Tab |
| Maximize detail panel | ⌘ ⇧ M | Ctrl + Shift + M |
| Maximize panel terminals | ⌘ ⇧ J | Ctrl + Shift + J |
| Show or hide changes in detail panel | ⌘ ⇧ G | Ctrl + Shift + G |
| Switch detail panels between columns and grid | ⌘ ⇧ L | Ctrl + Shift + L |
| Show or hide resources in detail panel | ⌘ ⇧ E | Ctrl + Shift + E |
| Find in dashboard | ⌘ F | Ctrl + F |

The earlier **Move panel left** and **Move panel right** keys, **⌘ ⌥ ←** and **⌘ ⌥ →**, still work but aren't listed.

### Task page

The **Task page** group works on a task's page:

| Action | Mac | Windows / Linux |
|---|---|---|
| Focus chat | ⌘ 1 | Ctrl + 1 |
| Focus changes | ⌘ 2 | Ctrl + 2 |
| Focus resources | ⌘ 3 | Ctrl + 3 |
| Switch sessions | ⌃ Tab | Ctrl + Tab |
| Switch sessions, oldest first | ⌃ ⇧ Tab | Ctrl + Shift + Tab |
| Maximize terminal drawer | ⌘ ⇧ J | Ctrl + Shift + J |

### Chat

The **Chat** group works in a session's conversation:

| Action | Mac | Windows / Linux |
|---|---|---|
| Find in conversation | ⌘ F | Ctrl + F |
| Previous message | ⌘ ⌥ ↑ | Ctrl + Alt + ↑ |
| Next message | ⌘ ⌥ ↓ | Ctrl + Alt + ↓ |
| Interrupt & send | ⌘ ⇧ ⏎ | Ctrl + Shift + ⏎ |

### Changes and code views

This section has two lists. The **Changes** list works in the Changes view:

| Action | Mac | Windows / Linux |
|---|---|---|
| Filter changed files | ⌘ P | Ctrl + P |
| Previous file | ⌥ ↑ | Alt + ↑ |
| Next file | ⌥ ↓ | Alt + ↓ |
| Next change | F7 | F7 |
| Previous change | ⇧ F7 | Shift + F7 |
| Show or hide changes panel | ⌘ B | Ctrl + B |
| Open all changes | ⌘ ⇧ A | Ctrl + Shift + A |
| Comment on selection | ⌘ ⇧ C | Ctrl + Shift + C |

The **Code views** list works in any code view, such as a diff or a file you've opened:

| Action | Mac | Windows / Linux |
|---|---|---|
| Find in file or diff | ⌘ F | Ctrl + F |
| Next match | F3 or ⌘ G | F3 |
| Previous match | ⇧ F3 or ⌘ ⇧ G | Shift + F3 |
| Match case | ⌘ ⌥ C | Alt + C |
| Match whole word | ⌘ ⌥ W | Alt + W |
| Use regular expression | ⌘ ⌥ R | Alt + R |

### Shortcuts that depend on where you are

Some keys do different things depending on where you are:

- **⌘ 1**, **⌘ 2**, and **⌘ 3** focus a detail panel on the Dashboard but a column on the task page.
- **⌃ Tab** switches detail panels on the Dashboard and sessions on the task page.
- **⌘ ⇧ J** maximizes the panel's terminals on the Dashboard and the terminal drawer on the task page.
- **⌘ P** filters changed files in the Changes view and opens **Go to file** elsewhere.
- **⌘ F** finds in the Dashboard from its list or header, finds in a file or diff in a code view, and finds in the conversation elsewhere.
- **⌘ ⇧ G** shows or hides changes in a Dashboard detail panel, and, on macOS, moves to the previous match in a code view.
- **⌘ C** copies what a focused row, chip, or link names, such as a task's Kepler link, a pull request or issue link, a file path, or a commit hash, without opening a menu. In a text field, the message box, a terminal, or a text selection, it copies as usual.

Kepler registers **Open quick launcher** with the OS, so it works while Kepler is in the background. Its row carries a **Global** badge. **Quit**, **Ctrl + F4**, and the **PageUp** / **PageDown** tab keys are Windows and Linux shortcuts only. Kepler hides those rows on macOS, which quits through the native **⌘ Q** menu role. **Close tab or panel** works only in the desktop app.

On Windows and Linux, a focused terminal keeps **Ctrl + W** and **Ctrl + L** for the shell. **Ctrl + `** always toggles the Ask Kepler terminal, even from a terminal.

**Back** and **Forward** are split by platform on purpose. **Alt + ←** is the Windows and Linux convention but moves by word on macOS, and **⌘ [** is the macOS convention (Safari, Finder) but not the Windows one. Holding either walks the history.

**Send feedback**, **Show release notes**, **Show About**, **Check for updates**, and **Clean up worktrees** have no default key, so they don't appear in this list. Reach the first four from the app menu.

***

## Remote environments

*Run your agents on another machine, like a dev server or cloud VM, while you work from here. Kepler installs itself over SSH, so there's nothing to set up on that machine first.* On Windows, a WSL distro works too, and needs nothing extra.

**⌘ ⇧ R** opens this page from anywhere, and so does **Manage remote environments…** in the remote chip's popover. The saved machine list lives on this computer, whichever machine a window is connected to.

The Remote environments page has three sections:

| Section | What it holds |
|---|---|
| **Your machines** | Your saved machines, each row showing whether it's connected and how many windows have it open. **Connect** opens it here, and the second button opens it in a new window. **Add machine** adds one by hand. On Windows, **Machine type** chooses **SSH** or **WSL**. A WSL machine takes a **Distro** and an optional **Name** |
| **Found on this machine** | *Machines from your SSH config and WSL that you haven't added yet.* Each has **Add**, or **Hide** to tuck it under **Show hidden ({count})**. On a plan without remote environments, **Add** reads **Try free and add** where a trial is open, or **Upgrade to add**, which opens the plan page and saves nothing. Shown only while something is found |
| **Remote windows** | How a window connected to another machine loads its interface. See below |

Click a saved machine to open its page:

| Control | What it does |
|---|---|
| Name | Rename the machine. Renaming is only possible from a local window |
| **Latency**, **Live sessions** | The connection's current state |
| **Color** | Tints the machine's chip, its popover, and a connected window's top strip, so you can tell machines apart. **None** leaves it plain |
| **Mute notifications from {host}** | *Kepler won't show desktop notifications for sessions on {host}. Alerts still appear inside its windows.* |
| **Connection** | Edit the SSH or WSL address. A new SSH address asks you to trust its host key, with **Trust and save**. Disconnect first to edit a machine you're connected to |
| **Remove {name}…** | Deletes the saved machine |

In a window connected to an SSH machine, a **Ports** list shows the ports forwarded from that machine to this computer. Forward another by number, **Stop** one, or **Stop all** when more than one is forwarded.

A window connected to a machine lists the others read-only: *To add, edit, or remove machines, open Remote environments in a local window.* Use **Open in a local window** to do so.

If a window can't get back to its machine, it shows a full-screen recovery screen instead of opening this page. See [The recovery screen](/kepler/remote-environments#the-recovery-screen).

### Remote windows

The following setting is saved on this machine:

| Setting | What it controls | Default |
|---|---|---|
| **Use this app's interface in remote windows** | *Windows connected to another machine load their interface from this app instead of from that machine, so only your data crosses the connection. If that machine runs a different version of Kepler, its own interface is used.* Experimental. Desktop app only | On |

The setting applies the next time you connect to a machine with no other window open on it.

See [Remote environments](/kepler/remote-environments) for connecting, port forwarding, and how sessions behave on a machine.

***

## Remote Access

*Use this machine from any browser or your phone, through a secure GitKraken relay.* No open port and no tunnel to set up yourself. Remote Access requires a paid GitKraken plan and isn't available on the Community plan.

The page explains **How it works** in three steps:

1. Turn it on and name this machine.
2. Scan the QR code or open the link that appears here, on your phone or any browser.
3. Sign in with your GitKraken account, and this machine's tasks and sessions are there.

To turn it on, click **Turn on Remote Access**, then enter a name in **Name this machine**. A status badge shows its state: **Connecting…**, **Active**, **Reconnecting…**, **Waiting to reconnect**, **Error**, or **Inactive**. While it's on, the page shows a QR code (*Scan with your phone camera to open*) and **Copy URL**. *This machine stays awake while Remote Access is on.* links to [Keep agents running](#keep-agents-running) with **Change in General**.

Remote Access stays on until you turn it off, sign out, or another account signs in. If it loses the connection, Kepler retries quickly, then shows **Waiting to reconnect** with the reason, under **Unable to connect**. *Kepler retries every 5 minutes.* **Retry now** tries at once, and paired devices stay paired. Two cases name their own fix:

- *Waiting for a GitKraken sign-in. Remote Access connects as soon as one is available.*
- *Your account has reached its limit of machines with Remote Access on. Remove one you no longer use, then retry.*, with **Manage machines on gitkraken.dev**.

To turn it off, use the switch. Kepler asks **Turn off Remote Access?** first, because *Every paired device is disconnected.*

**Machines on your account**: *See every machine on your account with Remote Access on, and remove the ones you no longer use.* Its **Manage machines on gitkraken.dev** button shows even while Remote Access is off.

**Connected devices** lists each device that has connected, marking **This device** and when each was **Last seen**, with **Revoke** to disconnect one device and **Refresh** to reload the list. *Only you can connect, signed in to your GitKraken account. Turning Remote Access off disconnects every device, and you can revoke any single device under Connected devices.*

A pairing link works once and expires after 5 minutes. A spent one reads *This pairing link no longer works*, so open a new link from the computer running Kepler. See [Remote environments](/kepler/remote-environments) for prerequisites, pairing, and managing sessions from gitkraken.dev.

***

## Updates

The Updates page has one section, shown without a heading. It's about the app itself:

| Row | What it does |
|---|---|
| **Current version** | The installed version, with **Release notes** beside it to open what's new in that release |
| **Check for updates** | Checks for a newer release and downloads it in the background. Reads **Up to date** when there's nothing newer, and becomes **Check again** |
| Download progress | While a release downloads: **Downloading** with a percentage, how much has arrived out of the total and the speed (*{done} of {total} at {rate}/s*), and the time left (*About {count} min left*). A **Verifying** step follows before it can install |
| **New version** | Appears once a release is ready, with **Restart to update** beside it, and how many running agents a restart would stop |

A ready update also shows as one chip in the top bar, on every screen, whose popover reads **Update ready to install** and says what a restart does to running work. If agents are mid-tool-call when you restart, Kepler shows *Preparing to restart. Finishing {count} active tool calls…* and waits up to 2 minutes. **Restart now** skips the wait.

**Check for updates** in the app menu answers where you are rather than opening this page. The top bar shows **Checking…**, then **Up to date** or the download. On the welcome screen, the version in the corner is itself the check, and a failure there reads **Unable to check for updates** with **Try again**.

After an update, the release notes open on their own in Kepler, once any guided start has ended. A release can lead with a highlights card, *Three things in {version} to try first:*, and each item jumps to its part of the notes.

The update controls only appear in the desktop app. In a browser window connected to Kepler, this page shows nothing to update.

***

## Help

*Docs, tips and logs for when something goes wrong.* The Help page has two sections: **Help** and **Logs**.

### Help

This section links out to the docs and release notes, and replays any tip you dismissed:

| Control | What it does |
|---|---|
| **Kepler documentation** | *Guides, keyboard shortcuts, and agent setup.* **Open docs** opens the Kepler docs site in your browser |
| **Release notes** | *See what changed in each version.* **Show release notes** opens them in Kepler, starting with the release's highlights when it has them. See [Updates](#updates) |
| **Show tips and guides again** | A disclosure, closed by default: *Kepler points out a few controls the first time they matter. Show any of those tips again here.* |

Inside the disclosure, each tip has a row that reads **Seen and dismissed** or **Not shown yet**, with its own **Show again** button. A tip that was shown but never dismissed still reads **Not shown yet**. The tips are the following:

- Actions callout
- Todo pointer
- Task page callout
- Panel layout callout

**Reset all onboarding and show everything again**, at the foot of the disclosure, clears every element's dismissed state in one action rather than one row at a time.

### Logs

*To report a problem, save the logs and attach the file.* The following table lists the section's controls:

| Control | What it does |
|---|---|
| **Copy path** | Copies the current log's path to your clipboard |
| **Show in Finder** | Opens the log's folder in your file manager (**Show in Explorer** on Windows, **Show in file manager** on Linux). Hidden where the machine can't open one |
| **Save logs…** | Saves Kepler's logs as a single zip file |
| **Clear log…** | Deletes the current and rotated log files, after a confirmation |

In a window connected to a remote environment, these are that machine's logs: *These are the logs on {machine}.* Saving them from there includes this machine's logs too, and **Show this machine's logs** opens your local ones.

Without opening Settings, **Help → Show Logs in Finder** (**Show Logs in Explorer**, **Show Logs in File Manager**) in the app menu reveals this computer's log.

---
