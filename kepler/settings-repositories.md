---
title: Repository Settings
description: The Repositories page of Kepler's Settings, covering the repositories folder, adding and editing repositories, per-repository branch prefixes and commands, cleaning up and updating worktrees and branches, and Projects.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, bitbucket-data-center, azure-devops, azure-devops-server]
integrations: []
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [settings, repositories, worktrees, branches, per-repository-commands, projects, aliases]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

The Repositories page has four sections: **Repositories folder**, **Your repos and folders**, **Worktrees and branches**, and **Projects**.

## Repositories folder

The following setting tells Kepler where to clone repositories:

| Setting | What it controls | Default |
|---|---|---|
| **Repositories folder** | *Kepler adds the repos it finds in this folder. It only looks when you change the folder or scan, so a repo you remove won't come back.* | `~/kepler/repositories` |

**Scan for repositories**, beside the field, registers every repository it finds there. It reports **Added {count} repositories.** or **No new repositories found.** in a notification. It runs only when you change the setting or press it, never on startup, so a repository you deliberately removed stays removed.

A scan that added repositories offers **Undo**, which removes them again. Undo keeps any repository you've started using or changed since the scan, and says which: *Kept {names}. You've used or changed them since the scan.* If nothing before a variable in the setting is a full folder path, the scan has nowhere to look and says so: *There is no folder to scan: nothing before the dynamic variable in this setting is a full folder path. Point it at one first.*

If the folder doesn't exist yet, the field says Kepler creates it when you clone. The field takes the `<REPOSITORY_NAME>` variable. See [The Variables menu](/kepler/settings-tasks#the-variables-menu).

## Your repos and folders

This section lists every repository Kepler tracks and every folder you've attached to a task. Each row shows its name, its path on disk, and how many commands it has: **No commands**, **1 command**, or a count. The following table lists the section's controls:

| Control | What it does |
|---|---|
| **Filter repos and folders** | Narrows the list by name |
| **Row** | Click it to open the repository's **Edit repo** page, or the folder's page |
| **Add repo** | Opens the **Add repo** page. See below |
| **Add folder…** | Adds a plain folder |
| **Trash icon** | Untracks the repository or folder. The folder on disk is left untouched |

With nothing tracked, the section reads *Add a repository or folder to manage it here.*

### Add a repository

**Add repo** opens a sub-page. You give a source, Kepler inspects it, and what it found becomes a card you can edit before you add it:

| Field | What it takes |
|---|---|
| **Folder or URL** | *Paste a URL to clone it, or pick a folder that already holds a repo.* You can also drop a folder onto the page, or **Create a new repo instead** |
| The card | The resolved repository (**{name} on {provider}**, its path, its branch count), plus the name, description, and branch prefix you can edit |

Kepler says what a source resolves to before you commit to it. For example, it reads **A new folder named {name} will be created here.**, *This folder already holds a clone of that repo. It will be added as is.*, or **This repo is already in Kepler.** A path that isn't a Git repository reads **That folder isn't a Git repo.**

While a clone runs, the page reads *Cloning {name} into {folder}* and *You can leave this page. Kepler tells you when the clone finishes.* Leaving doesn't stop the clone. If it fails later, a notification names the repository: *Unable to clone {name}: {reason}*.

### Edit a repository

Click a repository's row to open its **Edit repo** page. The page shows the repository's path, its remote, and its branches, and has these parts:

