---
title: Review Changes
description: Review what an agent changed. Read the diff in the Changes overlay, comment on it, stage and commit, update the branch from its base, resolve update conflicts with AI, and hand the rest to AI Sync or AI Compose.
product: Kepler
feature: Review Changes
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, azure-devops]
integrations: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, azure-devops]
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [review, diff, changes-overlay, working-changes, commits, staging, amend, review-comments, merge-conflicts, merge-target, push, force-push, pull-requests, ai-sync, ai-compose, ai-conflict-resolution, worktree-cleanup]
taxonomy:
  category: kepler
custom_fields:
    entry_title: "Review and ship what an agent wrote"
    entry_role: "Ship"
    entry_desc: "Read the diff, comment, commit, and update the branch from its base"
    entry_order: 30
    nav_category: "kepler-working-in-kepler"
    nav_label: "Review Changes"
    nav_order: 60
    nav_parent: "kepler-working-in-kepler"
    page_type: "content"
    card_icon: "git-compare"
    card_color: "blue"
    card_description: "Read the diff, comment, commit, update the branch and resolve conflicts with AI"
---
<kbd>Last updated: November 2026</kbd>

When an agent stops and says it is done, read what it actually changed.

The agent makes its changes in the task's **worktree**: the Git working copy for that task. To review them, open the worktree from the **Changes** group in the task page's context panel. See [The Task View](/kepler/task-view).

You review changes in 2 places:

| Where | Use it to |
|---|---|
| **The worktree tab's changes panel** | Pick what to show, see how much changed, scan the list of files, and commit |
| **The Changes overlay** | Read a large diff over the page, one file or many, with the file tree beside it |

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

In a narrow column, **Open in** and **Run a command** leave the header. You can still reach both from a right-click or from the tab's own menu.

To open a shell in this checkout, choose **New terminal here** on the worktree's row in the context panel, or press **Cmd/Ctrl+J**. Terminals open in the terminal drawer below the columns, not in the worktree tab. See [The Task View](/kepler/task-view#the-terminal-drawer).

### The changes panel

The changes panel has a view picker at the top, then the branch's changes, then the files.

