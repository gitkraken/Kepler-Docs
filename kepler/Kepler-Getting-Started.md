---
title: Getting Started with Kepler
description: Install Kepler, connect your first agent, and create your first Task.
product: Kepler
feature: Getting Started
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, opencode]
hosted_variant: both
status: GA
last_verified: 2026-06
llms_include: true
tags: [getting-started, install, setup, tasks, agents, first-task]
taxonomy:
  category: kepler
---
<kbd>Last updated: June 2026</kbd>

## What is Kepler?
Kepler is GitKraken's **Agentic Development Environment** (**ADE**), built for developers directing multiple AI coding agents across multiple repos in parallel.


<figure>
  <img src="/wp-content/uploads/kepler-full-screen.png" class="help-center-img img-bordered" alt="Kepler showing the task list on the left, a diff view in the center, and an agent chat panel on the right">
  <figcaption style="text-align:center; color:#888">Kepler with a Task open. The task list is on the left, the agent chat is in the center, and agent changes on the right.</figcaption>
</figure>



***

## Install Kepler

Kepler is available for **Windows**, **Mac**, and **Linux**.

| Platform | Installer | Minimum OS |
|---|---|---|
| Windows | 64-bit, ARM64 | Windows 10+ |
| Mac | Apple Silicon, Intel | macOS 12+ |
| Linux (x64) | .deb, .rpm, .AppImage | Ubuntu LTS 18.04+ / Debian 10+ / RHEL 8+ / Fedora 39+ |
| Linux (ARM) | .deb, .rpm, .AppImage | Ubuntu LTS 20.04+ / RHEL 8+ / Fedora 39+ |

1. Go to [gitkraken.com/kepler/download](https://www.gitkraken.com/kepler/download) and download the installer for your platform and architecture.
2. Run the installer and follow the on-screen prompts.
3. Launch Kepler.

On first open, Kepler displays the **Home** view. No repos are connected yet and no agents are configured. The next two sections cover the minimum setup required before creating your first Task.

<figure>
  <img src="..." class="help-center-img img-bordered" alt="Kepler Home view on first launch with no repos or agents configured">
  <figcaption style="text-align:center; color:#888">Kepler Home view on first launch, before any repos or agents are configured.</figcaption>
</figure>

<!-- TODO: confirm with engineering — confirm first-launch UI state and replace screenshot placeholder -->

***

## Minimum setup before creating your first Task

Two things must be in place before Kepler can create a Task: a default repos directory and at least one connected agent runtime.

### Set the default repos directory

Kepler uses a single local directory as the root for all repo clones and worktrees it manages. Set this first. Everything else depends on it.

1. Open **Settings** (gear icon, bottom-left).
2. Navigate to **Environment**.
3. Set **Default repos directory** to the local path where you want Kepler to store repos and worktrees.
4. Click **Save**.

The following table describes this setting:

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Default repos directory** | Root path for all Kepler-managed repo clones and worktrees | None (must be set manually) | Any valid local directory path |

### Connect an agent runtime

Kepler requires at least one agent integration before you can launch an agent session inside a Task.

For supported agents and connection steps, see [Agent Integrations](/kepler/agent-integrations).

***

## Create your first Task

A **Task** is the core unit of work in Kepler. It holds work across one or more repos and contains the **worktrees**, **agent sessions**, and changes that belong to a single unit of work.

This section covers creating a Task from scratch. For all three Task creation methods and full option details, see [Create a Task](/kepler/create-task).

1. Click **New Task** from the Home view or the task list.
2. Select a repo. Kepler clones it into your default repos directory if it is not already present locally.
3. Set a base branch. This is the branch the Task's worktree branches from.
4. Select an agent runtime.
5. Click **Create Task**.

Kepler automatically creates an isolated Git worktree for this Task. The agent session starts and the Task appears in **List** or **Kanban** view.

<figure>
  <img src="..." class="help-center-img img-bordered" alt="New Task creation dialog showing repo, base branch, and agent selection fields">
  <figcaption style="text-align:center; color:#888">The New Task dialog. Select a repo, base branch, and agent, then click Create Task.</figcaption>
</figure>

<!-- TODO: confirm with engineering — confirm exact button labels and dialog field names, replace screenshot placeholder -->

***

## Verify your setup

Setup is complete when all of the following are true:

- Your **Default repos directory** is set in **Settings → Environment**.
- At least one **agent runtime** is connected and shows as available.
- A **Task** has been created and is visible in **List** or **Kanban** view with an active agent session.

---
