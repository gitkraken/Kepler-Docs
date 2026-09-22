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
last_verified: 2026-09
llms_include: true
tags: [tasks, task-page, sessions, terminals, worktrees, resources, tabs, split-panes, drawer]
taxonomy:
  category: kepler
---
<kbd>Last updated: September 2026</kbd>

Opening a Task gives you its own screen — the **task page** — with everything attached to it on the left, and the sessions, working copies, and details you're looking at on the right.

Get here by double-clicking a row in [the Kepler interface](/kepler/kepler-interface), or by clicking **Open full view** in the side panel. For what a Task is and what can be attached to one, see [Tasks and Resources](/kepler/tasks-and-resources).

<figure style="text-align:center">
  <a href="/wp-content/uploads/full-task-view-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/full-task-view-aug-2026.png" class="help-center-img img-bordered" alt="The task view with the rail on the left, listing Sessions, Changes, Folders, Pull requests, Links, and Notes, and a session open on the right with tool-call approval prompts">
  </a>
  <figcaption style="text-align:center; color:#888">The task view: the rail on the left, a session open on the right.</figcaption>
</figure>

***

## The header

<figure style="text-align:center">
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

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-rail-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-rail-aug-2026.png" class="help-center-img img-bordered" alt="The task view's left rail, showing Sessions, Changes, Folders, Pull requests, Links, and Notes groups, with Add resource at the bottom">
  </a>
  <figcaption style="text-align:center; color:#888">The rail, grouped by resource kind.</figcaption>
</figure>

The worktree group is called **Changes**. Its rows carry each checkout's real state and open its diff review, so the header names what you go there for rather than the git object behind it.

**Sessions** always stays, even on a Task that has none, so you always have a way to start the first one. Every other group appears only once it has something in it.

**The rail can be put away.** **Hide context panel** collapses it and hands the width to the columns; **Show context panel** brings it back. While it's hidden the control carries the task's own session status, so a session that needs you is still visible from a collapsed rail. Drag its edge to resize it.

- **Add resource** sits at the bottom of the rail and opens the **Add resources** dialog.
- The **+** on a group header adds straight into that group: **Add issues**, **Add notes**, and so on. On **Changes** it reads **Add worktree**, because that's what actually lands there. On **Sessions** the **+** is **New session** instead.
- Every session that isn't live (archived ones, and ones that disconnected or terminated) collects under a **{count} archived** fold beneath the live ones. It starts collapsed. Clicking an archived session brings it back and opens it in one gesture; **Restore** in its menu does the same.

### What a row shows

Both of a row's lines truncate at rail width. Every row has a hover tip carrying its full name, plus the facts the row's lines had no room for:

<figure style="text-align:center">
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

- A **Changes** row's subtitle is a run of glyph-and-number chips reading the checkout's real state: uncommitted files, commits on the branch, behind and ahead of the upstream, behind the merge target, with conflicts and an unpublished branch drawn as glyphs alone. A checkout with nothing to report reads **Up to date**; one that has been deleted says so. Its tooltip is a two-column table of the same facts — the branch, the repository, the path, the working tree, the commits, the upstream and the merge target — with the numbers aligned so they never wrap.
- A **session** row leads with its state, and names which **Account** it runs under once a harness has more than one configured: the provider logo plus an ordinal, on the row, its tab, and its collapsed strip alike.

The end of the subtitle line carries the row's controls, always visible rather than revealed on hover:

| Row | Controls |
|---|---|
| **Folder** | **Open in…** |
| **Worktree** (on disk) | **Open in…** and the run-a-command control. The shell button stays out — the row's menu and **Cmd/Ctrl+J** both offer it, and the line has no room for a third control |
| **Session** | Show or hide the [Agent Graph](/kepler/agent-graph) for that session alone, and **Archive** |

Every rail row draws a selected fill when it's the one on screen, and the column you last pressed, focused, or opened from the rail carries an inset ring — the wide layout never moves focus on its own, so something has to say where it is.

### The row menu

Right-click any row. Every row opens with **Open**, **Open in new tab**, and **Open to the side**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/rail-row-menu-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/rail-row-menu-aug-2026.png" class="help-center-img img-bordered" alt="A worktree row's right-click menu, listing Open, session and terminal actions, Open in, copy actions, and Detach">
  </a>
  <figcaption style="text-align:center; color:#888">A worktree row's context menu.</figcaption>
</figure>

| On | Also holds |
|---|---|
| A worktree that's on disk | **New session here**, **New terminal here**, **Run command here**, **Open in…**, **Open remote repo**, **Rename branch**, **Copy path**, **Copy branch name**, **Copy remote URL** |
| A folder | **Open in…**, **Copy path** |
| A file | **Copy path** |
| A pull request or issue | **Open in browser**, **Copy link**, **Copy title**, **Copy number**, and **Copy branch name** on a pull request |

