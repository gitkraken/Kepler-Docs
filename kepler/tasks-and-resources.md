---
title: Tasks and Resources
description: A Task is the unit of work in Kepler. Learn what a Task holds, how worktrees work, and how everything attached to a Task reaches your agents.
product: Kepler
feature: Tasks
content_type: concept
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
integrations: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops, jira, linear, trello]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [tasks, resources, worktrees, shared-context, draft-sessions, notes, files, uploads, sessions, archive, mcp]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

A **Task** is the unit of work in Kepler. It's one thing you're trying to get done, plus everything the agents working on it need: the repositories, the issue or pull request it came from, the branches, the notes, and every agent session you've run against it.

A Task doesn't have to start with much. You can start one from an issue in [the Kepler interface](/kepler/kepler-interface) and it arrives with the repository and issue body already attached, or you can start one with nothing at all (no repository, no branch), chase an idea, and attach the real work to it later.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-creation-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-creation-sep-2026.png" class="help-center-img img-bordered" alt="The Task creation composer, with no repo or folder, issue, or pull request attached">
  </a>
  <figcaption style="text-align:center; color:#888">Starting a Task from an idea, with nothing attached yet.</figcaption>
</figure>

***

## What a Task holds

Everything attached to a Task is a **resource**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/add-resource-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/add-resource-oct-2026.png" class="help-center-img img-bordered" alt="The Notes group in the task rail, led by the task's Prompt row, with a + on the group header and the Add resource button below.">
  </a>
  <figcaption style="text-align:center; color:#888">The + on a group header and the Add resource button open the same dialog, scoped to that category.</figcaption>
</figure>

Attach them from **Add resource** at the bottom of the task view's rail, or from the **+** on any group header, which opens the same dialog on that category. The dialog's title bar says what it adds. Offering everything a Task can hold, it reads **Add to this task**, with a row of tabs beneath it: **Repos & Folders**, **Issues**, **Pull requests**, **Notes**, **Links** and **Files**. Opened for a single kind, the title names that kind, such as **Add a note** or **Add a link**.

| Resource | What it is |
|---|---|
| **Sessions** | Agent conversations running against this Task |
| **Terminals** | Shells opened inside one of the Task's working directories |
| **Worktrees** | Git working copies the agents make changes in. Grouped as **Changes** in the rail, because that's what you go there to read |
| **Folders** | A directory that isn't a Git repository. The agent works on it in place |
| **Files** | A single file, when the whole folder isn't the point: either linked from disk by its path, or a copy uploaded to the Task |
| **Pull requests** | Pull requests from your connected Git hosts |
| **Issues** | Issues from your connected trackers |
| **Links** | Any URL worth keeping with the work |
| **Notes** | Text you write: standing instructions, decisions, reference material. The Task's own **Prompt** leads this group |

A Task can hold **more than one** of any of these. Several repositories, several issues, several pull requests: a Task spanning three repos with two linked issues is a normal Task, not a special case.

For the screen itself (the rail, the columns, split panes, tabs), see [The Task View](/kepler/task-view).

### Picking issues and pull requests

The **Issues** and **Pull requests** tabs list work from your connected providers, under a search field and a row of filters. Each row shows the item's title, a line with its identifier, repository and provider, and its age. **Show preview**, beside the search field, splits the list with a preview of the focused item: its repository, author, labels and description. **Cmd/Ctrl+Shift+P** does the same, and Kepler remembers the choice on this computer. The preview needs room, so a narrow dialog doesn't offer it.

The list works from the keyboard:

| Key | What it does |
|---|---|
| **↓** from the search field | Moves into the list |
| **↑** / **↓**, **Home** / **End** | Moves between rows |
| **Space** | Selects or clears the focused row |
| **Enter** | Adds what you selected, or the focused row when nothing is selected |

Double-click a row to add just that one. The main button counts what you picked, as in **Add to task · 1**, and **Add & keep adding** adds the selection without closing the dialog.

<figure style="text-align:center">
  <a href="/wp-content/uploads/add-resources-issue-list-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/add-resources-issue-list-oct-2026.png" class="help-center-img img-bordered" alt="The Add to this task dialog on its Issues tab with the preview pane open. Under the search field and its Preview and Refresh buttons, filter pills read GitHub, Related to me, Any repo, Open, Last 90 days, Any label and No active task. Gift card codes are case-sensitive at checkout (42 · acme-web · GitHub, 1d) is ticked and focused, above Add a wishlist to product pages (45, 3d), and the preview shows issue #42 in acme/acme-web by sam-ortiz with its bug and checkout labels and description. The footer reads 1 selected, with Cancel, Add & keep adding and Add to task · 1.">
  </a>
  <figcaption style="text-align:center; color:#888">Picking an issue, with the preview open on the focused row.</figcaption>
