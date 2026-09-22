---
title: Review Changes
description: An agent finished. Read the diff in the Changes overlay, publish or sync the branch, and hand the rest to AI Sync or Compose.
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
last_verified: 2026-09
llms_include: true
tags: [review, diff, changes-overlay, working-changes, commits, push, pull-requests, ai-sync, compose]
taxonomy:
  category: kepler
---
<kbd>Last updated: September 2026</kbd>

An agent has stopped and says it is done. Now you read what it actually did.

All of that happens in the task's **worktree**: the Git working copy the agent made its changes in. The task view rail groups a task's worktrees under **Changes**: that's where you go to review them. See [the task view](/kepler/task-view).

Reading a diff has two surfaces, and they answer different questions:

| Surface | What it is for |
|---|---|
| **The worktree tab's changes panel** | The table of contents: which scope, how much changed, and the list of files |
| **The Changes overlay** | The reading surface: a full-window diff, one file or many, with the file tree beside it |

Every file in the panel leads into the overlay, opened on exactly the scope the panel was showing.

***

## The worktree tab

Open a worktree from the rail's **Changes** group and it opens in a tab of its own: a strip of verbs across the top, the changes panel below it.

### The strip

| Control | What it does |
|---|---|
| The **branch pill** | The branch this checkout is on. Its chevron opens **Open changes**, **Reveal in file manager**, **Copy branch name**, and **Copy worktree path** |
| The **sync control** | One button whose verb follows the upstream state — **Publish**, **Push**, **Pull** or **Fetch** — with the counts beside it |
| **Open in** | Hands the checkout to another app. The split button runs your default; the chevron lists the rest |
| **Run a command** | The repository's configured commands, and **Manage commands…**. See [Settings](/kepler/settings) |

The strip folds as the column narrows, one control at a time, rather than all at once at a breakpoint: the branch name gives first, then the verbs fold into an overflow, then the sync control follows them — where it gets its counts back, because the popover has the room the row did not.

For a shell in this checkout, use the rail row's **New terminal here**, or **Cmd/Ctrl+J**. Terminals live in the drawer beneath the columns, not on this strip. See [The Task View](/kepler/task-view#the-terminal-drawer).

### The changes panel

The panel is one bar over a list of files.

| Part | What it does |
|---|---|
| **Working changes** / **Commits** | The scope. Each side carries its own count, so you can see where the work actually is before switching |
| **All** / **Select** | On **Commits** only. **All** is every commit this branch adds against its base; **Select** narrows to one commit or a range you pick from the list |
| **Tree** / **Flat list** | How the files are drawn |
| **Changed** / **All** | Whether the tree shows only what changed, or every file in the checkout |
| **Filter files** | Narrows the list. **Cmd/Ctrl+P** focuses it |

The scope is chosen once and then left alone. Kepler won't flip you to **Commits** the moment the last working change is committed, or back to **Working changes** because an agent touched a file — either would move the list under whoever was reading it.

**Changed** / **All** is independent of the scope, so browsing every file in the checkout survives a scope switch.

The header above the commit list says how far the branch has come: **{count} commits ahead of {branch}**, with **branched here** marking the merge base.

***

## The Changes overlay

Click a file, or **Open changes** from the branch pill's menu, and the overlay takes the window.

<div class="note" markdown="1">

**The overlay reads; it does not write.** There is no staging, no commit box, and no inline editing in this release. Committing happens in the worktree's terminal or through the agent. See [Committing](#committing) below.

</div>

### The layout

| Part | What it holds |
|---|---|
| The tree | The same file tree the panel had, over the same scope, with its own scope and layout controls |
| The viewer | The diff, or several diffs stacked when you opened a folder or a selection |

**Hide changes panel** collapses the tree and hands its width to the viewer. With the tree hidden, the scope picker and a **Jump to file…** switcher move onto the viewer's own header, so you never lose the way back.

### Moving around

| Gesture | What it does |
|---|---|
| Click a file | Opens it on its own |
| **Cmd/Ctrl**-click | Adds a file to the set on screen |
| **Shift**-click | Extends the selection to a range |
| Click a folder | Opens every file in it, stacked |
| **Alt+↑** / **Alt+↓** | Previous and next file |
| **Cmd/Ctrl+P** | **Filter files** |
| **Escape** | Closes the overlay |

The header counts what you are reading: **{index} of {total}**, and **{count} files shown** once a filter is narrowing it.

### Reading a diff

- The **file path** heads each diff, with its **+/−** line stats.
- Added lines are green, removed lines red.
- **Unmodified regions are collapsed**, leaving three lines of context around each change.
- **Expand all** and **Collapse all** act on the whole stack; a single diff folds from its own header.
- A file that is unchanged in the current scope is drawn as such — **Unchanged in this scope** — rather than hidden, so an **All files** browse reads the whole checkout.

Right-click a file row for its own menu, including **Open in** with a per-row default toggle, **Copy path**, and **Open on {provider}** where the file exists on a supported host.

### Stacked or split

**Stacked** puts removals and additions in one column; **Split** puts the old and new file side by side. The toggle sits on the viewer's header, and **Settings → Appearance → Diff View** sets what it starts on.

Split needs room for two columns of code. Below roughly 640 pixels of viewer width the diff falls back to Stacked whatever the setting says — the header says **Too narrow for a split diff** rather than truncating both sides into noise.

### Diffs that are not code

| Case | What you see |
|---|---|
| Images and SVGs | **Before** and **After** previews, each with its size on disk |
| A new file | The whole file, syntax-highlighted, rather than an all-additions diff |
| A file with no textual change | **No textual changes to display** |
| Over 3,000 changed lines | **Large diff: N changed lines.** Rendering may freeze the window, so Kepler waits for **Show diff** |

