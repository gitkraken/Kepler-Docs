---
title: Getting Started with Kepler
description: Install Kepler on Windows, macOS, or Linux, connect an agent and your trackers, and put an agent on real work in a few minutes.
product: Kepler
feature: Getting Started
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot, cursor, auggie, opencode, grok, pi, antigravity]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [getting-started, install, setup, dashboard, actions, first-task]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Kepler is GitKraken's **Agentic Development Environment (ADE)**: a place to direct coding agents across your real work, in as many repositories as you need, at the same time.

You bring the agent. Kepler pulls in the issues and pull requests already assigned to you, hands any of them to an agent with the context attached, and takes the result through to a reviewed, mergeable change.

Kepler is in **public preview**. A free GitKraken account is all you need.

<div class="embed-container embed-container--16-9">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/U0w18ZXrZ5M?rel=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
</div>

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

**If you open an older copy of Kepler** than the one that last used your data, Kepler stops at **Kepler is out of date** before it opens, because the older copy can't read everything the newer one saved; sessions in particular may look like they have disappeared. The dialog names the version your data needs, and offers **Open Newer Version** when a newer copy is installed, or **Update and Restart** when this copy can update itself, plus **Quit** and **Open Anyway**. A Snap install doesn't offer **Update and Restart**.

***

## Sign in

Kepler opens on a welcome screen, **Launch any agent. Land every PR.** Click **Sign in with GitKraken**. If you do not have an account, you'll create one in the next step.

<figure style="text-align:center">
  <a href="/wp-content/uploads/sign-in-aug-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/sign-in-aug-2026-v3@2x.png" class="help-center-img img-bordered" alt="Kepler's sign-in screen over a night sky: on the left Kep says Hi, I'm Kep. Sign in, and your first task is moments away, above the Watch Quick Start Tour tile; on the right Kepler with its Public Preview badge, Launch any agent. Land every PR., the description, Sign in with GitKraken and New to GitKraken? You'll create an account in the next step. Version 0.15.0 sits top right.">
  </a>
  <figcaption style="text-align:center; color:#888">The welcome screen on first launch.</figcaption>
</figure>

Kepler opens the sign-in page in your browser, and the button's place becomes a sign-in panel: *Continue in your browser*. Kepler continues on its own once you're signed in. If no browser opened, use **Reopen browser**, or **Copy link** and open it in any browser. You can also paste the code from your browser under **Or paste the code from your browser**, then click **Sign in**. If Kepler can't reach GitKraken, it says *Unable to reach GitKraken to start sign-in. Check your connection and try again.*

The screen's top corner shows Kepler's version. Click it to check for updates: the corner shows **Checking…**, then **Up to date**, the download's progress, or *Unable to check for updates* with **Try again**. When an update has downloaded, it reads **Update ready to install** with **Update and restart**, so you can update before you sign in.

In a window connected to another machine, the screen says *Continue in your other Kepler window*: sign-in happens in the Kepler window on this computer, and the remote window carries on once you finish there. If that window can't be signed in, it says *Unable to sign this window in with your Kepler account. Reconnect it and try again.*

The **Watch Quick Start Tour** tile on that screen plays a short tour if you'd rather watch first, or watch the <a href="https://www.youtube.com/playlist?list=PLXIji1KJqw9A" target="_blank" rel="noopener noreferrer">Kepler Quick Start Tour playlist</a> on YouTube.

***

## Choose your agents and your look

After you sign in, a guided start takes you through two steps. It fills the whole window, without the top bar. **I'll explore on my own** skips it at any point. Kepler also sends existing users through it once, with a *Welcome back* note that your tasks are where you left them.

**Choose your coding agents.** Kepler looks for the coding agents installed on this computer. Switch on the ones you want Kepler to use, install any that are missing, and make one the default. Under **New sessions start in**, pick **Chat**, Kepler's own view of the agent, or **Terminal**, the agent's own command-line app. **Next** waits until at least one agent is installed or switched on. If your code lives on another machine, **Work on another machine?** lists the machines Kepler found in your SSH configuration, in WSL, or saved in Kepler, and moves this window there. Remote environments need a paid plan, so that choice offers **Try free and connect** or **Upgrade to connect** where your plan doesn't include them.

