---
title: Task Settings
description: Choose how new Kepler tasks start, including the default agent, where tasks make changes, where a new task opens on the Dashboard, the branch prefix, folder locations, and automatic task names, how a task's page looks, and your task groups.
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
tags: [settings, tasks, default-agent, worktrees, branch-prefix, folder-locations, variables]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "kepler-configuration"
    nav_label: "Task Settings"
    nav_order: 20
    nav_parent: "kepler-behavior-and-integration-settings"
    page_type: "content"
    card_icon: "checklist"
    card_color: "amber"
    card_description: "How new tasks start: default agent, branch prefix, folders and task names"
---
<kbd>Last updated: November 2026</kbd>

Use **Settings → Tasks** to choose how new tasks start and how a task's page looks, and to manage your task groups. A task is one piece of work: its prompt, the agent sessions working on it, and the worktree or folder they work in.

## New tasks

**New tasks** sets what Kepler preselects for every new task: the agent, where the task makes changes, where its panel opens on the Dashboard, how branches and folders are named, and whether Kepler names the task for you. These values belong to the environment you are working on, so in a remote window they are the remote machine's.

### Default agent

**New sessions start with** sets the agent that the **New task** composer, the Dashboard's composer, and a new draft session start with. It is the same agent-settings pill as in the composer: pick the agent and account, and optionally an [agent preset](/kepler/settings-agents#agent-presets), a model, and other options. Kepler saves each pick as you make it.

**Start each session on the agent you used last**, below the pill, is on by default. With it, your first session uses the pill's agent, and each later session starts with the agent, model, and mode you last picked. To start every session on the pill's agent and settings, clear it.

If you uninstall the agent you saved, the row warns you to pick another. This setting does not apply to Ask Kepler, which has its own default in [Settings → Agents](/kepler/settings-agents).

An [Action](/kepler/actions) inherits this configuration unless it names an agent of its own.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-sessions-start-with-oct-2026-v5@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-sessions-start-with-oct-2026-v5@2x.png" class="help-center-img img-bordered" alt="The top of the New tasks section of Settings › Tasks: New sessions start with, its agent-settings pill showing the Claude Code mark, the caption Your first session uses this agent. After that, each session starts on your last pick, and Start each session on the agent you used last ticked.">
  </a>
  <figcaption style="text-align:center; color:#888">The default agent for new sessions, in Settings → Tasks.</figcaption>
</figure>

### Where new tasks make changes

**Where new tasks make changes** sets what a repository starts on when you attach it to a new task in the **New task** composer. It has these options:

| Option | What it does |
|---|---|
| **Isolated worktree** | The default. Creates a new branch in its own worktree, so agents can work in parallel |
| **New branch** | Creates a new branch in the repository's own checkout, with no worktree |
| **Current branch** | Works on whichever branch the repository's own checkout has |

This setting is only the default. For a single task, the repository chip's own **Base branch** and **Isolated worktree** controls override it. See [Create a task](/kepler/create-task#configuring-a-repository).

**With New branch and Current branch, commits land on whichever branch is checked out at the time**, because both work in the repository's own checkout. If another task is already working in that checkout, Kepler says so and offers to switch that repository to an isolated worktree instead.

You can edit **Branch prefix**, **Worktrees folder**, and **Tasks folder** whichever option you choose, because a single task can still ask for a new branch or a worktree.

### Where a new task opens on the Dashboard

**Where a new task opens on the Dashboard** sets where the panel of a task you start, or open from a notification, appears among the Dashboard's open panels:

| Option | What it does |
|---|---|
| **Beside the focused panel** | The default. Opens the panel next to the one you are reading, or at the end once the panels fill more than one row |
| **At the end** | Always opens the panel after every open panel |

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-new-task-panel-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-new-task-panel-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="Where a new task opens on the Dashboard, in Settings › Tasks: two choice cards, Beside the focused panel (selected), which opens at the end once the panels fill more than one row, and At the end, always after every open panel.">
  </a>
  <figcaption style="text-align:center; color:#888">Where a new task opens on the Dashboard, in Settings → Tasks.</figcaption>
</figure>

### Branch prefix

The following setting starts the name of every branch Kepler creates:

| Setting | What it controls | Default |
|---|---|---|
| **Branch prefix** | *Starts the name of every branch Kepler creates. A repo can set its own in its settings.* | `kepler/` |

The prefix applies to **automatic** names only. Kepler uses a branch name you type exactly as you typed it, so a repository with an enforced `feat/` or `fix/` push rule still works. If your prefix does not end in a separator, Kepler adds a `/`, so `team` becomes `team/`, while `ea-` stays as you typed it.

