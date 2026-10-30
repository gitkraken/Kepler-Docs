---
title: Tasks and Resources
description: A task is the unit of work in Kepler. Learn what you can attach to a task, how worktrees work, and how a task's resources reach your agents.
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

A **task** is the unit of work in Kepler. It is one thing you want to get done, plus everything the agents working on it need: the repositories, the issue or pull request it came from, the branches, the notes, and every agent session you have run on it.

You can start a task with as much or as little as you have:

- Start a task from an issue in [the Kepler interface](/kepler/kepler-interface), and it opens with the repository and the issue body already attached.
- Start a task with nothing attached (no repository, no branch) to explore an idea, and attach the repositories and issues later.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-creation-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-creation-sep-2026.png" class="help-center-img img-bordered" alt="The New task composer, with no repo or folder, issue, or pull request attached">
  </a>
  <figcaption style="text-align:center; color:#888">Starting a task from an idea, with nothing attached yet.</figcaption>
</figure>

***

## What a task holds

Everything attached to a task is a **resource**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/add-resource-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/add-resource-oct-2026.png" class="help-center-img img-bordered" alt="The Notes group in the task's context panel, led by the task's Prompt row, with a + on the group header and the Add resource button below.">
  </a>
  <figcaption style="text-align:center; color:#888">The + on a group header and the Add resource button open the same dialog, scoped to that category.</figcaption>
</figure>

To attach a resource, use one of these controls on the task page:

- **Add resource**, at the bottom of the context panel, opens a dialog titled **Add to this task**. Its tabs cover every kind of resource: **Repos & Folders**, **Issues**, **Pull requests**, **Notes**, **Links** and **Files**.
- The **+** on a group header in the context panel opens the same dialog for that kind of resource only. Its title names the kind, such as **Add a note** or **Add a link**.

A task can hold these kinds of resource:

| Resource | What it is |
|---|---|
| **Sessions** | Agent conversations that run on this task |
| **Terminals** | Shells opened in one of the task's working directories |
| **Worktrees** | Git working copies that the agents change. The context panel lists them under **Changes**, because you go there to read the changes |
| **Folders** | A directory that is not a Git repository. The agent works on it in place |
| **Files** | A single file, when you need the file rather than its whole folder. A file is either linked from disk by its path or uploaded to the task as a copy |
| **Pull requests** | Pull requests from your connected Git hosts |
| **Issues** | Issues from your connected trackers |
| **Links** | Any URL you want to keep with the work |
| **Notes** | Text you write, such as standing instructions, decisions and reference material. The task's own **Prompt** is the first item in this group |

A task can hold **more than one** of each kind. For example, a task can span 3 repositories and link 2 issues.

To learn how the task page is laid out (the context panel, columns, split panes and tabs), see [the task page](/kepler/task-view).

### Picking issues and pull requests

The **Issues** and **Pull requests** tabs list work from your connected providers, under a search field and a row of filters. Each row shows the item's title, a line with its identifier, repository and provider, and its age.

To see more about an item before you add it, click **Show preview** beside the search field, or press **Cmd/Ctrl+Shift+P**. The list splits to show a preview of the focused item: its repository, author, labels and description. Kepler remembers this choice on this computer. A narrow dialog does not offer the preview, because the preview needs the room.

You can use the list from the keyboard:

| Key | What it does |
|---|---|
| **↓** from the search field | Moves into the list |
| **↑** / **↓**, **Home** / **End** | Moves between rows |
| **Space** | Selects or clears the focused row |
| **Enter** | Adds what you selected, or the focused row when nothing is selected |

To add a single item, double-click its row. The main button shows how many items you selected, as in **Add to task · 1**. To add the selection and keep the dialog open, click **Add & keep adding**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/add-resources-issue-list-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/add-resources-issue-list-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Add to this task dialog on its Issues tab with the preview pane open. Under the search field and its Preview and Refresh buttons, filter pills read GitHub, Related to me, Any repo, Open, Last 90 days, Any label and No active task. Gift card codes are case-sensitive at checkout (42 · acme-web · GitHub, 1d) is ticked and focused, above Add a wishlist to product pages (45, 3d), and the preview shows issue #42 in acme/acme-web by sam-ortiz with its bug and checkout labels and description. The footer reads 1 selected, with Cancel, Add & keep adding and Add to task · 1.">
  </a>
  <figcaption style="text-align:center; color:#888">Picking an issue, with the preview open on the focused row.</figcaption>
</figure>

### Pasting an issue link

The **Links** tab accepts any URL. When you paste an issue's URL, Kepler looks up the issue (*Looking up issue…*) before you can add it. If Kepler finds the issue, the field reads *Adds {provider} issue {key}: {title}*, and Kepler adds the link as that issue, under the issue's title, rather than as a plain link. To add it as a plain link anyway, click **Add as plain link**.

If the lookup finds nothing, or cannot reach the provider, Kepler shows one of these messages and adds a plain link instead:

- *No issue found for that link. It may not exist or you may not have access; it will be added as a plain link.*
- *Unable to look up that issue. It will be added as a plain link.*

