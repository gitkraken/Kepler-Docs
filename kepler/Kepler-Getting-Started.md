---
title: Getting Started with Kepler
description: Install Kepler, connect an agent and your trackers, and put an agent on real work in a few minutes.
product: Kepler
feature: Getting Started
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot, cursor, auggie, opencode]
hosted_variant: both
status: GA
last_verified: 2026-08
llms_include: true
tags: [getting-started, install, setup, dashboard, actions, first-task]
taxonomy:
  category: kepler
---
<kbd>Last updated: August 2026</kbd>

Kepler is GitKraken's **Agentic Development Environment (ADE)**: a place to direct coding agents across your real work, in as many repositories as you need, at the same time.

You bring the agent. Kepler pulls in the issues and pull requests already assigned to you, hands any of them to an agent with the context attached, and takes the result through to a reviewed, mergeable change.

Kepler is in **public preview**. A free GitKraken account is all you need.

<figure>
  <img src="/wp-content/uploads/kepler-getting-started-Aug-2026.png" class="help-center-img img-bordered" alt="Kepler's Todo list with an Action dropdown open on one row, offering Plan, Implement, and a custom action">
  <figcaption style="text-align:center; color:#888">The Todo list with the Action dropdown open on a row. Pick a built-in Action or one of your own to start an agent.</figcaption>
</figure>

***

## Install Kepler

| Platform | Installer | Minimum OS |
|---|---|---|
| Windows | 64-bit, ARM64 | Windows 10+ |
| macOS | Apple Silicon, Intel | macOS 12+ |
| Linux (x64) | .deb, .rpm, .AppImage, Flatpak, AUR | Ubuntu LTS 18.04+ / Debian 10+ / RHEL 8+ / Fedora 39+ |
| Linux (ARM) | .deb, .rpm, .AppImage | Ubuntu LTS 20.04+ / RHEL 8+ / Fedora 39+ |

1. Go to [gitkraken.com/kepler/download](https://www.gitkraken.com/kepler/download) and pick the installer for your platform.
2. Run it.
3. Launch Kepler.

***

## Sign in

Kepler opens on a welcome screen. Click **Sign in with GitKraken**. If you do not have an account, you'll create one in the next step.

<figure>
  <img src="/wp-content/uploads/sign-in-aug-2026.png" class="help-center-img img-bordered" alt="Kepler's welcome screen with the Sign in with GitKraken button">
  <figcaption style="text-align:center; color:#888">The welcome screen on first launch.</figcaption>
</figure>

A **Kepler Quick Start Tour** video appears on that screen if you'd rather watch first, or watch the <a href="https://www.youtube.com/playlist?list=PLXIji1KJqw9A" target="_blank" rel="noopener noreferrer">Kepler Quick Start Tour playlist</a> on YouTube.

***

## Finish the setup checklist

The **Setup** entry in the toolbar tracks 5 things, and shows **Setup · N/5** until they're done. Open it for **Finish setting up Kepler** and a progress readout.

| # | Item | What it does |
|---|---|---|
| 1 | **Sign in to GitKraken** | Done when you signed in above |
| 2 | **Connect an AI agent** | At least one coding agent. See [Agent Integrations](/kepler/agent-integrations) |
| 3 | **Connect issue & PR trackers** | Any provider. This is what fills your Todo list. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations) |
| 4 | **Set a default repositories folder** | Where Kepler clones repositories it does not find locally |
| 5 | **Set a default worktree folder** | Where Kepler creates one worktree per repository, per Task |

Expand **More setup options** for 3 optional items:

- **Connect a remote environment**, covered in [Remote Environments](/kepler/remote-environments)
- **Control Kepler remotely**, also in [Remote Environments](/kepler/remote-environments)
- **Add repo commands**

**Add repo commands** is worth doing early if your project needs a setup step. Save a repository's install or build command once and Kepler can run it automatically every time it creates a worktree, so an agent never starts in a checkout it cannot build. See [Tasks and Resources](/kepler/tasks-and-resources).

Folder paths and everything else live in [Settings](/kepler/settings). You can hide the checklist from the toolbar and still reach it there.

***

## Put an agent on real work

After you connect a tracker, the **Todo** segment of [the Kepler interface](/kepler/kepler-interface) fills with the issues and pull requests assigned to you.

1. Pick an item in **Todo**.
2. Click its **Action** button.

<figure>
  <img src="/wp-content/uploads/actions-drop-down.png" class="help-center-img img-bordered" alt="The Action dropdown open on a Todo row, listing Plan, Implement, Review, and Address Feedback">
  <figcaption style="text-align:center; color:#888">The Action dropdown, opened from the chevron next to the button.</figcaption>
</figure>

Nicely done! Kepler automatically does the following:

1. Creates a Task.
2. Attaches the repository and the item.
3. Sets up an isolated worktree.
4. Starts an agent with the context already in place.

The left half of the button runs the sensible default:

- **Plan** for an issue
- **Review** for someone else's pull request
- **Address Feedback** for one of yours

The chevron next to the button offers the rest of the Actions.

Every one of those prompts is yours to change, and you can add your own. That's the part worth reading next: [Actions](/kepler/actions).

***

## Start something that is not tracked yet

Click **New task**, or press **Shift+Alt+T** from anywhere. Write a prompt, attach a repository if the task needs one, and go. You can attach nothing at all and turn it into real work later. See [Create a Task](/kepler/create-task).

<figure>
  <img src="/wp-content/uploads/new-task-button-aug-2026.png" class="help-center-img img-bordered" alt="The New task button in the Kepler top navigation bar">
  <figcaption style="text-align:center; color:#888">The New task button, available from anywhere in Kepler.</figcaption>
</figure>

***

## Where to go next

| If you want to | Read |
|---|---|
| Change the prompts, or write your own | [Actions](/kepler/actions) |
| Understand what a Task holds | [Tasks and Resources](/kepler/tasks-and-resources) |
| Work inside a Task | [The Task View](/kepler/task-view) |
| Direct an agent mid-session | [Agent Sessions](/kepler/agent-sessions) |
| See what every agent is doing at once | [The Agent Graph](/kepler/agent-graph) |
| Reshape the list to fit how you work | [Arranging Your Work](/kepler/arranging-your-work) |
| Review and ship what an agent wrote | [Review Changes](/kepler/review-changes) |
| Run agents on another machine or in WSL | [Remote Environments](/kepler/remote-environments) |

---