</figure>

### Pasting an issue link

The **Links** tab takes any URL. Paste an issue's URL and Kepler looks it up (*Looking up issue…*) before you can add it. When it finds the issue, the field reads *Adds {provider} issue {key}: {title}*, and the link is added as that issue, under its own title, rather than as a plain link. To keep it as a plain link anyway, press **Add as plain link**.

When the lookup finds nothing, or can't reach the provider, Kepler says so and adds a plain link instead:

- *No issue found for that link. It may not exist or you may not have access; it will be added as a plain link.*
- *Unable to look up that issue. It will be added as a plain link.*

<figure style="text-align:center">
  <a href="/wp-content/uploads/add-link-issue-lookup-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/add-link-issue-lookup-oct-2026.png" class="help-center-img img-bordered" alt="The Add to this task dialog on its Links tab with a Linear issue URL pasted into Add a link. Under the field, Kepler has looked the link up: Adds Linear issue SHOP-128: Show saved cards at checkout. The footer offers Cancel, Add as plain link, Add & keep adding and Add link.">
  </a>
  <figcaption style="text-align:center; color:#888">A pasted Linear URL, resolved to the issue it points at.</figcaption>
</figure>

### Files: linked or uploaded

The **Files** group holds two kinds of file, and Kepler treats them differently because only one of them is Kepler's to destroy:

| Kind | Where it lives | Its row reads | Removing it |
|---|---|---|---|
| **Linked file** | Wherever it already was on disk. Kepler links to it by its path and never changes it | Its path | **Detach file…** leaves the file where it is |
| **Uploaded copy** | Inside the Task's own folder, and belongs to this Task alone | **Task folder** | **Delete file…** deletes the copy |

A file attached to a prompt that Kepler copies into the Task when you send it is an uploaded copy too. In a window connected to another machine, the file picker on the **Files** tab of **Add resources** also offers **Upload from this machine**, which copies files from the machine you're sitting at into the Task's folder. Either kind can be written somewhere else with **Save as…** from its menu.

<figure style="text-align:center">
  <a href="/wp-content/uploads/files-group-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/files-group-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Files group in the task rail, holding two files: checkout-style-guide.md, a linked file whose row reads its path on disk, /srv/acme/brand/checkout-style-guide.md, and checkout-copy-draft.md, an uploaded copy whose row reads Task folder.">
  </a>
  <figcaption style="text-align:center; color:#888">A linked file and an uploaded copy in the Files group.</figcaption>
</figure>

### Issues and pull requests attach themselves

You don't have to remember to attach the pull request. When a Task holds no pull request yet and one of its worktrees is sitting on a branch that exactly matches an open pull request's head branch, Kepler records that pull request as a resource on its own, however the pull request was opened, including from a terminal, from GitKraken, or on the web.

<figure style="text-align:center">
  <a href="/wp-content/uploads/prs-attach-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/prs-attach-aug-2026.png" class="help-center-img img-bordered" alt="A Pull requests group in the task view's rail, auto-populated with an open pull request matching the worktree's branch">
  </a>
  <figcaption style="text-align:center; color:#888">A pull request Kepler attached on its own, matched by branch.</figcaption>
</figure>

This auto-attach behavior is deliberately narrow, because a wrong guess would put a stranger's work into your agent's context:

- The branch names must match exactly. A near-miss doesn't count.
- Kepler attaches only open pull requests whose head branch lives in the same repository. A pull request from a fork never auto-attaches.
- If another active Task already owns the pull request, Kepler leaves it there.

**Issues attach the same way.** An issue whose branch matches one of the Task's checkouts is correlated and attached on its own, so a Task started from a branch name finds the ticket behind it.

Auto-attach only adds a link; it never removes one. Detach it yourself if you don't want it on the Task.

**Work item URLs attach as issues.** When you or an agent attaches one of the following URLs, Kepler records it as an issue rather than a plain link:

- A GitLab work item, such as `https://gitlab.com/{group}/{project}/-/work_items/{number}`
- An Azure DevOps work item, such as `https://dev.azure.com/{organization}/{project}/_workitems/edit/{id}`, or the organization-level `https://dev.azure.com/{organization}/_workitems/edit/{id}`

A GitLab work item that belongs to a group rather than a project stays a plain link.

### Keeping them current

A Task's pull requests and issues refresh themselves when something that could change them happens: an agent ends a turn, one of the Task's branches is pushed, or a pull request is published. Kepler re-reads only that Task, so a busy Task doesn't cost a refresh of your whole account. Each link is looked up where it lives: in the repository it names, or on the Jira site or Linear workspace in its URL. Two repositories with the same issue number, or two Jira sites with the same key, don't get confused.

