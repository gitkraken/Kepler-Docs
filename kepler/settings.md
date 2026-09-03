---
title: Settings
description: A reference for every setting in Kepler across the eight Settings sub-pages, plus folder locations, worktree path placeholders, per-repository startup commands, and the keyboard shortcut list.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
integrations: [claude-code, codex, copilot, cursor, opencode, auggie, github, gitlab, bitbucket, azure-devops, jira, linear, trello]
hosted_variant: both
status: GA
last_verified: 2026-09
llms_include: true
tags: [settings, configuration, keyboard-shortcuts, appearance, agents, actions, repositories, worktrees, terminal, voice-input, remote, gitkraken-dev, integrations, preferences]
taxonomy:
  category: kepler
---
<kbd>Last updated: September 2026</kbd>

Settings is eight sub-pages, each with its own sections. This page documents every one of them: what each setting controls, what it defaults to, and what changes when you change it.

Open Settings from the gear icon in the top bar, or with **⌘ ,** (**Ctrl ,** on Windows and Linux).

<figure>
  <a href="/wp-content/uploads/settings-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-aug-2026.png" class="help-center-img img-bordered" alt="Settings open on the General sub-page, with the left rail showing Setup plus all eight sub-pages">
  </a>
  <figcaption style="text-align:center; color:#888">Settings, open on General.</figcaption>
</figure>

***

## The eight sub-pages

Above the sub-pages sits **Setup**, a progress ring that reopens the first-run checklist. The left rail lists the sub-pages in this order:

| Sub-page | What it covers |
|---|---|
| **General** | App updates, folder locations, app behavior, diagnostics, language, keyboard shortcuts |
| **Appearance** | Color mode, terminal font, diff layout |
| **Agents** | Your default agent, per-agent configuration, cross-agent options, AI Sync and Compose |
| **Actions** | Preferred Actions per item kind, and the Action list |
| **Remote** | Remote environments over SSH, and remote access to this window from another device |
| **Integrations** | Issue tracker and Git host connections |
| **Voice Input** | On-device speech-to-text and its model |
| **Repositories** | Tracked repositories, per-repository commands, and Projects |

Moving between sub-pages replaces a single history entry. As a result, **Back** returns you to whatever you were doing before you opened Settings, rather than walking back through every sub-page you visited.

### Deep links and section anchors

Every section has a stable anchor id. A link of the form `/settings/<sub-page>#<section-id>` opens that sub-page and scrolls to the section.

Legacy links of the form `/settings#<section-id>` still work: Kepler resolves the id to whichever sub-page owns that section and keeps the hash. A naked `/settings` opens **General**. Here is each sub-page's path with its section anchors, in page order:

| Sub-page path | Section anchors, in page order |
|---|---|
| `/settings/general` | `updates`, `general`, `language`, `keyboard-shortcuts` |
| `/settings/appearance` | `appearance`, `terminal`, `diff-view` |
| `/settings/agents` | `default-agent`, `agents`, `agent-options`, `features` |
| `/settings/actions` | `preferred-actions`, `action-list` |
| `/settings/remote` | `remote-environments`, `remote-access` |
| `/settings/integrations` | `provider-integrations` |
| `/settings/voice` | `voice` |
| `/settings/repositories` | `repositories`, `projects` |

Each installed agent also gets its own anchor, `agent-<agent-id>`, for example `agent-claude-code`.

***

## General

Four sections: **Update**, **General**, **Language**, **Keyboard Shortcuts**.

### Update

The **Update** section has three rows:

| Row | What it does |
|---|---|
| **Current version** | The installed version. Click the version number to open **What's New** for that release |
| **Check for updates** | Checks for a newer release and downloads it in the background |
| **New version** | Appears once a release has downloaded, with **Restart to install** beside it |

The update controls only appear in the desktop app. In a browser window connected to Kepler, this section shows nothing to update.

### General

This section covers where Kepler stores things on disk, general app behavior, and diagnostics.

