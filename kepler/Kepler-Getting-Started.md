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

This page walks you through installing Kepler, completing setup, and creating your first Task.

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
| macOS | Apple Silicon, Intel | macOS 12+ |
| Linux (x64) | .deb, .rpm, .AppImage | Ubuntu LTS 18.04+ / Debian 10+ / RHEL 8+ / Fedora 39+ |
| Linux (ARM) | .deb, .rpm, .AppImage | Ubuntu LTS 20.04+ / RHEL 8+ / Fedora 39+ |

1. Go to [gitkraken.com/kepler/download](https://www.gitkraken.com/kepler/download) and download the installer for your platform and architecture.
2. Run the installer and follow the on-screen prompts.
3. Launch Kepler.

On first open, Kepler displays the **Home** view. No repos or agents are configured yet. The next two sections cover the minimum setup required before creating your first Task.

<figure>
  <img src="/wp-content/uploads/blank-kepler.png" class="help-center-img img-bordered" alt="Kepler List view on first launch showing an empty task list in the sidebar and a 'No task selected' state in the center panel with a Launch a task button">
  <figcaption style="text-align:center; color:#888">Kepler on first launch. No tasks exist yet — click <strong>Launch a task</strong> or <strong>+ New task</strong> to create your first one.</figcaption>
</figure>

***

## Complete the setup checklist

Complete all five items in the **Setup** checklist before creating your first Task. Access the checklist from the **Setup** button in the top navigation bar. The checklist shows **Setup · N/5** and turns fully green when all five items are complete.

<figure>
  <img src="/wp-content/uploads/set-up-kepler.png" class="help-center-img img-bordered" alt="The Finish setting up Kepler checklist showing 5 of 5 items marked DONE and More setup options expanded to reveal Connect a remote environment and Control Kepler remotely">
  <figcaption style="text-align:center; color:#888">The Setup checklist with all five required items complete and the optional items expanded.</figcaption>
</figure>

### 1. Sign in to GitKraken

Sign in with your [GitKraken account](https://gitkraken.dev) when prompted on first launch.

### 2. Connect an AI agent

Connect at least one coding agent in **Settings → Agents**. For supported agents and connection steps, see [Agent Integrations](/kepler/agent-integrations).

<figure>
  <img src="/wp-content/uploads/agent-settings.png" class="help-center-img img-bordered" alt="The Agents section in Kepler Settings showing GitHub Copilot, Cursor CLI, and OpenCode entries each with a Not installed status, an Install button, a Binary path row, and a Re-scan and Custom path option">
  <figcaption style="text-align:center; color:#888">Settings → Agents. Each agent shows its binary status. Click <strong>Install</strong> or <strong>Custom path…</strong> to point Kepler to an existing installation.</figcaption>
</figure>

### 3. Connect issue & PR trackers

Connect your issue tracker and Git hosting provider in **Settings → Provider Integrations**. For setup steps, see [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

<figure>
  <img src="/wp-content/uploads/provider-integrations.png" class="help-center-img img-bordered" alt="The Provider Integrations section in Kepler Settings listing Azure DevOps, Bitbucket, GitHub, GitHub Enterprise, GitLab, GitLab Self-Hosted, Jira, Linear, and Trello, each with a Connect or Reconnect button">
  <figcaption style="text-align:center; color:#888">Settings → Provider Integrations. Connected providers show a <strong>Reconnect</strong> button; others show <strong>Connect</strong>.</figcaption>
</figure>

### 4. Set default folder locations

Open **Settings → General** and set both paths before creating your first Task.

- **Default Repositories Folder** — where Kepler clones repos. Every Task that references a repo not already on disk will clone it here.
- **Default Worktrees Folder** — where Kepler creates Git worktrees. Kepler creates one worktree per Task per repo.

Click the folder icon next to each field to browse, or type a path directly. The worktree path supports placeholders:

| Placeholder | Value |
|---|---|
| `<REPOSITORY_PATH>` | Main repo folder |
| `<REPOSITORY_NAME>` | Repo name |
| `<SOURCE_PATH>` | Files source (main repo, or the source worktree when forking) |
| `<WORKTREE_PATH>` | The new worktree folder |

Commands run inside the new worktree folder using your default login shell, so there's no need to `cd` into it and tools configured in your shell profile (e.g. `nvm`) are available.

<figure>
  <img src="/wp-content/uploads/default-locations.png" class="help-center-img img-bordered" alt="Settings → General showing Default Repositories Folder set to /Users/jonathansilva/kepler/repositories and Default Worktrees Folder set to /Users/jonathansilva/worktrees, both highlighted with a teal dashed border, and a Placeholders table below listing REPOSITORY_PATH, REPOSITORY_NAME, SOURCE_PATH, and WORKTREE_PATH">
  <figcaption style="text-align:center; color:#888">Settings → General. Set both folder paths before launching your first Task.</figcaption>
</figure>

Expand **More setup options** in the checklist to see two optional items:

- **Connect a remote environment** — run Tasks on a remote machine or inside WSL. See [Remote Environments](/kepler/remote-environments).
- **Control Kepler remotely** — start Kepler's local server to access the UI from another device. See [Remote Environments](/kepler/remote-environments).

***

## Create your first Task

A **Task** is the core unit of work in Kepler. It holds work across one or more repos and contains the **worktrees**, **agent sessions**, and changes that belong to a single unit of work.

This section covers creating a Task from scratch. For all three Task creation methods and full option details, see [Create a Task](/kepler/create-task).

<figure>
  <img src="/wp-content/uploads/new-task-button.png" class="help-center-img img-bordered" alt="The + New task button in the Kepler top navigation bar, highlighted with a teal border">
  <figcaption style="text-align:center; color:#888">Click <strong>+ New task</strong> in the top-right corner to open the Task Launcher.</figcaption>
</figure>

<figure>
  <img src="/wp-content/uploads/start-task-modal.png" class="help-center-img img-bordered" alt="The Start a task dialog in Kepler showing the Repositories section with an Add repo button, Task Name field, Prompt field, and Agent, Model, Mode, and Effort dropdowns at the bottom">
  <figcaption style="text-align:center; color:#888">The Task Launcher. Add a repo, name the task, add a prompt, and click <strong>Launch task</strong>.</figcaption>
</figure>

1. Click **+ New task** in the top-right corner to open the Task Launcher.
2. Under **Repositories**, click **+ Add repo** and select a repository. Kepler clones it into your default repos directory if it is not already present locally.
3. Enter a **Task Name**.
4. (Optional) Enter a **Prompt** with starting instructions for the agent.
5. Select an **Agent** and configure **Model**, **Mode**, and **Effort** as needed.
6. Click **Launch task**.

Kepler creates an isolated Git worktree for this Task, starts the agent session, and the Task appears in **List** or **Kanban** view.

---