| Part | What it does |
|---|---|
| **Changes** | Shows what the branch changed, as one list you pick from. Its button counts the uncommitted files |
| **Files** | Shows every file in the worktree, not only what changed |
| **Comments** | Shows the task's review comments, with a count of the open ones and a dot for unread replies. See [Review comments](#review-comments) |
| The counts | Show the number of files and changed lines, measured **from {branch}**, the merge target, on **All changes**; click it to compare against another branch. See [Merge targets](#merge-targets) |
| **View as tree** / **View as list** | Sets how the files are listed |
| **Filter files** | Filters the list |
| **Refresh** | Reads the worktree again |

In **Changes**, the list shows the branch from the newest work down to where it started:

- **All changes**: everything from the merge target to the files on disk.
- **Working changes**: what is not committed yet.
- **Commits**: every commit the branch adds on top of its merge target, followed by each commit on its own.
- **branched here**: the merge base, where the branch started.

Click a row to show it. **Shift**-click another row to show everything between them, such as **Working changes** and the newest commits, which the counts read as **Working + {count} commits**. **Cmd/Ctrl**-click adds a row to what you show, or takes it away. A branch with commits opens on **All changes**, and a branch with only uncommitted work opens on **Working changes**. A branch with neither reads **No changes on this branch yet**.

What you picked stays picked when an agent edits a file, so the list does not move while you read it.

When you show commits together with uncommitted work, a file that also has uncommitted work shows a pencil mark, and its tooltip reads **Has uncommitted changes**.

**Files** lists the whole worktree. Changed files show their changes as in **All changes**, and a file you did not change opens as it is. Files and folders that Git ignores are set apart and marked **Ignored**, and symbolic links are marked **Symbolic link**. A very large folder shows only its first items.

Commits that the upstream does not have yet show a green dot and line, and read **Not pushed**. To see more about a commit:

- Hover over it to see its card: the author, when it was committed, the full message, the short hash, and its line and file counts.
- Right-click it, or press **Shift+F10**, to copy its SHA or message. A pushed commit also has **Open commit on {provider}** and **Copy commit URL**.

With a Jira or Jira Server account connected, Jira issue keys in a commit's message become links, and the commit's right-click menu adds **Open issue {issue}** and **Copy issue URL for {issue}**. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

<figure style="text-align:center">
  <a href="/wp-content/uploads/changes-commit-row-tip-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/changes-commit-row-tip-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="A worktree's column on its Changes view, whose list reads All changes, then three commits and origin/main branched here. The two newest commits have green dots because they are not pushed, and Apply the discount before tax, which is pushed, has a grey one. Hovering Clamp the discount at the subtotal opens its hover card, which shows Alex Lee, committed 4h ago, the subject, a body with a two-item list and a Refs: #38 trailer, then the short hash, its line changes, 1 file and a Not pushed chip.">
  </a>
  <figcaption style="text-align:center; color:#888">Unpushed commits, and the card for one of them.</figcaption>
</figure>

A wholly untracked folder with hundreds of files, such as a build output nobody ignored or a test sandbox, shows as one dimmed row with its file count instead of one row per file. Click **Show** on the row to list the files. Staging, discarding and committing act on the folder as a whole.

***

## The Changes overlay

To open the Changes overlay, click a file, or choose **Open changes** from the worktree's menu. The overlay opens over the page at a width for one column of code, or two if you last used **Split**. Drag its edges to resize it. At that default width, **Maximize** in its header fills the window, and **Restore** returns it to the default width.

<figure style="text-align:center">
  <a href="/wp-content/uploads/changes-overlay-maximize-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/changes-overlay-maximize-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total open over the task page at its default width, with the task page showing dimmed around it, and the Maximize button in the overlay's header ringed and hovered, its tooltip reading Maximize. The header also reads from main and Up to date; the overlay's side list has the view switch's icon buttons for Changes (2), Files and Comments over Working changes, 2 files and main branched here, then Commit… and the two changed files, beside cart.js's diff. The context panel behind ends with Manage resources.">
  </a>
  <figcaption style="text-align:center; color:#888">The Changes overlay at its default width, with Maximize in its header.</figcaption>
</figure>

> **Tip:** **You can act on a diff in the overlay as well as read it.** In **Working changes** and **All changes** you can edit a file in place. In **Working changes** you can also resolve its conflicts, discard it or delete it, and **Commit…** lets you stage and commit it. You can leave review comments for your agent too. See [Staging and committing](#staging-and-committing) and [Review comments](#review-comments).

### The layout

| Part | What it holds |
|---|---|
| The tree | The same view picker, list of changes and file tree as the changes panel, with its own controls. In commit mode, the rows have staging checkboxes and the commit box is below them; in **Comments**, the task's [comment list](#the-comments-view) replaces the tree |
| The viewer | The diff, or several diffs stacked when you opened a folder or a selection. A single file can show as **File**, the whole file with its changes marked in the gutter, or **Changes**, the diff |

**Hide changes panel**, or **Cmd/Ctrl+B**, hides the tree and gives its width to the viewer. While the tree is hidden, the view picker and a **Jump to file…** switcher move to the viewer's header, and the picker also lists the rows of **Changes**, so you can still change what you show and which file.

A file's header has **File** and **Changes**, **Find**, the diff layout button (**Stacked** or **Split**), **Wrap lines**, **Open in**, and a menu that includes **Add to task**. A file shown from a commit shows **As of {sha}**: the file as that commit left it, with **Edit** to switch to its working copy. See [Editing in place](#editing-in-place).

An unsaved edit goes with you when you switch between **File** and **Changes**. If the switch is unavailable, save or discard your edit first.

The overlay's header shows the branch the changes are measured against, **from {branch}**, with a chip that reads **{count} new** or **Up to date**. See [What's new on the merge target](#whats-new-on-the-merge-target).

### Moving around

| Gesture | What it does |
|---|---|
| Click a file | Opens it on its own |
| **Cmd/Ctrl**-click | Adds a file to the set on screen |
| **Shift**-click | Extends the selection to a range |
| Click a folder | Opens the changed files in it, stacked |
| Type a name in the tree | Jumps to the first file that starts with it |
| **Alt+↑** / **Alt+↓** | Previous and next file |
| **F7** / **Shift+F7** | Next and previous change, carrying on into the next file that has one |
| **Cmd/Ctrl+Shift+A** | **Open all changes** |
| **Cmd/Ctrl+B** | Shows or hides the changes panel |
| **F6** / **Shift+F6** | Moves between the header, the tree, the commit message and the viewer |
| **Cmd/Ctrl+P** | **Filter files**, or **Jump to file…** when the tree is hidden |
| **Cmd/Ctrl+F** | Filters the tree when the tree has focus, and finds in the code anywhere else |
| **↑** / **↓** in read-only code | Moves the line highlight. **Shift+↑** / **Shift+↓** extends it, and **C** comments on it |
| **←** / **→** in a split diff | Switches the line highlight between the old and new side |
| **Escape** | Clears a line selection, leaves commit mode, then closes the overlay. With an unsaved edit, it asks first |

In a file you can edit, the arrow keys move the caret instead. The same keys work in the file viewer.

The header counts what you are reading: **{index} of {total}**, and **{count} files shown** once a filter is narrowing it.

### Reading a diff

- Each diff is headed by the **file name**, then its folder, with its **+/−** line stats. Hover the name for the full path.
- Added lines are green, removed lines red.
- **Unmodified regions are collapsed**, leaving three lines of context around each change.
- **Expand all** and **Collapse all** act on every diff in the stack. To fold a single diff, use its own header.
- **Wrap lines** on the viewer's header wraps long lines instead of scrolling them sideways.
- A file that is unchanged in the current view shows as **Unchanged in this scope** instead of being hidden.
- A conflicted file is marked **!** in the tree and the viewer.

Hover a row to show its own buttons. A file still on disk has **Open in {editor}**. In **Working changes**, a row also has **Discard changes**, and a conflicted file has **Mark resolved**. In commit mode, **Stage file** or **Unstage file** takes the place of **Open in {editor}**.

Right-click a file row for its menu:

- **Discard changes** and **Delete**, and in commit mode **Stage file** or **Unstage file**.
- **Edit working copy**, on a file shown from a commit. See [Editing in place](#editing-in-place).
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
  <a href="/wp-content/uploads/code-find-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/code-find-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total showing cart.js and cart.test.js stacked, 2 files shown. The find bar at the top right holds discount, with Match case on beside Match whole word and Use regular expression, and reads 5 of 6 with Previous match, Next match and Close find. Every match is highlighted in both files, the current one on line 4 of cart.js. The overlay header reads from main and Up to date, and the stack bar ends with the Diff layout and Wrap lines buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">Finding across a stack of two files.</figcaption>
</figure>

You can select and copy across a whole file, including lines that are not on screen. Double-click to select a word.

### Editing in place

In **Working changes** and **All changes**, the viewer shows the file on disk. To edit it, click into the diff, or into the whole file in **File** view, and type. **Cmd/Ctrl+S** saves.

An unsaved edit shows **Unsaved** with **Save** and **Discard** beside it. Kepler never discards an edit without asking: **Escape**, closing the overlay, or moving to another file, view or worktree asks **Save your edit?** first. Switching between **File** and **Changes** carries the edit across instead. You cannot stage or commit a file with an unsaved edit until you save or discard it, because Git records what is on disk.

**Editing a file from a commit.** A file shown from a commit you picked in the list is read-only, but you can switch it to the file on disk: click **Edit** in its header, choose **Edit working copy** from its row menu, or press **Cmd/Ctrl+E**.

The file opens in **File** view, marked **Working**, ready to edit. Switch the file to **Changes** to see the diff counted from where the commit view started. **Stop editing** returns to the file as committed.

<figure style="text-align:center">
  <a href="/wp-content/uploads/changes-edit-working-copy-nov-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/changes-edit-working-copy-nov-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total, from origin/main, on its Changes view, with the oldest commit, Apply the discount before tax, picked in the list under All changes and the two newer commits, above origin/main (branched here) and the file cart.js. The viewer has switched cart.js to the working copy: its header reads 1 of 1, M, cart.js and Working, with Stop editing beside the File and Changes switch, File selected, and the file open for editing.">
  </a>
  <figcaption style="text-align:center; color:#888">A file from a commit switched to its working copy, ready to edit.</figcaption>
</figure>

When you edit a file through a symbolic link, Kepler saves the file the link points to and leaves the link as it is. A file you cannot edit, such as a file from a commit or one that is not UTF-8 text, shows a lock after its name. Hover over the lock to see why.

### Stacked or split

**Stacked** shows removals and additions in one column. **Split** shows the old and new file side by side. To switch, open the diff layout button on a file's header and pick **Stacked** or **Split**. **Diff layout**, in **Settings → Appearance**, sets which layout the overlay starts with.

**Split** needs room for 2 columns of code. When the viewer is narrower than 640 pixels, the diff shows as **Stacked** and **Split** is unavailable.

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

If Kepler cannot read the changes, the view says so instead of showing an empty list: **Unable to load these changes**, with **Try again**.

In a repository you have not trusted, Kepler runs no git, so the view reads **Trust this repository to see its changes**. To show the changes, click **Trust**. See [Trust a repository](/kepler/settings-repositories#trust-a-repository).

An empty view shows one of these messages:

- **No changes on this branch yet**, in **Changes**, when the branch has no commits and nothing uncommitted.
- **No working changes** or **No changes in this scope**, when what you picked has nothing to show.
- **No base branch to compare against yet**, when the branch has nothing to measure its commits against, such as a detached HEAD or a default branch with no upstream.
- **No commits**, when the branch is level with its base or has no commit yet.

### On a phone

When you use Kepler in a phone's browser through Remote Access, the overlay replaces its header and tree with one bar:

- **Close**.
- The file's name, which opens the list of changed files as a sheet from the bottom of the screen.
- Previous and next file.
- A menu with the remaining controls: the view and what to show from the list of changes, **File** or **Changes**, the diff layout, **Wrap lines**, saving or discarding an edit, why a file is read-only, and the file's own actions.

The overlay opens **Stacked** on a phone, with lines wrapped.

<figure style="text-align:center">
  <a href="/wp-content/uploads/phone-changes-bar-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/phone-changes-bar-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Changes overlay on a phone, showing cart.js with wrapped lines under one bar: Close, the file name cart.js with a chevron, Previous and Next file, and More actions, whose menu is open. It lists Change scope (Changes, 2 ticked, Files and Comments) with a Working changes submenu, File view (File, Changes ticked), Diff layout (Stacked ticked, Split unavailable as Too narrow for a split diff), Wrap lines ticked, Comment on selection and Open in editor (both unavailable), Copy path and Copy relative path.">
  </a>
  <figcaption style="text-align:center; color:#888">The Changes overlay on a phone, with its menu open.</figcaption>
</figure>

See [Remote Environments](/kepler/remote-environments).

***

## Review comments

Read the diff, mark what needs fixing, and send your notes to the agent, one at a time or as a batch. The agent can answer each comment in a thread of its own.

Kepler saves comments with the task, so they stay after a reload and appear in every window. Kepler does not post them to your Git host.

<figure style="text-align:center">
  <a href="/wp-content/uploads/review-comment-draft-oct-2026-v6@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/review-comment-draft-oct-2026-v6@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total with cart.js open in the Changes view. Lines 3 and 4 are selected and a review comment draft is open beneath them: Comment on lines 3 to 4 above the note Pull the discount and rounding into one helper, then the target: a TO stamp, the OpenCode logo and the session title Fix the cart total: discounts should apply before tax., with its chevron, then Cancel, Add comment and Send now. The overlay header reads from main and Up to date; the file header holds File and Changes, then Find, Diff layout, Wrap lines and More actions.">
  </a>
  <figcaption style="text-align:center; color:#888">A review comment draft, under the lines it's about.</figcaption>
</figure>

To start a comment, do one of the following:

| To comment on | Do this |
|---|---|
| One line | Hover it and click the **+** beside its line number |
| A range | Click the **+** on the first line, then **Shift**-click the last, or extend with **Shift+↑** / **Shift+↓** |
| The line highlight | Move it with **↑** / **↓** in read-only code, then press **C** |
| What you selected in the editor | **Cmd/Ctrl+Shift+C**, which also works on the line the caret is on |

You can comment in **Changes**, whatever you picked in its list, and in **Files**, including on a file shown whole, such as a new file. A file attached to the task, open in its tab, accepts comments too, and so does a file in the file viewer. Notes take comments too. See [Comment on a note](#comment-on-a-note). The file's header and its tree row show how many comments the file has.

### Write and send a comment

A draft opens under the last line. Below the note, **To** and the session's title show which session receives the comment. To send it to another of the task's sessions, pick one from its chevron. Comments for a session that is not running wait until it runs.

To finish the draft, follow these steps:

1. Type your note. A comment with no note sends the selected lines as context.
2. Choose how it goes:
   - **Add comment**, or **Cmd/Ctrl+Enter**, adds it to that session's queue.
   - **Send now**, or **Cmd/Ctrl+Shift+Enter**, sends it to the session at once.
3. To send the queued comments, press **Send comments ({count})** in the overlay's header, or send your next prompt in that session.

Queued comments show as a **{count} comments** chip in that session's composer and go out with its next prompt. The header's **Send comments ({count})** sends every queued comment on the task, in one prompt for each session. When the session is not on screen, a notification offers **Open** to go to it. Each comment reaches the agent with its file, lines, the code, and your note.

On a task with no session yet, **Send now** reads **Start a session**, which opens a new session's draft with the comments as its first prompt. To send comments, open the file from a conversation: an overlay opened some other way, such as from a file path, cannot send them.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-review-comments-01-v6@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-review-comments-01-v6@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total with cart.js open in the Changes view and three review comments under the lines they are about. The comment on line 2 reads Not sent yet, with Add to queue and Send now; the comments on lines 3 and 4 show the OpenCode logo and Queued for Fix the cart total: discounts should apply before tax., with Remove from queue and Send now. Each card opens with You, just now and its note, and has Edit comment and Delete comment icons. Line 2 is picked in the gutter. The overlay header reads 3 comments and Send comments (2), with the Comment options menu open on Discard unsent comments, beside from main and Up to date.">
  </a>
  <figcaption style="text-align:center; color:#888">Comments not sent and queued, with Send comments in the overlay header.</figcaption>
</figure>

Each comment appears as a card under its lines. What the card offers depends on its status:

| Status | The card offers |
|---|---|
| **Not sent yet** | **Edit comment**, **Delete comment**, **Add to queue** and **Send now** |
| **Queued for {session}** | **Edit comment**, **Delete comment**, **Remove from queue** and **Send now** |
| **Sending to {session}** | Nothing, until the prompt has gone out |
| **Sent to {session} {time}** | **Reply to {agent}**, **Resolve** and **Delete comment** |
| **Resolved**, or **Resolved in {session}** when the agent resolved it | **Reopen** |

After a comment goes out in a prompt, you cannot edit its text, because the agent has already read it. The overlay's header shows **{count} comments**, which opens the [Comments view](#the-comments-view), and a **Comment options** menu with **Discard unsent comments**. Discarding keeps the comments you have already sent.

Kepler keeps what you type. **Escape** only moves focus out of a draft's field, and a draft with text stays when you close the overlay or move to another file.

### Replies and resolving

The agent answers a comment you sent in a thread under it, and it can resolve the comment when the fix is done. The card shows your note, then each reply, oldest first.

<figure style="text-align:center">
  <a href="/wp-content/uploads/review-comment-thread-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/review-comment-thread-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total with cart.js open and a sent review comment under line 3, its status the OpenCode logo and Sent to Fix the cart total: discounts should apply before tax. just now. The card reads as a conversation: You with the note Clamp the discounted subtotal at zero so a large discount cannot make the total negative, then the reply under the OpenCode logo and the session title, Agreed. I'll clamp it with Math.max(0, subtotal - discount) and add a test for a discount larger than the order. Below them sit the Reply to OpenCode box, Resolve and Reply. The overlay header reads from main, Up to date and 1 comment.">
  </a>
  <figcaption style="text-align:center; color:#888">A sent comment with the agent's reply.</figcaption>
</figure>

- **Reply**: type in **Reply to {agent}** and press **Reply**, or **Cmd/Ctrl+Enter**. The reply goes to the session the comment was last sent to. If that session is gone, Kepler asks you to choose another.
- **Resolve** closes the comment, and **Reopen** opens it again. A resolved card starts collapsed.
- **Unread replies**: a card with replies you have not read shows **{count} new replies** and marks each one **New**. To change this yourself, use **Mark as read** or **Mark as unread**.

New replies also show in the session: its tab counts them, its composer shows a **{count} new replies** chip, and each reply appears in the conversation with **Open in Changes**. See [Reading the conversation](/kepler/agent-sessions#reading-the-conversation).

To collapse a card to a one-line row, click the chevron beside its lines. Click the row to expand it again.

### The Comments view

The **Comments** view lists every review comment on the task. Open it from the view picker in the changes panel or the overlay, after **Files**. Its button shows the number of open comments, with a dot when there are unread replies.

<figure style="text-align:center">
  <a href="/wp-content/uploads/review-comments-list-oct-2026-v5@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/review-comments-list-oct-2026-v5@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total on its Comments view (the speech-bubble segment, 3, picked beside the Changes and Files icons), its header reading 3 comments and Send comment. The side list reads 3 comments with View options, then the comments grouped by status: Not sent (cart.js:2), Queued (cart.js:4) and Sent (cart.js:3), each row with its place, just now, its note and its status. Beside it, cart.js shows the three cards: line 2 Not sent yet with Add to queue and Send now, line 3 Sent to Fix the cart total: discounts should apply before tax. beside the OpenCode logo, with the Reply to OpenCode box, Resolve and Reply, and line 4 Queued for the same session with Remove from queue and Send now. The header also reads from main and Up to date.">
  </a>
  <figcaption style="text-align:center; color:#888">The Comments view, grouped by status.</figcaption>
</figure>

Each row shows the comment's place, when it was written, the note and its status. Click a row to show its code and go to its card. A row's own buttons and its right-click menu offer **Send now**, **Resolve**, **Reopen**, **Mark as read** and **Delete comment**, as its status allows.

**View options** sets how the list reads:

- **Group by**: **File**, **Status** or **None**.
- **Sort by**: **Line order** or **Latest activity**.
- **Show resolved**: lists resolved comments too.

### When the code moves

A comment stays with its code. If the agent moves the lines it is on, the card moves with them. If the agent changes those lines, the card stays near where it was, marked **Outdated**, and shows the lines as they were when you commented.

A view of the files on disk shows every comment on a file, whichever commit it was written on, so a card stays visible after the agent edits or commits. A commit you pick in the list of changes shows only the comments written on that commit. The header counts comments on files that are not in the view. Opening a comment whose file has no changes in the view opens the file whole.

### Comment on a note

A task's notes take review comments too, so you can ask an agent to fix a note the way you ask it to fix code. In an open note, start a comment in one of these ways:

- Select lines, then click **Comment on the selected lines**.
- Hover a heading, then click **Comment on section**.
- Right-click the note and choose **Comment**.

While you edit a note, comment on its lines as you would in a file. The draft works like a comment on code: pick the session, then click **Add comment** or **Send now**. The agent's reply in the conversation offers **Open note**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/note-comment-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/note-comment-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Coding conventions note open on the task page, with its Money heading pointed at and its Copy link to section and Comment on section buttons beside it. Under the Money section's two lines a comment draft is open: Comment on lines 1 to 4, the note Say whether tax is worked out before or after the rounding, the target To with the OpenCode logo and the session Fix the cart total: discounts should apply before tax., then Cancel, Add comment and Send now. The Tests heading starts below the draft.">
  </a>
  <figcaption style="text-align:center; color:#888">A comment draft on a note's section.</figcaption>
</figure>

***

## Staging and committing

You stage and commit in commit mode. To enter it, pick **Working changes** in the list of changes and click **Commit…**, first on the files toolbar. **Commit…** appears only while the worktree has uncommitted files.

In commit mode, **Commit to {branch}** takes the place of the list of changes, each file gets a staging checkbox, and the commit box appears below the files. **Cancel**, or **Escape**, leaves commit mode. Committing leaves it too, and marks the new commit in the list. Outside commit mode, the rows have no checkboxes, and you can still open or discard a file.

The changes panel and the overlay share one commit box per worktree, so a message you start in one appears in the other, and Kepler keeps it when the overlay closes.

<figure style="text-align:center">
  <a href="/wp-content/uploads/staging-commit-box-oct-2026-v5@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/staging-commit-box-oct-2026-v5@2x.png" class="help-center-img img-bordered" alt="The worktree column for kepler/fix-cart-total in commit mode, on Changes 2 beside Files and Comments. The header reads Commit to kepler/fix-cart-total, Pick the files to commit, then write a message, with Cancel. cart.js is ticked and cart.test.js is not, so the header box is partly checked and its badge reads 1 of 2 staged; the file list's toolbar also holds the Discard button. Below the files sits the commit box, with Commit message, Amend last commit and Commit.">
  </a>
  <figcaption style="text-align:center; color:#888">Staging files in commit mode, above the commit box.</figcaption>
</figure>

### Staging

- In commit mode, each file and folder row has a checkbox: tick it to stage, untick to unstage. **Space** on a focused row does the same. The tree's header box stages or unstages everything listed, and its badge reads **{staged} of {total} staged**.
- A file you edited after staging it shows a hollow checkbox, *Has changes that aren't staged*, and so does a folder that holds one.
- A filter narrows what the header box acts on, so a file you filtered out is never staged with the rest.
- Hovering a row shows its own **Stage file** or **Unstage file** button.

To discard changes:

- **Discard changes** on a row, or **Delete** on a focused row (**Backspace** on a Mac), asks first. Your current version goes to the Trash (the Recycle Bin on Windows), so you can get it back. If Kepler cannot use the Trash, the confirmation says the change is permanent.
- On a file with staged and unstaged changes, discarding removes only the unstaged changes. Discard again to remove the staged ones too.
- **Discard folder**, in a folder's menu, discards the files under it.
- **Discard** in the tree's toolbar discards the selected files, or every listed file when nothing is selected. Its label says which, and it asks first. To discard every listed file instead of the selection, **Alt**-click it (**Option**-click on a Mac).
- **Discard** is unavailable on a conflicted file until you resolve the conflicts.
- **Delete** in the row menu moves the file to the Trash, and Git reports the deletion like any other.

### The commit box

The commit box looks like the prompt composer: one message field whose first line is the subject. A counter appears once the subject is longer than 50 characters.

| Control | What it does |
|---|---|
| The message field | **Cmd/Ctrl+Enter** commits |
| **Amend last commit** | Rewrites the last commit instead of adding one. Ticking it fills an empty box with the last commit's message and changes the button to **Amend commit** |
| **Commit** | Commits what is staged |

While the worktree has uncommitted files, you can amend with nothing staged to change only the message. If you amend a commit you have already pushed, Kepler asks **Amend a pushed commit?** first, because the next push will have to force.

When you cannot commit yet, such as with nothing staged or no message, the button's tooltip says why.

Kepler commits exactly what you were looking at. If an agent changes the staged files before you commit, Kepler stops the commit and keeps your message, so you can check the files and commit again.

When a Git hook stops the commit, the box says **A Git hook stopped the commit** and shows the end of the hook's output, with **Show output** for the rest. To stop a hook that does not finish, click **Cancel commit**.

If a commit fails after you left commit mode, Kepler takes you back to it to show why. When the commit box is not on screen, a notification reads **Unable to commit to {branch}**, with **Show** to open it.

### Resolving merge conflicts

When a merge, rebase, cherry-pick or revert stops on conflicts, the conflicted files show a **!**.

| To resolve a file | Do this |
|---|---|
| By hand | Edit it in the viewer, save, then choose **Mark resolved**, or tick its checkbox in commit mode. If conflict markers are still in it, Kepler asks first |
| Take one side whole | **Use current version** or **Use incoming version** from the row menu. Your hand-merged copy goes to the Trash first |

When no file is conflicted, finish the operation:

- A stopped merge, cherry-pick or revert finishes with a commit: click **Commit…** on **Working changes**, then **Commit**.
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
| Behind or diverged from its merge target | **Update**, or **Review conflicts** when updating would conflict | Opens the Sync view. See [Updating from the base](#updating-from-the-base) |
| Rebased by an applied sync, not yet pushed | **Sync** | Opens the Sync view, where you push the result or roll it back |
| No upstream | **Publish** | Creates the branch on the remote |
| Ahead | **Push**, with **{count} ahead** | Pushes. A branch that is also behind must pull first |
| Rebased outside the Sync view | **Force push** | Replaces the remote's old commits after you confirm |
| Behind | **Pull**, with **{count} behind** | Pulls |
| Up to date | **Fetch**, with **Up to date** | Fetches, and drops branches deleted on the remote from every branch picker |

The counts change only when Kepler fetches, so the control shows when it last checked: **Checked {time}**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/sync-control-push-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/sync-control-push-oct-2026.png" class="help-center-img img-bordered" alt="The sync control in the worktree's header reading Push with 2 commits ahead, and its card open: Push 2 commits, the remote branch it pushes to, 2 ahead, and Checked just now.">
  </a>
  <figcaption style="text-align:center; color:#888">The sync control on a branch that's ahead of its upstream.</figcaption>
</figure>

The chevron beside the button opens a menu. Its first item is the button's current action, followed by these items:

- **Push** (or **Publish**), **Pull** and **Fetch**, each with where it goes.
- **Set upstream** or **Change upstream**. See [Set or change the upstream](#set-or-change-the-upstream).
- **Force push**, when the branch has diverged from its upstream, so a force push is always a separate click.
- **Update**, which opens the Sync view. It reads **Review conflicts** when updating would conflict, and **Sync** after an applied sync.

After you apply a rebase in the Sync view, the main button reads **Sync** until you push the result there. For a branch rebased some other way, **Force push** becomes the main button. Kepler refuses a force push if someone else pushed in the meantime.

<figure style="text-align:center">
  <a href="/wp-content/uploads/sync-control-menu-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/sync-control-menu-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The sync control's chevron menu open beside the Publish button of kepler/fix-cart-total, a branch with no upstream yet: Publish (Choose where to publish), Pull, unavailable with Publish first, and Fetch, then Set upstream with a submenu arrow, then Update.">
  </a>
  <figcaption style="text-align:center; color:#888">The sync control's chevron menu on a branch with no upstream yet.</figcaption>
</figure>

**SSH keys that ask for a PIN or passphrase.** On macOS and Linux, a fetch you start yourself, such as **Fetch** or **Refresh branches**, can ask for your key's PIN or passphrase through your `SSH_ASKPASS` helper. Background fetches never ask. On Windows, Kepler never asks, so use an SSH agent.

### Set or change the upstream

The upstream is the remote branch that **Push** and **Pull** use. To set it, change it or remove it, open **Set upstream** or **Change upstream** from the sync control's menu or from the worktree's **Branch** submenu. **Change upstream** shows the branch it tracks now.

The picker lists every remote branch, and any of them can be the upstream, whatever its name. The branch you track now is marked **Current**. Above the list, **Unset upstream** removes the upstream, and **Publish as {remote}/{branch}…** publishes the branch when no remote has one of the same name.

When you pick a branch, Kepler saves it at once. The picker lists only branches already fetched. To find a branch someone else just pushed, click **Refresh branches**, beside the search field, which fetches from every remote.

<figure style="text-align:center">
  <a href="/wp-content/uploads/upstream-picker-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/upstream-picker-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The sync control's chevron menu on kepler/fix-cart-total, which reads Push with 2 ahead, with Change upstream (origin/kepler/fix-cart-total) open beside it: a Search remote branches field with a Refresh branches button, Unset upstream pinned above the list, the tracked branch first and marked Current and Same name, then origin/docs/style-guide, origin/main and origin/release/2.4.">
  </a>
  <figcaption style="text-align:center; color:#888">Change upstream, from the sync control's menu.</figcaption>
</figure>

### Updating from the base

The Sync view rebases or merges the branch onto its merge target. It works on a copy first, and your branch changes only when you apply the result.

<figure style="text-align:center">
  <a href="/wp-content/uploads/update-view-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/update-view-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The sync view titled Sync kepler/fix-cart-total, from origin/main with Rebase selected in the Rebase and Merge control and Push after update ticked beside it, at Ready to apply: The rebase onto origin/main is ready. Apply updates your branch. Sync sits beside Apply & push, which has no menu.">
  </a>
  <figcaption style="text-align:center; color:#888">The Sync view with Push after update ticked, ready to apply and push.</figcaption>
</figure>

To sync the branch with its merge target, follow these steps:

1. Open the Sync view from the sync control. Kepler picks the detected base. To use another base, choose it from the picker.
2. Choose **Rebase** or **Merge** in the **Sync method** control beside the base. It starts on the repository's default. See [Repository Settings](/kepler/settings-repositories#edit-a-repository).
3. To push the result when you apply it, tick **Push after update** beside the method. It also starts on the repository's setting.
4. Press **Sync**. To abandon a run in progress, press **Stop**. Your branch is not touched, and any earlier result stays available.
5. When the copy reaches **Ready to apply**, apply it:
   - With **Push after update** ticked, the button is **Apply & push**. A branch you never pushed gets **Apply**.
   - Otherwise the main button is **Apply**, with **Apply & push** in its menu when the branch can push.

**Apply** moves your branch to the result, and the view reads **Branch synced**. You can check the branch before you push it. On a branch already on the remote, **Push** is then the main button. On a branch you never pushed, the main button is **Roll back**, with **Push** in its menu. After a rebase, the push replaces the remote's old commits. A push from the Sync view never overwrites work someone else pushed in the meantime.

To undo an applied sync, press **Roll back**. The branch returns to how it was, and the result stays ready to apply again. When the remote holds exactly the applied result, **Roll back & push** also replaces the published branch with the restored one, after you confirm. The push stops if someone else changed the remote branch.

When a push from the Sync view fails, Kepler keeps your local result and says why. If the remote branch moved, press **Sync** to bring in its changes before you push. Otherwise, **Push** stays offered so you can try again.

A result waiting to be applied does not lock the branch. If the branch or its base moves on, or you pick another base or method, the view reads **The last update result is out of date**, and **Sync** prepares a new one. Kepler does not apply a result whose base moved.

<figure style="text-align:center">
  <a href="/wp-content/uploads/update-view-stale-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/update-view-stale-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The sync view for kepler/fix-cart-total, from main with Merge now selected in the Rebase and Merge control, reading The last update result is out of date: The branch, base, or selected method no longer matches this result. Sync before applying a result. Sync is the only action beside the title, next to the close button.">
  </a>
  <figcaption style="text-align:center; color:#888">A sync result that's out of date. Sync prepares a new one.</figcaption>
</figure>

After an applied sync, when the branch or its base moves on, press **Sync** to prepare the next result. A run that fails says why, under **Sync failed**. Press **Sync** to try again.

When syncing would conflict, the sync control reads **Review conflicts**, and the Sync view lists the conflicting files. Pick a file to see its conflicting hunks.

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

- A paid GitKraken plan. On the Community plan, the button shows a padlock.
- **AI Sync** turned on in **Settings → Agents → Agent tools**.
- A GitKraken sign-in.

To resolve conflicts with AI, follow these steps:

1. Open the Sync view from **Review conflicts** on the sync control.
2. Check the base under the title. To use another base, choose it from the picker.
3. Choose **Rebase** or **Merge** in the **Sync method** control, then press **Sync**.
4. Wait while the progress line counts the files resolved. To abandon the run, press **Stop**.
5. When the run reaches **Ready to apply**, read the review. See [Read the AI review](#read-the-ai-review).
6. Press **Apply**, or **Apply & push** to push too, as in [Updating from the base](#updating-from-the-base). To leave the result unapplied, close the view; your branch stays as it was.

If the AI cannot finish some files, such as a binary file, the run stops without changing your branch and lists each file with the reason. You resolve those files by hand.

#### Read the AI review

The review explains what the AI changed so you can decide whether to apply it. It contains the following parts:

- **A verdict badge**: **No issues found**, **Needs review** or **Blocked**.
- **A summary**: a short explanation of the run, with any files worth checking and why, and the overall confidence.
- **A card for each commit**: the commit's short SHA and subject, or **Merge** for a merge run, and its file count.
- **A row for each file**: the method used, a confidence badge and the AI's reasoning. A low confidence shows as a warning, and a file the AI did not finish is marked **Incomplete**.

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

Click a file row to review that file in full: each conflict at its line, marked **Kept {branch}** or **Merged**, with its own confidence and the AI's reason. **Conflict layout** sets how each conflict reads:

- **Conflict | Result**: the conflict with Git's markers for both branches and the common ancestor, beside the result.
- **Branches + ancestor**: both branches and the **Common ancestor** side by side, then the result.

To see more of the file around a conflict, use **Show {count} more lines above** and **below**, or **Show all lines**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/sync-ai-file-review-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/sync-ai-file-review-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The AI review of cart.js after a rebase onto main: commit 97c56d7 Apply the discount before tax, the AI method, a 75% badge and the AI's reasoning, with Conflict layout set to Conflict | Result beside Branches + ancestor. Below, Conflict 1 of 1 at Line 3 is marked Merged at 75% with the AI's reason, Main extracted roundCents; the branch reordered the discount. Combined both. The Conflict pane shows git's markers for main, the common ancestor and kepler/fix-cart-total, and the Result pane the merged code.">
  </a>
  <figcaption style="text-align:center; color:#888">One file's AI review, conflict by conflict.</figcaption>
</figure>

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
| Compare against another branch for now | Click **from {branch}** in the overlay's header, or in the changes panel on **All changes**, and pick a branch. Nothing is saved |
| Keep that comparison | Click **Save as merge target** beside the branch you picked (**Save** in a narrow panel). Only remote branches can be saved |
| Change it | Choose **Change merge target…** from the merge target chip on the Dashboard, or from the worktree's **Branch** submenu, which shows the current target beside it. The picker lists remote branches only, and choosing one saves it |
| Go back to the detected one | **Reset to automatic ({ref})** in the picker |
| Find a branch someone else just pushed | **Refresh branches**, beside the picker's search field, fetches from every remote. The pickers list only branches already fetched |
| Update the branch from its merge target | **Rebase onto {target}** or **Merge {target} into this branch** from the merge target chip's menu on the Dashboard, or from the worktree's **Branch** submenu. Both open the [Sync view](#updating-from-the-base) with that method chosen |
| See what landed on the merge target | **See what's new on {target}** from the merge target chip's menu on the Dashboard, while the merge target is ahead. See [What's new on the merge target](#whats-new-on-the-merge-target) |

<figure style="text-align:center">
  <a href="/wp-content/uploads/save-merge-target-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/save-merge-target-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The worktree column for kepler/fix-cart-total on its Changes view, with All changes selected over the branch's three commits (Cover discounted orders in tests, Clamp the discount at the subtotal, Apply the discount before tax) and origin/release/2.4 marked branched here. The files toolbar compares from origin/release/2.4, picked for this view only, with a Save as merge target button beside the picker, above cart.js and cart.test.js.">
  </a>
  <figcaption style="text-align:center; color:#888">A branch picked for this view only, with Save as merge target beside it.</figcaption>
</figure>

Kepler and GitLens share a branch's merge target, so a change you make in GitLens shows up in Kepler while it is running.

A branch that landed in its merge target without a pull request counts as merged. That includes rebase-merged and squash-merged branches, which Git itself does not see as merged; Kepler checks their content. The Dashboard says **Merged into {target}**.

### What's new on the merge target

Before you update a branch, check what landed on its merge target since you branched. In the Changes overlay's header, the chip beside **from {branch}** reads **{count} new** when the merge target has new commits, or **Up to date**. Click it for a summary of the new commits and the files that overlap or conflict with yours, with these actions:

- **Compare on {provider}** opens your host's compare page.
- **Rebase** opens the [Sync view](#updating-from-the-base) set to rebase.
- **Review changes** shows what landed in the overlay.

<figure style="text-align:center">
  <a href="/wp-content/uploads/changes-incoming-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/changes-incoming-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Changes overlay reviewing what is new on main for kepler/fix-cart-total. The header reads from where you branched, 2 new on main (pressed, with a close button) and Rebase onto main. On the left, the Overlaps 1 | All 2 switch; All new commits (2 commits) leads the list, then Use the 8.25% sales tax rate (8b89205, 1 file overlaps) and Mention gift cards in the README (2260509), over the changed files cart.js, marked as an overlap, and README.md. The viewer shows cart.js read-only, its tax rate changed from 0.08 to 0.0825.">
  </a>
  <figcaption style="text-align:center; color:#888">Reviewing what landed on the merge target, with the file you also changed marked.</figcaption>
</figure>

While you review, the list shows each pull request or commit that landed, with how many of its files overlap or conflict with yours. **Files to show** narrows the files to **Conflicts**, **Overlaps** or **All**, and **Rebase onto {target}** sits in the header.

The files show as they are on the merge target, so you cannot edit or comment on them here. To go back to your own changes, click the **X** on the chip or press **Escape**.

***

## Where else changes show up

The Dashboard's task preview shows each worktree as a two-row **worktree button**:

- The top row: the branch and repository, its menu, the pull request, and the sync control.
- The bottom row: chips for the uncommitted files, the commits and the merge target, with **Open in** and **Run** beside them. Each chip has a hover card that says what a click does, and a right-click menu of its own.
- A task with several worktrees shows one worktree button at a time, with **Show all {count} worktrees** on its leading edge. The branch name switches between them, and **Auto-switch to active worktree** lets it follow whichever worktree is busiest.

Click the uncommitted or commits chip to open that worktree's changes panel, showing those changes, in a side pane of the task panel, without going to the task page first. Its files open the same Changes overlay. Click the chip again to close the pane, or press **Cmd/Ctrl+Shift+G** to show or hide it. See [The Kepler Interface](/kepler/kepler-interface).

A file or folder in a worktree opens in the Changes overlay too, wherever you open it by its path, such as a file path in a terminal or **Open in Changes** on an attached file's tab. On the task page, only the task's attached files and folders open as tabs; any other file in a worktree opens here. A file opens in **File** view, at its line: on **Working changes** when it has uncommitted changes, and on **Files** otherwise. A folder opens on **Files**, with its changed files stacked.

### Update many worktrees at once

To bring several worktrees and local branches up to date with their bases in one pass, use **Update** in **Settings → Repositories → Worktrees and branches**. The **Update worktrees** panel checks each one and lists what it will update and what it skips, such as a worktree with uncommitted changes, one where an agent is working, or a branch already checked out in a worktree. A local branch with no worktree is updated in place, without being checked out.

Keep each repository's default way to update and push, or choose another for this update. **Push + Publish** also publishes branches that have no remote branch yet. Nothing changes until you press **Update**, and **Roll back** undoes a worktree's update. See [Settings](/kepler/settings-repositories#update-worktrees).

***

## Opening a pull request

**Kepler does not have a button that creates a pull request.** You open the pull request outside Kepler: the agent opens it, you run a command in the worktree's terminal, or you use your host's website. Once the pull request exists, Kepler tracks it as a task resource. A pull request gets attached to the task in one of 3 ways:

| Path | What happens |
|---|---|
| **The agent publishes it** | When an agent publishes a pull request on one of the worktree's remotes, Kepler attaches it to the task. You do not need to do anything |
| **The agent attaches it** | Agents can attach links to the task, or detach them, themselves, including a link you attached. Kepler shows each one as a pull request, an issue, or a plain link, with its title and status where it can |
| **You attach an existing one** | **Manage resources**, at the bottom of the task's context panel, opens the **Resources** screen. On its **Pull requests** tab, click **Add pull requests**, then **Add** on a result |

Only the task's own pull request is attached, not every link the agent reads along the way. Anything the agent attaches shows up in the task right away.

Attaching a pull request also unlocks the **Address Feedback** Action on that task. See [Actions](/kepler/actions) and [Pull Request Integrations](/kepler/pull-request-integrations).

***

## Agent tools: AI Sync and AI Compose

AI Sync and AI Compose give agents Git tools they do not otherwise have. Both are off until you turn them on, and both need a **paid GitKraken subscription**. Turn them on in **Settings → Agents → Agent tools**. With a tool turned on, the agents in your sessions gain the matching tools, and you ask for the work in the chat. AI Sync also powers the Sync view's **Sync** button when the branch has conflicts. See [Resolve update conflicts with AI](#resolve-update-conflicts-with-ai).

| Tool | How an agent uses it |
|---|---|
| **AI Sync** | Rebases or merges the branch onto its base and resolves conflicts, with a result you can read before it applies, and every run backed up. It can push the result, and follows the repository's update and push settings unless you ask otherwise |
| **AI Compose** | Plans the new commits for you to read before it applies them, can split a branch into a stack, and can undo what it applied |

When you ask for a sync, tell the agent what matters, such as which side is authoritative, and it uses that when it resolves conflicts.

A running session keeps the tools it started with. To use a tool you just turned on, start a new session.

Both sets of tools work on the session's own worktree by default. Each can also name another worktree attached to the same task, so one session can clean up a branch it is not working in.

On the Community plan, both rows still appear, with a padlock. Everything else on this page works on the Community plan, except AI conflict resolution.

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
- [Settings](/kepler/settings): [**Diff layout**](/kepler/settings-app#code), [**Agent tools**](/kepler/settings-agents#agent-tools), and [**Worktrees and branches**](/kepler/settings-repositories#worktrees-and-branches)

---
