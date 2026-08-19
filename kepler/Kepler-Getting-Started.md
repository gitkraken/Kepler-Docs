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

Kepler is GitKraken's **Agentic Development Environment (ADE)** — a place to direct coding agents across your real work, in as many repositories as you need, at the same time.

You bring the agent. Kepler pulls in the issues and pull requests already assigned to you, hands any of them to an agent with the context attached, and takes the result through to a reviewed, mergeable change.

Kepler is in **public preview**. A free GitKraken account is all you need.

<!-- TODO(screenshot): Kepler open on the Todo segment, work visible, an Action button on a row. -->

***

## Install Kepler

| Platform | Installer | Minimum OS |
|---|---|---|
| Windows | 64-bit, ARM64 | Windows 10+ |
| macOS | Apple Silicon, Intel | macOS 12+ |
| Linux (x64) | .deb, .rpm, .AppImage, Flatpak, AUR | Ubuntu LTS 18.04+ / Debian 10+ / RHEL 8+ / Fedora 39+ |
| Linux (ARM) | .deb, .rpm, .AppImage | Ubuntu LTS 20.04+ / RHEL 8+ / Fedora 39+ |

<!-- TODO(verify): minimum OS versions carried over from the June page; confirm against the v0.9 release build and the download page. -->

1. Go to [gitkraken.com/kepler/download](https://www.gitkraken.com/kepler/download) and pick the installer for your platform.
2. Run it.
3. Launch Kepler.

***

## Sign in

Kepler opens on a welcome screen. Click **Sign in with GitKraken** — if you don't have an account you'll create one in the next step. A **Kepler Quick Start Tour** video appears on that screen if you'd rather watch first.

***

## Finish the setup checklist

The **Setup** entry in the toolbar tracks five things, and shows **Setup · N/5** until they're done. Open it for **Finish setting up Kepler** and a progress readout.

| # | Item | What it does |
|---|---|---|
| 1 | **Sign in to GitKraken** | Done when you signed in above |
| 2 | **Connect an AI agent** | At least one coding agent. See [Agent Integrations](/kepler/agent-integrations) |
| 3 | **Connect issue & PR trackers** | Any provider. This is what fills your Todo list — see [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations) |
| 4 | **Set a default repositories folder** | Where Kepler clones repositories it doesn't find locally |
| 5 | **Set a default worktree folder** | Where Kepler creates worktrees — one per repository, per Task |

Expand **More setup options** for three optional items:

- **Connect a remote environment** — see [Remote Environments](/kepler/remote-environments)
- **Control Kepler remotely** — see [Remote Environments](/kepler/remote-environments)
- **Add repo commands**

**Add repo commands** is worth doing early if your project needs a setup step. Save a repository's install or build command once and Kepler can run it automatically every time it creates a worktree, so an agent never starts in a checkout it can't build. See [Tasks and Resources](/kepler/tasks-and-resources).

Folder paths and everything else live in [Settings](/kepler/settings). You can hide the checklist from the toolbar and still reach it there.

***

## Put an agent on real work

After you connect a tracker, the **Todo** segment of [the Kepler interface](/kepler/kepler-interface) fills with the issues and pull requests assigned to you — no blank prompt box, nothing to go find.

1. Pick an item in **Todo**.
2. Click its **Action** button.

That's the whole thing. Behind the scenes, Kepler:

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

## Start something that isn't tracked yet

Click **New task**, or press **Shift+Alt+T** from anywhere. Write a prompt, attach a repository if the task needs one, and go. You can attach nothing at all and turn it into real work later. See [Create a Task](/kepler/create-task).

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
