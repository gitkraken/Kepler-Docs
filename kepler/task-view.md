---
title: The Task View
description: Open a task to see its resources, agent sessions, changes, and files side by side. Use the header, the context panel, columns or tabs, the file viewer, and the terminal drawer, and start sessions from a draft tab.
product: Kepler
feature: Tasks
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, azure-devops]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode]
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [tasks, task-page, sessions, draft-sessions, terminals, worktrees, resources, tabs, tab-groups, split-panes, drawer, file-viewer, keyboard-shortcuts]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "kepler-core-concepts"
    nav_label: "The Task View"
    nav_order: 50
    nav_parent: "kepler-core-concepts"
    page_type: "content"
    card_icon: "layout-columns"
    card_color: "purple"
    card_description: "A task's resources, sessions, changes and files side by side"
---
<kbd>Last updated: November 2026</kbd>

Each task has its own screen, the **task page**. The context panel lists everything attached to the task. Beside it, the content area shows the sessions, working copies, files, and details you open.

To open the task page, double-click a task's row in [the Kepler interface](/kepler/kepler-interface), or click **Open task page** in the task's side panel. For what a task is and what you can attach to one, see [Tasks and Resources](/kepler/tasks-and-resources).

<figure style="text-align:center">
  <a href="/wp-content/uploads/full-task-view-oct-2026-v2.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/full-task-view-oct-2026-v2.png" class="help-center-img img-bordered" alt="The task page, its header holding the task name, the ⋮ menu, the In Development progress control, and Terminal at the right edge. The context panel lists Sessions, Changes, Pull requests, and Notes led by Prompt, and a session on the right is waiting on a command approval.">
  </a>
  <figcaption style="text-align:center; color:#888">The task page, with the context panel beside an open session.</figcaption>
</figure>

***

## The header

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-header-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-header-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The left side of the task header: the context panel toggle, the back chevron, the Fix the cart total task chip with its switcher chevron, the ⋮ Task actions menu, and the In Development progress control.">
  </a>
  <figcaption style="text-align:center; color:#888">The left side of the task header. Terminal sits at the far right.</figcaption>
</figure>

The header holds these controls, from left to right:

- **Hide context panel** or **Show context panel**, which hides and shows the context panel. See [The context panel](#the-context-panel).
- **Back to dashboard**, a back chevron, which returns you to the Dashboard as you left it. With the views on the left side, it sits at the top of the views column instead.
- **The task switcher**, the task's name as a chip, which jumps to another task without going back first. Type to search it. Right-click the name for the same actions as the **⋮** menu, or double-click it to rename the task.
- **⋮ Task actions**, a menu of actions on the whole task. See [Task actions](#task-actions).
- **The Progress control**, which shows the task's stage, such as **In Development** or **Done**. Click it to set the stage yourself, to put the task on hold, or to set it back to **Automatic**. See [Arranging your work](/kepler/arranging-your-work).
- **Terminal**, at the right edge, which shows and hides the [terminal drawer](#the-terminal-drawer) and counts the terminals running in it.

When a task looks finished, the header shows a **Ready to archive?** prompt with **Archive** beside it, until you archive the task or dismiss the prompt.

### Task actions

The **⋮ Task actions** menu holds these items:

- The task's **Progress** submenu, with **Reopen** leading on a finished task.
- **Mark as read** while any of the task's sessions is unread, which marks them all read. Otherwise the menu offers **Mark as unread**.
- **Star** or **Unstar**.
- **Rename task** and **Add to group**.
- **Manage resources**, which opens the task's **Resources** screen. See [What a task holds](/kepler/tasks-and-resources#what-a-task-holds).
- **Refresh**, which reads the task's worktrees and its pull requests and issues again.
- **Copy task link**, which copies a Kepler link that opens this task, and **Copy task prompt**.
- **Shut down all agents**, while any are running. When an agent is still working, Kepler asks you to confirm first.
- **Archive task** and **Delete task**. On an already-archived task, **Restore task** replaces **Archive task**.

### Rename a task

To rename a task, do one of the following:

- Pick **Rename task** in the **⋮ Task actions** menu.
- Press **F2** anywhere on the page outside a text field.
- Double-click the task switcher.

The name turns into an editable field. **Auto-name** fills the field with a name suggested from the task's prompt and resources, which you can accept or edit. It never renames the task on its own. To save, press **Enter** or click the check mark. To cancel, press **Escape** or click **×**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/rename-inline-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/rename-inline-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The task name turned into an editable field in the header with Fix the cart total selected, followed by the Auto-name button, × to cancel, and a check mark to save.">
  </a>
  <figcaption style="text-align:center; color:#888">Renaming a task in place.</figcaption>
</figure>

### On a phone

At phone width, for example in a phone browser connected through [Remote Access](/kepler/kepler-remote-access), the task page replaces its header with a single bar:

- **Back**, on the left, which shows a dot when another task needs you.
- The task's name as a chip, which opens the task switcher. Swipe sideways on the name to go back to the previous task.
- A segment for each of **Sessions**, **Changes**, **Terminal**, and **Resources**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/phone-task-view-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/phone-task-view-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The task page in a phone-width browser. One bar holds Back (with a dot, because another task needs you), the Fix the cart total chip, and the Sessions (1), Changes (2), Terminal and Resources (4) segments. Below it the details row reads In Review with Refresh and a fold chevron, then the checkout box for kepler/fix-cart-total (1/1, its #51 pull request with a red changes-requested dot, 2 uncommitted, origin/main) and the #51 Open and #38 Open chips, above the agent's session and its composer.">
  </a>
  <figcaption style="text-align:center; color:#888">The task page on a phone, with its single bar and details row.</figcaption>
</figure>

Tap a segment to go to what needs you in that group, or else to the last session you had open. Each segment has a picker that lists that group's rows, where you can archive or close a row, or add one with **New session**, **New terminal**, or **Add resource**. On a phone, a terminal fills the whole column instead of a drawer.

Below the bar, a details row holds the Progress control and **Refresh**. Unfold it to see the checkout and its pull request and issue chips.

Pull down on the bar, or long-press a segment, to open **Everything in this task**. This sheet takes the place of the context panel: it lists every session, checkout, terminal, and resource, each with its own actions menu. The sheet also offers **New session**, **Add resource**, **New terminal**, and the archived sessions. A long press opens it on that segment's group only.

<figure style="text-align:center">
  <a href="/wp-content/uploads/phone-context-sheet-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/phone-context-sheet-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Everything in this task sheet pulled up over the task page in a phone-width browser. Sessions (1) lists the agent's session, ticked as the one on screen, then New session; Changes (2) lists kepler/fix-cart-total and kepler/cart-rounding in acme-web; Terminals (0) offers New terminal; Resources (4) heads each kind with its count: Pull requests (1) with Apply discounts before tax in the cart total, Issues (1) with Cart total ignores discounts when tax is a…, and Notes (2) with note.md and Coding conventions. Each row has an actions menu, and the sheet ends with Add resource.">
  </a>
  <figcaption style="text-align:center; color:#888">Everything in this task, which takes the place of the context panel on a phone.</figcaption>
</figure>

On a phone, the task switcher is a sheet that lists every task. Its header holds the current task's actions menu.

***

## The context panel

The context panel, on the left of the task page, lists everything attached to the task, grouped by kind:

**Sessions · Changes · Merged · Terminals · Pull requests · Issues · Notes · Links · Files · Folders · Related tasks**

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-rail-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-rail-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The context panel: Sessions with the agent's session, Changes with the kepler/fix-cart-total worktree (2 uncommitted files), a folded Merged group (1) with Delete all…, Pull requests with Apply discounts before tax in… (#51, Open, Changes requested) and Issues with Cart total ignores discounts… (#38, Open, acme-web), each with refresh and add buttons, Notes with the Prompt and Coding conventions, and Related tasks with Add tests for discount codes (Sub-task) and Show the discount on the receipt (Follow-up), above Manage resources.">
  </a>
  <figcaption style="text-align:center; color:#888">The context panel, grouped by resource kind.</figcaption>
</figure>

The task's worktrees are listed under **Changes**. Each row shows the checkout's current state, and opening it opens the checkout's diff review.

**A planned worktree waits for the first session.** When an agent creates a task on a new branch, Kepler makes its worktree when the task's first session starts. Until then, **Changes** shows a row reading **Created when a session starts**. To drop the plan, right-click the row and pick **Remove planned worktree**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-planned-worktree-row-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-planned-worktree-row-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="The task page's context panel. Under Sessions is a New session draft; under Changes, a planned row for acme-web on kepler/receipt-discount reads Created when a session starts, with a remove button. Its tip reads acme-web, Branch: kepler/receipt-discount, A new worktree for this repository, created when the first session starts. Below are Notes with the Prompt, and Related tasks with Fix the cart total (Follows up on).">
  </a>
  <figcaption style="text-align:center; color:#888">A planned worktree, made when the task's first session starts.</figcaption>
</figure>

**Merged** holds the worktrees whose branch has been merged, so they do not crowd the work still in progress. Each row says where it was merged. To delete all the merged worktrees at once, click **Delete all…** on the group header and confirm.

**Related tasks** lists the tasks linked to this one, each with its stage and its relation, such as **Sub-task** or **Follow-up**. Hover a row to see the reason for the link. Click the row to go to that task.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-rail-merged-related-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-rail-merged-related-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The context panel with the Merged group unfolded: kepler/cart-rounding, merged into origin/main, under Merged (1) with Delete all…, above the Pull requests row Apply discounts before tax in… (#51) and the Issues row Cart total ignores discounts… (#38). At the bottom, Related tasks lists Add tests for discount codes as a Sub-task and Show the discount on the receipt as a Follow-up; pointing at the follow-up shows its tip, Follow-up · Exploration, with the reason: once the total is right, the receipt should show the discount. Beside the panel, the session's chat shows the agent's replies and the Type a message… box.">
  </a>
  <figcaption style="text-align:center; color:#888">The Merged and Related tasks groups, with a related task's tip.</figcaption>
</figure>

**Sessions** always appears, even on a task with no sessions, so you can always start the first one. Every other group appears only when it has something in it.

**The task's prompt has its own row.** **Prompt**, with its own icon, is the first row in the **Notes** group. Open it to read or edit the prompt the task started with. Your edit changes the task's prompt everywhere it appears. You cannot delete the **Prompt** row.

**Files** holds both files linked from disk and copies uploaded to the task. An uploaded copy shows **Task folder** under its name, where a linked file shows its path.

The context panel also has these controls and rows:

- **Manage resources**, at the bottom of the context panel, opens the task's **Resources** screen. See [What a task holds](/kepler/tasks-and-resources#what-a-task-holds).
- The **+** on a group header opens that kind's tab of the **Resources** screen, for example **Add issues** or **Add notes**. On **Changes**, the **+** is **Add worktree**. On **Sessions**, it's **New session**, which opens a draft session. See [Starting a session](#starting-a-session).
- A session you have not started yet shows as a **Draft** row in **Sessions**. Right-click it for **Discard draft**.
- Sessions that are not live, because they're archived or have ended, collect under a **{count} archived** fold below the live ones. Click an archived session to restore and open it in a single step, or pick **Restore** in its menu.

### Hide or show the context panel

To give the content area the full width, hide the context panel:

- Click **Hide context panel** in the header. **Show context panel** brings the panel back.
- Press **Cmd/Ctrl+B**. On Windows and Linux, a focused shell keeps **Ctrl+B** for itself.

While the context panel is hidden, the control shows the task's session status, so you can still see when a session needs you. Hover the control to peek at the context panel over the content, and press **Escape** to close it. To keep the context panel open, click the control while peeking. To resize the context panel, drag its edge.

When the window is too narrow for the context panel beside the open columns, Kepler hides the context panel, and you peek at it the same way. Widen the window to bring it back.

### What a row shows

Each row has 2 lines, cut off at the width of the context panel. Hover a row for a tip with its full name and the details the row has no room for, such as its path, repository, agent, or account.

<figure style="text-align:center">
  <a href="/wp-content/uploads/rail-hovers-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/rail-hovers-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Files group of the context panel with the hover card of checkout-style-guide.md open beside its row: the file name, Size, Modified, Type, Path (/srv/acme/brand/checkout-style-guide.md) and Added.">
  </a>
  <figcaption style="text-align:center; color:#888">A file row's hover card, with details the row has no room for.</figcaption>
</figure>

Some kinds of row show more:

- A **pull request** or **issue** row shows the same live card as the Dashboard. A pull request row leads its subtitle with what needs attention, such as **CI failed**.
- A **file** row's card adds the file's size, type, and dates. An image file shows its own thumbnail as the row's icon.
- A **Changes** row's subtitle is a series of chips that show the checkout's state: uncommitted files, commits on the branch, commits behind or ahead of the upstream and the merge target, conflicts, and an unpublished branch. A checkout with nothing to report shows **Up to date**. When the task spans more than 1 repository, each row also names its repository.
- A checkout in an unusual state shows that state instead of the chips, such as a paused rebase or merge, **Detached** for a detached HEAD, or **Not trusted. Kepler runs no git here.** for a repository you have not trusted. A detached row is titled with the commit's short hash. See [Trust a repository](/kepler/settings-repositories#trust-a-repository).
- A **Changes** row's hover tip lists the branch, the repository and path, any unusual state, the pull request the branch owns, and how the branch compares with its upstream and merge target. With tabs on, a worktree's tab shows the same tip.
- A **session** row starts with its state. When an agent has more than 1 account configured, the row also shows which **Account** the session runs under.
- A **session** row, and its tab, count the agent's replies to your review comments that you have not read. A **Changes** row counts the unread replies on comments in its changes. See [Replies and resolving](/kepler/review-changes#replies-and-resolving).

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-rail-detached-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-rail-detached-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The context panel's Changes group, above the Notes header, with a worktree on a detached HEAD: the row is titled cd919f0, the commit it sits on, with Detached in amber in its subtitle, and its hover card beside it lists cd919f0, acme-web and the worktree's path, then Detached · cd919f0 and Not published yet.">
  </a>
  <figcaption style="text-align:center; color:#888">A worktree on a detached HEAD, with its hover tip.</figcaption>
</figure>

Some rows have controls at the end of the subtitle line, always visible:

| Row | Controls |
|---|---|
| **Folder** | **Open in…** |
| **Worktree** (on disk) | **Open in…** and the run-a-command control. To open a shell, use the row's menu or **Cmd/Ctrl+J** |
| **Session** | Show or hide the [Agent Graph](/kepler/agent-graph) for that session alone, and **Archive** |

The run-a-command control shows the newest command running in that worktree, with **Stop**. When nothing is running, it shows your default command.

The row whose item is on screen is highlighted. A ring marks the column that has focus.

### The row menu

Right-click any row for its menu. Every row menu starts with **Open**. When there's somewhere for the item to go, **Open to the side** (tabs off) or **Open beside** (tabs on) follows. See [Columns or tabs](#columns-or-tabs). A worktree row adds **Open changes**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/worktree-row-menu-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/worktree-row-menu-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="A worktree row's right-click menu in the context panel, with its Branch submenu open on Rename branch, Set upstream, Change merge target… (main), Rebase onto main and Merge main into this branch. The menu also lists Open, Open changes, Open in, New session here, New terminal here, Run command here, Copy branch name, Copy worktree path, Copy remote URL, Refresh, and Detach worktree… and Delete worktree…, unavailable while a session is using the worktree.">
  </a>
  <figcaption style="text-align:center; color:#888">A worktree row's context menu, with its Branch submenu open.</figcaption>
</figure>

Each kind of row adds its own items to the menu:

| Row | Menu also holds |
|---|---|
| A worktree that's on disk | **Open changes**, **Open in**, the **Branch** submenu, **New session here**, **New terminal here**, **Run command here**, the copy actions, and **Refresh** |
| A folder | **New session here**, **New terminal here**, **Open in**, and **Copy path** |
| A file | **Open in default app**, a way to show it in your file manager, **Save as…**, and **Copy path** |
| A note | **Rename note**, **Copy note**, **Copy link to note**, and **Save as…**, which saves the note as a Markdown file |
| A session | **New session from this one**, **Rename session**, **Copy session link**, **Show Agent Graph**, the ways to continue it, **Restart agent**, and **Shut down agent** |
| A session started outside Kepler | **Open preview**, **Continue in this task**, **Create task**, and the copy actions |
| A pull request or issue | **Open**, which opens it in Kepler, **Open on {provider}**, the copy actions, **Refresh**, and **Go to worktree** when its branch is checked out |
| A plain link | **Open in browser** and the copy actions |
| A terminal that's closing | **Force close terminal** |

The worktree's **Branch** submenu holds the actions that change the branch itself: **Rename branch**, the upstream (**Set upstream**, **Change upstream**, **Unset upstream**, or **Publish as {remote}/{branch}…**), **Change merge target…**, **Rebase onto {target}**, **Merge {target} into this branch**, and the sync control. A stopped rebase or merge adds rows to continue or abort it.

**Run command here** lists the repository's commands, and so does the **Run a command** control on the row and on the worktree's own strip. Pick a command to run it in that worktree. Its terminal appears in the drawer without taking your focus. Picking a running command stops it.

- **Create command…**, at the end of the menu, adds a command without leaving the task.
- **Manage commands…** opens the repository's page in **Settings → Repositories**, and brings you back to the task when you leave it.

**Open in** lists your editors, with your default editor at the top. On a worktree, the list ends with **Open on {provider}**, which opens the branch on its Git host. To set the editor Kepler uses everywhere, use **Open files and folders in** under **Settings → General**.

**Picking an editor or a command does not make it your default.** To make one your default, use the set/unset toggle at the end of its row.

**Rename branch** opens a dialog for the new name. Tick **Also rename remote branch** to rename it on its remote too. **Change merge target…** opens a picker of remote branches; see [Review Changes](/kepler/review-changes).

**Rename session** lets you name a Chat session yourself. Automatic titles never overwrite a name you chose.

**Copy session link** copies a Kepler link that opens the session. When the window is connected to a remote machine, the link names that machine, so it opens there. With the row focused, **Cmd/Ctrl+C** copies the same link. See [Agent Sessions](/kepler/agent-sessions#pointing-an-agent-at-another-session).

**Continue as** moves the conversation to another signed-in account of the same agent. The agent restarts under that account and keeps the conversation. **Continue in Terminal** and **Continue in Chat** move the conversation between the 2 ways a session runs. When the session is still running, Kepler asks first, and warns when queued messages would be discarded. **Stop and switch** stops the session and moves it. See [Moving a session to another account](/kepler/kepler-agent-accounts#moving-a-session-to-another-account) and [How a session runs](/kepler/agent-sessions#how-a-session-runs).

<figure style="text-align:center">
  <a href="/wp-content/uploads/switch-mode-confirm-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/switch-mode-confirm-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Stop this session and continue in Terminal? dialog, warning that the session looks like it's still running and that switching stops it and resumes the conversation in Terminal, with a close button, Cancel and Stop and switch.">
  </a>
  <figcaption style="text-align:center; color:#888">Switching a running session to Terminal asks first.</figcaption>
</figure>

**Use another copy…** appears when Kepler has more than 1 saved copy of the conversation. It lists each copy, with **In use** on the current one. Pick the one to continue when you resume. See [Agent Sessions](/kepler/agent-sessions).

**Option/Alt-click** a resource row to open it in your browser instead of in Kepler.

The last item in a row menu removes the row from the task. It depends on the kind of row:

- **Detach worktree…**, **Detach folder…**, **Detach file…**, **Detach pull request…**, or **Detach issue…** for something that stays on disk or at its provider
- **Delete file…**, **Delete note…**, or **Delete link…** for something Kepler holds itself
- **Archive session** for a session
- **Close terminal** for a terminal

A worktree menu also ends with **Delete worktree…**, except on the repository's main worktree. **Detach worktree…**, **Delete worktree…**, and **Detach folder…** are unavailable while a session of this task still runs there. Archive that session first.

***

## Columns or tabs

The content area shows what you open in either columns or tabs. To choose, turn **Show tabs on the task page** on or off in **Settings → Tasks → Task page**:

| Setting | What the content area does |
|---|---|
| **Off** (the default) | Fixed **columns**, one per kind of thing, each showing one thing at a time |
| **On** | Free-form **tabs** you can pin, drag between groups, and arrange side by side |

<figure style="text-align:center">
  <a href="/wp-content/uploads/show-tabs-on-task-page-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/show-tabs-on-task-page-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Task page section of Settings › Tasks, with Show tabs on the task page and Preview tabs.">
  </a>
  <figcaption style="text-align:center; color:#888">The Show tabs on the task page setting.</figcaption>
</figure>

In both layouts, terminals open in the [drawer](#the-terminal-drawer) below the content area, never in a column or a tab. Closing a column or a tab only changes the view. It does not detach anything or stop a session, and the context panel still lists everything.

### The columns

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-columns-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-columns-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The task page for Fix the cart total with tabs off: the context panel on the left with Sessions, Changes and Notes, then three columns side by side: the session's conversation (the prompt, Thinking, a completed Plan, a Read cart.js tool call and the agent's replies, with the composer at the foot), the kepler/fix-cart-total worktree on Changes, with its Working changes row, the Commit… button and cart.js modified and cart.test.js added, and the task's Prompt note.">
  </a>
  <figcaption style="text-align:center; color:#888">The three content columns: Sessions, Changes, and Resources.</figcaption>
</figure>


With tabs off, the kind of row you open decides its column:

| Column | What opens here |
|---|---|
| **Sessions** | Agent conversations, whether they run in Chat or in a terminal, and draft sessions you have not started yet |
| **Changes** | A worktree: a strip of actions over its changed files. See [Review Changes](/kepler/review-changes) |
| **Resources** | Folders, files, pull requests, issues, links, notes |

To resize columns, drag the divider between them. Kepler keeps the sizes you set.

**Clicking a row toggles it.** Click a row to open it in its column. Click the row that's already on screen to close it again. A column with nothing open disappears, and the other columns take its space.

When the window is too narrow for the open columns side by side, the page shows one column at a time: the one with focus. Clicking a row in the context panel shows its column. Widen the window to see every column again.

When you open the task page, it shows a conversation and the checkout that conversation works in.

To close a column, click **Close panel** (**X**) on its strip.

<figure style="text-align:center">
  <a href="/wp-content/uploads/close-column-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/close-column-sep-2026.png" class="help-center-img img-bordered" alt="The Close panel (X) control on a column's strip, with its tooltip reading Close panel">
  </a>
  <figcaption style="text-align:center; color:#888">The Close panel control, on a column's strip.</figcaption>
</figure>

**Split a column to see 2 items of the same kind.** Cmd-click a row in the context panel (Ctrl-click on Windows and Linux), or pick **Open to the side** in its menu. The item opens beside what that column already shows. While a column is split, a plain click replaces only the focused pane and leaves the others alone.

**Shift-click to open a range of rows.** Use a range to watch several agents at once. Click one session, then shift-click another, and every session from the first to the second opens side by side in the Sessions column.

The close control on a session's strip depends on the session:

- On one of Kepler's own sessions, it's **Archive session**, which stops the agent, saves the conversation, and moves the session under the archived fold in **Sessions**.
- On an external session or a preview, it's **Close tab**, which only hides it.

### Tabs and groups

With tabs on, anything you open from the context panel, including sessions, worktrees, files, and every other resource, opens as a tab. Tabs sit in **groups** that you arrange freely, like editor tabs in VS Code.

<figure style="text-align:center">
  <a href="/wp-content/uploads/tabs-preview-oct-2026-v5@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/tabs-preview-oct-2026-v5@2x.png" class="help-center-img img-bordered" alt="Two tab groups side by side on the task page for Fix the cart total, with the left group's tabs ringed: they start with the pinned session tab, shrunk to its icon, beside the Prompt note in an italic preview tab, the note open below it, with a line saying when it was created and the Copy, Save as…, What changed and Edit buttons above its text; the right group holds the kepler/fix-cart-total worktree tab on Changes 2, beside Files and Comments, with the Working changes row above cart.js and cart.test.js. Each tab is a card rising to the top of its strip.">
  </a>
  <figcaption style="text-align:center; color:#888">An italic preview tab beside a session tab.</figcaption>
</figure>

- **Drag a tab** to reorder it, onto another group to move it there, or to a group's edge to split off a new group there. Drag the divider between groups to resize them.
- **A single click opens a preview.** A resource opened with one click shows in an italic preview tab that the next single click replaces. Double-click a row, or start editing in the tab, to keep it open. A session always opens as a tab you keep. Turn **Preview tabs** off in **Settings → Tasks → Task page** to have every click keep its tab.
- **Cmd-click a row** in the context panel (Ctrl-click on Windows and Linux), or pick **Open beside** in its menu, to open it in a new group beside the one you're reading.
- **Shift-click opens a range** of rows, each as its own tab.
- Clicking the row of something already open just brings its tab forward. Close a tab from the tab itself.

To open a tab's menu, right-click the tab, or press **Shift+F10** or the Menu key on a focused tab. The menu starts with the tab's own actions, such as **Keep open** on a preview, **Pin tab**, **Close others**, and **Close all**, followed by everything the item's row menu offers. A pinned tab shrinks to its icon at the front of its group and has no close control; unpin it to close it.

A draft session's tab shows **(draft)** after its name when the tab strip has room. With tabs off, right-click a draft tab for **Discard draft**. With tabs on, close a draft with **Close tab** in its menu. Closing a draft that has text in it asks you to confirm first, because your draft prompt and attachments are removed.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-draft-session-tab-menu-01-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-draft-session-tab-menu-01-v4@2x.png" class="help-center-img img-bordered" alt="The top of a task's side panel with a New session draft tab beside the task's first session, and the menu a right-click on the draft tab opens under it: Move left, with its Ctrl+Alt+[ shortcut, and Discard draft. The tabs carry no ⋮ button.">
  </a>
  <figcaption style="text-align:center; color:#888">A draft session's tab and its menu, opened with a right-click.</figcaption>
</figure>

A session tab swaps its close control for the session's status dot while the session has something unread or needs you, so you can see which conversation needs attention.

Closing a tab only hides it. You can close a tab in any of these ways:

- Click its **×** (**Close tab**).
- Middle-click the tab.
- Press **Cmd/Ctrl+W**, or **Ctrl+F4** on Windows and Linux.
- Press **Delete** on a focused tab.

A closed session keeps running and stays in the context panel. To archive a session, use **Archive** on its row. **Cmd/Ctrl+Shift+T** reopens the last tab you closed.

When every tab is closed, the content area offers **New session**, so you can start something right away.

To bring in an agent conversation you started outside Kepler, start a new session, then click **Open an external session** under its composer. The card shows only while Kepler lists [sessions started outside Kepler](/kepler/kepler-external-sessions). Each conversation you open gets its own tab. **Back to the new session** returns to the composer.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-session-external-card-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-session-external-card-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="A new session's draft on the task page: What should the agent work on?, the composer with its repository, branch and worktree chips, then &quot;or&quot;, then the Open an external session card, Pick up a Claude Code, Codex or other agent session you already started and bring it into this task.">
  </a>
  <figcaption style="text-align:center; color:#888">Open an external session, under a new session's composer.</figcaption>
</figure>

The list shows the agent conversations Kepler found outside it, under **Live now** and **Past sessions**, with the folder each ran in and when it was last active. **Show past sessions** and **Show sessions from every folder** widen the list.

### Keyboard

The task page has these keyboard shortcuts:

| Keys | What they do |
|---|---|
| **Ctrl+Tab** / **Ctrl+Shift+Tab** | Switch between the task's sessions, most recently used first |
| **F6** / **Shift+F6** | Move focus to the next or previous region of the page |
| **Cmd/Ctrl+1**, **2**, **3** | Focus the Sessions, Changes, or Resources column (tabs off) |
| **Cmd/Ctrl+Shift+[** and **Cmd/Ctrl+Shift+]** | Previous and next tab. Also **Ctrl+PageUp** and **Ctrl+PageDown** on Windows and Linux |
| **Alt+1** to **Alt+9** | Jump to a tab in the focused group (tabs on) |
| **Cmd/Ctrl+Alt+[** and **Cmd/Ctrl+Alt+]** | Move the focused tab left or right. Also **Ctrl+Shift+PageUp** and **Ctrl+Shift+PageDown** on Windows and Linux |
| **Cmd/Ctrl+W** | Close the focused tab or panel. Also **Ctrl+F4** on Windows and Linux |
| **Delete** | Close the focused tab, the way its **×** does |
| **Cmd/Ctrl+Shift+T** | Reopen the last closed tab (tabs on) |
| **Cmd/Ctrl+T** | New session, which opens a draft tab |
| **Cmd/Ctrl+B** | Show or hide the context panel |
| **Cmd/Ctrl+J** | Show or hide the terminal drawer |
| **Cmd/Ctrl+Shift+J** | Maximize the terminal drawer, opening it first if it's hidden |
| **Cmd/Ctrl+O** / **Cmd/Ctrl+P** | **Open File…** / **Go to File…**. See [Opening a file](#opening-a-file) |
| **Cmd/Ctrl+Shift+O** | **Open Folder…** |
| **Cmd/Ctrl+Shift+P** or **F1** | **Go to task**. See [Go to a task or file](#go-to-a-task-or-file) |
| **Cmd/Ctrl+F** | Find in the focused file or diff. See [Finding text in a file](#finding-text-in-a-file) |
| **F2** | Rename the task, or the note whose pane or tab has focus |
| **Cmd/Ctrl+Shift+Backspace** | Delete the task, after you confirm |
| **Cmd/Ctrl+C** | Copy what the focused row names, such as a session's link or a file's path |
| **Cmd/Ctrl+Shift+W** | Close the window |
| **Tab** to a divider, then the arrow keys | Move the divider between panes, columns, or tab groups. Hold **Shift** for bigger steps |

With tabs off, a tab's menu in a column strip also holds **Move left** and **Move right**.

***

## Starting a session

Every new session starts as a draft in its own tab, marked **(draft)** when the tab strip has room. In the draft's prompt composer, you choose where the agent works and how it runs before anything starts.

To start a session, follow these steps:

1. Click **+** on the **Sessions** group in the context panel, or press **Cmd/Ctrl+T**. A draft tab opens, and a **Draft** row appears in **Sessions**.
2. Choose where the agent works from the place chip at the bottom of the composer. The chip names the place, then its branch, then whether the session gets a new worktree.
3. Open **Agent settings** to choose the **Agent**, **Start in**, and the agent's own options, such as **Permission mode**.
4. Type your prompt.
5. Press **Start**.

The place chip has 3 segments. The first segment opens a menu of places in these groups, with a **Search places** field when the list is long:

| Group | What it lists |
|---|---|
| **Attached to this task** | The task's worktrees, by branch, and its folders, led by **All worktrees and folders**. That row runs the session in the task folder with access to every worktree and folder, and reads **Task folder** while nothing is attached |
| **Repositories** | The repositories the task has worktrees of |
| **Add a repository or folder** | A picker over all your repositories and folders. A folder you pick joins the task right away; a repository joins it when the session starts |

The second segment picks the branch the session works on. The third is a checkbox: tick it to start on a new branch in a new worktree of the session's own, or leave it clear to work in the place as it is.

If the place is a worktree that's gone from disk, **Start** recreates it, after Kepler asks you to confirm. On a task with no place to run, click **Add worktree or folder** first. On a task with a [planned worktree](#the-context-panel), a new draft starts on the planned branch. On a task with more than 1 worktree or folder, a new draft can start on **All worktrees and folders**. To narrow the session to one place, pick it from the place chip.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-session-flyout-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-session-flyout-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="A task's side panel with a New session draft tab and the place chip's menu open under its composer: Attached to this task with the kepler/fix-cart- total worktree, Repositories with acme-web, and Add a repository or folder. The chip reads acme-web, kepler/fix-cart-total and worktree.">
  </a>
  <figcaption style="text-align:center; color:#888">Choosing where a new session runs.</figcaption>
</figure>

**Task context** is a checkbox chip in the composer's footer, beside the place chip. It's on by default and gives the agent the task's prompt and notes, and later changes to them reach the agent with your next message. Turn it off when you want the session to form its own view without them. See [Starting a session without the task's context](/kepler/tasks-and-resources#starting-a-session-without-the-tasks-context).

**Which agent a draft starts with is a setting.** By default, each session starts on the agent you used last. **New sessions start with**, in **Settings → Tasks → New tasks**, sets the agent for your first session, and for every session once you untick **Start each session on the agent you used last** under it. See [Settings](/kepler/settings-tasks#default-agent).

If no agent is set up, the agent control reads **Set up an agent**, and **Start** opens a panel where you can install an agent or tell Kepler where yours is. See [Agent Integrations](/kepler/agent-integrations). If the agent is signed out, sign in to it before you start.

**Start a draft in a specific checkout.** Right-click a worktree or folder row and pick **New session here**. A draft opens with that checkout already chosen as its place, ready for your prompt.

**When a session cannot start.** If the agent fails after launch, the task page shows **{agent} was unable to start** with the agent's message. Press **Retry** to launch it again, or **Open agent settings** to fix the problem.

**Start from an existing session.** **New session from this one**, on a session's row or tab menu, picks an agent and starts a session in the same working directory that can read the source conversation. **New session from here**, on a message in a conversation, does the same but cuts the source off at that message. The new session shows a **Continues from** divider naming its source; **Open source session** in its menu takes you back.

To run an Action instead of typing a prompt, open the chevron beside the session composer's **Send** button and pick an Action. Kepler adds anything you typed to the Action's prompt as a refinement. See [Actions](/kepler/actions).

***

## Opening a file

The task's own files and folders open on the task page, in Kepler's file viewer: as a tab with tabs on, or in the **Resources** column with tabs off. To see a worktree file alongside its changes instead, pick **Open in Changes** in its tab's menu, which opens it in the Changes overlay on File view. Any other file opens in an overlay. See [Files that open in an overlay](#files-that-open-in-an-overlay).

<figure style="text-align:center">
  <a href="/wp-content/uploads/markdown-file-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/markdown-file-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="checkout-style-guide.md open in a task page tab, rendered as Markdown: the Checkout style guide heading, a Buttons table of what to say and not to say, and Totals and Errors lists. The header shows Add a description, the folder /srv/acme/brand and the file size, the Preview and Source toggle, Wrap lines and File actions.">
  </a>
  <figcaption style="text-align:center; color:#888">A Markdown file in the file viewer, in Preview.</figcaption>
</figure>

You can open a file in these ways:

| How to open one | What you get |
|---|---|
| **File › Open File…** (**Cmd/Ctrl+O**) | A file picker for the machine the window is connected to |
| **File › Open Folder…** (**Cmd/Ctrl+Shift+O**) | A folder picker. The folder opens with its file tree |
| **File › Go to File…** (**Cmd/Ctrl+P**) | The Go to palette on its **Files** tab. See [Go to a task or file](#go-to-a-task-or-file) |
| **View › Command Palette…** (**Cmd/Ctrl+Shift+P** or **F1**) | The Go to palette on its **Tasks** tab |
| A row in the context panel's **Files** group | That file |
| A file path an agent writes in the conversation | The file, at the line the agent named |
| A file path in a terminal | The file, at its line. See [File paths are links](#file-paths-are-links) |

**All file links work the same way.** A click, a Cmd/Ctrl+click, or a middle-click opens the file in Kepler. Cmd/Ctrl+Shift+click opens it in your default editor at its line.

A path that's already one of the task's files opens that file's own tab rather than a second copy, however the path was spelled.

### Go to a task or file

**Go to File…** and **Command Palette…** open the same Go to palette, on its **Files** tab or its **Tasks** tab. For its **Todo** and **Commands** tabs and how to switch tabs, see [Go to a task or file](/kepler/kepler-interface#go-to-a-task-or-file).

On the task page, **Files** starts on this task's files, shown as a pill in the search field. To search every task's files, click the pill's **×**. You can also type a full path. A path that names a folder offers **Open** and opens the folder.

### What the file viewer shows

The file viewer shows each kind of file in its own way:

- **Code and text**, with syntax highlighting, scrolled to the line you opened it at, with that line marked. **Wrap lines** turns soft wrapping on and off.
- **Markdown**, rendered, with a **Preview** / **Source** toggle. A Markdown file opened at a line, such as from a path an agent wrote, opens in **Source** so you see the line.
- **Images and SVG**, fitted to the pane, with **Fit** and **100%**.
- Anything else gets a **No preview for this file** card with the options available in this window: **Open in default app**, **Show in Finder** (macOS), **Show in Explorer** (Windows) or **Show in file manager** (Linux), and **Copy path**.

**An open file stays in sync with the file on disk.** When the file changes, the viewer updates in place and says **Updated just now**, naming the session that changed it when Kepler knows. **Show changes** shows what changed since the file was first shown; **Back to file** returns. A deleted file keeps showing the last version Kepler read, and says so.

<figure style="text-align:center">
  <a href="/wp-content/uploads/file-updated-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/file-updated-oct-2026.png" class="help-center-img img-bordered" alt="The file viewer after the open file changed on disk, with an Updated just now banner across the top and Show changes at its right end.">
  </a>
  <figcaption style="text-align:center; color:#888">An open file that just changed on disk.</figcaption>
</figure>

A very large file shows its start first, with **Load the rest**.

**Review comments work in the file viewer too.** Hover a line and click the gutter's **+** to leave a comment, the same way you do in the Changes overlay, then click **Send comments** in the tab's actions. From the keyboard, move to a line with **↑** and **↓**, hold **Shift** to select a range, and press **C** to comment. To send comments on a file outside the task's worktrees, open it from the conversation. See [Review comments](/kepler/review-changes#review-comments).

**Open in** on the viewer's header opens the file in your pinned editor, or else the one you used last. Its chevron lists the rest, including your computer's **Default app**, and any of them can be pinned with **Set as default**.

### Finding text in a file

Every code view, the file viewer and the diffs in the Changes overlay alike, has its own find bar. Press **Cmd/Ctrl+F** in the view to open it at the top right. It counts matches as *{current} of {total}*, or **No results**, and offers the following:

| Control | Keys |
|---|---|
| Next and previous match | **F3** and **Shift+F3**. Also **Cmd+G** and **Cmd+Shift+G** on macOS |
| **Match case** | **Alt+C**, or **Cmd+Option+C** on macOS |
| **Match whole word** | **Alt+W**, or **Cmd+Option+W** on macOS |
| **Use regular expression** | **Alt+R**, or **Cmd+Option+R** on macOS |

**Escape** closes the bar. In a diff, the search runs across every file in the stack but skips the unchanged lines that are folded away.

### Files that open in an overlay

A file that is not one of the task's files or folders opens in an overlay rather than a tab. So does any file opened away from the task page, such as from the Dashboard or a conversation link outside a task:

- A file or folder inside a worktree opens in the Changes overlay on File view. A changed file opens on **Working changes**. Any other file opens in the **Files** view, the worktree's whole tree. A folder opens the **Files** view with its changed files selected.
- Any other file opens in the file overlay, beside a file tree rooted at the attached folder or worktree that holds it, or else at the file's own folder.

<figure style="text-align:center">
  <a href="/wp-content/uploads/file-overlay-tree-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/file-overlay-tree-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="checkout-style-guide.md open in the file overlay, with the breadcrumb /, srv, acme, brand above it and the file tree of the brand folder beside it: the fonts and launch-2.4 folders, the logos folder opened on acme-mark-dark.svg and acme-mark.svg, then checkout-style-guide.md (selected), colors.json, README.txt and voice-and-tone.md. The viewer shows the guide rendered as Markdown, with the Preview and Source toggle and Wrap lines. The header holds Hide file tree, More file actions, Maximize and Close, and the tree pane a Filter files button.">
  </a>
  <figcaption style="text-align:center; color:#888">A file in the file overlay, with its folder's tree beside it.</figcaption>
</figure>

In the file overlay:

- **Show file tree** and **Hide file tree** toggle the tree, and the tree's edge resizes it. On a narrow window, widen the window to show the tree.
- **Filter files** narrows the tree. Right-click a tree row for the ways to open it and copy its path.
- Each folder in the breadcrumb lists its folders and files, and can open the folder in your file manager.
- **Add to task**, in **More file actions**, attaches the file to the task.
- Drag either edge of the overlay to widen it, or use **Maximize**.

***

## The terminal drawer

Terminals open in a drawer below the content area. Drag its divider to resize it. The **Terminal** control at the right edge of the header shows and hides the drawer, and counts the terminals running in it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-terminal-here-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-terminal-here-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A worktree row's right-click menu in the context panel with New terminal here highlighted, below New session here and above Run command here, the copy actions, Refresh, and Detach worktree… and Delete worktree…. The Branch submenu sits above New session here.">
  </a>
  <figcaption style="text-align:center; color:#888">New terminal here, on a worktree row's context menu.</figcaption>
</figure>

To show the drawer or open a terminal, use one of these:

| How to open one | What you get |
|---|---|
| **Cmd/Ctrl+J**, or the header's **Terminal** | Shows and hides the drawer |
| **New terminal here**, on a worktree or folder row | A shell in that checkout |
| **Run command here**, on a worktree row | The command you pick, running in that checkout, revealed without taking your focus |
| The strip's **+** | A shell. With several checkouts it becomes **New terminal in…**, listing them by branch |

Every terminal also has a row in the context panel's **Terminals** group. Click the row to open the drawer on that terminal. Click the row of the terminal already showing to hide the drawer. Drag the drawer's tabs to reorder them.

**Maximize terminal pane**, or **Cmd/Ctrl+Shift+J**, takes the whole height; **Restore terminal pane** brings it back.

On a phone, a terminal takes the whole column, with a row of the keys a phone keyboard lacks beneath it, and you select text with a long press. See [Remote Access](/kepler/kepler-remote-access).

### When a terminal reconnects

A terminal reattaches to its running shell rather than starting a new one:

- While it reconnects, the last screen stays readable. If it cannot reconnect, the shell is still running: click **Retry** to load its output again.
- What you type while it reconnects is sent once the terminal is back. If the program printed something in the meantime, Kepler drops your typing and tells you to type it again.
- Only 1 view can type in a terminal at a time. When another window or a Remote Access device is driving it, click **Take control** to type here.

### Reading a tab

Each tab shows **a single icon** that tells you both what kind of terminal it is and how it ended, so a clean finish and a crash look different:

| Kind | What it is |
|---|---|
| **Shell** | A plain terminal you opened |
| **Agent** | A session running an agent in Terminal mode. See [Agent Sessions](/kepler/agent-sessions#how-a-session-runs) |
| **Command run** | One of the repository's commands |

When the program in a shell tab reports a status, the tab shows it: **Running**, **Needs you**, **Done**, or **Failed**. Hover the tab for the program's message and progress. An agent tab keeps its own icon, because its session reports the status.

**A shell tab is named after what runs in it**, such as `pnpm dev`. Back at the prompt, the tab returns to its own label, such as **Terminal 2**. Command runs and agent tabs keep their names.

When a shell's program needs you or finishes, Kepler sends a notification that names the terminal and its task, unless that terminal is on screen in the focused window. These notifications follow the same settings as agent sessions, in **Settings → Notifications**.

A finished command run shows a **result bar** rather than leaving you to read the scrollback: **Exited with code {code}**, **Exited by signal {signal}**, or **Stopped**, with **Run again** and **Close** beside it. A still-running one offers **Stop**.

### File paths are links

File paths printed in a terminal are links, including relative paths, paths with a line suffix such as `src/app.ts:42`, and paths wrapped across lines. Cmd-click one (Ctrl-click on Windows and Linux) to open the file [on the task page](#opening-a-file) at its line, and Cmd/Ctrl+Shift+click to open it in your default editor.

Right-click a path for more: **Open file**, your default editor (opening at the line), **Open in** for the rest of your editors and your computer's **Default app**, **Save as…**, and **Copy path**. Any of those targets can be your default, with **Set as default**.

Kepler task and session links in a terminal are links too. Cmd/Ctrl-click one to open it in Kepler, or right-click it for **Open in Kepler** and **Copy link**.

On a phone, long-press a path or link instead, then pick **Open** from the small menu over the selection, which also offers **Copy**, **Paste**, and **Select all**. See [Remote Access](/kepler/kepler-remote-access).

### Closing a busy terminal

Closing a terminal with something running in it asks you to confirm first, naming the job that would stop. Click **Close terminal** to go ahead. A terminal that is already closing offers **Force close**.

Shell tabs survive a Kepler update and come back after a restart. With **Keep agents and terminals running across restarts and updates** on, in **Settings → General**, command runs do too. A plain **Quit** ends them. When you quit Kepler with busy terminals or sessions, it asks first.

***

## What each resource pane shows

Each kind of resource opens in its own pane:

| Resource | Details |
|---|---|
| **Worktree**, on disk | A strip of actions (the branch, the sync control, **Open in**, **Run a command**) over its changed files, which lead into the Changes overlay, plus a **Comments** view that lists the task's review comments with how many are open and unread. See [Review Changes](/kepler/review-changes) |
| **Worktree**, missing | Its branch, base branch, and recorded path, with a way to recreate it. See [When a worktree goes missing](/kepler/tasks-and-resources#when-a-worktree-goes-missing) |
| **Folder** | The folder's name and its **Path** |
| **File** | The file itself, in the [file viewer](#opening-a-file), with its description, where it came from, and its size on the viewer's toolbar. An uploaded copy says it's a copy in the task folder, and has **Rename** in **File actions** |
| **Pull request** / **Issue** | Status, who it involves, the item's description and its labels. An issue adds its comments |
| **Link** | Every plain link (one that is not a pull request or issue) shares one **Links** pane, scrolled to the link you picked |
| **Note** | The note itself, with **Copy**, **Save as…**, **What changed**, and **Edit**. The **Prompt** note edits the task's prompt |

**The worktree strip.** The **⋮** beside the branch, and a right-click on the branch, both open the worktree's full [row menu](#the-row-menu). With more than 1 worktree, the branch name also switches between the task's worktrees. **Detach worktree…** leaves the worktree on disk, and **Delete worktree…** removes it from disk.

**Files.** A description you edit saves as you type, and **Done** closes the field. **Rename** on an uploaded copy renames its file on disk. A linked file has no **Rename**.

**Pull requests and issues.** You can select and copy the description text. When Kepler cannot read a description or the provider, the pane says so and points you to the item on its provider.

A pull request's **People** section shows its author, its **Assignees**, and each reviewer with their review state. An issue shows its **Assignee**.

An issue from GitHub, GitHub Enterprise, GitLab, GitLab Self-Hosted, Jira, or Jira Server also shows its latest comments under **Comments · {count}**. **Show earlier comments** pages back, and **Refresh comments** reads them again. Kepler shows the comments for you to read. It does not pass them to the agent.

<figure style="text-align:center">
  <a href="/wp-content/uploads/issue-comments-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/issue-comments-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Fix the cart total panel (In Review, its worktree card with #51 marked Changes requested, and the #51 Open and #38 Open chips) with GitHub issue #38 open in its side pane: Back to sessions, the issue title Cart total ignores discounts when tax is applied, the GITHUB and ISSUE #38 chips, Open, acme-web and the assignee alex-lee, the bug label and the description, then Comments · 3 with Refresh comments: jo-park, sam-ortiz and alex-lee, each with an avatar, an age and the comment text.">
  </a>
  <figcaption style="text-align:center; color:#888">An issue's comments, in the same reader the task page uses, here in a Dashboard panel.</figcaption>
</figure>

**Links.** The **Links** pane lists every plain link on the task with its title and URL, an **Open in browser** button, and **Link actions**, scrolled to the link you clicked.

**Notes.** A note's pane has **Edit**, **Copy**, **Save as…** and **What changed**, and you can rename the note in place. To rename, edit, or restore a note, see [Notes are how you give standing instructions](/kepler/tasks-and-resources#notes-are-how-you-give-standing-instructions).

<figure style="text-align:center">
  <a href="/wp-content/uploads/note-rename-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/note-rename-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Coding conventions note open in a task page pane, its name turned into an inline field with the name selected for renaming, above the note's two standing instructions: money is in cents until it is shown, and every cart change gets a test in cart.test.js.">
  </a>
  <figcaption style="text-align:center; color:#888">Renaming a note in place.</figcaption>
</figure>

---
