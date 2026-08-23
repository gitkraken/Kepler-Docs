---
title: The Kepler Interface
description: Kepler opens on your work: every issue and pull request assigned to you, alongside the tasks you already have running. Learn how to read it and start work from it.
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
last_verified: 2026-08
llms_include: true
tags: [interface, todo, tasks, issues, pull-requests, actions, sessions, panel]
taxonomy:
  category: kepler
---
<kbd>Last updated: August 2026</kbd>

This may sound odd, but Kepler "opens" on your work. It offers one interface instead of a set of views to switch between, and you shape it to fit how you work. See [Arranging Your Work](/kepler/arranging-your-work).

Kepler pulls every issue and pull request assigned to you across your connected trackers and Git hosts into one list, alongside the tasks you already have in motion. To start work, pick something that's already there instead of describing it from scratch.

Beyond this list, you'll find a task's own page, Settings, and remote connections. The top bar displays the following at all times:

- New task
- Your setup progress
- The remote indicator
- Feedback
- Your account
- Settings

<figure>
  <img src="/wp-content/uploads/top-tool-bar-aug-2026.png" class="help-center-img img-bordered" alt="Kepler's top bar showing New task, setup progress, the remote indicator, Feedback, account, and Settings">
  <figcaption style="text-align:center; color:#888">The top bar's trailing cluster.</figcaption>
</figure>


***

## Todo + Tasks in progress

The control at the top left switches between 2 views of your work.

<figure>
  <img src="/wp-content/uploads/todo-task-in-progress-aug-2026.png" class="help-center-img img-bordered" alt="The control at the top left of Kepler, switching between Todo and Tasks in progress">
  <figcaption style="text-align:center; color:#888">The Todo and Tasks in progress switcher.</figcaption>
</figure>

| Segment | What it shows |
|---|---|
| **Todo** | Issues and pull requests assigned to you across every connected provider, and not yet picked up |
| **Tasks in progress** | The tasks you already have running in Kepler |

Todo is where a working session starts; **Tasks in progress** is where it lives while underway.

When launching the app, Kepler opens on **Tasks in progress**. When you start Kepler for the first time (like on a new machine), you get a **Welcome to Kepler** screen, with a summary of what's already set up and 3 options:

- **Start from scratch**
- **Start from issues**
- **Start from pull requests**


To populate the Todo tab, first connect at least one provider. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

***

## Reading a row

A row reads differently depending on whether it holds a tracked issue or pull request, or a task you already started. The next 2 sections cover each case.

### Todo rows: issues and pull requests

<figure>
  <img src="/wp-content/uploads/todo-row-aug-2026.png" class="help-center-img img-bordered" alt="A Todo row showing the provider, type badge, role, reference, title, repository, session activity, status pill, assignee, and Action button">
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

<figure>
  <img src="/wp-content/uploads/task-row-aug-2026.png" class="help-center-img img-bordered" alt="A Task row showing the Task badge, title, repository, session activity, status pill, assignee, and time">
  <figcaption style="text-align:center; color:#888">A Task row.</figcaption>
</figure>

Task rows show:

- A **Task** badge
- The title
- The repository
- Session activity
- A status pill
- The assignee
- Time

The task's own operations sit behind the **⋮** menu:

- **Rename task**
- **Archive task** (or **Restore task**, when the task is already archived)
- **Delete task**

Task rows deliberately have no reference column and no Action button. A task's reference is the head of its identifier and names nothing you'd recognize, so the title takes that cell instead. Firing an Action from a *Todo* row is how an untracked issue or pull request becomes a task in the first place; you manage a task that already exists from its **⋮** menu.

### Status

Both segments carry a status pill, but they answer different questions.

| Where | Values | What it means |
|---|---|---|
| **Task rows** | **Exploration**, **In Development**, **In Review**, **Done**, **Archived** | Where the *work* has got to. Kepler derives it from the task's checkouts: uncommitted or unpushed changes, an open pull request, or a merged or closed one. The exception is **Archived**, which is your own filing decision |
| **Todo rows** | **Open**, **Draft**, **Merged**, **Closed** | The provider's own state on the issue or pull request |

Beside the pill sits one dot per distinct **session state**, with a count of each.

<figure>
  <img src="/wp-content/uploads/task-status-aug-2026.png" class="help-center-img img-bordered" alt="A status pill next to session-state dots on a row">
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

<figure>
  <img src="/wp-content/uploads/actions-drop-down.png" class="help-center-img img-bordered" alt="The Action dropdown open on a Todo row, listing Plan, Implement, Review, and Address Feedback">
  <figcaption style="text-align:center; color:#888">The Action dropdown, opened from the chevron next to the button.</figcaption>
