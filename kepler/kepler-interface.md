---
title: The Kepler Interface
description: "Kepler's Dashboard shows the issues and pull requests that involve you, alongside the tasks you already have running. Learn how to read it, work several items side by side, and start work from it."
product: Kepler
feature: Kepler Interface
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, azure-devops]
integrations: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, azure-devops, jira, linear, trello, asana]
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [interface, dashboard, todo, tasks, draft-sessions, issues, pull-requests, actions, sessions, panel, preview, worktrees, progress, keyboard, navigation, go-to-task, command-palette, automations, windows, updates]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "kepler-core-concepts"
    nav_label: "The Kepler Interface"
    nav_order: 10
    nav_parent: "kepler-core-concepts"
    page_type: "content"
    card_icon: "layout-dashboard"
    card_color: "purple"
    card_description: "Read the Dashboard of issues, pull requests and tasks, and start work from any row"
---
<kbd>Last updated: November 2026</kbd>

Kepler's Dashboard shows your work: the issues and pull requests that involve you across your connected trackers and Git hosts, beside the tasks you already have running. To start work, pick an item from the list instead of describing it from scratch.

You can arrange the Dashboard to fit how you work. See [Arranging Your Work](/kepler/arranging-your-work).

***

## The top bar

The top bar holds the following controls, from the leading edge:

