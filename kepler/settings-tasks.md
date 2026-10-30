---
title: Task Settings
description: The Tasks page of Kepler's Settings, covering the default agent, what new sessions start with, where new tasks make changes, branch prefix, folder locations and the Variables menu, task naming, and the task page.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot, cursor, antigravity, opencode, pi, auggie, grok]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [settings, tasks, default-agent, worktrees, branch-prefix, folder-locations, variables]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

*A task is one piece of work: its prompt, the agent sessions working on it, and the worktree or folder they work in. Set how new tasks start and how a task's page looks.*

The Tasks page has two sections: **New tasks** and **Task page**.

## New tasks

This section sets what Kepler preselects for every new task. Its values belong to the environment you're working on, so in a remote window they're that machine's.

### Default agent

**Default agent** picks the agent, account, model, mode, and thinking effort that Kepler preselects for a new task. Its description reads *Used when new sessions start with the default agent, when Kepler has no earlier pick to go on, and whenever you choose Use default agent in the launcher.* The following table lists its controls:

| Control | What it does |
|---|---|
| **New tasks use** | Chooses the agent, and the account when that agent supports more than one |
| Options | Model, mode, and the agent's own configuration options. Available once an agent is picked |
| **Clear default** | Removes the saved default. Appears only once one is set |

Nothing is set out of the box, and the control is hidden entirely when no agent is installed. If the agent you saved is later uninstalled, the row warns you: *Your default agent, {name}, is no longer installed. Pick another.*

An [Action](/kepler/actions) inherits this configuration unless it names an agent of its own.

### New sessions start with

Under **Default agent**, the following setting decides which agent the Task Composer, the Dashboard's composer, and a new draft session preselect:

| Option | What it does |
|---|---|
| **Last used agent** | *The agent, model and mode you last picked.* The default |
| **Default agent** | *Always the default agent above.* |

With **Last used agent**, a task an agent created that has no session yet starts with the agent that created it. An Action's own agent isn't remembered as your last pick. If you choose **Default agent** with no default set, Kepler points you at the **Default agent** picker. Neither setting applies to Ask Kepler, which keeps its own last pick and its own default in [Settings → Agents](/kepler/settings-agents).

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-sessions-start-with-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-sessions-start-with-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The New tasks section of Settings › Tasks: New tasks use Claude Code CLI with Options and Clear default, its description, and New sessions start with offering Last used agent (The agent, model and mode you last picked) beside Default agent (Always the default agent above).">
  </a>
  <figcaption style="text-align:center; color:#888">Default agent and New sessions start with, in Settings → Tasks.</figcaption>
</figure>

### Where new tasks make changes

The following setting chooses what a newly attached repository starts on:

| Setting | What it controls | Default |
|---|---|---|
| **Where new tasks make changes** | What a newly attached repository starts on, in the Task Composer | Isolated worktree |

The following table lists its options:

| Option | What it does |
|---|---|
| **Isolated worktree** | *Own folder, agents run side by side.* Forks a new branch into its own worktree |
| **New branch** | *Switches your repo to a new branch.* Forks a new branch directly in the repository's own checkout, with no worktree |
| **Current branch** | *Works on whatever is checked out.* Runs on the repository's own checkout, on whichever branch it currently has, with no new branch created |

This setting sets the default only. The repository chip's own **Base branch** and **Isolated worktree** controls still override it for any single Task. See [Create a Task](/kepler/create-task#configuring-a-repository).

**Commits made on the current branch land on whichever branch is checked out at the time.** That caveat applies to **New branch** and **Current branch** alike, since both run in the repository's own checkout rather than an isolated one. If another Task is already working in that checkout, Kepler says so and offers to switch that one repository to an isolated worktree instead.

Two settings sit under **Where new tasks make changes**, because they apply only when Kepler creates a branch or a worktree: **Branch prefix** and **Worktrees folder**.

### Branch prefix

The following setting starts the name of every branch Kepler creates:

| Setting | What it controls | Default |
|---|---|---|
| **Branch prefix** | *Starts the name of every branch Kepler creates. A repo can set its own in its settings.* | `kepler/` |

The prefix applies to **automatic** names only. A branch name you type is used verbatim, which is how a repository with an enforced `feat/` or `fix/` push rule still works. A prefix you type without a trailing separator gains a `/`, so typing `team` stores `team/`. A personal `ea-` style prefix is kept as the literal lead-in it is. The prefix saves when you press **Enter** or **Escape**, or leave the field, and the field shows its save status.

