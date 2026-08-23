---
title: Review Changes
description: An agent finished. Read the diff, stage and commit the parts you want, push the branch, and hand the rest to AI Sync or Compose.
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
last_verified: 2026-08
llms_include: true
tags: [review, diff, working-changes, staging, commits, push, pull-requests, ai-sync, compose]
taxonomy:
  category: kepler
---
<kbd>Last updated: August 2026</kbd>

An agent has stopped and says it is done. Now you read what it actually did, keep the parts that are right, and get them onto a branch.

All of that happens in the task's **worktree**: the Git working copy the agent made its changes in. The task view rail groups a task's worktrees under **Changes**: that's where you go to review them. Open one from that group, and it opens in a column of its own. See [the task view](/kepler/task-view).

<!-- TODO(screenshot): a task's worktree column — commit graph and working changes on the left, a file diff on the right. -->

***

## The worktree view

The worktree opens as two panes: the commit graph and working changes on the left, and a diff on the right once you pick a file.

The header shows the branch, the repository, and how far the branch is ahead of or behind its remote, as **↑n** and **↓n**. It also carries three controls, ordered by how far each takes you from the pane:

- The worktree's configured commands.
- **Open in**, for handing the checkout to another app.
- **Terminal**, for a plain shell.

A command you run opens its terminal as a tab in this same column.

The left pane is a single list, newest first:

| Row | What it is |
|---|---|
| **Working changes** | Everything uncommitted. Selected by default |
| One row per commit | The commit message, its branch and tag decorations, and how long ago it landed |
| **common ancestor** | Where your branch and its upstream diverged, when they have |

When the branch has diverged from its upstream, the graph draws both lanes so you can see the split. Kepler tints branch chips to their lane: a monitor glyph marks a local branch, and a cloud glyph marks a remote one. Tags render as **#name** pills.

Selecting a commit swaps the pane below the graph from working changes to that commit's detail. **×** returns you to working changes.

***

## Working changes: staged and unstaged

Selecting **Working changes** lists what is uncommitted, in up to two sections with counts.

| Section | What it holds |
|---|---|
| **Staged (N)** | Files that will go into the next commit |
| **Changes (N)** | Modified and untracked files that will not |

With nothing uncommitted, the pane reads **No changes to display**.

Each row shows the file path and a one-letter change indicator. Hover a row for its own actions.

| Indicator | Meaning |
|---|---|
| **A** | Added |
| **M** | Modified |
| **D** | Deleted |
| **R** | Renamed |
| **C** | Copied |
| **?** | Untracked: not in Git yet |

| Control | Where | What it does |
|---|---|---|
| **+** | A row in **Changes** | Stages that file |
| **−** | A row in **Staged** | Unstages that file |
| Trash | Any row | Discards that file's changes |
| **Stage All** / **Unstage All** | Section header | Moves the whole section |
| **Discard All** | Section header | Discards the whole section |

Discarding always asks first: **Discard changes?**, naming the file (or the number of files) and warning that discarding cannot be undone. Staging never asks, because staging is reversible.

Right-click a file row for:

- **Copy path**.
- **Open containing folder**, where this window can reach the file manager.
- **Open file on remote**, on rows that belong to a commit.

***

## Reading the diff

Click any file (in working changes or in a commit) to open its diff in the pane on the right.

- The **file path** heads the diff, with its **+/−** line stats.
- Added lines are green, removed lines red.
- **Unmodified regions are collapsed**, leaving three lines of context around each change.
- **↑** and **↓** move to the previous and next file in the same set, so you can read a whole change without going back to the list. They are ignored while you are typing in a field.
- Pick another file to replace what is in the pane. The pane also clears itself when the file you are looking at stops existing: committed, discarded, or gone.

### Stacked or split

**Stacked** puts removals and additions in one column; **Split** puts the old and new file side by side.

The layout comes from **Settings → Appearance → Diff View**, which defaults to **Stacked**, and that setting is the only control. The diff pane here has no header of its own (the file path already heads the diff body), so there is no per-diff **Stacked** / **Split** toggle to reach for.

Split needs room for two columns of code. Below roughly 640 pixels of pane width the diff falls back to Stacked whatever the setting says, rather than truncating both sides into noise.

### Diffs that are not code

Some diffs render differently:

| Case | What you see |
|---|---|
| Images and SVGs | **Before** and **After** previews, each with its size on disk |
| A new file | The whole file, syntax-highlighted, rather than an all-additions diff |
| Over 3,000 changed lines | **Large diff: N changed lines.** Rendering may freeze the window, so Kepler waits for **Show diff** |

Diffs normalize line endings, so a file that changed from CRLF to LF does not read as a rewrite.

***

## Commit history and commit detail

Select a commit in the graph to see everything about it:

| Part | What it shows |
|---|---|
| Title | The commit's subject line |
| Description | The rest of the message, clamped with **Show more** / **Show less** when it runs long |
| Author | Name, email, and initials |
| Timestamp | How long ago the commit landed |
| Hash | The short hash in the header, the full hash below it, with a copy button |
| Branch and tag decorations | Branches in green, tags in amber |
| **Files changed (N)** | Every file, with **+** and **−** totals for the commit and per-file `+/−` stats and change indicator |

Click a file in that list to see its diff **as of that commit**.

Right-click a commit row in the graph for **Copy SHA** and **Copy message**, plus **Open commit on remote** and **Copy commit URL** once the commit exists on a supported host.

***

## Commit

The commit box sits below the file list, and appears once something is staged.

1. Stage what belongs in this commit.
2. Write the message in the **Commit message...** box.
3. Click **Commit**.

**Commit** stays disabled until the message has content. On a repository configured to sign commits, a signing failure keeps your draft message in the box; Kepler explains the failure in a banner instead of discarding what you typed.

> Signing does not work over a remote connection. See [Remote Environments](/kepler/remote-environments).

***

## Push, pull, and fetch

The three buttons above the graph act on this worktree's branch:

| Button | What it does | When it is unavailable |
|---|---|---|
| **Push** | Pushes the branch to its remote | — |
| **Pull** | Pulls from the upstream | With no upstream — *No upstream configured. Publish this branch to enable Pull.* — or on a detached HEAD — *Pull is unavailable while HEAD is detached.* |
| **Fetch** | Updates your remote-tracking refs | — |

**Push** tries first and asks only when it has to:

- **No upstream yet** opens **Publish branch** — *What remote/branch should "name" push to and pull from?* — where you pick the **Remote** and the **Remote branch name**.
- **A diverged branch** opens **Force push required**, which names how far ahead and behind you are and pushes with `--force-with-lease` only if you confirm. It rewrites the remote branch history, so it is a deliberate click.

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

<!-- TODO(screenshot): Settings → Agents → Features, with AI Sync and Compose. -->

***

## Related

- [The Task View](/kepler/task-view) — the rail, the columns, and where the worktree opens
- [Tasks and Resources](/kepler/tasks-and-resources) — worktrees, and detaching or deleting one safely
- [Agent Sessions](/kepler/agent-sessions) — directing the agent that produced these changes
- [Actions](/kepler/actions) — **Review** on a task reviews exactly this uncommitted work
- [Settings](/kepler/settings) — **Diff View**, and the **Features** section

---