<figure style="text-align:center">
  <a href="/wp-content/uploads/add-link-issue-lookup-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/add-link-issue-lookup-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Add to this task dialog on its Links tab with a Linear issue URL pasted into Add a link. Under the field, Kepler has looked the link up: Adds Linear issue SHOP-128: Show saved cards at checkout. The footer offers Cancel, Add as plain link, Add & keep adding and Add link.">
  </a>
  <figcaption style="text-align:center; color:#888">A pasted Linear URL, resolved to the issue it points at.</figcaption>
</figure>

### Files: linked or uploaded

The **Files** group holds 2 kinds of file. Kepler removes them differently, because it owns only the uploaded copy:

| Kind | Where it lives | Its row reads | Removing it |
|---|---|---|---|
| **Linked file** | Where it already was on disk. Kepler links to it by its path and never changes it | Its path | **Detach file…** leaves the file where it is |
| **Uploaded copy** | In the task's own folder. It belongs to this task only | **Task folder** | **Delete file…** deletes the copy |

Other ways files reach a task:

- When you attach a file to a prompt, Kepler copies it into the task when you send the prompt. That copy is an uploaded copy too.
- In a window connected to another machine, the file picker on the **Files** tab of **Add resources** also offers **Upload from this machine**. It copies files from the machine you are using into the task's folder.

To save either kind of file somewhere else, choose **Save as…** from its menu.

<figure style="text-align:center">
  <a href="/wp-content/uploads/files-group-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/files-group-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Files group in the task's context panel, holding two files: checkout-style-guide.md, a linked file whose row reads its path on disk, /srv/acme/brand/checkout-style-guide.md, and checkout-copy-draft.md, an uploaded copy whose row reads Task folder.">
  </a>
  <figcaption style="text-align:center; color:#888">A linked file and an uploaded copy in the Files group.</figcaption>
</figure>

### Issues and pull requests attach themselves

You do not have to attach a task's pull request yourself. If a task holds no pull request yet, and one of its worktrees is on a branch that exactly matches an open pull request's head branch, Kepler attaches that pull request to the task. This works however the pull request was opened, including from a terminal, from GitKraken, or on the web.

<figure style="text-align:center">
  <a href="/wp-content/uploads/prs-attach-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/prs-attach-aug-2026.png" class="help-center-img img-bordered" alt="A Pull requests group in the task's context panel, auto-populated with an open pull request matching the worktree's branch">
  </a>
  <figcaption style="text-align:center; color:#888">A pull request Kepler attached on its own, matched by branch.</figcaption>
</figure>

Kepler limits automatic attachment to these cases, because a wrong match would put someone else's work into your agent's context:

- The branch names must match exactly. A similar name does not match.
- Kepler attaches only open pull requests whose head branch is in the same repository. A pull request from a fork is never attached automatically.
- Kepler attaches a pull request even when another active task already holds it. Several tasks can share 1 pull request, and attaching it to one task never archives it or detaches it from the other.

**Issues attach the same way.** When an issue's branch matches one of the task's checkouts, Kepler attaches the issue. A task you start from a branch name therefore gets the issue behind that branch.

Automatic attachment only adds links. It never removes one. To remove a link you do not want on the task, detach it.

**Work item URLs attach as issues.** When you or an agent attaches one of the following URLs, Kepler records it as an issue rather than a plain link:

- A GitLab work item, such as `https://gitlab.com/{group}/{project}/-/work_items/{number}`
- An Azure DevOps work item, such as `https://dev.azure.com/{organization}/{project}/_workitems/edit/{id}`, or the organization-level `https://dev.azure.com/{organization}/_workitems/edit/{id}`

A GitLab work item that belongs to a group rather than a project stays a plain link.

### Keeping them current

Kepler refreshes a task's pull requests and issues when something happens that could change them:

- An agent ends a turn.
- Someone pushes one of the task's branches.
- Someone publishes a pull request.

Kepler re-reads only that task, so a busy task does not trigger a refresh of your whole account. Kepler looks up each link where it lives: in the repository it names, or on the Jira site or Linear workspace in its URL. As a result, 2 repositories with the same issue number, or 2 Jira sites with the same key, stay separate.

A Jira or Linear issue that moves to a new key stays attached under the link you added, and Kepler keeps refreshing it from that link.

To refresh by hand, click the refresh button on the **Pull requests** or **Issues** group header, or choose **Refresh** in the task's **⋮** menu. A refresh you ask for re-reads the provider instead of showing what Kepler already had. It re-reads every stored link in full, including merged pull requests.

***

## Worktrees and working in place

A **worktree** is a private Git working copy for one task. Agents make their changes in the worktree, so nothing they do touches the checkout you work in, and several agents can run at once without changing each other's files. Use a worktree for most work.

