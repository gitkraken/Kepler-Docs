---
title: Create a Task
description: Start a Task from an issue, a pull request, or nothing at all, with the repository, branch, and context already attached.
product: Kepler
feature: Tasks
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
integrations: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops, jira, linear, trello]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [tasks, create-task, composer, worktrees, branches, folders, issues, pull-requests, actions, gitlens, gitkraken-desktop]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Kepler gives you several ways to start work, and the first is usually better: pick something that's already waiting for you.

| Start from | How |
|---|---|
| **Work assigned to you** | Fire an Action on an issue or pull request in the **Todo** segment of [the Kepler interface](/kepler/kepler-interface). One click, context attached |
| **Something you're describing yourself** | **New task** opens the Task Composer, where you write the prompt and attach what it needs |
| **A conversation you already started** | **New task → New task from an external session** wraps a task around an agent session you began in your own terminal |
| **Another GitKraken app** | A link from GitLens or GitKraken Desktop opens Kepler on the work you were looking at |

***

## From an issue or pull request

<figure style="text-align:center">
  <a href="/wp-content/uploads/action-button-todo-row-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/action-button-todo-row-aug-2026.png" class="help-center-img img-bordered" alt="The Action split button on a Todo row, reading Plan">
  </a>
  <figcaption style="text-align:center; color:#888">The Action button on a Todo row.</figcaption>
</figure>

This is the shortest path, and the reason Kepler opens on your work. Find the item in **Todo** and click its **Action** button. Kepler then:

1. Creates the Task.
2. Attaches the repository and the item.
3. Sets up a worktree.
4. Starts an agent with the context in place.

Defaults depend on what you're acting on:

- **Plan** for an issue.
- **Address Feedback** for a pull request you authored.
- **Review** for someone else's pull request.

All of these are editable. See [Actions](/kepler/actions).

Kepler names Tasks automatically from what you started them with. Rename one whenever the name stops fitting: **Rename task** in the **⋮** menu, whose field also has an **Auto-name** button that suggests a name from the Task's prompt and resources. See [Tasks and Resources](/kepler/tasks-and-resources).

<div class="note" markdown="1">

**Nothing in Todo?** Set up your [issue tracker](/kepler/issue-tracker-integrations) and [pull request](/kepler/pull-request-integrations) integrations in **Settings** first. Kepler can only populate Todo with work from connected accounts.

</div>

***

## From the Task Composer

Click **New task** or press **Cmd/Ctrl+N**. To start one without switching to Kepler first, press **Shift+Alt+N** to open the quick launcher from anywhere, including when Kepler isn't the focused window.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-button-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-button-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The New task split button at the left end of the Kepler top bar, after the application menu, the window switcher and the Back and Forward buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">The New task button, available from anywhere in Kepler.</figcaption>
</figure>

The Composer is one prompt box above a row of four buttons:

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-composer-add-buttons-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-composer-add-buttons-sep-2026.png" class="help-center-img img-bordered" alt="The Composer's four buttons: Add repo or folder, Add issue, Add PR, and Add context">
  </a>
  <figcaption style="text-align:center; color:#888">The Composer's four attach buttons.</figcaption>
</figure>

| Control | What it attaches |
|---|---|
| **Add repo or folder** | A repository to work in, or a plain folder |
| **Add issue** → **Issues** | Issues from your connected trackers. With only Linear in the list, a team picker shows every open issue in the team you pick, not just yours |
| **Add PR** → **PRs** | Pull requests from your connected hosts |
| **Add context** | Everything without a button of its own: folders, files, and links |

In a window connected to another machine, picking a file through **Add context** also offers **Upload from this machine**. Uploads are kept with your draft and saved into the Task's own folder when it starts; if one expired before you pressed **Start**, Kepler names it rather than dropping it silently.

**Repositories and folders come from one ranked list**, not two pickers (*Find a repository or folder…*), and the list learns. Kepler records how often you actually use each place and ranks the picker by it, so the repositories you work in daily are at the top on the day you start using them. The same list is behind the chip's own **Change repository or folder**. Picking a folder that is one of a repository's existing worktrees attaches that worktree itself, and the chip reads **Worktree {branch}**. If the worktree disappears before the Task starts, the chip reads **Worktree not found**; pick the repository again to choose another working copy.

