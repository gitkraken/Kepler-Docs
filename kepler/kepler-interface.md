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

Kepler opens on your work: every issue and pull request assigned to you across your connected trackers and Git hosts, in one list beside the tasks you already have running. To start work, pick an item from that list instead of describing it from scratch.

You work in one interface rather than switching between separate views, and you can arrange it to fit how you work. See [Arranging Your Work](/kepler/arranging-your-work). Besides the list, Kepler has a page for each task, Settings, and remote connections.

***

## The top bar

The top bar holds the following controls, from the leading edge:

- The window switcher
- **Back** and **Forward**, in the desktop app only
- **New task**
- Your setup progress, until you finish the primary setup steps
- The remote indicator: the environment chip that shows which machine this window works on
- **Remote Access**, a monitor-and-phone button whose color shows whether Remote Access is on. Hover it to turn Remote Access on or off and, while it's on, to scan its QR code or copy its link. See [Remote access](/kepler/remote-environments#remote-access-reach-kepler-from-another-device).
- **Ask Kepler** (**Cmd/Ctrl+L** or **Cmd/Ctrl+K**), shown as Kep, Kepler's mascot, with the word **Ask**. It opens a chat and quick terminals in a panel beside the page. See [Ask Kepler](/kepler/ask-kepler).
- Feedback
- Settings
- Your account

The guided first-run setup fills the whole window, so the top bar does not appear there.

The **Ask Kepler** button also shows the state of the panel's chats. When a chat needs you, has a new reply, or failed, the button becomes a **Needs you**, **New reply**, or **Failed** pill. Click the pill to open that chat. In a narrow window, the button shows Kep alone. A focused shell keeps **Ctrl+L** for itself, so use **Ctrl+K** there. See [Ask Kepler](/kepler/ask-kepler).

While an update downloads, a chip near the trailing end of the top bar shows its progress as a ring and a percentage. Hover the chip to see **Downloading update** (then **Verifying update**), the version, how much has downloaded, about how long is left, and *Keep working. Kepler will let you know when the update is ready to install.*

When the update is ready, an **Update available** chip replaces the progress chip. It opens a popover that says what a restart does to running work, such as how many agents it stops and whether terminals close, and offers **Restart to update**. When agents and terminals can survive the restart, the popover says *Running agents and open terminals keep going through the restart.* The chip shows on every screen, so you cannot miss the update by scrolling past a banner.

On Windows and Linux, Kepler replaces the native title bar with its own. The menu button at the leading edge holds the full application menu (**File**, **Edit**, **View**, **Window**, **Help**), including **Settings**, **Check for Updates…**, and **About**. macOS keeps its native menu bar. Both menus open the same **About Kepler** dialog.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-button-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-button-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The New task button at the left end of the Kepler top bar, a single button with a plus sign, after the application menu, the window switcher and the Back and Forward buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">The top bar's leading edge.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/top-tool-bar-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/top-tool-bar-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The right end of the Kepler top bar: the Local environment chip, the Remote Access button's monitor-and-phone icon in green because Remote Access is on, the Ask button with Kep, Feedback, Settings, and the account avatar.">
  </a>
  <figcaption style="text-align:center; color:#888">The top bar's trailing cluster.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/update-available-chip-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/update-available-chip-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The right end of the Kepler top bar with a green Update available chip before the Local environment chip, Remote Access, the Ask button with Kep, Feedback, Settings, and the account avatar.">
  </a>
  <figcaption style="text-align:center; color:#888">The trailing cluster when an update is ready.</figcaption>
</figure>

As the window narrows, the top bar hides the controls that no longer fit. It measures the room actually available rather than using fixed widths, so a control disappears only when it will not fit.

Menu items and button tooltips show a command's keyboard shortcut when the item does exactly what the key does. For the full list, see [Keyboard shortcuts](/kepler/settings-app#keyboard-shortcuts).

### The window switcher

The **Windows** menu in the top bar lists every open Kepler window and what its agents are doing. Its button shows what's happening in your other windows, such as **Windows · {count} waiting elsewhere** or **{count} running elsewhere**. In the menu:

- **This window** marks the window you're in.
- **New window** (**Cmd/Ctrl+Shift+N**) opens another window on the same connection as this one.
- **New local window**, in a remote window, opens a window on this computer instead.

