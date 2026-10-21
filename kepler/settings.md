---
title: Settings
description: A reference for every setting in Kepler across the 15 Settings pages, plus folder locations, branch prefixes, the Variables menu, per-repository commands, worktree cleanup, MCP server defaults, notifications, and the keyboard shortcut list.
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
| **Agents** | Your agents, custom agents, MCP servers, agent tools, and usage limits |
| **Tasks** | How new tasks start, including the default agent, and how a task's page looks |
| **Repositories** | The repositories folder, your repos and folders, worktree cleanup, and Projects |
| **Integrations** | Issue tracker and Git host connections, and sessions started in your own terminal |
| **Actions** | Preferred Actions per item kind, and the Action list |
| **General** | Language, windows, and keeping agents running |
| **Notifications** | Which agent events notify you, on the desktop and in Kepler |
| **Appearance** | Theme, chat scrolling, terminal font, and diff layout |
| **Voice input** | On-device speech-to-text and its model |
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

If you leave a sub-page with unsaved changes, by pressing **Escape** or **Back**, Kepler asks before it discards anything:

- A form that can save asks **Save your changes?**, with **Cancel**, **Don't save**, and **Save**.
- A form that has nothing to save yet, such as a step-by-step add flow, asks **Discard your changes?**, with **Keep editing** and **Discard**.

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
| `/settings/agents` | `agents`, `custom-agents`, `mcp-servers`, `agent-git-tools`, `usage-limits` |
| `/settings/tasks` | `new-tasks`, `default-agent`, `task-page` |
| `/settings/repositories` | `repositories-root`, `repositories`, `worktrees`, `projects` |
| `/settings/integrations` | `provider-integrations`, `agent-options` |
| `/settings/actions` | `preferred-actions`, `action-list` |
| `/settings/general` | `language`, `windows`, `keep-running` |
| `/settings/notifications` | `system-notifications` |
| `/settings/appearance` | `appearance`, `transcript`, `terminal`, `diff-view` |
| `/settings/voice` | `voice`, `voice-dictation` |
| `/settings/keyboard-shortcuts` | `shortcuts-general`, `shortcuts-navigation`, `shortcuts-dashboard`, `shortcuts-task-page`, `shortcuts-chat`, `shortcuts-changes` |
| `/settings/remote-environments` | `remote-environments`, `found-machines`, `remote-windows` |
| `/settings/remote-access` | `remote-access` |
| `/settings/updates` | `updates` |
| `/settings/help` | `onboarding-help`, `logs` |

`default-agent` sits inside **New tasks** rather than being a section of its own. From the rail or search, `worktrees` opens the **Worktree cleanup** sub-page instead of scrolling to its row. Each agent also gets its own anchor on the Agents page, `agent-<agent-id>`, for example `agent-claude-code`.

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
| **GitKraken AI credits** | Your credit balance, with **Buy credits**. Shown only when there's a balance to show |

When a feature is locked on the organization you're acting as but included on another one you belong to, Kepler says so and offers the switch rather than sending you to a paywall: *{organization} ({plan}) already includes this.*, with **Switch to organization**.

A paywall also asks **Already upgraded?** with **Check again**, for a plan you've just changed. If nothing has changed, it says so briefly: *Still on {plan}*.

***

## Agents

