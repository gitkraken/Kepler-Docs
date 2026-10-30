---
title: Review Changes
description: Review what an agent changed. Read the diff in the Changes overlay, comment on it, stage and commit, update the branch from its base, resolve update conflicts with AI, and hand the rest to AI Sync or AI Compose.
product: Kepler
feature: Review Changes
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
integrations: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [review, diff, changes-overlay, working-changes, commits, staging, amend, review-comments, merge-conflicts, merge-target, push, force-push, pull-requests, ai-sync, ai-compose, ai-conflict-resolution, worktree-cleanup]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

When an agent stops and says it is done, read what it actually changed.

The agent makes its changes in the task's **worktree**: the Git working copy for that task. To review them, open the worktree from the **Changes** group in the task page's context panel. See [The Task View](/kepler/task-view).

You review changes in 2 places:

| Where | Use it to |
|---|---|
| **The worktree tab's changes panel** | Pick a view, see how much changed, scan the list of files, and commit from the commit box |
| **The Changes overlay** | Read a large diff over the page, one file or many, with the file tree and commit box beside it |

Click a file in the changes panel to open it in the Changes overlay, in the same view the panel is showing.

***

## The worktree tab

When you open a worktree from the context panel's **Changes** group, it opens in its own tab. The tab has a row of controls in its header and the changes panel below it.

### Header controls

| Control | What it does |
|---|---|
| The **branch** | Shows the branch this checkout is on. **⋮** beside it, or a right-click, opens the worktree's menu, the same menu the worktree has in the context panel and on the Dashboard. On a task with several worktrees, the branch name also switches between them |
| The **sync control** | One button whose label follows the branch's state (**Publish**, **Push**, **Pull**, **Fetch**, **Update** or **Sync**), with the counts beside it. See [Publishing and syncing the branch](#publishing-and-syncing-the-branch) |
| **Open in** | Opens the checkout in another app. The split button runs your default; the chevron lists the others, ending with **Open on {provider}** when the branch is on a supported host |
| **Run a command** | Lists the repository's configured commands, and **Manage commands…**. See [Settings](/kepler/settings-repositories#per-repository-commands) |

The worktree's menu has these items:

- **Open changes**, **Open in**, and **Open pull request** when one is linked.
- **Continue {operation}** and **Abort {operation}…**, during a stopped rebase or merge.
- A **Branch** submenu: **Rename branch**, the upstream (see [Set or change the upstream](#set-or-change-the-upstream)), **Change merge target…**, **Rebase onto {target}** or **Merge {target} into this branch**, and **Push**, **Pull** and **Fetch**.
- **New session here**, **New terminal here** and **Run command here**.
- **Copy branch name**, **Copy worktree path** and **Copy remote URL**.
- **Refresh**, **Detach worktree…** and **Delete worktree…**.

A header control shows its outline only when you hover over it, when it has keyboard focus, or while its menu is open.

As the column gets narrower, the header shrinks in stages. First, the sync control hides its counts and keeps its icon. Next, the branch name is truncated. Last, **Open in** and **Run a command** leave the row. You can still reach both from a right-click or from the tab's own menu.

To open a shell in this checkout, choose **New terminal here** on the worktree's row in the context panel, or press **Cmd/Ctrl+J**. Terminals open in the terminal drawer below the columns, not in the worktree tab. See [The Task View](/kepler/task-view#the-terminal-drawer).

### The changes panel

The changes panel has a row of views above a list of files, and the commit box below the list.

| Part | What it does |
|---|---|
| **Working changes** | Shows what is not committed yet. Its button shows a count |
| **Commits** | Shows the commits the branch adds on top of its merge target, with a count. The commit list starts with **All commits**; click a commit to show only that commit, or **Shift**-click another to select a range |
| **All changes** | Shows both together: everything from the merge target to the files on disk. With no merge target it reads *No base branch, so this shows uncommitted changes* |
| **All files** | Shows every file in the worktree, not only what changed |
| **Comments** | Shows the task's review comments, with a count of the open ones and a dot for unread replies. See [Review comments](#review-comments) |
| The counts | Show the number of commits, files and changed lines, then **from {branch}**, the merge target they are measured against; in **Commits** and **All changes**, click it to compare against another branch. See [Merge targets](#merge-targets) |
| **View as tree** / **View as list** | Sets how the files are listed |
| **Filter files** | Filters the list |
| **Refresh** | Reads the worktree again |

The view stays where you put it. Kepler does not switch to **Commits** when the last working change is committed, or back to **Working changes** when an agent edits a file, so the list does not move while you read it.

In **All changes**, a file that also has uncommitted work shows a pencil mark, and its tooltip reads **Has uncommitted changes**.

**All files** lists the whole worktree. Changed files show their changes as in **All changes**, and a file you did not change opens as it is. Files and folders that Git ignores are set apart and marked **Ignored**, and symbolic links are marked **Symbolic link**. A folder lists its contents when you open it. A very large folder shows only its first items (*Showing the first {countText} items*).

The header above the commit list reads **{count} commits ahead of {branch}**, and **branched here** marks the merge base. Commits that the upstream does not have yet show a green dot and line, and read **Not pushed**. To see more about a commit:

- Hover over it to see its card: the author, when it was committed, the full message with its lists and trailers, the short hash, its line changes and its file count.
- Right-click it, or press **Shift+F10** or the context menu key, for **Copy commit SHA**, **Copy commit message**, **Open commit on {provider}** and **Copy commit URL**. A commit that is not pushed yet has no page on the host, so its menu leaves out the last two.

With a Jira or Jira Server account connected, Jira issue keys in a commit's message become links. The commit's right-click menu then adds **Open issue {issue}** and **Copy issue URL for {issue}** for each issue the message references. When a message references too many issues, the menu reads **Issue reference matching limit reached**. When a message is too large to read, it reads **Issue references unavailable: commit message is too large**. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

<figure style="text-align:center">
  <a href="/wp-content/uploads/changes-commit-row-tip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/changes-commit-row-tip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A worktree's column on Commits, where the two newest commits have green dots because they are not pushed, and Apply the discount before tax, which is pushed, has a gray one. Clamp the discount at the subtotal is hovered, and its hover card shows Alex Lee, committed 4h ago, the subject, a body with a two-item list and a Refs: #38 trailer, then the short hash, its line changes, 1 file and a Not pushed chip.">
  </a>
  <figcaption style="text-align:center; color:#888">Unpushed commits, and the card for one of them.</figcaption>
</figure>

A wholly untracked folder with hundreds of files, such as a build output nobody ignored or a test sandbox, shows as one dimmed row with its file count instead of one row per file. Click **Show** on the row to list the files. Untracked files never show line counts, and a line total that leaves out a collapsed folder's files is marked **partial**. Staging, discarding and committing act on the folder as a whole, and the confirmation names its file count.

***

## The Changes overlay

To open the Changes overlay, click a file, or choose **Open changes** from the worktree's menu. The overlay opens over the page at a width for one column of code, or two if you last used **Split**. Drag its edges to resize it. At that default width, **Maximize** in its header fills the window, and **Restore size** returns it to the default width.

<figure style="text-align:center">
  <a href="/wp-content/uploads/changes-overlay-maximize-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/changes-overlay-maximize-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total open over the task page at its default width, with the task page showing around it, and the Maximize button in the overlay's header hovered, its tooltip reading Maximize.">
  </a>
  <figcaption style="text-align:center; color:#888">The Changes overlay at its default width, with Maximize in its header.</figcaption>
</figure>

<div class="note" markdown="1">

**You can act on a diff in the overlay as well as read it.** In **Working changes** and **All changes** you can edit a file in place. In **Working changes** you can also stage it, commit it, resolve its conflicts, discard it or delete it. You can leave review comments for your agent too. See [Staging and committing](#staging-and-committing) and [Review comments](#review-comments).

</div>

### The layout

| Part | What it holds |
|---|---|
| The tree | The same file tree and view as the changes panel, with its own view and layout controls. In **Working changes**, each row has a staging checkbox and the commit box is below the list; in **Comments**, the task's [comment list](#the-comments-view) replaces the tree |
| The viewer | The diff, or several diffs stacked when you opened a folder or a selection. A single file can show as **File**, the whole file with its changes marked in the gutter, or **Changes**, the diff |

**Hide changes panel**, or **Cmd/Ctrl+B**, hides the tree and gives its width to the viewer. While the tree is hidden, the view picker and a **Jump to file…** switcher move to the viewer's header, so you can still change views and files.

A file's header has **File** and **Changes**, **Stacked** and **Split**, then **Find**, **Wrap lines**, **Open in**, and a menu that includes **Add to task**. An unchanged file always shows as **File**, and a deleted file as **Changes**. A file in **Commits** shows **As of {sha}**: the file as that commit left it. While an edit is unsaved, the **File** and **Changes** toggle is unavailable and reads *Save or discard your edit to switch views*.

### Moving around

| Gesture | What it does |
|---|---|
| Click a file | Opens it on its own |
| **Cmd/Ctrl**-click | Adds a file to the set on screen |
| **Shift**-click | Extends the selection to a range |
| Click a folder | Opens every file in it, stacked |
| Type a name in the tree | Jumps to the first file that starts with it |
| **Alt+↑** / **Alt+↓** | Previous and next file |
| **F7** / **Shift+F7** | Next and previous change, carrying on into the next file that has one |
| **Cmd/Ctrl+Shift+A** | **Open all changes** |
| **Cmd/Ctrl+B** | Shows or hides the changes panel |
| **F6** / **Shift+F6** | Moves between the header, the tree, the commit message and the viewer |
| **Cmd/Ctrl+P** | **Filter files**, or **Jump to file…** when the tree is hidden |
| **Cmd/Ctrl+F** | Filters the tree when the tree has focus, and finds in the code anywhere else |
| **Escape** | Closes the overlay. With an unsaved edit, it asks first |

The header counts what you are reading: **{index} of {total}**, and **{count} files shown** once a filter is narrowing it.

### Reading a diff

- Each diff is headed by the **file name**, then its folder, with its **+/−** line stats. Hover the name for the full path.
- Added lines are green, removed lines red.
- **Unmodified regions are collapsed**, leaving three lines of context around each change.
- **Expand all** and **Collapse all** act on every diff in the stack. To fold a single diff, use its own header.
- **Wrap lines** on the viewer's header wraps long lines instead of scrolling them sideways.
- A file that is unchanged in the current view shows as **Unchanged in this scope** instead of being hidden.
- A conflicted file is marked **!** in the tree and the viewer.

Right-click a file row for its menu:

- **Stage file** or **Unstage file**, **Discard changes** and **Delete**.
- **Open in editor**.
- An **Open in** submenu with your editors, **Open in default app**, **Show in Finder** (macOS), **Show in Explorer** (Windows) or **Show in file manager** (Linux), and **Open file on {provider}** when the file exists on a supported host.
- **Copy path** and **Copy relative path**, at the end of the menu.

If you select several rows, the menu items act on all of them.

### Finding in the code

**Cmd/Ctrl+F** in the viewer opens a find bar at the viewer's top right. The find bar searches every file in the stack, including your edits, and counts the matches as **{current} of {total}**, or **No results**. It does not search collapsed unchanged lines.

Use these keys in the find bar:

| Control | Windows and Linux | macOS |
|---|---|---|
| Next match | **F3** | **Cmd+G** |
| Previous match | **Shift+F3** | **Cmd+Shift+G** |
| **Match case** | **Alt+C** | **Cmd+Option+C** |
| **Match whole word** | **Alt+W** | **Cmd+Option+W** |
| **Use regular expression** | **Alt+R** | **Cmd+Option+R** |

**Escape** closes the bar. Kepler remembers the 3 toggles. If you select text on one line before you open the bar, the selection fills the search field.

<figure style="text-align:center">
  <a href="/wp-content/uploads/code-find-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/code-find-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total showing cart.js and cart.test.js stacked, 2 files shown. The find bar at the top right holds discount, with Match case on beside Match whole word and Use regular expression, and reads 5 of 6 with Previous match, Next match and Close find. Every match is highlighted in both files, the current one on line 4 of cart.js.">
  </a>
  <figcaption style="text-align:center; color:#888">Finding across a stack of two files.</figcaption>
</figure>

You can select and copy across a whole file, including lines that are not on screen. Double-click to select a word.

### Editing in place

In **Working changes** and **All changes**, the viewer shows the file on disk. To edit it, click into the diff, or into the whole file in **File** view, and type. **Cmd/Ctrl+S** saves.

An unsaved edit shows **Unsaved** with **Save** and **Discard** beside it. Kepler never discards an edit without asking: **Escape**, closing the overlay, or moving to another file, view or worktree asks **Save your edit?** first. You cannot stage or commit a file with an unsaved edit until you save or discard it, because Git records what is on disk.

When you edit a file through a symbolic link, Kepler saves the file the link points to and leaves the link as it is. A file you cannot edit shows a lock after its name. Hover over it or focus it to see the reason:

- *To edit this file, switch to Working changes or All changes. Commits are read-only.*
- *A symbolic link's target can't be edited here.*
- *Only UTF-8 text files can be edited here.*
- *This file is read-only here.*

### Stacked or split

**Stacked** shows removals and additions in one column. **Split** shows the old and new file side by side. The toggle is on the viewer's header, and **Settings → Appearance → Diff view** sets which layout it starts with.

**Split** needs room for 2 columns of code. When the viewer is narrower than 640 pixels, the diff shows as **Stacked** whatever the setting says, and the header reads **Too narrow for a split diff** instead of cutting off both sides.

### Diffs that are not code

| Case | What you see |
|---|---|
| Images and SVGs | **Before** and **After** previews, each with its size on disk |
| A new file | The whole file, syntax-highlighted, rather than an all-additions diff |
| A file with no textual change | **No textual changes to display** |
| A file whose change is too large | *This file is too large to show here ({size}).* |
| A very large diff | Once the diff is too large as a whole, each remaining file reads *This change is not shown because the whole diff is too large.* and has no line stats |

Kepler normalizes line endings in diffs, so a file that changed from CRLF to LF does not show as fully rewritten.

### When changes fail to load

If Kepler cannot read the changes, the view says so instead of showing an empty list: **Unable to load these changes**, with **Try again**. When Git gives no reason, the view adds *Git did not say why.*

An empty view shows one of these messages:

- **No working changes** or **No changes in this scope**, when there is nothing to show.
- **No base branch to compare against yet**, in **Commits**, when the branch has nothing to measure against, such as a detached HEAD or a default branch with no upstream.
- **No commits**, when the branch is level with its base or has no commit yet.

### On a phone

When you use Kepler in a phone's browser through Remote Access, the overlay replaces its header and tree with one bar:

- **Close**.
- The file's name, which opens the list of changed files as a sheet from the bottom of the screen.
- Previous and next file.
- A menu with the remaining controls: the view and the commit pick, **File** or **Changes**, the diff layout, **Wrap lines**, saving or discarding an edit, why a file is read-only, and the file's own actions.

The overlay opens **Stacked** on a phone, with lines wrapped.

<figure style="text-align:center">
  <a href="/wp-content/uploads/phone-changes-bar-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/phone-changes-bar-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Changes overlay on a phone, showing cart.js with wrapped lines under one bar: Close, the file name cart.js with a chevron, Previous and Next file, and More actions, whose menu is open. It lists Change scope (Working changes, 2 ticked, Commits, All changes, All files), File view (File, Changes ticked), Diff layout (Stacked ticked, Split unavailable as Too narrow for a split diff), Wrap lines ticked, Comment on selection and Open in editor (both unavailable), Copy path and Copy relative path.">
  </a>
  <figcaption style="text-align:center; color:#888">The Changes overlay on a phone, with its menu open.</figcaption>
</figure>

See [Remote Environments](/kepler/remote-environments).

***

## Review comments

Read the diff, mark what needs fixing, and send your notes to the agent, one at a time or as a batch. The agent can answer each comment in a thread of its own.

Kepler saves comments with the task, so they stay after a reload and appear in every window. Kepler does not post them to your Git host.

<figure style="text-align:center">
  <a href="/wp-content/uploads/review-comment-draft-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/review-comment-draft-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total with cart.js open in the Changes view. Lines 3 and 4 are selected and a review comment draft is open beneath them: Comment on lines 3 to 4 above the note Pull the discount and rounding into one helper, then the target To OpenCode Fix the cart total: discounts should apply before tax. with its chevron, Cancel, Add comment and Send now.">
  </a>
  <figcaption style="text-align:center; color:#888">A review comment draft, under the lines it's about.</figcaption>
</figure>

To start a comment, do one of the following:

| To comment on | Do this |
|---|---|
| One line | Hover it and click the **+** beside its line number |
| A range | Click the **+** on the first line, then **Shift**-click the last, or extend with **Shift+↑** / **Shift+↓** |
| What you selected in the editor | **Cmd/Ctrl+Shift+C**, which also works on the line the caret is on |

You can comment in every view (**Working changes**, **Commits**, **All changes** and **All files**), including on a file shown whole, such as a new file. A file you open in a file tab or the file viewer accepts comments too. The file's header and its tree row show how many comments the file has.

### Write and send a comment

A draft opens under the last line, headed **Comment on line {line}** or **Comment on lines {start} to {end}**. Below the note, **To {agent} {name}** names the session that receives the comment. Its chevron opens a list of the task's sessions, each marked **Chat** or **Terminal**, and **Task folder** for a session in the task's own folder. A session that is not running reads *Comments wait here until it runs*.

To finish the draft, follow these steps:

1. Type your note. A comment with no note sends the selected lines as context.
2. Choose how it goes:
   - **Add comment**, or **Cmd/Ctrl+Enter**, adds it to that session's queue.
   - **Send now**, or **Cmd/Ctrl+Shift+Enter**, sends it to the session at once.
3. To send the queued comments, press **Send comments ({count})** in the overlay's header, or send your next prompt in that session.

Queued comments show as a **{count} comments** chip in that session's composer and go out with its next prompt. The header's **Send comments ({count})** sends every queued comment on the task, in one prompt for each session. When the session is not on screen, a notification says *Queued for {agent} session {name}* or *Comments are waiting in {agent} session {name}*, with **Open** to go to it. Each comment in a prompt carries its `path:lines`, the quoted code, and your note.

On a task with no session yet, **Send now** reads **Start a session**, which opens a new session's draft with the comments as its first prompt. In an overlay opened from outside a conversation, such as from a file path, you cannot send comments: *Open this file from a conversation to send comments*.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-review-comments-01-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-review-comments-01-v4@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total with cart.js open in the Changes view and three review comments under the lines they are about. The comment on line 2 reads Not sent yet, with Add to queue and Send now; the comments on lines 3 and 4 read Queued for OpenCode Fix the cart total: discounts should apply before tax., with Remove from queue and Send now. Each card opens with You, just now and its note, and has Edit comment and Delete comment icons. Line 2 is picked in the gutter. The overlay header reads 3 comments and Send comments (2), with the Comment options menu open on Discard unsent comments.">
  </a>
  <figcaption style="text-align:center; color:#888">Comments not sent and queued, with Send comments in the overlay header.</figcaption>
</figure>

Each comment appears as a card under its lines. The card's status line shows the comment's state, and the actions the card offers depend on that state:

| Status | The card offers |
|---|---|
| **Not sent yet** | **Edit comment**, **Delete comment**, **Add to queue** and **Send now** |
| **Queued for {agent} {name}** | **Edit comment**, **Delete comment**, **Remove from queue** and **Send now** |
| **Sending to {agent} {name}** | Nothing, until the prompt has gone out |
| **Sent to {agent} {name} {time}** | **Reply to {agent}**, **Resolve** and **Delete comment** |
| **Resolved**, or **Resolved by {agent} {name}** | **Reopen** |

After a comment goes out in a prompt, you cannot edit its text, because the agent has already read it. The overlay's header shows **{count} comments**, which opens the [Comments view](#the-comments-view), and a **Comment options** menu with **Discard unsent comments**. Discarding keeps the comments you have already sent.

Kepler keeps what you type. **Escape** only moves focus out of a draft's field, and a draft with text stays when you close the overlay or move to another file.

### Replies and resolving

The agent answers a comment you sent in a thread under it, and it can resolve the comment when the fix is done. The card shows the conversation in order: your note, then each reply, oldest first, labeled **You** or with the agent and its session.

<figure style="text-align:center">
  <a href="/wp-content/uploads/review-comment-thread-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/review-comment-thread-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total with cart.js open and a sent review comment under line 3, its status Sent to OpenCode Fix the cart total: discounts should apply before tax. just now. The card reads as a conversation: You with the note Clamp the discounted subtotal at zero so a large discount cannot make the total negative, then OpenCode's reply under the session's name, Agreed. I'll clamp it with Math.max(0, subtotal - discount) and add a test for a discount larger than the order. Below them sit the Reply to OpenCode box, Resolve and Reply.">
  </a>
  <figcaption style="text-align:center; color:#888">A sent comment with the agent's reply.</figcaption>
</figure>

- **Reply**: type in **Reply to {agent}** and press **Reply**, or **Cmd/Ctrl+Enter**. The reply goes to the session the comment was last sent to. If that session is gone, choose another: *Choose a session to reply to*.
- **Resolve** closes the comment, and **Reopen** opens it again. A resolved card starts collapsed.
- **Unread replies**: a card with replies you have not read shows **{count} new replies** and marks each one **New**. The replies count as read once the card has been on screen for a moment. To set this yourself, use **Mark as read** or **Mark as unread**.

To collapse a card to a one-line row, click the chevron beside its lines. Click the row to expand it again.

### The Comments view

The **Comments** view lists every review comment on the task. Open it from the view picker in the changes panel or the overlay, after **All files**. Its button shows the number of open comments, with a dot when there are unread replies.

<figure style="text-align:center">
  <a href="/wp-content/uploads/review-comments-list-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/review-comments-list-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total on its Comments view, its header reading 3 comments and Send comment. The side list reads 3 comments with View options, then the comments grouped by status: Not sent (cart.js:2), Queued (cart.js:4) and Sent (cart.js:3), each row with its place, just now, its note and its status. Beside it, cart.js shows the three cards: line 2 Not sent yet with Add to queue and Send now, line 3 Sent to OpenCode with the Reply to OpenCode box, Resolve and Reply, and line 4 Queued for OpenCode with Remove from queue and Send now.">
  </a>
  <figcaption style="text-align:center; color:#888">The Comments view, grouped by status.</figcaption>
</figure>

Each row shows the comment's place, when it was written, the note and its status. Click a row to show its code and go to its card. A comment whose worktree was removed reads *Its worktree was removed*. A row's own buttons and its right-click menu offer **Send now**, **Resolve**, **Reopen**, **Mark as read** and **Delete comment**, as its status allows.

**View options** sets how the list reads:

- **Group by**: **File**, **Status** or **None**. By status, the sections are **Unread replies**, **Not sent**, **Queued**, **Sent** and **Resolved**.
- **Sort by**: **Line order** or **Latest activity**.
- **Show resolved**: lists resolved comments too.

With no comments, the view reads *To comment on code, press + beside a line number or select some text.*

### When the code moves

A comment stays with its code. If the agent moves the lines it is on, the card moves with them. If the agent changes those lines, the card stays near where it was, marked **Outdated** (*The code changed after this comment*), and shows **Lines as they were when commented on**.

A view of the files on disk shows every comment on a file, whichever commit it was written on, so a card stays visible after the agent edits or commits. A commit you pick in **Commits** shows only the comments written on that commit. Comments on files that are not in the view are listed in the header as **{count} comments outside this diff**, or **{count} comments not shown here** in a file view. Opening a comment whose file has no changes in the view opens the file whole: *This file has no changes here now, so it opens as a whole file.*

***

## Staging and committing

In **Working changes**, you stage files in the tree and commit them from the commit box below it. The changes panel and the overlay share one commit box per worktree, so a message you start in one appears in the other, and Kepler keeps it when the overlay closes.

<figure style="text-align:center">
  <a href="/wp-content/uploads/staging-commit-box-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/staging-commit-box-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The worktree column for kepler/fix-cart-total on Working changes, beside Commits, All changes and All files. cart.js is ticked and cart.test.js is not, so the header box is partly checked and its badge reads 1 of 2 staged. Below the files sits the commit box, with Commit message, Amend last commit and Commit.">
  </a>
  <figcaption style="text-align:center; color:#888">Staging files in Working changes, above the commit box.</figcaption>
</figure>

### Staging

- Each file and folder row has a checkbox: tick it to stage, untick to unstage. **Space** on a focused row does the same. The tree's header box stages or unstages everything listed, and its badge reads **{staged} of {total} staged**.
- A filter narrows what the header box acts on, so a file you filtered out is never swept up with the rest.
- **Discard changes**, or pressing **Delete** on a focused row (**Backspace** on a Mac), asks first. Your current version goes to the Trash (the Recycle Bin on Windows), so you can get it back.
- **Delete** in the row menu removes the file from disk without changing the index, so Git reports the deletion like any other. It also moves the file to the Trash.

If Kepler cannot use the Trash, the confirmation says the change is permanent before you confirm it.

### The commit box

The commit box looks like the prompt composer: one message field whose first line is the subject. A counter appears once the subject is longer than 50 characters.

| Control | What it does |
|---|---|
| The message field | **Cmd/Ctrl+Enter** commits |
| **Amend last commit** | Rewrites the last commit instead of adding one. Ticking it fills an empty box with the last commit's message and changes the button to **Amend commit** |
| **Commit** | Commits what is staged |

You can amend with nothing staged to change only the message. If you amend a commit you have already pushed, Kepler asks **Amend a pushed commit?** first, because the next push will have to force.

When you cannot commit yet, the button's tooltip says why: **Stage changes above to commit**, **Enter a commit message**, **Save or discard your edit first**, **Wait for staging to finish**, or **Resolve the conflicts first**.

Kepler commits exactly what you were looking at. It waits for any staging still in progress. If an agent changes the index in the meantime, Kepler refuses the commit, keeps your message, and says *The staged files changed since you looked. Check them, then commit again.*

When a Git hook stops the commit, the box says **A Git hook stopped the commit** and shows the end of the hook's output, with **Show output** for the rest. To stop a hook that does not finish, click **Cancel commit**.

### Resolving merge conflicts

When a merge, rebase, cherry-pick or revert stops on conflicts, the conflicted files show a **!**.

| To resolve a file | Do this |
|---|---|
| By hand | Edit it in the viewer, save, then tick its checkbox or choose **Mark resolved**. If conflict markers are still in it, Kepler asks first |
| Take one side whole | **Use current version** or **Use incoming version** from the row menu. Your hand-merged copy goes to the Trash first |

When no file is conflicted, finish the operation:

- A stopped merge, cherry-pick or revert finishes with a commit from the commit box.
- A rebase continues from the worktree's menu with **Continue rebase**, which is unavailable until every conflict is resolved.

**Abort {operation}…** returns the branch to the state it was in before the operation started.

### Other ways to commit

| How | When |
|---|---|
| **Ask the agent** | The common case. The agent that wrote the change commits it, and you read the result |
| **The worktree's terminal** | `git add`, `git commit`, your own aliases. **New terminal here** on the worktree's row in the context panel opens one already in the right folder |
| **AI Compose** | Give an agent tools that reorganize messy changes into clean, focused commits. See [Agent tools: AI Sync and AI Compose](#agent-tools-ai-sync-and-ai-compose) |

***

## Publishing and syncing the branch

The **sync control** in the worktree tab's header is one button. Its label changes with what the branch needs:

| State | The button reads | What it does |
|---|---|---|
| Behind or diverged from its merge target | **Update**, or **Review conflicts** with a warning icon when updating would conflict | Opens the Sync view in the worktree panel. See [Updating from the base](#updating-from-the-base) |
| Rebased by an applied sync, with the result not yet pushed | **Sync**, with *Open Sync to push this result* | Opens the Sync view, where you push the result or roll it back |
| No upstream | **Publish**, with *Creates {remote}/{branch} on the remote* | Publishes the branch |
| Ahead | **Push**, with **{count} ahead** | Pushes |
| Rebased outside the Sync view, so the remote has the old commits | **Force push**, with *Rebased onto {target} — force push to update the remote* | Replaces the remote's old commits after you confirm **Force push?** |
| Behind | **Pull**, with **{count} behind** | Pulls. A branch that is both ahead and behind its upstream reads *Behind, pull first* on Push |
| Up to date | **Fetch**, with **Up to date** | Updates your remote-tracking refs, and removes the ones whose branch was deleted on the remote, so deleted branches leave every branch picker |

The counts change only when Kepler fetches, so the control shows when it last checked: **Checked {time}**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/sync-control-push-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/sync-control-push-oct-2026.png" class="help-center-img img-bordered" alt="The sync control in the worktree's header reading Push with 2 commits ahead, and its card open: Push 2 commits, the remote branch it pushes to, 2 ahead, and Checked just now.">
  </a>
  <figcaption style="text-align:center; color:#888">The sync control on a branch that's ahead of its upstream.</figcaption>
</figure>

The chevron beside the button opens a menu. Its first item is the button's current action, followed by these items:

- **Push** (or **Publish**), **Pull** and **Fetch**. Each says where it goes: *To {upstream}*, *From {upstream}*, and *From {remote}* or *From all remotes: {remotes}*.
- **Set upstream** or **Change upstream**, on any branch that is not a detached HEAD. See [Set or change the upstream](#set-or-change-the-upstream).
- **Force push**: *Rewrites the remote branch*. The menu offers it when the branch has diverged from its upstream, so a force push is always a separate, deliberate click. While an applied sync result is waiting to be pushed, the menu leaves it out, unless the branch changed after the sync.
- **Update**: shows where the branch stands against its merge target and opens the Sync view. It reads **Review conflicts** when updating would conflict, and **Sync** after an applied sync.

After you apply a rebase, the remote still has the branch's old commits. The main button then reads **Sync** and opens the Sync view, where **Push** sends the result. See [Updating from the base](#updating-from-the-base). For a branch rebased some other way, **Force push** becomes the main button instead. The **Force push?** confirmation explains that the branch was rebased and that Kepler refuses the force push if someone else pushed in the meantime.

<figure style="text-align:center">
  <a href="/wp-content/uploads/sync-control-menu-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/sync-control-menu-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The sync control's chevron menu open beside the Publish button of kepler/fix-cart-total, a branch with no upstream yet: Publish (Choose where to publish), Pull, unavailable with Publish first, and Fetch, then Set upstream with a submenu arrow, then Update.">
  </a>
  <figcaption style="text-align:center; color:#888">The sync control's chevron menu on a branch with no upstream yet.</figcaption>
</figure>

**SSH keys that ask for a PIN or passphrase.** On macOS and Linux, a fetch you start yourself, such as **Fetch** or **Refresh branches**, can use your `SSH_ASKPASS` helper, so a key that needs a PIN or passphrase, such as a security key, can fetch. Kepler allows at most 3 prompts per connection, and 60 seconds for each. Fetches that Kepler runs in the background never prompt. On Windows, Kepler never prompts, so use an SSH agent.

### Set or change the upstream

The upstream is the remote branch that **Push** and **Pull** use. To set it, change it or remove it, open **Set upstream** or **Change upstream** from the sync control's menu or from the worktree's **Branch** submenu. **Change upstream** shows the branch it tracks now.

The picker lists every remote branch under **Search remote branches**:

- A tracked branch that no longer exists comes first, marked **Not found**.
- A remote branch with the same name as yours is marked **Same name**, and the one you track now **Current**.
- **Publish as {remote}/{branch}…** sits above the list when no remote has a branch of the same name, and opens the publish dialog.
- **Unset upstream** sits above the list when the branch tracks one.

Any remote branch can be the upstream, whatever its name. When you pick one, Kepler saves it at once: *Upstream set to {upstream}*. The picker lists only branches already fetched. To find a branch someone else just pushed, click **Refresh branches**, beside the search field, which fetches from every remote.

<figure style="text-align:center">
  <a href="/wp-content/uploads/upstream-picker-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/upstream-picker-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The sync control's chevron menu on kepler/fix-cart-total, which reads Push with 2 ahead, with Change upstream (origin/kepler/fix-cart-total) open beside it: a Search remote branches field with a Refresh branches button, Unset upstream pinned above the list, the tracked branch first and marked Current and Same name, then origin/docs/style-guide, origin/main and origin/release/2.4.">
  </a>
  <figcaption style="text-align:center; color:#888">Change upstream, from the sync control's menu.</figcaption>
</figure>

### Updating from the base

The Sync view rebases or merges the branch onto its merge target. It works on a copy first, and your branch changes only when you apply the result: *Sync prepares a result to review before applying it.*

<figure style="text-align:center">
  <a href="/wp-content/uploads/update-view-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/update-view-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The sync view titled Sync kepler/fix-cart-total, from origin/main with Rebase selected in the Rebase and Merge control, at Ready to apply: The rebase onto origin/main is ready. Apply updates your branch. Sync sits beside Apply & push and its chevron.">
  </a>
  <figcaption style="text-align:center; color:#888">The sync view with a clean result, ready to apply and push.</figcaption>
</figure>

To sync the branch with its merge target, follow these steps:

1. Open the Sync view from the sync control. The title reads **Sync {branch}**, with **from {branch}** under it. Kepler picks the detected base. To use another base, choose it from the picker. **Refresh branches**, beside the picker's search field, fetches from every remote first.
2. Choose **Rebase** or **Merge** in the **Sync method** control beside the base.
3. Press **Sync**. The view reads *Preparing the sync result…* while it works. To abandon a run in progress, press **Stop**. Your branch is never touched, and any earlier result stays available.
4. When the copy reaches **Ready to apply**, apply it:
   - For a clean result (no conflicts, nothing resolved by AI) on a branch that can push, the main button is **Apply & push**, with **Apply** in its menu.
   - Otherwise the main button is **Apply**, with **Apply & push** in its menu when the branch can push.

**Apply** moves your branch to the result, and the view reads **Branch synced**. If the branch can push, **Push** then sends it, so you can apply first and push once you have checked the branch. After a rebase, the push replaces the remote's old commits. Kepler pins every push from the Sync view to the local and remote commits you saw, so it never overwrites work someone else pushed in the meantime.

To undo an applied sync, press **Roll back**: *Restore the branch to before sync and keep this result ready to apply again.* When the remote holds exactly the applied result, **Roll back & push** is offered too. It asks **Roll back and push?** first, because it replaces the published branch with the restored one, and the push stops if someone else changed the remote branch.

When a push from the Sync view fails, your local result is kept:

- If the remote branch moved, the view reads *The remote branch changed. Sync with it before pushing; your local result is preserved.* It fetches and points the base at the remote branch, so the next **Sync** brings in the remote's changes.
- If your local branch changed, it reads *The local branch changed. Refresh and review it before retrying Push.*
- For any other failure, **Push** stays offered so you can try again. If a **Roll back & push** restored the branch but the push failed, the view keeps that push offered until it goes through.

A result waiting to be applied does not lock the branch, so the branch or its base can move on in the meantime. You can also pick another base or switch the method after a run. In each case, the result no longer matches: the view reads *The last update result is out of date*, and **Sync** becomes the main button to prepare a new one. Kepler does not apply a result whose base moved.

<figure style="text-align:center">
  <a href="/wp-content/uploads/update-view-stale-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/update-view-stale-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The sync view for kepler/fix-cart-total, from main with Merge now selected in the Rebase and Merge control, reading The last update result is out of date: The branch, base, or selected method no longer matches this result. Sync before applying a result. Sync is the only action beside the title, next to the close button.">
  </a>
  <figcaption style="text-align:center; color:#888">A sync result that's out of date. Sync prepares a new one.</figcaption>
</figure>

After an applied sync, when the branch or its base moves on, the view reads *The branch or {base} changed. Sync to prepare the next result.* If your branch changed after the sync instead, it reads *Your branch changed after the update. Sync to prepare a new result.* If a new base needs nothing from your branch, the view says so and keeps your earlier result.

A run that fails says why, under **Sync failed**. Press **Sync** to try again.

When syncing would conflict, the sync control reads **Review conflicts**. The view title reads **Sync {branch} with conflicts**, with **with {branch}** under it, and lists the conflicting files. Pick a file to see its conflicting hunks.

You can resolve the conflicts in 2 ways:

- **Resolve them with AI.** Press **Sync**: on a conflicting branch, it resolves the conflicts with AI. See [Resolve update conflicts with AI](#resolve-update-conflicts-with-ai).
- **Resolve them yourself.** Rebase in the worktree's terminal and resolve each file in the [file tree](#resolving-merge-conflicts).

### Resolve update conflicts with AI

AI conflict resolution runs the rebase or merge on a copy and resolves each conflicted file for you. Your branch changes only when you apply the result.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-sync-ai-conflicts-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-sync-ai-conflicts-01-v3@2x.png" class="help-center-img img-bordered" alt="The sync view for kepler/fix-cart-total in its conflict state: Sync kepler/fix-cart-total with conflicts, with main and the Rebase and Merge control (Rebase selected), the Sync button, 1 file conflicts with main, and cart.js with 1 conflict region.">
  </a>
  <figcaption style="text-align:center; color:#888">The sync view on a conflicting branch. Sync resolves the conflicts with AI.</figcaption>
</figure>

AI conflict resolution needs all of the following:

- A paid GitKraken plan. On the Community plan, the button shows a padlock and its tooltip reads *AI conflict resolution needs a paid plan.*
- **AI Sync** turned on in **Settings → Agents → Agent tools**. While it is off, the tooltip reads *Turn on Sync in Settings → Agents → Agent tools to resolve conflicts with AI.*
- A GitKraken sign-in. If you are not signed in, the run stops with *Sign in to GitKraken to resolve conflicts with AI.*

To resolve conflicts with AI, follow these steps:

1. Open the Sync view from **Review conflicts** on the sync control.
2. Check the base under the title. To use another base, choose it from the picker.
3. Choose **Rebase** or **Merge** in the **Sync method** control, then press **Sync**.
4. Watch the progress line, which reads *Resolving conflicts · {count} files resolved*. To abandon the run, press **Stop**.
5. When the run reaches **Ready to apply**, read the review. See [Read the AI review](#read-the-ai-review).
6. Press **Apply**. If the branch can push, **Apply & push** is in its menu. To leave the result unapplied, close the view; your branch stays as it was.

If the AI cannot finish some files, the run stops without changing your branch: *Your branch wasn't changed. The AI was unable to finish these files, so the update stopped.* Each file is listed with the reason, such as a binary file, or a conflict Git cannot merge as text. You resolve those files by hand.

#### Read the AI review

The review explains what the AI changed so you can decide whether to apply it. It contains the following parts:

- **A verdict badge**: **No issues found**, **Needs review** or **Blocked**.
- **A summary**: a short explanation of the run, followed by any *Check:* items that name a file and the reason to look at it, such as *low confidence*, *possible issue* or *left unresolved*.
- **A summary line**: *AI resolved {count} files · confidence {confidence}%*.
- **A card for each commit**: the commit's short SHA and subject, or **Merge** for a merge run, and its file count. A card shows **Resolving…** while the AI works on it.
- **A row for each file**: the method used and a confidence badge, followed by the AI's reasoning for that file. A low confidence shows as a warning. A file the run stopped on before the AI finished it is marked **Incomplete** with a warning icon, and neither it nor a **Skipped** file carries a confidence badge.

Each file row shows one of the following methods. **Ours** and **Theirs** are Git's names for the two sides of the conflict. In a merge, **Ours** is your branch and **Theirs** is the base. In a rebase they swap: **Ours** is the branch you are rebasing onto, and **Theirs** is your branch.

| Method | Meaning |
|---|---|
| **AI** | The AI wrote the resolution |
| **Ours** | Kept the **Ours** side |
| **Theirs** | Kept the **Theirs** side |
| **Deleted** | Resolved by deleting the file |
| **Auto** | Resolved mechanically, without the AI |
| **Skipped** | Left unresolved |

Kepler keeps the review across reloads and windows, so you can close the view and come back to it before you apply.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-sync-ai-review-01-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-sync-ai-review-01-v4@2x.png" class="help-center-img img-bordered" alt="The sync view for kepler/fix-cart-total after an AI rebase: Sync kepler/fix-cart-total with conflicts, with main and Rebase selected, Ready to apply with Sync and Apply, a Needs review badge over the AI's summary and the check &quot;cart.js — low confidence&quot;, the line AI resolved 1 file · confidence 75%, and a commit card for Apply the discount before tax listing cart.js with its AI method, a 75% confidence badge and what the AI did.">
  </a>
  <figcaption style="text-align:center; color:#888">An AI review at Ready to apply.</figcaption>
</figure>

Click a file row to review that file in full. Its review names the commit, the method (**Kept {branch}** when the AI kept one side), the confidence and the AI's reasoning. Then it shows each conflict as **Conflict {n} of {total}**, at its line, marked **Kept {branch}** or **Merged**, with its own confidence and the AI's reason for it. **Conflict layout** sets how each conflict reads:

- **Conflict | Result**: the conflict with Git's markers for both branches and the common ancestor, beside the result.
- **Branches + ancestor**: both branches and the **Common ancestor** side by side, then the result.

To see more of the file around a conflict, use **Show {count} more lines above** and **below**, or **Show all lines**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/sync-ai-file-review-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/sync-ai-file-review-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The AI review of cart.js after a rebase onto main: commit 97c56d7 Apply the discount before tax, the AI method, a 75% badge and the AI's reasoning, with Conflict layout set to Conflict | Result beside Branches + ancestor. Below, Conflict 1 of 1 at Line 3 is marked Merged at 75% with the AI's reason, Main extracted roundCents; the branch reordered the discount. Combined both. The Conflict pane shows git's markers for main, the common ancestor and kepler/fix-cart-total, and the Result pane the merged code.">
  </a>
  <figcaption style="text-align:center; color:#888">One file's AI review, conflict by conflict.</figcaption>
</figure>

<!-- TODO(verify): Resolution method and persistence behavior verified against kepler v0.15.0 strings and src/ui/components/git/sync/; check against a live AI run before publishing. -->

***

## Merge targets

A branch's **merge target** is the branch it will merge into: what its commits, counts and **Update** are measured against. Kepler detects one, and you can change it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/change-merge-target-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/change-merge-target-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A worktree's right-click menu in the task view with Branch open, and Change merge target, reading origin/release/2.4, open beside it: a Search branches field with a Refresh branches button above a list of remote branches, with origin/main marked Automatic, origin/release/2.4 marked Saved, and Reset to automatic (origin/main) at the bottom.">
  </a>
  <figcaption style="text-align:center; color:#888">Change merge target, from a worktree's Branch submenu.</figcaption>
</figure>

| To | Do this |
|---|---|
| Compare against another branch for now | In **Commits** or **All changes**, click **from {branch}** in the changes panel or the overlay and pick a branch. The commit list, counts and header controls follow it, the label's tooltip reads **For this view only**, and nothing is saved |
| Keep that comparison | Click **Save as merge target** beside the branch you picked (**Save** in a narrow panel). Only remote branches can be saved |
| Change it | Choose **Change merge target…** from the merge target chip on the Dashboard, or from the worktree's **Branch** submenu, which shows the current target beside it. The picker lists remote branches only, and choosing one saves it |
| Go back to the detected one | **Reset to automatic ({ref})** in the picker |
| Find a branch someone else just pushed | **Refresh branches**, beside the picker's search field, fetches from every remote. The pickers list only branches already fetched |
| Update the branch from its merge target | **Rebase onto {target}** or **Merge {target} into this branch** from the merge target chip's menu on the Dashboard, or from the worktree's **Branch** submenu. Both open the [Sync view](#updating-from-the-base) with that method chosen |

<figure style="text-align:center">
  <a href="/wp-content/uploads/save-merge-target-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/save-merge-target-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The worktree column for kepler/fix-cart-total on Commits, with All commits over three commits and origin/release/2.4 marked branched here. The counts row compares from origin/release/2.4, picked for this view only, with a Save as merge target button beside the picker, above cart.js and cart.test.js.">
  </a>
  <figcaption style="text-align:center; color:#888">A branch picked for this view only, with Save as merge target beside it.</figcaption>
</figure>

Kepler and GitLens share a branch's merge target, so a change you make in GitLens shows up in Kepler while it is running.

A branch that landed in its merge target without a pull request counts as merged. That includes rebase-merged and squash-merged branches, which Git itself does not see as merged; Kepler checks their content. The Dashboard says **Merged into {target}**.

***

## Where else changes show up

The Dashboard's task preview shows each worktree as a two-row **worktree button**:

- The top row: the branch and repository, its menu, the pull request, and the sync control.
- The bottom row: chips for the uncommitted files, the commits and the merge target, with **Open in** and **Run** beside them. Each chip has a hover card that says what a click does, and a right-click menu of its own.
- A task with several worktrees shows one worktree button at a time. Its leading edge shows the position (**{position}/{count}**) and expands to **Show all {count} worktrees**. The branch name becomes a switcher you can also step through with the arrow keys, and **Auto-switch to active worktree** lets it follow whichever worktree is busiest.

Click the uncommitted or commits chip to open that worktree's changes panel, on that view, in a side pane of the task panel, without going to the task page first. The pane appears beside the sessions when the panel is wide enough, and in place of them when it is not. Its files open the same Changes overlay. Click the chip again to close the pane, or press **Cmd/Ctrl+Shift+G** to show or hide it. See [The Kepler Interface](/kepler/kepler-interface).

A file or folder in a worktree opens in the Changes overlay too, wherever you open it by its path, such as a file path in a terminal or **Open in Changes** on a file tab's menu. A file opens in **File** view, at its line: on **Working changes** when it has uncommitted changes, and on **All files** otherwise. A folder opens on **All files**, with its changed files stacked.

### Update many worktrees at once

To bring several worktrees and local branches up to date with their bases in one pass, use **Update** in **Settings → Repositories → Worktrees and branches**. The **Update worktrees** panel checks each one and lists what it will update and what it skips, such as a worktree with uncommitted changes, one where an agent is working, or a branch already checked out in a worktree. A local branch with no worktree is updated in place, without being checked out.

Choose **Rebase** or **Merge**, and tick **Push after update** to push each updated branch too. Branches with no upstream are updated but not pushed, and say *No upstream, update only*. Nothing changes until you press **Update**, and **Roll back** undoes a worktree's update. See [Settings](/kepler/settings-repositories#update-worktrees).

***

## Opening a pull request

**Kepler does not have a button that creates a pull request.** You open the pull request outside Kepler: the agent opens it, you run a command in the worktree's terminal, or you use your host's website. Once the pull request exists, Kepler tracks it as a task resource. A pull request gets attached to the task in one of 3 ways:

| Path | What happens |
|---|---|
| **The agent publishes it** | When an agent publishes a pull request, Kepler reads the result, checks that it belongs to one of the worktree's remotes, and attaches it to the task. You do not need to do anything |
| **The agent attaches it** | Agents can attach a link to the task themselves with Kepler's workspace tools. Kepler works out from the URL whether it is a pull request, an issue, or a plain link, and fetches its title and status where it can, attaching the link even when that lookup fails. The same tools detach a link, including one you attached yourself |
| **You attach an existing one** | **Add resource → Pull requests** in the task view searches your connected hosts. **Add to task** attaches what you pick |

Kepler asks an agent to attach only the pull request the task is actually about, not every URL it reads while investigating. Anything the agent attaches shows up in the task right away.

Attaching a pull request also unlocks the **Address Feedback** Action on that task. See [Actions](/kepler/actions) and [Pull Request Integrations](/kepler/pull-request-integrations).

***

## Agent tools: AI Sync and AI Compose

AI Sync and AI Compose give agents Git tools they do not otherwise have. Both are off until you turn them on, and both need a **paid GitKraken subscription**. Turn them on in **Settings → Agents → Agent tools**, which Kepler describes as *Kepler's own tools your agents can call, starting with rebasing, merging and cleaning up commits.* The section lists these tools:

| Tool | What it gives agents |
|---|---|
| **AI Sync** | *Lets agents rebase or merge your branch and resolve conflicts for you. Every change can be undone.* |
| **AI Compose** | *Lets agents turn messy changes into clean, focused commits. Every change can be undone.* |

With a tool turned on, the agents in your sessions gain the matching tools, and you ask for the work in the chat. AI Sync also powers the Sync view's **Sync** button when the branch has conflicts. See [Resolve update conflicts with AI](#resolve-update-conflicts-with-ai).

| Tool | How an agent uses it |
|---|---|
| **AI Sync** | Updates the branch from its base with a rebase or merge, and resolves conflicts as it goes. By default, the agent prepares the result for review and leaves the branch untouched until it applies the result. You can read the outcome first and have it applied or rolled back. AI Sync backs up every run. It also drops commits whose changes are already upstream, which helps after a squash-merge. Tell the agent what matters, such as which side is authoritative and what it must preserve, and it passes that guidance to the conflict resolver |
| **AI Compose** | Plans the reorganization first and applies it as a second step, so you can read the plan before anything moves. It can also split a multi-commit branch into a stack, and undo what it applied |

When you turn either tool on, Kepler confirms that *New agent sessions will pick up this change.* A running session keeps the tools it started with. To use a new tool, start a new session.

Both sets of tools work on the session's own worktree by default. Each can also name another worktree attached to the same task, so one session can clean up a branch it is not working in.

On the Community plan, both rows still appear, with a padlock and the tooltip *Not available on the Community plan. Upgrade to unlock.* Everything else on this page works on the Community plan, except AI conflict resolution.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-features-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-features-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Agent tools section of Settings › Agents, with AI Sync (lets agents rebase or merge your branch and resolve conflicts) and AI Compose (lets agents turn messy changes into focused commits), both off.">
  </a>
  <figcaption style="text-align:center; color:#888">AI Sync and Compose, in the agent settings.</figcaption>
</figure>

***

## Related

- [The Task View](/kepler/task-view): the context panel, the columns, and where the worktree opens
- [Tasks and Resources](/kepler/tasks-and-resources): worktrees, and detaching or deleting one safely
- [Agent Sessions](/kepler/agent-sessions): directing the agent that produced these changes
- [Actions](/kepler/actions): **Review** on a task reviews exactly this uncommitted work
- [Settings](/kepler/settings): [**Diff view**](/kepler/settings-app#diff-view), [**Agent tools**](/kepler/settings-agents#agent-tools), and [**Worktrees and branches**](/kepler/settings-repositories#worktrees-and-branches)

---