A Jira or Linear issue that moves to a new key stays attached under the link you added, and keeps refreshing from it.

To refresh by hand, use the refresh on the **Pull requests** or **Issues** group header, or **Refresh** in the Task's **⋮** menu. A refresh you ask for re-reads the provider rather than redrawing what Kepler already had, and it re-reads every stored link in full, merged pull requests included.

***

## Worktrees, and when you don't need one

Most work benefits from a **worktree**: a private Git working copy for this Task. Agents make their changes there, so nothing they do touches the checkout you're working in, and several agents can run at once without stepping on each other.

When you add a repository to a Task through **Add resource**, the **Isolated worktree** toggle decides how it's set up. The Task Composer's own repository chip, used when you create a Task, reaches the same in-place-or-isolated choice through a different control with an added branch-name field. See [Create a Task](/kepler/create-task#configuring-a-repository).

| Setting | What it says |
|---|---|
| **On** | *Its own folder. Nothing else can switch its branch.* |
| **Off** | *Uses your repository folder. Anything that switches its branch switches it here too.* |

When the branch you picked is already checked out somewhere, Git can't check it out a second time, so the toggle locks and says where the Task will work instead: *Uses {worktree}, which already has this branch.* or *Uses your repository folder, which already has this branch.*

With isolation off, the picker reads **directly in repo**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/isolated-worktree-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/isolated-worktree-aug-2026.png" class="help-center-img img-bordered" alt="The repository picker reading 'directly in repo' with isolation off">
  </a>
  <figcaption style="text-align:center; color:#888">The picker with isolation off, reading directly in repo.</figcaption>
</figure>

> **Turning isolation off means the Task has no branch of its own.** The Task uses your repository folder exactly as it stands: nothing is copied and nothing is guaranteed. Use it when you deliberately want an agent working in the checkout you're sitting in; leave it on otherwise.

Kepler always isolates a repository linked to a pull request, and locks the toggle: *This repository is linked to a pull request and always opens in its own isolated working copy.*

You can also pick the branch when you attach the repository: **Use this branch** to work directly on an existing branch, or **New branch** to branch off the repository's default branch. Each option says where the work will happen, such as *Branch off {branch} in a new worktree*. Kepler names a new branch for you unless you set one. The branch list is read fresh each time you open it, and **Refresh branches** beside **Find a branch…** fetches from your remotes first.

**A new branch forks from the repository's remote default branch**, not from whatever branch you happen to have checked out. Naming a base yourself overrides that default. A local base forks from its upstream, unless it has commits you haven't pushed: then it forks from your local tip, so those commits come along. If no remote default can be resolved (no remote, a shallow clone, offline with nothing cached), Kepler falls back to the current HEAD rather than refusing to start.

Automatic branch names are suggested from the Task's own context, led by the issue identifier where there is one, and namespaced under `kepler/` unless you configure another prefix. See [Create a Task](/kepler/create-task#naming-the-branch).

Prefer not to use a worktree? **A Task does not require a worktree, or even a repository.** Attach a plain folder and the agent works on it in place. Attach nothing and you have a space to think with the option to turn it into real work whenever the idea earns it.

### When a worktree goes missing

A worktree deleted outside Kepler **stays bound to its Task** rather than quietly disappearing from it. The row is flagged **Gone from disk**, and the pane shows the metadata Kepler recorded: **Current branch**, **Base branch**, and **Recorded path**. **Recreate worktree**, on the pane or in the worktree's menu, brings the branch back at the recorded path. If the branch itself was deleted, Kepler restores it at its last commit when that commit still exists in the repository, history and all. Failing that, it creates the branch again from the recorded base, or from the repository's default branch when the base is gone too (as it usually is once its pull request merged), and says what it branched from. That way a `git worktree prune` doesn't cost you the Task's record of where the work lived. Recreating one worktree clears only that worktree's stale Git entry, so other missing worktrees, such as ones on a drive that's unplugged, keep theirs.

The same goes for an attached folder that's been removed. Start a new session in a worktree or folder that's gone and Kepler asks first (*Recreate the worktree and start the session?*), then rebuilds it before the session starts, rather than launching an agent into a directory that isn't there. A Task with no repository or folder at all starts its sessions in the Task's own folder.

### Make a new worktree ready to build

A fresh worktree is a clean checkout: no `node_modules`, no build output, nothing your setup script would normally leave behind. An agent that starts there has to install dependencies before it can do anything, or it fails on the first build.

**Commands** solve that problem. Save a repository's setup steps once (`pnpm install`, a codegen step, whatever your project needs) and tick **Run on worktree creation**. Kepler runs them in the new worktree's folder every time it makes one for that repository, in order, before the agent starts. Commands you don't flag stay on demand: right-click a worktree in the task view rail and pick **Run command here**.

The worktree's menu is the same wherever the worktree appears. Beside **Run command here** it holds **New session here**, which opens a draft session in that worktree, and **New terminal here**. Its **Branch** submenu holds **Rename branch**, the upstream, **Change merge target…**, and **Rebase onto {target}** or **Merge {target} into this branch**. Below them come the copy actions, **Refresh**, and **Detach worktree…** and **Delete worktree…**. See [Review Changes](/kepler/review-changes#publishing-and-syncing-the-branch) for the upstream and the update.

<figure style="text-align:center">
  <a href="/wp-content/uploads/worktree-row-menu-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/worktree-row-menu-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A worktree row's right-click menu in the task rail, with its Branch submenu open on Rename branch, Set upstream, Change merge target… (main), Rebase onto main and Merge main into this branch. The menu also lists Open, Open changes, Open in, New session here, New terminal here, Run command here, Copy branch name, Copy worktree path, Copy remote URL, Refresh, and Detach worktree… and Delete worktree…, unavailable while a session is using the worktree.">
  </a>
  <figcaption style="text-align:center; color:#888">A worktree's right-click menu, with its Branch submenu open.</figcaption>
</figure>

Set them up in **Settings → Repositories**, on the repository's own page. See [Settings](/kepler/settings#per-repository-commands) for the fields, the **Variables** a command can use, and what happens when one fails.

***

## Shared context: how resources reach your agents

Kepler sends everything attached to a Task to **every agent session in it** as *shared context*. That's what a prompt means when it says *"described in the shared context above"*: the Task's prompt, the issue body, the pull request, your notes, the links.

The prompt goes in full, framed as background to the work rather than as an instruction: the agent acts on the messages you send it. Each note goes as a reference, its title and size, and the agent reads the note's text when it needs it, through Kepler's MCP server. A session with no route to that server gets every note's text in full instead.

**A launched Task brings its issues' descriptions along.** When you launch a Task with linked issues, Kepler reads each issue fresh and saves its description as a note titled *Issue {identifier}: {title}*, headed by the issue's URL. Each description is capped at 8 KB, and all of them together at 16 KB; a longer one is cut short with a pointer to the URL. Agents are told the text comes from a third party, so they treat it as information rather than instructions.

<figure style="text-align:center">
  <a href="/wp-content/uploads/shared-context-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/shared-context-aug-2026.png" class="help-center-img img-bordered" alt="A session with a collapsible 'Task context added' row listing one attached item">
  </a>
  <figcaption style="text-align:center; color:#888">A session's shared context, expanded to show what was attached.</figcaption>
</figure>

You'll see it in the conversation as a collapsible row reading **Task context added** the first time, and **Task context updated** whenever it changes, with a count of the items included. Expand it to see exactly what the agent was given.

You don't edit shared context directly. You change it by attaching, detaching, and editing resources. A change reaches each session with its next prompt rather than interrupting an agent mid-turn.

### The Task's prompt is context too

What you wrote when you started the Task is a context item of its own: the **Prompt**, at the top of the **Notes** group. It's what every session on the Task is working toward, so it rides along with the rest of the shared context, and you can edit it like a note when the goal shifts. Unlike a note, it can't be deleted.

### Starting a session without the Task's context

Sometimes you want an agent that forms its own view, such as a reviewer that shouldn't be steered by the implementer's brief. To start a session without the Task's prompt and notes, follow these steps:

1. Click **+** on the rail's **Sessions** group, or press **Cmd/Ctrl+T**. A draft session tab opens.
2. In the draft's composer footer, untick the **Task context** chip. It's on by default, and its tooltip reads *Gives the agent the task’s prompt and notes. Later changes reach it with your next message.*
3. Type your prompt and press **Start**.

The new session doesn't receive the Task's prompt or notes. It still gets the Task's worktrees, folders, files, and links, because it still needs to know where to work. The switch belongs to that draft, so turning it off doesn't change your other sessions. See [The Task View](/kepler/task-view#starting-a-session).

<figure style="text-align:center">
  <a href="/wp-content/uploads/start-with-task-context-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/start-with-task-context-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A draft session's composer with the Task context chip ticked in its footer, beside the attach and microphone buttons, and its tooltip open: Leave out the task context. Gives the agent the task's prompt and notes. Later changes reach it with your next message.">
  </a>
  <figcaption style="text-align:center; color:#888">The Task context chip, on by default.</figcaption>
</figure>

### Notes are how you give standing instructions

Attach a **Note** for anything every agent on the Task should follow: a style rule, a constraint, a decision you don't want re-litigated. Write it once and every session gets it, including sessions you start later. Because a session sees a note's title first and opens the note when it's relevant, give each note a title that says what it governs. A note can be up to 1 MB; a longer one is refused with *This note is too long. Notes can be up to 1 MB.*

<figure style="text-align:center">
  <a href="/wp-content/uploads/add-note-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/add-note-aug-2026.png" class="help-center-img img-bordered" alt="The Add to this task dialog on its Notes tab, beside Repos & Folders, Issues, Pull requests, Links and Files. The note is titled Coding conventions, and its Markdown content lists three standing instructions. Cancel, Add & keep adding and Add note sit at the bottom.">
  </a>
  <figcaption style="text-align:center; color:#888">Adding a Note with a title and Markdown content.</figcaption>
</figure>

To rename a note, double-click its name, press **F2** on the open note, or choose **Rename note** from its right-click menu. The name becomes a field: **Enter** keeps the new name and **Escape** puts the old one back. A note with no name reads **Untitled note**. The Task's **Prompt** keeps its name.

An open note has **Copy note** beside **Edit**, and **Enter** on the focused note starts editing it. An edit you left unsaved is kept as a draft: the note reads **Unsaved draft**, and **Edit** becomes **Resume draft**.

***

## Detaching and deleting

Most of what you remove from a Task isn't destroyed. The menu says which you're doing: **Detach** for something that lives elsewhere, **Delete** for something only the Task holds.

<figure style="text-align:center">
  <a href="/wp-content/uploads/detach-resource-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/detach-resource-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A linked file's right-click menu in the task rail, open on checkout-style-guide.md, with Open, Open to the side, Save as…, Copy path, and Detach file… at the bottom.">
  </a>
  <figcaption style="text-align:center; color:#888">Removing a resource from its context menu in the rail.</figcaption>
</figure>

Kepler asks separately in each case, because the answer differs:

| Resource | Dialog | What removing it does |
|---|---|---|
| **Folder** | *Detach folder?* | *The folder stays on disk — it's only removed from this task.* |
| **Linked file** | *Detach file?* | *The file stays on disk — it's only removed from this task.* |
| **Uploaded copy** | *Delete file?* | *Deletes the copy in the task folder.* |
| **Pull request** or **issue** | *Detach pull request?* / *Detach issue?* | *It's removed from this task.* |
| **Link** | *Delete link?* | *It's removed from this task.* |
| **Note** | *Delete note?* | *Deletes the note.* |

The Task's **Prompt** has no remove action.

Worktrees get more care, because deleting one can lose work.

<figure style="text-align:center">
  <a href="/wp-content/uploads/detach-worktree-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/detach-worktree-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Detach worktree? dialog, saying the worktree stays on disk and is only removed from this task, with Cancel and Detach worktree buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">Detaching a worktree leaves it on disk.</figcaption>
</figure>

The worktree's menu, in the rail or on the worktree strip, offers both, as separate entries:

- **Detach worktree…** removes it from the Task and leaves it on disk. Its dialog says only *The worktree stays on disk — it’s only removed from this task.*
- **Delete worktree…** removes it entirely. It opens **Delete worktree?**, which warns *This can’t be undone.* while confirming would delete something. The repository's main worktree has no **Delete worktree…**.

The **Delete worktree?** dialog lists the worktree with what deleting it would cost, such as **No uncommitted changes** and **Branch kept**, under a verdict like **Safe to delete**. Tick **Also delete branch** to remove the branch along with the worktree. A worktree another Task still uses can't be deleted: the dialog says which Task keeps it, and offers **Detach worktree** in place of **Delete worktree**.

Neither is possible while a session is still running in the worktree; the menu tells you how many to archive first. If another program has the folder open, the delete fails with *Kepler could not delete {path} because another program is using it. Close any editors, terminals or file explorers that have the folder open, then try again.*

Below that, a live check shows what deleting would cost, read fresh from the worktree rather than written in advance. Tick **Also delete branch** to take the branch with it, and the check re-reads, because the branch is a separate risk. Each worktree carries short tags for what's at stake:

| Tag | What it means |
|---|---|
| *{count} uncommitted files* | Changes that exist only in this working copy |
| *{count} commits not on any remote* | Commits the branch holds that were never pushed. Kepler counts them before it deletes anything |
| *Detached HEAD* | Commits that aren't on any branch |
| *In open PR #{prNumber}*, *Merged in PR #{prNumber}*, *Merged into {base}*, *Pushed* | The branch's commits are safe somewhere else, so deleting it loses nothing |
| *No uncommitted changes* | Nothing to lose |

Kepler recognizes a branch that landed through a rebase merge or a squash merge as merged, so cleaning one up doesn't warn about commits that are already in its target.

A worktree that would lose work is **kept**, not deleted, unless you tick the extra box that names it and what it would lose: *Also delete {branch}, losing {what}*. Kepler refuses the delete outright unless you confirmed it there. Nothing can destroy uncommitted or unpushed work behind your back, no matter what requested the delete.

***

## Renaming, archiving, and deleting a Task

<figure style="text-align:center">
  <a href="/wp-content/uploads/rename-task-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/rename-task-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Task actions menu of the Fix the cart total row, unread with a New reply, with Rename task highlighted among Open task page, Progress (In Development), Mark as read, Copy task link, Copy task prompt, Add resource…, Refresh, Shut down all agents, Archive task and Delete task.">
  </a>
  <figcaption style="text-align:center; color:#888">The Task actions menu, open from a task's row.</figcaption>
</figure>

From the **Task actions** (**⋮**) menu, on the task's row or in the task view's header:

| Action | What it does |
|---|---|
| **Mark as read** / **Mark as unread** | **Mark as read** appears while any of the Task's sessions is unread, and marks them all read. Otherwise the menu offers **Mark as unread** |
| **Rename task** | Tasks name themselves when they're created; rename when the name stops fitting. The name becomes an editable field in place; its **Auto-name** button suggests one from the Task's prompt and resources, into the field, for you to accept or edit; on the task page, double-clicking the Task's name does the same |
| **Copy task link** | Copies a Kepler link to the Task. **Cmd/Ctrl+C** on a focused task row copies it too |
| **Refresh** | Re-reads the Task's worktrees and its pull request and issue links. Shortly after a refresh, the providers can't be read again yet, so the row is locked and says when you can try again |
| **Archive task** | Takes it out of the active list and keeps it as history. Its sessions and resources are kept, and nothing is destroyed unless you ask for it |
| **Restore task** | On an archived Task, in place of **Archive task**. It goes straight back, unless another active Task now holds the same pull request; then Kepler asks first, because restoring archives that one |
| **Delete task** | Removes the Task along with its sessions and resources |

**Kepler suggests archiving a finished Task.** Once a Task reaches **Done**, with no unpushed work in its worktrees and no session still working or waiting on you, its header asks *Ready to archive?* with an **Archive** button. Dismiss it and that Task stops asking.

**Archive** and **Delete** ask the same three questions, in the same dialog, because they're the same act. Each box stays unavailable until the one above it is ticked, and Kepler remembers your choices for next time:

- **Also delete worktrees**
- **Also delete branches**
- **Also delete the branch on the remote**

Until you tick them, *Worktrees and branches stay on disk unless you tick the boxes below.* Tick the first, and Kepler lists every worktree with the same tags a single worktree delete shows, and says what will happen to each:

- A worktree that's safe goes.
- A worktree that would lose work is **kept**, *because deleting it would lose work*, unless you tick the box that names it and confirms the loss.
- A worktree Kepler can't touch is listed with why it's staying: another Task still uses it, it's the repository's main worktree, a session still runs in it, or it's already gone from disk.

Ticking **Also delete branches** re-reads the list, so a worktree that was safe a moment ago can turn into a warning. If the check is slow you can confirm anyway; any worktree that would lose work is kept.

With **Also delete the branch on the remote** ticked, Kepler deletes each branch's remote copy after the local branch goes. It leaves the remote branch alone when deleting it could lose something, and a *Kept a branch on the remote* notice gives the reason: the branch has an open pull request, it has commits that are not on the remote, the remote has commits this branch does not, or the remote branch changed after it was checked.

<figure style="text-align:center">
  <a href="/wp-content/uploads/archive-task-dialog-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/archive-task-dialog-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Archive task? dialog for Upgrade the payment SDK, saying the task moves to the Archived section, its sessions and resources are kept, it can be restored any time, and its worktrees and branches stay on disk unless you tick the boxes below. Also delete worktrees is unticked, and Also delete branches and Also delete the branch on the remote are unavailable until the box above each is ticked. Cancel and Archive task close the dialog.">
  </a>
  <figcaption style="text-align:center; color:#888">The Archive task? dialog, before you tick anything.</figcaption>
</figure>
<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-archive-task-worktrees-01-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-archive-task-worktrees-01-v2@2x.png" class="help-center-img img-bordered" alt="The Archive task? dialog for Upgrade the payment SDK with Also delete worktrees and Also delete branches ticked, and Also delete the branch on the remote unticked. Its Worktrees and branches list reads 1 of 2 will be deleted: kepler/payment-sdk-v5, with 1 uncommitted file, is kept because deleting it would lose work, and kepler/payment-sdk-docs, with no unpushed commits, will be deleted. Below it, an unticked box offers to also delete kepler/payment-sdk-v5, losing 1 uncommitted file.">
  </a>
  <figcaption style="text-align:center; color:#888">The same dialog with worktrees and branches ticked: one worktree goes, one is kept.</figcaption>
</figure>

**Restore task** appears in the task view's header as soon as the Task is archived. From a row in the main list, it appears only once you've filtered **Activity** to **Archived**. See [Arranging Your Work](/kepler/arranging-your-work).

You can archive and restore individual sessions the same way, from the session's own menu in the rail.

***

## What an agent can do with a Task's resources

Agents reach the Task through Kepler's own MCP (Model Context Protocol) server, `kepler-workspace`, so an agent can keep the Task's resource list honest instead of leaving it to you, and can find and coordinate with the rest of your work.

<div class="note" markdown="1">

**The workspace tools were renamed in Kepler 0.15.** Each tool is now named for what it acts on, then what it does, such as `task_get` or `worktree_create`. If an agent's settings allow-list `mcp__kepler-workspace__` tools by name, update them to the names below.

</div>

The tools name things by id, and each id carries its kind: `task:`, `session:`, `repo:`, `worktree:`, `folder:`, `note:`, `file:` and `account:`. A Kepler link to a Task or a session that you paste into the chat works as its id. Wherever a tool takes a repository, the agent can also name it by one of its **Aliases**, set on the repository's page in **Settings → Repositories**. See [Settings](/kepler/settings).

**Reading Tasks and notes**

| Tool | What it does |
|---|---|
| `task_get` | Read a Task: its stage, its worktrees and folders, notes, files, links, related Tasks and newest sessions. On the agent's own Task, later calls return only what changed, and `refresh` re-reads pull request and issue state, the disk and Git first |
| `task_list` | Find Tasks by name, prompt, note text or file name, filtered by stage, hold, repository, or whether they belong to the agent's own work. Archived Tasks only on request |
| `task_note_read` | Read one note's full text. Notes otherwise arrive as references (title and size) |

**Finding sessions, agents and places**

| Tool | What it does |
|---|---|
| `session_list` | Find agent sessions by name, Task, agent or place, with each one's state and what it's waiting on: a permission, an answer, or an approval. It can keep only the sessions that need you |
| `session_read` | Read another session's conversation, at the level of detail the agent asks for, by its id or a link from **Copy session link**. It returns the newest messages, or only the last reply with `limit:1`, and reports what a running session waits on, including a plan it's holding for your review |
| `agent_list` | List the agents, accounts, models and effort values a new session can start with, and the modes each agent supports |
| `repo_list` | List the repositories and folders work can happen in, marking the ones this Task uses. It finds one by name, path or alias |

**Notes, links and files**

| Tool | What it does |
|---|---|
| `task_note_write` | Create a note, or edit one: replace the whole note, replace the section under one heading, or add to the end. A replace carries the version the agent last read, so a note changed underneath it is refused rather than overwritten |
| `task_note_delete` | Delete a note. The Task's **Prompt** can't be deleted |
| `task_link_update` | Attach or detach issue, pull request and other links. Kepler classifies each URL and fetches its title and status when it can, and an agent that starts a server you're meant to open (a dev server, Storybook, a preview) attaches its local URL so it shows on the Task, and detaches it when it stops the server for good |
| `task_file_attach` | Attach files by path, linked rather than copied. A file the agent wrote in a temporary folder can be attached as a copy saved with the Task instead, up to 10 MiB |
| `task_file_detach` | Detach files. A linked file stays on disk; an uploaded copy is deleted |

**Worktrees**

| Tool | What it does |
|---|---|
| `worktree_create` | Create a worktree on a new branch and bind it to the Task, forked from the repository's remote default branch or from a base the agent names |
| `worktree_attach` | Bind a worktree or folder that already exists on disk to the Task, changing no files |
| `worktree_detach` | Remove a binding without touching the worktree, the branch, the files, or the sessions running there. Neither the Task's own folder nor the place the agent itself runs in can be detached |
| `worktree_update` | Record a new merge target after the agent rebased a stacked branch or moved it onto another branch. A merge target you saved yourself takes precedence |
| `worktree_delete` | Delete a worktree from disk. Its branch goes too when Kepler finds it merged; an unmerged branch is kept unless the agent asks to delete it |

Where AI Sync and AI Compose are turned on, the `sync_*` and `compose_*` tools also let an agent update a branch from its base with a rebase or merge, and reorganize its commits. See [Review Changes](/kepler/review-changes#agent-tools-ai-sync-and-ai-compose).

**Progress and lifecycle**

| Tool | What it does |
|---|---|
| `task_create` | Create a *separate* Task beside this one, with its own prompt, places, notes, links and files, for work that deserves tracking in its own right. It's linked back to this one (as a sub-task, parent, follow-up, or just related), and nothing starts on it |
| `task_update` | Set the stage your board shows (**Exploration**, **In Development**, **In Review**, **Done**), put the Task on hold or lift the hold, rename it, or restore it from the archive, or hand the stage back to Kepler's own reading of Git and pull requests. If it replaces a stage or a hold you set, it tells you |
| `task_archive` | Archive a Task, which alone stops nothing and deletes nothing. With cleanup, it also deletes the Task's worktrees and their merged branches |

**Starting and coordinating work**

| Tool | What it does |
|---|---|
| `session_start` | Start an agent session on a Task and send it a first message, in a place the agent names or in a new worktree, as the starting session's child: a delegate, a reviewer, or a handoff. It runs on the same agent, account, model, mode and effort unless the agent picks others from `agent_list`, and it can start without the Task's context, as a reviewer would |
| `session_send` | Send another session a prompt to act on, or a message for its inbox. A session reports back to the one that started it with a status (progress, done, blocked or failed), and can also stop the other session's running turn |
| `session_update` | Rename a session. Sessions that run in the terminal or outside Kepler can't be renamed |
| `session_archive` | Archive a session: its history stays and its agent stops. A session can't archive itself |
| `inbox_read` | Read this session's inbox, or wait up to 60 seconds for reports from the sessions it started |
| `approval_list` | List every request waiting on your approval. It can't approve or deny anything |
| `theme_get` / `theme_save` | Read Kepler's theme format, then check a theme file and install it into the themes folder |

### What runs at once, and what asks you

Every workspace tool is pre-approved, in Chat and in Terminal alike, so none of them shows the agent's own permission prompt. Instead, Kepler decides for itself which requests can run at once.

An agent works freely within its own work: its own Task, and the Tasks and sessions connected to it because the agent created them or started sessions on them. Reads run at once anywhere, and so do creating a Task, a note or a worktree. Changes inside the agent's own work run at once too, except the ones that can lose something.

The following wait for your approval:

- Sending a prompt to any session other than one the agent started itself, or a message to a session outside its own work
- Stopping or renaming a session outside its own work, or archiving any session other than one it started
- Changing a Task outside its own work: its stage, hold, name, links or notes, or detaching its files
- Restoring a Task when another active Task holds the same pull request
- Deleting any note
- Detaching an uploaded file, because its saved copy is deleted
- Archiving a Task outside its own work or with other live sessions, and any archive that also deletes worktrees
- Deleting a worktree that has something to lose (uncommitted changes, unpushed commits on a branch being deleted, commits on a detached HEAD, a status Kepler can't read), or that another Task is bound to
- Starting a session in a more permissive mode than the agent's own, or on a Task outside its own work
- Overwriting a theme file where there's no Trash to keep the old one
- The AI Sync and Compose tools that change a repository or rewrite its history

Modes are compared on three levels, plan, edit and auto, which Kepler maps onto each agent's own permission modes. A session an agent starts can't run above the mode of the session that started it unless you approve; the request says *More permissive than the asking session, which is in {mode} mode.*

The request shows up as an approval card above the asking session's composer, with **Approve** and **Deny**. **Approve**'s menu can approve every request of that kind from the session, or always. A rule you make with **Always approve** is listed under **Settings → Agents → Approvals**, where **Remove** takes it away. **Always approve** isn't offered for actions that can lose work. See [Agent Sessions](/kepler/agent-sessions#when-the-agent-asks-you-something).

The agent doesn't wait on the card. It's told the request is awaiting your approval and carries on, and the outcome arrives in its inbox. Before an approved request runs, Kepler checks again: if what it would act on changed in the meantime, such as a worktree that picked up new commits, nothing runs.

Deleting a worktree through `worktree_delete` carries the same protection your own delete does. It refuses while a live session is running in the worktree, including the agent's own. A worktree it deletes stays on the Task, marked gone, until it's detached.

### Reports between sessions

Each session has an **inbox** for what other agents send it: reports and messages, changes in the state of a session it started, and the outcomes of its approval requests. When an item arrives for an idle session, Kepler wakes the session to read it; a busy session reads it when its turn ends. Sessions running in Terminal are woken the same way. A session whose agent can't reach Kepler's workspace tools isn't sent state changes.

A session with unread reports carries a badge with their count on its tab and rail row. Above its composer, **Have it read them** asks the agent to read them now.

Agents that keep waking each other can loop, so after 20 turns started by agents rather than by you, reports stop waking the session. The session reads *Reports from other agents are paused*, with **Resume reports** to turn wakes back on. Sending the session a message of your own resumes them too.

---