Add as much or as little context as you wish. 

1. Write the prompt: *Describe a task or ask a question…*
2. Attach what it needs, or nothing (which is fine!)
3. Configure each repository (below), if you attached one.
4. Start it.

**The Composer remembers the repositories you last started a Task with** and stages them again the next time you open it. That way, you don't have to re-pick a repository you work in every day. Kepler remembers only the repositories (the branch and worktree settings reset to their defaults), and starting from an issue or a pull request never overwrites the remembered set. Kepler drops a repository that no longer exists rather than staging it.

**It also remembers an unsent draft.** Closing the dialog with a prompt half written keeps it, so reopening picks up where you left off. A Task you have genuinely started writing confirms before it's discarded rather than vanishing on a stray Escape.

**Kepler remembers which repositories you pick for a tracker project too.** Attach a Jira, Linear, or Azure issue and the repositories you chose for that project last time are preselected, marked **Suggested from this tracker project** or **From history** depending on whether the tracker said so or Kepler inferred it from where that project's issues were worked before.

The primary button shows a sending state from the moment you click it, so a slow start doesn't read as a dead button. It fires the Action that matches what you've attached, exactly as it would from a Todo row. A linked pull request resolves to **Address Feedback** or **Review**, depending on who wrote it; a linked issue resolves to **Plan**. With nothing attached, the button reads **Start** and starts the Task with your prompt as written.

The chevron beside the primary button opens the rest: **Prepare**, which creates the session without starting work yet, and every Action that applies to what you've attached. Picking one doesn't fire it here: it relabels the primary button, and an Action that names its own agent puts that agent in the agent pill, so you can check or change what will run before you press the button. The Action sends its prompt, with anything you typed appended as a refinement.

A Task that has its prompt but no session yet, such as one an agent created for you, says so in a draft session tab: *Start with the task prompt, or describe something else…*. To send the Task's prompt as written, press **Start** on the empty box.

The Task appears in the list as soon as you press **Start**, before its worktrees exist. Until setup finishes, the row carries a **Preparing** pill, and the Task's panel shows its progress under **Getting your task ready**, such as *Cloning {repo}…* or *Setting up worktrees…*. **Cancel** stops a launch while a repository is still cloning. When the new branch is being updated from its base, the session area reads **Preparing branch**: *Updating from the base branch before the session starts.*

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-task-preparing-row-01.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-task-preparing-row-01-v2@2x.png" class="help-center-img img-bordered" alt="The Recent group of Tasks in progress: Write the 2.4 release notes, then a new task, Add a gift-card field to checkout, with acme-web, the Preparing pill and its spinner.">
  </a>
  <figcaption style="text-align:center; color:#888">A new task in the list while Kepler prepares it.</figcaption>
</figure>

If setup fails, the row's pill reads **Failed** and the panel reads **Couldn't start this task**. To change the Task and try again, click **Edit and retry**, or **Dismiss** to clear it. A launch you cancelled reads **Task not started**. If the request itself can't be sent, you see **Failed to start the task**. A Task that starts without some of its repositories warns *Some repositories weren't added: The task started without {repos}.*

