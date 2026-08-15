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
last_verified: 2026-08
llms_include: true
tags: [tasks, resources, worktrees, shared-context, notes, sessions, archive, mcp]
taxonomy:
  category: kepler
---
<kbd>Last updated: August 2026</kbd>

A **Task** is the unit of work in Kepler. It's one thing you're trying to get done, plus everything the agents working on it need — the repositories, the issue or pull request it came from, the branches, the notes, and every agent session you've run against it.

A Task doesn't have to start with much. You can start one from an issue in [the Kepler interface](/kepler/kepler-interface) and it arrives with the repository and issue body already attached, or you can start one with nothing at all — no repository, no branch — chase an idea, and attach the real work to it later.

***

## What a Task holds

Everything attached to a Task is a **resource**. Attach them from **Add resource** at the bottom of the task view's rail, or from the **+** on any group header, which opens the same **Add resources** dialog on that category.

| Resource | What it is |
|---|---|
| **Sessions** | Agent conversations running against this Task |
| **Terminals** | Shells opened inside one of the Task's working directories |
| **Worktrees** | Git working copies the agents make changes in. Grouped as **Changes** in the rail, because that's what you go there to read |
| **Folders** | A directory that isn't a Git repository — the agent works on it in place |
| **Files** | A single file, when the whole folder isn't the point |
| **Pull requests** | PRs from your connected Git hosts |
| **Issues** | Issues from your connected trackers |
| **Links** | Any URL worth keeping with the work |
| **Notes** | Text you write — standing instructions, decisions, reference material |
| **Attachments** | Files you upload to the Task |

A Task can hold **more than one** of any of these. Several repositories, several issues, several pull requests — a Task spanning three repos with two linked issues is a normal Task, not a special case.

For the screen itself — the rail, the columns, split panes, tabs — see [The Task View](/kepler/task-view).

### Pull requests attach themselves

You don't have to remember to attach the PR. When a Task holds no pull request yet and one of its worktrees is sitting on a branch that exactly matches an open PR's head branch, Kepler records that PR as a resource on its own — however the PR was opened, including from a terminal, from GitKraken, or on the web.

It is deliberately narrow, because a wrong guess would put a stranger's work into your agent's context:

- The branch names must match exactly. A near-miss doesn't count.
- Only open pull requests, and only ones whose head branch lives in the same repository — a PR from a fork never auto-attaches.
- A pull request another active Task already owns is left where it is.

It only ever attaches; it never detaches. Detach it yourself if you don't want it.

***

## Worktrees, and when you don't need one

Most work benefits from a **worktree**: a private Git working copy for this Task. Agents make their changes there, so nothing they do touches the checkout you're working in, and several agents can run at once without stepping on each other.

When you add a repository to a Task, the **Isolated worktree** toggle decides how it's set up.

| Setting | What it says |
|---|---|
| **On** | *On — a private worktree for this task. The branch is pinned here; nothing else can move it.* |
| **Off** | *Off — shares your repo folder. Whoever switches its branch — an agent, another task, a terminal — switches it for this task too.* |

With isolation off, the picker reads **directly in repo**.

> **Turning isolation off means the Task has no branch of its own.** *Your repository folder, used exactly as it stands. Nothing is copied and nothing is guaranteed.* Use it when you deliberately want an agent working in the checkout you're sitting in; leave it on otherwise.

A repository linked to a pull request is always isolated, and the toggle is locked: *This repository is linked to a pull request and always opens in its own isolated working copy.*

You can also pick the branch when you attach the repository: **Use this branch** to work directly on an existing branch, or **New branch** to branch off it. A new branch takes its name from the Task name unless you set one — the field reads *Derived from the task name*.

**A new branch forks from the repository's remote default branch**, not from whatever branch you happen to have checked out. Naming a base yourself overrides that. If no remote default can be resolved — no remote, a shallow clone, offline with nothing cached — Kepler falls back to the current HEAD rather than refusing to start.

**A Task needs no worktree at all.** Attach a plain folder and the agent works on it in place. Attach nothing and you have somewhere to think, which you can turn into real work whenever it earns it.

### Make a new worktree ready to build

A fresh worktree is a clean checkout: no `node_modules`, no build output, nothing your setup script would normally leave behind. An agent that starts there has to install dependencies before it can do anything, or it fails on the first build.

**Commands** solve that. Save a repository's setup steps once — `pnpm install`, a codegen step, whatever your project needs — and tick **Run on worktree creation**. Kepler runs them in the new worktree's folder every time it makes one for that repository, in order, before the agent starts. Commands you don't flag stay on demand: right-click a worktree in the task view rail and pick **Run command here**.

Set them up in **Settings → Repositories**, on the repository's own row. See [Settings](/kepler/settings) for the fields, the path placeholders, and what happens when one fails.

***

## Shared context — how resources reach your agents

Everything attached to a Task is sent to **every agent session in it** as *shared context*. That's what a prompt means when it says *"described in the shared context above"* — the issue body, the pull request, your notes, the links.

You'll see it in the conversation as a collapsible row reading **Shared context shared** the first time, and **Shared context updated** whenever it changes, with a count of the items included. Expand it to see exactly what the agent was given.