When you add a repository to a task through **Add resource**, the **Isolated worktree** toggle sets whether the task gets a worktree. When you create a task, the repository chip in the **New task** composer offers the same choice through a different control, which adds a branch-name field. See [Create a task](/kepler/create-task#configuring-a-repository).

| Setting | What it says |
|---|---|
| **On** | *Its own folder. Nothing else can switch its branch.* |
| **Off** | *Uses your repository folder. Anything that switches its branch switches it here too.* |

If the branch you picked is already checked out somewhere, Git cannot check it out a second time. The toggle locks and says where the task will work instead: *Uses {worktree}, which already has this branch.* or *Uses your repository folder, which already has this branch.* With isolation off, the picker reads **directly in repo**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/isolated-worktree-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/isolated-worktree-aug-2026.png" class="help-center-img img-bordered" alt="The repository picker reading 'directly in repo' with isolation off">
  </a>
  <figcaption style="text-align:center; color:#888">The picker with isolation off, reading directly in repo.</figcaption>
</figure>

> **With isolation off, the task has no branch of its own.** The task uses your repository folder exactly as it is. Kepler copies nothing and protects nothing. Turn isolation off only when you want an agent to work in your own checkout. Otherwise, leave it on.

Kepler always isolates a repository linked to a pull request, and locks the toggle: *This repository is linked to a pull request and always opens in its own isolated working copy.*

When you attach the repository, you can also pick the branch:

- **Use this branch** works directly on an existing branch.
- **New branch** creates a branch from the repository's default branch.

Each option says where the work will happen, such as *Branch off {branch} in a new worktree*. Kepler names a new branch for you unless you set a name. Kepler reads the branch list again each time you open it, and **Refresh branches**, beside **Find a branch…**, fetches from your remotes first.

**A new branch starts from the repository's remote default branch**, not from the branch you have checked out. To start from another branch, name a base yourself:

- A local base starts from its upstream.
- If the local base has commits you have not pushed, the new branch starts from your local tip instead, so it includes those commits.

If Kepler cannot resolve a remote default branch (no remote, a shallow clone, or offline with nothing cached), it starts the branch from the current HEAD instead of refusing to start.

Kepler suggests branch names from the task's own context. A suggested name starts with the issue identifier when the task has one, and sits under the `kepler/` prefix unless you configure another prefix. See [Create a task](/kepler/create-task#naming-the-branch).

**A task does not require a worktree, or even a repository.** Attach a plain folder, and the agent works on it in place. Attach nothing, and you have a space to explore an idea. You can attach repositories and other resources later, when you are ready to start the work.

### When a worktree goes missing

A worktree deleted outside Kepler **stays bound to its task**, so the task keeps its record of where the work was, even after a `git worktree prune`. The row is flagged **Gone from disk**, and the pane shows the details Kepler recorded: **Current branch**, **Base branch**, and **Recorded path**.

To bring the worktree back, click **Recreate worktree** on the pane, or choose it from the worktree's menu. Kepler recreates the worktree at the recorded path. If the branch was deleted too, Kepler rebuilds it in this order:

1. If the branch's last commit still exists in the repository, Kepler restores the branch at that commit, with its history.
2. Otherwise, Kepler creates the branch again from the recorded base branch.
3. If the base branch is gone too, as it usually is after its pull request merges, Kepler creates the branch from the repository's default branch.

Kepler tells you which branch it started from. Recreating one worktree clears only that worktree's stale Git entry. Other missing worktrees, such as ones on an unplugged drive, keep their entries.

An attached folder that was removed stays on the task the same way. If you start a new session in a worktree or folder that is gone, Kepler asks first (*Recreate the worktree and start the session?*). It then rebuilds the worktree or folder before the session starts, so the agent never starts in a directory that does not exist. A task with no repository or folder starts its sessions in the task's own folder.

### Make a new worktree ready to build

A new worktree is a clean checkout. It has no `node_modules`, no build output, and none of the files your setup script would normally create. An agent that starts there has to install dependencies first, or its first build fails.

To prepare new worktrees automatically, use **Commands**. Save a repository's setup steps once, such as `pnpm install` or a code generation step, and tick **Run on worktree creation**. Each time Kepler creates a worktree for that repository, it runs those commands in order in the new worktree's folder, before the agent starts. To run a command that is not set to run on creation, right-click a worktree in the context panel and choose **Run command here**.

The worktree's menu has the same entries wherever the worktree appears:

- **Run command here**, **New session here**, which opens a draft session in that worktree, and **New terminal here**.
- The **Branch** submenu, with **Rename branch**, the upstream, **Change merge target…**, and **Rebase onto {target}** or **Merge {target} into this branch**. For the upstream and updating the branch, see [Review Changes](/kepler/review-changes#publishing-and-syncing-the-branch).
- The copy actions, **Refresh**, **Detach worktree…** and **Delete worktree…**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/worktree-row-menu-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/worktree-row-menu-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="A worktree row's right-click menu in the task's context panel, with its Branch submenu open on Rename branch, Set upstream, Change merge target… (main), Rebase onto main and Merge main into this branch. The menu also lists Open, Open changes, Open in, New session here, New terminal here, Run command here, Copy branch name, Copy worktree path, Copy remote URL, Refresh, and Detach worktree… and Delete worktree…, unavailable while a session is using the worktree.">
  </a>
  <figcaption style="text-align:center; color:#888">A worktree's right-click menu, with its Branch submenu open.</figcaption>
</figure>

To set up commands, open **Settings → Repositories** and go to the repository's own page. See [Settings](/kepler/settings-repositories#per-repository-commands) for the fields, the **Variables** a command can use, and what happens when one fails.

### What a worktree does not separate

A worktree gives each task its own copy of the files, but nothing else. Tasks still share everything outside the worktree's folder:

- **Ports.** Two worktrees that start the same dev server on the same port collide, and the second server fails to start.
- **Databases and other local services.** Agents in different worktrees that point at the same database read and write the same data.
- **Caches and files outside the repository.** A global package cache or a file in your home folder is the same for every worktree.

To keep tasks apart, give each worktree its own settings when Kepler creates it. Add a per-repository command that runs on worktree creation and writes those settings, such as a port or a database name, into a local config file in the new worktree. The command runs in the new worktree's folder, and its **Variables** menu can insert the worktree's path. See [Settings](/kepler/settings-repositories#per-repository-commands).

***

## Shared context: how resources reach your agents

Kepler sends everything attached to a task to **every agent session in the task** as *shared context*: the task's prompt, the issue body, the pull request, your notes and the links. When a prompt refers to something *"described in the shared context above"*, it means these items.

Kepler sends each kind of item differently:

- **The task's prompt** goes in full, as background to the work rather than as an instruction. The agent acts on the messages you send it.
- **Each note** goes as a reference, with its title and size. The agent reads the note's text through Kepler's Model Context Protocol (MCP) server when it needs it. A session that cannot reach that server gets the full text of every note instead.

**Launching a task saves its issues' descriptions as notes.** When you launch a task with linked issues, Kepler reads each issue again and saves its description as a note titled *Issue {identifier}: {title}*, with the issue's URL at the top. Each description is limited to 8 KB, and all of them together to 16 KB. Kepler cuts a longer description short and adds a pointer to the URL. Kepler tells agents that the text comes from a third party, so they treat it as information rather than instructions.

<figure style="text-align:center">
  <a href="/wp-content/uploads/shared-context-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/shared-context-aug-2026.png" class="help-center-img img-bordered" alt="A session with a collapsible 'Task context added' row listing one attached item">
  </a>
  <figcaption style="text-align:center; color:#888">A session's shared context, expanded to show what was attached.</figcaption>
</figure>

In the conversation, shared context appears as a collapsible row with a count of the items included. The row reads **Task context added** the first time, and **Task context updated** each time the context changes. Expand the row to see exactly what the agent received.

You do not edit shared context directly. To change it, attach, detach or edit resources. Each session receives the change with its next prompt, so the change does not interrupt an agent during a turn.

### The task's prompt is context too

The text you wrote when you started the task is a context item of its own: the **Prompt**, at the top of the **Notes** group. Every session on the task works toward this prompt, so Kepler sends it with the rest of the shared context. When the goal changes, edit the prompt the same way you edit a note. Unlike a note, the prompt cannot be deleted.

### Starting a session without the task's context

Sometimes you want an agent that forms its own view, such as a reviewer that should not be influenced by the implementer's brief. To start a session without the task's prompt and notes, follow these steps:

1. Click **+** on the **Sessions** group in the context panel, or press **Cmd/Ctrl+T**. A draft session tab opens.
2. In the draft's composer footer, untick the **Task context** chip. The chip is on by default, and its tooltip reads *Gives the agent the task’s prompt and notes. Later changes reach it with your next message.*
3. Type your prompt and click **Start**.

The new session does not receive the task's prompt or notes. It still gets the task's worktrees, folders, files and links, because it still needs to know where to work. The chip applies only to that draft, so turning it off does not change your other sessions. See [Starting a session](/kepler/task-view#starting-a-session).

<figure style="text-align:center">
  <a href="/wp-content/uploads/start-with-task-context-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/start-with-task-context-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="A draft session's composer with the Task context chip ticked in its footer, beside the attach and microphone buttons, and its tooltip open: Leave out the task context. Gives the agent the task's prompt and notes. Later changes reach it with your next message.">
  </a>
  <figcaption style="text-align:center; color:#888">The Task context chip, on by default.</figcaption>
</figure>

### Notes are how you give standing instructions

Attach a **Note** for anything every agent on the task should follow, such as a style rule, a constraint, or a decision you do not want reopened. Write it once, and every session gets it, including sessions you start later. A session sees a note's title first and opens the note when it is relevant, so give each note a title that says what it covers. A note can be up to 1 MB. Kepler refuses a longer note with *This note is too long. Notes can be up to 1 MB.*

<figure style="text-align:center">
  <a href="/wp-content/uploads/add-note-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/add-note-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Add to this task dialog on its Notes tab, beside Repos & Folders, Issues, Pull requests, Links and Files. The note is titled Coding conventions, and its Markdown content lists three standing instructions. Cancel, Add & keep adding and Add note sit at the bottom.">
  </a>
  <figcaption style="text-align:center; color:#888">Adding a Note with a title and Markdown content.</figcaption>
</figure>

To rename a note, double-click its name, press **F2** on the open note, or choose **Rename note** from its right-click menu. The name becomes a field. Press **Enter** to keep the new name, or **Escape** to restore the old one. A note with no name reads **Untitled note**. The task's **Prompt** cannot be renamed.

To edit an open note, click **Edit**, or press **Enter** on the focused note. **Copy note**, beside **Edit**, copies the note. If you leave an edit unsaved, Kepler keeps it as a draft: the note reads **Unsaved draft**, and **Edit** becomes **Resume draft**.

***

## Detaching and deleting

Removing a resource from a task usually leaves the resource itself intact. The menu shows which action you are taking:

- **Detach** removes something that lives elsewhere, such as a folder or a pull request, from the task.
- **Delete** removes something that only the task holds, such as a note or an uploaded copy.

<figure style="text-align:center">
  <a href="/wp-content/uploads/detach-resource-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/detach-resource-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A linked file's right-click menu in the task's context panel, open on checkout-style-guide.md, with Open, Open to the side, Save as…, Copy path, and Detach file… at the bottom.">
  </a>
  <figcaption style="text-align:center; color:#888">Removing a resource from its right-click menu in the context panel.</figcaption>
</figure>

Each kind of resource has its own confirmation dialog, because removing it has a different effect:

| Resource | Dialog | What removing it does |
|---|---|---|
| **Folder** | *Detach folder?* | *The folder stays on disk — it's only removed from this task.* |
| **Linked file** | *Detach file?* | *The file stays on disk — it's only removed from this task.* |
| **Uploaded copy** | *Delete file?* | *Deletes the copy in the task folder.* |
| **Pull request** or **issue** | *Detach pull request?* / *Detach issue?* | *It's removed from this task.* |
| **Link** | *Delete link?* | *It's removed from this task.* |
| **Note** | *Delete note?* | *Deletes the note.* |

The task's **Prompt** has no remove action.

Deleting a worktree can lose work, so Kepler adds more checks before it deletes one.

<figure style="text-align:center">
  <a href="/wp-content/uploads/detach-worktree-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/detach-worktree-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Detach worktree? dialog, saying the worktree stays on disk and is only removed from this task, with Cancel and Detach worktree buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">Detaching a worktree leaves it on disk.</figcaption>
</figure>

The worktree's menu, in the context panel or in the worktree tab's header, has 2 separate entries:

- **Detach worktree…** removes the worktree from the task and leaves it on disk. Its dialog says only *The worktree stays on disk — it’s only removed from this task.*
- **Delete worktree…** removes the worktree from disk. It opens **Delete worktree?**, which warns *This can’t be undone.* when confirming would delete something. The repository's main worktree has no **Delete worktree…** entry.

The **Delete worktree?** dialog lists the worktree with what deleting it would cost, such as **No uncommitted changes** and **Branch kept**, under a verdict such as **Safe to delete**. To remove the branch along with the worktree, tick **Also delete branch**. You cannot delete a worktree that another task still uses. In that case, the dialog names the task that uses it and offers **Detach worktree** instead of **Delete worktree**.

You cannot detach or delete a worktree while a session is still running in it. The menu tells you how many sessions to archive first. If another program has the folder open, the delete fails with *Kepler could not delete {path} because another program is using it. Close any editors, terminals or file explorers that have the folder open, then try again.*

Below the worktree, a live check shows what deleting would cost. Kepler reads this from the worktree when the dialog opens. When you tick **Also delete branch**, the check runs again, because deleting the branch can lose different work. Each worktree has short tags that show what you could lose:

| Tag | What it means |
|---|---|
| *{count} uncommitted files* | Changes that exist only in this working copy |
| *{count} commits not on any remote* | Commits on the branch that were never pushed. Kepler counts them before it deletes anything |
| *Detached HEAD* | Commits that are not on any branch |
| *In open PR #{prNumber}*, *Merged in PR #{prNumber}*, *Merged into {base}*, *Pushed* | The branch's commits are stored somewhere else, so deleting the branch loses nothing |
| *No uncommitted changes* | Nothing to lose |

Kepler treats a branch that was merged through a rebase merge or a squash merge as merged. When you clean up such a branch, Kepler does not warn about commits that are already in its target.

Kepler **keeps** a worktree that would lose work, unless you tick the extra box that names the worktree and what it would lose: *Also delete {branch}, losing {what}*. Without that confirmation, Kepler refuses the delete. Whatever requests the delete, Kepler never deletes uncommitted or unpushed work without your confirmation.

***

## Renaming, archiving, and deleting a task

<figure style="text-align:center">
  <a href="/wp-content/uploads/rename-task-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/rename-task-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Task actions menu of the Fix the cart total row, unread with a New reply, with Rename task highlighted among Open task page, Progress (In Development), Mark as read, Add to group, Copy task link, Copy task prompt, Add resource…, Refresh, Shut down all agents, Archive task and Delete task.">
  </a>
  <figcaption style="text-align:center; color:#888">The Task actions menu, open from a task's row.</figcaption>
</figure>

To rename, archive or delete a task, open the **Task actions** (**⋮**) menu on the task's row or in the task page's header. The menu has these actions:

| Action | What it does |
|---|---|
| **Mark as read** / **Mark as unread** | **Mark as read** appears while any of the task's sessions is unread, and marks them all read. Otherwise the menu offers **Mark as unread** |
| **Rename task** | Turns the name, which Kepler set when you created the task, into a field (on the task page, double-clicking the name does the same). **Auto-name** puts a suggestion based on the task's prompt and resources into the field, for you to accept or edit |
| **Add to group** | Puts the task in one of [your groups](/kepler/arranging-your-work#your-groups), starts a **New group…** with it, or offers **Remove from group** when the task is in a group. A task with sub-tasks also offers **Group with its {count} sub-tasks**, and an archived task does not offer **Add to group** |
| **Copy task link** | Copies a Kepler link to the task. **Cmd/Ctrl+C** on a focused task row also copies it |
| **Refresh** | Reads the task's worktrees and its pull request and issue links again. For a short time after a refresh, Kepler cannot read the providers again, so the row is locked and says when you can try again |
| **Archive task** | Removes the task from the active list and keeps it as history. Kepler keeps its sessions and resources, and deletes nothing unless you ask it to |
| **Restore task** | Replaces **Archive task** on an archived task, and returns it to the active list, even when another active task holds the same pull request (several tasks can share one). The task stays in its group, and restores the group too if the group was archived |
| **Delete task** | Removes the task along with its sessions and resources |

**Kepler suggests archiving a finished task.** When a task meets all of these conditions, its header asks *Ready to archive?* with an **Archive** button:

- The task is at **Done**.
- Its worktrees have no unpushed work.
- No session is still working, waiting on you, or running background work.

If you dismiss the suggestion, Kepler stops suggesting it for that task.

**Archive** and **Delete** open the same dialog, with the same 3 checkboxes for the task's worktrees and branches. Each box stays unavailable until you tick the one above it, and Kepler remembers your choices for next time:

- **Also delete worktrees**
- **Also delete branches**
- **Also delete the branch on the remote**

Until you tick a box, the dialog reads *Worktrees and branches stay on disk unless you tick the boxes below.* When you tick **Also delete worktrees**, Kepler lists every worktree with the same tags that a single worktree delete shows, and says what will happen to each:

- Kepler deletes a worktree that is safe to delete.
- Kepler **keeps** a worktree that would lose work, *because deleting it would lose work*, unless you tick the box that names the worktree and confirms the loss.
- Kepler lists a worktree it cannot delete with the reason: another task still uses it, it is the repository's main worktree, a session still runs in it, or it is already gone from disk.

When you tick **Also delete branches**, Kepler checks the list again, so a worktree that was safe can now show a warning. If the check is slow, you can confirm anyway. Kepler still keeps any worktree that would lose work.

When **Also delete the branch on the remote** is ticked, Kepler deletes each branch's remote copy after it deletes the local branch. Kepler keeps the remote branch if deleting it could lose something, and a *Kept a branch on the remote* notice gives the reason:

- The branch has an open pull request.
- The branch has commits that are not on the remote.
- The remote has commits that this branch does not have.
- The remote branch changed after Kepler checked it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/archive-task-dialog-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/archive-task-dialog-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Archive task? dialog for Upgrade the payment SDK, saying the task moves to the Archived section, its sessions and resources are kept, it can be restored any time, and its worktrees and branches stay on disk unless you tick the boxes below. Also delete worktrees is unticked, and Also delete branches and Also delete the branch on the remote are unavailable until the box above each is ticked. Cancel and Archive task close the dialog.">
  </a>
  <figcaption style="text-align:center; color:#888">The Archive task? dialog, before you tick anything.</figcaption>
</figure>
<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-archive-task-worktrees-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-archive-task-worktrees-01-v3@2x.png" class="help-center-img img-bordered" alt="The Archive task? dialog for Upgrade the payment SDK with Also delete worktrees and Also delete branches ticked, and Also delete the branch on the remote unticked. Its Worktrees and branches list reads 1 of 2 will be deleted: kepler/payment-sdk-v5, with 1 uncommitted file, is kept because deleting it would lose work, and kepler/payment-sdk-docs, with no unpushed commits, will be deleted. Below it, an unticked box offers to also delete kepler/payment-sdk-v5, losing 1 uncommitted file.">
  </a>
  <figcaption style="text-align:center; color:#888">The same dialog with worktrees and branches ticked: one worktree goes, one is kept.</figcaption>
</figure>

**Restore task** appears in the task page's header as soon as you archive the task. On a row in the main list, it appears only after you filter **Activity** to **Archived**. See [Arranging Your Work](/kepler/arranging-your-work).

To archive or restore a single session, use the session's own menu in the context panel.

***

## What an agent can do with a task's resources

Agents work with tasks through Kepler's own MCP server, `kepler-workspace`. With its tools, an agent can keep the task's resources up to date for you, and can find and coordinate with the rest of your work.

<div class="note" markdown="1">

**The workspace tools were renamed in Kepler 0.15.** Each tool is now named for what it acts on, then what it does, such as `task_get` or `worktree_create`. If an agent's settings allow-list `mcp__kepler-workspace__` tools by name, update them to the names below.

</div>

The tools refer to things by id, and each id starts with its kind: `task:`, `session:`, `repo:`, `worktree:`, `folder:`, `note:`, `file:`, `account:`, `group:` and `comment:`. If you paste a Kepler link to a task or a session into the chat, the agent can use it as the id. Wherever a tool takes a repository, the agent can also name the repository by one of its **Aliases**, which you set on the repository's page in **Settings → Repositories**. See [Settings](/kepler/settings-repositories#edit-a-repository).

**Reading tasks and notes**

| Tool | What it does |
|---|---|
| `task_get` | Read a task: its stage, group, worktrees and folders, notes, files, links, related tasks, newest sessions, and how many of your review comments are still open. On the agent's own task, later calls return only what changed, and `refresh` first reads the pull request and issue state, the disk and Git again |
| `task_list` | Find tasks by name, prompt, note text or file name, filtered by stage, hold, repository, [group](/kepler/arranging-your-work#your-groups), or whether they belong to the agent's own work. Each task shows its group, the first page lists every group you have, including empty ones, and archived tasks appear only on request |
| `task_note_read` | Read one note's full text. Otherwise, notes arrive as references (title and size) |
| `task_comment_read` | Read the open [review comments](/kepler/review-changes#review-comments) you sent on a task's code (those still waiting on an agent's answer first, each with its file, lines, the code it is on, and its replies), or read one comment by id, resolved or not. Comments you have not sent cannot be read |

**Finding sessions, agents and places**

| Tool | What it does |
|---|---|
| `session_list` | Find agent sessions by name, task, agent or place, with each session's state and what it is waiting on: a permission, an answer, or an approval. It can list only the sessions that need you |
| `session_read` | Read another session's conversation, at the level of detail the agent asks for, by its id or a link from **Copy session link**. It returns the newest messages, or only the last reply with `limit:1`, and reports what a running session waits on, including a plan it is holding for your review |
| `agent_list` | List the agents, accounts, models and effort values a new session can start with, and the modes each agent supports |
| `repo_list` | List the repositories and folders where work can happen, and mark the ones this task uses. It finds one by name, path or alias |

**Notes, links and files**

| Tool | What it does |
|---|---|
| `task_note_write` | Create a note, or edit one: replace the whole note, replace the section under one heading, or add to the end. A replace includes the version the agent last read, so if the note changed since then, Kepler refuses the replace rather than overwriting the note |
| `task_note_delete` | Delete a note. The task's **Prompt** cannot be deleted |
| `task_comment_reply` | Reply on a review comment you sent, so the answer shows on the comment's card in Kepler, and resolve the comment once the request is done. You can reopen it |
| `task_link_update` | Attach or detach issue, pull request and other links, which Kepler classifies, fetching each one's title and status when it can. An agent that starts a server for you to open (a dev server, Storybook, a preview) attaches its local URL to the task, and detaches it when it stops the server for good |
| `task_file_attach` | Attach files by path, linked rather than copied. The agent can instead attach a file it wrote in a temporary folder as a copy saved with the task, up to 10 MiB |
| `task_file_detach` | Detach files. A linked file stays on disk, and an uploaded copy is deleted |

**Worktrees**

| Tool | What it does |
|---|---|
| `worktree_create` | Create a worktree on a new branch and bind it to the task. The branch starts from the repository's remote default branch or from a base the agent names |
| `worktree_attach` | Bind a worktree or folder that already exists on disk to the task, without changing any files |
| `worktree_detach` | Remove a binding without touching the worktree, the branch, the files, or the sessions running there. The agent cannot detach the task's own folder or the place it runs in |
| `worktree_update` | Record a new merge target after the agent rebased a stacked branch or moved it onto another branch. A merge target you saved yourself takes precedence |
| `worktree_delete` | Delete a worktree from disk. Its branch goes too when Kepler finds it merged; an unmerged branch is kept unless the agent asks to delete it |

Where AI Sync and AI Compose are turned on, the `sync_*` and `compose_*` tools also let an agent update a branch from its base with a rebase or merge, and reorganize its commits. See [Review Changes](/kepler/review-changes#agent-tools-ai-sync-and-ai-compose).

**Progress and lifecycle**

| Tool | What it does |
|---|---|
| `task_create` | Create a *separate* task beside this one, with its own prompt, places, notes, links and files, for work that needs its own tracking. Kepler links it back to this task (as a sub-task, parent, follow-up, or related task), nothing starts on it, and it can go into a group, which is created if the name is new |
| `task_update` | Set the stage your board shows (**Exploration**, **In Development**, **In Review**, **Done**), put the task on hold or lift the hold, rename it, move it into or out of a group (a new name creates the group), restore it from the archive, or let Kepler set the stage again from Git and pull requests. If it replaces a stage or a hold you set, it tells you |
| `task_archive` | Archive a task. Archiving alone stops nothing and deletes nothing, and with cleanup, it also deletes the task's worktrees and their merged branches |

**Starting and coordinating work**

| Tool | What it does |
|---|---|
| `session_start` | Start an agent session on a task, as the starting session's child (a delegate, a reviewer, or a handoff), and send it a first message, in a place the agent names or in a new worktree. It uses the same agent, account, model, mode and effort unless the agent picks others from `agent_list`, and it can start without the task's context, as a reviewer would |
| `session_send` | Send another session a prompt to act on, or a message for its inbox. A session reports back to the session that started it with a status (progress, done, blocked or failed), and can also stop the other session's running turn |
| `session_update` | Rename a session. Sessions that run in the terminal or outside Kepler cannot be renamed |
| `session_archive` | Archive a session: its history stays and its agent stops. A session cannot archive itself |
| `inbox_read` | Read this session's inbox, or wait up to 60 seconds for reports from the sessions it started |
| `approval_list` | List every request waiting on your approval. It cannot approve or deny anything |
| `theme_get` / `theme_save` | Read Kepler's theme format, then check a theme file and install it into the themes folder |

### What runs at once, and what asks you

Every workspace tool is pre-approved, in Chat and in Terminal, so none of them shows the agent's own permission prompt. Instead, Kepler decides which requests can run at once.

An agent works freely within its own work. Its own work is its own task, plus the tasks and sessions it created or started sessions on. These requests run at once:

- Reads, anywhere.
- Creating a task, a note or a worktree.
- Changes inside the agent's own work, except changes that can lose something.

These requests wait for your approval:

- Sending a prompt to any session other than one the agent started itself, or a message to a session outside its own work
- Stopping or renaming a session outside its own work, or archiving any session other than one it started
- Changing a task outside its own work: its stage, hold, name, group, links or notes, or detaching its files. A group change reads on the card as *Put it in the group "{name}"*, *Create the group "{name}" and put it there*, or *Take it out of its group*
- Changing a Kepler setting that affects your accounts, privacy, other tools, what runs, or where files go. Only [Ask Kepler](/kepler/ask-kepler) can change settings, never a task's agent. The card names the setting and its change, *From {from} to {to}*, and offers no wider approval, so you approve each change on its own. See [Approval requests](/kepler/agent-sessions#approval-requests)
- Deleting any note
- Detaching an uploaded file, because Kepler deletes its saved copy
- Archiving a task outside its own work or with other live sessions, and any archive that also deletes worktrees
- Deleting a worktree that has something to lose (uncommitted changes, unpushed commits on a branch being deleted, commits on a detached HEAD, a status Kepler cannot read), or that another task is bound to
- Starting a session in a more permissive mode than the agent's own, or on a task outside its own work
- Overwriting a theme file when there is no Trash to keep the old one
- The AI Sync and Compose tools that change a repository or rewrite its history

Kepler compares modes on 3 levels, plan, edit and auto, and maps them onto each agent's own permission modes. A session that an agent starts cannot run in a higher mode than the session that started it unless you approve. The request says *More permissive than the asking session, which is in {mode} mode.*

The request appears as an approval card above the asking session's composer, with **Approve** and **Deny**. The **Approve** menu can approve every request of that kind from the session, or always. A rule you make with **Always approve** is listed under **Settings → Agents → Approvals**, where **Remove** deletes it. **Always approve** is not offered for actions that can lose work. See [Agent Sessions](/kepler/agent-sessions#when-the-agent-asks-you-something).

The agent does not wait for you to answer the card. Kepler tells the agent the request is awaiting your approval, the agent continues, and the outcome arrives in its inbox. Before an approved request runs, Kepler checks again. If the target changed in the meantime, such as a worktree that has new commits, nothing runs.

`worktree_delete` has the same protection as your own delete. It refuses while a live session is running in the worktree, including the agent's own session. A worktree it deletes stays on the task, marked as gone, until someone detaches it.

### Reports between sessions

Each session has an **inbox** for what other agents send it:

- Reports and messages
- Changes in the state of a session it started
- The outcomes of its approval requests

When an item arrives for an idle session, Kepler wakes the session to read it. A busy session reads it when its turn ends. Kepler wakes sessions running in Terminal the same way. A session whose agent cannot reach Kepler's workspace tools does not receive state changes.

A session with unread reports has a badge with their count on its tab and on its row in the context panel. To have the agent read them now, click **Have it read them** above its composer.

Agents that keep waking each other can loop. To stop a loop, after 20 turns started by agents rather than by you, reports stop waking the session. The session reads *Reports from other agents are paused*. To turn wakes back on, click **Resume reports**, or send the session a message of your own.

---