#### Folder locations

Three paths tell Kepler where to put things. All three are unset out of the box; Kepler computes a fallback under your home folder without writing it, so an untouched setting still reads as untouched. These are the three folder settings:

| Setting | What it controls | Default |
|---|---|---|
| **Default Repositories Folder** | Where Kepler clones repositories | `~/kepler/repositories` |
| **Default Worktrees Folder** | Where Kepler creates new worktrees | `~/kepler/worktrees` |
| **Default Tasks Folder** | Where Kepler creates task folders | `~/kepler/tasks` |

Type a path directly, or use the folder button beside the field to browse. Edits save automatically as you type, so no separate Save button exists.

<figure>
  <a href="/wp-content/uploads/placeholder-legend-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/placeholder-legend-aug-2026.png" class="help-center-img img-bordered" alt="Settings → General, showing the three folder fields and the Placeholders legend beneath them">
  </a>
  <figcaption style="text-align:center; color:#888">The three folder fields, with the Placeholders legend.</figcaption>
</figure>

#### Path placeholders

The folder paths and per-repository commands both accept the same placeholders. Kepler substitutes them at worktree creation time, so one pattern covers every repository. Kepler defines four placeholders:

| Placeholder | Resolves to |
|---|---|
| `<REPOSITORY_PATH>` | Main repo folder |
| `<REPOSITORY_NAME>` | Repo name |
| `<SOURCE_PATH>` | Where files come from (the main repo, or the source worktree when forking) |
| `<WORKTREE_PATH>` | The new worktree folder |

For example, `<REPOSITORY_PATH>/.worktrees/<REPOSITORY_NAME>` nests each worktree inside the repository it belongs to. Kepler collapses any `..` segments you write, and resolves `<REPOSITORY_PATH>` and `<REPOSITORY_NAME>` as soon as it knows which repository it is planning for. `<SOURCE_PATH>` and `<WORKTREE_PATH>` only carry a value once a source and a target exist, which is why they are most useful in commands rather than in the folder path itself.

Commands run inside the new worktree folder using your default login shell, so you don't need to `cd` into it, and tools configured in your shell profile (`nvm`, for instance) are available.

#### App behavior

These six settings control app behavior:

| Setting | What it controls | Default |
|---|---|---|
| **Always use the custom folder picker** | Local windows use the native OS folder dialog and remote windows use Kepler's own picker, which can browse a remote filesystem. Turn this on to use Kepler's picker everywhere | Off |
| **Restore windows on launch** | Reopens every window from your last session at its previous size, route, and connection. Turn it off to start in a single window | On |
| **Show tabs on the task page** | Keeps several sessions, worktrees, or resources open as tabs in the same column. With it off, each column shows one thing at a time and you switch from the list on the left. You can close columns either way. See [The task view](/kepler/task-view) | Off |
| **Prevent sleep while agent sessions are active** | Keeps this computer awake while an agent session is starting, running, or waiting for your input | On |
| **Enable system notifications** | Shows desktop notifications when an agent finishes, needs your attention, or errors while Kepler is in the background. Turning it on sends a sample notification so your OS asks for permission | Off |
| **Notify for external terminal tasks** | Notifications for Claude tasks running in your own terminal. Turn it off to silence those while keeping notifications for Kepler-managed tasks. Disabled while system notifications are off | On |

Kepler reads **Restore windows on launch** during cold start, so a change takes effect on the next launch.

**Prevent sleep while agent sessions are active** holds the machine awake through the platform's own mechanism: `caffeinate` on macOS, an execution-state assertion on Windows, `systemd-inhibit` on Linux. It does nothing where the platform offers none, so a machine that sleeps anyway is a degraded experience rather than a broken one. This setting applies to the computer the agents run on, which on a remote connection is the remote host, and it counts Claude Code sessions detected outside Kepler alongside Kepler's own. Kepler releases the machine as soon as the last such session settles.

