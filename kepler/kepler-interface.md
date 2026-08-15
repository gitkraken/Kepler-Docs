---
title: The Kepler Interface
description: Kepler opens on your work — every issue and pull request assigned to you, alongside the tasks you already have running. Learn how to read it and start work from it.
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

Kepler opens on your work. There is one interface rather than a set of views to switch between, and you shape it to fit how you work — see [Arranging Your Work](/kepler/arranging-your-work).

It pulls every issue and pull request assigned to you across your connected trackers and Git hosts into one list, alongside the tasks you already have in motion. Starting work is picking something that's already there rather than describing it from scratch.

The List, Kanban and Console views are gone, and so is the view switcher. The only other places to be are a task's own page, Settings, and remote connections. The top bar keeps one cluster on its trailing edge — **New task**, your setup progress, the remote indicator, **Feedback**, your account, and Settings.

<!-- TODO(screenshot): the Todo segment, wide, with provider tags, status pills, and an Action button legible. -->

***

## Two segments

The control at the top left switches between two views of your work.

| Segment | What it shows |
|---|---|
| **Todo** | Issues and pull requests assigned to you across every connected provider, and not yet picked up |
| **Tasks in progress** | The tasks you already have running in Kepler |

Todo is where a working session starts; **Tasks in progress** is where it leads.

The control lists **Todo** first, but Kepler opens on **Tasks in progress** until you choose otherwise. On a first run that segment has nothing in it, so instead of an empty list you get a welcome panel — **Welcome to Kepler**, a summary of what's already set up, and three ways in: **Start from scratch**, **Start from issues**, and **Start from pull requests**. Todo stays one click away for work that's already assigned to you. Once you have tasks, the same panel returns as the no-tasks empty state, headed **You're all caught up**.

The Todo segment needs at least one connected provider. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

***

## Reading a row

### Todo rows — issues and pull requests

Each row shows, left to right: the **provider**, a **type** badge (**Issue** or **PR**), **your role** on a pull request, the **reference** (issue key or PR number), the **title**, the **repository**, any **session** activity, a **status** pill, the **assignee**, when it last changed, and an **Action** button.

**Your role** on a pull request is one of:

| Role | Meaning |
|---|---|
| **Yours** | You authored the pull request |
| **Review** | You're a reviewer on it |
| **Unattributed** | The provider didn't say |

### Task rows

Task rows show a **Task** badge, the title, the repository, session activity, a status pill, the assignee, and time — with the task's own operations behind the **⋮** menu: **Rename task**, **Archive task** (or **Restore task**, when it already is archived), and **Delete task**.

Task rows deliberately have no reference column and no Action button. A task's reference is the head of its identifier and names nothing you'd recognize, so the cell is given to the title instead. Firing an Action from a *Todo* row is how an untracked issue or pull request becomes a task in the first place; a task that already exists is managed from its **⋮** menu.

### Status

Both segments carry a status pill, but they answer different questions.

| Where | Values | What it means |
|---|---|---|
| **Task rows** | **Exploration**, **In Development**, **In Review**, **Done**, **Archived** | Where the *work* has got to. Kepler derives it from the task's checkouts — uncommitted or unpushed changes, an open pull request, a merged or closed one — except **Archived**, which is your own filing decision |
| **Todo rows** | **Open**, **Draft**, **Merged**, **Closed** | The provider's own state on the issue or pull request |

Beside the pill, one dot per distinct **session state**, with a count — what the *agents* are doing, which is a separate question from where the work stands. The vocabulary is the agent's own: **Spawning**, **Ready**, **Running**, **Idle**, **Unread**, **Waiting**, **Error**, **Terminated**, **Disconnected**. A dormant session draws as an outline rather than a filled dot.

A task is placed at the furthest stage any of its checkouts reached, except **Done**, which needs every one of them done.

***

## Starting work from a row

Click the **Action** button on a Todo row to hand the item to an agent with its context already attached — the repository, the issue body, the branch, the diff. One click, no copy-paste.

The left half of the button runs your preferred Action for that kind of item; the chevron opens the full list. Defaults are **Plan** for issues, **Address Feedback** for pull requests you authored, and **Review** for everyone else's. All of that is editable — see [Actions](/kepler/actions).

