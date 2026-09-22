---
title: The Kepler Interface
description: "Kepler opens on your work - every issue and pull request assigned to you, alongside the tasks you already have running. Learn how to read it and start work from it."
product: Kepler
feature: Kepler Interface
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
integrations: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops, jira, linear, trello]
hosted_variant: both
status: GA
last_verified: 2026-09
llms_include: true
tags: [interface, dashboard, todo, tasks, issues, pull-requests, actions, sessions, panel, windows]
taxonomy:
  category: kepler
---
<kbd>Last updated: September 2026</kbd>

This may sound odd, but Kepler "opens" on your work. It offers one interface instead of a set of views to switch between, and you shape it to fit how you work. See [Arranging Your Work](/kepler/arranging-your-work).

Kepler pulls every issue and pull request assigned to you across your connected trackers and Git hosts into one list, alongside the tasks you already have in motion. To start work, pick something that's already there instead of describing it from scratch.

Beyond this list, you'll find a task's own page, Settings, and remote connections. The top bar displays the following at all times:

- New task
- Your setup progress
- The remote indicator
- The window switcher
- Feedback
- Your account
- Settings

On **Windows and Linux** the native title bar is gone and Kepler draws its own. The menu button at the leading edge holds the full application menu — **File**, **Edit**, **View**, **Window**, **Help** — including **Settings**, **Check for Updates…**, and **About**. macOS keeps its native menu bar, and both menus open the same **About Kepler** dialog.

<figure style="text-align:center">
  <a href="/wp-content/uploads/top-tool-bar-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/top-tool-bar-sep-2026.png" class="help-center-img img-bordered" alt="Kepler's top bar showing the New task split button, the window switcher, Feedback, Settings, and account">
  </a>
  <figcaption style="text-align:center; color:#888">The top bar's trailing cluster.</figcaption>
</figure>

The top bar sheds controls as the window narrows based on the room actually available, rather than at fixed widths, so a control disappears only when it genuinely will not fit.

### The window switcher

**Windows** in the top bar lists every open Kepler window and what its agents are doing, so you don't have to go and look. Its trigger carries the reason to: **Windows · {count} waiting elsewhere**, or **{count} running elsewhere**. **This window** marks the one you're in, and **New Window** opens another. The same list is on the tray icon.

Each window's own title leads with the remote it's connected to and how many of its sessions are waiting on you.

### New task