#### Diagnostics

The **Diagnostics** section has four rows:

| Row | What it does |
|---|---|
| **Log file** | The full path to the current log, read-only |
| **Reveal** | Opens the log's folder in your file manager. Hidden where the host cannot open one |
| **Copy path** | Copies the log path to your clipboard |
| **Clear log** | Deletes the current and rotated log files, after a confirmation |

The log grows to roughly 20 MB. Attach it when you file a bug report.

### Language

**Language** has one setting:

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Language** | The display language for Kepler's interface | English | English, Español |

The choice also applies to native dialogs, not only the in-app interface.

### Keyboard Shortcuts

This section lists Kepler's shortcuts. They are a reference, not editable. Mac symbols are shown first; the Windows and Linux column substitutes **Ctrl** for **⌘** and **Alt** for **⌥**:

| Action | Mac | Windows / Linux |
|---|---|---|
| Open settings | ⌘ , | Ctrl + , |
| New task | ⌘ ⇧ N | Ctrl + Shift + N |
| Switch to tab 1–9 | ⌥ 1–9 | Alt + 1–9 |
| Previous tab | ⌘ ⇧ [ | Ctrl + Shift + [ |
| Next tab | ⌘ ⇧ ] | Ctrl + Shift + ] |
| Open quick launcher (global) | ⇧ ⌥ T | Shift + Alt + T |
| New window | ⌘ N | Ctrl + N |
| Quit | — | Ctrl + Q |
| Zoom in | ⌘ = | Ctrl + = |
| Zoom out | ⌘ – | Ctrl + – |
| Reset zoom | ⌘ 0 | Ctrl + 0 |
| Close tab | ⌘ W | Ctrl + W |
| Toggle terminal | ⌘ J | Ctrl + J |
| New tab | ⌘ T | Ctrl + T |
| Manage remote environments | ⌘ ⇧ R | Ctrl + Shift + R |
| Find in conversation | ⌘ F | Ctrl + F |
| Dismiss / Cancel | Escape | Escape |

Kepler registers **Open quick launcher** with the OS, so it works while Kepler is in the background. **Quit** is a Windows and Linux shortcut only. macOS quits through the native **⌘ Q** menu role, and Kepler hides the row there.

That table is the whole set. Kepler has no view-switching shortcuts, since only one interface exists, so **⌘ 1**, **⌘ 2**, and **⌘ 3** stay unbound. The sidebar toggles that once sat on **⌘ B** and **⌘ ⌥ B** are also gone, along with the surfaces they opened.

***

## Appearance

Three sections: **Theme**, **Terminal**, **Diff View**.

### Theme

**Theme** has one setting:

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Theme** | Whether Kepler renders in its dark or light palette. **System** follows your OS color scheme and switches when the OS does | Dark | Dark, Light, System |

Color mode is the only appearance choice in this section. No second, design-language picker exists: an earlier build paired the mode switcher with a **Base** / **Observatory** choice, and that pair no longer exists.

### Terminal

Controls the font Kepler's embedded terminals use:

| Setting | What it controls | Default |
|---|---|---|
| **Font Family** | Comma-separated list of font families. The first available font is used | Empty, which falls back to your platform's monospace stack |
| **Font Size** | Terminal font size in pixels. Values outside 8–32 are clamped | 13 |
| **Line Height** | Vertical spacing between lines, to one decimal place. Values outside 1–2 are clamped | 1.2 |

The greyed text in the **Font Family** field (`Fira Code, JetBrains Mono, Menlo`) is an example of the format, not the value in effect. If you name a font Kepler cannot find on this machine, the field says so and keeps your text; the terminal falls through to the next name in your list.

#### Embedded terminals

Kepler scopes its terminals to a worktree. Opening one starts a shell in that worktree's folder, so you do not need to `cd` into it, and the shell sources your profile the same way an interactive login shell would. Use **⌘ J** to show and hide the terminal panel, **New terminal** to open another, and **Close terminal** to end one.

