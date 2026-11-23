---
title: Task Settings
description: Choose how new Kepler tasks start (where they make changes, the tasks folder, and automatic task names), where tasks open, how a task's page and Dashboard panels look, and your task groups.
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
tags: [settings, tasks, default-agent, worktrees, tasks-folder, task-page, side-pane, groups]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Use **Settings → Tasks** to choose how new tasks start, where tasks open, and how a task's page and Dashboard panels look, and to manage your task groups. A task is one piece of work: its prompt, the agent sessions working on it, and the worktree or folder they work in.

## New tasks

**New tasks** sets what Kepler preselects for every new task: where the task makes changes, where its files go, and whether Kepler names the task for you. These values belong to the environment you are working on, so in a remote window they are the remote machine's.

### Default agent

**New tasks** shows the agent new sessions start with. To change it, click **Change in Agents**, which opens [Defaults](/kepler/settings-agents#defaults) in **Settings → Agents**. There you also choose the agent Ask Kepler chats start with, and whether new sessions start in **Chat** or **Terminal**. An [Action](/kepler/actions) uses the default agent unless it names an agent of its own.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-sessions-start-with-oct-2026-v5@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-sessions-start-with-oct-2026-v5@2x.png" class="help-center-img img-bordered" alt="The top of the New tasks section of Settings › Tasks: New sessions start with, its agent-settings pill showing the Claude Code mark, the caption Your first session uses this agent. After that, each session starts on your last pick, and Start each session on the agent you used last ticked.">
  </a>
  <figcaption style="text-align:center; color:#888">The Defaults section of Settings → Agents.</figcaption>
</figure>

### Where new tasks make changes

**Where new tasks make changes** sets what a repository starts on when you attach it to a new task in the **New task** composer. Pick one of these options from its dropdown:

| Option | What it does |
|---|---|
| **Isolated worktree** | The default. Creates a new branch in its own worktree, so agents can work in parallel |
| **New branch** | Creates a new branch in the repository's own checkout, with no worktree |
| **Current branch** | Works on whichever branch the repository's own checkout has |

This setting is only the default. For a single task, the repository chip's own **Base branch** and **Isolated worktree** controls override it. Under **Isolated worktree**, the composer names the default as **New tasks:** and the option, and **Change** opens this setting. See [Create a task](/kepler/create-task#configuring-a-repository).

**With New branch and Current branch, commits land on whichever branch is checked out at the time**, because both work in the repository's own checkout. If another task is already working in that checkout, Kepler says so and offers to switch that repository to an isolated worktree instead.

New branches start with the branch prefix, and new worktrees go in the worktrees folder, whichever option you choose. **New tasks** shows both, and **Change in Repositories** opens them in [Settings → Repositories → Default locations](/kepler/settings-repositories#default-locations).

### Folder locations

The following setting decides where each task keeps its files:

| Setting | What it controls | Default |
|---|---|---|
| **Tasks folder** | *Each task gets a folder here for its attachments and files.* | `~/kepler/tasks` |

Type a path, or click **Choose a folder** beside the field to browse. An edit saves when you leave the field. The worktrees folder and the repositories folder are in [Settings → Repositories](/kepler/settings-repositories#default-locations).

### Automatically name new tasks

The following setting names new tasks for you:

| Setting | What it controls | Default |
|---|---|---|
| **Automatically name new tasks** | *Names a new task with AI from its prompt and attached resources. A task created from a single issue or PR keeps that item's name.* | On |

A change takes effect on the next task you create.

<a id="task-page"></a>

## Task page and panels

**Task page and panels** sets where a task opens and how its page and Dashboard panel look. Kepler saves these settings on this machine:

| Setting | What it controls | Default |
|---|---|---|
| **Where tasks open** | Whether a task you open from a link, Go To, or a notification opens as its own page or as a Dashboard panel | Automatic |
| **Where a new task opens on the Dashboard** | Where a new task's panel appears among the open panels | Beside the focused panel |
| **Show tabs on the task page** | Keeps sessions, worktrees, and resources open as tabs you can pin, drag between groups, and arrange side by side | Off |
| **Preview tabs** | *A single click opens a preview that the next click replaces. Double-click, or edit, to keep it open.* | On |
| **Open the side pane in Dashboard panels** | When a Dashboard panel has room, shows its worktree's changes beside the session, or its resources when it has no worktree | Only when there are changes |

**Where tasks open** has these options:

- **Automatic** opens a Dashboard panel when you are on the Dashboard, and the task page everywhere else.
- **Task page** always opens the task's own page.
- **Dashboard panel** always opens a Dashboard panel.

The phone app always opens the task page.

With **Show tabs on the task page** off, each column of a task shows one thing at a time, and you switch between them from the list on the left. **Preview tabs** works only with it turned on. Sessions always open as permanent tabs. See [The task view](/kepler/task-view).

**Open the side pane in Dashboard panels** has these options:

- **Always** opens the side pane whenever the panel has room.
- **Only when there are changes** opens it for a worktree with uncommitted files or commits on its branch.
- **Never** leaves it closed. Open it from the panel header.

Closing the pane keeps it closed for that task in that view.

### Where a new task opens on the Dashboard

**Where a new task opens on the Dashboard** sets where the panel of a task you start, or open from a notification, appears among the Dashboard's open panels. Pick one of these options from its dropdown:

| Option | What it does |
|---|---|
| **Beside the focused panel** | The default. Opens the panel next to the one you are reading, or at the end once the panels fill more than one row |
| **At the end** | Always opens the panel after every open panel |

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-new-task-panel-nov-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-new-task-panel-nov-2026-v3@2x.png" class="help-center-img img-bordered" alt="Where a new task opens on the Dashboard, in Settings › Tasks, with its dropdown open: Beside the focused panel (selected), which opens at the end once the panels fill more than one row, and At the end, always after every open panel.">
  </a>
  <figcaption style="text-align:center; color:#888">Where a new task opens on the Dashboard, in Settings → Tasks.</figcaption>
</figure>

## Groups

**Groups** lists all your task groups, including archived ones. To open it from the Dashboard, choose **Manage groups…** in a group header's menu.

- To add a group, click **New group** in the section header.
- To edit a group's name or color, click its name.
- To reorder groups, drag a row by its grip.
- To archive or delete a group, use its **⋮** menu. You can archive a group once all its tasks are archived.

Archived groups are listed under **Archived**, where their menu has **Restore group**. When you delete a group, its tasks stay, ungrouped, unless you tick **Also delete its *n* tasks** in the confirmation. See [Your groups](/kepler/arranging-your-work#your-groups).

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-groups-settings-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-groups-settings-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Groups section of Settings › Tasks with New group: Checkout (blue, 2 tasks), Search (yellow, 1 task) and Payments (green, 1 task), each with a drag grip and a menu, then Archived with Holiday sale (pink, 1 task) and its menu.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings → Tasks, with 3 groups and 1 archived group.</figcaption>
</figure>

***

---
