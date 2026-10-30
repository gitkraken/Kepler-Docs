---
title: The Kepler Interface
description: "Kepler opens on your work - every issue and pull request assigned to you, alongside the tasks you already have running. Learn how to read it, work several items side by side, and start work from it."
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
last_verified: 2026-10
llms_include: true
tags: [interface, dashboard, todo, tasks, draft-sessions, issues, pull-requests, actions, sessions, panel, preview, worktrees, progress, keyboard, navigation, windows, updates]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Kepler opens on your work, not on an empty editor or a blank prompt. It has one interface instead of a set of views to switch between, and you shape it to fit how you work. See [Arranging Your Work](/kepler/arranging-your-work).

Kepler pulls every issue and pull request assigned to you across your connected trackers and Git hosts into one list, alongside the tasks you already have in motion. To start work, pick something that's already there instead of describing it from scratch.

Beyond this list, you'll find a task's own page, Settings, and remote connections. The top bar displays the following, leading edge first:

- The window switcher
- **Back** and **Forward**, in the desktop app only
- **New task**
- Your setup progress, only until the primary setup steps are done
- The remote indicator, the environment chip for the machine this window works on
- **Remote Access**, a monitor-and-phone button whose colour shows whether Remote Access is on. Hover it to turn Remote Access on or off and, while it's on, scan its QR code or copy its link. See [Remote access](/kepler/remote-environments#remote-access-reach-kepler-from-another-device).
- **Ask Kepler** (**Cmd/Ctrl+L**), which opens a chat and quick terminals in a panel beside the page. See [Ask Kepler](/kepler/ask-kepler).
- Feedback
- Settings
- Your account

The guided first-run flow owns the whole window, so Kepler doesn't draw the top bar there.

While an update downloads, a chip in the trailing cluster shows its progress as a ring and a percentage. Hover it for **Downloading update** (then **Verifying update**), the version, how much has arrived and about how long is left, and *Keep working. Kepler will let you know when the update is ready to install.*

When an update is ready, an **Update available** chip takes its place. It opens a popover that says what a restart would do to running work (how many agents it stops, whether terminals close) and offers **Restart to update**. When agents and terminals can survive the restart, the popover says *Running agents and open terminals keep going through the restart.* The same chip shows on every screen, so an update never waits on a banner you scrolled past.

On **Windows and Linux** the native title bar is gone and Kepler draws its own. The menu button at the leading edge holds the full application menu (**File**, **Edit**, **View**, **Window**, **Help**), including **Settings**, **Check for Updates…**, and **About**. macOS keeps its native menu bar, and both menus open the same **About Kepler** dialog.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-button-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-button-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The New task button at the left end of the Kepler top bar, a single button with a plus sign, after the application menu, the window switcher and the Back and Forward buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">The top bar's leading edge.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/top-tool-bar-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/top-tool-bar-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The right end of the Kepler top bar: the Local environment chip, the Remote Access button's monitor-and-phone icon in green because Remote Access is on, Ask Kepler, Feedback, Settings, and the account avatar.">
  </a>
  <figcaption style="text-align:center; color:#888">The top bar's trailing cluster.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/update-available-chip-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/update-available-chip-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The right end of the Kepler top bar with a green Update available chip before the Local environment chip, Remote Access, Ask Kepler, Feedback, Settings, and the account avatar.">
  </a>
  <figcaption style="text-align:center; color:#888">The trailing cluster when an update is ready.</figcaption>
</figure>

The top bar sheds controls as the window narrows based on the room actually available, rather than at fixed widths, so a control disappears only when it will not fit.

Menu items and button tooltips show a command's keyboard shortcut beside it, wherever the item does exactly what the key does. The full list is in [Settings](/kepler/settings-app#keyboard-shortcuts).

### The window switcher

**Windows** in the top bar lists every open Kepler window and what its agents are doing, so you don't have to go and look. Its trigger carries the reason to: **Windows · {count} waiting elsewhere**, or **{count} running elsewhere**. **This window** marks the one you're in, and **New window** (**Cmd/Ctrl+Shift+N**) opens another on the same connection as the window you're in. From a remote window, **New local window** opens one on this computer instead. The same list is on the tray icon.

<figure style="text-align:center">
  <a href="/wp-content/uploads/window-switcher-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/window-switcher-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The window switcher open under its top bar button, listing This window with a check mark, a second window named Local, and New window with its Ctrl+Shift+N shortcut.">
  </a>
  <figcaption style="text-align:center; color:#888">The window switcher, open.</figcaption>
</figure>

Each window's own title leads with the remote it's connected to and how many of its sessions are waiting on you. Each window keeps its own layout, and if you close the last window while Kepler keeps running, the next one opens where that window was.

### New task