**Run command here** — and the **Run a command** control on the row and the worktree's own strip — lists the repository's commands (configured in **Settings → Repos & Folders**) and runs the one you pick in that worktree, revealing its terminal in the drawer without taking your focus. A repository with none reads **No commands yet**, and the menu ends with **Create command…** so you can add one from where you noticed you wanted it, plus **Manage commands…**, which deep-links to that repository's own settings.

**Open in** works the same way, with your default editor hoisted above the list rather than buried in it.

**Picking an editor or a command no longer silently makes it your default.** Each row carries its own set/unset toggle at its trailing edge, reachable from the keyboard, so choosing something once and pinning it are two separate decisions.

**Rename branch** opens a dialog with the branch's own name field and **Also rename remote branch**, which renames the branch on its remote too rather than just locally.

**Option/Alt-click** a resource row to open it in your browser instead of in Kepler.

The last entry is how the row leaves the Task, and it differs by kind: **Detach** for a resource, **Archive** for a session, **Close terminal** for a terminal.

***

## The columns

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-columns-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-columns-sep-2026.png" class="help-center-img img-bordered" alt="The three content columns side by side: a session conversation, a worktree's changes, and a resource's details">
  </a>
  <figcaption style="text-align:center; color:#888">The three content columns: Sessions, Changes, and Resources.</figcaption>
</figure>

The content area is fixed slots, not free-form panes. A rail row's kind decides which slot it opens into, so a session never lands next to a note and you never have to remember where you put something.

| Column | What opens here |
|---|---|
| **Sessions** | Agent conversations, whether they run as rich chat or in a terminal |
| **Changes** | A worktree: a strip of verbs over its changed files. See [Review Changes](/kepler/review-changes) |
| **Resources** | Folders, files, pull requests, issues, links, notes, attachments |

**Terminals are no longer a column.** They live in a drawer beneath all three, covered below, so opening a shell never evicts the changes or the conversation you were reading.

Every boundary is a draggable sash, and the size you drag it to persists. The three content columns share whatever the rail leaves: equally until you drag one, and in the ratio you set from then on. Kepler keeps the ratios as proportions, not pixels, so they survive a window resize and a column opening or closing.

Click a rail row to open it in its slot. Double-click to pin it. A slot with nothing open renders no column at all, and the others take its space.

The page opens on a conversation and on the checkout that conversation is working in, inferred from the session or terminal it auto-opened, so **Changes** isn't an empty column you have to go fill on every visit.

Close a column with the **X** on its strip, labeled **Close panel**. Closing a column doesn't detach anything, and it doesn't stop or archive a session; the rail still has it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/close-column-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/close-column-sep-2026.png" class="help-center-img img-bordered" alt="The Close panel (X) control on a column's strip, with its tooltip reading Close panel">
  </a>
  <figcaption style="text-align:center; color:#888">The Close panel control, on a column's strip.</figcaption>
</figure>

### Tabs or splits

**Show tabs on the task page** in **Settings → General** decides which of two shapes a column takes. Both are supported; neither is a subset of the other.

| Setting | What a column does | How you get a second thing on screen |
|---|---|---|
| **Off** (the default) | Shows one thing at a time | **Split it.** Cmd-click a rail row (Ctrl-click on Windows and Linux), or **Open to the side** in its menu |
| **On** | Keeps several things open as tabs, mirroring the rail | **Open in new tab** on a rail row, or a multi-select, which opens as tabs |

<figure style="text-align:center">
  <a href="/wp-content/uploads/show-tabs-on-task-page-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/show-tabs-on-task-page-aug-2026.png" class="help-center-img img-bordered" alt="The Show tabs on the task page setting, checked, in Settings → General">
  </a>
  <figcaption style="text-align:center; color:#888">The Show tabs on the task page setting, in Settings → General.</figcaption>
</figure>

**With tabs on, a column's tab strip mirrors the rail**, so the two never disagree about what's open. Clicking the rail row of the card already showing hides its pane; **Open beside** splits it.

**Splitting is a tabs-off gesture.** Turning tabs off doesn't fold side-by-side panes back into one.

**Shift-click opens a range.** This is how you watch several agents at once: shift-click from your last plain click through another session and the whole run opens side by side in the Sessions column, so you can read them in parallel and answer whichever needs you. The anchor is your last plain click and a shift-click doesn't move it, the way it works in Finder or VS Code. With no prior click in that group, the range starts from the row already on screen.

A plain click while a slot is split replaces only the focused pane and leaves the others alone.

### What a tab's close control does

A tab's close control is named and drawn for **what it is closing**, rather than being three identical **×**s that do different things.

