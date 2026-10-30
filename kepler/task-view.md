---
title: The Task View
description: Open a Task to see its resources, agent sessions, changes, and files side by side. Learn the header, the rail, columns and free-form tabs, the file viewer, and how to start sessions from a draft tab and open terminals.
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
last_verified: 2026-10
llms_include: true
tags: [tasks, task-page, sessions, draft-sessions, terminals, worktrees, resources, tabs, tab-groups, split-panes, drawer, file-viewer, keyboard-shortcuts]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Opening a Task gives you its own screen, the **task page**, with everything attached to it on the left and the sessions, working copies, files, and details you're looking at on the right.

Get here by double-clicking a row in [the Kepler interface](/kepler/kepler-interface), or by clicking **Open task page** in the side panel. For what a Task is and what can be attached to one, see [Tasks and Resources](/kepler/tasks-and-resources).

<figure style="text-align:center">
  <a href="/wp-content/uploads/full-task-view-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/full-task-view-oct-2026.png" class="help-center-img img-bordered" alt="The task page. Its header holds the task name, the ⋮ menu, the In Development progress control, and Terminal at the right edge. The rail lists Sessions, Changes, Pull requests, and Notes led by Prompt, and a session on the right is waiting on a command approval.">
  </a>
  <figcaption style="text-align:center; color:#888">The task view: the rail on the left, a session open on the right.</figcaption>
</figure>

***

## The header

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-header-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-header-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The left side of the task header: the context panel toggle, the back chevron, the Fix the cart total task chip with its switcher chevron, the ⋮ Task actions menu, and the In Development progress control.">
  </a>
  <figcaption style="text-align:center; color:#888">The left side of the task header. Terminal sits at the far right.</figcaption>
</figure>

From left to right, the header carries:

- **Show/Hide context panel**, which puts the rail away and brings it back. See [The rail](#the-rail).
- **Back to dashboard**, a back chevron, returns you to the list exactly as you left it: same segment, grouping, filters, and selection.
- **The task switcher**, the Task's name as a chip, jumps to another Task without going back first. It searches as you type, and each row carries the same session status dots a row does. Right-click the name for the same task actions the **⋮** menu holds, or double-click it to rename the Task.
- **⋮ Task actions**. See below.
- **The Progress control**, showing where the work stands: **Exploration**, **In Development**, **In Review**, **On hold**, or **Done**. Click it to set the stage yourself or hand it back to **Automatic**. An archived Task reads **Archived** here instead. See [Arranging your work](/kepler/arranging-your-work).
- **Terminal**, at the right edge, which shows and hides the [terminal drawer](#the-terminal-drawer) and counts the terminals running in it.

When a Task looks finished, a **Ready to archive?** prompt joins the header with **Archive** beside it, until you archive the Task or dismiss it.

**⋮ Task actions** holds the following:

- The Task's **Progress** submenu, with **Reopen** leading on a finished Task.
- **Mark as read** while any of the Task's sessions is unread, which marks them all read. Otherwise the menu offers **Mark as unread**.
- **Rename task**.
- **Copy task link**, which copies a Kepler link that opens this Task.
- **Copy task prompt** and **Add resource…**.
- **Refresh**, which reads the Task's worktrees and its pull requests and issues again. While the provider is cooling down it's locked, and its tooltip says when to try again.
- **Shut down all agents**, while any are running.
- **Archive task** and **Delete task**. On an already-archived Task, **Restore task** replaces **Archive task**.

**Rename task**, **F2** anywhere on the page outside a text field, or a double-click on the task switcher turns the name into an editable field in place. The field carries **Auto-name** (*Suggest a name from the task's prompt and resources*), which fills the field with a suggestion for you to accept or edit. It never renames on its own: **Enter** or the check mark saves, **Escape** or the **×** cancels.

<figure style="text-align:center">
  <a href="/wp-content/uploads/rename-inline-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/rename-inline-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The task name turned into an editable field in the header with Fix the cart total selected, followed by the Auto-name button, × to cancel, and a check mark to save.">
  </a>
  <figcaption style="text-align:center; color:#888">Renaming a task in place.</figcaption>
</figure>

### On a phone

At phone width, such as a phone browser connected through [Remote Access](/kepler/remote-environments#remote-access-reach-kepler-from-another-device), the task page folds its header into one bar:

- **Back** on the left. It carries a dot when another task needs you.
- The Task's name as a chip, which opens the task switcher. Swipe sideways on the name to go back to the previous task.
- One segment each for **Sessions**, **Changes**, **Terminal**, and **Resources**. **Resources** drops first when the name would be cut off.

<figure style="text-align:center">
  <a href="/wp-content/uploads/phone-task-view-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/phone-task-view-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The task page in a phone-width browser. One bar holds Back (with a dot, because another task needs you), the Fix the cart total chip, and the Sessions (1), Changes (2), Terminal and Resources (4) segments. Below it the details row reads In Review with Refresh and a fold chevron, then the checkout box for kepler/fix-cart-total (1/1, its #51 pull request with a red changes-requested dot, 2 uncommitted, origin/main) and the #51 Open and #38 Open chips, above the agent's session and its composer.">
  </a>
  <figcaption style="text-align:center; color:#888">The task page on a phone, with its single bar and details row.</figcaption>
</figure>

Tapping a segment goes to what's waiting first, such as a blocked question, or else to the last session you had open. Each segment has a picker listing that group's rows, with a way to archive or close each one and a way to add another: **New session**, **New terminal**, or **Add resource**. The terminal takes the whole column rather than a drawer.

Below the bar, a details row holds the Progress control, **Refresh**, and a fold chevron. Unfolded, it shows the checkout and its pull request and issue chips. It folds away while **Terminal** or **Changes** is on screen.

Pull down on the bar, or long-press a segment, to open **Everything in this task**. This sheet lists every session, checkout, terminal, and resource under the rail's headings, each with its own actions menu. It also offers **New session**, **Add resource**, **New terminal**, the archived sessions, and the sessions started outside Kepler. A long press opens it on that segment's group only.

<figure style="text-align:center">
  <a href="/wp-content/uploads/phone-context-sheet-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/phone-context-sheet-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Everything in this task sheet pulled up over the task page in a phone-width browser. Sessions (1) lists the agent's session, ticked as the one on screen, then New session and Import an external session; Changes (2) lists kepler/fix-cart-total and kepler/cart-rounding in acme-web; Terminals (0) offers New terminal; Resources (4) lists the pull request Apply discounts before tax in the cart total, the issue Cart total ignores discounts when tax is a…, note.md and Coding conventions. Each row has an actions menu.">
  </a>
  <figcaption style="text-align:center; color:#888">Everything in this task, the phone's stand-in for the rail.</figcaption>
</figure>

The task switcher on a phone is a sheet listing every task in the Dashboard's inbox order, with the current Task's actions menu in its header.

***

## The rail

The left rail lists everything attached to the Task, grouped by kind:

**Sessions · Changes · Merged · Terminals · Folders · Files · Pull requests · Issues · Links · Notes · Related tasks**

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-rail-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-rail-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The task rail: Sessions with the agent's session, Changes with the kepler/fix-cart-total worktree (2 uncommitted files), a folded Merged group (1) with Delete all…, Pull requests with Apply discounts before tax in… (#51, Open, Changes requested) and Issues with Cart total ignores discounts… (#38, Open, acme-web), each with refresh and add buttons, Notes with the Prompt and Coding conventions, and Related tasks with Add tests for discount codes (Sub-task) and Show the discount on the receipt (Follow-up), above Add resource.">
  </a>
  <figcaption style="text-align:center; color:#888">The rail, grouped by resource kind.</figcaption>
</figure>

The worktree group is called **Changes**. Its rows carry each checkout's real state and open its diff review, so the header names what you go there for rather than the git object behind it.

**Merged** collects the worktrees whose branch has landed, so they stop crowding the work still in progress. Each row reads **Merged via PR {pr}** or **Merged into {target}** in place of its change chips. The group starts folded while the Task still has an active worktree. **Delete all…** on its header opens a dialog for deleting the merged worktrees in one go.

**Related tasks** lists the Tasks linked to this one, each with its stage, its relation, and its session dots: **Parent**, **Sub-task**, **Follows up on**, **Follow-up**, **Related**, or **Created from**. Point at a row for its relation and stage, plus the reason for the link, and click it to go to that Task.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-rail-merged-related-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-rail-merged-related-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The task rail with the Merged group unfolded: kepler/cart-rounding, merged into origin/main, under Merged (1) with Delete all…, above the Pull requests row Apply discounts before tax in… (#51) and the Issues row Cart total ignores discounts… (#38). At the bottom, Related tasks lists Add tests for discount codes as a Sub-task and Show the discount on the receipt as a Follow-up; pointing at the follow-up shows its tip, Follow-up · Exploration, with the reason: once the total is right, the receipt should show the discount.">
  </a>
  <figcaption style="text-align:center; color:#888">The Merged and Related tasks groups, with a related task's tip.</figcaption>
</figure>

**Sessions** always stays, even on a Task that has none, so you always have a way to start the first one. Every other group appears only once it has something in it.

**The Task's prompt is a row of its own.** It leads the **Notes** group as **Prompt**, with its own icon. Open it to read or edit what the Task was started with; editing it changes the Task's prompt everywhere it shows. It can't be deleted.

**Files** holds both files linked from disk and copies uploaded to the Task. An uploaded copy reads **Task folder** under its name where a linked file shows its path.

**The rail can be put away.** **Hide context panel** collapses it and hands the width to the content area; **Show context panel** brings it back. **Cmd/Ctrl+B** does the same from anywhere on the page, except in the single-column layout; on Windows and Linux a focused shell keeps **Ctrl+B** for itself. While it's hidden the control carries the task's own session status, so a session that needs you is still visible from a collapsed rail. Hover the control to peek at the rail floating over the content. It stays up while the pointer or focus is inside it, and **Escape** puts it away; click the control while peeking to keep the rail open. Drag its edge to resize it.

- **Add resource** sits at the bottom of the rail and opens the **Add resources** dialog.
- The **+** on a group header adds straight into that group: **Add issues**, **Add notes**, and so on. On **Changes** it reads **Add worktree**, because that's what actually lands there. On **Sessions** the **+** is **New session** instead, which opens a draft session. See [Starting a session](#starting-a-session).
- A session you haven't started yet shows as a **Draft** row in **Sessions**. Right-click it for **Discard draft**.
- Every session that isn't live (archived ones, and ones that ended) collects under a **{count} archived** fold beneath the live ones. It starts collapsed. Clicking an archived session brings it back and opens it in one gesture; **Restore** in its menu does the same.

### What a row shows

Both of a row's lines truncate at rail width. Every row has a hover tip carrying its full name, plus the facts the row's lines had no room for:

<figure style="text-align:center">
  <a href="/wp-content/uploads/rail-hovers-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/rail-hovers-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Files group of the task rail with the hover card of checkout-style-guide.md open beside its row: the file name, Size, Modified, Type, Path (/srv/acme/brand/checkout-style-guide.md) and Added.">
  </a>
  <figcaption style="text-align:center; color:#888">A file row's hover card, showing what its truncated lines couldn't.</figcaption>
</figure>

- **Path**
- **Repository**
- **Base**
- **Agent**
- **Account**
- **Status**
- Flags such as **Repository's main worktree** or **Gone from disk**

Some kinds of row show more:

- A **pull request** or **issue** row shows the same live card the Dashboard does, ending with **Status as of {time}**. A pull request row leads its subtitle with what needs attention, such as **CI failed**, and its card adds the checks and whether it can merge.
- A **file** row's card adds **Size**, **Modified**, and **Type**, plus when it was added. An image file shows its own thumbnail as the row's icon.
- A **terminal** row's tip adds **Started** and, once it has finished, **Ended**.

- A **Changes** row's subtitle is a run of glyph-and-number chips reading the checkout's real state: uncommitted files, commits on the branch, behind and ahead of the upstream, and how far it's behind the merge target, named after the count. Conflicts and an unpublished branch are drawn as glyphs alone, and a merge target Kepler can't compare with reads *Can't compare with the merge target*. A checkout with nothing to report reads **Up to date**; one that has been deleted says so. When the task's worktrees span more than one repository, each row also names its repository.
- A checkout in an unusual state leads its subtitle with that state instead of the chips: **Unable to read git status** when Kepler couldn't read it, a paused rebase or merge (in red when it has conflicts), or **Detached** for a detached HEAD, which also titles the row with the commit's short hash instead of a branch.
- A **Changes** row's hover tip is a list of lines, each marked with an icon: the branch in bold, then the repository and the path, then any state (such as **Gone from disk**, a paused operation, or *Detached · {commit}*), then the pull request the branch owns with its state or review decision, then the commits, the working tree, the upstream, and the merge target. A merged pull request leaves the upstream and merge-target lines out. A worktree's tab, with tabs on, shows the same tip.
- A **session** row leads with its state, and names which **Account** it runs under once a harness has more than one configured: the provider logo plus an ordinal, on the row, its tab, and its collapsed strip alike.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-rail-detached-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-rail-detached-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The task rail's Changes group, above the Notes header, with a worktree on a detached HEAD: the row is titled cd919f0, the commit it sits on, with Detached in amber in its subtitle, and its hover card beside it lists cd919f0, acme-web and the worktree's path, then Detached · cd919f0 and Not published yet.">
  </a>
  <figcaption style="text-align:center; color:#888">A worktree on a detached HEAD, with its hover tip.</figcaption>
</figure>

The end of the subtitle line carries the row's controls, always visible rather than revealed on hover:

| Row | Controls |
|---|---|
| **Folder** | **Open in…** |
| **Worktree** (on disk) | **Open in…** and the run-a-command control. The shell button stays out: the row's menu and **Cmd/Ctrl+J** both offer it, and the line has no room for a third control |
| **Session** | Show or hide the [Agent Graph](/kepler/agent-graph) for that session alone, and **Archive** |

The run-a-command control shows the newest command running in that worktree, with **Stop**, and falls back to your default command once nothing is running.

Every rail row draws a selected fill when it's the one on screen, and the column you last pressed, focused, or opened from the rail carries an inset ring. The wide layout never moves focus on its own, so something has to say where it is.

### The row menu

Right-click any row. Every row opens with **Open**, followed by **Open to the side** with tabs off or **Open beside** with tabs on (see [Columns or tabs](#columns-or-tabs)), when there's somewhere for it to go. A worktree row adds **Open changes**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/worktree-row-menu-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/worktree-row-menu-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="A worktree row's right-click menu in the task rail, with its Branch submenu open on Rename branch, Set upstream, Change merge target… (main), Rebase onto main and Merge main into this branch. The menu also lists Open, Open changes, Open in, New session here, New terminal here, Run command here, Copy branch name, Copy worktree path, Copy remote URL, Refresh, and Detach worktree… and Delete worktree…, unavailable while a session is using the worktree.">
  </a>
  <figcaption style="text-align:center; color:#888">A worktree row's context menu, with its Branch submenu open.</figcaption>
</figure>

| On | Also holds |
|---|---|
| A worktree that's on disk | **Open changes**, your default editor, **Open in**, and **Open pull request** when one is linked. A **Branch** submenu, then **New session here**, **New terminal here**, **Run command here**, **Copy branch name**, **Copy worktree path**, **Copy remote URL**, **Show in Finder** (macOS), **Show in Explorer** (Windows) or **Show in file manager** (Linux), and **Refresh** |
| A folder | **New session here**, **New terminal here**, your default editor, **Open in**, **Copy path** |
| A file | **Open in default app**, **Show in Finder** (macOS), **Show in Explorer** (Windows) or **Show in file manager** (Linux), **Save as…**, **Copy path** |
| A note | **Rename note**, which opens the note with its name ready to edit, and **Copy note** |
| A session | **Rename session**, **New session from this one**, **Open source session** on a session started from another, **Copy session link**, **Continue as**, **Continue in Terminal** or **Continue in Chat**, **Restart agent**, **Shut down agent**, **Show Agent Graph**, and **Use another copy…** when Kepler has more than one saved copy of the conversation |
| A session started outside Kepler | **Open preview**, **Continue in this task**, **Create task**, **Copy session ID**, **Copy working directory path**, and a way to reveal the working directory in your file manager |
| A pull request or issue | **Open**, which opens it in Kepler, then **Open on {provider}**, **Copy link**, **Copy title**, **Copy number**, **Copy branch name** on a pull request, **Refresh**, and **Go to worktree** on a pull request whose branch is checked out |
| A plain link | **Open in browser** and the copy actions |
| A terminal that's closing | **Force close terminal** |

The worktree's **Branch** submenu gathers what changes the branch itself: **Rename branch**, the upstream (**Set upstream**, **Change upstream**, **Unset upstream**, or **Publish as {remote}/{branch}…**), **Change merge target…**, **Rebase onto {target}**, **Merge {target} into this branch**, and the sync control. A stopped rebase or merge adds rows to continue or abort it.

**Run command here**, and the **Run a command** control on the row and the worktree's own strip, lists the repository's commands (configured on the repository's own page in **Settings → Repositories**) and runs the one you pick in that worktree, revealing its terminal in the drawer without taking your focus. Each command row leads with its state: a play glyph, a spinner while it warms up, or **Stop** while it runs, and picking a running command stops it rather than starting a second copy. A repository with none reads **No commands yet**, and the menu ends with **Create command…** so you can add one from where you noticed you wanted it, plus **Manage commands…**, which deep-links to that repository's own settings. When you leave that settings page, whether you saved or not, Kepler takes you back to the Task.

**Open in** works the same way, with your default editor hoisted above the list rather than buried in it. On a worktree the list ends with **Open on {provider}**, which opens the branch on its git host, or the repository's home page when the branch has no upstream. To set the editor Kepler uses everywhere, see **Open files and folders in** under **Settings → General**.

**Picking an editor or a command doesn't make it your default.** Each row carries its own set/unset toggle at its trailing edge, reachable from the keyboard, so choosing something once and pinning it are two separate decisions.

**Rename branch** opens a dialog with the branch's own name field and **Also rename remote branch**, which renames the branch on its remote too rather than just locally. **Change merge target…** opens a picker of remote branches; see [Review Changes](/kepler/review-changes).

**Rename session** names a Chat session yourself; automatic titling never overwrites a name you chose.

**Copy session link** copies a Kepler link that opens the session. When the window is connected to a remote machine, the link names that machine, so it opens there. With the row focused, **Cmd/Ctrl+C** copies the same link. See [Agent Sessions](/kepler/agent-sessions#pointing-an-agent-at-another-session).

**Continue as** moves the conversation to another signed-in account of the same agent, restarting the agent with the conversation as that account. **Continue in Terminal** and **Continue in Chat** move it between the two ways a session runs, keeping the conversation. When the session is still running a turn or background work, Kepler asks first, for example **Stop this session and continue in Terminal?** (or **Stop this session and continue as {login}?**), and warns when queued messages would be discarded. **Stop and switch** stops the session and moves it. See [Moving a session to another account](/kepler/agent-sessions#moving-a-session-to-another-account) and [How a session runs](/kepler/agent-sessions#how-a-session-runs).

<figure style="text-align:center">
  <a href="/wp-content/uploads/switch-mode-confirm-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/switch-mode-confirm-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Stop this session and continue in Terminal? dialog, warning that the session looks like it's still running and that switching stops it and resumes the conversation in Terminal, with a close button, Cancel and Stop and switch.">
  </a>
  <figcaption style="text-align:center; color:#888">Switching a running session to Terminal asks first.</figcaption>
</figure>

**Use another copy…** opens a dialog listing each saved copy of the conversation, when it was updated and how many messages it holds, with **In use** on the current one. Pick the one to continue when you resume. See [Agent Sessions](/kepler/agent-sessions).

**Option/Alt-click** a resource row to open it in your browser instead of in Kepler.

The last entry is how the row leaves the Task, and it differs by kind: **Detach worktree…**, **Detach folder…**, **Detach file…**, **Detach pull request…** or **Detach issue…** for something that stays on disk or at its provider, **Delete file…**, **Delete note…** or **Delete link…** for something Kepler holds itself, **Archive session** for a session, **Close terminal** for a terminal. A worktree also ends with **Delete worktree…**, except the repository's main worktree. **Detach worktree…**, **Delete worktree…** and **Detach folder…** are locked while a session of this Task still runs there, with the reason in their tooltip, such as *To detach, archive the session in this worktree.*

***

## Columns or tabs

The content area takes one of two shapes, set by **Show tabs on the task page** in **Settings → Tasks → Task page**:

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

Either way, terminals live in the [drawer](#the-terminal-drawer) beneath the content area, never in a column or a tab, so opening a shell never evicts the changes or the conversation you were reading. And either way, closing something is a view change: it detaches nothing, and it doesn't stop a session. The rail still has it all.

### The columns

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-columns-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-columns-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The task page for Fix the cart total with tabs off: the rail on the left with Sessions, Changes and Notes, then three columns side by side: the session's conversation (thinking, plan, a Read cart.js tool call and the agent's replies), the kepler/fix-cart-total worktree's Working changes with cart.js modified and cart.test.js added above the commit box, and the task's Prompt note in Resources.">
  </a>
  <figcaption style="text-align:center; color:#888">The three content columns: Sessions, Changes, and Resources.</figcaption>
</figure>


With tabs off, the content area is fixed slots, not free-form panes. A rail row's kind decides which slot it opens into, so a session never lands next to a note and you never have to remember where you put something.

| Column | What opens here |
|---|---|
| **Sessions** | Agent conversations, whether they run in Chat or in a terminal, and draft sessions you haven't started yet |
| **Changes** | A worktree: a strip of verbs over its changed files. See [Review Changes](/kepler/review-changes) |
| **Resources** | Folders, files, pull requests, issues, links, notes |

Every boundary is a draggable sash, and the size you drag it to persists. The three content columns share whatever the rail leaves: equally until you drag one, and in the ratio you set from then on. Kepler keeps the ratios as proportions, not pixels, so they survive a window resize and a column opening or closing.

**A rail row is a toggle.** Click it to open it in its slot; click the row that's already on screen to put it away again. A slot with nothing open renders no column at all, and the others take its space.

The page opens on a conversation and on the checkout that conversation is working in, inferred from the session or terminal it auto-opened, so **Changes** isn't an empty column you have to go fill on every visit.

Close a column with the **X** on its strip, labeled **Close panel**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/close-column-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/close-column-sep-2026.png" class="help-center-img img-bordered" alt="The Close panel (X) control on a column's strip, with its tooltip reading Close panel">
  </a>
  <figcaption style="text-align:center; color:#888">The Close panel control, on a column's strip.</figcaption>
</figure>

**Split a column to see two things of the same kind.** Cmd-click a rail row (Ctrl-click on Windows and Linux), or pick **Open to the side** in its menu, and it opens beside what that column already shows. A plain click while a column is split replaces only the focused pane and leaves the others alone.

**Shift-click opens a range.** This is how you watch several agents at once: shift-click from your last plain click through another session and the whole run opens side by side in the Sessions column, so you can read them in parallel and answer whichever needs you. The anchor is your last plain click and a shift-click doesn't move it, the way it works in Finder or VS Code. With no prior click in that group, the range starts from the row already on screen.

A session's control on its strip is named for what it does: **Archive session** on one of Kepler's own sessions stops the agent, saves the conversation, and files it under the rail's archived fold. An external session or a preview gets **Close tab**, which only hides it.

### Tabs and groups

With tabs on, anything you open from the rail (sessions, worktrees, files, and every other resource) becomes a tab, and tabs live in **groups** you arrange freely, the way editor tabs work in VS Code.

<figure style="text-align:center">
  <a href="/wp-content/uploads/tabs-preview-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/tabs-preview-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Two tab groups side by side on the task page for Fix the cart total, with the left group's tab strip ringed: it starts with the pinned session tab, shrunk to its icon, beside the Prompt note in an italic preview tab, the note's text below with its Copy note and Edit buttons; the right group holds the kepler/fix-cart-total worktree tab showing Working changes 2, cart.js and cart.test.js. Each tab is a card rising to the top of its strip.">
  </a>
  <figcaption style="text-align:center; color:#888">An italic preview tab beside a session tab.</figcaption>
</figure>

- **Drag a tab** to reorder it, onto another group to move it there, or to a group's edge to split off a new group there. Drag the sash between groups to resize them.
- **A single click opens a preview.** A resource opened with one click shows in an italic preview tab that the next single click replaces, so browsing the rail doesn't pile up tabs. Double-click a row, or start editing in the tab, to keep it open. A session always opens as a tab you keep. Turn **Preview tabs** off in **Settings → Tasks → Task page** to have every click keep its tab.
- **Cmd-click a rail row** (Ctrl-click on Windows and Linux), or pick **Open beside** in its menu, to open it in a new group beside the one you're reading.
- **Shift-click opens a range** of rows, each as its own tab.
- Clicking the row of something already open just brings its tab forward. Close a tab from the tab itself.

A tab's **Tab actions** (**⋮**) button and its right-click menu hold everything the thing's rail row offers, plus **Rename** on a file or folder tab. They lead with the tab's own verbs: **Keep open** on a preview, **Pin tab** or **Unpin tab**, **Close tab**, **Close others**, **Close to the right**, **Close all**, and **Close group** when there's more than one group. A pinned tab shrinks to its icon at the front of its group and has no close control; unpin it to close it.

A draft session's tab reads **(draft)** after its name when the tab strip has room; in a crowded strip every tab drops its extra text, and a draft shows its name alone. With tabs off, right-click a draft tab for **Discard draft**, plus **Move left** and **Move right** where the tab can move. With tabs on, its menu holds the tab's own verbs instead: **Keep open** while it's a preview, **Pin tab** or **Unpin tab**, and **Close tab**, which is a draft's only close. Closing a draft that has text in it asks **Discard new session?** first, because *Your draft prompt and attachments will be removed.*

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-draft-session-tab-menu-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-draft-session-tab-menu-01-v3@2x.png" class="help-center-img img-bordered" alt="The top of a task's side panel with a New session draft tab beside the task's first session, and the draft tab's Tab actions menu open under it: Move left, with its Ctrl+Alt+[ shortcut, and Discard draft.">
  </a>
  <figcaption style="text-align:center; color:#888">A draft session's tab and its Tab actions menu, the same one a right-click opens.</figcaption>
</figure>

A session tab swaps its close control for the session's status dot while the session has something unread or needs you, so a group's tabs say which conversation wants attention.

Closing a tab with its **×** (**Close tab**), a middle-click, **Cmd/Ctrl+W** (or **Ctrl+F4** on Windows and Linux), or **Delete** on a focused tab only hides it. **Delete** goes through the tab's own close, so a draft with text in it still asks first. **Backspace** doesn't close a tab, except on a Mac keyboard, whose delete key sends Backspace. A session keeps running and stays on the rail; to archive one, use **Archive** on its rail row. **Cmd/Ctrl+Shift+T** reopens the last tab you closed.

When every tab is closed, the content area offers **New session** and the external-session importer, so a Task with nothing open is never a dead end. With tabs on, those two controls also sit in the header, beside **Terminal**.

The importer lists the agent conversations Kepler found outside it, under **Live now** and **Past sessions**. Each row shows the agent's logo, a status dot, the folder it ran in, and when it was last active; point at one for its session card. **Show past sessions** and **Show sessions from every folder** widen the list. Sessions older than an agent's listing window are left out, and the picker names the window for each agent: *{adapter} sessions older than {days} days aren't listed*.

### Keyboard

| Keys | What they do |
|---|---|
| **Ctrl+Tab** / **Ctrl+Shift+Tab** | Switch between the Task's sessions, most recently used first |
| **F6** / **Shift+F6** | Move focus to the next or previous region of the page |
| **Cmd/Ctrl+1**, **2**, **3** | Focus the Sessions, Changes, or Resources column (tabs off) |
| **Cmd/Ctrl+Shift+[** and **Cmd/Ctrl+Shift+]** | Previous and next tab. Also **Ctrl+PageUp** and **Ctrl+PageDown** on Windows and Linux |
| **Alt+1** to **Alt+9** | Jump to a tab in the focused group (tabs on) |
| **Cmd/Ctrl+Alt+[** and **Cmd/Ctrl+Alt+]** | Move the focused tab left or right. Also **Ctrl+Shift+PageUp** and **Ctrl+Shift+PageDown** on Windows and Linux |
| **Cmd/Ctrl+W** | Close the focused tab or panel. Also **Ctrl+F4** on Windows and Linux |
| **Delete** | Close the focused tab, the way its **×** does |
| **Cmd/Ctrl+Shift+T** | Reopen the last closed tab (tabs on) |
| **Cmd/Ctrl+T** | New session, which opens a draft tab |
| **Cmd/Ctrl+B** | Show or hide the context panel (the rail) |
| **Cmd/Ctrl+J** | Show or hide the terminal drawer |
| **Cmd/Ctrl+Shift+J** | Maximize the terminal drawer, opening it first if it's hidden |
| **Cmd/Ctrl+O** / **Cmd/Ctrl+P** | **Open File…** / **Go to File…**. See [Opening a file](#opening-a-file) |
| **Cmd/Ctrl+F** | Find in the focused file or diff. See [Finding text in a file](#finding-text-in-a-file) |
| **F2** | Rename the Task, or the note whose pane or tab has focus |
| **Cmd/Ctrl+C** | Copy what the focused row names, such as a session's link or a file's path |
| **Cmd/Ctrl+Shift+W** | Close the window |
| **Tab** to a divider, then the arrow keys | Move the divider between panes, columns, or tab groups 16 pixels per press, or 64 with **Shift**. A screen reader announces each divider as *Resize {first} and {second}* with its size |

With tabs off, the column strips' **Tab actions** menus also hold **Move left** and **Move right**.

***

## Starting a session

**New session** opens a draft session in its own tab, marked **(draft)** when the tab strip has room. The draft holds the prompt composer, so you choose where the agent works and how it runs before anything starts. To open a draft, click the **+** on the rail's **Sessions** group, or press **Cmd/Ctrl+T**.

To start a session from a draft, follow these steps:

1. Click **+** on **Sessions**, or press **Cmd/Ctrl+T**. A draft tab opens, and a **Draft** row joins the rail.
2. Choose where the agent works from the place chip at the bottom of the composer. The chip names the place, then its branch, then whether the session gets a new worktree.
3. Open **Agent settings** to choose the **Agent** and how to **Start in**, along with the agent's own options, such as **Permission mode**.
4. Type your prompt.
5. Press **Start**.

The place chip has three segments. The first opens a menu of places, with a **Search places** field on a long list and the following groups:

| Group | What it lists |
|---|---|
| **Attached to this task** | The Task's worktrees, by branch, and its folders, led by **All worktrees and folders**. That row runs the session in the task folder with access to every worktree and folder, and reads **Task folder** while nothing is attached |
| **Repositories** | The repositories the Task has worktrees of |
| **Add a repository or folder** | A picker over all your repositories and folders. A folder you pick joins the Task right away; a repository joins it when the session starts |

The second segment picks the branch the session works on. The third is a checkbox: tick it to start on a new branch in a new worktree of the session's own, or leave it clear to work in the place as it is.

A worktree that's gone from disk reads *Not on disk. Start recreates it.*, and Kepler asks **Recreate the worktree and start the session?** before the session starts. A Task with no place to run at all says **Add a worktree or folder to start a session**, with **Add worktree or folder**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-session-flyout-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-session-flyout-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="A task's side panel with a New session draft tab and the place chip's menu open under its composer: Attached to this task with the kepler/fix-cart- total worktree, Repositories with acme-web, and Add a repository or folder. The chip reads acme-web, kepler/fix-cart-total and worktree.">
  </a>
  <figcaption style="text-align:center; color:#888">Choosing where a new session runs.</figcaption>
</figure>

**Task context** is a checkbox chip in the composer's footer, beside the place chip. It's on by default and *Gives the agent the task’s prompt and notes. Later changes reach it with your next message.* Its tooltip reads **Leave out the task context** while it's on and **Include the task context** while it's off. Turn it off for a session that forms its own view instead.

**Which agent a draft starts with is a setting.** **New sessions start with**, in **Settings → Tasks → New tasks**, is **Last used agent** by default (*The agent, model and mode you last picked*), or **Default agent** to always start with the default agent. See [Settings](/kepler/settings-tasks#new-sessions-start-with).

If no agents are connected, **Agent settings** reads **No agents available**, and its menu offers **Connect an AI agent**: an **Install** row per agent, **See all {count} agents in Settings**, and **Check again** for one you installed yourself. See [Agent Integrations](/kepler/agent-integrations). An agent that's signed out reads *Sign in to {agent} to start a session*. When an agent doesn't share its options, the menu says *You can still start a session. It uses {agent}'s own model and mode.*

**Start a draft in a specific checkout.** Right-click a worktree or folder row and pick **New session here**. A draft opens with that checkout already chosen as its place, ready for your prompt.

**When a session can't start.** If the agent fails after launch, the task page shows **{agent} was unable to start** with the agent's message. Press **Retry** to launch it again, or **Open agent settings** to fix the problem. **Dismiss** hides the notice in that window.

<!-- TODO(verify): Draft tab, target chip, Agent settings and start-failure labels verified against kepler v0.13.0. -->

**Start from an existing session.** **New session from this one**, on a session's row or tab menu, picks an agent and starts a session in the same working directory that can read the source conversation. **New session from here**, on a message in a conversation, does the same but cuts the source off at that message. The new session shows a **Continues from** divider naming its source; **Open source session** in its menu takes you back.

To fire a preconfigured prompt instead of typing one, open the chevron beside the session composer's **Send** button and pick an Action. Anything you typed rides along as a refinement. See [Actions](/kepler/actions).

***

## Opening a file

Any file can open on the task page, whether or not it's attached to the Task. It opens as a tab with tabs on, or in the **Resources** column with tabs off, in Kepler's file viewer. To see a worktree file alongside its changes instead, pick **Open in Changes** in its tab's menu, which opens it in the Changes overlay on File view. For what happens away from the task page, see [Outside the task page](#outside-the-task-page).

<figure style="text-align:center">
  <a href="/wp-content/uploads/markdown-file-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/markdown-file-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="checkout-style-guide.md open in a task page tab, rendered as Markdown: the Checkout style guide heading, a Buttons table of what to say and not to say, and Totals and Errors lists. The header shows Add a description, the folder /srv/acme/brand and the file size, the Preview and Source toggle, Wrap lines and File actions.">
  </a>
  <figcaption style="text-align:center; color:#888">A Markdown file in the file viewer, in Preview.</figcaption>
</figure>

| How to open one | What you get |
|---|---|
| **File › Open File…** (**Cmd/Ctrl+O**) | A file picker for the machine the window is connected to |
| **File › Go to File…** (**Cmd/Ctrl+P**) | Finds a file by name across **This task** or **All tasks**, opens a full path you type, and lists **Recent** files before you type anything. A path that names a folder, or ends in a separator, offers **Open** and opens the folder |
| A file row in the rail's **Files** group | That file |
| A file path an agent writes in the conversation | The file, at the line the agent named. A click or Cmd/Ctrl+click opens it in Kepler, and Cmd/Ctrl+Shift+click opens it in your default editor. |
| A file path in a terminal | The file, at its line. See [File paths are links](#file-paths-are-links) |

**Every file link follows one rule.** A click or a Cmd/Ctrl+click opens the file in Kepler, and a middle-click does the same. Cmd/Ctrl+Shift+click opens it in your default editor at its line, or in your default app when that's your pinned target or no editor is installed. If no editor takes it, the file opens in Kepler instead.

A path that's already one of the Task's files opens that file's own tab rather than a second copy, however the path was spelled. A file that isn't attached yet offers **Add to task**, which attaches it and turns the tab into its resource tab in place.

**What the viewer shows**

- **Code and text**, highlighted, scrolled to and marking the line you opened it at. **Wrap lines** toggles soft wrapping.
- **Markdown**, rendered, with a **Preview** / **Source** toggle. A Markdown file opened at a line, such as from a path an agent wrote, opens in **Source** so you see the line, and a toggle you make then applies to that open only.
- **Images and SVG**, fitted to the pane, with **Fit** and **100%**.
- Anything else gets a **No preview for this file** card with the ways out the window allows: **Open in default app**, **Show in Finder** (macOS), **Show in Explorer** (Windows) or **Show in file manager** (Linux), and **Copy path**.

**An open file follows the disk.** When it changes, the viewer updates in place without moving you, and says **Updated just now**, or **Updated just now by** the session that changed it when Kepler saw the edit. **Show changes** shows what changed since the file was first shown; **Back to file** returns. A deleted file keeps showing the last version Kepler read, and says so.

<figure style="text-align:center">
  <a href="/wp-content/uploads/file-updated-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/file-updated-oct-2026.png" class="help-center-img img-bordered" alt="The file viewer after the open file changed on disk, with an Updated just now banner across the top and Show changes at its right end.">
  </a>
  <figcaption style="text-align:center; color:#888">An open file that just changed on disk.</figcaption>
</figure>

A very large file shows its start first, labeled *Showing the first {shown} of {total}*, with **Load the rest**.

**Review comments work in the file viewer too.** Hover a line for the gutter's **+** (**Comment on line {line}**) to leave a comment, the same way you do in the Changes overlay. The tab's actions then lead with the file's comment count and **Send comments**. Comments on a file in one of the task's worktrees are kept with that worktree, alongside the ones you write in its changes. A file outside the task's worktrees keeps them with the conversation you opened it from; opened any other way, including a tab restored after a reload, it reads *Open this file from a conversation to send comments*. See [Review comments](/kepler/review-changes#review-comments).

**Open in** on the viewer's header is an icon button that opens the file in your pinned editor, or else the one you used last, with its chevron listing the rest. Your computer's default app is one of the targets, listed as **Default app**, and like any editor it can be pinned as your default with **Set as default**.

### Finding text in a file

Every code view, the file viewer and the diffs in the Changes overlay alike, has its own find bar. Press **Cmd/Ctrl+F** in the view to open it at the top right. It counts matches as *{current} of {total}*, or **No results**, and offers the following:

| Control | Keys |
|---|---|
| Next and previous match | **F3** and **Shift+F3**. Also **Cmd+G** and **Cmd+Shift+G** on macOS |
| **Match case** | **Alt+C**, or **Cmd+Option+C** on macOS |
| **Match whole word** | **Alt+W**, or **Cmd+Option+W** on macOS |
| **Use regular expression** | **Alt+R**, or **Cmd+Option+R** on macOS |

**Escape** closes the bar. In a diff, the search runs across every file in the stack but skips the unchanged lines that are folded away. A file that has only partly loaded says it searched the first part, with **Load the rest**.

Selecting text works across the whole file, not only the lines on screen. Drag or select all and copy, and Kepler loads the rest of the file if it needs to. Double-click selects a word.

### Outside the task page

A file opened anywhere else, such as from the Dashboard or a conversation link outside a Task, opens in an overlay rather than a tab:

- A file or folder inside a worktree opens in the Changes overlay on File view. A changed file lands on **Working changes**; anything else lands on the **All files** tree. A folder opens the **All files** tree with its changed files selected.
- Any other file opens in the file overlay, beside a file tree rooted at the attached folder or worktree that holds it, or else at the file's own folder.

<figure style="text-align:center">
  <a href="/wp-content/uploads/file-overlay-tree-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/file-overlay-tree-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="checkout-style-guide.md open in the file overlay, with the breadcrumb /, srv, acme, brand above it and the file tree of the brand folder beside it: the fonts and launch-2.4 folders, the logos folder opened on acme-mark-dark.svg and acme-mark.svg, then checkout-style-guide.md (selected), colors.json, README.txt and voice-and-tone.md. The viewer shows the guide rendered as Markdown, with the Preview and Source toggle and Wrap lines. The header holds Hide file tree, More file actions, Maximize and Close, and the tree pane a Filter files button.">
  </a>
  <figcaption style="text-align:center; color:#888">A file in the file overlay, with its folder's tree beside it.</figcaption>
</figure>

In the file overlay:

- **Show file tree** and **Hide file tree** toggle the tree, and the tree's edge resizes it. On a narrow window the toggle is locked: *Widen the window to show the file tree*.
- **Filter files** narrows the tree. Right-click a tree row for the ways to open it and copy its path.
- The breadcrumb's folders each list their folders and files, plus **Open {folder} in file manager**. As room runs out, folders fold into **More folders**.
- Opening a folder shows its tree with **Pick a file** in the viewer.
- **Add to task** is the last item in **More file actions**.
- Drag either edge of the overlay to widen it, or use **Maximize**.

***

## The terminal drawer

Terminals live in a drawer beneath the content area, spanning all of it, sized by a sash of its own. The **Terminal** control at the right edge of the header shows and hides it, and counts what's running.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-terminal-here-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-terminal-here-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A worktree row's right-click menu in the task rail with New terminal here highlighted, below New session here and above Run command here, the copy actions, Refresh, and Detach worktree… and Delete worktree…. The Branch submenu sits above New session here.">
  </a>
  <figcaption style="text-align:center; color:#888">New terminal here, on a worktree row's context menu.</figcaption>
</figure>


| How to open one | What you get |
|---|---|
| **Cmd/Ctrl+J**, or the header's **Terminal** | Shows and hides the drawer |
| **New terminal here**, on a worktree or folder row | A shell in that checkout |
| **Run command here**, on a worktree row | The command you pick, running in that checkout, revealed without taking your focus |
| The strip's **+** | A shell. With several checkouts it becomes **New terminal in…**, listing them by branch |

Every terminal also has a row in the rail's **Terminals** group. Clicking it brings the drawer up on that terminal; clicking the row already showing puts the drawer away. Drag the drawer's tabs to reorder them.

**Maximize terminal pane**, or **Cmd/Ctrl+Shift+J**, takes the whole height; **Restore terminal pane** brings it back.

On a phone, a terminal takes the whole column, with a row of the keys a phone keyboard lacks beneath it, and you select text with a long press. See [Remote Access](/kepler/remote-environments#remote-access-reach-kepler-from-another-device).

### When a terminal reconnects

A terminal reattaches to its running shell rather than starting a new one:

- While it loads it reads **Loading terminal…**. When the connection drops, nothing shows for the first second. After that, a **Reconnecting to the terminal…** strip leaves the last screen readable and scrollable, and only after five seconds does it cover the terminal. If it can't reconnect, **Unable to restore this terminal** says *The terminal is still running. Retry to load its output again.*, with **Retry**.
- What you type while it reconnects is held and sent once the terminal is back. If the program printed something in the meantime, Kepler drops it instead and says **The terminal changed while reconnecting**: *Nothing you typed was sent. Type it again.* Typing that couldn't reach the terminal at all reads **Unable to send what you typed**.
- One view types at a time. A terminal another view is driving, in another window or on a Remote Access device, reads **Another view is controlling this terminal**. **Take control** lets you type here and sizes the terminal to this view.
- A terminal printing faster than the connection can show reads **Showing the latest output**: *This terminal is printing faster than this connection can show, so older lines are skipped.*
- Input Kepler can't confirm is never resent. See [Agent Sessions](/kepler/agent-sessions#whats-different-in-terminal).

### Reading a tab

Each tab carries **one glyph** that says both what the tab is and how it ended, so a clean finish and a crash don't look alike:

| Kind | What it is |
|---|---|
| **Shell** | A plain terminal you opened |
| **Agent** | A session running an agent in Terminal mode. See [Agent Sessions](/kepler/agent-sessions#how-a-session-runs) |
| **Command run** | One of the repository's commands |

A shell tab also shows what its program reports, when the program reports a status: **Running**, **Needs you**, **Done** or **Failed**. Hover the tab to see the state and, from a minute on, how long it's been in it, plus its message, its progress as a bar reading *{percent}% done*, and any sub-tasks with their own ages. A program that's blocked or failed without saying why gets a next step, such as *Approve it in the terminal.* **Reported by {app}** shows only when the app isn't already the tab's name. An agent tab keeps its own glyph, because its session owns its status.

**A shell tab is named after what runs in it.** That's the app, when the program reports its status, or else the job in front, such as `pnpm dev`. On Windows, it can be the window title the program set. Back at the prompt, the tab returns to its own label, such as **Terminal 2**. While the name differs from the label, hovering the tab shows the label and the job's command line or window title. Command runs and agent tabs keep their names.

When a shell's program needs you or finishes, Kepler sends a notification that names the terminal and its Task, such as *Approve it in {terminal}* or *Finished in {terminal}*. Kepler stays quiet while that terminal is on screen in the focused window. These notifications follow the same notification settings as agent sessions, in **Settings → Notifications**.

A finished command run shows a **result bar** rather than leaving you to read the scrollback: **Exited with code {code}**, **Exited by signal {signal}**, or **Stopped**, with **Run again** and **Close** beside it. A still-running one offers **Stop**.

### File paths are links

File paths printed in a terminal are links, including relative paths, paths with a line suffix such as `src/app.ts:42`, and paths wrapped across lines. Kepler also spots a path an agent mentions as `@src/app.ts`, and one glued to a flag, such as `--config=/etc/app.json`. Cmd-click one (Ctrl-click on Windows and Linux) to open the file [on the task page](#opening-a-file) at its line, and Cmd/Ctrl+Shift+click to open it in your default editor. The hover hint says *Click to open*, or *Click to preview* where the click opens a preview tab, and adds *Click to open in editor* when an editor can take the file.

Right-click a path for more: **Open file**, your default editor (opening at the line), **Open in** for the rest of your editors and your computer's **Default app**, **Save as…**, and **Copy path**. Any of those targets can be your default, with **Set as default**.

Kepler task and session links in a terminal are links too, and so are the task and session IDs Kepler recognizes. The hover hint says *Click to open in Kepler*; Cmd/Ctrl-click opens it, and right-click offers **Open in Kepler** and **Copy link**.

On a phone, long-press a path or link instead, then pick **Open** from the small menu over the selection, which also offers **Copy**, **Paste**, and **Select all**. See [Remote Access](/kepler/remote-environments#remote-access-reach-kepler-from-another-device).

### Closing a busy terminal

Closing a terminal with something running in it confirms first, naming the job you actually launched:

> **Close terminal?** *Stops {command}, which is still running in this terminal.*

**Close terminal** goes ahead. A terminal already closing offers only **Force close**.

Shell tabs survive a Kepler update and come back after a restart. With **Keep agents and terminals running across restarts and updates** on, in **Settings → General**, command runs do too, and each takes up its run again: still running with **Stop**, or finished with its result bar. A plain **Quit** ends them, the way quitting any terminal app does. Quitting Kepler counts busy terminals alongside busy sessions and asks before it takes them down.

***

## What each resource pane shows

| Resource | Details |
|---|---|
| **Worktree**, on disk | A strip of verbs (the branch, the sync control, **Open in**, **Run a command**) over its changed files, which lead into the Changes overlay, plus a **Comments** view that lists the task's review comments with how many are open and unread. See [Review Changes](/kepler/review-changes) |
| **Worktree**, missing | A metadata card instead: **Current branch**, **Base branch**, and the **Recorded path**, flagged **not on disk** or **gone** when it's been removed outside Kepler. A worktree that has gone stays bound to the Task, and Kepler offers to recreate it rather than quietly dropping it |
| **Folder** | Path, plus an editable name and description |
| **File** | The file itself, in the [file viewer](#opening-a-file), with its description, where it came from, and its size on the viewer's toolbar. **Rename** is in **File actions**, and an uploaded copy says it's a copy in the task folder |
| **Pull request** / **Issue** | Status, who it involves, the item's description and its labels. An issue adds its comments |
| **Link** | Every plain link (one that isn't a pull request or issue) shares one **Links** pane, scrolled to the link you picked |
| **Note** | The note itself, with **Copy note** and **Edit**. The **Prompt** note edits the Task's prompt |

**The worktree strip.** The **⋮** beside the branch, **Worktree actions for {branch}**, and a right-click on the branch both open the worktree's full [row menu](#the-row-menu). With more than one worktree, the branch name also switches between the Task's worktrees. **Detach worktree…** only detaches: *The worktree stays on disk — it’s only removed from this task.* **Delete worktree…** is its own entry, never offered on the repository's main worktree.

**Folders and files.** A name or description you edit saves as you type, and **Done** closes the fields.

**Pull requests and issues.** You can select and copy the description text. When Kepler can't read a description, the pane says where to read it, such as *To read the full description, open it on {provider}.* When the read from the provider fails, the pane says *Unable to read this from {provider}, so its details may be missing.*, with a way to fix it.

A pull request's **People** section shows its author, its **Assignees**, and each reviewer with a badge for their review state, tallied as *{reviewed} of {count} reviewed*. Fold it to just the faces. An issue shows its **Assignee**.

An issue from GitHub, GitHub Enterprise, GitLab, GitLab Self-Managed, Jira, or Jira Server also shows its discussion under **Comments · {count}**: the latest comments, each with its author, its age, and its text. **Show earlier comments** pages back, and **Refresh comments** reads them again. Kepler shows the comments for you to read; it doesn't hand them to the agent. When it can't read them, the section says why, such as *Sign in to read this issue’s comments.* or *Comments for {provider} issues aren’t available in Kepler yet.*

<figure style="text-align:center">
  <a href="/wp-content/uploads/issue-comments-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/issue-comments-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Fix the cart total panel (In Review, its worktree card with #51 marked Changes requested, and the #51 Open and #38 Open chips) with GitHub issue #38 open in its side pane: Back to sessions, the issue title Cart total ignores discounts when tax is applied, the GITHUB and ISSUE #38 chips, Open, acme-web and the assignee alex-lee, the bug label and the description, then Comments · 3 with Refresh comments: jo-park, sam-ortiz and alex-lee, each with an avatar, an age and the comment text.">
  </a>
  <figcaption style="text-align:center; color:#888">An issue's comments, in the same reader the task page uses, here in a Dashboard panel.</figcaption>
</figure>

**Links.** The **Links** pane lists every plain link on the Task with its title and URL, an **Open in browser** button, and **Link actions**. The link you clicked is scrolled into view and flashes.

**Notes.** A note has a name you rename in place: double-click it, press **F2** with the note focused, or pick **Rename note** from its row menu. **Enter** saves the name and **Escape** puts it back. Clearing the name leaves an **Untitled note**. The Prompt note can't be renamed. **Enter** on a focused note opens it for editing. A note with unsaved edits says **Unsaved draft**, and **Edit** reads **Resume draft**. Double-clicking the note's text selects a word.

<figure style="text-align:center">
  <a href="/wp-content/uploads/note-rename-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/note-rename-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Coding conventions note open in a task page pane, its name turned into an inline field with the name selected for renaming, above the note's two standing instructions: money is in cents until it is shown, and every cart change gets a test in cart.test.js.">
  </a>
  <figcaption style="text-align:center; color:#888">Renaming a note in place.</figcaption>
</figure>

---
