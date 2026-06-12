---
title: Environment and Setup
description: "Configure Kepler's environment settings: repos directory, worktree paths, custom startup commands, and embedded terminals."
product: Kepler
feature: Environment and Setup
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: []
hosted_variant: both
status: GA
last_verified: 2026-06
llms_include: true
tags: [environment, setup, repositories, worktrees, terminal, custom-commands, startup]
taxonomy:
  category: kepler
---
<kbd>Last updated: June 2026</kbd>

## Overview

Before Kepler's **Tasks** work reliably, three settings must be in place:

- A default repositories folder
- A default worktrees folder
- Custom startup commands (for repos that need them)

This page walks through each setting in order and explains the embedded terminal you can use once Tasks are running.

**Task** is the core unit of work in Kepler, GitKraken's Agentic Development Environment (ADE). Each Task holds work across one or more repos and contains worktrees, agent sessions, and changes. Configuring the settings below correctly ensures that every new worktree Kepler creates lands in the right place and starts in a usable state.

***

## Setup Order

Complete these steps in order. Each one depends on the previous.

1. Set the **Default Repositories Folder**.
2. Set the **Default Worktrees Folder**.
3. Add custom commands for repos that need them.

***

## Default Repositories Folder

The **Default Repositories Folder** defines where Kepler clones repositories. Every other environment setting depends on a valid path here. If this is not set, Kepler cannot locate repos when creating worktrees or running agents.

### How to set it

1. Open **Settings**.
2. Navigate to **General**.
3. Under **Default Repositories Folder**, click **Browse** and select the directory you want Kepler to use for cloned repos.
4. Click **Save**.

<figure>
  <img src="/wp-content/uploads/settings-default-repos-folder.png" class="help-center-img img-bordered" alt="Default Repositories Folder field in Settings → General">
  <figcaption style="text-align:center; color:#888">Settings → General — Default Repositories Folder</figcaption>
</figure>

### What happens if the Default Repositories Folder is not set

If the **Default Repositories Folder** is empty, Kepler cannot resolve repo paths when a Task creates a new worktree. Worktree creation will fail or prompt you to supply a path manually each time. Set this before doing anything else.

***

## Default Worktrees Folder

The **Default Worktrees Folder** is the directory where Kepler creates new worktrees. Kepler creates one worktree per Task per repo, so setting this keeps worktrees in a consistent location instead of spreading across arbitrary directories.

### How to set it

1. Open **Settings**.
2. Navigate to **General**.
3. Under **Default Worktrees Folder**, click **Browse** and select the directory, or type a path directly using the placeholders described below.
4. Click **Save**.

<figure>
  <img src="/wp-content/uploads/settings-default-worktrees-folder.png" class="help-center-img img-bordered" alt="Default Worktrees Folder field in Settings → General">
  <figcaption style="text-align:center; color:#888">Settings → General — Default Worktrees Folder</figcaption>
</figure>

### Path placeholders

The **Default Worktrees Folder** path supports placeholders. Kepler substitutes these at worktree creation time, so worktrees always land in a consistent, predictable location for every repo.

| Placeholder | Resolves to |
|---|---|
| `<REPOSITORY_PATH>` | Full path to the main repo folder |
| `<REPOSITORY_NAME>` | Name of the repository |
| `<SOURCE_PATH>` | Path of the source location (main repo, or source worktree when forking from an existing worktree) |
| `<WORKTREE_PATH>` | Full path to the new worktree folder |

**Example path using placeholders:**

```
<REPOSITORY_PATH>/worktrees/<WORKTREE_PATH>
```

With this pattern, every repo gets its worktrees nested inside its own directory. A repo at `/projects/my-app` would produce worktrees at `/projects/my-app/worktrees/<worktree-name>`.

***

## Custom Commands Per Repository

Custom commands are shell commands that Kepler runs automatically when it creates a new worktree for a specific repo. Use them to install dependencies, run a build, or start a file watcher. The worktree starts ready for the agent session, with no manual setup required.

### Where to configure

1. Open **Settings**.
2. Navigate to **Repositories**.
3. Find the repo you want to configure. Repos without custom commands show a **No commands >** row.
4. Click the **No commands >** row to open the command editor for that repo.

<figure>
  <img src="/wp-content/uploads/settings-repo-custom-commands.png" class="help-center-img img-bordered" alt="Repositories list in Settings showing 'No commands >' rows per repo">
  <figcaption style="text-align:center; color:#888">Settings → Repositories — click a repo row to add custom commands</figcaption>
</figure>

### How to add commands

1. In the command editor, click **Add Command**.
2. Enter the shell command to run (for example, `npm install` or `pnpm build`).
3. Add additional commands as needed. Commands run in the order listed.
4. Click **Save**.

Kepler runs these commands in the worktree's directory immediately after the worktree is created, before any agent session starts.

### Troubleshoot a failed custom command

If a custom command exits with a non-zero status, Kepler stops running remaining commands for that worktree and surfaces the error. The worktree is created, but it may not be in a usable state. Check the command output in the Task view to diagnose the failure, correct the command in **Settings → Repositories**, and create a new Task to retry.

<!-- TODO: confirm with engineering — does Kepler surface a specific error UI when a custom command fails, and is there a way to re-run setup commands on an existing worktree without creating a new Task? -->

***

## Embedded Terminals

Kepler has an embedded terminal scoped to each worktree. Use it to run commands or inspect files without leaving the app.

### How to open a terminal for a worktree

<!-- TODO: confirm with engineering — exact UI path to open the embedded terminal for a specific worktree (e.g., right-click menu, button in the Task view, keyboard shortcut) -->

When you open a terminal for a worktree, it starts in that worktree's directory. You do not need to `cd` into it manually.

### When to use the embedded terminal

- Run one-off commands (linting, tests, manual builds) while an agent session is active in the same worktree.
- Inspect files or git state without switching context.
- Debug issues that a running agent session does not surface on its own.

### Limitations

The embedded terminal is scoped to a single worktree. It does not provide access to the broader filesystem outside that worktree's directory without navigating manually. For workflows that span multiple repos or worktrees simultaneously, a standalone terminal may be more practical.

<!-- TODO: confirm with engineering — are there any other known limitations (e.g., shell type, environment variable inheritance, multiplexing, persistent sessions across Task restarts)? -->

---