Each repository can override the prefix on its [Edit repo](/kepler/settings-repositories#edit-a-repository) page under **Settings → Repositories**. If a repository already has a branch literally named after the prefix, Kepler says which one and points you there: *Can't be used in {repo}: it has a branch named {branch}. Set a different prefix for that repository under Repositories.*

### Folder locations

Three paths tell Kepler where to put things. Two of them are on this page, and the third is on the Repositories page:

| Setting | Where it is | What it controls | Default |
|---|---|---|---|
| **Worktrees folder** | Tasks → New tasks | *Where Kepler creates the worktree for each new task.* | `~/kepler/worktrees` |
| **Tasks folder** | Tasks → New tasks | *Each task gets a folder here for its attachments and files.* | `~/kepler/tasks` |
| **Repositories folder** | [Repositories](/kepler/settings-repositories#repositories-folder) | Where Kepler clones repositories, and where it looks for repositories to add | `~/kepler/repositories` |

All three are unset out of the box. Kepler computes a fallback under your home folder without writing it, so an untouched setting still reads as untouched.

Type a path directly, or click **Choose a folder** beside the field to browse. Edits save when you leave the field, so no separate Save button exists, and the field shows its save status.

The fields also warn you about paths that won't work as you expect:

- If a **Worktrees folder** has text before `<REPOSITORY_PATH>`, Kepler adds each repository's full path after that text. The field says so, *Each repo's full path is added after this folder.*, shows where an example repository would land, and suggests a template for worktrees next to each repository and one for a subfolder per repository. On Windows, such a path is invalid, so Kepler refuses it: *Not saved: adding each repo's full path after this folder creates an invalid path.*
- If the **Repositories folder** doesn't exist yet, the field reads *This folder doesn't exist yet. Kepler creates it when you clone.*

### The Variables menu

A folder field that can contain a dynamic variable has a **Variables** menu beside it. The menu shows each variable as a named tag, such as **REPOSITORY PATH**, beside its raw token. Pick a variable and Kepler inserts it at the cursor. Kepler fills it in when it creates the folder, so one pattern covers every repository. Each field offers only the variables it can actually resolve:

| Field | Variables offered |
|---|---|
| **Worktrees folder** | `<REPOSITORY_PATH>` (*Main repo folder*), `<REPOSITORY_NAME>` (*Repo name*) |
| **Repositories folder** | `<REPOSITORY_NAME>` |
| **Tasks folder** | None |

For example, `<REPOSITORY_PATH>/.worktrees/<REPOSITORY_NAME>` nests each worktree inside the repository it belongs to. Kepler collapses any `..` segments you write.

**Tasks folder** takes no variables. A task folder has no repository behind it, so nothing would ever fill one in. Kepler refuses the value rather than storing a path that can't resolve: *Dynamic variables cannot be used here. A task folder has no repository behind it, so nothing would ever fill one in. This value was not saved.*

Per-repository commands have a **Variables** menu of their own, with two more variables. See [Per-repository commands](/kepler/settings-repositories#per-repository-commands).

<figure style="text-align:center">
  <a href="/wp-content/uploads/folder-fields-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/folder-fields-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Worktrees folder field in Settings › Tasks, set to /home/alex/kepler/worktrees, with its Variables menu open listing the REPOSITORY PATH tag (Main repo folder) and the REPOSITORY NAME tag (Repo name), each beside its raw token, and the Choose a folder button beside the field.">
  </a>
  <figcaption style="text-align:center; color:#888">The Worktrees folder field in Settings → Tasks, with the Variables menu open.</figcaption>
</figure>

### Automatically name new tasks

The following setting names new tasks for you:

| Setting | What it controls | Default |
|---|---|---|
| **Automatically name new tasks** | *Names a new task with AI from its prompt and attached resources. A task created from a single issue or PR keeps that item's name.* | On |

This setting requires a paid GitKraken subscription to turn on. On the Community plan, when you're signed out, or with no organization, the lock replaces its checkbox only while the setting is off. Since the setting starts on, you see a ticked checkbox until you turn it off, and you can always turn it off. A change takes effect on the next task you create.

## Task page

This section sets how a task's page looks in this window. It's saved on this machine:

| Setting | What it controls | Default |
|---|---|---|
| **Show tabs on the task page** | Keeps sessions, worktrees, and resources open as tabs you can pin, drag between groups, and arrange side by side. With it off, each column of a task shows one thing at a time and you switch from the list on the left. See [The task view](/kepler/task-view) | Off |
| **Preview tabs** | *A single click opens a preview that the next click replaces. Double-click, or edit, to keep it open.* Sessions always open as permanent tabs. Needs tabs turned on | On |

***

---