You don't edit shared context directly. You change it by attaching and detaching resources — and when it changes while a session is mid-turn, Kepler tells you **New shared context will be sent on next prompt** rather than interrupting the agent.

### Notes are how you give standing instructions

Attach a **Note** for anything every agent on the Task should follow — a style rule, a constraint, a decision you don't want re-litigated. Write it once and every session gets it, including sessions you start later.

***

## Detaching and deleting

Removing a resource from a Task doesn't destroy it. Kepler asks separately in each case, because the answer differs:

| Resource | Dialog | What removing it does |
|---|---|---|
| **Folder** | *Detach folder?* | *The folder stays on disk — it's only removed from this task.* |
| **File** | *Detach file?* | *The file stays on disk — it's only removed from this task.* |
| **Link** | *Detach link?* | *It's removed from this task.* |
| **Note** | *Delete note?* | *This permanently deletes the note.* |
| **Attachment** | *Delete attachment?* | *This permanently deletes the attachment.* |

Worktrees get more care, because deleting one can lose work. **Detach** removes the worktree from the Task and leaves it on disk. **Detach & Delete** removes it entirely, and Kepler checks first:

- If the worktree is used by **other Tasks**: *This worktree is used by other tasks, so it can't be deleted — detaching only removes it from this task.* The dialog names them under **Also used by**.
- If it's the repository's **main worktree**: *This is the repository's main worktree — it can't be deleted, only detached from the task.*
- Otherwise: *This worktree is only used by this task. Detach it (it stays on disk) or delete it entirely.*

Below that, a live checklist of what deleting would cost, read fresh from the worktree rather than written in advance. The working copy and the branch are reported separately, because they're separate risks:

| Reported on | What you'll see |
|---|---|
| The working copy | *{count} uncommitted files will be lost.*, or *Detached HEAD — commits may become unreachable after delete.*, or *No uncommitted changes — safe to delete.* |
| The branch, beside **Also delete branch** | Left unticked: *This branch isn't on any remote.* Ticked: *{count} unpushed commits will be lost.*, *This branch isn't published anywhere — deleting it may discard local commits.*, or *Nothing to lose — the branch is safe to delete.* |

Deleting a worktree that has something to lose is only possible through that checklist. Kepler refuses the delete outright when it wasn't confirmed there, and names what would have been lost — so nothing can destroy uncommitted or unpushed work behind your back, whatever asked for it.

***

## Renaming, archiving, and deleting a Task

From the **Task actions** (**⋮**) menu, on the task's row or in the task view's header:

| Action | What it does |
|---|---|
| **Rename task** | Tasks name themselves when they're created; rename when the name stops fitting. The dialog's **Auto-name** button suggests one from the Task's prompt and resources, into the field, for you to accept or edit |
| **Archive task** | Takes it out of the active list and keeps it as history. Nothing is destroyed unless you ask for it |
| **Restore task** | On an archived Task, in place of **Archive task**. No confirmation — it goes straight back |
| **Delete task** | Removes the Task |

<!-- TODO(verify): the archive dialog's description reads "It leaves the sidebar and stays in the dashboard as history" (src/ui/components/task/TaskCleanupDialog.tsx), but the sidebar it names went away with the List view in 29a06035a. Paraphrased above; check whether the app copy is being updated. -->

**Archive** and **Delete** ask the same two questions, in the same dialog, because they're the same act: **Also delete worktrees**, and — only once that's ticked — **Also delete branches**. Tick the first and Kepler lists every worktree under **Will be deleted**, each with what deleting it costs, and separately lists any it will keep under **Kept — still used by other tasks**. Ticking **Also delete branches** re-reads the list, so a worktree that was safe a moment ago can turn into a warning.

Individual sessions can be archived and restored the same way, from the session's own menu in the rail.

***

## What an agent can do with a Task's resources

Agents reach the Task through Kepler's own MCP server, so an agent can keep the Task's resource list honest instead of leaving it to you.

| Tool | What it does |
|---|---|
| `get_task_context` | Read the Task's current shared context |
| `list_task_resources` | List what's attached — worktrees, folders, files, PR and issue links, notes |
| `list_repos` | List the repositories a worktree could be created in, flagging the ones this Task already uses |
| `attach_link` | Attach an issue, pull request, or URL. Kepler classifies it and fetches its title and status when it can |
| `detach_link` | Remove a link, by URL or by id |
| `create_worktree` | Create a worktree on a fresh branch, forked from the repository's remote default branch or from a base you name |
| `discard_worktree` | Delete a worktree, and by default its branch |

Every one of them is scoped to the agent's own Task. An agent can't touch another Task's resources, and it never names a Task as an argument — Kepler derives it from who's calling.

Reads, `attach_link` and `create_worktree` run without asking, because none of them destroy anything. The two that can — `detach_link` and `discard_worktree` — go through the normal permission prompt, so you allow them once, for the session, or always.

`discard_worktree` carries the same protection your own delete does. It refuses while a live session is running in the worktree, including the agent's own. And when deleting would lose work, the first call refuses and hands the agent the inventory of what's at stake, so it has to bring that back to you and ask before it can retry.

---