**New task** is a split button. The left half opens the Task Composer; the chevron holds **From an external session**, which starts a task from a conversation you began outside Kepler. See [Create a Task](/kepler/create-task#from-a-session-you-already-started).


***

## Todo, Tasks in progress, and the Agent Graph

The control at the top left switches between 3 views of your work.

<figure style="text-align:center">
  <a href="/wp-content/uploads/todo-task-in-progress-agent-graph-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/todo-task-in-progress-agent-graph-sep-2026.png" class="help-center-img img-bordered" alt="The control at the top left of Kepler, switching between Todo, Tasks in progress, and Agent Graph">
  </a>
  <figcaption style="text-align:center; color:#888">The Todo, Tasks in progress, and Agent Graph switcher.</figcaption>
</figure>

| Segment | What it shows |
|---|---|
| **Todo** | Issues and pull requests assigned to you across every connected provider, and not yet picked up |
| **Tasks in progress** | The tasks you already have running in Kepler |
| **Agent Graph** | A live visualization of every task, session, turn, tool call, and file. See [The Agent Graph](/kepler/agent-graph) |

Todo is where a working session starts; **Tasks in progress** is where it lives while underway. The **Agent Graph** is a segment of its own rather than a way of arranging the list, because it replaces the list instead of laying it out — it scopes over every task, narrowed by your search and filters, and the **Group** and **View** controls step aside while it's on.

When launching the app, Kepler opens on **Tasks in progress**. When you start Kepler for the first time (like on a new machine), you get a **Welcome to Kepler** screen, with a summary of what's already set up and 3 options:

- **Start from scratch**
- **Start from issues**
- **Start from pull requests**


To populate the Todo tab, first connect at least one provider. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

### External sessions

Above the list sits an **External sessions** section: the agent conversations running outside Kepler right now. It's pinned rather than mixed into the groups, because it answers a different question from the rest of the list — *what's running that Kepler didn't start?*

| Part | What it does |
|---|---|
| The header | **{count} live** and **{count} waiting** |
| **Show past sessions** | Extends the section to conversations found on disk, not just ones running now |
| **Show {count} more** | The section keeps itself short; this opens the rest |
| A row | Opens the conversation read-only, where you can fork it, continue it here, or adopt it into a task |

With detection off, the section says so rather than sitting empty — *Sessions you start in your terminal can appear here. Kepler detects them through the agent's hooks.* — with **Turn on detection** beside it. With detection on and nothing to show, it reads **No sessions running outside Kepler right now.**

External sessions stay listed under a filter that has no way to answer for them, rather than vanishing because a facet couldn't classify them.

For what those sessions are and what you can do with one, see [Agent Sessions](/kepler/agent-sessions#sessions-started-outside-kepler).

***

## Reading a row

A row reads differently depending on whether it holds a tracked issue or pull request, or a task you already started. The next 2 sections cover each case.

### Todo rows: issues and pull requests

<figure style="text-align:center">
  <a href="/wp-content/uploads/todo-row-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/todo-row-sep-2026.png" class="help-center-img img-bordered" alt="Two Todo rows for pull requests, one badged Review and one badged Needs my review, each with its repository, status pill, time, and Action button">
  </a>
  <figcaption style="text-align:center; color:#888">A Todo row, left to right.</figcaption>
</figure>

Each row shows, left to right:

- The provider
- A type badge (Issue or PR)
- Your role on a pull request
- The reference (issue key or PR number)
- The title
- The repository
- Any session activity
- A status pill
- The assignee
- When it last changed
- An Action button



**Your role** on a pull request is one of:

| Role | Meaning |
|---|---|
| **Yours** | You authored the pull request |
| **Review** | You're a reviewer on it |
| **Unattributed** | The provider did not say |

### Task rows

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-row-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-row-sep-2026.png" class="help-center-img img-bordered" alt="A Task row with no type badge, showing its title, both repositories it spans, a status pill, a session dot, and time">
  </a>
  <figcaption style="text-align:center; color:#888">A Task row.</figcaption>
</figure>

Task rows show:

- The title
- The repository, or every repository when the task spans several — *app, api +2* beyond two
- Session activity
- A status pill
- The assignee
- Time

Task rows carry no type badge. Everything in **Tasks in progress** is a task, so a chip saying so earned nothing and cost the width the timestamp needed; a narrowing row now drops other cells before it drops the time.

A task that spans several repositories is listed under **each** of them when the list is grouped by repository, rather than under only the first one.

The task's own operations sit behind the **⋮** menu:

- **Rename task**
- **Archive task** (or **Restore task**, when the task is already archived and the list is filtered to **Activity: Archived** — see [Arranging Your Work](/kepler/arranging-your-work))
- **Delete task**

Task rows deliberately have no reference column and no Action button. A task's reference is the head of its identifier and names nothing you'd recognize, so the title takes that cell instead. Firing an Action from a *Todo* row is how an untracked issue or pull request becomes a task in the first place; you manage a task that already exists from its **⋮** menu.

### Status

Both segments carry a status pill, but they answer different questions.

| Where | Values | What it means |
|---|---|---|
| **Task rows** | **Exploration**, **In Development**, **In Review**, **Done**, **Archived** | Where the *work* has got to, derived from the task's checkouts. **In Development** reads the commits ahead of the branch's recorded base; **In Review** needs an open pull request; a dirty working tree withholds **Done**; and a task can reach **Done** from the pull-request links it has stored. The exception is **Archived**, which is your own filing decision |
| **Todo rows** | **Open**, **Draft**, **Merged**, **Closed** | The provider's own state on the issue or pull request |

Beside the pill sits one dot per distinct **session state**, with a count of each.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-status-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-status-aug-2026.png" class="help-center-img img-bordered" alt="A status pill next to session-state dots on a row">
  </a>
  <figcaption style="text-align:center; color:#888">The status pill and session-state dots.</figcaption>
</figure>

This shows what the *agents* are doing, a separate question from where the work stands. The vocabulary is the agent's own:

- **Spawning**
- **Ready**
- **Running**
- **Idle**
- **Unread**
- **Waiting**
- **Error**
- **Terminated**
- **Disconnected**

A dormant session draws as an outline rather than a filled dot.

Kepler places a task at the furthest stage any of its checkouts reached, except **Done**, which needs every one of them done.

***

## Starting work from a row

Click the **Action** button on a Todo row to hand the item to an agent with its context already attached: the repository, the issue body, the branch, and the diff. One click, no copy-paste.

<figure style="text-align:center">
  <a href="/wp-content/uploads/actions-drop-down.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/actions-drop-down.png" class="help-center-img img-bordered" alt="The Action dropdown open on a Todo row, listing Plan, Implement, Review, and Address Feedback">
  </a>
  <figcaption style="text-align:center; color:#888">The Action dropdown, opened from the chevron next to the button.</figcaption>
</figure>

The left half of the button runs your preferred Action for that kind of item; the chevron opens the full list. The defaults are:

- **Plan** for issues
- **Address Feedback** for pull requests you authored
- **Review** for everyone else's

All of these defaults are editable. See [Actions](/kepler/actions).

### Open a panel

<figure style="text-align:center">
  <a href="/wp-content/uploads/open-a-task-panel-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/open-a-task-panel-sep-2026.png" class="help-center-img img-bordered" alt="The side panel open beside the list after clicking a row">
  </a>
  <figcaption style="text-align:center; color:#888">The side panel, opened from a row.</figcaption>
</figure>

- **Click a row** to select it and open the side panel. A plain click replaces whatever was open, except for panels you've pinned.
- **Shift-click** a second row to open both side by side. The panel holds one column per open item, each with its own chat, so you can work several tasks at once without leaving the list.
- **Cmd-click** (**Ctrl-click** on Windows and Linux) to add one row to the open set, or to close it again.
- **Double-click a row** to open the item's full task page. From a Todo row that's the page of the task behind it, so a row with no task yet does not respond.

Shift-clicking ranges from your last plain click, the way it does in Finder or VS Code. You can open up to 8 panels at once. Opening a 9th evicts the oldest unpinned one.

<figure style="text-align:center">
  <a href="/wp-content/uploads/multi-task-panels-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/multi-task-panels-sep-2026.png" class="help-center-img img-bordered" alt="Several task panels open side by side, each with its own chat">
  </a>
  <figcaption style="text-align:center; color:#888">Several panels open side by side, each with its own chat.</figcaption>
</figure>

Drag the sash between two columns to resize the one on its left. Double-click the sash, or press Home, to hand the column back to the automatic fill. The list keeps a minimum width of its own, so a wide panel cannot shrink it too far. Once the panel strip grows wider than the window, it scrolls instead of squeezing the columns below a readable width.

Starting a task from **New task** while you're on the list opens the new task as a panel and leaves the list where it was, rather than throwing you onto its page.

Reorder the open panels from a panel's own **Panel actions** menu (**Move left**, **Move right**) or with **Cmd/Ctrl+Alt+←** and **Cmd/Ctrl+Alt+→**.

When the list reorders under you — a session finishes, a task moves bucket — the row you have selected glides to its new position rather than jumping, so you can see where it went.

### Pin a panel

<figure style="text-align:center">
  <a href="/wp-content/uploads/pin-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/pin-sep-2026.png" class="help-center-img img-bordered" alt="The pin control in a panel's header, keeping the panel open">
  </a>
  <figcaption style="text-align:center; color:#888">The pin in a panel's header.</figcaption>
</figure>

A panel is a place you're browsing until you pin it. **Keep this panel open** (the pin in the panel's header) holds it in place. After that:

- A plain click on a row opens beside your pins instead of replacing them.
- Following a link in **Related** swaps the panel out in place if it is not pinned, and opens the linked item beside it if it is.
- Switching segments keeps the pinned panels and drops the rest.
- Nothing evicts a pin when the open set is full.

One slot always stays unpinned so browsing never has to evict a pin; once every other panel is pinned, the control reads **Keep one panel unpinned for browsing** and will not take another. **Stop keeping this panel open** releases it.

***

## The side panel

Selecting a row opens a panel beside the list with everything about that item, as a stack of collapsible, resizable sections.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-side-panel-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-side-panel-sep-2026.png" class="help-center-img img-bordered" alt="The side panel beside the list, showing a stack of collapsible sections for a selected item">
  </a>
  <figcaption style="text-align:center; color:#888">The side panel, with its stack of collapsible sections.</figcaption>
</figure>

Kepler does not draw a section that has nothing behind it.

| Section | What's in it | When it's there |
|---|---|---|
| **Summary** | The issue or pull request description | An issue or pull request that has a description. Tasks carry none of their own |
| **Related ({count})** | Linked issues and pull requests, counted in the heading so a folded pane still says how many | There's at least one |
| **Start a session** | A prompt box (*Describe what to work on…*) plus the same Actions | Nothing has run on this item yet |
| **What's running** | The live agent conversation. This is the chat | A session exists. Resizable, but not foldable: it's what the panel is for |
| **Plan** | The plan the conversation on screen has proposed | The agent produced one |
| **Changes** | The checkout's commits, working changes, and file diffs | You clicked a worktree chip's branch cell |
| **Terminals** | Terminal tabs across the task's checkouts | A terminal is open. Its **✕** takes the section away without stopping the shells; the chip's Terminal cell and **Cmd/Ctrl+J** are the way back |

Kepler sizes **Summary** and **Related** to their contents and then the chat takes whatever height is left over.

For unstarted issues or PRs, the side panel's primary button follows that item's preferred Action (Plan, Implement vs Review, Address Feedback). 

In the side panel for a Task, the primary button reads **Start**, and once a session exists the composer becomes that session's chat, where it reads **Send**. If the preferred Action is **None**, no longer exists, or cannot aim at this kind of item, the button falls back to **Start**.

The header carries:

<figure style="text-align:center">
  <a href="/wp-content/uploads/issue-header-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/issue-header-sep-2026.png" class="help-center-img img-bordered" alt="The side panel's header, showing badges, the reference, the pin, and the header controls">
  </a>
  <figcaption style="text-align:center; color:#888">The side panel's header.</figcaption>
</figure>

- The item's badges and reference
- The pin
- **Open full view**, for the task's own page
- **Open in browser**, for the item on its provider
- **Close**

You can edit a task's name in place. Enter commits the change; Escape or clicking away discards it.

An archived task is badged as such in both its preview and its detail header, so you can't mistake a filed task for a live one.

### The worktree chip

Below the header sits one line per checkout: a **status chip** on the left and an **actions chip** pinned to the right edge, so several checkouts line up as a column.

<figure style="text-align:center">
  <a href="/wp-content/uploads/line-deltas-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/line-deltas-sep-2026.png" class="help-center-img img-bordered" alt="A checkout's branch cell below the header, with its tooltip open showing the repository, branch, and change counts">
  </a>
  <figcaption style="text-align:center; color:#888">A checkout's chip, below the header.</figcaption>
</figure>

| Cell | What it shows | What clicking it does |
|---|---|---|
| **Branch** | The branch name and what it adds against its base: commits, files, and the line delta, with a dot when some of it is still uncommitted | Opens the **Changes** section on that checkout |
| **Upstream** | Behind then ahead, or **Publish** when there is no upstream at all | Runs the verb the counts call for. The chevron offers only that verb plus **Fetch** — **Pull** when behind, **Push** when ahead, and **Force push** behind a confirmation only when the branch has genuinely diverged |
| **Terminal** | How many shells are running in this checkout | Brings the most recent one forward, or spawns one when there is none |
| **Open in** | Your default editor | Opens the checkout there. The chevron lists the rest |
| **Run** | The repository's commands | Runs the one you pick |

The branch cell's tooltip carries the repository, the path, and the change counts broken into their committed and uncommitted halves — because only one of those two halves can still be lost.

The chip sheds labels as the panel narrows by measuring the room it actually has, and truncates the branch name only once there is nothing else left to shed.

The terminal strip's **+** becomes a chooser listing the task's checkouts by branch when the task has more than one.

An issue or pull request keeps a status line as well, with its provider state, session dots, repository, assignee, and last activity. A task does not, because the row you clicked already showed that information.

***

## Back and forward

Back follows one rule: **it leaves the place or mode you're in.** It never retraces a search you typed, a filter you set, or a change of view mode, so pressing it after narrowing the list takes you out of the list rather than walking back through every keystroke.

| | Mac | Windows / Linux |
|---|---|---|
| **Back** | ⌘ [ | Alt + ← |
| **Forward** | ⌘ ] | Alt + → |

Each set of open panels gets its own history entry, so Back closes the set you just opened rather than the whole visit. Moving between Settings sub-pages replaces a single entry, so Back from Settings returns you to what you were doing before you opened it.

***

## Empty states

| What you see | What it means |
|---|---|
| **Welcome to Kepler** / **You're all caught up** | Nothing in motion. The welcome panel stands in for the Tasks list, with 3 ways to start one |
| **No tasks yet** | Nothing in motion, before the welcome panel resolves |
| **No assigned PRs or issues** | Providers are connected, but nothing is assigned to you |
| **Nothing matches these filters** | Your search or filters exclude everything. Use **Clear filters** |
| **Nothing here** | One column of the **Columns** arrangement is empty while its neighbours are not |
| **No provider integrations** | *Connect a provider to see assigned PRs and issues here.* |
| **Sign in to see your assigned work** | *Connect a GitKraken account to load the PRs and issues assigned to you.* |

---