<figure style="text-align:center">
  <a href="/wp-content/uploads/onboarding-agents-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/onboarding-agents-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The guided start's first step, Choose your coding agents, under Welcome to Kepler and the 01 Agents / 02 Theme & notifications steps: Claude Code and Codex are switched on among the nine coding agents, the others offer an install button, and New sessions start in offers Chat (selected) or Terminal. Kep says Kepler found Claude Code and Codex, with I'll explore on my own and Next at the bottom.">
  </a>
  <figcaption style="text-align:center; color:#888">The first step of the guided start, with two agents found and switched on.</figcaption>
</figure>

**Make it yours.** Pick a theme, or open the **Theme gallery**, and choose how Kepler gets your attention under **Notify me**:

- **Everything**: every reply and request on the desktop as well
- **When I'm needed**: questions, approvals, and errors on the desktop, while replies stay in Kepler. This is the default on the desktop
- **Only in Kepler**: no desktop notifications

**Send a test notification** shows what an alert looks like. You can change any of these later in [Settings](/kepler/settings-app#notifications). **Finish** takes you to **Tasks in progress** on the Dashboard, with the task composer open for your first task.

<figure style="text-align:center">
  <a href="/wp-content/uploads/onboarding-theme-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/onboarding-theme-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The guided start's second step, Make it yours: Theme tiles Kepler Dark (selected), Midnight, Kepler Light and Theme gallery beside the System / Light / Dark switch on Dark, and Notify me presets Everything, When I'm needed (selected) and Only in Kepler, with Play a sound with desktop notifications ticked, Send a test notification, Back and Finish.">
  </a>
  <figcaption style="text-align:center; color:#888">The second step, with the theme and notification choices.</figcaption>
</figure>

During the guided start, Kepler also adds the repositories you already work in, so your repository picker isn't empty: the folders of agent sessions you ran outside Kepler, and the repositories GitKraken Desktop, GitLens, and the GitKraken CLI remember.

***

## Finish the setup checklist

After the guided start, the **Setup** entry in the toolbar tracks 2 things, and shows **Setup · N/2** until they're done. Open it for **Finish setting up Kepler** and a progress readout. Once both are done, the **Setup** entry leaves the toolbar.

| # | Item | What it does |
|---|---|---|
| 1 | **Connect an AI agent** | At least one coding agent. See [Agent Integrations](/kepler/agent-integrations) |
| 2 | **Connect issue & PR trackers** | Any provider. This is what fills your Todo list. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations) |

Expand **More setup options** for optional items:

- **Set a default repositories folder**: where Kepler clones repositories it does not find locally
- **Set a default worktree folder**: where Kepler creates one worktree per repository, per Task
- **Connect a remote environment**, covered in [Remote Environments](/kepler/remote-environments), where your plan can use it
- **Control Kepler remotely**, also in [Remote Environments](/kepler/remote-environments)
- **Add repo commands**, once you have a repository

**Add repo commands** is worth doing early if your project needs a setup step. Save a repository's install or build command once and Kepler can run it automatically every time it creates a worktree, so an agent never starts in a checkout it cannot build. See [Tasks and Resources](/kepler/tasks-and-resources).

Folder paths and everything else live in [Settings](/kepler/settings-setup-account#setup). **Hide from toolbar (still available in Settings)** hides the checklist from the toolbar, and you can still reach it there.

***

## Put an agent on real work

After you connect a tracker, the **Todo** segment of [the Kepler interface](/kepler/kepler-interface) fills with the issues and pull requests assigned to you.

1. Pick an item in **Todo**.
2. Click its **Action** button.

<figure style="text-align:center">
  <a href="/wp-content/uploads/actions-drop-down.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/actions-drop-down.png" class="help-center-img img-bordered" alt="The Action dropdown open on a Todo row, listing Plan, Implement, Review, and Address Feedback">
  </a>
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

Click **New task** or press **Cmd/Ctrl+N**. From outside Kepler, **Shift+Alt+N** opens the quick launcher. Write a prompt, attach a repository if the task needs one, and go. You can attach nothing at all and turn it into real work later. See [Create a Task](/kepler/create-task).

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-button-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-button-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The New task button at the left end of the Kepler top bar, a single button with a plus sign, after the application menu, the window switcher and the Back and Forward buttons.">
  </a>
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
| Find a quick answer to a common question | [Quick Answers](/kepler/quick-answers) |

---
