---
title: Create a Task
description: Learn how to create Tasks in Kepler from scratch, from issues, or from pull requests, and how to manage them through completion.
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
last_verified: 2026-06
llms_include: true
tags: [tasks, create-task, worktrees, issues, pull-requests, kanban, shared-context]
taxonomy:
    category: kepler

<kbd>Last updated: June 2026</kbd>

## What is a Task?

A **Task** is the core unit of work in Kepler, GitKraken's Agentic Development Environment (ADE). A Task holds work across one or more repos.

Every Task contains:

- One or more **worktrees** — one Git worktree per repo
- One or more **agent sessions** — running coding agents within the Task
- A diff and changes view
- **Shared context** — standing instructions sent to every agent session in the Task

Tasks move through four stages on the Kepler board:

1. **Exploration**
2. **In Development**
3. **In Review**
4. **Done**

***

## Three ways to create a Task

Kepler gives you three starting points depending on where your work lives:

| Starting point | When to use |
|---|---|
| [From scratch](#creating-a-task-from-scratch) | You know the goal and don't need to pull context from an existing issue or PR. |
| [From an issue](#creating-a-task-from-an-issue) | You want Kepler to pull issue title, description, and metadata into the agent's context automatically. |
| [From a pull request](#creating-a-task-from-a-pull-request) | You want an agent to start a review or address open review comments on an existing PR. |

***

## Creating a Task from scratch

Start here when you have a clear goal and no existing issue or PR to pull context from.

1. Click **+ New task**.
2. Select one or more repos.
3. Choose **New worktree** or select an existing branch.
4. Set the base branch using the **From** dropdown. The dropdown is searchable; `origin/main` is labeled **DEFAULT**.
5. Optionally click **+ Add repo** to include additional repos in the same Task. Each repo gets its own worktree and base branch configuration.
6. Set **Agent**, **Mode**, **Model**, and **Effort** in the bottom bar.
7. Click **Launch task**.

<figure>
  <img src="..." class="help-center-img img-bordered" alt="New task creation screen showing repo selection, worktree options, and bottom bar settings" />
  <figcaption style="text-align: center; color: #888">Creating a Task from scratch: repo selector, worktree picker, base branch dropdown, and launch settings.</figcaption>
</figure>

### Settings reference

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Repo(s)** | Which repos are included in the Task | — | Any connected repo |
| **Worktree** | Whether to create a new Git worktree or use an existing branch | New worktree | New worktree, existing branch |
| **Base branch** | The branch the worktree is created from | `origin/main` | Any branch (searchable) |
| **Agent** | Which coding agent runs sessions in the Task | — | Configured agents |
| **Mode** | Agent operating mode | — | Depends on agent |
| **Model** | The underlying language model the agent uses | — | Available models |
| **Effort** | How much work the agent does before pausing for review | — | Low, Medium, High |

***

## Creating a Task from an issue

Use this path to have Kepler pass issue context (title, description, and metadata) to the agent automatically.

### Supported issue trackers

GitHub Issues, GitHub Enterprise, GitLab, GitLab Self-Hosted, Jira, Linear, Trello, Azure DevOps.

For integration setup, see [Issue Tracker Integrations](issue-tracker-integrations.md).

### Finding an issue

Use the search bar to find issues by title or by pasting a URL. Use the filter bar to narrow results:

- **Assigned to me / All visible** toggle
- **Provider** — filter by issue tracker
- **Repo** — filter by repository
- **Hide tasked** — hides issues that already have an active Task

### Launching Tasks from issues

1. Select one or more issues. Kepler creates one Task per issue.
2. In the Task preview row, confirm or change the **repo**, **worktree type**, and **base branch** for each Task.
3. Click **+ Add repo** on any Task row to span that Task across multiple repos.
4. Set **Agent**, **Mode**, **Model**, and **Effort** in the bottom bar. These settings apply to all Tasks being launched.
5. Review the summary (e.g., "3 issues → 3 tasks"), then click **Launch task**.

Kepler passes the issue title, description, and metadata to the agent when the session starts.

<figure>
  <img src="..." class="help-center-img img-bordered" alt="Issue selection screen showing filter bar, issue list, Task preview rows, and bottom bar" />
  <figcaption style="text-align: center; color: #888">Selecting issues to launch as Tasks. Each issue gets its own Task preview row.</figcaption>
</figure>

***

## Creating a Task from a pull request

Use this when starting a PR review or having an agent address open review comments.

### Supported PR providers

GitHub, GitHub Enterprise, GitLab, GitLab Self-Managed, Bitbucket, Azure DevOps.

For integration setup, see [Pull Request Integrations](pull-request-integrations.md).

### Finding a pull request

Use the search bar to find PRs by title or by pasting a URL. Use the filter bar to narrow results by **provider**, **repo**, or **Hide tasked**.

### Launching Tasks from a single PR

1. Select the PR.
2. In the Task preview, confirm the repo and the worktree branch Kepler will create (e.g., "Worktree will be created on `new-example-page`").
3. Set **Agent**, **Mode**, **Model**, and **Effort** in the bottom bar.
4. Click **Launch task**.

Kepler infers **"Address feedback"** as the agent's starting instruction from the PR diff, description, and open comments.

### Launching Tasks from multiple PRs

1. Select two or more PRs. Two options appear:
   - **Split into N tasks** — creates one Task per PR. Use this when each PR represents independent work.
   - **Group as 1 task** — places all PRs under a single Task. Use this when the PRs are related and you want a single agent to work across them.
2. Choose your grouping option.
3. Confirm the per-task repo selector in each Task preview row.
4. Set **Agent**, **Mode**, **Model**, and **Effort** in the bottom bar. The summary shows "N PRs → N tasks."
5. Click **Launch task**.

<figure>
  <img src="..." class="help-center-img img-bordered" alt="Pull request selection screen showing multi-PR grouping options and Task preview rows" />
  <figcaption style="text-align: center; color: #888">Selecting multiple PRs: split into separate Tasks or group under one Task.</figcaption>
</figure>

***

## Task detail: worktrees, sessions, and shared context

Once a Task is open, the Task header shows the Task name and the total worktree count (e.g., "5 worktrees").

### Worktrees

The **Worktrees** section lists every Git worktree in the Task with its branch name and repo.

### Sessions

The **Sessions** panel lists all agent sessions in the Task. Each entry shows the branch, repo, and a **NEW CONTEXT** badge when there is unread context.

### Shared context

**Shared context** is content you add to a Task that every agent session receives. Use it for standing instructions, style rules, or reference material that all agents should follow.

**Example:** "If a `.md` file has a date stamp, change it to June 2026." Adding this to shared context means every agent session in the Task follows the rule without you repeating it per session.

To manage shared context:

- Each piece of shared context appears as a **prompt card** showing the prompt text and version number (e.g., "v2").
- Click **Edit** on a card to update it or **Remove** to delete it.
- Click **+ Add markdown** to add a new context block.

<figure>
  <img src="..." class="help-center-img img-bordered" alt="Task detail view showing worktrees list, sessions panel, and shared context section with a prompt card" />
  <figcaption style="text-align: center; color: #888">Task detail view: worktrees, sessions, and shared context.</figcaption>
</figure>

***

## Managing Tasks

### Session status vs. Task stage

**Task stage** is the Kanban column the Task occupies (Exploration → In Development → In Review → Done). **Session status** is the real-time state of an individual agent session.

| Status | Meaning |
|---|---|
| 🟠 **Needs Attention** | The agent is waiting for your input. |
| 🟢 **Active** | The agent is running. |
| ⚫ **Idle** | The session stopped but is not complete. |
| 🔴 **Errored** | The session hit an error. |
| ⚫ **Inactive** | The session is not running and has no pending work. |
| **Disconnected** | The session lost connection to the agent runtime. <!-- TODO: confirm cause and reconnect steps with engineering --> |

### Notifications

Kepler sends a toast notification when a Task completes or needs attention. The notification shows the Task name, the agent that ran it, and the repo and branch. Click **View** to jump directly to the Task.

### Moving a Task between stages

<!-- TODO: confirm with engineering — confirm the exact interaction (drag-and-drop, dropdown, or right-click menu) for moving a Task between Kanban columns manually -->

### Archiving a Task

Click the **archive icon** on the Task card to archive it. Archived Tasks are removed from the active board.

### Closing a Task and its worktrees

<!-- TODO: confirm with engineering — describe what happens to worktrees (deleted, retained, merged) when a Task is closed or archived -->

---