If the Task starts but its agent session doesn't, the task page and the Dashboard panel show **{agent} couldn't start**, with **Retry**. See [Agent Sessions](/kepler/agent-sessions#when-a-session-drops).

### Configuring a repository

Each attached repository gets a chip with three segments:

<figure style="text-align:center">
  <a href="/wp-content/uploads/composer-repo-chip-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/composer-repo-chip-sep-2026.png" class="help-center-img img-bordered" alt="Two repository chips, each with its base branch, an editable branch name, and the Isolated worktree checkbox">
  </a>
  <figcaption style="text-align:center; color:#888">A repository chip, with its base branch and Isolated worktree controls.</figcaption>
</figure>

- **Base branch**: the branch segment of the chip. By default, the Task gets a new branch forked from **the repository's remote default branch**, which is what the chip reads until you pick something: *New branch off origin's default branch, or the current branch if unavailable*. Open it to fork off a different branch instead, to work directly on an existing one, or to take the repository's **current** branch in place.
- **Branch name**: the new branch's own name, suggested from your prompt as you type and editable in place. See below.
- **Isolated worktree**: the worktree segment, a direct on/off toggle rather than a menu. On by default, giving the Task its own working copy: *Runs in its own working copy of the repository*. Turning it off means the Task shares your repository folder: *Uses the repository's own folder, so a branch switch here moves your checkout*. See [Tasks and Resources](/kepler/tasks-and-resources).

**What a newly attached repository starts on is a setting.** These three segments open on **Settings → Tasks → New tasks → Where new tasks make changes**: **Isolated worktree** (the default), **New branch**, or **Current branch**. Changing it changes the starting point only; every segment above still overrides it per repository, per Task. See [Settings](/kepler/settings).

Picking **New branch** or **Current branch** means the Task runs in the repository's own checkout rather than an isolated one, so only one Task can use that checkout at a time. If another Task already has it, the chip shows an **Another task is working here** card naming that Task and why, such as *Both would edit the same files.*, with **Create a worktree for this task** to put this one repository in an isolated worktree instead.

### Naming the branch

Kepler names a Task's branch from what the Task is actually about, rather than from the Task's name alone.

- **The name is suggested from your prompt** and appears on the chip as you type: *Suggested from your prompt. Click to edit.* Clicking it opens the field (**Enter keeps, Esc restores the suggestion**), and an edited name reads *Named by you.*
- **An issue identifier leads the name** when the Task came from one, so `KEP-421-fix-the-import-path` rather than a slug with the ticket buried in it.
- **Automatic names are namespaced under `kepler/`.** That way a `git branch` listing in any other tool says where the branch came from, and a hand-made `feat/x` can never collide with one.
- **A name you type is yours verbatim.** The prefix applies to automatic names only, which is how a repository with an enforced `feat/` or `fix/` push rule still works.
- **Your repository's own branch-naming policy is applied** where the host publishes one.

You can set the prefix in two places: **Settings → Tasks → New tasks → Branch prefix** for the app, and per repository in **Settings → Repositories**, on the repository's own page. The repository's page offers **Default ({value})**, **None**, or **Custom**, and shows an example of what a branch will actually look like. Leave the app setting empty for no prefix at all. If a repository already has a branch literally named `kepler`, Kepler says so rather than creating an impossible ref: *This repository has a branch named {branch}, so the {prefix} prefix can't be used here.*

Kepler intentionally forks from the remote by default. If no remote default resolves (no remote, a shallow clone, or no network connection), Kepler falls back to the current HEAD rather than failing the launch.

A repository linked to a pull request always opens in its own isolated working copy, and the toggle is locked: *This repository is linked to a pull request and always opens in its own isolated working copy.* If the pull request's branch already exists on this machine with commits that aren't on the pull request, Kepler leaves that branch alone and starts the Task on a new branch tracking the pull request: *Kept your local branch {branch}*.

Kepler clones a repository you haven't cloned yet when the Task starts, into your **Repositories folder**: *This repository is cloned when you start the task.* Its branch is locked until then (*its branches become available after cloning*) because Kepler doesn't yet know what branches it has, and the chip reads **default branch** in the meantime.

Attaching the same repository twice gives the Task two independent worktrees on it: useful for comparing two approaches, or a mistake if you didn't mean it. Two chips that would resolve to the *same* worktree get a **Duplicate worktree** marker instead, and Kepler creates only one of them. If a chip works in place on a branch another chip has already claimed for an isolated worktree, Kepler marks it **Superseded by a worktree** and skips it; git can't check one branch out in two places.

***

## From a session you already started

You may have begun the work in a terminal before deciding it deserved tracking. The chevron on **New task** holds **New task from an external session** (*Continue a session you started outside Kepler*), which opens a picker over every agent conversation Kepler can see.

| Part | What it does |
|---|---|
| **Running now** | Sessions live in a terminal right now |
| **Past sessions** | Conversations found on disk, from whenever |
| **Find an external session…** | Searches across both groups |

The picker reports what it actually swept, rather than implying it found everything: **Showing the newest {shown} of {scanned} sessions** when it capped the list, **Couldn't list sessions from {adapters}** when one agent's scan failed but the others didn't, and, when detection is off, *External sessions are not detected* with **Turn on in Integrations**, which opens the setting.

### When a task already covers that folder

Kepler checks whether the conversation's working directory already belongs to a task, so you don't end up with two tasks over one folder:

> **Add to existing task?** *This conversation runs in {path}, which {task} already includes.*

**Add to task** binds the conversation there; **Create a new task** overrides. When several tasks include the folder, the dialog lists each as a card (*includes {path}*), marks the **closest**, and **Add to task** waits until you pick one. Recording the conversation on a task can take a minute, and Kepler says so rather than appearing to hang.

Because a task can be created in any plain folder, a conversation you had in a scratch directory can be adopted just like one in a checkout.

For what happens to the conversation once it's on a task (forking, continuing, and what Kepler will and won't answer on its behalf), see [Agent Sessions](/kepler/agent-sessions#sessions-started-outside-kepler).

***

## From a folder, or from nothing at all

**A Task doesn't need a repository.** Attach a plain folder from the same ranked picker and the agent works on it in place, with no branch, no worktree, and no Git at all. A folder of notes, a scratch directory, a checkout of something that isn't a repository: all of it is a normal Task.

When you browse for a folder in a window connected to another machine, Kepler opens its own folder picker (turn on **Always use the custom folder picker** in **Settings → General** to use it everywhere). Type a path into its path bar and Kepler checks it before you select it: a folder that doesn't exist, can't be read, or is actually a file is refused with the reason, and a near miss offers **Did you mean** the closest folder.

Or attach nothing. No repository, no folder, no issue. You get somewhere to think (ask a question, explore an idea) and you can attach the real work later, once it's worth tracking. See [The Task View](/kepler/task-view).

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-composer-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-composer-sep-2026.png" class="help-center-img img-bordered" alt="The Task Composer with a prompt typed in and Add issue, Add PR, Add context, and Add repo or folder buttons, nothing attached yet">
  </a>
  <figcaption style="text-align:center; color:#888">The Task Composer, ready to attach a repo, issue, pull request, or other context.</figcaption>
</figure>

***

## From another GitKraken app

You can jump into Kepler from other GitKraken products, such as GitLens and GitKraken Desktop. A link from one of them can open the Task Composer already filled in with the issue, pull request, or repository you were looking at, or open a task or session you already have. A link can also carry a prompt and an Action into the Composer, start a new session on a task you already have, and start right away rather than waiting for you to press **Start**. A link for an item a task already holds says *You already have a task for this item*, with **Open task**. If the repository isn't on this machine, Kepler stages it to be cloned when the task starts. A link Kepler can't fully resolve still opens, with one clear warning about what it couldn't use.

***

## After the Task starts

The Task appears in **Tasks in progress** right away, with the **Preparing** pill until its setup finishes. Click it for the side panel, or double-click to open [the task view](/kepler/task-view).

<figure style="text-align:center">
  <a href="/wp-content/uploads/full-task-view-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/full-task-view-oct-2026.png" class="help-center-img img-bordered" alt="The task page. Its header holds the task name, the ⋮ menu, the In Development progress control, and Terminal at the right edge. The rail lists Sessions, Changes, Pull requests, and Notes led by Prompt, and a session on the right is waiting on a command approval.">
  </a>
  <figcaption style="text-align:center; color:#888">The task view: the rail on the left, a session open on the right.</figcaption>
</figure>

From there you can add more sessions, attach more resources, and review what the agent changed. See [Agent Sessions](/kepler/agent-sessions) and [Review Changes](/kepler/review-changes).

### Context: what gets handed to the agent

Both paths send the same Action prompt, but they attach different amounts of detail:

| Started from | What the agent receives |
|---|---|
| **A row in Todo** | The full issue or pull request body, attached as shared context |
| **The Task Composer** | A reference (identifier, title, and URL) which the agent fetches the detail from itself |

---