- **Click a row** to select it and open the side panel. A plain click replaces whatever was open, except for panels you've pinned.
- **Shift-click** a second row to open both side by side — the panel holds one column per open item, each with its own chat, so you can work several tasks at once without leaving the list.
- **Cmd-click** (**Ctrl-click** on Windows and Linux) to add one row to the open set, or to close it again.
- **Double-click a row** to open the item's full task page. From a Todo row that's the page of the task behind it, so a row with no task yet doesn't respond.

Shift-clicking ranges from your last plain click, the way it does in Finder or VS Code. Up to eight panels can be open at once; opening a ninth evicts the oldest unpinned one. Drag the sash between two columns to resize the one on its left — double-click it, or press Home, to hand the column back to the automatic fill. The list keeps a floor of its own so a wide panel can't crush it, and once the strip outgrows the window it scrolls rather than squeezing the columns below a readable width.

Starting a task from **New task** while you're on the list opens the new task as a panel and leaves the list where it was, rather than throwing you onto its page.

### Pin a panel

A panel is a place you're browsing until you pin it. **Keep this panel open** — the pin in the panel's header — holds it in place, and after that:

- A plain click on a row opens beside your pins instead of replacing them.
- Following a link in **Related** swaps the panel out in place if it isn't pinned, and opens the linked item beside it if it is.
- Switching segments keeps the pinned panels and drops the rest.
- Nothing evicts a pin when the open set is full.

One slot always stays unpinned so browsing never has to evict a pin; once every other panel is pinned, the control reads **Keep one panel unpinned for browsing** and won't take another. **Stop keeping this panel open** releases it.

***

## The side panel

Selecting a row opens a panel beside the list with everything about that item, as a stack of collapsible, resizable sections. A section with nothing behind it isn't drawn at all.

| Section | What's in it | When it's there |
|---|---|---|
| **Summary** | The issue or pull request description | An issue or pull request that has a description. Tasks carry none of their own |
| **Related ({count})** | Linked issues and pull requests, counted in the heading so a folded pane still says how many | There's at least one |
| **Start a session** | A prompt box — *Describe what to work on…* — plus the same Actions | Nothing has run on this item yet |
| **What's running** | The live agent conversation. This is the chat | A session exists. Resizable, but not foldable — it's what the panel is for |
| **Terminals** | Terminal tabs across the task's checkouts | A terminal is open. **New terminal here**, from a checkout in the header, is what creates it |

**Summary** and **Related** are sized to their contents; the chat takes whatever height is left over.

The panel's primary button follows the item rather than the box. On an issue or pull request with nothing running yet, it fires that item's preferred Action — the same default its header's split button offers, so the two halves of one panel can't disagree. On a task panel it reads **Start**, and once a session exists the composer becomes that session's, where it reads **Send**. If the preferred Action is set to **None**, has been deleted, or can't aim at this kind of item, the button falls back to **Start**.

The header carries the item's badges and reference, the pin, **Open full view** for the task's own page, **Open in browser** for the item on its provider, and **Close**. A task's name is editable in place — Enter commits, Escape or clicking away discards. Below it sit the task's checkouts with their line deltas; each one opens a popover with its file count, **Run command**, **Open in…**, and **New terminal here**. An issue or pull request keeps a status line as well, with its provider state, session dots, repository, assignee, and last activity; a task doesn't, because the row you clicked already said all of it.

<!-- TODO(screenshot): the side panel with a session running — Summary, Related, and What's running visible. -->

***

## Empty states

| What you see | What it means |
|---|---|
| **Welcome to Kepler** / **You're all caught up** | Nothing in motion. The welcome panel stands in for the Tasks list, with three ways to start one |
| **No tasks yet** | Nothing in motion, before the welcome panel resolves |
| **No assigned PRs or issues** | Providers are connected, but nothing is assigned to you |
| **Nothing matches these filters** | Your search or filters exclude everything. Use **Clear filters** |
| **Nothing here** | One column of the **Columns** arrangement is empty while its neighbours aren't |
| **No provider integrations** | *Connect a provider to see assigned PRs and issues here.* |
| **Sign in to see your assigned work** | *Connect a GitKraken account to load the PRs and issues assigned to you.* |

---