*The coding agents that work on your tasks: install them, sign in, choose how you work with each, and give them more tools.* The page opens with a line that names your default agent, *New tasks use {agent}.*, and a **Change in Tasks** link to [Default agent](#default-agent).

The Agents page has five sections: **Your agents**, **Custom agents**, **MCP servers**, **Agent tools**, and **Usage limits**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-settings-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-settings-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Settings › Agents: the page description, New tasks use Claude Code with Change in Tasks, and Your agents with Update all and Re-scan above the Claude Code card, which shows its account (alex.lee@example.com, Acme, Default), New sessions start in set to Chat, Let artifact comments start turns, and a collapsed Program and data folder.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings → Agents.</figcaption>
</figure>

### Your agents

Kepler ships adapters for **Claude Code**, **Codex**, **GitHub Copilot**, **Cursor**, **Antigravity**, **OpenCode**, **Pi**, **Auggie**, and **Grok Build**. Settings lists the agents installed on this machine first, then the rest, each group in that order.

Two buttons sit in the section header: **Update all** runs each installed agent's own updater, and **Re-scan** re-detects the agent CLIs installed on this system. Run **Re-scan** after you install or remove an agent outside Kepler.

Each card's title line carries the agent's name and these controls:

| Control | What it does |
|---|---|
| Version | The installed version. **Not installed** when Kepler can't find the CLI. A warning-toned **Version unknown** means Kepler couldn't read it, which turns off features that depend on the version, such as sending a new session's first message automatically. Reinstalling or updating the agent usually fixes it |
| **Update** | Runs the agent's updater and streams its output. Shown when Kepler has an updater for that agent |
| **Install** | Runs an install method on your behalf and streams the output. Shown on a not-installed agent that has an installer for your OS. **Cancel** stops an install in progress: *Install cancelled: {name}* |
| **Enabled** | *Off keeps it installed but hidden when you start work.* |

The card body holds the rest:

| Control | What it does |
|---|---|
| **Accounts** | Runs multiple logins side by side, each with its own credentials and history but sharing your skills, agents, commands, and settings. **Add account** asks whether its conversations **Keep separate** or **Share with the CLI**. Each account row has a color picker that tints the agent icon wherever that account runs (the default account stays uncolored, so its picker shows the ⊘ **No color** mark), plus **Sign in** and an account menu with **Rename**, **Share history with the CLI**, **Sign in another way**, **Sign out**, and **Remove account**. Removing an account stops its running sessions and deletes the sessions stored only in it, unless you first **Move to CLI account**; see [Agent Sessions](/kepler/agent-sessions#several-accounts-for-one-agent). Available for Claude Code, Codex, GitHub Copilot, Auggie, and Grok Build |
| **Account** | On an agent with a single login: who is signed in, with **Sign in** or **Sign out**. Signing out deletes the stored credentials |
| **New sessions start in** | The default mode for new sessions. See below |
| **Let artifact comments start turns** | Claude Code only. See below |
| **Program and data folder** | A disclosure holding **Binary**, **Components**, and **Data folder** |

Under **Program and data folder**:

| Setting | What it controls | Default |
|---|---|---|
| **Binary** | The binary Kepler spawns. **Auto** resolves it the way your shell does (the first match on your `PATH`), so it matches `which`. Pick a specific install, or **Custom path…**, to override. **Re-scan** searches again | Auto |
| **Components** | Extra pieces an agent can need, such as its CLI for Terminal mode (*Needed for Terminal mode.*), each with **Install** or **Update to {version}** | None |
| **Data folder** | *Overrides the agent's default data and config folder.* | Empty, meaning the agent's own default |

**Codex runs your own CLI.** Kepler resolves and spawns the `codex` you have installed, like every other agent. Usage figures read the OAuth token from `~/.codex/auth.json`, or `CODEX_HOME/auth.json` when you have set a custom data folder.

**OpenCode v1 and v2 work side by side.** Its installers come in a v1 and a v2 flavor. Point **Binary** at whichever one you want Kepler to run. **Antigravity** runs in Chat through its ACP server, a separate component from its `agy` terminal CLI. See [Agent Integrations](/kepler/agent-integrations).

#### Default mode for new sessions

Every agent that can run both ways carries this setting:

| Setting | What it controls | Default |
|---|---|---|
| **New sessions start in** | **Chat**: *{agent} built into Kepler, with replies, diffs and plans you can read, review and search.* **Terminal**: *{agent}'s own command-line app, with its commands, shortcuts and settings, just as you use it today.* | Chat. Google Antigravity starts on Terminal, because its Chat server signs in separately |

The choice is saved per agent, so one agent can default to Terminal while another stays on Chat. The help text reads *You can pick the other one when you start a session.*: a new session can start in the other mode without changing the setting. A terminal-only agent shows **Terminal** with no switch. See [Agent Sessions](/kepler/agent-sessions#how-a-session-runs).

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

This setting is about the MCP clients on your machine. It differs from the workspace MCP server that Kepler attaches to every session it starts itself, which is always on and has no setting. That server gives the agent tools to:

- Read the task's shared context and resources, and read another session's transcript.
- Write, edit, and remove the task's notes.
- Attach and detach issue, pull request, and URL links, including a dev server the agent starts, and refresh the task's pull requests and issues.
- Set the task's Progress stage, or put it on hold.
- List the repositories and folders in your workspace.
- Create, attach, detach, or discard one of the task's worktrees.
- Find the workspace's tasks and sessions, archive and restore a task, and create a task with files attached.
- Start a session on a task with the agent it chooses, name it, rename it later, and send follow-ups to existing sessions.

See [Tasks and Resources](/kepler/tasks-and-resources) for the full list and which of them ask permission first.

### Agent tools

*Kepler's own tools your agents can call, starting with rebasing, merging and cleaning up commits.* The following table lists them:

| Setting | What it does | Default |
|---|---|---|
| **AI Sync** | *Lets agents rebase or merge your branch and resolve conflicts for you. Every change can be undone.* | Off |
| **AI Compose** | *Lets agents turn messy changes into clean, focused commits. Every change can be undone.* | Off |

**AI Sync** and **AI Compose** add their tools to the workspace MCP server. Both require a paid GitKraken subscription. On the Community plan, they show a lock: *Not available on the Community plan. Upgrade to unlock.* Turning either on confirms that *New agent sessions will pick up this change.* Sessions already running keep the tools they started with.

### Usage limits

Two settings handle your agent plans' usage limits:

| Setting | What it controls | Default |
|---|---|---|
| **Show plan usage for Claude Code, Codex and Augment** | *Kepler reads each agent's sign-in from this machine to show how much of your plan is left. Nothing is sent anywhere except to that agent's provider.* The readout says when it was last updated | Off |
| **Resume after the usage limit resets** | When a turn is cut off by your account usage limit and nothing is queued, Kepler queues a "continue" message that is sent shortly after the limit resets | Off |

***

## Tasks

*A task is one piece of work: its prompt, the agent sessions working on it, and the worktree or folder they work in. Set how new tasks start and how a task's page looks.*

The Tasks page has two sections: **New tasks** and **Task page**.

### New tasks

This section sets what Kepler preselects for every new task. Its values belong to the environment you're working on, so in a remote window they're that machine's.

#### Default agent

**Default agent** picks the agent, account, model, mode, and thinking effort that Kepler preselects for a new task. Its description reads *Used when Kepler has no earlier pick to go on, and whenever you choose Use default agent in the launcher.* The following table lists its controls:

| Control | What it does |
|---|---|
| **New tasks use** | Chooses the agent, and the account when that agent supports more than one |
| Options | Model, mode, and the agent's own configuration options. Available once an agent is picked |
| **Clear default** | Removes the saved default. Appears only once one is set |

Nothing is set out of the box, and the control is hidden entirely when no agent is installed. If the agent you saved is later uninstalled, the row warns you: *Your default agent, {name}, is no longer installed. Pick another.*

An [Action](/kepler/actions) inherits this configuration unless it names an agent of its own.

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

The prefix applies to **automatic** names only. A branch name you type is used verbatim, which is how a repository with an enforced `feat/` or `fix/` push rule still works. A prefix you type without a trailing separator gains a `/`, so typing `team` stores `team/`. A personal `ea-` style prefix is kept as the literal lead-in it is.

Each repository can override the prefix on its [Edit repo](#edit-a-repository) page under **Settings → Repositories**. If a repository already has a branch literally named after the prefix, Kepler says which one and points you there: *Can't be used in {repo}: it has a branch named {branch}. Set a different prefix for that repository under Repositories.*

#### Folder locations

Three paths tell Kepler where to put things. Two of them are on this page, and the third is on the Repositories page:

| Setting | Where it is | What it controls | Default |
|---|---|---|---|
| **Worktrees folder** | Tasks → New tasks | *Where Kepler creates the worktree for each new task.* | `~/kepler/worktrees` |
| **Tasks folder** | Tasks → New tasks | *Each task gets a folder here for its attachments and files.* | `~/kepler/tasks` |
| **Repositories folder** | [Repositories](#repositories-folder) | Where Kepler clones repositories, and where it looks for repositories to add | `~/kepler/repositories` |

All three are unset out of the box. Kepler computes a fallback under your home folder without writing it, so an untouched setting still reads as untouched.

Type a path directly, or use the folder button beside the field to browse. Edits save when you leave the field, so no separate Save button exists.

#### The Variables menu

A folder field that can contain a dynamic variable has a **Variables** menu beside it. Pick a variable and Kepler inserts it at the cursor. Kepler fills it in when it creates the folder, so one pattern covers every repository. Each field offers only the variables it can actually resolve:

| Field | Variables offered |
|---|---|
| **Worktrees folder** | `<REPOSITORY_PATH>` (*Main repo folder*), `<REPOSITORY_NAME>` (*Repo name*) |
| **Repositories folder** | `<REPOSITORY_NAME>` |
| **Tasks folder** | None |

For example, `<REPOSITORY_PATH>/.worktrees/<REPOSITORY_NAME>` nests each worktree inside the repository it belongs to. Kepler collapses any `..` segments you write.

**Tasks folder** takes no variables. A task folder has no repository behind it, so nothing would ever fill one in. Kepler refuses the value rather than storing a path that can't resolve: *Dynamic variables cannot be used here.*

Per-repository commands have a **Variables** menu of their own, with two more variables. See [Per-repository commands](#per-repository-commands).

<figure style="text-align:center">
  <a href="/wp-content/uploads/folder-fields-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/folder-fields-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The New tasks section of Settings › Tasks with the Variables menu open beside Worktrees folder, offering REPOSITORY_PATH and REPOSITORY_NAME; the Tasks folder field below has no Variables menu.">
  </a>
  <figcaption style="text-align:center; color:#888">The Worktrees and Tasks folder fields in Settings → Tasks, with the Variables menu open.</figcaption>
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

The Repositories page has four sections: **Repositories folder**, **Your repos and folders**, **Worktree cleanup**, and **Projects**.

### Repositories folder

The following setting tells Kepler where to clone repositories:

| Setting | What it controls | Default |
|---|---|---|
| **Repositories folder** | *Kepler adds the repos it finds in this folder. It only looks when you change the folder or scan, so a repo you remove won't come back.* | `~/kepler/repositories` |

**Scan for repositories**, beside the field, registers every repository it finds there. It reports **Added {count} repositories.** or **No new repositories found.** It runs only when you change the setting or press it, never on startup, so a repository you deliberately removed stays removed.

The field takes the `<REPOSITORY_NAME>` variable. See [The Variables menu](#the-variables-menu).

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

#### Edit a repository

Click a repository's row to open its **Edit repo** page. The page shows the repository's path, its remote, and its branches, and has these parts:

| Part | What it holds |
|---|---|
| **Name** | An alias Kepler shows wherever it names this repository. The field's placeholder is the folder name. Leave it empty to use the folder name. A repository you name this way keeps that name verbatim and stops competing with same-named folders for a disambiguating suffix |
| **Description** | Free text. Its placeholder reads *What this repo is for. Agents working in it read this.* Kepler appends it to the repository's line in the resource list it hands a session, so a full sentence is more useful here than a single label |
| **Branch prefix** | Overrides the prefix from **Settings → Tasks** for this repository alone. See below |
| **Commands** | Shell commands for this repository. See [Per-repository commands](#per-repository-commands) |
| **MCP servers** | *Extra tools your agents get in this repo, on top of their own lists. Changes here apply right away.* See [MCP Servers](/kepler/mcp-servers) |

**Name** and **Description** are optional. Kepler stores whitespace-only text as empty.

<figure style="text-align:center">
  <a href="/wp-content/uploads/edit-repo-dialog-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/edit-repo-dialog-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Edit repo sub-page for acme-web in Settings › Repositories: the breadcrumb back to Repositories, its path and branches, Name, Description, Branch prefix set to Default (kepler/), the Commands section with Add command and two saved commands, and the MCP servers section.">
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

Removing a repository deletes its sessions, terminals, and configured commands, and terminates any live agent and terminal sessions tied to it. Kepler confirms before it does.

#### Per-repository commands

*Run your dev server, tests or build from a task's worktree in one click. A command can also run when Kepler creates a new worktree, like installing dependencies.* Commands are shell commands scoped to one repository.

To add a command, click **Add command** in the **Commands** section of the Edit repo page. With no commands, the section reads *No commands yet.* and suggests examples. Each command row has three fields:

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

Drag a row by its handle to reorder it, or move it from the keyboard with **Alt + ↑** and **Alt + ↓**. Order sets the **Run** menu order and the order that commands set to run on worktree creation run in.

A row with a name but no command, or a command but no name, holds back **Save** with *Some commands are incomplete.* and takes you to the missing field. A row left completely empty is dropped on save, so an accidental **Add command** leaves no trace.

Commands flagged to run on worktree creation execute sequentially, in list order, and stop on the first failing command. Kepler skips the rest and reports them as skipped. Each one runs in the new worktree's folder through your login shell, so you don't need to `cd` into it, and tools configured in your shell profile (`nvm`, for instance) are available. Each has a ten-minute timeout.

A failed command does not undo the worktree. The worktree exists but may not be usable. To fix it:

1. Read the command output in the task.
2. Correct the command here.
3. Run it again from the **Run** menu.

To run a command from the task view, right-click a worktree row in the rail and use **Run command here**. It lists that repository's commands and runs the one you pick in that worktree, opening its terminal in place. A repository with none yet reads **No commands yet** and offers **Create command…**. A command that's running shows on the run button and its menus, where you can stop it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/repo-commands-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/repo-commands-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Commands section of the Edit repo page for acme-web: Add command, Install deps (pnpm install) with the Runs on creation chip, and Dev server open for editing with its Variables menu listing REPOSITORY_PATH, REPOSITORY_NAME, SOURCE_PATH and WORKTREE_PATH.">
  </a>
  <figcaption style="text-align:center; color:#888">A repository's Commands, with the Variables menu open.</figcaption>
</figure>

### Worktree cleanup

*Quickly find and delete unused worktrees to free up disk space.* On the Repositories page, this section is one row, **Find unused worktrees**. Click it to open the **Worktree cleanup** sub-page.

*The check finds worktrees whose work has landed or gone quiet, and deletes nothing on its own.* To start it, click **Check for unused worktrees**. The sub-page then lists your worktrees grouped by repository, with a summary such as *{count} worktrees in {count} repos. {count} look safe to delete.*

The following table lists the sub-page's controls:

| Control | What it does |
|---|---|
| **Show worktrees** | Filters the list: **Safe to delete ({count})**, **Idle ({count})**, or **All ({count})** |
| **Treat a worktree as idle after** *n* **days** | How many days without activity before a worktree counts as idle. Defaults to 14 |
| **Re-check** | Inspects the worktrees again for uncommitted or unpushed work |
| **Select all safe to delete** / **Select all idle** / **Select all** | Selects worktrees in the current view. **Clear** empties the selection |
| **Delete {count} worktrees** | Deletes the selected worktrees after a confirmation that lists anything that would be lost, with **Also delete the branches** |
| **Update** | Brings the selected worktrees up to date with their base. See [Update worktrees](#update-worktrees) |

Each worktree shows how long since it was touched, why it may be finished (**merged into {base}**, **upstream deleted**, **PR merged**, or **PR closed**), the tasks using it, and how far behind its base it is. A worktree counts as one of the following:

- **Safe to delete**: its branch is merged, its upstream is gone, or its PR is merged, and nothing is uncommitted, unpushed, or still in use.
- **Idle**: untouched for longer than the idle threshold. It may still hold uncommitted or unpushed work, so deleting it can lose something.

A lock Kepler itself left on a worktree, for a task this install knows or a task since deleted, is cleared and the worktree deleted. Kepler never deletes a repository's main checkout. It keeps any worktree that still has uncommitted or unpushed work, other tasks, running agent sessions, or a lock from another tool, and says why for each. Where forcing can help, the result offers **Force delete**, which discards the listed work and ends the agent sessions running there.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-worktree-cleanup-01-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-worktree-cleanup-01-v2@2x.png" class="help-center-img img-bordered" alt="The Worktree cleanup page after a check: 4 worktrees in 1 repo, 2 look safe to delete, with Idle after 14 days and Re-check. Show worktrees is set to Safe to delete, and the acme-web group lists kepler/old-banner and kepler/promo-page, both merged into main, untouched for weeks and tagged with their archived task, Spring sale banner, both selected. The selection bar reads 2 selected with Update, Delete 2 worktrees and Clear.">
  </a>
  <figcaption style="text-align:center; color:#888">The Worktree cleanup sub-page, after a check.</figcaption>
</figure>

#### Update worktrees

To bring several worktrees up to date with their base branch at once:

1. On the Worktree cleanup sub-page, select the worktrees.
2. Click **Update**. The **Update worktrees** dialog opens: *Each branch is brought up to date with its base. Nothing changes until you pick an action.*
3. Review the plan. Each worktree reads **Will update** with how many commits it's behind, **Up to date**, or **Skipped** with the reason, such as *an agent is working in it*, *uncommitted changes*, or *would conflict*.
4. Under **How to update**, choose **Rebase** or **Merge**.
5. Click **Update**, or **Update + Push** to also push each updated branch.

While the update runs, each row shows its status: **Waiting**, **Updating…**, **Updated**, **Up to date**, **Skipped**, **Conflict**, or **Failed**. When it finishes, you can undo one row with **Roll back**, or every row with **Roll back all**. If you didn't push during the update, **Push** and **Push all** push the updated branches.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-worktree-batch-update-01-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-worktree-batch-update-01-v2@2x.png" class="help-center-img img-bordered" alt="The Update worktrees dialog with How to update set to Rebase. It plans three worktrees: kepler/gift-card-ui is Up to date, kepler/old-banner Will update · 3 commits behind, and kepler/wishlist is Skipped · uncommitted changes. The footer reads 1 worktree to update beside Cancel and the Update button with its menu.">
  </a>
  <figcaption style="text-align:center; color:#888">The Update worktrees plan, before you pick an action.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-worktree-batch-update-02-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-worktree-batch-update-02-v2@2x.png" class="help-center-img img-bordered" alt="The finished update: Update finished, 1 updated, with Push all, Roll back all and Dismiss in its header, and kepler/old-banner marked Updated with Push and Roll back on its row.">
  </a>
  <figcaption style="text-align:center; color:#888">The finished update, with Roll back and Push on each row.</figcaption>
</figure>

### Projects

*Group repos that belong together under one name.* A **Project** groups repositories so they act as a unit, such as a frontend and a backend you change together. The following table lists the section's controls:

| Control | What it does |
|---|---|
| **Row** | Shows the project's name and its repository count. Click it to open the project's page |
| **New project** | Opens a page where you name a project and pick its repositories. **Add from folder** adds a repository without leaving the page |

A project's page also has **Delete project**. Deleting a project keeps its repositories in your repository list. With no projects, the section reads *No projects yet.*

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
| **Disconnect** | Disconnects the provider from GitKraken everywhere: every GitKraken product and service that uses this connection loses access too. Other accounts for that provider stay connected, and you can reconnect at any time |
| **Refresh** | Re-checks every provider's connection status. It's in the section header |

Providers connect through your GitKraken account, so the section asks you to sign in before it shows anything to manage.

When a provider has more than one account, an **Accounts** block lists them. **Set as primary** chooses which account Kepler acts as, and **Read from this account** chooses which one Kepler reads issues and pull requests from. They can be different accounts.

When an organization refuses a working connection (it blocks third-party OAuth apps, or hasn't approved GitKraken), the row names the organization and says its items aren't shown, with a link to fix it, such as **Request access on GitHub**.

Under the list, *Agents can use these through the GitKraken MCP server.* links to [MCP servers](#mcp-servers).

For per-provider setup, see [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

### Your terminal

The following setting covers agent sessions you start outside Kepler:

| Setting | What it controls | Default |
|---|---|---|
| **Show sessions started outside Kepler** | *Lists sessions you start in your own terminal, so you can follow and continue them here.* Kepler installs GitKraken hooks to do this. One switch covers every agent that reports through hooks, and the help text names them. See [Agent Sessions](/kepler/agent-sessions#sessions-started-outside-kepler) | On |

If Kepler stops receiving hook events from a running Claude session, every window shows *Claude sessions aren't reporting to Kepler* with a **Repair** button. **Repair** reinstalls the hooks. Restart any Claude session that still isn't responding, since a running CLI doesn't reload its hooks.

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

The General page has three sections: **Language**, **Windows**, and **Keep agents running**.

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

### Keep agents running

This section keeps agent work alive when the machine would otherwise stop it. It applies to the machine the agents run on, which on a remote connection is that machine:

| Setting | What it controls | Default |
|---|---|---|
| **Keep this machine awake while agents work** | Blocks sleep and standby while an agent session is starting, running, or waiting for your input, and while Remote Access is on, because sleeping would drop the connection. The screen can still turn off | On |
| **Keep agents and terminals running across restarts and updates** | *Agent sessions and terminals stay alive while Kepler restarts or updates, and reconnect afterwards. Experimental.* | Off |

Kepler holds the machine awake through the platform's own mechanism: `caffeinate` on macOS, an execution-state assertion on Windows, and `systemd-inhibit` on Linux. Where that isn't possible, the setting says so under the switch. For example, it reads *Can't stay awake: there is no sleep-blocking mechanism available on this platform.* On Linux, it can say that the system's polkit policy is refusing the request, with a rule an administrator can install. The setting counts Claude Code sessions detected outside Kepler alongside Kepler's own. Kepler releases the machine as soon as the last such session settles.

**Keep agents and terminals running across restarts and updates** applies from the next session you start. With it on, a ready update's popover says *Running agents and open terminals keep going through the restart.* On a build that doesn't include the runtime it needs, the switch is disabled and says so: *This build can't keep agents running across restarts.*

***

## Notifications

*Choose how Kepler tells you what your agents are doing. Desktop notifications show while Kepler is in the background, In Kepler alerts while you're using it. Sessions started outside Kepler notify only once they're on a task.*

The Notifications page has one section, **What to notify you about**. Its settings are saved on this machine.

### What to notify you about

The section is a grid. Each row is an event, and each column is a place Kepler can notify you: **Desktop** or **In Kepler**. The following table lists the events and their defaults:

| Event | When it fires | Desktop | In Kepler |
|---|---|---|---|
| **Replies** | *An agent finished replying and it's your turn.* | Off | Off |
| **Questions** | *An agent asks you something and waits for your answer.* | Off | On |
| **Permission requests** | *An agent wants permission to do something.* | Off | On |
| **Errors** | *A session stops because something went wrong.* | Off | On |

If you turned on system notifications in an earlier version of Kepler, every **Desktop** box starts on. When you turn on the first **Desktop** box, Kepler sends a sample notification so your OS asks for permission.

Two more settings sit under the grid:

| Setting | What it controls | Default |
|---|---|---|
| **Play a sound with desktop notifications** | Whether a desktop notification makes the OS notification sound | On |
| **Notify even for the task you're looking at** | *Otherwise Kepler stays quiet about the task open in the window you're using.* | Off |

To silence desktop notifications from one remote machine only, use **Mute notifications from {host}** on that machine in [Remote environments](#remote-environments).

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-settings-notifications-01-01-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-settings-notifications-01-01-v2@2x.png" class="help-center-img img-bordered" alt="Settings › Notifications: a grid of events (Replies, Questions, Permission requests, Errors) against Desktop and In Kepler, at their defaults, with Play a sound with desktop notifications and Notify even for the task you're looking at below it.">
  </a>
  <figcaption style="text-align:center; color:#888">What to notify you about, in Settings → Notifications.</figcaption>
</figure>

***

## Appearance

The Appearance page has four sections: **Theme**, **Chat**, **Terminal**, and **Diff view**. Its settings are saved on this machine.

### Theme

**Theme** has one setting, with four values:

| Option | What it is |
|---|---|
| **Dark** | The middle-dark theme, and **the default a fresh install runs** |
| **Midnight** | The near-black theme |
| **Light** | The light palette |
| **System** | Follows your OS color scheme and switches when the OS does. Its dark is **Dark**, not Midnight |

**System** resolves to **Dark** because your OS says "light or dark" and nothing finer. Someone following the room is asking to follow the room, not to opt into the highest contrast Kepler can draw.

Color mode is the only appearance choice in this section. No second, design-language picker exists.

Terminals follow the theme too. A terminal program that asks, such as an agent's own command-line app, is told the terminal's background color as it starts, so it draws a palette that suits the theme you're on. One that asks to follow theme changes is redrawn when you switch, while it runs.

### Chat

This section sets how a session's transcript scrolls:

| Setting | What it controls | Default |
|---|---|---|
| Auto-scroll | **Auto-scroll to the end** *keeps the newest output in view. Scroll up to stop.* **Stay on my message** *keeps your message in view. The transcript doesn't scroll on its own.* | Auto-scroll to the end |
| **Remember scroll position** | *Return to where you left off when you come back to a session.* | Off |

Neither mode fights you: once you scroll up, the transcript stays where you put it.

### Terminal

This section controls Kepler's embedded terminals:

| Setting | What it controls | Default |
|---|---|---|
| **Font family** | *Separate fonts with commas. The terminal uses the first one installed on this machine.* | Empty, which falls back to your platform's monospace stack |
| **Font size** | Terminal font size in pixels. Values outside 8–32 are clamped | 13 |
| **Line height** | Vertical spacing between lines, to one decimal place. Values outside 1–2 are clamped | 1.2 |
| **Show the message box under terminal sessions** | *Adds Kepler's message box under an agent's terminal, for attachments and voice. You can also switch it from the terminal's status bar.* | Off |

The greyed text in the **Font family** field (`Fira Code, JetBrains Mono, Menlo`) is an example of the format, not the value in effect. If you name a font Kepler can't find on this machine, the field says so and keeps your text. The terminal falls through to the next name in your list.

#### Embedded terminals

Kepler scopes its terminals to a worktree. Opening one starts a shell in that worktree's folder, so you don't need to `cd` into it, and the shell sources your profile the same way an interactive login shell would. Use **⌘ J** to show and hide the terminal panel, **New terminal** to open another, and **Close terminal** to end one.

Terminals are for the work that sits alongside an agent session: running tests while the agent writes code, checking Git state, or reproducing something the session didn't surface. A terminal starts in one worktree and stays there, so work that spans several repositories is usually easier in a standalone terminal.

### Diff view

**Diff view** has one setting:

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Diff view** | The layout diffs open in | Stacked | Stacked, Split |

This setting is what the layout starts on. A per-diff **Stacked** / **Split** toggle also sits on the Changes overlay's viewer header, so you can switch a single diff without changing the default. See [Review changes](/kepler/review-changes).

***

## Voice input

*Talk to your agents instead of typing. Speech is transcribed on this machine and never leaves it.* The Voice input page has two sections: **Model** and **When you stop talking**. Its settings are saved on this machine.

### Model

The section is a guided sequence rather than a flat list. It shows one step at a time, and each step appears only once it can do something:

| Step | What it is |
|---|---|
| **Set up voice input** | *Takes a minute: Kepler checks what this machine can run, then downloads a model.* **Get started** begins setup. Setting up is what turns voice input on |
| Hardware check | A one-time measurement of how fast this machine transcribes: *Checking what this machine can run…* It runs once. Later quality changes skip it |
| **Choose transcription quality** | Picks a model, with the check's recommendation marked **Suggested**. **Download and set up** installs it |
| Ready | The installed model and its size on disk, with **Change quality**, **Remove voice input**, **Technical details**, and **Use voice input in the chat prompt** |

Kepler offers four quality levels:

| Option | What it's best at |
|---|---|
| **Fast** | Short prompts in a quiet room, transcribed almost instantly on any machine. The best place to start |
| **Balanced** | Longer sentences and technical words, still quick on most machines |
| **Accurate** | Accents, names, and background noise. Expect a short pause after speaking on machines without a modern graphics card |
| **Most accurate** | The best quality available, including for languages other than English. Worth it on Apple Silicon or a recent graphics card, and slow on anything older |

Each option shows its approximate download size, calculated for the runtime your hardware check measured, so the number you read before installing is the one you download. Downloads continue if you leave the page, and Kepler notifies you when the model is ready.

Once a model is installed, these controls manage it:

| Control | What it does |
|---|---|
| **Use voice input in the chat prompt** | Shows the microphone in the chat prompt. *Turn this off to pause it. The downloaded model stays on this machine.* |
| **Change quality** | Reopens the quality picker |
| **Remove voice input** | *Removes voice input, frees up its local storage and turns the chat microphone off.* |
| **Technical details** | Shows the model's revision, and the backend and data type it runs on |

### When you stop talking

This section appears once a model is installed. It chooses what happens when you stop recording:

| Option | What it does |
|---|---|
| **Insert the text so you can edit it** | Puts the transcript in the prompt for you to review. The default |
| **Send the prompt** | Sends the prompt automatically |
| **Keep listening, transcribing each phrase as you pause** | Keeps the microphone open and transcribes each phrase as you pause |

Kepler downloads the model from the internet once. Transcription then runs entirely on your device, and your audio is never uploaded. See [Voice Input](/kepler/voice-input).

***

## Keyboard shortcuts

*These shortcuts can't be changed yet.* The Keyboard shortcuts page lists Kepler's shortcuts in six groups, each its own section. Kepler also shows each shortcut in the menu items and button tooltips it belongs to. A few tab shortcuts that Settings doesn't list, such as reopening a closed tab and jumping to a tab by position, are in [Task View](/kepler/task-view#keyboard).

Mac symbols are shown first. On Windows and Linux, **⌘** is **Ctrl** and **⌥** is **Alt**, and **⌃** is **Ctrl** on every platform.

### General

The **General** group holds app-wide shortcuts:

| Action | Mac | Windows / Linux |
|---|---|---|
| Open settings | ⌘ , | Ctrl + , |
| New task | ⌘ N | Ctrl + N |
| Open quick launcher (global) | ⇧ ⌥ N | Shift + Alt + N |
| New window | ⌘ ⇧ N | Ctrl + Shift + N |
| Quit | None | Ctrl + Q |
| Zoom in | ⌘ = | Ctrl + = |
| Zoom out | ⌘ – | Ctrl + – |
| Reset zoom | ⌘ 0 | Ctrl + 0 |
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
| Close tab | ⌘ W | Ctrl + W |
| Toggle terminal | ⌘ J | Ctrl + J |
| Next region | F6 | F6 |
| Previous region | ⇧ F6 | Shift + F6 |

### Dashboard

The **Dashboard** group works on the Dashboard's panels and tasks:

| Action | Mac | Windows / Linux |
|---|---|---|
| Move panel left | ⌘ ⌥ ← | Ctrl + Alt + ← |
| Move panel right | ⌘ ⌥ → | Ctrl + Alt + → |
| Move task to the previous Progress stage | ⌘ ⇧ ← | Ctrl + Shift + ← |
| Move task to the next Progress stage | ⌘ ⇧ → | Ctrl + Shift + → |
| Focus preview panel 1–8 | ⌘ 1–8 | Ctrl + 1–8 |
| Focus last preview panel | ⌘ 9 | Ctrl + 9 |
| Switch preview panels | ⌃ Tab | Ctrl + Tab |
| Switch preview panels, oldest first | ⌃ ⇧ Tab | Ctrl + Shift + Tab |
| Maximize preview panel | ⌘ ⇧ M | Ctrl + Shift + M |
| Maximize panel terminals | ⌘ ⇧ J | Ctrl + Shift + J |

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

### Changes

The **Changes** group works in the Changes view:

| Action | Mac | Windows / Linux |
|---|---|---|
| Filter changed files | ⌘ P | Ctrl + P |
| Previous file | ⌥ ↑ | Alt + ↑ |
| Next file | ⌥ ↓ | Alt + ↓ |
| Comment on selection | ⌘ ⇧ C | Ctrl + Shift + C |

### Shortcuts that depend on where you are

Some keys do different things depending on where you are:

- **⌘ 1**, **⌘ 2**, and **⌘ 3** focus a preview panel on the Dashboard but a column on the task page.
- **⌃ Tab** switches preview panels on the Dashboard and sessions on the task page.
- **⌘ ⇧ J** maximizes the panel's terminals on the Dashboard and the terminal drawer on the task page.
- **⌘ P** filters changed files in the Changes view and opens **Go to file** elsewhere.

Kepler registers **Open quick launcher** with the OS, so it works while Kepler is in the background. Its row carries a **Global** badge. **Quit** and the **PageUp** / **PageDown** tab keys are Windows and Linux shortcuts only. Kepler hides those rows on macOS, which quits through the native **⌘ Q** menu role.

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
| **Use this app's interface in remote windows** | *Windows connected to another machine load their interface from this app instead of from that machine, so only your data crosses the connection. If that machine runs a different version of Kepler, its own interface is used.* Experimental. Desktop app only | Off |

The setting applies the next time you connect to a machine with no other window open on it.

See [Remote environments](/kepler/remote-environments) for connecting, port forwarding, and how sessions behave on a machine.

***

## Remote Access

*Use this machine from any browser or your phone, through a secure GitKraken relay.* No open port and no tunnel to set up yourself. Remote Access requires a paid GitKraken plan and isn't available on the Community plan.

The page explains **How it works** in three steps:

1. Turn it on and name this machine.
2. Scan the QR code or open the link that appears here, on your phone or any browser.
3. Sign in with your GitKraken account, and this machine's tasks and sessions are there.

To turn it on, click **Turn on Remote Access**, then enter a name in **Name this machine**. A status badge shows whether it's on. While it's on, the page shows a QR code (*Scan with your phone camera to open*) and **Copy URL**. *This machine stays awake while Remote Access is on.* links to [Keep agents running](#keep-agents-running) with **Change in General**.

**Connected devices** lists each device that has connected, marking **This device** and when each was **Last seen**, with **Revoke** to disconnect one device and **Refresh** to reload the list. *Only you can connect, signed in to your GitKraken account. Turning Remote Access off disconnects every device, and you can revoke any single device under Connected devices.*

See [Remote environments](/kepler/remote-environments) for prerequisites, pairing, and managing sessions from gitkraken.dev.

***

## Updates

The Updates page has one section, shown without a heading. It's about the app itself:

| Row | What it does |
|---|---|
| **Current version** | The installed version, with **Release notes** beside it to open what's new in that release |
| **Check for updates** | Checks for a newer release and downloads it in the background. Reads **Kepler is up to date** when there's nothing newer, and becomes **Check again** |
| Download progress | While a release downloads: **Downloading** with a percentage, how much has arrived out of the total and the speed (*{done} of {total} at {rate}/s*), and the time left (*About {count} min left*). A **Verifying** step follows before it can install |
| **New version** | Appears once a release is ready, with **Restart to update** beside it, and how many running agents a restart would stop |

A ready update also shows as one chip in the top bar, on every screen, whose popover reads **Update ready to install** and says what a restart does to running work. If agents are mid-tool-call when you restart, Kepler shows *Preparing to restart. Finishing {count} active tool calls…* and waits up to 2 minutes. **Restart now** skips the wait.

The update controls only appear in the desktop app. In a browser window connected to Kepler, this page shows nothing to update.

***

## Help

*Docs, tips and logs for when something goes wrong.* The Help page has two sections: **Help** and **Logs**.

### Help

This section links out to the docs and release notes, and replays any explainer you dismissed:

| Control | What it does |
|---|---|
| **Kepler documentation** | *Guides, keyboard shortcuts, and agent setup.* **Open docs** opens the Kepler docs site in your browser |
| **Release notes** | *See what changed in each version.* **Show release notes** opens them in Kepler |
| **Show tips and guides again** | A disclosure, closed by default: *Kepler explains each view the first time you open it. Show any of those again here.* |

Inside the disclosure, each explainer has a row that reads **Seen and dismissed** or **Not shown yet**, with its own **Show again** button:

- Todo view explainer
- Tasks view explainer
- Agent Graph explainer
- Actions callout
- Task page callout

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
