---
title: Create a Task
description: Start a Task from an issue, a pull request, or nothing at all — with the repository, branch, and context already attached.
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

There are two ways to start work in Kepler, and the first one is usually better: pick something that's already waiting for you.

| Start from | How |
|---|---|
| **Work assigned to you** | Fire an Action on an issue or pull request in the **Todo** segment of [the Kepler interface](/kepler/kepler-interface). One click, context attached |
| **Something you're describing yourself** | **New task** opens the Task Composer, where you write the prompt and attach what it needs |

<!-- TODO(screenshot): the Task Composer with a repo and an issue attached. -->

***

## From an issue or pull request

This is the shortest path, and it's the reason Kepler opens on your work. Find the item in **Todo**, click its **Action** button, and Kepler creates the Task, attaches the repository and the item, sets up a worktree, and starts an agent with the context in place.

Defaults are **Plan** for an issue, **Address Feedback** for a pull request you authored, and **Review** for someone else's — all editable. See [Actions](/kepler/actions).

Tasks are named automatically from what you started them with. Rename one whenever the name stops fitting — **Rename task** in the **⋮** menu, whose field also has an **Auto-name** button that suggests a name from the Task's prompt and resources. See [Tasks and Resources](/kepler/tasks-and-resources).

***

## From the Task Composer

Click **New task**, or press **Shift+Alt+T** to open the quick launcher from anywhere — including when Kepler isn't the focused window.

The Composer is one prompt box above a row of four buttons:

| Control | What it attaches |
|---|---|
| **Add repo** → **Repos** | A repository to work in |
| **Add issue** → **Issues** | Issues from your connected trackers |
| **Add PR** → **PRs** | Pull requests from your connected hosts |
| **Add context** | Everything without a button of its own — folders, files, and links |

The first three read **Add …** while empty and switch to the plural with a count once they hold something. **Add context** always reads the same, because it isn't a category waiting to be filled. Picks accumulate — attach three repositories and two issues to the same Task if that's the shape of the work.

1. Write the prompt: *Describe a task or ask a question…*
2. Attach what it needs, or nothing.
3. Configure each repository (below), if you attached one.
4. Start it.

**The Composer remembers the repositories you last started a Task with** and stages them again the next time you open it, so a repository you work in every day doesn't have to be re-picked every time. Only the repositories are remembered — the branch and worktree settings reset to their defaults — and starting from an issue or a pull request never overwrites the remembered set. A repository that no longer exists is dropped rather than staged.

The primary button fires the Action that matches what you've attached — a linked pull request resolves to **Address Feedback** or **Review** by who wrote it, a linked issue to **Plan** — exactly as it would from a Todo row. With nothing attached it reads **Start**, and starts the Task with your prompt as written.

The chevron beside it opens the rest: **Prepare**, which creates the session without starting work yet, and every Action that applies to what you've attached. Firing an Action sends that Action's prompt, with anything you typed appended as a refinement.

If it can't start you'll see **Failed to start the task**.

### Configuring a repository

Each attached repository gets a chip with two controls:

- **Base branch** — the branch segment of the chip. Leave it alone and the Task gets a new branch forked from **the repository's remote default branch**, which is what the chip reads until you pick something: *New branch off origin's default branch, or the current branch if unavailable*. Open it to fork off a different branch instead, or to work directly on an existing one. A new branch takes its name from the Task name.
- **Isolated worktree** — the worktree segment, a direct on/off toggle rather than a menu. On by default, giving the Task its own working copy. Turning it off means the Task shares your repository folder, and anything that switches that folder's branch switches it for the Task too. See [Tasks and Resources](/kepler/tasks-and-resources).

Forking off the remote default is the point, not an implementation detail: the branch you happen to have checked out is rarely where new work belongs, and it used to be where it landed. If no remote default resolves — no remote, a shallow clone, offline — Kepler falls back to the current HEAD rather than failing the launch.

A repository linked to a pull request always opens in its own isolated working copy, and the toggle is locked: *This repository is linked to a pull request and always opens in its own isolated working copy.*

A repository you haven't cloned yet is cloned when the Task starts, into your **Default Repositories Folder**: *This repository is cloned when you start the task.* Its branch is locked until then — *its branches become available after cloning* — because Kepler doesn't yet know what branches it has, and the chip reads **default branch** in the meantime.

Attaching the same repository twice gives the Task two independent worktrees on it — useful for comparing two approaches, and a mistake if you didn't mean it. Two chips that would resolve to the *same* worktree get a **Duplicate worktree** marker instead, and only one of them is created. A chip working in place on a branch another chip has claimed for an isolated worktree is marked **Superseded by a worktree** and skipped, because git can't check one branch out in two places.

***

## From nothing at all

Attach nothing. No repository, no branch, no issue. You get somewhere to think — ask a question, explore an idea — and you can attach the real work later, once it's worth tracking. See [The Task View](/kepler/task-view).

***

## After it starts

The Task appears in **Tasks in progress**. Click it for the side panel, or double-click to open [the task view](/kepler/task-view).

From there you can add more sessions, attach more resources, and review what the agent changed. See [Agent Sessions](/kepler/agent-sessions) and [Review Changes](/kepler/review-changes).

### Context: what gets handed to the agent

Both paths send the same Action prompt, but they attach different amounts of detail:

| Started from | What the agent receives |
|---|---|
| **A row in Todo** | The full issue or pull request body, attached as shared context |
| **The Task Composer** | A reference — identifier, title, and URL — which the agent fetches the detail from itself |

---
