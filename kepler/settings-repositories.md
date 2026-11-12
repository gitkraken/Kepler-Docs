---
title: Repository Settings
description: Choose where Kepler clones repositories, add and edit repositories with their own branch prefixes and commands, update and clean up worktrees and branches, and group repositories into projects.
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
last_verified: 2026-11
llms_include: true
tags: [settings, repositories, worktrees, branches, per-repository-commands, projects, aliases]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Use **Settings → Repositories** to choose where Kepler clones repositories, add and edit the repositories and folders Kepler tracks, update and clean up worktrees and branches, and group repositories into projects.

## Repositories folder

To choose where Kepler clones repositories, use this setting:

| Setting | What it controls | Default |
|---|---|---|
| **Repositories folder** | Where Kepler clones repositories, and where it looks for repositories to add | `~/kepler/repositories` |

To add every repository already in that folder, click **Scan for repositories** beside the field. Kepler scans only when you change the setting or click the button. A scan skips any repository you removed; to bring one back, add it yourself with **Add repo**. Repositories a scan adds start untrusted. See [Trust a repository](#trust-a-repository).

After a scan that added repositories, **Undo** removes them again, except any you have used or changed since the scan. To scan, the setting needs a full folder path before any variable in it.

If the folder does not exist yet, Kepler creates it when you clone. The field takes the `<REPOSITORY_NAME>` variable. See [The Variables menu](/kepler/settings-tasks#the-variables-menu).

## Your repos and folders

**Your repos and folders** lists every repository Kepler tracks and every folder you have attached to a task. Each row shows its name, its path on disk, and how many commands it has. A repository or folder you have not trusted shows an **Untrusted** badge. The section has these controls:

| Control | What it does |
|---|---|
| **Filter repos and folders** | Narrows the list by name |
| A row | Click it to open the repository's **Edit repo** page, or the folder's page |
| **Add repo** | Opens the **Add repo** page. See below |
| **Add folder…** | Adds a plain folder |
| Trash icon | Stops tracking the repository or folder, and leaves the folder on disk |

If a folder you added later becomes a Git repository, for example after `git init`, Kepler treats it as a repository from then on.

Removing a repository deletes its sessions, terminals, and configured commands, and ends any live agent and terminal sessions tied to it. Kepler asks you to confirm first.

### Add a repository

To add a repository, follow these steps:

1. Click **Add repo**.
2. In **Folder or URL**, paste a URL to clone, or pick a folder that already holds a repository. You can also drop a folder onto the page, or click **Create a new repo instead**.
3. Kepler shows what it found as a card, and says what it will do, such as clone into a new folder or add an existing clone as it is. It also tells you when the repository is already in Kepler, or the folder is not a Git repository. Edit the name, description, and branch prefix on the card if you need to.
4. Click **Add repo**, or **Clone** for a URL.

You can leave the page while a clone runs; the clone continues, and a notification tells you when it finishes or why it failed.

### Edit a repository

Click a repository's row to open its **Edit repo** page. The page shows the repository's path, its remote, and its branches. When Kepler knows the remote's host, click the remote's provider line to open the repository there (**Open on {provider}**). The page has these parts:

| Part | What it holds |
|---|---|
| **Name** | How this repo is listed in Kepler. Leave it empty to use the folder name |
| **Aliases** | Short names for this repo when talking to agents, separated by commas, such as `api, backend` |
| **Description** | What this repo is for. Agents working in it read this |
| **Trusted** | Lets Kepler run git in this repo. See [Trust a repository](#trust-a-repository) |
| **Branch prefix** | Overrides the prefix from **Settings → Tasks** for this repository only. See below |
| **Branch synchronization** | How this repo's branches update by default (**Rebase** or **Merge**), and whether to push after an update. See [Update worktrees](#update-worktrees) |
| **Commands** | Shell commands for this repository. See [Per-repository commands](#per-repository-commands) |
| **MCP servers** | Extra tools your agents get in this repo, on top of their own lists. See [MCP Servers](/kepler/mcp-servers) |

**Name**, **Aliases**, and **Description** are optional. The page has no **Save** button: each field saves on its own and shows its save status. Some fields have more rules:

- A repository you name keeps that name exactly.
- An alias cannot contain a colon, or repeat another repository's alias or name.
- Agents working in this repo read the description, so write a full sentence.

<figure style="text-align:center">
  <a href="/wp-content/uploads/edit-repo-dialog-oct-2026-v5@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/edit-repo-dialog-oct-2026-v5@2x.png" class="help-center-img img-bordered" alt="The Edit repo page for acme-web in Settings › Repositories: its path and main · 2 branches, then Name, Aliases (empty, placeholder api, backend) and Description, each with its help line; Trusted switched on (Kepler runs git here, and agent sessions skip the agent's own trust question); Branch prefix on Default (kepler/) with the example kepler/fix-login-form; Branch synchronization with How to update set to Rebase and Push after update unticked; the Commands section with Add command, Install deps (Runs on creation) and Dev server; and MCP servers with Add server, Agent set to Claude Code CLI and acme-issues, docs-search and acme-analytics switched on.">
  </a>
  <figcaption style="text-align:center; color:#888">The Edit repo page.</figcaption>
</figure>

#### Branch prefix, per repository

The **Branch prefix** control has 3 options:

| Option | What it does |
|---|---|
| **Default ({value})** | Uses the prefix from **Settings → Tasks** |
| **None** | Creates task branches with no prefix |
| **Custom** | A prefix for this repository only |

**New task branches will look like** shows an example branch name for your choice.

Kepler does not save a prefix that the repository already uses as a local branch name. Rename that branch, or choose another prefix.

#### Trust a repository

Kepler runs no git in a repository or folder you have not trusted, because a repository's own settings can run programs. Until you trust it, its status, branches, and changes stay empty.

To trust a repository or folder, turn on **Trusted** on its page. You can also click **Trust** where Kepler asks, such as in a task's Changes view. While **Trusted** is on, agent sessions in it also skip the agent's own trust question.

### Per-repository commands

Use commands to run your dev server, tests, or build from a task's worktree in one click. A command can also run when Kepler creates a new worktree, for example to install dependencies. Commands are shell commands for one repository.

To add a command, click **Add command** in the **Commands** section of the Edit repo page. Each command row has 3 fields:

| Field | What it does |
|---|---|
| Name | A label, for example *Install deps*. You pick the command by this name from the **Run** menu |
| Command | The shell command, for example `pnpm install`. Its **Variables** menu inserts any of the variables below |
| **Run on worktree creation** | Runs the command each time Kepler creates a worktree for this repository. Off by default |

To save a row, click **Add command** (or **Save** on a stored command), or press **⌘ Enter** (**Ctrl + Enter** on Windows and Linux). Each command saves on its own.

Commands accept 4 variables, which Kepler fills in when the command runs:

| Variable | Resolves to |
|---|---|
| `<REPOSITORY_PATH>` | Main repo folder |
| `<REPOSITORY_NAME>` | Repo name |
| `<SOURCE_PATH>` | Where files come from (the main repo, or the source worktree when forking) |
| `<WORKTREE_PATH>` | The new worktree folder |

To reorder commands, drag a row by its handle, or move it from the keyboard with **Alt + ↑** and **Alt + ↓**. A new order saves at once. The order sets the order of the **Run** menu, and the order in which commands set to run on worktree creation run.

A row needs both a name and a command before you can save it. A closed row that is not saved yet shows **Not saved**. **Remove command** deletes a saved command, and the notification that follows offers **Undo**.

Commands set to run on worktree creation run one at a time, in list order. If one fails, Kepler skips the rest. Each command runs in the new worktree's folder through your login shell, so tools set up in your shell profile, such as `nvm`, are available. Each command has a 10-minute timeout.

A failed command does not undo the worktree. The worktree exists but may not be usable. To fix it:

1. Read the command output in the task.
2. Correct the command here.
3. Run it again from the **Run** menu.

To run a command from the task view, right-click a worktree row in the task's context panel and use **Run command here**. It lists that repository's commands and runs the one you pick in that worktree, in a terminal. For a repository with no commands yet, **Create command…** opens the Edit repo page. To stop a running command, use the run button or its menu.

<figure style="text-align:center">
  <a href="/wp-content/uploads/repo-commands-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/repo-commands-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Commands section of the Edit repo page for acme-web: Add command, Install deps (pnpm install) with the Runs on creation chip, and Dev server open for editing with its name, Run on worktree creation, the command pnpm dev with Variables, and Cancel and Save, above the note that commands run in the worktree folder with your login shell.">
  </a>
  <figcaption style="text-align:center; color:#888">A repository's Commands, with one row open for editing.</figcaption>
</figure>

### Copy ignored files into new worktrees

A new worktree starts without your repository's git-ignored files, such as `.env`. To copy some of them, list them in a `.worktreeinclude` file at the repository's root, in the same format as `.gitignore`. Kepler copies them before any command set to run on worktree creation starts. It copies only files that git also ignores in the new worktree, so a copied secret cannot be committed by mistake, and it never overwrites a file already there.

## Worktrees and branches

To update, clean up, or delete worktrees and local branches across your repositories, click **Manage worktrees and branches** on the Repositories page. The **Worktrees and branches** sub-page opens.

On the sub-page, you can see which worktrees and local branches are stale, update the ones that are behind, and delete what is done. It lists every worktree, and every local branch that no worktree holds, grouped by repository, and a summary says how many look safe to delete. Kepler deletes nothing until you ask, and never deletes the base branch, which has a **Base** badge.

The sub-page has these controls:

| Control | What it does |
|---|---|
| **Search branch, path or repo** | Narrows the list. Every word you type must match the branch, the path, or the repository name |
| **Show worktrees and branches** | Filters by status: **Safe to delete**, **Needs update**, **Conflicts**, **Stale**, or **All** |
| **Show worktrees, branches or both** | Shows **All**, **Worktrees only**, or **Branches only** |
| **Stale after** *n* **days** | Sets how many days without activity make a row stale. Defaults to 14 |
| **Re-check** | Fetches every repository's remotes and checks the list again |
| **Select all** | Selects the rows in the current view |
| Selection bar | Has **Clear**, **Create task**, **Update**, and **Delete**. **Update** and **Delete** act only on selected rows you can see |

**Create task** opens the **New task** composer with the selected worktrees and branches already added: each worktree as it is, and each branch without a worktree as a branch to work on. Kepler creates nothing until you start or prepare the task. See [Create a task](/kepler/create-task).

Each row shows the following:

- Where it stands with its upstream: commits to push (↑) and pull (↓), **No upstream**, or **Upstream gone**.
- How it compares with its base, such as **3 behind main**, and how many files are uncommitted.
- How long since it was last touched, and why it may be finished, such as being merged into its base.
- The tasks, sessions, and pull request tied to it. An **External** count shows sessions started outside Kepler.

With a Jira or Jira Server account connected, a row whose branch name references a Jira issue shows a chip for that issue. To open the issue in your browser, click the chip. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

A row counts as one or more of the following:

- **Safe to delete**: its work has landed (merged into the base, or its pull request merged or closed with the upstream gone), and nothing is uncommitted, unpushed, or in use.
- **Needs update**: behind the base branch with no known conflict, so an update can bring it up to date.
- **Conflicts**: behind the base branch, and merging the base in would conflict, so you have to update it by hand.
- **Stale**: no activity for longer than the stale threshold, but nothing proves the work landed. Deleting it can lose uncommitted or unpushed work.

**Needs update** and **Conflicts** leave out rows that are safe to delete.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-worktree-cleanup-01-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-worktree-cleanup-01-v4@2x.png" class="help-center-img img-bordered" alt="The Worktrees and branches page from its description down (See which worktrees and local branches of your repositories are stale…): 4 worktrees and 2 branches in 1 repo, 3 look safe to delete, with Stale after 14 days and Re-check; Search branch, path or repo, the Safe to delete (3), Needs update, Conflicts, Stale and All filters, and All / Worktrees only / Branches only. The bar reads 2 selected with Clear, Create task, Update and Delete. Under acme-web, kepler/old-banner and kepler/promo-page (worktrees tagged Spring sale banner) and kepler/summer-teaser (Not checked out) are each 3 behind main and merged into main; old-banner and summer-teaser are ticked.">
  </a>
  <figcaption style="text-align:center; color:#888">The Worktrees and branches sub-page, filtered to what is safe to delete.</figcaption>
</figure>

### Delete worktrees and branches

Select rows, then click **Delete**. The confirmation says what is lost:

- For worktrees, their folders are removed from disk with anything the dialog lists. **Also delete the branches** deletes each worktree's branch too.
- For local branches, commits that exist only on them are lost. The dialog marks each branch that is not merged as **not merged**. **Force delete branches that are not merged** deletes those too, and **Also delete the branches on the remote** deletes the remote branches.

<figure style="text-align:center">
  <a href="/wp-content/uploads/worktree-branch-delete-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/worktree-branch-delete-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Delete 2 items? dialog for two local branches: The local branches are deleted, with Force delete branches that are not merged and Also delete the branches on the remote unticked, kepler/size-guide marked not merged, and Cancel and Delete 2 items.">
  </a>
  <figcaption style="text-align:center; color:#888">Deleting two local branches, one of them not merged.</figcaption>
</figure>

Kepler keeps any branch it cannot delete safely and says why, for example when a worktree still has it checked out. A local branch with commits that are not merged is kept too, and the result offers **Force delete** for it, which deletes the branch with those commits.

Kepler never deletes a repository's main checkout. It keeps any worktree that still has uncommitted or unpushed work, other tasks, running agent sessions, or a lock from another tool, and says why for each one. Where forcing can help, the result offers **Force delete**, which discards the listed work and ends the agent sessions running there.

### Update worktrees

To bring several worktrees and local branches up to date with their base branch at once:

1. On the Worktrees and branches sub-page, select the worktrees and branches.
2. Click **Update**. The **Update worktrees** dialog opens. Nothing changes until you confirm.
3. Under **How to update**, keep **Default** to use each repository's own setting (see [Edit a repository](#edit-a-repository)), or choose **Rebase** or **Merge** for this update.
4. Under **Push after update**, keep **Default**, or choose **Don't push**, **Push**, or **Push + Publish**. **Push** pushes only branches that already have a remote branch; **Push + Publish** also publishes the ones that do not.
5. Review the plan. Each row says how the branch will update and where it will be pushed, or **Skipped** with the reason, such as uncommitted changes or a conflict.
6. Click **Update**.

A branch with no worktree is updated in place; it is skipped if a worktree holds it or the main checkout has uncommitted changes. If Kepler prepared an update but could not apply it automatically, Kepler keeps it for you to review instead of discarding it.

When the update finishes, you can undo one row with **Roll back**, or every row with **Roll back all**. If you did not push during the update, **Push** and **Push all** push the updated branches that have an upstream. Kepler does not push a branch that moved since the update. The finished report stays in every window until you click **Dismiss**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-worktree-batch-update-01-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-worktree-batch-update-01-v4@2x.png" class="help-center-img img-bordered" alt="The Update worktrees dialog with How to update on Default and Push after update on Push + Publish. kepler/old-banner reads 3 commits behind with Rebase · Will publish to origin/kepler/old-banner, kepler/summer-teaser 3 commits behind with Rebase · Will push to origin/kepler/summer-teaser, kepler/gift-card-ui Will publish to origin/kepler/gift-card-ui, and kepler/wishlist Skipped · uncommitted changes. The footer reads 2 updates · 1 push · 2 publications beside Cancel and Update.">
  </a>
  <figcaption style="text-align:center; color:#888">The Update worktrees plan, with Push after update on Push + Publish.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-worktree-batch-update-02-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-worktree-batch-update-02-v3@2x.png" class="help-center-img img-bordered" alt="The finished update on the Worktrees and branches page: Update finished, 2 updated · 1 pushed, with Roll back all and Dismiss; kepler/old-banner reads Not pushed: no upstream and Updated, kepler/summer-teaser Pushed and Updated, each with Roll back.">
  </a>
  <figcaption style="text-align:center; color:#888">The finished update, with Roll back on each row.</figcaption>
</figure>

## Projects

Use **Projects** to group repositories that belong together under one name, such as a frontend and a backend you change together. A project's repositories act as a unit. The section has these controls:

| Control | What it does |
|---|---|
| A row | Opens the project's page |
| **New project** | Opens a page where you name a project and pick its repositories. **Add from folder** adds a repository without leaving the page |

To create the project, give it a name and click **Create**. After that, its page has no **Save** button: its name and each repository you tick or untick save as you change them. A folder's page saves its name and description the same way.

To delete a project, click **Delete project** on its page. Its repositories stay in your repository list.

***

---
