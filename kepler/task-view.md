---
title: The Task View
description: Open a Task to see its resources, agent sessions, and changes side by side. Learn the rail, the columns, split panes, and how to start sessions and terminals.
product: Kepler
feature: Tasks
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode]
hosted_variant: both
status: GA
last_verified: 2026-08
llms_include: true
tags: [tasks, task-view, sessions, terminals, worktrees, resources, tabs, split-panes]
taxonomy:
  category: kepler
---
<kbd>Last updated: August 2026</kbd>

Opening a Task gives you its own screen: everything attached to it on the left, and the sessions, working copies, and details you're looking at on the right.

Get here by double-clicking a row in [the Kepler interface](/kepler/kepler-interface), or by clicking **Open full view** in the side panel. For what a Task is and what can be attached to one, see [Tasks and Resources](/kepler/tasks-and-resources).

<figure>
  <a href="/wp-content/uploads/full-task-view-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/full-task-view-aug-2026.png" class="help-center-img img-bordered" alt="The task view with the rail on the left, listing Sessions, Changes, Folders, Pull requests, Links, and Notes, and a session open on the right with tool-call approval prompts">
  </a>
  <figcaption style="text-align:center; color:#888">The task view: the rail on the left, a session open on the right.</figcaption>
</figure>

***

## The header

<figure>
  <a href="/wp-content/uploads/task-header-3-elements-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-header-3-elements-aug-2026.png" class="help-center-img img-bordered" alt="The task header, showing the Dashboard back button, the task switcher, and the task actions menu">
  </a>
  <figcaption style="text-align:center; color:#888">The task header's three elements.</figcaption>
</figure>

The task header has 3 key elements:

- **← Dashboard** (the back button, labelled that in the app) returns you to the list exactly as you left it: same segment, grouping, filters, and selection.
- **The task switcher** jumps to another Task without going back first. It searches as you type, and each row carries the same session status dots a row does.
- **⋮ Task actions** holds **Rename task**, **Archive task**, and **Delete task**. On an already-archived Task, **Restore task** replaces **Archive task** and puts the Task straight back with no confirmation.

**Rename task** opens a dialog with the name in an editable field. The field carries an **Auto-name** button — *Suggest a name from the task's prompt and resources* — which fills the field with a suggestion for you to accept or edit. It never renames on its own; the dialog's **Rename** button is what applies it.

***

## The rail

The left rail lists everything attached to the Task, grouped by kind:

**Sessions · Terminals · Changes · Folders · Files · Pull requests · Issues · Links · Notes · Attachments**

<figure>
  <a href="/wp-content/uploads/task-rail-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-rail-aug-2026.png" class="help-center-img img-bordered" alt="The task view's left rail, showing Sessions, Changes, Folders, Pull requests, Links, and Notes groups, with Add resource at the bottom">
  </a>
  <figcaption style="text-align:center; color:#888">The rail, grouped by resource kind.</figcaption>
</figure>

The worktree group is called **Changes**. Its rows carry each checkout's line count and open its diff review, so the header names what you go there for rather than the git object behind it.

**Sessions** always stays, even on a Task that has none, so you always have a way to start the first one. Every other group appears only once it has something in it.

- **Add resource** sits at the bottom of the rail and opens the **Add resources** dialog.
- The **+** on a group header adds straight into that group: **Add issues**, **Add notes**, and so on. On **Changes** it reads **Add worktree**, because that's what actually lands there. On **Sessions** the **+** is **New session** instead.
- Every session that isn't live (archived ones, and ones that disconnected or terminated) collects under a **{count} archived** fold beneath the live ones. It starts collapsed. Clicking an archived session brings it back and opens it in one gesture; **Restore** in its menu does the same.

### What a row shows

Both of a row's lines truncate at rail width. Every row has a hover tip carrying its full name, plus the facts the row's lines had no room for:

<figure>
  <a href="/wp-content/uploads/rail-hovers-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/rail-hovers-aug-2026.png" class="help-center-img img-bordered" alt="A truncated Changes row with its hover tip open, showing the full name, repository, base branch, and path">
  </a>
  <figcaption style="text-align:center; color:#888">A row's hover tip, showing what its truncated lines couldn't.</figcaption>