To override the prefix for one repository, use its [Edit repo](/kepler/settings-repositories#edit-a-repository) page under **Settings → Repositories**.

### Folder locations

Kepler uses 3 folder settings to decide where to put things:

| Setting | Where it is | What it controls | Default |
|---|---|---|---|
| **Worktrees folder** | Tasks → New tasks | *Where Kepler creates the worktree for each new task.* | `~/kepler/worktrees` |
| **Tasks folder** | Tasks → New tasks | *Each task gets a folder here for its attachments and files.* | `~/kepler/tasks` |
| **Repositories folder** | [Repositories](/kepler/settings-repositories#repositories-folder) | Where Kepler clones repositories, and where it looks for repositories to add | `~/kepler/repositories` |

Type a path, or click **Choose a folder** beside the field to browse. An edit saves when you leave the field.

The fields also warn you about paths that do not work the way you might expect:

- If a **Worktrees folder** has text before `<REPOSITORY_PATH>`, Kepler adds each repository's full path after that text. The field suggests 2 patterns that work: worktrees next to each repository, or a subfolder per repository. On Windows, Kepler does not save a path like this, so use one of the 2 patterns.
- If the **Repositories folder** does not exist yet, the field tells you that Kepler creates it when you clone.

### The Variables menu

A folder field that takes variables has a **Variables** menu beside it. Pick a variable, such as **REPOSITORY PATH**, to insert it at the cursor. Kepler fills it in when it creates the folder, so one pattern works for every repository. Each field offers only the variables it can fill in:

| Field | Variables offered |
|---|---|
| **Worktrees folder** | `<REPOSITORY_PATH>` (*Main repo folder*), `<REPOSITORY_NAME>` (*Repo name*) |
| **Repositories folder** | `<REPOSITORY_NAME>` |
| **Tasks folder** | None |

For example, `<REPOSITORY_PATH>/.worktrees/<REPOSITORY_NAME>` nests each worktree inside the repository it belongs to.

Per-repository commands have a **Variables** menu of their own, with 2 more variables. See [Per-repository commands](/kepler/settings-repositories#per-repository-commands).

<figure style="text-align:center">
  <a href="/wp-content/uploads/folder-fields-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/folder-fields-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Worktrees folder field in Settings › Tasks, set to /home/alex/kepler/worktrees, with its Variables menu open listing the REPOSITORY PATH tag (Main repo folder) and the REPOSITORY NAME tag (Repo name), each beside its raw token, and the Choose a folder button beside the field.">
  </a>
  <figcaption style="text-align:center; color:#888">The Worktrees folder field in Settings → Tasks, with the Variables menu open.</figcaption>
</figure>

### Automatically name new tasks

The following setting names new tasks for you:

| Setting | What it controls | Default |
|---|---|---|
| **Automatically name new tasks** | *Names a new task with AI from its prompt and attached resources. A task created from a single issue or PR keeps that item's name.* | On |

You need a paid GitKraken subscription to turn this setting on. Without one, a lock replaces the checkbox while the setting is off. If the setting is on, you can still turn it off. A change takes effect on the next task you create.

## Task page

**Task page** sets how a task's page looks in this window. Kepler saves these settings on this machine:

| Setting | What it controls | Default |
|---|---|---|
| **Show tabs on the task page** | Keeps sessions, worktrees, and resources open as tabs you can pin, drag between groups, and arrange side by side | Off |
| **Preview tabs** | *A single click opens a preview that the next click replaces. Double-click, or edit, to keep it open.* | On |

With **Show tabs on the task page** off, each column of a task shows one thing at a time, and you switch between them from the list on the left. **Preview tabs** works only with it turned on. Sessions always open as permanent tabs. See [The task view](/kepler/task-view).

## Groups

**Groups** lists all your task groups, including archived ones. To open it from the Dashboard, choose **Manage groups…** in a group header's menu.

- To add a group, click **New group** in the section header.
- To edit a group's name or color, click its name.
- To reorder groups, drag a row by its grip.
- To archive or delete a group, use its **⋮** menu. You can archive a group once all its tasks are archived.

Archived groups are listed under **Archived**, where their menu has **Restore group**. Deleting a group never deletes its tasks; they stay, ungrouped. See [Your groups](/kepler/arranging-your-work#your-groups).

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-groups-settings-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-groups-settings-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Groups section of Settings › Tasks with New group: Checkout (blue, 2 tasks), Search (yellow, 1 task) and Payments (green, 1 task), each with a drag grip and a menu, then Archived with Holiday sale (pink, 1 task) and its menu.">
  </a>
  <figcaption style="text-align:center; color:#888">3 groups and 1 archived group, in Settings → Tasks.</figcaption>
</figure>

***

---