Diffs normalize line endings, so a file that changed from CRLF to LF does not read as a rewrite.

### When a scope can't be read

A failed read says so rather than standing in for an empty one: **Couldn't load these changes**, with **Try again**, and *Git did not say why.* when Git offered no reason. An empty scope reads **No working changes** or **No changes in this scope**; a branch with no base yet reads **No base branch to compare against yet**.

***

## Publishing and syncing the branch

The strip's **sync control** is one button, and its verb is whatever the branch actually needs.

| State | The button reads | What it does |
|---|---|---|
| No upstream | **Publish** — *Push to publish this branch to a remote* | Publishes the branch |
| Ahead | **Push**, with **{count} ahead** | Pushes |
| Behind | **Pull**, with **{count} behind** | Pulls. A branch that is both ahead and behind reads *Behind, pull first* |
| In step | **Fetch**, with **Up to date** | Updates your remote-tracking refs |

Counts only move on a fetch, so the control says when it last looked: **Checked {time}**.

The chevron beside it holds the two things that are never the default:

- **Force push** — *Rewrites the remote branch*. A deliberate, separate click.
- **Sync summary** — a full-height report of how this branch stands against its base, which takes the panel's place while it is open.

***

## Committing

Kepler does not stage or commit in this release. The Changes overlay reads a diff; it does not write one.

That leaves three ways to get work onto a branch, and all three are normal:

| How | When |
|---|---|
| **Ask the agent** | The common case. The agent that wrote the change commits it, and you read the result |
| **The worktree's terminal** | `git add`, `git commit`, your own aliases. **New terminal here** on the worktree's rail row opens one already in the right folder |
| **Compose** | Hand an agent the tools to reorganize messy changes into clean, atomic commits. See below |

Pushing, pulling, publishing and force-pushing all stay in Kepler, on the strip above.

***

## Where else changes show up

The Dashboard's task preview carries a **worktree chip** per checkout, and its changes cell is a summary of the same thing:

- What the branch adds against its base — commits, files, and the line delta — under **Compared to {branch}**.
- **{count} commits changed {files}**, with uncommitted files counted separately, because only one of the two halves can still be lost.
- Clicking it opens the same Changes overlay, without going to the task page first.

See [The Kepler Interface](/kepler/kepler-interface).

***

## Opening a pull request

**Kepler has no "create pull request" button.** You open the pull request outside Kepler: the agent opens it, you run a command in the worktree's terminal, or you use your host's website. Kepler's part starts once the pull request exists: it tracks the pull request as a task resource. Three paths attach one:

| Path | What happens |
|---|---|
| **The agent publishes it** | When an agent publishes a pull request, Kepler reads the result, checks that it belongs to one of the worktree's remotes, and attaches it to the task: no action from you |
| **The agent attaches it** | Agents can attach a link to the task themselves through Kepler's workspace tools. Kepler works out from the URL whether it is a pull request, an issue, or a plain link, and fetches its title and status where it can. Kepler attaches the link even when that lookup fails. The same tools detach one, including a link you attached yourself |
| **You attach an existing one** | **Add resource → Pull requests** in the task view searches your connected hosts. **Add to task** attaches what you pick |

Kepler asks an agent to attach only the pull request the task is actually about, not every URL it reads while investigating. Anything the agent attaches shows up in the task right away.

Attaching a pull request also unlocks the **Address Feedback** Action on that task. See [Actions](/kepler/actions) and [Pull Request Integrations](/kepler/pull-request-integrations).

***

## AI Sync and Compose

AI Sync and Compose are two shipped features that hand agents Git tooling they don't otherwise have. Both are off until you turn them on, and both need a **paid GitKraken subscription**. Enable them in **Settings → Agents → Features**:

| Feature | What it gives agents |
|---|---|
| **AI Sync** | *Gives agents tools to rebase or merge with automatic conflict resolution. Operations are safe and can be easily rolled back.* |
| **Compose** | *Gives agents tools to reorganize messy changes into clean, atomic commits. Operations are safe and can be easily undone.* |

These are agent tools, not buttons in the interface. With one enabled, the agents in your sessions gain the matching tools and you ask for the work in the chat.

| Feature | How an agent uses it |
|---|---|
| **AI Sync** | Runs the rebase or merge, resolving conflicts as it goes, then reports the result for you to accept or roll back. AI Sync backs up every run first. It also drops commits whose changes are already upstream: useful after a squash-merge |
| **Compose** | Plans the reorganization first and applies it as a second step, so you can read the plan before anything moves. It can also split a multi-commit branch into a stack, and undo what it applied |

Turning either one on confirms that **New agent sessions will pick up this change**. A session already running keeps the tools it started with, so start a new session to use them.

Both sets of tools default to the session's own worktree, and both can name another worktree attached to the same task instead, so one session can tidy a branch it is not itself sitting in.

On a Free plan both rows still appear, with a padlock where the checkbox goes and the tooltip *"Not available on the Free plan. Upgrade to unlock."* Everything else on this page works on a free account.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ai-sync-compose-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ai-sync-compose-aug-2026.png" class="help-center-img img-bordered" alt="Settings → Agents → Features, with AI Sync and Compose both enabled">
  </a>
  <figcaption style="text-align:center; color:#888">AI Sync and Compose, in Settings → Agents → Features.</figcaption>
</figure>

***

## Related

- [The Task View](/kepler/task-view) — the rail, the columns, and where the worktree opens
- [Tasks and Resources](/kepler/tasks-and-resources) — worktrees, and detaching or deleting one safely
- [Agent Sessions](/kepler/agent-sessions) — directing the agent that produced these changes
- [Actions](/kepler/actions) — **Review** on a task reviews exactly this uncommitted work
- [Settings](/kepler/settings) — **Diff View**, and the **Features** section

---