</figure>

- **Path**
- **Repository**
- **Base**
- **Agent**
- **Account**
- **Status**
- Flags such as **Repository's main worktree** or **Gone from disk**

- A **Changes** row's subtitle is its repository and base branch, followed by the checkout's added and removed line counts.
- A **session** row leads with its state, and names which **Account** it runs under once a harness has more than one configured: the provider logo plus an ordinal, on the row, its tab, and its collapsed strip alike.

The end of the subtitle line carries the row's controls, always visible rather than revealed on hover:

| Row | Controls |
|---|---|
| **Folder** | **Open in…** |
| **Worktree** (on disk) | **Open in…**, **New terminal here**, and the run-a-command control |
| **Session** | Show or hide the [Agent Graph](/kepler/agent-graph) for that session alone, and **Archive** |

### The row menu

Right-click any row. Every row opens with **Open**, **Open in new tab**, and **Open to the side**.

<figure>
  <a href="/wp-content/uploads/rail-row-menu-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/rail-row-menu-aug-2026.png" class="help-center-img img-bordered" alt="A worktree row's right-click menu, listing Open, session and terminal actions, Open in, copy actions, and Detach">
  </a>
  <figcaption style="text-align:center; color:#888">A worktree row's context menu.</figcaption>
</figure>

| On | Also holds |
|---|---|
| A worktree that's on disk | **New session here**, **New terminal here**, **Run command here**, **Open in…**, **Open remote repo**, **Copy path**, **Copy branch name**, **Copy remote URL** |
| A folder | **Open in…**, **Copy path** |
| A file | **Copy path** |
| A pull request or issue | **Open in browser**, **Copy link**, **Copy title**, **Copy number**, and **Copy branch name** on a pull request |

**Run command here** lists the repository's commands (configured in **Settings → Repositories**) and runs the one you pick in that worktree, revealing its terminal in place without taking your focus. A repository with none reads **No commands yet**, and the submenu ends with **Create command…** so you can add one from where you noticed you wanted it.

The last entry is how the row leaves the Task, and it differs by kind: **Detach** for a resource, **Archive** for a session, **Close terminal** for a terminal.

***

## The columns

<figure>
  <a href="/wp-content/uploads/task-columns-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-columns-aug-2026.png" class="help-center-img img-bordered" alt="The three content columns side by side: a session conversation, a worktree's changes, and a resource's details">
  </a>
  <figcaption style="text-align:center; color:#888">The three content columns: Sessions, Changes, and Resources.</figcaption>
</figure>

The content area is fixed slots, not free-form panes. A rail row's kind decides which slot it opens into, so a session never lands next to a note and you never have to remember where you put something.

| Column | What opens here |
|---|---|
| **Sessions** | Agent conversations |
| **Changes** | A worktree (its commits, its changed files, and the diff) with **Terminals** stacked underneath it in the same column |
| **Resources** | Folders, files, pull requests, issues, links, notes, attachments |

Terminals get a slot of their own rather than sharing the worktree's. A terminal is a view *onto* a checkout, so the two belong on screen at the same time: opening a shell no longer evicts the changes you were reading. When only one of the two halves has something open, it takes the whole height.

Every boundary is a draggable sash, and the size you drag it to persists. The three content columns share whatever the rail leaves: equally until you drag one, and in the ratio you set from then on. Kepler keeps the ratios as proportions, not pixels, so they survive a window resize and a column opening or closing.

Click a rail row to open it in its slot. Double-click to pin it. A slot with nothing open renders no column at all, and the others take its space.

The page opens on a conversation and on the checkout that conversation is working in, inferred from the session or terminal it auto-opened, so **Changes** isn't an empty column you have to go fill on every visit.

Close a column with the arrow icon on its strip. Closing a column doesn't detach anything, and it doesn't stop or archive a session; the rail still has it.

