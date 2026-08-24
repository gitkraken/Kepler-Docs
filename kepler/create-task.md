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
last_verified: 2026-08
llms_include: true
tags: [tasks, create-task, composer, worktrees, issues, pull-requests, actions]
taxonomy:
  category: kepler
---
<kbd>Last updated: August 2026</kbd>

Kepler gives you two ways to start work, and the first is usually better: pick something that's already waiting for you.

| Start from | How |
|---|---|
| **Work assigned to you** | Fire an Action on an issue or pull request in the **Todo** segment of [the Kepler interface](/kepler/kepler-interface). One click, context attached |
| **Something you're describing yourself** | **New task** opens the Task Composer, where you write the prompt and attach what it needs |

***

## From an issue or pull request

<figure>
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

Click **New task**, or press **Shift+Alt+T** to open the quick launcher from anywhere, including when Kepler isn't the focused window.

<figure>
  <a href="/wp-content/uploads/new-task-button-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-button-aug-2026.png" class="help-center-img img-bordered" alt="The New task button in the Kepler top navigation bar">
  </a>
  <figcaption style="text-align:center; color:#888">The New task button, available from anywhere in Kepler.</figcaption>
</figure>

The Composer is one prompt box above a row of four buttons:

<figure>
  <a href="/wp-content/uploads/new-task-composer-add-buttons-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-composer-add-buttons-aug-2026.png" class="help-center-img img-bordered" alt="The Composer's four buttons: Add repo, Add issue, Add PR, and Add context">
  </a>
  <figcaption style="text-align:center; color:#888">The Composer's four attach buttons.</figcaption>
</figure>

| Control | What it attaches |
|---|---|
| **Add repo** → **Repos** | A repository to work in |
| **Add issue** → **Issues** | Issues from your connected trackers |
| **Add PR** → **PRs** | Pull requests from your connected hosts |
| **Add context** | Everything without a button of its own: folders, files, and links |

Add as much or as little context as you wish. 

1. Write the prompt: *Describe a task or ask a question…*
2. Attach what it needs, or nothing (which is fine!)
3. Configure each repository (below), if you attached one.
4. Start it.

**The Composer remembers the repositories you last started a Task with** and stages them again the next time you open it. That way, you don't have to re-pick a repository you work in every day. Kepler remembers only the repositories (the branch and worktree settings reset to their defaults), and starting from an issue or a pull request never overwrites the remembered set. Kepler drops a repository that no longer exists rather than staging it.

The primary button fires the Action that matches what you've attached, exactly as it would from a Todo row. A linked pull request resolves to **Address Feedback** or **Review**, depending on who wrote it; a linked issue resolves to **Plan**. With nothing attached, the button reads **Start** and starts the Task with your prompt as written.

The chevron beside the primary button opens the rest: **Prepare**, which creates the session without starting work yet, and every Action that applies to what you've attached. Firing an Action sends that Action's prompt, with anything you typed appended as a refinement.

If the Task can't start, you'll see **Failed to start the task**.

### Configuring a repository

Each attached repository gets a chip with two controls:

<figure>
  <a href="/wp-content/uploads/isolated-worktree-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/isolated-worktree-aug-2026.png" class="help-center-img img-bordered" alt="A repository chip with its base branch and Isolated worktree controls">
  </a>
  <figcaption style="text-align:center; color:#888">A repository chip, with its base branch and Isolated worktree controls.</figcaption>
</figure>

- **Base branch**: the branch segment of the chip. By default, the Task gets a new branch forked from **the repository's remote default branch**, which is what the chip reads until you pick something: *New branch off origin's default branch, or the current branch if unavailable*. Open it to fork off a different branch instead, or to work directly on an existing one. A new branch takes its name from the Task name.
- **Isolated worktree**: the worktree segment, a direct on/off toggle rather than a menu. On by default, giving the Task its own working copy. Turning it off means the Task shares your repository folder, and anything that switches that folder's branch switches the Task's branch too. See [Tasks and Resources](/kepler/tasks-and-resources).

Kepler intentionally forks from the remote by default. If no remote default resolves (no remote, a shallow clone, or no network connection), Kepler falls back to the current HEAD rather than failing the launch.

A repository linked to a pull request always opens in its own isolated working copy, and the toggle is locked: *This repository is linked to a pull request and always opens in its own isolated working copy.*

Kepler clones a repository you haven't cloned yet when the Task starts, into your **Default Repositories Folder**: *This repository is cloned when you start the task.* Its branch is locked until then — *its branches become available after cloning* — because Kepler doesn't yet know what branches it has, and the chip reads **default branch** in the meantime.

Attaching the same repository twice gives the Task two independent worktrees on it: useful for comparing two approaches, or a mistake if you didn't mean it. Two chips that would resolve to the *same* worktree get a **Duplicate worktree** marker instead, and Kepler creates only one of them. If a chip works in place on a branch another chip has already claimed for an isolated worktree, Kepler marks it **Superseded by a worktree** and skips it; git can't check one branch out in two places.

***

## From nothing at all

Attach nothing. No repository, no branch, no issue. You get somewhere to think (ask a question, explore an idea) and you can attach the real work later, once it's worth tracking. See [The Task View](/kepler/task-view).

<figure>
  <a href="/wp-content/uploads/new-task-composer-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-composer-aug-2026.png" class="help-center-img img-bordered" alt="The Task Composer with a prompt typed in and Add repo, Add issue, Add PR, and Add context buttons, nothing attached yet">
  </a>
  <figcaption style="text-align:center; color:#888">The Task Composer, ready to attach a repo, issue, pull request, or other context.</figcaption>
</figure>

***

## After the Task starts

The Task appears in **Tasks in progress**. Click it for the side panel, or double-click to open [the task view](/kepler/task-view).

<figure>
  <a href="/wp-content/uploads/full-task-view-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/full-task-view-aug-2026.png" class="help-center-img img-bordered" alt="The task view with the rail on the left, listing Sessions, Changes, Folders, Pull requests, Links, and Notes, and a session open on the right with tool-call approval prompts">
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