- The window switcher
- **Back** and **Forward**, in the desktop app only
- **New task**
- The Dashboard's views, when you place them in the title bar. By default they sit in a row below it. See [The Dashboard's views](#the-dashboards-views).
- Your setup progress, until you finish the primary setup steps
- **Stop reading**, on every page while Kepler reads an agent's reply aloud. Click it to stop. Hover it to see the sentence being read. See [Read aloud](/kepler/voice-input#read-aloud).
- The remote indicator: the environment chip that shows which machine this window works on
- **Remote Access**, a monitor-and-phone button whose color shows whether Remote Access is on. Hover it to turn Remote Access on or off and, while it's on, to scan its QR code or copy its link. See [Remote access](/kepler/kepler-remote-access).
- **Ask Kepler** (**Cmd/Ctrl+L** or **Cmd/Ctrl+K**), shown as Kep, Kepler's mascot, with the word **Ask**. It opens a chat and quick terminals in a panel beside the page. See [Ask Kepler](/kepler/ask-kepler).
- Feedback
- Settings
- Your account

The **Ask Kepler** button also shows the state of the panel's chats. When a chat needs you, has a new reply, or failed, the button becomes a **Needs you**, **New reply**, or **Failed** pill. Click the pill to open that chat. A focused shell keeps **Ctrl+L** for itself, so use **Ctrl+K** there.

While an update downloads, a chip near the trailing end of the top bar shows its progress. Hover the chip to see the version and about how long is left. You can keep working meanwhile.

When the update is ready, an **Update available** chip replaces the progress chip. It opens a popover that says what a restart does to running work, such as how many agents it stops, and offers **Restart to update**.

On Windows and Linux, the menu button at the leading edge of the top bar holds the full application menu (**File**, **Edit**, **View**, **Window**, **Help**), including **Settings**, **Check for Updates…**, and **About**. macOS keeps its native menu bar.

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

Menu items and button tooltips show a command's keyboard shortcut when the item does exactly what the key does, including a key you assigned yourself. To see every shortcut or change one, see [Keyboard shortcuts](/kepler/settings-app#keyboard-shortcuts).

### The window switcher

The **Windows** menu in the top bar lists every open Kepler window and what its agents are doing. Its button shows how many sessions are waiting or running in your other windows. In the menu:

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

Each window's title starts with the remote it's connected to and how many of its sessions are waiting on you. Each window keeps its own layout.

### The tray icon

Kepler's icon in the system tray (the menu bar on macOS) shows the most urgent thing your agents are doing, even when no window is open. The icon counts every agent session Kepler runs on this computer and on each remote machine that an open window connects to. It counts each session at one level, listed here from most urgent:

| Level | Which sessions |
|---|---|
| Needs your answer | Waiting on your answer or on an approval |
| Failed | A turn that ended in an error and that you have not opened |
| Finished | A finished turn you have not read |
| Working | Running a turn |

Hover the icon to see a count of each level. On macOS, a count of the agents that need a look (waiting, failed, or finished) appears beside the icon, in red while any of them is waiting or failed.

On Windows and Linux, click the icon to open the window that needs you. The icon's menu holds:

- **Open Kepler**
- **Windows**, a submenu with **New Window**, **New Local Window** when the window you used last is remote, and every open window, with a check beside the one you used last
- **Quit** and **Quit & End Sessions**

<!-- TODO(screenshot): New — ade-tray-menu-01: the Kepler tray icon's menu with Open Kepler, the Windows submenu open on New Window and the open windows, the current one checked, then Quit and Quit & End Sessions. -->

### New task

**New task** (**Cmd/Ctrl+N**) opens the **New task** composer. To start a task from a conversation you began outside Kepler, use **Open an external session** in the composer. See [Create a task](/kepler/create-task#from-a-session-you-already-started).

***

## The Dashboard's views

The Dashboard shows your work in views. To move between them, click a view in the row of views, which sits below the top bar by default.

<figure style="text-align:center">
  <a href="/wp-content/uploads/todo-task-in-progress-agent-graph-sep-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/todo-task-in-progress-agent-graph-sep-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Dashboard's row of views below the title bar: Todo and Tasks, selected, with Kepler's own Todo and Task icons, and Agent Graph with its graph icon, then New view. Tasks and Agent Graph carry an orange mark on their icons for a task waiting on you.">
  </a>
  <figcaption style="text-align:center; color:#888">The Dashboard's starting views: Todo, Tasks, and Agent Graph.</figcaption>
</figure>

Kepler starts you with 3 views:

| View | What it shows |
|---|---|
| **Todo** | Issues and pull requests from your connected integrations |
| **Tasks** | The tasks you already have running in Kepler |
| **Agent Graph** | A live graph of every task, session, turn, tool call, and file. See [The Agent Graph](/kepler/agent-graph) |

Each view keeps its own layout, grouping, sort, filters, search and, on a Todo view, scope. Changes you make in the view's **View** menu save automatically, and switching to another view and back restores its open panels. See [Arranging Your Work](/kepler/arranging-your-work).

The **Automations** button, after the views, opens your automations: agents that run on a schedule or when new GitHub or Jira activity matches a query. A count on the button shows the runs that need you. See [Automations](/kepler/kepler-automations).

To work with views:

- **New view** adds a **Todo**, **Tasks** or **Agent Graph** view, or a copy of the one you're on. Name it, pick its **Icon** and layout, then choose **Done**.
- Click the view you're on, or right-click any view, for its menu, with **Rename** (**F2**), **Change icon**, **Duplicate view**, **Views position**, **Delete view**, and more.
- Double-click a view to rename it. Drag a view to reorder the row.
- You always keep at least 1 **Todo** and 1 **Tasks** view.

The views show on every page. Pick one to go back to the Dashboard on that view.

Views can also sit in the top bar or down the left side of the window, as **Tabs** or **Pills**. Choose in the view menu's **Views position**, or in [Settings → Appearance → Dashboard](/kepler/settings-app#dashboard).

What a Todo view lists depends on its **Scope**, a switch in its **View** menu:

- **Mine**, the default: work created by you, assigned to you, mentioning you, or awaiting your review
- **All**: everything open in Kepler's repositories, plus your work elsewhere

Under **Mine**, each provider lists:

| Integration | Issues | Pull requests |
|---|---|---|
| **GitHub**, **GitHub Enterprise** | Yours, assigned to you or mentioning you | Yours, assigned to you or ones you review |
| **GitLab**, **GitLab Self-Hosted**, **Azure DevOps**, **Azure DevOps Server** | Yours or assigned to you | Yours or awaiting your review |
| **Bitbucket Cloud** | None | Yours, or awaiting your review in your workspaces and repositories added to Kepler |
| **Bitbucket Data Center** | None | Yours or awaiting your review |
| **Jira**, **Jira Server**, **Linear**, **Trello**, **Asana** | Assigned to you | None |

**Mine** covers every organization you belong to.

**All** adds every open pull request and issue of the repositories added to Kepler. On Bitbucket and Azure DevOps it adds pull requests only, and issue trackers add nothing. Under **All**, 2 more rows narrow the list:

- **Repos**: **All repos in Kepler**, or **Custom** to choose from a searchable list of your repositories with their open counts.
- **Updated**: **Last 7 days**, **Last 30 days**, **Last 90 days** (the default), or **Last year**.

**All repos in Kepler** skips a very large repository, one with 1,000 or more open pull requests or 2,000 or more open issues, and Todo says so. To load it anyway, click **Choose repos** and add it under **Repos**.

To browse issues outside the scope, use **New task** → **Issues** → **All visible**.

Work starts in **Todo** and moves to **Tasks** while it's underway. The **Agent Graph** view shows tasks as a graph instead of a list.

The Dashboard opens on the view you used last. The first time you start Kepler, a guided setup helps you connect your agents. See [Getting Started with Kepler](/kepler/kepler-getting-started). If you have no tasks yet, **Tasks** shows the **New task** composer. See [Empty states](#empty-states).

To fill **Todo**, connect at least one provider. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

### External sessions

Todo lists only issues and pull requests. To pick up an agent conversation you started outside Kepler, open **New task** and use **Open an external session**. See [Create a task](/kepler/create-task#from-a-session-you-already-started).

To learn what external sessions are and what you can do with them, see [Agent Sessions](/kepler/kepler-external-sessions).

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
- On a pull request, what it needs from you, such as **Changes requested**, or else your role: **Yours** or **Review**
- A **Task** badge (or **{count} tasks**) when tasks were already started from the item, or **Archived task** (**{count} archived tasks**) when every one of them is archived
- The repository
- A status pill
- Any session activity: the session dots of the task linked to the item, and that task's running terminals
- The people: a pull request's author and an avatar for each reviewer, ringed in the color of their review (green for approved, red for changes requested), or an issue's assignee
- When it last changed
- An Action button

Hover the avatars to see a card that names everyone on the item and shows where each review stands. An issue that's on your list only because it mentions you carries a muted **Mentioned** badge, so you can tell it apart from work assigned to you.

When a Linear issue is synced with a GitHub issue and both copies are listed, Todo shows one row for them: the Linear row. A task started from either copy counts as the issue's task, and a task started from the Linear row works in the GitHub copy's repository.

When a provider fails to load, Kepler keeps showing its rows from the last successful load, with a crossed-out cloud on their provider chip. A notice above the list names the provider and the fix, such as signing in again or **Retry**. If you do not need that provider, click **Filter out {provider}** beside its fix to hide it from Todo, so the notice stops reporting it. To show it again, clear it in **Filter**.

Right-click a Todo row to open its menu. It holds:

- **Open task page**, when the item already has a task
- **Open on {provider}**
- **Copy link** (**Cmd/Ctrl+C** on a focused row)
- **Copy title**
- **Copy number**
- **Copy branch name**, on a pull request

On the **Board** layout, a pull request's card also shows its branch.

The **Your role** grouping and filter sort items by your part in them:

| Role | Meaning |
|---|---|
| **Yours** | You authored the pull request. The row shows **Yours** |
| **Review** | You're a reviewer on it. The row shows **Review** |
| **Unattributed** | The provider did not say. The row shows no role |
| **Not mine** | Under the **All** scope, you have no part in the pull request or issue. The row shows no role |

### Task rows

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-row-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-row-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Unread group of the Tasks view with three task rows: Fix the cart total, Update checkout copy and Upgrade the payment SDK. Each row shows its title, the acme-web repository, its progress stage (In Development, On hold, In Review), New reply, its blue session dot, its age and the ⋮ menu. Fix the cart total is starred, so its filled Star button stays in view.">
  </a>
  <figcaption style="text-align:center; color:#888">Task rows, one of them starred.</figcaption>
</figure>

Each task row shows:

- The title
- The repository, or every repository when the task spans several
- The task's pull request and issue as chips, each with its state
- Its group, when it's in one: a colored bar on the **List** layout, or a chip on a **Board** card
- A progress control
- What the task needs from you
- Session activity, and a pill for its running terminals
- Time
- A **Star** button, shown when you hover or focus the row, and kept in view once the task is starred
- An **Automation** badge, on a task an automation started. Hover it to see the automation's query. See [Automations](/kepler/kepler-automations).

Star a task to mark it important. In the **Inbox** grouping, a starred task lists under **Important**, and in every sort except **Manual**, starred tasks list first in their section. To take the star off, click **Unstar**. On a touch screen, use **Star** in the task's menu.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-row-needs-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-row-needs-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Two task rows in the Tasks view, grouped by progress. Under In Development, Add product search shows acme-web, In Development, Approval needed for Run npm test in orange and an orange session dot. Under In Review, Fix the cart total shows acme-web, a pull request chip #51 and an issue chip #38, In Review, Changes requested in red, its session dot and a square for one running terminal. Each row ends with its age and the ⋮ menu.">
  </a>
  <figcaption style="text-align:center; color:#888">Task rows that say what they need from you, with pull request, issue and terminal chips.</figcaption>
</figure>

The needs cell gives the most pressing reason first, such as **Approval needed for {tool}**, **Waiting for you**, **Turn failed**, **Agent stopped** or **CI failing**. **Turn failed** means an agent's turn ended in an error. **Agent stopped** means the agent itself stopped with an error. On a task on hold, it says what the hold waits for, or why the hold lifted.

A failed turn, a stopped agent, failing CI, a new **Changes requested** review, or a hold that lifted on bad news moves the task into **Needs attention**.

Hover **Approval needed for {tool}** to answer the request, such as with **Allow** or **Reject**, without opening the task.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-row-answer-permission-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-row-answer-permission-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="Add product search's row in Needs attention with its Approval needed for Run npm test reason hovered, which opens the permission request itself below the row: the agent's message, the Run npm test call marked Needs approval, then Allow, Allow for this session, Allow always and Reject, and the task's other reason, New reply, under them. The hovered row shows its Star button.">
  </a>
  <figcaption style="text-align:center; color:#888">A permission request answered from its task row.</figcaption>
</figure>

When a session or a terminal in a task waits on you, the task's title shows in bold. Click the terminals pill to open the most urgent terminal, or the session dots to open the most urgent session.

Hover a pull request or issue chip to see its card, or click the chip to keep the card open. When the task has more than one link of that kind, the card lists them all. Right-click the chip for the link's menu.

On a **Board** card, hover the group chip to see a summary of the group's tasks. Click the chip for **Open group**, **Show only this group**, **Remove from group** and the grouping options. See [Arranging Your Work](/kepler/arranging-your-work).

A Done task that's ready to archive also gets an **Archive task** button on its row.

When the list is grouped by repository, a task that spans several repositories appears under each of them.

To manage a task, open its **⋮** menu or right-click its row. The menu holds:

- **Open task page** and **Open in new window**
- **Reopen**, while the task is Done, and a **Progress** submenu. See [Arranging Your Work](/kepler/arranging-your-work).
- **Mark as read** or **Mark as unread**
- **Star** or **Unstar**
- **Rename task** (**F2** on a focused panel) and **Add to group**
- **Move up**, **Move down**, and **Move to top of {section}**, while the list is sorted by **Manual**. See [Arranging Your Work](/kepler/arranging-your-work#sort).
- **Manage resources**, which opens the task's **Resources** screen
- **Refresh**, which re-reads the task's worktrees and its linked pull requests and issues
- **Copy task link** (**Cmd/Ctrl+C** on a focused row), a `kepler://` link to the task
- **Copy task prompt**
- **Panel**, a submenu with the panel's own items, on a task open in a panel. See [The side panel](#the-side-panel).
- **Shut down all agents**, which asks first while an agent is still working
- **Archive task**, or **Restore task** when the task is already archived
- **Delete task**

**Act on several tasks at once.** Open 2 or more tasks with **Shift-click** or **Cmd/Ctrl-click** (see [Open a panel](#open-a-panel)), then right-click any of them. The menu acts on the whole selection, and each label counts the tasks:

- **Progress of {count} tasks**, which sets the stage of every selected task
- **Mark {count} tasks as read** or **Mark {count} tasks as unread**
- **Star {count} tasks** or **Unstar {count} tasks**
- **New group with {count} tasks…**
- **Add {count} tasks to group**
- **Remove {count} tasks from group**
- **Shut down agents in {count} tasks**, which asks first while an agent is still working
- **Archive {count} tasks**
- **Restore {count} tasks**
- **Delete {count} tasks**

The menu shows only the items that apply, and grouping and **Progress** leave archived tasks out. **Archive**, **Restore**, and **Delete** ask first, with the same confirmation as a section's **Select** bar. If you right-click a task outside the selection, or use a row's **⋮** menu, the action applies to that task alone.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-selection-menu-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-selection-menu-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Tasks list grouped by your groups: the Checkout and Payments sections, then Ungrouped, where Add product search and Write the 2.4 release notes are selected and outlined, with the selection's right-click menu open below them: Progress of 2 tasks, Mark 1 task as read and Star 2 tasks, then New group with 2 tasks… and Add 2 tasks to group, then Shut down agents in 1 task, Archive 2 tasks and Delete 2 tasks.">
  </a>
  <figcaption style="text-align:center; color:#888">The menu for two selected tasks.</figcaption>
</figure>

Drag any selected task to move the whole selection. See [Act on several tasks at once](/kepler/arranging-your-work#act-on-several-tasks-at-once).

### Status

Task rows and Todo rows both show a status, but the 2 statuses mean different things:

| Where | Values | What it means |
|---|---|---|
| **Task rows** | **Exploration**, **In Development**, **In Review**, **On hold**, **Later**, **Done**, **Archived** | How far the *work* has got. Kepler derives it from the task's checkouts and pull requests, unless you or an agent set it by hand |
| **Todo rows** | **Open**, **Draft**, **Merged**, **Closed** for a pull request; the tracker's own state for an issue | The provider's own state on the pull request, and the workflow state your tracker uses for the issue (such as a Linear *In Progress* or a Jira *To Verify*) rather than a flat Open |

Kepler derives a task's stage from this evidence:

- **In Development**: uncommitted changes, or commits not yet merged into the base branch.
- **In Review**: an open or draft pull request of the task's own.
- **Done**: at least one of the task's branches has landed, the task has no open pull request of its own, and no checkout still carries commits that have not landed.
- **On hold**, **Later**, and **Archived**: filing decisions, not evidence.

A task sits at the furthest stage any of its checkouts reached, except **Done**, which follows its own rule.

**Done** waits for the work to land, however it got there, including a rebase or squash merge, or a merge with no pull request. A task that's done but still has uncommitted changes or unpushed commits in a checkout reads **Done · local changes**, so you can decide whether to keep them before you archive.

To set the stage yourself, click the progress control on its row. The same menu puts a task **On hold**, which pauses it until something happens, or sets it aside for **Later**. A Done task offers neither. See [Set a task's progress](/kepler/arranging-your-work#set-a-tasks-progress).

Each task row also shows one dot for each distinct session state, with a count of each.

<figure style="text-align:center">
  <a href="/wp-content/uploads/session-dots-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/session-dots-oct-2026.png" class="help-center-img img-bordered" alt="A task row's In Development pill beside two outlined session dots, an orange 2 and a blue 1, with a tooltip reading 2 Waiting (ended) and 1 Ready (ended).">
  </a>
  <figcaption style="text-align:center; color:#888">The status pill and session-state dots, with the breakdown on hover.</figcaption>
</figure>
<!-- TODO(screenshot): Replace — ade-session-dots-01: a v0.15 task row with two or more session states and a count above 1, one of them dormant so its dot is an outline, with the hover card open (its {count} agent sessions title and per-state tallies, for example 2 Waiting (ended), 1 Ready). The current figure stays until it's replaced. -->

The dots show what the *agents* are doing, which is separate from where the work stands, such as **Running**, **Waiting**, **Unread** or **Error**.

A waiting session also says what it's waiting on, such as **Permission** or **Question**. A session with an unanswered Kepler approval request reads **Approval needed**, even while its agent keeps working. A session that stopped after a failed turn, such as a rate limit, reads **Error**.

When a session's turn ends but something it started keeps going in the background, such as a shell, the session reads **Background task running**, with a solid green dot. See [Agent Sessions](/kepler/agent-sessions).

A dormant session shows as an outlined dot rather than a filled one. Hover the dots to see a count of each state, most urgent first.

***

## Starting work from a row

Click the **Action** button on a Todo row to hand the item to an agent with its context already attached: the repository, the issue body, the branch, and the diff. You do not need to copy or paste anything.

<figure style="text-align:center">
  <a href="/wp-content/uploads/actions-drop-down.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/actions-drop-down.png" class="help-center-img img-bordered" alt="The Action dropdown open on a Todo row, listing Plan, Implement, Review, and Address Feedback">
  </a>
  <figcaption style="text-align:center; color:#888">The Action dropdown, opened from the chevron next to the button.</figcaption>
</figure>

The left half of the button runs the suggested Action for that kind of item, and the chevron opens the full list. The defaults are:

- **Plan** for issues
- **Address Feedback** for pull requests you authored
- **Review** for everyone else's

You can change all of these defaults. See [Actions](/kepler/actions).

### Open a panel

<figure style="text-align:center">
  <a href="/wp-content/uploads/open-a-task-panel-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/open-a-task-panel-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Todo view, with two pull requests above three issues, GitHub issue #42 selected and its side panel open on the right: the issue header with Plan, the GITHUB, ISSUE #42 and Mentioned chips, its Summary with the bug and checkout labels and description, and a composer at the bottom, with #42 attached, for starting a task from it. Above are the row of views, with Todo selected, and the toolbar with the View button reading Type and Mine before the search box.">
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

On the **Board** layout, **←** and **→** move between columns. **Tab** leaves the list.

**Alt+Shift+↑** and **Alt+Shift+↓** (**⌥⇧↑** and **⌥⇧↓** on macOS) open the previous or next item in the list.

A new task appears in the list as soon as you press **Start** in the **New task** composer. While Kepler sets it up, its row shows a **Preparing** pill, and its panel shows each step, with **Cancel** while a repository clones. If setup fails, the row shows **Failed**. Choose **Edit and retry** to change the task and start it again, or **Dismiss**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-task-preparing-panel-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-task-preparing-panel-01-v3@2x.png" class="help-center-img img-bordered" alt="The Tasks view with a new task, Add a gift-card field to checkout, in Recent with the Preparing pill and its spinner. Its side panel, also marked Preparing, shows Kep narrating the launch: Making your worktree. So your other work stays put., over the task's steps, Setting up worktrees… (in progress), Starting OpenCode with your prompt and Opening the chat.">
  </a>
  <figcaption style="text-align:center; color:#888">A new task while Kepler prepares it, with Kep narrating in its panel.</figcaption>
</figure>

Shift-click selects a range from your last plain click, as it does in Finder or VS Code. You can open up to 16 panels at once. Once they're all open, opening another closes the unpinned panel you opened longest ago. To arrange the panels in rows, see [Lay panels out in a grid](#lay-panels-out-in-a-grid).

<figure style="text-align:center">
  <a href="/wp-content/uploads/multi-task-panels-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/multi-task-panels-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Two task panels open side by side beside the Tasks list: Fix the cart total (In Development, pinned, with its Unpin panel button) and Upgrade the payment SDK (In Review, the active panel, outlined), each with its worktree card, session tab, conversation and message box. Both tasks are highlighted in the list's Recent group, and the row of views and the toolbar run across the top.">
  </a>
  <figcaption style="text-align:center; color:#888">Several panels open side by side, each with its own chat.</figcaption>
</figure>

**Resize.** Drag the divider between 2 columns to resize the one on its left. Hold **Shift** as you drag to give every panel the same width or, with **Auto columns** on, to set how wide the columns should be. Double-click the divider to split the space evenly again. Each view remembers its own widths.

**Scroll.** Once the panel strip grows wider than the window, it scrolls instead of squeezing the columns below a readable width. Scroll it sideways with **Shift** and the mouse wheel, or a sideways trackpad swipe, even over a terminal.

**Reorder.** Drag a panel by its header to a new place in the strip. A panel's **Panel actions** menu (**⋮**) offers **Move panel left** and **Move panel right**, and so do **Cmd/Ctrl+Alt+Shift+←** and **Cmd/Ctrl+Alt+Shift+→**.

**Solo.** Once 2 or more panels are open, **Solo panel** in the **⋮** menu (or **Cmd/Ctrl+Shift+M**) widens one panel across the strip. Drag the soloed panel's edges to resize it, or click **Maximize** in its header to fill the space. Click outside it, or click **Unsolo panel** in its header, to put the layout back.

**Move between panels.** **Ctrl+Tab** opens **Recent panels**, a switcher of your open panels and the ones you replaced recently, so you can switch back to an item you moved away from. **Delete** or **Backspace** closes the highlighted panel, or removes it from the list. **Cmd/Ctrl+1** through **Cmd/Ctrl+8** jump to a panel by its position from the left, and **Cmd/Ctrl+9** to the last.

If you start a task from **New task** while you're on the list, the new task opens as a panel and the list stays where it was, instead of switching to the task's page. The panel opens beside the one you're reading, or at the end in a grid. To always open it at the end, change **Where a new task opens on the Dashboard** in [Settings → Tasks](/kepler/settings-tasks#new-tasks).

**Open several at once.** Each section's header has a button that opens that section's rows in panels, up to the panel limit. A group's chip offers **Open group** for its tasks.

**Hide the list.** With at least one panel open, the toggle at the start of the Dashboard header, **Hide list** (**Cmd/Ctrl+B**), hides the list so the panels get the full width. While the list is hidden:

- Hover the toggle, now **Dock list**, to see the list float over the panels as the **Task list** (or **Todo list**). **Cmd/Ctrl+Shift+B** shows the floating list or hides it again.
- Click a row in the floating list to open it. The list closes and focus moves into that panel; **Escape** closes the list while focus is in it.
- Drag the floating list's edge (**Resize list**) to resize it, and double-click the edge to reset it.
- When a task in the hidden list needs you and has no panel open, the toggle shows its status dot.
- **Dock list**, or **Cmd/Ctrl+B** again, brings the list back beside the panels.

A hidden list always uses the **List** layout. **Cmd/Ctrl+B** works from a terminal on macOS only; on Windows and Linux a focused shell keeps **Ctrl+B**.

When the window is too narrow for the list beside the open panels, Kepler hides the list, and the toggle reads **Show list**. Click it to float the list over the panels. The list returns when you widen the window.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-list-floating-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-list-floating-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Dashboard with the task list hidden and an open task panel taking the window: hovering the Dock list button at the start of the toolbar floats the task list over the panel, with Fix the cart total highlighted as the open task in Recent, and the button's tooltip reads Dock list, Ctrl+B, and Ctrl+Shift+B shows it floating. Above are the row of views and the search box and View button.">
  </a>
  <figcaption style="text-align:center; color:#888">The hidden task list, floating over a panel from the Dock list button.</figcaption>
</figure>

### Lay panels out in a grid

<figure style="text-align:center">
  <a href="/wp-content/uploads/dashboard-grid-formation-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/dashboard-grid-formation-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Dashboard with four task panels in a 2 by 2 grid beside a narrow task list grouped by Repository (acme-web, 4, and No repository, 1). The Panel layout popover is open under the 2 × 2 toolbar button: Auto columns unticked, a size matrix with a 2 by 2 block marked, and 2 × 2, 4 panels, Up to 16 panels, fewer in smaller windows.">
  </a>
  <figcaption style="text-align:center; color:#888">Panels in a grid, with the Panel layout popover open.</figcaption>
</figure>

By default, open panels sit side by side in 1 row, with **Auto columns**: as many columns as the window has room for. To see more panels at once, lay them out in a grid. Click **Panel layout** in the toolbar, whose button shows the current size, such as **Auto × 1** or **3 × 2**:

- Pick a size in the **Grid size** matrix. 1 row puts panels side by side, and 2 or more rows make a grid.
- Turn off **Auto columns** to choose a fixed number of columns.
- **Reset sizes** evens out rows and columns you've resized.

A grid holds up to 16 panels, fewer in smaller windows. In a grid:

- Drag the dividers between grid columns (**Resize grid column**) and rows (**Resize grid row**). Hold **Shift** to resize every track at once, and double-click a divider or press **Home** on it to even them out.
- Panels that do not fit the grid go on further pages that scroll sideways.
- Drag a panel by its header to reorder it, row by row. **Move panel up** and **Move panel down** (**Cmd/Ctrl+Alt+Shift+↑** and **Cmd/Ctrl+Alt+Shift+↓**) join the left and right moves.
- **Solo panel** spreads one panel over its page.
- Panels in short cells start with their headers folded, until you unfold them.
- Clicking rows opens and closes panels the same way as in 1 row. See [Open a panel](#open-a-panel).

### Pin a panel

<figure style="text-align:center">
  <a href="/wp-content/uploads/pin-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/pin-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="A task panel's Task actions menu open from the ⋮ beside its title, Fix the cart total: Open task page; Progress, In Development, Mark as unread and Star; Rename task (F2) and Add to group; Manage resources and Refresh; Copy task link and Copy task prompt; Panel, open on its submenu with Pin panel highlighted; then Shut down all agents, Archive task and Delete task.">
  </a>
  <figcaption style="text-align:center; color:#888">Pin panel, in the Panel submenu of a task panel's ⋮ menu.</figcaption>
</figure>

An unpinned panel is for browsing: a plain click on another row replaces it. To keep a panel in place, choose **Pin panel** from the panel's **⋮** menu (on a task, under **Panel**). After you pin a panel:

- A plain click on a row opens beside your pinned panels instead of replacing them.
- The pin stays with the view you pinned it in.
- Kepler never closes a pinned panel to make room when the maximum number of panels is open.

Kepler always keeps one panel unpinned for browsing, so once every other panel is pinned, you cannot pin another. To release a pinned panel, click **Unpin panel** in its header.

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
| **Summary** | The description and labels, which you can select and copy | An issue or pull request with a description |
| **Related ({count})** | Every task linked to the issue or pull request, archived ones included | An issue or pull request with at least one linked task |
| **What's running** | The chat: session tabs and draft session tabs | Always, on an item you can start work on. You can resize it but not fold it |
| **Plan** | The plan the conversation on screen has proposed | The agent produced one |
| **Changes** | The checkout's commits, working changes, and file diffs, in the [side pane](#the-side-pane) | You opened a worktree's changes from its worktree button |
| **Terminals** | Terminal tabs across the task's checkouts, each with its program's status when it reports one | While a terminal is open. **Cmd/Ctrl+J** shows or hides it without stopping the shells |

In **Related**, click a live task to open it in the panel, or an archived one to open its task page without restoring it. A task shows its own pull requests and issues as chips instead.

To reorder the tabs in **What's running** or **Terminals**, drag a tab to a new place. Kepler keeps each task's terminal tab order.

To archive a session from the keyboard, focus its tab in **What's running** and press **Delete**. Kepler asks first. The tab's own archive control and its menu item archive in one click, without asking.

A plain shell tab takes the name of what's running in it, such as `pnpm dev`. Hover a tab with a program status to see how long the program has been in that state, its progress, and, for a blocked or failed program, what to do next.

If an agent fails after you start a session, **What's running** shows **{agent} was unable to start** with the agent's message. Press **Retry** to launch it again, or **Open agent settings** to fix the problem.

For an issue or pull request with no task yet, the side panel's primary button runs the item's suggested Action, such as **Plan**, **Implement**, **Review**, or **Address Feedback**. When there is no suggested Action to run, the button reads **Start** instead.

In the side panel for a task, the primary button reads **Start**. Once a session exists, the composer becomes that session's chat, and the button reads **Send**.

If you created a task with a prompt but have not started it, press **Start** with the box empty to send the task's prompt as the first message, or type something to send that instead.

The side panel's header holds:

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-preview-header-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-preview-header-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task's side panel header: the fold chevron, the task title Upgrade the payment SDK, Open task page, the ⋮ Task actions menu, the In Review progress control, the Terminal button and Close, above its worktree button with the kepler/payment-sdk-v5 branch in acme-web, 1 uncommitted file and the main merge target.">
  </a>
  <figcaption style="text-align:center; color:#888">The side panel's header, on a task.</figcaption>
</figure>

- The item's badges and reference
- On an issue or pull request, the people on it: a pull request's author, assignees and reviewers, each reviewer marked with the state of their review, or an issue's assignee
- The title, with a dot when a session needs you: blue for an unread turn, orange for one waiting on you
- The progress control, on a task
- The terminal control, on a task
- **Unsolo panel** and **Maximize**, while the panel is soloed
- **Unpin panel**, when the panel is pinned
- **Close panel** (**Cmd/Ctrl+W** on the focused panel)
- **Panel actions** (**⋮**): **Close panel**, **Open task page**, **Open on {provider}** for an issue or pull request, **Pin panel**, **Solo panel**, **Move panel left**, **Move panel right**, **Close other panels**, and **Close all panels**. On a task, these items are part of its **Task actions** menu

An issue or pull request also has a status line with its provider state, session dots, repository, and last activity.

Each pull request, issue, or artifact linked to a task has a chip under the header. While a pull request is open or in draft, its chip ends with its CI status: failing, pending, or passing. Hover a chip to see its card, or click it to read the item in the side pane. The **Resources** chip opens the task's **Resources** list in the [side pane](#the-side-pane), or closes it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/artifact-chip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/artifact-chip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The artifact attached to the task as a link chip, Acme gift cards, under the task's worktree button, with its hover card open showing the artifact's title, its link, Open and Copy link.">
  </a>
  <figcaption style="text-align:center; color:#888">A linked item's chip under the header, with its hover card.</figcaption>
</figure>

Hover a task's title to read its prompt. To copy the whole prompt, use **Copy task prompt** in the **⋮** menu. The prompt also appears first among the task's notes, labeled **Prompt**, and you cannot delete it.

To rename a task, choose **Rename task** from its **⋮** menu, or press **F2** on its focused panel, then edit the name in place. Press **Enter** to save the change, or **Escape** to discard it.

To fold the header down to its title row, use the chevron beside the title. A folded task header has a run control, and a row of icons that each open a view in the side pane.

The run control runs the worktree's command, or opens the worktree in your editor when it has no commands. Its menu lists every command and an **Open in** submenu. The icons are:

- **Show changes**: the changes of the worktree on its worktree button
- **Show pull request**: the pull request that asks the most of you
- **Show issue**: the unfinished issue updated last
- **Show resources**: the **Resources** list

A Done task with no unpushed work, and no agent working, waiting on you, or keeping background work alive (such as a dev server), shows *Ready to archive?* in its header. See [Arranging Your Work](/kepler/arranging-your-work).

An archived task reads **Archived** where its progress control would be, in both its panel and its task page.

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

The **Resources** list holds everything the task carries: **Pull requests**, **Issues**, notes, files, folders, links, and **Related tasks**. Click a group's heading to fold the group. Each row has a **⋮** menu. To add a resource of one kind, click the **+** on its group's heading. To add or change resources, click **Manage resources**, which opens the task's **Resources** screen.

In a wide panel, the pane opens beside the sessions. Drag its edge to resize it, and close it with **Close side pane** or **Escape**. In a narrower panel, the pane takes the sessions' place, with **Back to sessions** to return.

Click the same chip again to close the pane. To move between the task's linked items and resources without closing the pane, use the switcher in the pane's title row. On the focused panel, 2 shortcuts show or hide the pane:

- **Cmd/Ctrl+Shift+G** shows or hides the worktree's changes.
- **Cmd/Ctrl+Shift+E** shows or hides the **Resources** list.

### Issue comments

<figure style="text-align:center">
  <a href="/wp-content/uploads/issue-comments-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/issue-comments-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Fix the cart total panel (In Review, its worktree card with #51 marked Changes requested, and the #51 Open and #38 Open chips) with GitHub issue #38 open in its side pane: Back to sessions, the issue title Cart total ignores discounts when tax is applied, the GITHUB and ISSUE #38 chips, Open, acme-web and the assignee alex-lee, the bug label and the description, then Comments · 3 with Refresh comments: jo-park, sam-ortiz and alex-lee, each with an avatar, an age and the comment text.">
  </a>
  <figcaption style="text-align:center; color:#888">An issue's comments, under its summary in the side pane.</figcaption>
</figure>

An issue you open in a side pane, or on the task page, shows its discussion under the summary as **Comments**. Kepler loads the newest 100 comments. **Show earlier comments** reveals older ones, and **Refresh comments** reads them again.

Comments work for GitHub, GitHub Enterprise, GitLab, GitLab Self-Hosted, Jira, and Jira Server issues. Kepler shows comments to you but does not pass them to the agent as task context.

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
| **Top** | The branch and repository, the worktree's own pull request with its CI status, and the upstream control |
| **Bottom** | Chips for uncommitted files, commits, and the merge target, plus **Open in** and **Run** |

The button's controls do the following:

- **Branch name**: opens or closes the worktree's changes in the side pane. Its **⋮** opens the [worktree menu](#the-worktree-menu).
- **Upstream control**: runs the action its counts call for. It offers **Pull** when the branch is behind, **Push** when it's ahead, and **Publish** when the branch is not on a remote yet. When the branch has diverged, or after you apply a rebase, it offers **Force push** after a confirmation. **Fetch** and the upstream row are in its chevron menu.
- **Uncommitted** and **commits** chips: open the worktree's changes in the side pane, on that scope. Click the chip that's showing again to close the side pane, or the other chip to switch scope.
- **Merge target** chip: shows how the branch compares with its merge target. While the target is ahead, its menu offers **See what's new on {target}**. See [What's new on the merge target](/kepler/review-changes#whats-new-on-the-merge-target). The menu also offers **Rebase onto {target}** and **Merge {target} into this branch**. See [Review Changes](/kepler/review-changes#updating-from-the-base).
- **Open in**: opens the checkout in your default editor. Other editors are in its chevron menu.
- **Run**: runs one of the repository's commands.

The button also tells you what needs doing, such as unpushed commits, or a paused rebase or merge you can continue or abort from the button. Hover any chip to see what a click does, or right-click the chip for the worktree's menu.

#### The worktree menu

The worktree menu is the same wherever a worktree appears, on the worktree button and on the task page. It holds:

- **Open changes** (or **Close changes** while they're showing), **Open in**, and the worktree's pull request
- **Continue {operation}** and **Abort {operation}** during a stopped rebase or merge
- A **Branch** submenu: **Rename branch**, **Rebase onto {target}** and **Merge {target} into this branch**, **Push**, **Pull** and **Fetch**, **Set upstream** or **Change upstream**, and **Change merge target…**
- **New session here**, **New terminal here**, and **Run command here**
- **Copy branch name**, **Copy worktree path**, and **Copy remote URL**
- **Detach worktree…** and **Delete worktree…**, or **Recreate worktree** for a checkout that's gone

**Set or change the upstream.** **Set upstream** or **Change upstream** opens a searchable list of remote branches. Any remote branch can be the upstream, under any name, and **Push** then pushes there. See [Set or change the upstream](/kepler/review-changes#set-or-change-the-upstream).

**More than one worktree.** A task's worktrees collapse into one worktree button. Step through them with the switcher on the branch name, or with the up and down arrow keys on the button. Until you pick one, the button shows the worktree with the latest changes. To see them all at once, use the toggle on the button's leading edge (**Show all {count} worktrees**). Worktrees whose branches have merged share a single row, from which you can delete them through the same cleanup list that archiving uses.

From the keyboard, a worktree button is 2 tab stops, one for its changes and one for its actions. Use the left and right arrow keys to move inside each.

When a task has more than one checkout, the terminal strip's **+** opens a chooser that lists the checkouts by branch.

***

## Go to a task or file

To jump to a task, a pull request or issue, or a file, or to run a command, open the Go to palette from anywhere. It has 4 tabs: **Tasks**, **Todo**, **Files** and **Commands**. To open it:

- **Cmd/Ctrl+Shift+P** or **F1** (**View › Command Palette…**) opens **Go to task**, on **Tasks**.
- **Cmd/Ctrl+P** (**File › Go to File…**) opens **Go to file**, on **Files**.

To switch tabs, click a tab or press **Shift+Tab**. In an empty field, you can also type **#** for **Todo**, **@** for **Files**, or **>** for **Commands**, and press **Backspace** to return to **Tasks**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/go-to-task-palette-nov-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/go-to-task-palette-nov-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Go to task palette: a search field reading Go to task, or type # for todos, @ for files or > for commands, the Tasks, Todo, Files and Commands tabs with Tasks selected, and your tasks listed under Needs attention, Unread, Recent and Not started, with Fix the cart total checked as the current task, above key hints such as Open and Task files.">
  </a>
  <figcaption style="text-align:center; color:#888">Go to task, listing your tasks to switch to.</figcaption>
</figure>

**Tasks** lists your tasks in the same groups as the Dashboard, with the one you're in marked **Current**. Type to narrow the list, or paste a Kepler task link. Press **Enter** to switch to the highlighted task, or **→** to search that task's files. Below the matches, 3 rows turn what you typed into something else:

- **Search files for “{query}”** searches every task's files for it.
- **New task: “{query}”** puts it in the **New task** composer.
- **Ask Kepler: “{query}”** starts an [Ask Kepler](/kepler/ask-kepler) chat with it.

**Files** searches the files of the task you're in, whose name shows as a pill at the end of the field. Before you type, it lists the files **Changed in this task**, then **Recent in this task**. Type a name, or a full path to open it. To search every task's files, click the pill's **×**.

**Todo** finds the pull requests and issues in your Todo by title, number, or pasted link. Its **Mine** and **All** switch sets which ones it searches. Press **Enter** to open the item's panel on the Dashboard.

**Commands** lists the commands you can run from where you are, each with its keyboard shortcut, and a row for each Settings page and for actions such as switching windows. Press **Enter** to run the highlighted command.

<figure style="text-align:center">
  <a href="/wp-content/uploads/palette-commands-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/palette-commands-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="The palette on its Commands tab: a search field reading Search commands, or type @ for files or # for todos, the Tasks, Todo, Files and Commands tabs with Commands selected, and the General commands, such as Open settings, Toggle Ask Kepler chat, New Ask Kepler chat and New task (highlighted), some with their keyboard shortcut on the right, then Send feedback, Open documentation and the Appearance commands, above key hints such as Run and Next tab.">
  </a>
  <figcaption style="text-align:center; color:#888">The Commands tab, listing commands with their shortcuts.</figcaption>
</figure>

Each row has a menu of its actions, also on **Alt+Enter**. For how a file opens on the task page, see [The Task View](/kepler/task-view#opening-a-file).

***

## Back and forward

**Back** leaves the place or mode you're in. It does not undo a search you typed, a filter you set, or a change of layout. If you narrow the list and then press **Back**, you leave the list instead of stepping back through every keystroke.

Use these shortcuts to go back and forward:

| Command | Mac | Windows / Linux |
|---|---|---|
| **Back** | ⌘ [ | Alt + ← |
| **Forward** | ⌘ ] | Alt + → |

The **Back** and **Forward** buttons in the top bar do the same, and so do a mouse's side buttons. On macOS, a sideways swipe on a trackpad or Magic Mouse also goes back and forward.

Each set of open panels gets its own history entry, so **Back** closes the set you just opened rather than the whole visit. Each Settings page you open gets its own entry too, so **Back** steps through the Settings pages you visited. To leave Settings in one step, use the back arrow in the Settings header, which returns you to what you were doing before you opened it.

***

## Empty states

When a view has nothing to show, or Kepler cannot load it, you see one of these messages:

| What you see | What it means |
|---|---|
| **Your agents' work lives here** | You have no tasks. **Tasks** shows the **New task** composer, plus an import card, such as **Import from Conductor**, if Kepler finds another agent app's work. See [Create a task](/kepler/create-task#from-another-agent-app) |
| **No tasks yet** | The tasks list is empty |
| **No assigned PRs or issues** | Providers are connected, but nothing related to you is open. Open **View** to see what the view's scope covers |
| **Nothing matches your search** | Your search excludes everything. Use **Clear search** beneath it |
| **Nothing matches these filters** | Your filters exclude everything. Use **Clear filters** beneath it |
| **Nothing here** | One column of the **Board** layout is empty |
| **Hand your issues and PRs to agents** | You have no provider connected. Connect one from the list |
| **Unable to load your work** | Every connected provider failed to load. The notice below names each fix, such as **Reconnect** or **Retry** |
| **Unable to load your issues and pull requests.** | Loading the whole list failed. Press **Retry** |
| **Sign in to see your assigned work** | Connect a GitKraken account to load your work |
| **Unable to find this task** | The task was deleted, or its link is from another machine |

<figure style="text-align:center">
  <a href="/wp-content/uploads/tasks-empty-state-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/tasks-empty-state-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Tasks view's empty state: the heading Your agents' work lives here and a line on what a task is, then Add issue, Add PR and Add context above the composer (Describe a task or ask a question…, the agent pill and Start), Add repo or folder below it, handwritten hints pointing at each, and an Open an external session card under an or divider.">
  </a>
  <figcaption style="text-align:center; color:#888">The Tasks view with no tasks yet.</figcaption>
</figure>

### Kep

Kep, Kepler's planet mascot, appears on empty, loading and error screens. On a crash screen, **Show details** reveals **Error details**, with **Copy details** for a bug report.

<figure style="text-align:center">
  <a href="/wp-content/uploads/kep-empty-chat-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/kep-empty-chat-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A new session's empty chat in a task panel: Kep, Kepler's planet mascot, above What should the agent work on? and Describe the task, add a file with @, or type / for commands. Below them the draft composer reads Start with the task prompt, or describe something else…, with Task context, the agent pill and Start, and the Task folder picker under it.">
  </a>
  <figcaption style="text-align:center; color:#888">Kep over a new session's empty chat.</figcaption>
</figure>

---