<figure>
  <a href="/wp-content/uploads/close-column-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/close-column-aug-2026.png" class="help-center-img img-bordered" alt="The close-column arrow icon on a column's strip, with its tooltip reading Close strip">
  </a>
  <figcaption style="text-align:center; color:#888">The arrow icon that closes a column.</figcaption>
</figure>

### Split panes

**Cmd-click a rail row (Ctrl-click on Windows and Linux) to open it beside what's already there** rather than in place of it. **Open to the side** in the row's menu is the same gesture without the modifier. The new pane lands in that row's own slot, so a session splits the Sessions column and a worktree splits the Changes column.

**Shift-click opens a range.** This is how you watch several agents at once: shift-click from your last plain click through another session and the whole run opens side by side in the Sessions column, so you can read them in parallel and answer whichever needs you. The anchor is your last plain click and a shift-click doesn't move it, the way it works in Finder or VS Code. With no prior click in that group, the range starts from the row already on screen.

A plain click while a slot is split replaces only the focused pane and leaves the others alone.

### Tabs

By default each column shows one thing at a time and you switch by picking a different row in the rail.

Turn on **Show tabs on the task page** in **Settings → General** to keep several sessions, worktrees, or resources open as tabs in the same column instead. **Open in new tab** on a rail row then adds to the strip rather than replacing what's there.

<figure>
  <a href="/wp-content/uploads/show-tabs-on-task-page-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/show-tabs-on-task-page-aug-2026.png" class="help-center-img img-bordered" alt="The Show tabs on the task page setting, checked, in Settings → General">
  </a>
  <figcaption style="text-align:center; color:#888">The Show tabs on the task page setting, in Settings → General.</figcaption>
</figure>

A split is independent of this setting. Turning tabs off doesn't fold side-by-side panes back into one, and a Cmd-click still splits with tabs off. That's the whole point of the gesture.

**Closing a session's tab only closes the tab.** It doesn't archive the session or stop the agent. The session stays in the rail, and archiving is a separate action there. Those are two different intentions and Kepler keeps them separate.

***

## Starting a session

**New session** starts an agent in one of the Task's working directories.

| Where it can run | When you'd use it |
|---|---|
| **Global** | *Runs in the task folder*: the Task's own folder rather than any checkout, for work that isn't about one repository. Always first in the menu |
| A specific **worktree** or **folder** | The normal case: the agent works in that checkout |
| **In every worktree or folder** | Fan the same starting instruction across all of them at once, one session each |

With a single place to run, the menu lists the agents directly instead of asking twice. If the Task has nowhere to run yet, Kepler says so: **Attach a worktree or folder to start a session in.** Attach one from the rail and the option appears. If no agents are connected you'll see **No agents available**. Connect one in [Agent Integrations](/kepler/agent-integrations).

To fire a preconfigured prompt instead of typing one, open the chevron beside the session composer's **Send** button and pick an Action. Anything you typed rides along as a refinement. See [Actions](/kepler/actions).

### Terminals

**New terminal here** on a worktree row opens a shell in that checkout, in the **Terminals** slot directly under the worktree it belongs to. Running one of the repository's commands from the row does the same thing, and reveals the terminal it spawned without taking your focus.

<figure>
  <a href="/wp-content/uploads/new-terminal-here-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-terminal-here-aug-2026.png" class="help-center-img img-bordered" alt="A worktree row's context menu with New terminal here highlighted">
  </a>
  <figcaption style="text-align:center; color:#888">New terminal here, on a worktree row's context menu.</figcaption>
</figure>

***

## What each resource pane shows

| Resource | Details |
|---|---|
| **Worktree**, on disk | Its commits, its changed files, and the diff. The same review you'd get anywhere else in Kepler. See [Review Changes](/kepler/review-changes) |
| **Worktree**, missing | A metadata card instead: **Current branch**, **Base branch**, and the **Recorded path**, flagged **not on disk** or **gone** when it's been removed outside Kepler |
| **Folder** / **File** | Path, plus an editable name and description |
| **Pull request** / **Issue** | Author, assignee, and status. *Full description lives in the provider — open the link above to view it.* |
| **Link** | Last synced time, or **not synced** |
| **Note** | The note itself, editable in place |

---