Terminals are for the work that sits alongside an agent session: running tests while the agent writes code, checking git state, or reproducing something the session did not surface. A terminal starts in one worktree and stays there, so work that spans several repositories is usually easier in a standalone terminal.

### Diff View

**Diff View** has one setting:

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Diff View** | The layout diffs open in | Stacked | Stacked, Split |

This setting is the only control over diff layout. The diff pane in a task's worktree column carries no header of its own, so no per-diff **Stacked** / **Split** toggle appears beside it. See [Review changes](/kepler/review-changes).

***

## Agents

Four parts: **Default agent**, one section per agent Kepler detects, **Agent options**, and **Features**.

<figure>
  <a href="/wp-content/uploads/agent-settings-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-settings-aug-2026.png" class="help-center-img img-bordered" alt="Settings → Agents, showing the Default agent row and the Claude Code and Codex sections with their status badges">
  </a>
  <figcaption style="text-align:center; color:#888">Settings → Agents.</figcaption>
</figure>

### Default agent

Picks the agent, account, model, mode, and thinking effort that Kepler preselects in the Task Launcher and applies when you start a new session inside a worktree:

| Control | What it does |
|---|---|
| **Agent picker** | Chooses the agent, and the account when that agent supports more than one |
| **Options** | Model, mode, and the agent's own configuration options. Available once an agent is picked |
| **Clear default** | Removes the saved default. Appears only once one is set |

Nothing is set out of the box, and the section is hidden entirely when no agent is installed. If the agent you saved is later uninstalled, the row warns you and asks you to pick another.

An [Action](/kepler/actions) inherits this configuration unless it names an agent of its own.

### One section per agent

Kepler ships adapters for **Claude Code**, **Codex**, **GitHub Copilot**, **Cursor CLI**, **OpenCode**, and **Auggie**, listed in that order. Each gets a section titled with the agent's name. Each agent's section carries five controls:

| Control | What it does |
|---|---|
| **Status** | **Installed** for a detected command-line interface (CLI), **Bundled** for Codex, which runs on Kepler's own engine, or **Not installed** |
| **Install** | Runs an install method on your behalf and streams the output. Shown on a not-installed agent that has an installer for your OS |
| **Sign in** / **Sign out** | Authenticates the agent with its provider. Signing out deletes the stored credentials |
| **Enabled** | Whether Kepler offers the agent anywhere |
| **Configure** | Expands the agent's own configuration |

Under **Configure**:

| Setting | What it controls | Default |
|---|---|---|
| **Binary** | The binary Kepler spawns. **Auto** resolves it the way your shell does (the first match on your `PATH`), so it matches `which`. Pick a specific install, or **Custom path…**, to override. **Re-scan** searches again | Auto |
| **Data directory** | Overrides the agent's default data and config directory | Empty, meaning the agent's own default |
| **Accounts** | Runs multiple logins side by side, each with its own credentials and history but sharing your skills, agents, commands, and settings. Available for Claude Code, Codex, GitHub Copilot, and Auggie | One account |

Codex has no binary picker. Its sessions and local sign-in run on Kepler's bundled `codex-acp` engine rather than an installed `codex` CLI, and usage figures read the OAuth token from `~/.codex/auth.json`, or `CODEX_HOME/auth.json` when you have set a custom data directory.

#### Claude Code options

Claude Code adds two settings once it is installed:

| Setting | What it controls | Default |
|---|---|---|
| **Default mode for new sessions** | **Rich chat** is the full visual experience, with plans, model, and effort controls, and richer input. **Terminal** runs Claude as a command-line session in an embedded terminal, the same as the Claude Code CLI. You can switch modes inside a session at any time | Rich chat |
| **Detect Claude Code sessions started outside Kepler** | Adds hooks to `~/.claude/settings.json` so Kepler surfaces sessions you start in your own terminal | Off |

