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
last_verified: 2026-11
llms_include: true
tags: [getting-started, install, setup, dashboard, actions, first-task]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Kepler is GitKraken's **agentic development environment** (**ADE**). Use it to direct coding agents on your real work, in as many repositories as you need, at the same time.

You use your own coding agent. Kepler pulls in the issues and pull requests already assigned to you, hands any of them to an agent with the context attached, and takes the result through review to a change you can merge.

Kepler is in **public preview**. To use it, you need only a free GitKraken account.

<div class="embed-container embed-container--16-9">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/U0w18ZXrZ5M?rel=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
</div>

***

## Install Kepler

Kepler has installers for these platforms:

| Platform | Installer | Minimum OS |
|---|---|---|
| Windows | 64-bit, ARM64 | Windows 10+ |
| macOS | Apple Silicon, Intel | macOS 12+ |
| Linux (x64) | .deb, .rpm, .AppImage, Flatpak, AUR | Ubuntu LTS 18.04+ / Debian 10+ / RHEL 8+ / Fedora 39+ |
| Linux (ARM) | .deb, .rpm, .AppImage | Ubuntu LTS 20.04+ / RHEL 8+ / Fedora 39+ |

1. Go to [gitkraken.com/kepler/download](https://www.gitkraken.com/kepler/download) and pick the installer for your platform.
2. Run the installer.
3. Launch Kepler.

**If you open an older copy of Kepler** than the one that last used your data, Kepler stops at **Kepler is out of date** before it opens. The older copy cannot read everything the newer one saved, so sessions may seem to have disappeared. Click **Open Newer Version** when a newer copy is installed, or **Update and Restart** to update this copy (a Snap install does not offer it).

***

## Sign in

Kepler opens on a welcome screen, **Launch any agent. Land every PR.** Click **Sign in with GitKraken**. If you do not have an account, you'll create one in the next step.

<figure style="text-align:center">
  <a href="/wp-content/uploads/sign-in-aug-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/sign-in-aug-2026-v3@2x.png" class="help-center-img img-bordered" alt="Kepler's sign-in screen over a night sky: on the left Kep says Hi, I'm Kep. Sign in, and your first task is moments away, above the Watch Quick Start Tour tile; on the right Kepler with its Public Preview badge, Launch any agent. Land every PR., the description, Sign in with GitKraken and New to GitKraken? You'll create an account in the next step. Version 0.15.0 sits top right.">
  </a>
  <figcaption style="text-align:center; color:#888">The welcome screen on first launch.</figcaption>
</figure>

Kepler opens the sign-in page in your browser. Once you sign in there, Kepler continues on its own. If no browser opened, click **Reopen browser**, or click **Copy link** and open the link in any browser. You can also paste the code from your browser under **Or paste the code from your browser**, then click **Sign in**.

**Behind a proxy.** Kepler uses your system's proxy settings, or the `HTTPS_PROXY` environment variable when you set it, and passes the same proxy to the agents and terminals it starts. If a request fails through the proxy, the error names the proxy's address.

To check for updates before you sign in, click the version in the screen's top corner. When an update has downloaded, click **Update and restart**.

In a window connected to another machine, you sign in from the Kepler window on this computer, and the remote window continues once you finish there.

To watch a short tour before you start, click the **Watch Quick Start Tour** tile on the welcome screen, or watch the <a href="https://www.youtube.com/playlist?list=PLXIji1KJqw9A" target="_blank" rel="noopener noreferrer">Kepler Quick Start Tour playlist</a> on YouTube.

***

## Choose your agents, repos, and look

After you sign in, a guided start walks you through setup. To skip it at any point, click **I'll explore on my own**.

**Choose your coding agents.** Kepler finds the coding agents installed on this computer. In this step:

- Switch on the agents you want Kepler to use, and make one the default. To add a missing agent, click its tile to install or locate it. After an install, Kepler offers to sign you in to the agent. See [Agent Integrations](/kepler/agent-integrations#install-an-agent).
- Under **New sessions start in**, pick **Chat**, Kepler's own view of the agent, or **Terminal**, the agent's command-line app.
- If your code is on another machine, use **Work on another machine?** to move this window there. Remote environments need a paid plan.

If you installed an agent that Kepler did not find, click **Rescan**. To go on without an agent, click **Continue without an agent**. You can set one up later in **Settings → Agents**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/onboarding-no-agent-nov-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/onboarding-no-agent-nov-2026-v3@2x.png" class="help-center-img img-bordered" alt="The guided start's first step, Choose your coding agents, with no agent found: the list is headed Set up a coding agent to get started, with Rescan and the line Install one here, or Rescan if you installed one yourself., and the nine coding agents are dashed tiles, each ending in an arrow that you click to install or locate it. Kep says Hmm, no agents here yet. Installed one yourself? Press Rescan., and the step ends with I'll explore on my own and Continue without an agent.">
  </a>
  <figcaption style="text-align:center; color:#888">The first step of the guided start, with no agent found.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/onboarding-agents-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/onboarding-agents-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The guided start's first step, Choose your coding agents, under Welcome to Kepler and the 01 Agents / 02 Repos / 03 Theme & notifications steps: Claude Code and Codex are switched on among the nine coding agents, the others are dashed tiles ending in an arrow that you click to install or locate them, and New sessions start in offers Chat (selected) or Terminal. Kep says Kepler found Claude Code and Codex, with I'll explore on my own and Next at the bottom.">
  </a>
  <figcaption style="text-align:center; color:#888">The first step of the guided start, with two agents found and switched on.</figcaption>
</figure>

**Bring in your repos.** Every task runs in a repo or folder you add here. Kepler lists the repos and folders it found where you have worked, with the ones you use most already checked. In this step:

- Check the repos you work in. To add one Kepler did not find, click **Add a folder**.
- Confirm the **Repos folder**. Kepler finds your repos there and clones new ones into it.

Then click the button that adds them, such as **Add 2 and continue**. Kepler adds only what you check. If you leave the guided start before you finish this step, Kepler adds the repos it checked for you.

<figure style="text-align:center">
  <a href="/wp-content/uploads/onboarding-repos-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/onboarding-repos-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="The guided start's second step, Bring in your repos, with 02 Repos current in the step header: the Repos folder field reads /home/alex/code, and Repos and folders lists acme-web and acme-api checked and design-tokens unchecked, each with its path and when it was last used, under Filter, Select all, Unselect all and Add a folder. Back, I'll explore on my own and Add 2 and continue sit at the bottom.">
  </a>
  <figcaption style="text-align:center; color:#888">The second step, with the 2 repos Kepler picked checked.</figcaption>
</figure>

**Make it yours.** Pick a theme, or open the **Theme gallery**, and choose how Kepler gets your attention under **Notify me**:

- **Everything**: every reply and request on the desktop as well
- **When I'm needed**: questions, approvals, and errors on the desktop, while replies stay in Kepler
- **Only in Kepler**: no desktop notifications

To try an alert, click **Send a test notification**. You can change these choices later in [Settings](/kepler/settings-app#notifications). Click **Finish** to open the **New task** composer on the Dashboard and start your first task.

<figure style="text-align:center">
  <a href="/wp-content/uploads/onboarding-theme-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/onboarding-theme-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The guided start's third step, Make it yours, with 01 Agents and 02 Repos checked off and 03 Theme & notifications current: Theme tiles Kepler Dark (selected), Midnight, Kepler Light and Theme gallery beside the System / Light / Dark switch on Dark, and Notify me presets Everything, When I'm needed (selected) and Only in Kepler, with Play a sound with desktop notifications ticked, Send a test notification, Back and Finish.">
  </a>
  <figcaption style="text-align:center; color:#888">The third step, with the theme and notification choices.</figcaption>
</figure>

***

## Finish the setup checklist

After the guided start, the **Setup** entry in the top bar tracks 2 setup items and shows **Setup · N/2** until you finish them. Open it to see **Finish setting up Kepler** and your progress. Once both items are done, the **Setup** entry disappears from the top bar.

| # | Item | What it does |
|---|---|---|
| 1 | **Connect an AI agent** | At least one coding agent. See [Agent Integrations](/kepler/agent-integrations) |
| 2 | **Connect issue & PR trackers** | Any provider, which fills your Todo list. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations) |

Expand **More setup options** for optional items:

- **Set a default repositories folder**: where Kepler clones repositories it does not find locally
- **Set a default worktree folder**: where Kepler creates one worktree per repository, per task
- **Connect a remote environment**, covered in [Remote Environments](/kepler/remote-environments), where your plan can use it
- **Control Kepler remotely**, also in [Remote Environments](/kepler/remote-environments)
- **Add repo commands**, once you have a repository

If your project needs a setup step, use **Add repo commands** early. Save a repository's install or build command once, and Kepler can run it every time it creates a worktree, so an agent never starts in a checkout it cannot build. See [Tasks and Resources](/kepler/tasks-and-resources).

You can set folder paths and everything else on the checklist in [Settings](/kepler/settings-setup-account#setup). To remove the checklist from the top bar, click **Hide from toolbar (still available in Settings)**.

***

## Put an agent on real work

After you connect a tracker, the **Todo** view of [the Kepler interface](/kepler/kepler-interface) fills with the issues and pull requests related to you.

1. Pick an item in **Todo**.
2. Click its **Action** button.

<figure style="text-align:center">
  <a href="/wp-content/uploads/actions-drop-down.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/actions-drop-down.png" class="help-center-img img-bordered" alt="The Action dropdown open on a Todo row, listing Plan, Implement, Review, and Address Feedback">
  </a>
  <figcaption style="text-align:center; color:#888">The Action dropdown, opened from the chevron next to the button.</figcaption>
</figure>

Kepler then does the following on its own:

1. Creates a task.
2. Attaches the repository and the item.
3. Sets up an isolated worktree.
4. Starts an agent with the context already in place.

The left half of the button runs the default Action for the item:

- **Plan** for an issue
- **Review** for someone else's pull request
- **Address Feedback** for one of yours

The chevron next to the button offers the rest of the Actions.

You can change the prompt behind every Action and add Actions of your own. See [Actions](/kepler/actions).

***

## Start something that is not tracked yet

To start a task that has no issue or pull request behind it:

1. Click **New task** or press **Cmd/Ctrl+N**. From outside Kepler, press **Shift+Alt+N** to open the quick launcher.
2. Write a prompt.
3. If the task needs a repository, attach one.
4. Start the task.

You can also attach nothing at all and turn the task into real work later. See [Create a task](/kepler/create-task).

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-button-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-button-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The New task button at the left end of the Kepler top bar, a single button with a plus sign, after the application menu, the window switcher and the Back and Forward buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">The New task button, available from anywhere in Kepler.</figcaption>
</figure>

***

## Where to go next

Pick the next step that fits what you want to do:

| If you want to | Read |
|---|---|
| Change the prompts, or write your own | [Actions](/kepler/actions) |
| Understand what a task holds | [Tasks and Resources](/kepler/tasks-and-resources) |
| Work inside a task | [The Task View](/kepler/task-view) |
| Direct an agent mid-session | [Agent Sessions](/kepler/agent-sessions) |
| Run an agent on a schedule, or on new GitHub or Jira activity | [Automations](/kepler/automations) |
| See what every agent is doing at once | [The Agent Graph](/kepler/agent-graph) |
| Reshape the list to fit how you work | [Arranging Your Work](/kepler/arranging-your-work) |
| Review and ship what an agent wrote | [Review Changes](/kepler/review-changes) |
| Run agents on another machine or in WSL | [Remote Environments](/kepler/remote-environments) |
| Find a quick answer to a common question | [Quick Answers](/kepler/quick-answers) |

---