| Part | What it holds |
|---|---|
| **Name** | The name Kepler shows wherever it names this repository. The field's placeholder is the folder name. Leave it empty to use the folder name. A repository you name this way keeps that name verbatim and stops competing with same-named folders for a disambiguating suffix |
| **Aliases** | *Short names for this repo when talking to agents, separated by commas.* An agent can name the repository by an alias wherever Kepler's workspace tools take a repository, and finds it by alias when it lists your repositories. An alias can't contain a colon or repeat another repository's alias or name |
| **Description** | Free text. Its placeholder reads *What this repo is for. Agents working in it read this.* Kepler appends it to the repository's line in the resource list it hands a session, so a full sentence is more useful here than a single label |
| **Branch prefix** | Overrides the prefix from **Settings → Tasks** for this repository alone. See below |
| **Commands** | Shell commands for this repository. See [Per-repository commands](#per-repository-commands) |
| **MCP servers** | *Extra tools your agents get in this repo, on top of their own lists. Changes here apply right away.* See [MCP Servers](/kepler/mcp-servers) |

**Name**, **Aliases**, and **Description** are optional. Kepler stores whitespace-only text as empty. The page has no **Save** button: each field saves on its own and shows its save status.

<figure style="text-align:center">
  <a href="/wp-content/uploads/edit-repo-dialog-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/edit-repo-dialog-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Edit repo page for acme-web in Settings › Repositories: its path and main · 2 branches, then Name, Aliases (empty, Short names for this repo when talking to agents, separated by commas), Description and Branch prefix on Default (kepler/) with the example kepler/fix-login-form; the Commands section with Add command, Install deps (Runs on creation) and Dev server; and MCP servers with Add server, Agent set to Claude Code CLI and acme-issues, docs-search and acme-analytics switched on.">
  </a>
  <figcaption style="text-align:center; color:#888">The Edit repo page.</figcaption>
</figure>

#### Branch prefix, per repository

The **Branch prefix** control has three options:

| Option | What it does |
|---|---|
| **Default ({value})** | Uses the prefix from **Settings → Tasks** |
| **None** | Creates task branches with no prefix |
| **Custom** | A prefix for this repository only |

**New task branches will look like** shows an example, so you can see what you're choosing before a branch exists.

**Default** and **None** save the moment you pick them. **Custom** saves its text when you press **Enter** or **Escape**, or leave the field. If the repository already has a local branch named like the prefix, Kepler refuses it rather than saving it: *Can't create {prefix} branches here: this repo already has a branch named {branch}. Rename that branch or choose another prefix.*

Removing a repository deletes its sessions, terminals, and configured commands, and terminates any live agent and terminal sessions tied to it. Kepler confirms before it does.

### Per-repository commands

*Run your dev server, tests or build from a task's worktree in one click. A command can also run when Kepler creates a new worktree, like installing dependencies.* Commands are shell commands scoped to one repository.

To add a command, click **Add command** in the **Commands** section of the Edit repo page. With no commands, the section reads *No commands yet.* and suggests examples. Each command saves on its own: an open row has its own **Cancel** and a primary button, **Add command** for a new row or **Save** for a stored one. **Enter** in the name field, or **⌘ Enter** (**Ctrl + Enter** on Windows and Linux), also saves the row. Each command row has three fields:

| Field | What it does |
|---|---|
| Name | A label, for example *Install deps*. It's what you pick from the **Run** menu later |
| Command | The shell command, for example `pnpm install`. Its **Variables** menu inserts any of the variables below |
| **Run on worktree creation** | Runs this command automatically when Kepler creates a worktree for this repository. Off by default, which leaves it a command you run on demand. A row with it on shows a **Runs on creation** chip |

Commands accept four variables, which Kepler fills in when the command runs:

| Variable | Resolves to |
|---|---|
| `<REPOSITORY_PATH>` | Main repo folder |
| `<REPOSITORY_NAME>` | Repo name |
| `<SOURCE_PATH>` | Where files come from (the main repo, or the source worktree when forking) |
| `<WORKTREE_PATH>` | The new worktree folder |

Drag a row by its handle to reorder it, or move it from the keyboard with **Alt + ↑** and **Alt + ↓**. A new order saves at once. Order sets the **Run** menu order and the order that commands set to run on worktree creation run in.

A row missing its name or its command can't be saved: Kepler opens it on the missing field, with *Add a name to show in the Run menu.* or *Add the command to run.* **Cancel** discards a row you opened by accident. A closed row that isn't saved yet shows a **Not saved** chip. **Remove command** deletes a saved command at once, with a *Deleted command {name}* notification that offers **Undo**.

Commands flagged to run on worktree creation execute sequentially, in list order, and stop on the first failing command. Kepler skips the rest and reports them as skipped. Each one runs in the new worktree's folder through your login shell, so you don't need to `cd` into it, and tools configured in your shell profile (`nvm`, for instance) are available. Each has a ten-minute timeout.

A failed command does not undo the worktree. The worktree exists but may not be usable. To fix it:

1. Read the command output in the task.
2. Correct the command here.
3. Run it again from the **Run** menu.

To run a command from the task view, right-click a worktree row in the rail and use **Run command here**. It lists that repository's commands and runs the one you pick in that worktree, opening its terminal in place. A repository with none yet reads **No commands yet** and offers **Create command…**, which opens this page and returns you to the task when you leave it. A command that's running shows on the run button and its menus, where you can stop it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/repo-commands-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/repo-commands-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Commands section of the Edit repo page for acme-web: Add command, Install deps (pnpm install) with the Runs on creation chip, and Dev server open for editing with its name, Run on worktree creation, the command pnpm dev with Variables, and Cancel and Save, above the note that commands run in the worktree folder with your login shell.">
  </a>
  <figcaption style="text-align:center; color:#888">A repository's Commands, with one row open for editing.</figcaption>
</figure>

## Worktrees and branches

*Update, clean up and delete worktrees and local branches across your repositories.* On the Repositories page, this section is one row, **Manage worktrees and branches**. Click it to open the **Worktrees and branches** sub-page.

*See which worktrees and local branches of your repositories are stale, update the ones that can be brought up to date, and delete what is done.* The sub-page reads your repositories as soon as it opens, and deletes nothing on its own. It lists every worktree, and every local branch that no worktree holds, grouped by repository. A summary such as *{worktrees} and {branches} in {repos}.* says how many look safe to delete. A branch with no worktree reads **Not checked out** where a worktree shows its path. The base branch carries a **Base** badge and is never deleted.

The following table lists the sub-page's controls:

| Control | What it does |
|---|---|
| **Search branch, path or repo** | Narrows the list. Every word you type must match the branch, the path, or the repository name |
| **Show worktrees and branches** | Filters by status: **Safe to delete ({count})**, **Needs update ({count})**, **Conflicts ({count})**, **Stale ({count})**, or **All ({count})**. A count reads *checking…* until Kepler has compared each branch with its base |
| **Show worktrees, branches or both** | **All**, **Worktrees only**, or **Branches only** |
| **Stale after** *n* **days** | How many days without activity before a worktree or branch counts as stale. Defaults to 14 |
| **Re-check** | Fetches every repository's remotes, then inspects the list again. A repository whose fetch failed says so beside its name: *Unable to fetch: {reason}; numbers may be stale* |
| **Select all safe to delete** / **Select all that need an update** / **Select all with conflicts** / **Select all stale** / **Select all** | Selects the rows in the current view |
| Selection bar | Reads *{count} selected*, or *{count} selected · {hidden} hidden by filters*, with **Clear**, **Update**, and **Delete**. **Update** and **Delete** act only on the selected rows you can see |

Each row shows how it stands with its upstream: commits to push (↑) and pull (↓), **No upstream**, or **Upstream gone**. Badges then compare it with its base: **{count} behind {base}**, **Conflicts with {base}**, or **Up to date with {base}**, plus how many files are uncommitted. A row also says how long since it was touched and why it may be finished, such as being merged into its base. On the right, it shows the tasks using it, an **External** count for sessions started outside Kepler, and its pull request. A branch row shows the tasks, sessions, and pull requests tied to that branch.

A row counts as one or more of the following:

- **Safe to delete**: *Its work has landed: merged into the base or its pull request merged (a branch whose upstream is gone and whose pull request was closed counts too), and nothing is uncommitted, unpushed or in use.*
- **Needs update**: behind the base branch with no known conflict, so an update can bring it up to date.
- **Conflicts**: behind the base branch, and merging the base in would conflict, so you have to update it by hand.
- **Stale**: no activity for longer than the stale threshold, but nothing proves the work landed. It may still hold uncommitted or unpushed work, so deleting it can lose something.

**Needs update** and **Conflicts** leave out rows that are safe to delete. Activity includes what Kepler recorded on the branch, not only changes in the worktree.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-worktree-cleanup-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-worktree-cleanup-01-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Repositories › Worktrees and branches: 4 worktrees and 2 branches in 1 repo, 3 look safe to delete, with Stale after 14 days and Re-check; Search branch, path or repo, the Safe to delete (3), Needs update, Conflicts, Stale and All filters, and All / Worktrees only / Branches only. Under acme-web, kepler/old-banner and kepler/promo-page (worktrees tagged Spring sale banner) and kepler/summer-teaser (Not checked out) are each 3 behind main and merged into main; old-banner and summer-teaser are ticked, and the bar reads 2 selected with Clear, Update and Delete.">
  </a>
  <figcaption style="text-align:center; color:#888">The Worktrees and branches sub-page, filtered to what is safe to delete.</figcaption>
</figure>

### Delete worktrees and branches

Select rows, then click **Delete**. The confirmation, **Delete {count} items?**, says what is lost:

- For worktrees: *The directories are removed from disk. Anything listed below is lost with them.* **Also delete the branches** deletes each worktree's branch too.
- For local branches: *The local branches are deleted. Commits that exist only on them are lost.* When every branch's work has landed, it reads *Their work is already in the base branch, so nothing is lost.* instead. Each branch that isn't merged is marked **not merged**. **Force delete branches that are not merged** deletes those too, and **Also delete the branches on the remote** deletes the remote branches.

<figure style="text-align:center">
  <a href="/wp-content/uploads/worktree-branch-delete-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/worktree-branch-delete-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Delete 2 items? dialog for two local branches: The local branches are deleted, with Force delete branches that are not merged and Also delete the branches on the remote unticked, kepler/size-guide marked not merged, and Cancel and Delete 2 items.">
  </a>
  <figcaption style="text-align:center; color:#888">Deleting two local branches, one of them not merged.</figcaption>
</figure>

Kepler keeps any branch it can't delete safely and says why, for example *Checked out in {path}. Remove that worktree first.* or *Its work is not in the base branch, so it was kept.*

A lock Kepler itself left on a worktree, for a task this install knows or a task since deleted, is cleared and the worktree deleted. Kepler never deletes a repository's main checkout. It keeps any worktree that still has uncommitted or unpushed work, other tasks, running agent sessions, or a lock from another tool, and says why for each. Where forcing can help, the result offers **Force delete**, which discards the listed work and ends the agent sessions running there.

### Update worktrees

To bring several worktrees and local branches up to date with their base branch at once:

1. On the Worktrees and branches sub-page, select the worktrees and branches.
2. Click **Update**. The **Update worktrees** dialog opens: *Each branch is brought up to date with its base. Nothing changes until Update is pressed.*
3. Review the plan. Each row reads **Will update** with how many commits it's behind, **Up to date**, or **Skipped** with the reason, such as *an agent is working in it*, *uncommitted changes*, *checked out in a worktree*, *would conflict*, or *a sync result is waiting for review*.
4. Under **How to update**, choose **Rebase** or **Merge**.
5. To push each updated branch too, tick **Push after update**. Each row that will update then reads **Will push**, or **No upstream, update only** for a branch with no upstream.
6. Click **Update**.

Kepler updates a local branch that has no worktree in place, from the repository's main checkout, without checking it out. It skips such a branch when a worktree holds it, or when the main checkout has uncommitted changes. If an update was prepared but couldn't be applied on its own, Kepler keeps it for you to review instead of discarding it.

While the update runs, each row shows its status: **Waiting**, **Updating…**, **Updated**, **Up to date**, **Skipped**, **Conflict**, or **Failed**. When it finishes, you can undo one row with **Roll back**, or every row with **Roll back all**. If you didn't push during the update, **Push** and **Push all** push the updated branches that have an upstream. A branch that moved since the update isn't pushed. The finished report stays in every window until you click **Dismiss**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-worktree-batch-update-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-worktree-batch-update-01-v3@2x.png" class="help-center-img img-bordered" alt="The Update worktrees dialog with How to update set to Rebase and Push after update ticked: kepler/gift-card-ui is Up to date, kepler/old-banner Will update · 3 commits behind with No upstream, update only, kepler/wishlist is Skipped · uncommitted changes, and kepler/summer-teaser Will update · 3 commits behind with Will push. The footer reads 2 worktrees to update beside Cancel and Update.">
  </a>
  <figcaption style="text-align:center; color:#888">The Update worktrees plan, with Push after update ticked.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-worktree-batch-update-02-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-worktree-batch-update-02-v3@2x.png" class="help-center-img img-bordered" alt="The finished update on the Worktrees and branches page: Update finished, 2 updated · 1 pushed, with Roll back all and Dismiss; kepler/old-banner reads Not pushed: no upstream and Updated, kepler/summer-teaser Pushed and Updated, each with Roll back.">
  </a>
  <figcaption style="text-align:center; color:#888">The finished update, with Roll back on each row.</figcaption>
</figure>

## Projects

*Group repos that belong together under one name.* A **Project** groups repositories so they act as a unit, such as a frontend and a backend you change together. The following table lists the section's controls:

| Control | What it does |
|---|---|
| **Row** | Shows the project's name and its repository count. Click it to open the project's page |
| **New project** | Opens a page where you name a project and pick its repositories. **Add from folder** adds a repository without leaving the page |

A new project shows **Create** and **Cancel**, and **Create** refuses a blank name: *Give the project a name.* Once the project exists, its page has no **Save** button: its name saves as you edit it, and each repository you tick or untick saves at once. A folder's page saves its name and description the same way. A project's page also has **Delete project**. Deleting a project keeps its repositories in your repository list. With no projects, the section reads *No projects yet.*

***

---