In **Terminal** mode with detection off, Kepler warns you: Claude Code runs as a plain terminal command there, and detection is what lets Kepler track those sessions.

#### Custom agent servers

Below the detected agents, **Custom agent servers** lets you add your own agent that speaks the Agent Client Protocol (ACP), by name and command. Added servers appear with the built-in agents everywhere an agent can be picked.

### Agent options

Settings that apply across every agent:

| Setting | What it controls | Default |
|---|---|---|
| **Installed agents** → **Refresh** | Re-detects the agent CLIs installed on this system. Run it after installing or removing one outside Kepler | — |
| **Install GitKraken MCP for detected clients** | Adds the GitKraken Model Context Protocol (MCP) server to every detected MCP client on this machine so agents can call provider APIs directly. Reinstalls on app startup; uninstalling is not supported | On |
| **Show token usage** → **Enable** | Reads your Claude Code, Codex, and Augment access tokens from disk and calls the providers' private usage APIs. Those endpoints are undocumented and may change without notice. Kepler never sends tokens anywhere except to their respective provider | Off |

Each agent's binary picker carries its own **Re-scan** for the single-agent case; **Refresh** here sweeps all of them.

**Install GitKraken MCP for detected clients** is about the *other* MCP clients on your machine. It differs from the workspace MCP server that Kepler attaches to every session it starts itself, which is always on and has no setting. That server gives the agent tools to:

- Read the task's shared context and resources.
- Attach and detach issue, pull request, and URL links.
- List the repositories in your workspace.
- Create or discard one of the task's worktrees.

**AI Sync** and **Compose** below add their tools to that same server.

### Features

Two shipped capabilities that give agents extra Git tooling. Both are off until you turn them on, and both require a paid GitKraken subscription:

| Setting | What it gives agents | Default |
|---|---|---|
| **AI Sync** | Tools to rebase or merge with automatic conflict resolution. Every operation is safe, and you can roll it back easily | Off |
| **Compose** | Tools to reorganize messy changes into clean, atomic commits. Every operation is safe, and you can undo it easily | Off |

Turning either one on confirms that **New agent sessions will pick up this change**. Sessions already running keep the tools they started with, so start a new session to use them.

***

## Actions

An **Action** is an editable named prompt you fire at a task, issue, or pull request. This sub-page is where you edit them. It has two sections:

| Section | What it holds |
|---|---|
| **Preferred actions** | One picker per kind of item (**Tasks**, **Issues**, **Pull requests I authored**, **Pull requests from others**) setting which Action the one-click half of the Action button runs. Any slot can be **None** |
| **Actions** | The shipped Actions under **Built in** and yours under **Custom**, each with **Edit**, **Restore default** where you have edited it, and **Delete** on a custom row. **New action** creates one; **Restore all defaults** discards every edit |

Kepler ships four default Actions:

- **Tasks** default to **Implement**.
- **Issues** default to **Plan**.
- Pull requests you authored default to **Address Feedback**.
- Pull requests from others default to **Review**.

For what the built-in Actions ask an agent to do, how the editor's **Title**, **Prompt**, **Applies to**, and **Agent** fields behave, and how an Action picks the agent it runs on, see [Actions](/kepler/actions).

***

## Remote

Two sections that sound alike and do opposite things. **Remote Environments** runs your agents on another machine. **Remote Access** opens this Kepler from another device.

### Remote Environments

Runs your agents on another machine (a dev server, a cloud VM, or WSL on Windows) while you work from here. Kepler installs itself over SSH, so the host needs nothing pre-installed.

This section describes the feature and routes you to it. **Manage remote environments…** opens the connections panel, where you add, connect, and remove hosts. **⌘ ⇧ R** opens the same panel from anywhere. See [Remote environments](/kepler/remote-environments).

### Remote Access