| Tab | Its control | What happens |
|---|---|---|
| **Session** (Kepler's own) | **Archive session** | Stops the agent, saves the conversation, and files the session under the rail's archived fold |
| **Session** (external, or a preview) | **Close tab** | Hides the pane. The conversation is untouched |
| **Terminal** | **Close terminal** | Runs the busy check and confirms before stopping anything. A terminal already closing offers only **Force close** |
| **Worktree** or **resource** | **Close tab** | Hides the pane. Nothing is detached |

**Cmd/Ctrl+W** does whatever the visible tab's own control does.

Closing a *column* — the **Close panel** control on its strip — is always just a view change. It detaches nothing, archives nothing, and stops nothing; the rail still has it all.

### Reordering

| Gesture | What it moves |
|---|---|
| **Move tab left** / **Move tab right**, in a tab's **Tab actions** menu | That tab |
| **Cmd/Ctrl+Alt+[** and **Cmd/Ctrl+Alt+]** | The focused tab |
| **Cmd/Ctrl+Alt+←** and **Cmd/Ctrl+Alt+→** | A Dashboard preview panel |

***

## Starting a session

**New session** starts an agent in one of the Task's working directories.

| Where it can run | When you'd use it |
|---|---|
| **Global** | *Runs in the task folder*: the Task's own folder rather than any checkout, for work that isn't about one repository. Always first in the menu |
| A specific **worktree** or **folder** | The normal case: the agent works in that checkout |
| **In every worktree or folder** | Fan the same starting instruction across all of them at once, one session each |

With a single place to run, the menu lists the agents directly instead of asking twice. If the Task has nowhere to run yet, Kepler says so: **Attach a worktree or folder to start a session in.** Attach one from the rail and the option appears. If no agents are connected you'll see **No agents available**. Connect one in [Agent Integrations](/kepler/agent-integrations).

**Each agent row can start either run mode.** The row itself launches that agent in its default mode; the trailing button on the row starts the other one — **Start in Terminal**, or **Start in Rich chat** on an agent that already defaults to Terminal. An agent that offers only one mode shows no second control. See [Agent Sessions](/kepler/agent-sessions#how-a-session-runs).

To fire a preconfigured prompt instead of typing one, open the chevron beside the session composer's **Send** button and pick an Action. Anything you typed rides along as a refinement. See [Actions](/kepler/actions).

***

## The terminal drawer

Terminals live in a drawer beneath the columns, spanning all of them, sized by a sash of its own.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-terminal-here-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-terminal-here-sep-2026.png" class="help-center-img img-bordered" alt="A worktree row's context menu with New terminal here highlighted">
  </a>
  <figcaption style="text-align:center; color:#888">New terminal here, on a worktree row's context menu.</figcaption>
</figure>

| How to open one | What you get |
|---|---|
| **Cmd/Ctrl+J** | Shows and hides the drawer |
| **New terminal here**, on a worktree row | A shell in that checkout |
| **Run command here**, on a worktree row | The command you pick, running in that checkout, revealed without taking your focus |
| The strip's **+** | A shell. With several checkouts it becomes a chooser listing them by branch |

The drawer's header says how many terminals are open and how many are running. **Maximize terminal pane** takes the whole height; pressing the strip restores it.

### Reading a tab

Each tab carries **one glyph** that says both what the tab is and how it ended, so a clean finish and a crash don't look alike:

| Kind | What it is |
|---|---|
| **Shell** | A plain terminal you opened |
| **Agent** | A session running an agent in Terminal mode. See [Agent Sessions](/kepler/agent-sessions#how-a-session-runs) |
| **Command run** | One of the repository's commands |

A finished command run shows a **result bar** rather than leaving you to read the scrollback: **Exited with code {code}**, **Exited by signal {signal}**, or **Stopped**, with **Run again** and **Close** beside it. A still-running one offers **Stop**.

### Closing a busy terminal

Closing a terminal with something running in it confirms first, naming the job you actually launched:

> **Close terminal?** — *{command} is still running in this terminal. Closing the terminal stops it.*

**Stop & close** goes ahead. Quitting Kepler counts busy terminals alongside busy sessions and asks before it takes them down.

***

## What each resource pane shows

| Resource | Details |
|---|---|
| **Worktree**, on disk | A strip of verbs — the branch, the sync control, **Open in**, **Run a command** — over its changed files, which lead into the Changes overlay. See [Review Changes](/kepler/review-changes) |
| **Worktree**, missing | A metadata card instead: **Current branch**, **Base branch**, and the **Recorded path**, flagged **not on disk** or **gone** when it's been removed outside Kepler. A worktree that has gone stays bound to the Task, and Kepler offers to recreate it rather than quietly dropping it |
| **Folder** / **File** | Path, plus an editable name and description |
| **Pull request** / **Issue** | Author, assignee, and status. *Full description lives in the provider — open the link above to view it.* |
| **Link** | Last synced time, or **not synced** |
| **Note** | The note itself, editable in place |

---