**New task** (**Cmd/Ctrl+N**) opens the Task Composer. To start a task from a conversation you began outside Kepler, use **Continue an external session** in the composer. See [Create a Task](/kepler/create-task#from-a-session-you-already-started).

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
| **Todo** | Issues and pull requests related to you on each connected integration, and not yet picked up. What counts as related depends on the provider (see below) |
| **Tasks in progress** | The tasks you already have running in Kepler |
| **Agent Graph** | A live visualization of every task, session, turn, tool call, and file. See [The Agent Graph](/kepler/agent-graph) |

Providers differ in what they can be asked for, so what Todo lists depends on the integration:

| Integration | Issues | Pull requests |
|---|---|---|
| **GitHub**, **GitHub Enterprise** | Yours, assigned to you or mentioning you | Yours, assigned to you or ones you review |
| **GitLab**, **GitLab Self-Hosted**, **Azure DevOps**, **Azure DevOps Server** | Yours or assigned to you | Yours or awaiting your review |
| **Bitbucket Cloud** | None | Yours, or awaiting your review in your workspaces and repositories added to Kepler |
| **Bitbucket Data Center** | None | Yours or awaiting your review |
| **Jira**, **Jira Server**, **Linear**, **Trello** | Assigned to you | None |

The **Related to me** chip in Todo's header lists the same thing for each integration you have connected, across every organization you belong to; hover it to read it. To browse issues beyond it, use **New task** → **Issues** → **All visible**.

Todo is where a working session starts; **Tasks in progress** is where it lives while underway. The **Agent Graph** is a segment of its own rather than a way of arranging the list, because it replaces the list instead of laying it out. It scopes over every task, narrowed by your search and filters, and the **Group** and **View** controls step aside while it's on.

When launching the app, Kepler opens on **Tasks in progress**. When you start Kepler for the first time (like on a new machine), a guided setup takes over the whole window to connect your agents and trackers, and Kepler covers the list with a loading screen while it decides whether to send you there. See [Getting Started with Kepler](/kepler/kepler-getting-started). With no tasks yet, **Tasks in progress** shows the Task Composer under *Your agents' work lives here*; see [Empty states](#empty-states).

To populate the Todo tab, first connect at least one provider. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

### External sessions

Todo lists only issues and pull requests. Agent conversations running outside Kepler no longer have a section of their own in the list, and they don't open as panels. To pick one up, open **New task** and use **Continue an external session** in the Task Composer. See [Create a Task](/kepler/create-task#from-a-session-you-already-started).

For what those sessions are and what you can do with one, see [Agent Sessions](/kepler/agent-sessions#sessions-started-outside-kepler).

***

## Reading a row

A row reads differently depending on whether it holds a tracked issue or pull request, or a task you already started. The next 2 sections cover each case.

### Todo rows: issues and pull requests

<figure style="text-align:center">
  <a href="/wp-content/uploads/todo-row-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/todo-row-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The PR 2 group with pull requests #51 and #49, each marked Changes requested, and the ISSUE 3 group with #42 (Mentioned badge), #38 and #45. Each row shows its reference, title, repository and Open status; a pull request shows its author's avatar beside a reviewer whose ring is red for changes requested, issue #38 its assignee, and #51 and #38 the session dot of the task linked to them. Then the age and the outlined Action button: Address Feedback on the pull requests, Plan on the issues.">
  </a>
  <figcaption style="text-align:center; color:#888">Todo rows for pull requests and issues.</figcaption>
</figure>
<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-todo-mentioned-badge-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-todo-mentioned-badge-01-v3@2x.png" class="help-center-img img-bordered" alt="The ISSUE 3 group of the Todo list: GitHub issue #42, Gift card codes are case-sensitive at checkout, with the muted Mentioned badge, then #38, Cart total ignores discounts when tax is applied, with its assignee's avatar, and #45, Add a wishlist to product pages. Each row shows its repository, Open status, age and the outlined Plan action.">
  </a>
  <figcaption style="text-align:center; color:#888">An issue listed because it mentions you, with the Mentioned badge.</figcaption>
</figure>

Each row shows, left to right:

- The provider
- A type badge (Issue or PR) with the reference (issue key or PR number)
- The title
- Your role on a pull request
- The repository
- A status pill
- Any session activity: the session dots of the task linked to the item, and that task's running terminals
- The people: a pull request's author, with a face for each reviewer ringed in the colour of their review (green for approved, red for changes requested), or an issue's assignee
- When it last changed
- An Action button

Hover the people for one card that names everyone on the item and where each reviewer's review stands.

An issue that's on your list only because it mentions you carries a muted **Mentioned** badge, so you can tell it apart from work assigned to you.

When a provider fails to load, Kepler keeps showing the rows from its last successful load and marks each one's provider chip with a dashed outline and a crossed-out cloud. Hover the chip for *Not refreshed: shown from the last successful {provider} load.*

Right-click a Todo row for its menu, which leaves the open panel alone:

- **Open task page**, when the item already has a task
- **Open on {provider}**
- **Copy link** (**Cmd/Ctrl+C** on a focused row)
- **Copy title**
- **Copy number**
- **Copy branch name**, on a pull request

When the list is narrow, each row folds onto two lines instead of dropping cells. On the **Board** layout, a pull request's card also shows its branch.

**Your role** on a pull request is one of:

| Role | Meaning |
|---|---|
| **Yours** | You authored the pull request |
| **Review** | You're a reviewer on it |
| **Unattributed** | The provider did not say |

### Task rows

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-row-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-row-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Unread group of Tasks in progress with three task rows: Fix the cart total, Update checkout copy and Upgrade the payment SDK. Each row shows its title, the acme-web repository, its progress stage (In Development, On hold, In Review), New reply, its blue session dot, its age and the ⋮ menu.">
  </a>
  <figcaption style="text-align:center; color:#888">Task rows.</figcaption>
</figure>

Task rows show:

- The title
- The repository, or every repository when the task spans several (*app, api +2* beyond two)
- The task's pull request and issue as chips, each with its state, and *+N* when there are more
- A progress control
- What the task needs from you
- Session activity, and a pill for its running terminals
- Time

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-row-needs-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-row-needs-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Two task rows in Tasks in progress, grouped by progress. Under In Development, Add product search shows acme-web, In Development, Approval needed for Run npm test in orange and an orange session dot. Under In Review, Fix the cart total shows acme-web, a pull request chip #51 and an issue chip #38, In Review, Changes requested in red, its session dot and a square for one running terminal. Each row ends with its age and the ⋮ menu.">
  </a>
  <figcaption style="text-align:center; color:#888">Task rows that say what they need from you, with pull request, issue and terminal chips.</figcaption>
</figure>

The needs cell gives one reason, the most pressing first:

- **Approval needed for {tool}**
- **Asking: {question}**
- **Waiting for you**
- **Terminal waiting for you**, when a program in one of the task's terminals is waiting on you
- A pull request's verdict, such as **Changes requested**
- **New reply**

A task with a terminal waiting on you shows its title in bold, like one with a session waiting. The terminals pill draws a square for each running shell and a triangle for each running repository command, in the session-state colours. Hover it for **Open terminals**, or click it to open the most urgent terminal. Click the session dots to open the most urgent session.

A Done task that's ready to archive also gets an **Archive task** button on its row. When the list is narrow, each row folds onto two lines: the title and time on top, and the rest below.

Task rows carry no type badge. Everything in **Tasks in progress** is a task, so a chip saying so earned nothing and cost the width the timestamp needed; a narrowing row drops other cells before it drops the time.

A task that spans several repositories is listed under **each** of them when the list is grouped by repository, rather than under only the first one.

The task's own operations sit behind the **⋮** menu, and on a right-click:

- **Open task page** and **Open in new window**
- **Reopen**, while the task is Done, and a **Progress** submenu. See [Arranging Your Work](/kepler/arranging-your-work).
- **Mark as read**, when any of the task's sessions is unread, which marks them all read. Otherwise **Mark as unread**.
- **Rename task** (**F2** on a focused panel)
- **Move up**, **Move down**, and **Move to top of {section}**, while the list is sorted by **Manual**. See [Arranging Your Work](/kepler/arranging-your-work#sort).
- **Copy task link** (**Cmd/Ctrl+C** on a focused row), a `kepler://` link to the task
- **Copy task prompt**
- **Add resource…**
- **Refresh**, which re-reads the task's worktrees and its linked pull requests and issues. While the provider asks Kepler to wait, the row is locked and says how long to wait.
- **Shut down all agents**
- **Archive task**, or **Restore task** when the task is already archived
- **Delete task**

Task rows deliberately have no reference column and no Action button. A task's reference is the head of its identifier and names nothing you'd recognize, so the title takes that cell instead. Firing an Action from a *Todo* row is how an untracked issue or pull request becomes a task in the first place; you manage a task that already exists from its **⋮** menu.

### Status

Both segments carry a status, but they answer different questions.

| Where | Values | What it means |
|---|---|---|
| **Task rows** | **Exploration**, **In Development**, **In Review**, **On hold**, **Done**, **Archived** | Where the *work* has got to. Kepler derives it from the task's checkouts and pull requests unless you or an agent set it by hand. **In Development** reads uncommitted changes or commits ahead of the branch's recorded base; **In Review** needs an open or draft pull request of the task's own; **Done** needs at least one of the task's branches to have landed, with no open pull request and no commits left unlanded. **On hold** and **Archived** are filing decisions, not evidence |
| **Todo rows** | **Open**, **Draft**, **Merged**, **Closed** for a pull request; the tracker's own state for an issue | The provider's own state on the pull request, and the workflow state your tracker uses for the issue (such as a Linear *In Progress* or a Jira *To Verify*) rather than a flat Open |

Each pull request and issue state has its own icon and colour, so a column of pills reads at a glance.

**Done** waits for the work to land, however it got there: a pull request merged normally, by rebase, or by squash; a branch that diverged locally after its pull request merged; or a branch merged into its base with no pull request at all. A task that's done but still has uncommitted changes or unpushed commits in a checkout reads **Done · local changes**, so you can decide whether to keep them before you archive.

When the uncommitted-changes reading behind a task's stage comes from a cache rather than a live check, the progress control's tooltip says when it was taken: *Uncommitted changes as of {time}. Open the task to refresh them.*

The progress control on a task row is also a menu: click it to set the stage yourself, or put the task on hold. A stage you set holds until the evidence catches up or moves on. See [Arranging Your Work](/kepler/arranging-your-work).

Each task row also carries one dot per distinct **session state**, with a count of each.

<figure style="text-align:center">
  <a href="/wp-content/uploads/session-dots-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/session-dots-oct-2026.png" class="help-center-img img-bordered" alt="A task row's In Development pill beside two outlined session dots, an orange 2 and a blue 1, with a tooltip reading 2 Waiting (ended) and 1 Ready (ended).">
  </a>
  <figcaption style="text-align:center; color:#888">The status pill and session-state dots, with the breakdown on hover.</figcaption>
</figure>
<!-- TODO(screenshot): Replace — ade-session-dots-01: a v0.15 task row with two or more session states and a count above 1, one of them dormant so its dot is an outline, with the hover card open (its {count} agent sessions title and per-state tallies, for example 2 Waiting (ended), 1 Ready). The current figure stays until it's replaced. -->

This shows what the *agents* are doing, a separate question from where the work stands. The vocabulary is the agent's own:

- **Spawning**
- **Ready**
- **Running**
- **Idle**
- **Unread**
- **Waiting**
- **Error**
- **Working in background**
- **Reconnecting**
- **Ended**

A waiting session also says what it's waiting on: **Permission**, **Question**, **Plan review**, or **Prompt not sent**. A session with a Kepler approval request nobody has answered counts as waiting, even while its agent keeps working, and reads **Approval needed** (or **Approval needed, destructive**). A live session resting after a failed turn, such as a rate limit, an exhausted quota, or an overloaded agent, reads **Error**.

A dormant session draws as an outline rather than a filled dot. Hover the dots for a card titled with the number of agent sessions, then a count of each state, most urgent first; a state held by only one session names it. A dormant session is marked *(ended)*, as in *2 Waiting (ended)*.

Kepler places a task at the furthest stage any of its checkouts reached, except **Done**. Done needs at least one of the task's branches to have landed, no open pull request of its own, and no checkout still carrying commits that haven't landed. A sibling checkout you never touched doesn't hold a task back.

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
  <a href="/wp-content/uploads/open-a-task-panel-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/open-a-task-panel-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Todo list, with two pull requests above three issues, with GitHub issue #42 selected and its side panel open on the right: the issue header with Plan, the GITHUB, ISSUE #42 and Mentioned chips, Open in acme-web by sam-ortiz, the Summary with its labels and description, and a composer at the bottom, with #42 attached, for starting a task from it.">
  </a>
  <figcaption style="text-align:center; color:#888">The side panel, opened from a row.</figcaption>
</figure>

- **Click a row** to select it and open the side panel. A plain click replaces whatever was open, except for panels you've pinned.
- **Shift-click** a second row to open both side by side. The panel holds one column per open item, each with its own chat, so you can work several tasks at once without leaving the list.
- **Cmd-click** (**Ctrl-click** on Windows and Linux) to add one row to the open set, or to close it again.
- **Double-click a row** to open the item's full task page. From a Todo row that's the page of the task behind it. A row with no task yet has no page, so a double-click opens its panel with the cursor in the prompt box instead.

**From the keyboard**, the list is one tab stop that you walk like a tree:

| Key | What it does |
|---|---|
| **↑** / **↓** | Move between section headers and rows. Landing on a header opens nothing |
| **→** | Unfold a folded section, or step into an open one |
| **←** | Fold an open section, or climb from a row to its section header |
| **Home** / **End** | Jump to the first or last row |
| **Page Up** / **Page Down** | Move by a screenful |
| **Space** | Open the focused row's panel, or close it if it's open |
| **Enter** | On a row whose panel is open, move focus into that panel |
| **Alt+Enter** | Open the item's task page, like a double-click |

On the **Board** layout, **←** and **→** cross to the next column instead. **Tab** leaves the list rather than walking every row, and when the focused row disappears, focus moves to its neighbour.

A new task appears in the list as soon as you press **Start** in the Task Composer, before its worktrees are ready. Its row shows a **Preparing** pill while Kepler sets it up, or a **Failed** pill if setup fails. You can't drag or select a task that's still being prepared. Its panel shows Kep, Kepler's mascot, narrating each step: *Fetching {repo}.* while a repository clones (with **Cancel**), *Making your worktree.*, *Starting {agent}.*, and *Opening the chat.* (or *Opening the terminal.*). If setup fails, Kep says *That didn't go through.* (or *Task not started.* after you cancel), with **Edit and retry**, so you can change the task and start it again, and **Dismiss**. Without Kep, the panel shows **Getting your task ready**, with *Cloning {repo}…* or *Setting up worktrees…*, and a failure reads **Unable to start this task**. When a task starts without some of its repositories, Kepler warns *Some repositories weren't added* and names them.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-task-preparing-panel-01-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-task-preparing-panel-01-v2@2x.png" class="help-center-img img-bordered" alt="Tasks in progress with a new task, Add a gift-card field to checkout, in Recent with the Preparing pill and its spinner. Its side panel, also marked Preparing, reads Getting your task ready and Setting up worktrees….">
  </a>
  <figcaption style="text-align:center; color:#888">A new task while Kepler prepares it, in the list and in its panel.</figcaption>
</figure>

Shift-clicking ranges from your last plain click, the way it does in Finder or VS Code. You can open up to 16 panels at once. In the **Columns** panel layout, opening another closes the leftmost unpinned one. For **Grid**, see [Lay panels out in a grid](#lay-panels-out-in-a-grid).

Every open panel gets its own column straight away. Until its item loads, the column shows a placeholder that says it's loading, that the item is gone, or that Kepler was unable to load it, with **Try again** when retrying can help. A pull request or issue opened while you're signed out reads *Sign in to see this pull request* (or issue) with **Sign in**. Every placeholder can be closed. A remembered panel for a task that's since been deleted closes on its own.

<figure style="text-align:center">
  <a href="/wp-content/uploads/multi-task-panels-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/multi-task-panels-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Two task panels open side by side beside the Tasks in progress list: Fix the cart total (In Development, pinned) and Upgrade the payment SDK (In Review), each with its own header, worktree pill, session tab and chat.">
  </a>
  <figcaption style="text-align:center; color:#888">Several panels open side by side, each with its own chat.</figcaption>
</figure>

**Resize.** Drag the divider between two columns to resize the one on its left. Hold **Shift** as you drag to give every panel the same width at once. Double-click the divider, or press **Home** on it, to split the space evenly again. The list keeps a minimum width of its own, so a wide panel cannot shrink it too far. Kepler remembers the widths per window, across reloads, restarts, and segment switches.

**Scroll.** Once the panel strip grows wider than the window, it scrolls instead of squeezing the columns below a readable width. Scroll it sideways with **Shift** and the mouse wheel, or a sideways trackpad swipe, even over a terminal.

**Reorder.** Drag a panel by its header to a new place in the strip. A panel's **Panel actions** menu (**⋮**) offers **Move panel left** and **Move panel right**, and so do **Cmd/Ctrl+Alt+Shift+←** and **Cmd/Ctrl+Alt+Shift+→**. The older **Cmd/Ctrl+Alt+←** and **Cmd/Ctrl+Alt+→** still work.

**Maximize.** Once two or more panels are open, **Maximize panel** in the **⋮** menu (or **Cmd/Ctrl+Shift+M**, or a double-click on empty header space) spreads one panel across the strip, leaving a sliver of each neighbour. Click anywhere outside it, or use the **Restore panel** button in its header, to put the layout back exactly as it was. Switching to another panel from the keyboard moves the maximize with you, so you can read panels one after another at full size.

**Move between panels.** **Ctrl+Tab** opens **Recent panels**, a switcher of your open panels and the ones a plain click replaced since, most recently used first, so you can switch back to an item you moved away from. **Delete** or **Backspace** closes the highlighted panel, or removes a panel that's no longer open from the list (**Remove from recent panels**). With two or more unpinned panels open, the switcher moves among the open ones only. **Cmd/Ctrl+1** through **Cmd/Ctrl+8** jump to a panel by its position from the left, and **Cmd/Ctrl+9** to the last.

Starting a task from **New task** while you're on the list opens the new task as a panel and leaves the list where it was, rather than throwing you onto its page.

When the list reorders under you (a session finishes, or a task moves bucket), the row you have selected glides to its new position rather than jumping, so you can see where it went.

**Open several at once.** **Open all**, in the controls strip (or in **Options** when the window is narrow), opens every listed row in panels, up to the panel limit. Each section's header has the same button for that section alone, **Open all {count} in this section in panels**. When not everything fits, the button reads **Open {opened} of {total} in panels**, and Kepler tells you how many didn't fit.

### Lay panels out in a grid

<figure style="text-align:center">
  <a href="/wp-content/uploads/dashboard-grid-formation-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/dashboard-grid-formation-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Dashboard with five task panels in a 3 by 2 grid beside a narrow task list. The Panel layout popover is open under the 3 × 2 toolbar button: a Columns and Grid switch with Grid selected, a grid of cells with the top-left 3 by 2 block highlighted, and 3 × 2, 6 panels, Up to 16 panels, fewer in smaller windows.">
  </a>
  <figcaption style="text-align:center; color:#888">Panels in a 3 × 2 grid, with the Panel layout popover open.</figcaption>
</figure>

Open panels sit side by side in **Columns** by default. To see more of them at once, switch the **Panel layout** to **Grid**, from its button in the controls strip or with **Cmd/Ctrl+Shift+L**. The button shows the current layout, such as **3 × 2**.

In the **Panel layout** popover, pick a **Grid size** from the matrix of cells. The default is 3 × 2, and cells past the 16-panel limit are faded and can't be picked. The footer says how many panels the size holds, and *Up to 16 panels, fewer in smaller windows*. Kepler keeps the size you picked but draws only what the window fits, and the button's tooltip says what this window shows. **Reset sizes** evens out rows and columns you've resized. On a phone, panels always use **Columns**.

In a grid:

- Drag the dividers between grid columns (**Resize grid column**) and rows (**Resize grid row**). Hold **Shift** to resize every track at once, and double-click a divider or press **Home** on it to even them out.
- Panels that don't fit the grid go on further pages that scroll sideways.
- Drag a panel by its header to reorder it, row by row. **Move panel up** and **Move panel down** (**Cmd/Ctrl+Alt+Shift+↑** and **Cmd/Ctrl+Alt+Shift+↓**) join the left and right moves.
- **Maximize panel** spreads one panel over its page.
- Panels in short cells start with their headers folded, until you unfold them.
- Opening a panel never closes another. Once the grid is full, Kepler refuses the new one and says *The grid is full ({count} panels). Close one to open another.*

### Pin a panel

<figure style="text-align:center">
  <a href="/wp-content/uploads/pin-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/pin-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task panel's Task actions menu open from its header, with Pin panel highlighted.">
  </a>
  <figcaption style="text-align:center; color:#888">Pin panel, in a panel's ⋮ menu.</figcaption>
</figure>

A panel is a place you're browsing until you pin it. **Pin panel**, in the panel's **⋮** menu, holds it in place. After that:

- A plain click on a row opens beside your pins instead of replacing them.
- Following a link in **Related** swaps the panel out in place if it is not pinned, and opens the linked item beside it if it is.
- Switching segments keeps the pinned panels and drops the rest.
- Nothing evicts a pin when the open set is full.

One slot always stays unpinned so browsing never has to evict a pin; once every other panel is pinned, the menu row reads **Keep one panel unpinned for browsing** and will not take another. A pinned panel shows **Unpin panel** in its header to release it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/unpin-panel-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/unpin-panel-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A pinned panel's header for Fix the cart total, with the Unpin panel button showing its tooltip between Terminal and the close button, above the task's worktree pill.">
  </a>
  <figcaption style="text-align:center; color:#888">Unpin panel, in a pinned panel's header.</figcaption>
</figure>

***

## The side panel

Selecting a row opens a panel beside the list with everything about that item, as a stack of collapsible, resizable sections.

<figure style="text-align:center">
  <a href="/wp-content/uploads/issue-side-panel-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/issue-side-panel-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The side panel for GitHub issue #38, Cart total ignores discounts when tax is applied, as a stack of sections: its header with the Open on GitHub, panel menu, Plan Action and Close buttons, the GITHUB and ISSUE #38 chips, Open, acme-web, the linked task's session dot, the age, and alex-lee as Assignee; Summary with the bug label and the description; Related (1) listing the task Fix the cart total, In Review; and that task's session with its conversation and composer.">
  </a>
  <figcaption style="text-align:center; color:#888">The side panel, with its stack of collapsible sections.</figcaption>
</figure>

Kepler does not draw a section that has nothing behind it.

| Section | What's in it | When it's there |
|---|---|---|
| **Summary** | The issue or pull request description, with its labels shown as badges. You can select and copy the description text | An issue or pull request that has a description. Tasks carry none of their own |
| **Related ({count})** | Linked issues and pull requests, counted in the heading so a folded pane still says how many | There's at least one |
| **What's running** | Session tabs and draft session tabs. A session tab holds the live agent conversation; a draft tab holds a prompt box plus the same Actions. This is the chat | Always, on an item you can start work on. Resizable, but not foldable: it's what the panel is for |
| **Plan** | The plan the conversation on screen has proposed | The agent produced one |
| **Changes** | The checkout's commits, working changes, and file diffs, in the [side pane](#the-side-pane) | You opened a worktree's changes from its pill |
| **Terminals** | Terminal tabs across the task's checkouts. A shell tab shows its program's status, such as **Running**, **Needs you**, **Done** or **Failed**, when the program reports one | A terminal is open. Its **✕** takes the section away without stopping the shells; the header's terminal control and **Cmd/Ctrl+J** are the way back |

Kepler sizes **Summary** and **Related** to their contents and then the chat takes whatever height is left over.

To reorder the tabs in **What's running** or **Terminals**, drag a tab to a new place. Kepler remembers each task's terminal tab order and selected terminal across reloads and in new windows. Closing the selected terminal moves you to the leftmost one left.

Pressing **Delete** on a focused session tab in **What's running** asks first: *Archive session?*, *Stops the agent and moves {session} to Archived sessions. Restore it any time.* The tab's own archive control and its menu row still archive in one click.

A plain shell tab takes the name of what's running in it: the app that reports its status, the job in front (such as `pnpm dev`), or on Windows the window title the program set. Back at the prompt it returns to its own label, such as *Terminal 2*. When the two differ, hover the tab to see the label and the job's command line or title. Hover a tab with a program status for how long the program has been in that state, its progress as a bar, and, for a program that's blocked or failed without saying why, what to do next, such as *Approve it in the terminal.*

If an agent fails after you start a session, **What's running** shows **{agent} was unable to start** with the agent's message. Press **Retry** to launch it again, or **Open agent settings** to fix the problem.

For unstarted issues or PRs, the side panel's primary button follows that item's preferred Action (Plan, Implement vs Review, Address Feedback). 

In the side panel for a Task, the primary button reads **Start**, and once a session exists the composer becomes that session's chat, where it reads **Send**. If the preferred Action is **None**, no longer exists, or cannot aim at this kind of item, the button falls back to **Start**.

A task you created with a prompt but haven't started reads *Start with the task prompt, or describe something else…*. Press **Start** on the empty box and the task's prompt goes out as the first message; type something to send that instead.

The header carries:

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-preview-header-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-preview-header-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task's side panel header: the fold chevron, the task title Upgrade the payment SDK, Open task page, the ⋮ Task actions menu, the In Review progress control, the Terminal button and Close, above its worktree pill with the kepler/payment-sdk-v5 branch in acme-web, 1 uncommitted file and the main merge target.">
  </a>
  <figcaption style="text-align:center; color:#888">The side panel's header, on a task.</figcaption>
</figure>

- The item's badges and reference
- On an issue or pull request, the people on it: a pull request's author, its **Assignees**, and its reviewers, each ringed and badged by the state of their review with a tally such as *1 of 2 reviewed*, or an issue's assignee. The reviewers fold to a line of faces
- The title, with a dot when a session needs you: blue for an unread turn, orange for one waiting on you
- The progress control, on a task
- The terminal control, on a task
- **Restore panel**, when the panel is maximized
- **Unpin panel**, when the panel is pinned
- **Close panel** (**Cmd/Ctrl+W** on the focused panel)
- **Panel actions** (**⋮**): **Close panel**, **Open task page**, **Open on {provider}** for an issue or pull request, **Pin panel**, **Maximize panel**, **Move panel left**, **Move panel right**, **Close other panels**, and **Close all panels**. On a task, these rows join its **Task actions** menu. **Maximize panel**, the moves, and the two close-many rows appear only once more than one panel is open

Each pull request, issue, or artifact linked to a task has a chip under the header; hover one for its card, or click it to read it in the side pane. A pull request whose branch name was used before reads *Opened from an earlier branch with the same name*. The **Resources** chip lists the task's notes, files, folders, and links, plus a **Related tasks** group, and every row opens in the side pane.

<figure style="text-align:center">
  <a href="/wp-content/uploads/artifact-chip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/artifact-chip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The artifact attached to the task as a link chip, Acme gift cards, under the task's worktree pill, with its hover card open showing the artifact's title, its link, Open and Copy link.">
  </a>
  <figcaption style="text-align:center; color:#888">A linked item's chip under the header, with its hover card.</figcaption>
</figure>

Hover a task's title to read its prompt, cut off after 10 lines, with the hint *Double-click to rename*. To copy the whole prompt, use **Copy task prompt** in the **⋮** menu. The prompt is a context item of its own, labelled **Prompt**, shown first among the task's notes in the card, the preview, and the task page's rail, and it can't be deleted.

To rename a task, double-click its title, choose **Rename task** from its **⋮** menu, or press **F2** on its focused panel, and edit the name in place. Enter commits the change; Escape or clicking away discards it.

### The side pane

<figure style="text-align:center">
  <a href="/wp-content/uploads/dashboard-side-pane-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/dashboard-side-pane-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A wide task panel for Fix the cart total with the Prompt note open in its side pane, right of the session. The panel's header reads In Review and holds the worktree card (kepler/fix-cart-total, its #51 pull request marked Changes requested, 2 uncommitted, main) and the #51 Open and #38 Open chips; the session shows its conversation and composer; the side pane's title row holds the resource switcher on Prompt, Copy, Edit and Close side pane, with the note's text below.">
  </a>
  <figcaption style="text-align:center; color:#888">A note open in a task panel's side pane, beside the session.</figcaption>
</figure>

A task panel reads its linked items, resources, and changes in a **side pane**, so you don't have to leave the list for the task page. These open in it:

- A linked pull request or issue chip
- A row of the **Resources** chip: a note, a file, a folder, a related task, or the task's links as one list
- The uncommitted or commits chip on a worktree pill

When the panel is at least 960 pixels wide, the pane opens beside the sessions. Drag its edge (**Resize side pane**) to resize it, and close it with **Close side pane** or **Escape**. In a narrower panel, the pane takes the sessions' place, with **Back to sessions** to return. The pane shows the same view of the item as the task page does.

Click the same chip again to close the pane. The switcher in the pane's title row moves between the task's linked items and resources without closing it. Two shortcuts toggle it on the focused panel:

- **Cmd/Ctrl+Shift+G** shows or hides the worktree's changes.
- **Cmd/Ctrl+Shift+E** shows or hides the last resource the panel showed.

Kepler remembers the open pane for each item and the pane's width for each window.

### Issue comments

<figure style="text-align:center">
  <a href="/wp-content/uploads/issue-comments-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/issue-comments-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Fix the cart total panel (In Review, its worktree card with #51 marked Changes requested, and the #51 Open and #38 Open chips) with GitHub issue #38 open in its side pane: Back to sessions, the issue title Cart total ignores discounts when tax is applied, the GITHUB and ISSUE #38 chips, Open, acme-web and the assignee alex-lee, the bug label and the description, then Comments · 3 with Refresh comments: jo-park, sam-ortiz and alex-lee, each with an avatar, an age and the comment text.">
  </a>
  <figcaption style="text-align:center; color:#888">An issue's comments, under its summary in the side pane.</figcaption>
</figure>

An issue you open in a side pane, or on the task page, shows its discussion under the summary as **Comments**, with the count in the heading. Each comment has the author's avatar and name, how long ago it was posted, and its text. Kepler reads the newest 100 comments through the same connection it reads the issue with:

- **Show earlier comments** reveals older ones that Kepler already loaded. When the issue has more than that, the section says that more may be available on the provider.
- **Refresh comments** reads them again.
- With none yet, the section reads *No comments yet.* When a read fails, it reads *Unable to load comments.* with **Retry**.

Comments work for GitHub, GitHub Enterprise, GitLab, GitLab Self-Hosted, Jira, and Jira Server issues. For other providers, when you're signed out, or when the connected account can't read the issue's comments, the section says so instead. Kepler shows comments to you; it doesn't hand them to the agent as task context.

The header folds down to its title row with the chevron beside it, for a task, a pull request, or an issue. A folded pull request still shows its number and review decision. Each segment remembers its own fold.

A Done task with no unpushed work and no agent working or waiting on you shows *Ready to archive?* in its header. See [Arranging Your Work](/kepler/arranging-your-work).

An archived task reads **Archived** where its progress control would be, in both its preview and its detail header, so you can't mistake a filed task for a live one.

### The worktree pill

Below the header, each of the task's checkouts is a **pill** with two rows: who it is on top, and what's in it below.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-preview-header-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-preview-header-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task's side panel header: the fold chevron, the task title Upgrade the payment SDK, Open task page, the ⋮ Task actions menu, the In Review progress control, the Terminal button and Close, above its worktree pill with the kepler/payment-sdk-v5 branch in acme-web, 1 uncommitted file and the main merge target.">
  </a>
  <figcaption style="text-align:center; color:#888">A task's worktree pill, below the header.</figcaption>
</figure>

| Row | What it shows | What it does |
|---|---|---|
| **Top** | The branch and repository, the worktree's own pull request, and the upstream control | The branch name opens or closes the worktree's changes in the side pane (**Open worktree changes** / **Close worktree changes**); its **⋮** opens the worktree's menu (see below). The upstream control runs the verb its counts call for: **Pull** when behind, **Push** when ahead, **Publish** when the branch isn't on a remote yet, and **Force push** behind a confirmation when the branch has diverged or after you apply a rebase. **Fetch** and the upstream row are in its chevron |
| **Bottom** | Chips for uncommitted files, commits, and the merge target, plus **Open in** and **Run** | The uncommitted and commits chips open the worktree's changes in the side pane, on that scope, and the merge target chip shows how the branch compares with its merge target. Its own menu also offers **Rebase onto {target}** and **Merge {target} into this branch**, which open the update view. See [Review Changes](/kepler/review-changes#updating-from-the-base). **Open in** opens the checkout in your default editor, with the rest in its chevron. **Run** runs one of the repository's commands |

Click the uncommitted or commits chip that's showing again to close the side pane, or the other one to switch scope.

The pill says what needs doing rather than just counting: unpushed commits, a paused rebase or merge you can continue or abort from the pill, a merge target it was unable to read with a retry, a detached HEAD explained, and **No changes** only when there really are none. Hover any chip for a card that leads with what a click does; right-click it for the worktree's menu.

**The worktree menu** is the same wherever a worktree appears, on the pill and on the task page:

- **Open changes** (or **Close changes** while they're showing), **Open in**, and the worktree's pull request
- **Continue {operation}** and **Abort {operation}** during a stopped rebase or merge
- A **Branch** submenu: **Rename branch**, **Rebase onto {target}** and **Merge {target} into this branch**, **Push**, **Pull** and **Fetch**, **Set upstream** or **Change upstream**, and **Change merge target…**
- **New session here**, **New terminal here**, and **Run command here**
- **Copy branch name**, **Copy worktree path**, and **Copy remote URL**
- **Detach worktree…** and **Delete worktree…**, or **Recreate worktree** for a checkout that's gone

**Set or change the upstream.** **Set upstream** (or **Change upstream**, which shows the branch it tracks now) opens a searchable list of remote branches, **Search remote branches**. A tracked branch that's gone comes first, marked **Not found**, then any remote's branch with the same name (**Same name**), then the rest; the branch tracked now is marked **Current**. Pinned above the list are **Publish as {remote}/{branch}…**, when no remote has a branch of the same name, and **Unset upstream**, when the branch tracks one. **Refresh branches**, beside the search box, fetches the list again. Any remote branch can be the upstream, under any name, and **Push** then goes there. The row is hidden on a detached HEAD. As the panel narrows, the chips shrink to their icons and counts rather than disappearing, and the branch name is cut last.

**More than one worktree.** A task's worktrees collapse into one pill, led by a count such as *1/3*. Step through them with the switcher on the branch name, or with the up and down arrow keys on the pill. Until you pick one, the pill follows the worktree with the latest changes. The toggle on the pill's leading edge (**Show all {count} worktrees**) lays them all out at once. Worktrees whose branches have merged share a single row, with a way to delete them through the same cleanup list archiving uses.

From the keyboard, a pill is two tab stops (its changes and its actions), with the left and right arrows moving inside each.

The terminal strip's **+** becomes a chooser listing the task's checkouts by branch when the task has more than one.

An issue or pull request keeps a status line as well, with its provider state, session dots, repository, and last activity, and the people on it sit in the header. A task does not, because the row you clicked already showed that information.

***

## Back and forward

Back follows one rule: **it leaves the place or mode you're in.** It never retraces a search you typed, a filter you set, or a change of view mode, so pressing it after narrowing the list takes you out of the list rather than walking back through every keystroke.

| | Mac | Windows / Linux |
|---|---|---|
| **Back** | ⌘ [ | Alt + ← |
| **Forward** | ⌘ ] | Alt + → |

The **Back** and **Forward** buttons in the top bar do the same, as do a mouse's side buttons. On macOS, a two- or three-finger sideways swipe on a trackpad or Magic Mouse goes back and forward too, wherever nothing under the pointer scrolls sideways. A sideways scroll or a mouse's tilt wheel never goes Back on Windows and Linux, so a stray scroll can't throw you out of what you were reading.

Each set of open panels gets its own history entry, so Back closes the set you just opened rather than the whole visit. Moving between Settings sub-pages replaces a single entry, so Back from Settings returns you to what you were doing before you opened it.

***

## Empty states

| What you see | What it means |
|---|---|
| **Your agents' work lives here** | You have no tasks. **Tasks in progress** shows the Task Composer, with hints to add an issue, a pull request, or a repository or folder, to start from a saved Action, or to **Continue an external session**. After the guided setup it reads *You're set up* above the heading |
| **No tasks yet** | The Tasks list is empty |
| **No assigned PRs or issues** | Providers are connected, but nothing related to you is open. Hover **Related to me** for what Todo lists |
| **Nothing matches your search** | Your search, with or without filters, excludes everything. On Todo it adds *Todo only searches work related to you.* Use the button beneath it: **Clear search** or **Clear search and filters** |
| **Nothing matches these filters** | Your filters exclude everything. Use **Clear filters** beneath it |
| **Nothing here** | One column of the **Board** layout is empty while its neighbours are not |
| **Hand your issues and PRs to agents** | You have no provider connected, so Todo lists every provider as a one-click connect, grouped under **Code hosting** and **Issue trackers**. The same view introduces Todo the first time you open it |
| **Unable to load your work** | Every connected provider failed to load. The notice below names each one, what went wrong, and the fix, such as **Reconnect** or **Retry** |
| **Unable to load your issues and pull requests.** | Loading the whole list failed. Press **Retry** |
| **Sign in to see your assigned work** | *Connect a GitKraken account to load the PRs and issues assigned to you.* |
| **Unable to find this task** | The task you opened was deleted, or its link is from another machine: *It may have been deleted, or the link may be from another machine.* An archived task still opens |

<figure style="text-align:center">
  <a href="/wp-content/uploads/tasks-empty-state-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/tasks-empty-state-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Tasks in progress empty state: the heading Your agents' work lives here and a line on what a task is, then Add issue, Add PR and Add context above the composer (Describe a task or ask a question…, the agent pill and Start), Add repo or folder below it, handwritten hints pointing at each, and a Continue an external session card under an or divider.">
  </a>
  <figcaption style="text-align:center; color:#888">Tasks in progress with no tasks yet.</figcaption>
</figure>

### Kep

Kep, Kepler's planet mascot, keeps empty and waiting screens company. He appears on the loading screen while Kepler starts, over a new session's empty chat, over empty views, in loading spinners, in the **About Kepler** dialog and What's New, and on the crash and sign-in error screens. When your search or filters empty the list, he sleeps above the message. On a crash screen, **Show details** reveals **Error details**, with **Copy details** for a bug report.

<figure style="text-align:center">
  <a href="/wp-content/uploads/kep-empty-chat-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/kep-empty-chat-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A new session's empty chat in a task panel: Kep, Kepler's planet mascot, above What should the agent work on? and Describe the task, add a file with @, or type / for commands. Below them the draft composer reads Start with the task prompt, or describe something else…, with Task context, the agent pill and Start, and the Task folder picker under it.">
  </a>
  <figcaption style="text-align:center; color:#888">Kep over a new session's empty chat.</figcaption>
</figure>

Kep's eyes follow your pointer, except when your system asks for reduced motion. Kepler can also show him without his speech card, or not at all, in which case the plain text and icons he replaces come back.

---