Opens this Kepler window from another device over a secure tunnel relayed through your GitKraken account, with no open port and no tunnel to set up yourself. Requires a paid GitKraken plan; not available on the free Community edition. Click **Enable**, name the machine, then scan the QR code or open the link on the other device to pair it.

This section describes the feature and routes you to it. See [Remote access](/kepler/remote-environments#remote-access-reach-this-kepler-from-another-device) for prerequisites, pairing, and managing sessions from gitkraken.dev.

***

## Integrations

One section, **Provider Integrations**. Connect your issue and pull-request providers to see them in the Task Composer and in [the Kepler interface](/kepler/kepler-interface).

Kepler lists every supported provider whether or not it is connected, in this order:

| Provider |
|---|
| Azure DevOps |
| Bitbucket |
| GitHub |
| GitHub Enterprise |
| GitLab |
| GitLab Self-Managed |
| Jira |
| Linear |
| Trello |

Each provider row carries five controls:

| Control | What it does |
|---|---|
| **Connect** | Starts the connection flow for a provider you have not connected |
| **Connected** | Shown on a working connection |
| **Reconnect** | Refreshes an expired token. A warning icon and the hint *"Sign-in has expired. Click Reconnect to refresh this provider's token."* mark the rows that need it |
| **Disconnect** | Disconnects the provider from GitKraken everywhere: the `gk` CLI and GitKraken Desktop lose access too, along with any additional accounts for that provider. You can reconnect at any time |
| **Refresh** | Re-checks every provider's connection status |

Providers connect through your GitKraken account, so the section asks you to sign in before it shows anything to manage.

When a provider has more than one account, an **Accounts** block lists them. **Set as primary** chooses which account Kepler acts as, and **Read from this account** chooses which one Kepler reads issues and pull requests from. They can be different accounts.

For per-provider setup, see [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

***

## Voice Input

One section. Dictate into the agent chat instead of typing. Kepler transcribes audio locally on your device.

The panel is a sequence rather than a flat list: it shows one step at a time, and each step appears only once it can do something:

| Step | What it is |
|---|---|
| **Enable voice input** | Adds a microphone to the agent chat prompt. Off by default; everything below stays hidden until you turn it on |
| **Check what this computer can run** | A one-time measurement of how fast this machine transcribes. It downloads a small test model and takes about a minute. **Run the check** starts it |
| **Set up voice input** | Picks transcription quality, with the check's recommendation marked **Suggested**. **Download and set up** installs it |
| **Voice input is ready** | The installed model, its size on disk, and when it was added |
| **Dictation** | How the microphone behaves. Appears once a model is installed |

The check requires you to start it explicitly, because it pulls roughly 80 MB to time your GPU. It runs once. Later quality changes skip it.

### Transcription quality

Kepler offers four quality levels:

| Option | What it is best at |
|---|---|
| **Fast** | Short prompts in a quiet room, transcribed almost instantly on any machine. The place to start, and the preselected option |
| **Balanced** | Longer sentences and technical words, still quick on most machines |
| **Accurate** | Accents, names, and background noise. Expect a short pause after speaking without a modern graphics card |
| **Most accurate** | The best quality on offer, including for languages other than English. Worth it on Apple Silicon or a recent graphics card; slow on anything older |

Each option shows its approximate download size, calculated for the runtime your hardware check measured, so the number you read before installing is the one you download. Downloads continue if you leave the page, and Kepler notifies you when the model is ready.

From the ready state, **Change quality** reopens the picker, **Remove** deletes the model and turns the chat microphone off, and **Technical details** shows the model id, its revision, and the backend and data type it runs on.

### Dictation

**Dictation** has two settings:

| Setting | What it controls | Default |
|---|---|---|
| **Submit after speaking** | Sends the prompt automatically when you stop recording, instead of inserting the text for you to review | Off |
| **Continuous dictation** | Keeps the microphone open and transcribes each phrase as you pause, instead of press-and-hold | Off |

The two are mutually exclusive, and Kepler disables whichever one you did not choose with a hint saying why: continuous dictation keeps the microphone open, so no single stop exists to submit on.

Kepler downloads the model from the internet once. Transcription then runs entirely on your device, and your audio is never uploaded. See [Voice Input](/kepler/voice-input).

***

## Repositories

Two sections: **Repositories** and **Projects**.

### Repositories

Every repository Kepler tracks, each row showing its name (the display name where you have set one, otherwise the folder name), its path on disk, and how many commands it has: **No commands**, **1 command**, or a count:

| Control | What it does |
|---|---|
| **Row** | Click it to open **Edit &lt;name&gt;**, which holds the repository's display name, description, and commands |
| **Add repository** | Registers an existing local repository with Kepler |
| **Trash icon** | Untracks the repository. The folder on disk is left untouched |

Removing a repository deletes its sessions, terminals, and configured commands, and terminates any live agent and terminal sessions tied to it. Kepler confirms before it does.

With no repositories tracked, the section reads *"Add a repo to configure per-repository commands."*

#### Display name and description

**Edit &lt;name&gt;** opens on two fields above the command list:

| Field | What it does |
|---|---|
| **Display name** | An alias Kepler shows wherever it names this repository — *Shown across Kepler. Leave empty to use the folder name.* The field's placeholder is the folder name, and the full path on disk sits under the field, which is what tells two checkouts of one repository apart. A repository you have named this way keeps that name verbatim and stops competing with same-named folders for a disambiguating suffix |
| **Description** | Free text — *What this repository is for (optional)* — described as *Given to agents working on this repo, so they know what it is for.* Kepler appends it to the repository's line in the resource list it hands a session, so a full sentence is more useful here than a single label |

Both are optional. Kepler stores whitespace-only text as empty, and **Save** stays disabled until something has actually changed.

#### Per-repository commands

Commands are shell commands scoped to one repository. Use them to install dependencies, run a build, or start a watcher, so a new worktree is ready for an agent session with no manual setup.

In the commands editor, **Add command** appends a row with three fields:

| Field | What it does |
|---|---|
| **Name** | A label, for example *Install deps*. It is what you pick from the **Run** menu later |
| **Command** | The shell command, for example `pnpm install`. Accepts the same path placeholders listed under **General → Path placeholders** |
| **Run on worktree creation** | Runs this command automatically when Kepler creates a worktree for this repository. Off by default, which leaves it a command you run on demand |

Kepler drops rows left completely empty on save, so an accidental **Add command** leaves no trace.

Commands flagged to run on worktree creation execute sequentially, in list order, and stop on the first failing command. Kepler skips the rest and reports them as skipped. Each one runs in the new worktree's folder through your interactive login shell, with a ten-minute timeout.

A failed command does not undo the worktree. The worktree exists but may not be usable. To fix it:

1. Read the command output in the task.
2. Correct the command here.
3. Run it again from the **Run** menu.

From the task view, right-click a worktree row in the rail and use **Run command here** for a second way in. It lists that repository's commands and runs the one you pick in that worktree, opening its terminal in place. A repository with none yet reads **No commands yet** and offers **Create command…**.

<figure>
  <a href="/wp-content/uploads/create-command-for-repo-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/create-command-for-repo-aug-2026.png" class="help-center-img img-bordered" alt="The Commands section of the Edit repo modal, with a command flagged Run on worktree creation and the Placeholders legend beneath it">
  </a>
  <figcaption style="text-align:center; color:#888">A repository's Commands, with the Placeholders legend.</figcaption>
</figure>

### Projects

A **Project** groups repositories so they act as a unit (a frontend and a backend you change together, for instance). **Projects** has two controls:

| Control | What it does |
|---|---|
| **Row** | Shows the project's name and its repository count. The pencil icon opens it for editing |
| **New project** | Names a project and picks its repositories. You can add a repository from a folder without leaving the dialog |

With no projects, the section reads *"No projects yet. Create one to group your repos."*

---