The [tray icon](#the-tray-icon) has the same list.

<figure style="text-align:center">
  <a href="/wp-content/uploads/window-switcher-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/window-switcher-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The window switcher open under its top bar button, listing This window with a check mark, a second window named Local, and New window with its Ctrl+Shift+N shortcut.">
  </a>
  <figcaption style="text-align:center; color:#888">The window switcher, open.</figcaption>
</figure>

Each window's title starts with the remote it's connected to and how many of its sessions are waiting on you. Each window keeps its own layout. If you close the last window while Kepler keeps running, the next window opens where that one was.

### The tray icon

Kepler's icon in the system tray (the menu bar on macOS) shows the most urgent thing your agents are doing, even when no window is open. The icon counts every agent session Kepler runs on this computer and on each remote machine that an open window connects to. It counts each session at one level, listed here from most urgent:

| Level | Which sessions |
|---|---|
| Needs your answer | Waiting on your answer or on an approval |
| Failed | A turn that ended in an error and that you have not opened |
| Finished | A finished turn you have not read |
| Working | Running a turn |

The icon does not count idle sessions, sessions started outside Kepler, plain terminals, archived sessions, or sessions whose only work is a background task.

Hover the icon to see a status line under the app's name, such as *2 agents need your answer, 1 failed, 3 working* or *No agents running*. On macOS, a count of the agents that need a look (waiting, failed, or finished) appears beside the icon. The count is red while any of them is waiting or failed. On Windows, the icon follows your taskbar's light or dark theme. On Linux, it follows the system theme.

On Windows and Linux, click the icon to open the window that needs you. Kepler picks the window you used last on the machine with the most urgent agent, or else the window you used last overall. The icon's menu holds:

- **Open Kepler**
- **Windows**, a submenu with **New Window**, **New Local Window** when the window you used last is remote, and every open window, with a check beside the one you used last
- **Quit** and **Quit & End Sessions**

<!-- TODO(screenshot): New — ade-tray-menu-01: the Kepler tray icon's menu with Open Kepler, the Windows submenu open on New Window and the open windows, the current one checked, then Quit and Quit & End Sessions. -->

### New task

**New task** (**Cmd/Ctrl+N**) opens the **New task** composer. To start a task from a conversation you began outside Kepler, use **Open an external session** in the composer. A session that's still live in its terminal opens read-only in its task, and **Continue here** and **Fork** become available once it's idle. See [Create a task](/kepler/create-task#from-a-session-you-already-started).

***

## Todo, Tasks in progress, and the Agent Graph

Use the switcher at the top left to move between 3 views of your work.

<figure style="text-align:center">
  <a href="/wp-content/uploads/todo-task-in-progress-agent-graph-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/todo-task-in-progress-agent-graph-sep-2026.png" class="help-center-img img-bordered" alt="The control at the top left of Kepler, switching between Todo, Tasks in progress, and Agent Graph">
  </a>
  <figcaption style="text-align:center; color:#888">The Todo, Tasks in progress, and Agent Graph switcher.</figcaption>
</figure>

The switcher has these segments:

| Segment | What it shows |
|---|---|
| **Todo** | Issues and pull requests related to you on each connected integration, and not yet picked up. What counts as related depends on the provider |
| **Tasks in progress** | The tasks you already have running in Kepler |
| **Agent Graph** | A live visualization of every task, session, turn, tool call, and file. See [The Agent Graph](/kepler/agent-graph) |

What Todo lists depends on what each provider lets Kepler ask for:

| Integration | Issues | Pull requests |
|---|---|---|
| **GitHub**, **GitHub Enterprise** | Yours, assigned to you or mentioning you | Yours, assigned to you or ones you review |
| **GitLab**, **GitLab Self-Hosted**, **Azure DevOps**, **Azure DevOps Server** | Yours or assigned to you | Yours or awaiting your review |
| **Bitbucket Cloud** | None | Yours, or awaiting your review in your workspaces and repositories added to Kepler |
| **Bitbucket Data Center** | None | Yours or awaiting your review |
| **Jira**, **Jira Server**, **Linear**, **Trello** | Assigned to you | None |

To see this scope for the integrations you've connected, hover the **Related to me** chip in Todo's header. The scope covers every organization you belong to. To browse issues outside it, use **New task** → **Issues** → **All visible**.

Work starts in **Todo** and moves to **Tasks in progress** while it's underway. The **Agent Graph** replaces the list rather than arranging it, so it's a segment of its own. It shows every task that matches your search and filters, and the **Group** and **View** controls are not available while it's on.

Kepler opens on **Tasks in progress**. The first time you start Kepler, such as on a new machine, a guided setup fills the whole window to connect your agents and trackers. Until Kepler decides whether to send you there, a loading screen covers the list. See [Getting Started with Kepler](/kepler/kepler-getting-started). If you have no tasks yet, **Tasks in progress** shows the **New task** composer under *Your agents' work lives here*. See [Empty states](#empty-states).

To fill **Todo**, connect at least one provider. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

### External sessions

Todo lists only issues and pull requests. Agent conversations running outside Kepler do not have a section of their own in the list, and they do not open as panels. To pick one up, open **New task** and use **Open an external session** in the **New task** composer. See [Create a task](/kepler/create-task#from-a-session-you-already-started).

To learn what external sessions are and what you can do with them, see [Agent Sessions](/kepler/agent-sessions#sessions-started-outside-kepler).

***

## Reading a row

Todo rows and task rows show different information. A Todo row describes an issue or pull request. A task row describes a task you already started.

### Todo rows: issues and pull requests

<figure style="text-align:center">
  <a href="/wp-content/uploads/todo-row-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/todo-row-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The PR 2 group with pull requests #51 and #49, each marked Changes requested, and the ISSUE 3 group with #42 (Mentioned badge), #38 and #45. Each row shows its reference, title, repository and Open status; #51 and #38 also carry a Task badge for the task already started from them, with that task's session dot. A pull request shows its author's avatar beside a reviewer whose ring is red for changes requested, issue #38 its assignee. Then the age and the outlined Action button: Address Feedback on the pull requests, Plan on the issues.">
  </a>
  <figcaption style="text-align:center; color:#888">Todo rows for pull requests and issues.</figcaption>
</figure>
<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-todo-mentioned-badge-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-todo-mentioned-badge-01-v3@2x.png" class="help-center-img img-bordered" alt="The ISSUE 3 group of the Todo list: GitHub issue #42, Gift card codes are case-sensitive at checkout, with the muted Mentioned badge, then #38, Cart total ignores discounts when tax is applied, with its assignee's avatar, and #45, Add a wishlist to product pages. Each row shows its repository, Open status, age and the outlined Plan action.">
  </a>
  <figcaption style="text-align:center; color:#888">An issue listed because it mentions you, with the Mentioned badge.</figcaption>
</figure>

Each Todo row shows, from left to right:

- The provider
- A type badge (Issue or PR) with the reference (issue key or PR number)
- The title
- Your role on a pull request
- A **Task** badge (or **{count} tasks**) when tasks were already started from the item, or **Archived task** (**{count} archived tasks**) when every one of them is archived
- The repository
- A status pill
- Any session activity: the session dots of the task linked to the item, and that task's running terminals
- The people: a pull request's author and an avatar for each reviewer, ringed in the color of their review (green for approved, red for changes requested), or an issue's assignee
- When it last changed
- An Action button

Hover the avatars to see a card that names everyone on the item and shows where each review stands. An issue that's on your list only because it mentions you carries a muted **Mentioned** badge, so you can tell it apart from work assigned to you.

When a Linear issue is synced with a GitHub issue and both copies are listed, Todo shows one row for them: the Linear row. The 2 copies share one task history. A task started from either copy counts as the issue's task, and a task started from the Linear row works in the GitHub copy's repository. If you filter the list to GitHub, the GitHub copy shows on its own.

When a provider fails to load, Kepler keeps showing the rows from its last successful load. It marks each of those rows' provider chip with a dashed outline and a crossed-out cloud. Hover the chip to see *Not refreshed: shown from the last successful {provider} load.*

Right-click a Todo row to open its menu. The menu does not change which panel is open. It holds:

- **Open task page**, when the item already has a task
- **Open on {provider}**
- **Copy link** (**Cmd/Ctrl+C** on a focused row)
- **Copy title**
- **Copy number**
- **Copy branch name**, on a pull request

When the list is narrow, each row wraps onto 2 lines instead of dropping cells. On the **Board** layout, a pull request's card also shows its branch.

**Your role** on a pull request is one of the following:

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

Each task row shows:

- The title
- The repository, or every repository when the task spans several (*app, api +2* beyond 2)
- The task's pull request and issue as chips, each with its state, and *+N* when there are more
- Its group, when it's in one and the list is not already grouped by your groups: a colored bar in the row's gutter on the **List** layout, or a chip after the title on a **Board** card
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

When a session or a terminal in a task waits on you, the task's title shows in bold. The terminals pill shows a square for each running shell and a triangle for each running repository command, in the session-state colors. Hover the pill to see **Open terminals**, or click it to open the most urgent terminal. To open the most urgent session, click the session dots.

Hover a pull request or issue chip to see the same card the chip shows in the task's panel. Click the chip to keep the card open; the click does not select the row. When the task has more than one link of that kind, the card lists them all under **Pull requests** or **Issues**, and you can choose one to see its card. Right-click the chip for the link's menu.

On a **Board** card, hover the group chip, **Group: {name}**, to see a summary of the group's tasks, such as *4 tasks: 1 needs you, 2 running*. Click the chip for **Open group**, **Show only this group**, **Group by your groups** (or **{axis} within your groups**), and **Remove from group**. See [Arranging Your Work](/kepler/arranging-your-work).

A Done task that's ready to archive also gets an **Archive task** button on its row.

Task rows have no type badge, no reference column, and no Action button:

- Everything in **Tasks in progress** is a task, so a type badge would add nothing. As a row narrows, it drops other cells before it drops the time.
- A task's reference is the start of its identifier and names nothing you'd recognize, so the title takes that cell instead.
- An Action on a Todo row is what turns an untracked issue or pull request into a task. To manage a task that already exists, use its **⋮** menu.

When the list is narrow, each task row wraps onto 2 lines: the title and time on top, and the rest below. When the list is grouped by repository, a task that spans several repositories appears under **each** of them, rather than under only the first one.

To manage a task, open its **⋮** menu or right-click its row. The menu holds:

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

**Act on several tasks at once.** Open 2 or more tasks with **Shift-click** or **Cmd/Ctrl-click** (see [Open a panel](#open-a-panel)), then right-click any of them. The menu acts on the whole selection, and each label counts the tasks:

- **New group with {count} tasks…**
- **Add {count} tasks to group**
- **Remove {count} tasks from group**
- **Archive {count} tasks**
- **Restore {count} tasks**
- **Delete {count} tasks**

The menu shows only the items that apply, and grouping leaves archived tasks out. The rows the menu acts on stay outlined until it closes. **Archive**, **Restore**, and **Delete** ask first, with the same confirmation as a section's **Select** bar. If you right-click a task outside the selection, or use a row's **⋮** menu, the action applies to that task alone.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-selection-menu-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-selection-menu-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Tasks in progress grouped by your groups, with Add product search and Write the 2.4 release notes selected and outlined in the Ungrouped section, and the selection's right-click menu open below them: New group with 2 tasks…, Add 2 tasks to group, Archive 2 tasks and Delete 2 tasks. Above are the Checkout and Payments sections.">
  </a>
  <figcaption style="text-align:center; color:#888">The menu for two selected tasks.</figcaption>
</figure>

Drag any selected task to move the whole selection to another section or column or, under **Manual** sort, to a new place in the list. Press **Escape** to cancel the drag. Each task moves only where it can, and Kepler tells you how many moved and how many stayed where they were.

### Status

Task rows and Todo rows both show a status, but the 2 statuses mean different things:

| Where | Values | What it means |
|---|---|---|
| **Task rows** | **Exploration**, **In Development**, **In Review**, **On hold**, **Done**, **Archived** | How far the *work* has got. Kepler derives it from the task's checkouts and pull requests, unless you or an agent set it by hand |
| **Todo rows** | **Open**, **Draft**, **Merged**, **Closed** for a pull request; the tracker's own state for an issue | The provider's own state on the pull request, and the workflow state your tracker uses for the issue (such as a Linear *In Progress* or a Jira *To Verify*) rather than a flat Open |

Each pull request and issue state has its own icon and color, so you can read a column of pills at a glance.

Kepler derives a task's stage from this evidence:

- **In Development**: uncommitted changes, or commits ahead of the branch's recorded base.
- **In Review**: an open or draft pull request of the task's own.
- **Done**: at least one of the task's branches has landed, the task has no open pull request of its own, and no checkout still carries commits that have not landed.
- **On hold** and **Archived**: filing decisions, not evidence.

A task sits at the furthest stage any of its checkouts reached, except **Done**, which follows its own rule. A sibling checkout you never touched does not hold a task back.

**Done** waits for the work to land, however it got there: a pull request merged normally, by rebase, or by squash; a branch that diverged locally after its pull request merged; or a branch merged into its base with no pull request at all. A task that's done but still has uncommitted changes or unpushed commits in a checkout reads **Done · local changes**, so you can decide whether to keep them before you archive.

When Kepler bases a task's stage on cached uncommitted changes rather than a live check, the progress control's tooltip says when it read them: *Uncommitted changes as of {time}. Open the task to refresh them.*

To set the stage yourself, or to put the task on hold, click the progress control on its row. A stage you set stays until the evidence catches up or moves past it. See [Arranging Your Work](/kepler/arranging-your-work).

Each task row also shows one dot for each distinct session state, with a count of each.

<figure style="text-align:center">
  <a href="/wp-content/uploads/session-dots-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/session-dots-oct-2026.png" class="help-center-img img-bordered" alt="A task row's In Development pill beside two outlined session dots, an orange 2 and a blue 1, with a tooltip reading 2 Waiting (ended) and 1 Ready (ended).">
  </a>
  <figcaption style="text-align:center; color:#888">The status pill and session-state dots, with the breakdown on hover.</figcaption>
</figure>
<!-- TODO(screenshot): Replace — ade-session-dots-01: a v0.15 task row with two or more session states and a count above 1, one of them dormant so its dot is an outline, with the hover card open (its {count} agent sessions title and per-state tallies, for example 2 Waiting (ended), 1 Ready). The current figure stays until it's replaced. -->

The dots show what the *agents* are doing, which is separate from where the work stands. A session can be in one of these states:

- **Spawning**
- **Ready**
- **Running**
- **Idle**
- **Unread**
- **Waiting**
- **Error**
- **Background task running**
- **Reconnecting**
- **Ended**

A waiting session also says what it's waiting on: **Permission**, **Question**, **Plan review**, or **Prompt not sent**. A session with an unanswered Kepler approval request counts as waiting, even while its agent keeps working, and reads **Approval needed** (or **Approval needed, destructive**). A live session that stopped after a failed turn, such as a rate limit, an exhausted quota, or an overloaded agent, reads **Error**.

When a session's turn ends but something it started keeps going in the background, such as a shell or a monitor, the session reads **Background task running**. Its dot looks idle: gray, with a green ring that does not pulse. It has its own count in the hover card rather than joining **Running**, and it does not keep the machine awake. See [Agent Sessions](/kepler/agent-sessions).

A dormant session shows as an outlined dot rather than a filled one. Hover the dots to see a card titled with the number of agent sessions, followed by a count of each state, most urgent first. When only one session is in a state, the card names that session. A dormant session is marked *(ended)*, as in *2 Waiting (ended)*.

***

## Starting work from a row

Click the **Action** button on a Todo row to hand the item to an agent with its context already attached: the repository, the issue body, the branch, and the diff. You do not need to copy or paste anything.

<figure style="text-align:center">
  <a href="/wp-content/uploads/actions-drop-down.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/actions-drop-down.png" class="help-center-img img-bordered" alt="The Action dropdown open on a Todo row, listing Plan, Implement, Review, and Address Feedback">
  </a>
  <figcaption style="text-align:center; color:#888">The Action dropdown, opened from the chevron next to the button.</figcaption>
</figure>

The left half of the button runs your preferred Action for that kind of item, and the chevron opens the full list. The defaults are:

- **Plan** for issues
- **Address Feedback** for pull requests you authored
- **Review** for everyone else's

You can change all of these defaults. See [Actions](/kepler/actions).

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

**From the keyboard**, the list is a single tab stop. Move through it like a tree with these keys:

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

A new task appears in the list as soon as you press **Start** in the **New task** composer, before its worktrees are ready. While Kepler sets it up, its row shows a **Preparing** pill, or a **Failed** pill if setup fails. You cannot drag or select a task that's still being prepared. The task's panel shows Kep, Kepler's mascot, narrating each step:

- *Fetching {repo}.* while a repository clones, with **Cancel**
- *Making your worktree.*
- *Starting {agent}.*
- *Opening the chat.* (or *Opening the terminal.*)

If setup fails, Kep says *That didn't go through.* (or *Task not started.* after you cancel). Choose **Edit and retry** to change the task and start it again, or **Dismiss**. When Kep is hidden, the panel shows **Getting your task ready** with *Cloning {repo}…* or *Setting up worktrees…*, and a failure reads **Unable to start this task**. When a task starts without some of its repositories, Kepler warns *Some repositories weren't added* and names them.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-task-preparing-panel-01-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-task-preparing-panel-01-v2@2x.png" class="help-center-img img-bordered" alt="Tasks in progress with a new task, Add a gift-card field to checkout, in Recent with the Preparing pill and its spinner. Its side panel, also marked Preparing, reads Getting your task ready and Setting up worktrees….">
  </a>
  <figcaption style="text-align:center; color:#888">A new task while Kepler prepares it, in the list and in its panel.</figcaption>
</figure>

Shift-click selects a range from your last plain click, as it does in Finder or VS Code. You can open up to 16 panels at once. In the **Columns** panel layout, opening another closes the leftmost unpinned one. For **Grid**, see [Lay panels out in a grid](#lay-panels-out-in-a-grid).

Each panel gets its own column as soon as you open it. Until its item loads, the column shows a placeholder that says the item is loading, is gone, or could not be loaded, with **Try again** when retrying can help. A pull request or issue opened while you're signed out reads *Sign in to see this pull request* (or issue) with **Sign in**. You can close any placeholder. If Kepler remembers a panel for a task that has since been deleted, that panel closes on its own.

<figure style="text-align:center">
  <a href="/wp-content/uploads/multi-task-panels-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/multi-task-panels-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Two task panels open side by side beside the Tasks in progress list: Fix the cart total (In Development, pinned) and Upgrade the payment SDK (In Review), each with its own header, worktree button, session tab and chat.">
  </a>
  <figcaption style="text-align:center; color:#888">Several panels open side by side, each with its own chat.</figcaption>
</figure>

**Resize.** Drag the divider between 2 columns to resize the one on its left. Hold **Shift** as you drag to give every panel the same width at once. Double-click the divider, or press **Home** on it, to split the space evenly again. The list keeps a minimum width of its own, so a wide panel cannot shrink it too far. Kepler remembers the widths per window, across reloads, restarts, and segment switches.

**Scroll.** Once the panel strip grows wider than the window, it scrolls instead of squeezing the columns below a readable width. Scroll it sideways with **Shift** and the mouse wheel, or a sideways trackpad swipe, even over a terminal.

**Reorder.** Drag a panel by its header to a new place in the strip. A panel's **Panel actions** menu (**⋮**) offers **Move panel left** and **Move panel right**, and so do **Cmd/Ctrl+Alt+Shift+←** and **Cmd/Ctrl+Alt+Shift+→**. The older **Cmd/Ctrl+Alt+←** and **Cmd/Ctrl+Alt+→** still work.

**Maximize.** Once 2 or more panels are open, **Maximize panel** in the **⋮** menu (or **Cmd/Ctrl+Shift+M**, or a double-click on empty header space) widens one panel across the strip, leaving a narrow edge of each neighbour in view. Click anywhere outside it, or use the **Restore panel** button in its header, to put the layout back exactly as it was. If you switch to another panel from the keyboard, that panel is maximized instead, so you can read panels one after another at full size.

**Move between panels.** **Ctrl+Tab** opens **Recent panels**, a switcher of your open panels and the ones a plain click replaced since, most recently used first, so you can switch back to an item you moved away from. **Delete** or **Backspace** closes the highlighted panel, or removes a panel that's no longer open from the list (**Remove from recent panels**). With 2 or more unpinned panels open, the switcher moves among the open ones only. **Cmd/Ctrl+1** through **Cmd/Ctrl+8** jump to a panel by its position from the left, and **Cmd/Ctrl+9** to the last.

If you start a task from **New task** while you're on the list, the new task opens as a panel and the list stays where it was, instead of switching to the task's page.

When the list reorders under you, such as when a session finishes or a task moves to another section, the row you have selected slides to its new position rather than jumping, so you can see where it went.

**Open several at once.** Each section's header has a button that opens that section's rows in panels, up to the panel limit: **Open all {count} in this section in panels**. When not everything fits, the button reads **Open {opened} of {total} in this section in panels**, and Kepler tells you how many did not fit. A group's chip offers **Open group** for its tasks. The whole list has no **Open all** button.

**Hide the list.** With at least one panel open, the toggle at the start of the Dashboard header, **Hide list** (**Cmd/Ctrl+B**), hides the list so the panels get the full width. With no panel open, the toggle is locked: *Open a task to hide the list*. While the list is hidden:

- Hover the toggle, now **Dock list**, to see the list float over the panels as the **Task list** (or **Todo list**). **Cmd/Ctrl+Shift+B** shows the floating list or hides it again.
- Click a row in the floating list to open it. The list closes and focus moves into that panel; **Escape** closes the list while focus is in it.
- Drag the floating list's edge (**Resize list**) to resize it, and double-click the edge to reset it.
- When a task in the hidden list needs you and has no panel open, the toggle shows the task's status dot and reads **Dock list ({status})**.
- **Dock list**, or **Cmd/Ctrl+B** again, brings the list back beside the panels.

A hidden list always uses the **List** layout. Kepler remembers per window whether the list is hidden and how wide it floats. **Cmd/Ctrl+B** works from a terminal on macOS only; on Windows and Linux a focused shell keeps **Ctrl+B**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-list-floating-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-list-floating-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The dashboard with the task list hidden and an open task panel taking the window: hovering the Dock list button at the start of the header floats the task list over the panel, with Fix the cart total highlighted as the open task, and the button's tooltip reads Dock list, Ctrl+B, and Ctrl+Shift+B shows it floating.">
  </a>
  <figcaption style="text-align:center; color:#888">The hidden task list, floating over a panel from the Dock list button.</figcaption>
</figure>

### Lay panels out in a grid

<figure style="text-align:center">
  <a href="/wp-content/uploads/dashboard-grid-formation-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/dashboard-grid-formation-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Dashboard with five task panels in a 3 by 2 grid beside a narrow task list. The Panel layout popover is open under the 3 × 2 toolbar button: a Columns and Grid switch with Grid selected, a grid of cells with the top-left 3 by 2 block highlighted, and 3 × 2, 6 panels, Up to 16 panels, fewer in smaller windows.">
  </a>
  <figcaption style="text-align:center; color:#888">Panels in a 3 × 2 grid, with the Panel layout popover open.</figcaption>
</figure>

Open panels sit side by side in **Columns** by default. To see more of them at once, switch the **Panel layout** to **Grid**, from its button in the toolbar or with **Cmd/Ctrl+Shift+L**. The button shows the current layout, such as **3 × 2**.

In the **Panel layout** popover, pick a **Grid size** from the matrix of cells. The default is 3 × 2, and cells past the 16-panel limit are faded and cannot be picked. The footer says how many panels the size holds, and *Up to 16 panels, fewer in smaller windows*. Kepler keeps the size you picked but draws only what the window fits, and the button's tooltip says what this window shows. **Reset sizes** evens out rows and columns you've resized. On a phone, panels always use **Columns**.

In a grid:

- Drag the dividers between grid columns (**Resize grid column**) and rows (**Resize grid row**). Hold **Shift** to resize every track at once, and double-click a divider or press **Home** on it to even them out.
- Panels that do not fit the grid go on further pages that scroll sideways.
- Drag a panel by its header to reorder it, row by row. **Move panel up** and **Move panel down** (**Cmd/Ctrl+Alt+Shift+↑** and **Cmd/Ctrl+Alt+Shift+↓**) join the left and right moves.
- **Maximize panel** spreads one panel over its page.
- Panels in short cells start with their headers folded, until you unfold them.
- Opening a panel never closes another. Once the grid is full, Kepler does not open the new panel and says *The grid is full ({count} panels). Close one to open another.*

### Pin a panel

<figure style="text-align:center">
  <a href="/wp-content/uploads/pin-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/pin-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task panel's Task actions menu open from its header, with Pin panel highlighted.">
  </a>
  <figcaption style="text-align:center; color:#888">Pin panel, in a panel's ⋮ menu.</figcaption>
</figure>

An unpinned panel is for browsing: a plain click on another row replaces it. To keep a panel in place, choose **Pin panel** from the panel's **⋮** menu. After you pin a panel:

- A plain click on a row opens beside your pinned panels instead of replacing them.
- Following a link in **Related** replaces an unpinned panel in place, but opens the linked item beside a pinned one.
- Switching segments keeps the pinned panels and closes the rest.
- Kepler never closes a pinned panel to make room when the maximum number of panels is open.

Kepler always keeps one panel unpinned for browsing, so browsing never has to close a pinned panel. Once every other panel is pinned, the menu item reads **Keep one panel unpinned for browsing** and you cannot pin another. To release a pinned panel, click **Unpin panel** in its header.

<figure style="text-align:center">
  <a href="/wp-content/uploads/unpin-panel-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/unpin-panel-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A pinned panel's header for Fix the cart total, with the Unpin panel button showing its tooltip between Terminal and the close button, above the task's worktree button.">
  </a>
  <figcaption style="text-align:center; color:#888">Unpin panel, in a pinned panel's header.</figcaption>
</figure>

***

## The side panel

Select a row to open its side panel beside the list. The side panel shows everything about the item in a stack of collapsible, resizable sections.

<figure style="text-align:center">
  <a href="/wp-content/uploads/issue-side-panel-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/issue-side-panel-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The side panel for GitHub issue #38, Cart total ignores discounts when tax is applied, as a stack of sections: its header with the Open on GitHub, panel menu, Plan Action and Close buttons, the GITHUB and ISSUE #38 chips, Open, acme-web, the linked task's session dot, the age, and alex-lee as Assignee; Summary with the bug label and the description; Related (1) listing the task Fix the cart total, In Review; and that task's session with its conversation and composer.">
  </a>
  <figcaption style="text-align:center; color:#888">The side panel, with its stack of collapsible sections.</figcaption>
</figure>

A section appears only when it has something to show:

| Section | What's in it | When it's there |
|---|---|---|
| **Summary** | The issue or pull request description, with its labels shown as badges. You can select and copy the description text | An issue or pull request that has a description. Tasks carry none of their own |
| **Related ({count})** | Every task ever linked to the issue or pull request, archived ones included, counted in the heading so a folded pane still says how many. Click a live task to open it in the panel, or an archived one to open its task page without restoring it | An issue or pull request with at least one linked task; a task shows its own pull requests and issues as chips instead |
| **What's running** | The chat: session tabs and draft session tabs. A session tab holds the live agent conversation, and a draft tab holds a prompt box plus the same Actions | Always, on an item you can start work on. You can resize it but not fold it, because the chat is the panel's main purpose |
| **Plan** | The plan the conversation on screen has proposed | The agent produced one |
| **Changes** | The checkout's commits, working changes, and file diffs, in the [side pane](#the-side-pane) | You opened a worktree's changes from its worktree button |
| **Terminals** | Terminal tabs across the task's checkouts. A shell tab shows its program's status, such as **Running**, **Needs you**, **Done** or **Failed**, when the program reports one | While a terminal is open. Its **✕** hides the section without stopping the shells, and the header's terminal control or **Cmd/Ctrl+J** shows it again |

Kepler sizes **Summary** and **Related** to fit their contents, and the chat takes the remaining height.

To reorder the tabs in **What's running** or **Terminals**, drag a tab to a new place. Kepler remembers each task's terminal tab order and selected terminal across reloads and in new windows. When you close the selected terminal, Kepler selects the leftmost terminal that remains.

To archive a session from the keyboard, focus its tab in **What's running** and press **Delete**. Kepler asks first: *Archive session?*, *Stops the agent and moves {session} to Archived sessions. Restore it any time.* The tab's own archive control and its menu item archive in one click, without asking.

A plain shell tab takes the name of what's running in it: the app that reports its status, the foreground job (such as `pnpm dev`), or on Windows the window title the program set. When the shell returns to the prompt, the tab returns to its own label, such as *Terminal 2*. When the 2 names differ, hover the tab to see the label and the job's command line or title.

Hover a tab with a program status to see how long the program has been in that state and its progress as a bar. For a program that's blocked or failed without saying why, the tab also says what to do next, such as *Approve it in the terminal.*

If an agent fails after you start a session, **What's running** shows **{agent} was unable to start** with the agent's message. Press **Retry** to launch it again, or **Open agent settings** to fix the problem.

For an issue or pull request with no task yet, the side panel's primary button runs the item's preferred Action, such as **Plan**, **Implement**, **Review**, or **Address Feedback**. If the preferred Action is **None**, no longer exists, or cannot apply to this kind of item, the button reads **Start** instead.

In the side panel for a task, the primary button reads **Start**. Once a session exists, the composer becomes that session's chat, and the button reads **Send**.

If you created a task with a prompt but have not started it, its composer reads *Start with the task prompt, or describe something else…*. Press **Start** with the box empty to send the task's prompt as the first message, or type something to send that instead.

The side panel's header holds:

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-preview-header-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-preview-header-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task's side panel header: the fold chevron, the task title Upgrade the payment SDK, Open task page, the ⋮ Task actions menu, the In Review progress control, the Terminal button and Close, above its worktree button with the kepler/payment-sdk-v5 branch in acme-web, 1 uncommitted file and the main merge target.">
  </a>
  <figcaption style="text-align:center; color:#888">The side panel's header, on a task.</figcaption>
</figure>

- The item's badges and reference
- On an issue or pull request, the people on it: a pull request's author, its **Assignees**, and its reviewers, each ringed and badged by the state of their review with a tally such as *1 of 2 reviewed*, or an issue's assignee. The reviewers collapse to a row of avatars
- The title, with a dot when a session needs you: blue for an unread turn, orange for one waiting on you
- The progress control, on a task
- The terminal control, on a task
- **Restore panel**, when the panel is maximized
- **Unpin panel**, when the panel is pinned
- **Close panel** (**Cmd/Ctrl+W** on the focused panel)
- **Panel actions** (**⋮**): **Close panel**, **Open task page**, **Open on {provider}** for an issue or pull request, **Pin panel**, **Maximize panel**, **Move panel left**, **Move panel right**, **Close other panels**, and **Close all panels**. On a task, these items are part of its **Task actions** menu. **Maximize panel**, the move items, **Close other panels**, and **Close all panels** appear only when more than one panel is open

An issue or pull request also has a status line with its provider state, session dots, repository, and last activity, and the people on it appear in the header. A task has no status line, because the row you clicked already shows that information.

Each pull request, issue, or artifact linked to a task has a chip under the header. Hover a chip to see its card, or click it to read the item in the side pane. A pull request whose branch name was used before reads *Opened from an earlier branch with the same name*. The **Resources** chip opens the task's **Resources** list in the [side pane](#the-side-pane), or closes it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/artifact-chip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/artifact-chip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The artifact attached to the task as a link chip, Acme gift cards, under the task's worktree button, with its hover card open showing the artifact's title, its link, Open and Copy link.">
  </a>
  <figcaption style="text-align:center; color:#888">A linked item's chip under the header, with its hover card.</figcaption>
</figure>

Hover a task's title to read its prompt, cut off after 10 lines, with the hint *Double-click to rename*. To copy the whole prompt, use **Copy task prompt** in the **⋮** menu. The prompt is a context item of its own, labeled **Prompt**. It appears first among the task's notes in the card, the preview, and the task page's context panel, and you cannot delete it.

To rename a task, double-click its title, choose **Rename task** from its **⋮** menu, or press **F2** on its focused panel, then edit the name in place. Press **Enter** to save the change, or press **Escape** or click away to discard it.

To fold the header down to its title row, use the chevron beside the title. This works on a task, a pull request, or an issue, and each segment remembers its own fold. A folded pull request header still shows its number and review decision. A folded task header shows a row of icons, each of which opens a view in the side pane:

- **Show changes**: the changes of the worktree on its worktree button
- **Show pull request**: the pull request that asks the most of you
- **Show issue**: the unfinished issue updated last
- **Show resources**: the **Resources** list

Each icon shows as pressed while its view is open. In the narrowest panels, the icons fold into one paperclip icon that opens the **Resources** list.

A Done task with no unpushed work, and no agent working, waiting on you, or keeping background work alive (such as a dev server), shows *Ready to archive?* in its header. See [Arranging Your Work](/kepler/arranging-your-work).

An archived task reads **Archived** where its progress control would be, in both its preview and its detail header, so you can tell a filed task from a live one.

### The side pane

<figure style="text-align:center">
  <a href="/wp-content/uploads/dashboard-side-pane-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/dashboard-side-pane-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A wide task panel for Fix the cart total with the Prompt note open in its side pane, right of the session. The panel's header reads In Review and holds the worktree card (kepler/fix-cart-total, its #51 pull request marked Changes requested, 2 uncommitted, main) and the #51 Open and #38 Open chips; the session shows its conversation and composer; the side pane's title row holds the resource switcher on Prompt, Copy, Edit and Close side pane, with the note's text below.">
  </a>
  <figcaption style="text-align:center; color:#888">A note open in a task panel's side pane, beside the session.</figcaption>
</figure>

A task panel opens its linked items, resources, and changes in a **side pane**, so you can read them without leaving the list for the task page. The following open in the side pane:

- A linked pull request or issue chip
- The **Resources** list, from the **Resources** chip, and any row in it
- The uncommitted or commits chip on a worktree button

The **Resources** list holds everything the task carries, in the order of the header: **Pull requests** (those that need your action first, with *Checks failing* where they are), **Issues**, notes, files, folders, links, and **Related tasks**. Click a group's heading to fold the group. A folded **Pull requests** heading still says how many need your action. Each row has a **⋮** menu, and a link row has **Open in browser**. When the task has no resources, the list reads *Keep notes, files and links with this task.* with **Add resource…**.

When the panel is at least 960 pixels wide, the pane opens beside the sessions. Drag its edge (**Resize side pane**) to resize it, and close it with **Close side pane** or **Escape**. In a narrower panel, the pane takes the sessions' place, with **Back to sessions** to return. The pane shows the same view of the item as the task page does.

Click the same chip again to close the pane. To move between the task's linked items and resources without closing the pane, use the switcher in the pane's title row. Its menu starts with **All resources** and ends with **Add resource…**. On the focused panel, 2 shortcuts show or hide the pane:

- **Cmd/Ctrl+Shift+G** shows or hides the worktree's changes.
- **Cmd/Ctrl+Shift+E** shows or hides the **Resources** list, even when the task holds nothing yet.

Kepler remembers the open pane for each item and the pane's width for each window.

### Issue comments

<figure style="text-align:center">
  <a href="/wp-content/uploads/issue-comments-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/issue-comments-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Fix the cart total panel (In Review, its worktree card with #51 marked Changes requested, and the #51 Open and #38 Open chips) with GitHub issue #38 open in its side pane: Back to sessions, the issue title Cart total ignores discounts when tax is applied, the GITHUB and ISSUE #38 chips, Open, acme-web and the assignee alex-lee, the bug label and the description, then Comments · 3 with Refresh comments: jo-park, sam-ortiz and alex-lee, each with an avatar, an age and the comment text.">
  </a>
  <figcaption style="text-align:center; color:#888">An issue's comments, under its summary in the side pane.</figcaption>
</figure>

An issue you open in a side pane, or on the task page, shows its discussion under the summary as **Comments**, with the count in the heading. Each comment has the author's avatar and name, how long ago it was posted, and its text. Kepler reads the newest 100 comments through the same connection it uses for the issue. In the **Comments** section:

- **Show earlier comments** reveals older ones that Kepler already loaded. When the issue has more than that, the section says that more may be available on the provider.
- **Refresh comments** reads them again.
- With none yet, the section reads *No comments yet.* When a read fails, it reads *Unable to load comments.* with **Retry**.

Comments work for GitHub, GitHub Enterprise, GitLab, GitLab Self-Hosted, Jira, and Jira Server issues. For other providers, when you're signed out, or when the connected account cannot read the issue's comments, the section says so instead. Kepler shows comments to you but does not pass them to the agent as task context.

### The worktree button

Below the header, each of the task's checkouts appears as a **worktree button** with 2 rows: what identifies the checkout on top, and what's in it below.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-preview-header-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-preview-header-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task's side panel header: the fold chevron, the task title Upgrade the payment SDK, Open task page, the ⋮ Task actions menu, the In Review progress control, the Terminal button and Close, above its worktree button with the kepler/payment-sdk-v5 branch in acme-web, 1 uncommitted file and the main merge target.">
  </a>
  <figcaption style="text-align:center; color:#888">A task's worktree button, below the header.</figcaption>
</figure>

The button's rows hold:

| Row | What it shows |
|---|---|
| **Top** | The branch and repository, the worktree's own pull request, and the upstream control |
| **Bottom** | Chips for uncommitted files, commits, and the merge target, plus **Open in** and **Run** |

The button's controls do the following:

- **Branch name**: opens or closes the worktree's changes in the side pane (**Open worktree changes** / **Close worktree changes**). Its **⋮** opens the [worktree menu](#the-worktree-menu).
- **Upstream control**: runs the action its counts call for. It offers **Pull** when the branch is behind, **Push** when it's ahead, and **Publish** when the branch is not on a remote yet. When the branch has diverged, or after you apply a rebase, it offers **Force push** after a confirmation. **Fetch** and the upstream row are in its chevron menu.
- **Uncommitted** and **commits** chips: open the worktree's changes in the side pane, on that scope. Click the chip that's showing again to close the side pane, or the other chip to switch scope.
- **Merge target** chip: shows how the branch compares with its merge target. Its menu also offers **Rebase onto {target}** and **Merge {target} into this branch**, which open the update view. See [Review Changes](/kepler/review-changes#updating-from-the-base).
- **Open in**: opens the checkout in your default editor. Other editors are in its chevron menu.
- **Run**: runs one of the repository's commands.

The button tells you what needs doing rather than only counting: unpushed commits, a paused rebase or merge you can continue or abort from the button, a merge target it was unable to read (with a retry), an explanation of a detached HEAD, and **No changes** only when there are none. Hover any chip to see a card that starts with what a click does, or right-click the chip for the worktree's menu. As the panel narrows, the chips shrink to their icons and counts rather than disappearing, and the branch name is cut last.

#### The worktree menu

The worktree menu is the same wherever a worktree appears, on the worktree button and on the task page. It holds:

- **Open changes** (or **Close changes** while they're showing), **Open in**, and the worktree's pull request
- **Continue {operation}** and **Abort {operation}** during a stopped rebase or merge
- A **Branch** submenu: **Rename branch**, **Rebase onto {target}** and **Merge {target} into this branch**, **Push**, **Pull** and **Fetch**, **Set upstream** or **Change upstream**, and **Change merge target…**
- **New session here**, **New terminal here**, and **Run command here**
- **Copy branch name**, **Copy worktree path**, and **Copy remote URL**
- **Detach worktree…** and **Delete worktree…**, or **Recreate worktree** for a checkout that's gone

**Set or change the upstream.** **Set upstream** (or **Change upstream**, which shows the branch tracked now) opens **Search remote branches**, a searchable list of remote branches. The list shows, in this order:

- A tracked branch that no longer exists, marked **Not found**
- Any remote's branch with the same name, marked **Same name**
- The other remote branches

The branch tracked now is marked **Current**. Above the list, Kepler pins **Publish as {remote}/{branch}…** when no remote has a branch of the same name, and **Unset upstream** when the branch tracks one. To fetch the list again, click **Refresh branches** beside the search box. Any remote branch can be the upstream, under any name, and **Push** then pushes there. The upstream item is hidden on a detached HEAD.

**More than one worktree.** A task's worktrees collapse into one worktree button, which starts with a count such as *1/3*. Step through them with the switcher on the branch name, or with the up and down arrow keys on the button. Until you pick one, the button shows the worktree with the latest changes. To see them all at once, use the toggle on the button's leading edge (**Show all {count} worktrees**). Worktrees whose branches have merged share a single row, from which you can delete them through the same cleanup list that archiving uses.

From the keyboard, a worktree button is 2 tab stops, one for its changes and one for its actions. Use the left and right arrow keys to move inside each.

When a task has more than one checkout, the terminal strip's **+** opens a chooser that lists the checkouts by branch.

***

## Back and forward

**Back** leaves the place or mode you're in. It does not undo a search you typed, a filter you set, or a change of view mode. If you narrow the list and then press **Back**, you leave the list instead of stepping back through every keystroke.

Use these shortcuts to go back and forward:

| Command | Mac | Windows / Linux |
|---|---|---|
| **Back** | ⌘ [ | Alt + ← |
| **Forward** | ⌘ ] | Alt + → |

The **Back** and **Forward** buttons in the top bar do the same, and so do a mouse's side buttons. On macOS, a 2- or 3-finger sideways swipe on a trackpad or Magic Mouse also goes back and forward, wherever nothing under the pointer scrolls sideways. On Windows and Linux, a sideways scroll or a mouse's tilt wheel never goes back, so an accidental scroll cannot take you away from what you were reading.

Each set of open panels gets its own history entry, so **Back** closes the set you just opened rather than the whole visit. Each Settings page you open gets its own entry too, so **Back** steps through the Settings pages you visited. To leave Settings in one step, use the back arrow in the Settings header, which returns you to what you were doing before you opened it.

***

## Empty states

When a view has nothing to show, or Kepler cannot load it, you see one of these messages:

| What you see | What it means |
|---|---|
| **Your agents' work lives here** | You have no tasks. **Tasks in progress** shows the **New task** composer, with hints to add an issue, a pull request, or a repository or folder, to start from a saved Action, or to **Open an external session**. After the guided setup it reads *You're set up* above the heading |
| **No tasks yet** | The tasks list is empty |
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
  <a href="/wp-content/uploads/tasks-empty-state-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/tasks-empty-state-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Tasks in progress empty state: the heading Your agents' work lives here and a line on what a task is, then Add issue, Add PR and Add context above the composer (Describe a task or ask a question…, the agent pill and Start), Add repo or folder below it, handwritten hints pointing at each, and an Open an external session card under an or divider.">
  </a>
  <figcaption style="text-align:center; color:#888">Tasks in progress with no tasks yet.</figcaption>
</figure>

### Kep

Kep, Kepler's planet mascot, appears on empty and waiting screens:

- The loading screen while Kepler starts
- A new session's empty chat
- Empty views
- Loading spinners
- The **About Kepler** dialog and What's New
- The crash and sign-in error screens

When your search or filters leave the list empty, Kep sleeps above the message. On a crash screen, **Show details** reveals **Error details**, with **Copy details** for a bug report.

<figure style="text-align:center">
  <a href="/wp-content/uploads/kep-empty-chat-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/kep-empty-chat-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A new session's empty chat in a task panel: Kep, Kepler's planet mascot, above What should the agent work on? and Describe the task, add a file with @, or type / for commands. Below them the draft composer reads Start with the task prompt, or describe something else…, with Task context, the agent pill and Start, and the Task folder picker under it.">
  </a>
  <figcaption style="text-align:center; color:#888">Kep over a new session's empty chat.</figcaption>
</figure>

Kep's eyes follow your pointer unless your system is set to reduce motion. Kepler can also show Kep without his speech card, or hide him. When Kep is hidden, Kepler shows the plain text and icons he would replace.

---