</figure>

The left half of the button runs your preferred Action for that kind of item; the chevron opens the full list. The defaults are:

- **Plan** for issues
- **Address Feedback** for pull requests you authored
- **Review** for everyone else's

All of these defaults are editable. See [Actions](/kepler/actions).

### Open a panel

<figure>
  <img src="/wp-content/uploads/open-a-task-panel-aug-2026.png" class="help-center-img img-bordered" alt="The side panel open beside the list after clicking a row">
  <figcaption style="text-align:center; color:#888">The side panel, opened from a row.</figcaption>
</figure>

- **Click a row** to select it and open the side panel. A plain click replaces whatever was open, except for panels you've pinned.
- **Shift-click** a second row to open both side by side. The panel holds one column per open item, each with its own chat, so you can work several tasks at once without leaving the list.
- **Cmd-click** (**Ctrl-click** on Windows and Linux) to add one row to the open set, or to close it again.
- **Double-click a row** to open the item's full task page. From a Todo row that's the page of the task behind it, so a row with no task yet does not respond.

Shift-clicking ranges from your last plain click, the way it does in Finder or VS Code. You can open up to 8 panels at once. Opening a 9th evicts the oldest unpinned one.

<figure>
  <img src="/wp-content/uploads/multi-task-panels-aug-2026.png" class="help-center-img img-bordered" alt="Several task panels open side by side, each with its own chat">
  <figcaption style="text-align:center; color:#888">Several panels open side by side, each with its own chat.</figcaption>
</figure>

Drag the sash between two columns to resize the one on its left. Double-click the sash, or press Home, to hand the column back to the automatic fill. The list keeps a minimum width of its own, so a wide panel cannot shrink it too far. Once the panel strip grows wider than the window, it scrolls instead of squeezing the columns below a readable width.

Starting a task from **New task** while you're on the list opens the new task as a panel and leaves the list where it was, rather than throwing you onto its page.

### Pin a panel

<figure>
  <img src="/wp-content/uploads/pin-aug-2026.png" class="help-center-img img-bordered" alt="The pin control in a panel's header, keeping the panel open">
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

<figure>
  <img src="/wp-content/uploads/task-side-panel-aug-2026.png" class="help-center-img img-bordered" alt="The side panel beside the list, showing a stack of collapsible sections for a selected item">
  <figcaption style="text-align:center; color:#888">The side panel, with its stack of collapsible sections.</figcaption>
</figure>

Kepler does not draw a section that has nothing behind it.

| Section | What's in it | When it's there |
|---|---|---|
| **Summary** | The issue or pull request description | An issue or pull request that has a description. Tasks carry none of their own |
| **Related ({count})** | Linked issues and pull requests, counted in the heading so a folded pane still says how many | There's at least one |
| **Start a session** | A prompt box (*Describe what to work on…*) plus the same Actions | Nothing has run on this item yet |
| **What's running** | The live agent conversation. This is the chat | A session exists. Resizable, but not foldable: it's what the panel is for |
| **Terminals** | Terminal tabs across the task's checkouts | A terminal is open. **New terminal here**, from a checkout in the header, is what creates it |

Kepler sizes **Summary** and **Related** to their contents and then the chat takes whatever height is left over.

For unstarted issues or PRs, the side panel's primary button follows that item's preferred Action (Plan, Implement vs Review, Address Feedback). 

In the side panel for a Task, the primary button reads **Start**, and once a session exists the composer becomes that session's chat, where it reads **Send**. If the preferred Action is **None**, no longer exists, or cannot aim at this kind of item, the button falls back to **Start**.

The header carries:

<figure>
  <img src="/wp-content/uploads/issue-header-aug-2026.png" class="help-center-img img-bordered" alt="The side panel's header, showing badges, the reference, the pin, and the header controls">
  <figcaption style="text-align:center; color:#888">The side panel's header.</figcaption>
</figure>

- The item's badges and reference
- The pin
- **Open full view**, for the task's own page
- **Open in browser**, for the item on its provider
- **Close**

You can edit a task's name in place. Enter commits the change; Escape or clicking away discards it.

Below the header sit the task's checkouts with their line deltas. Each one opens a popover with its file count, **Run command**, **Open in…**, and **New terminal here**.

<figure>
  <img src="/wp-content/uploads/line-deltas-aug-2026.png" class="help-center-img img-bordered" alt="A task's checkouts below the header, each showing its line deltas">
  <figcaption style="text-align:center; color:#888">A checkout's line deltas, below the header.</figcaption>
</figure>

An issue or pull request keeps a status line as well, with its provider state, session dots, repository, assignee, and last activity. A task does not, because the row you clicked already showed that information.

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
