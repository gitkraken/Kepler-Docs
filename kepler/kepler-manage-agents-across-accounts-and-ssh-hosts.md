---
title: Manage Claude Code and Codex Sessions Across Accounts and SSH Hosts in Kepler
description: In Kepler, run Claude Code and Codex sessions on several accounts and on SSH hosts, pick the account per session, and move a conversation to another account.
product: Kepler
feature: Agent Accounts and Remote Environments
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, auggie, grok]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [claude-code, codex, multiple-accounts, ssh, remote-environments, agent-sessions, accounts]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Kepler by GitKraken manages your Claude Code and Codex sessions across several accounts and SSH hosts in 1 app. You add each account once in **Settings → Agents**, pick the account when you start a session, and add each remote server in **Settings → Remote environments**. Sessions on a server run there and keep running when you disconnect.

**Requirements and limits**

- Scope: Several signed-in accounts for 1 agent, choosing the account for each session, moving a conversation to another account, and running agent sessions on SSH hosts.
- Agents with several accounts: Claude Code, Codex, GitHub Copilot, Auggie, and Grok Build.
- Moving a conversation to another account: Claude Code and Codex only, and only between accounts that share history with the CLI.
- SSH hosts: Kepler installs itself on the host over SSH. The agent you want to run must also be installed and signed in on the host.
- Limits: SSH hosts and WSL distros need the Kepler desktop app. Kepler in a browser cannot connect to them.
- Limits: Each Kepler window works on 1 machine at a time. Open 1 window per machine to watch several machines side by side.

***

## Quick Start

1. Open **Settings → Agents** and expand **Claude Code** or **Codex**.
2. Under **Accounts**, click **Add account**, name the account, and sign in. Repeat for each account.
3. Open **Settings → Remote environments**, click **Add machine**, and follow the steps to add your SSH host.
4. Click **Connect** on the host. In the window connected to the host, install and sign in to Claude Code or Codex in **Settings → Agents**.
5. Start a task. In the **Agent** list, pick the agent and the account in 1 click.
6. To move a running conversation to another account, use **Continue as** on the session's tab menu.

***

## How to add several accounts to 1 agent

Claude Code, Codex, GitHub Copilot, Auggie, and Grok Build can each have more than 1 signed-in account, such as a work account and a personal account.

1. Open **Settings → Agents** and expand the agent.
2. Under **Accounts**, click **Add account**.
3. For Claude Code, Codex, and GitHub Copilot, choose how the account handles conversation history:
   - **Share with the CLI**: the account reads the same conversations as the agent's own login. Pick this to move conversations between accounts later.
   - **Keep separate**: the account keeps its own conversations.
4. Sign in.

The first row is the agent's own login. The account badged **Default** is the one new sessions use. Each account keeps its own sign-in and shares your skills, commands, and settings. Give each added account a color to tell sessions apart: the color tints the agent icon on session tabs.

With 2 or more accounts, the list is in priority order. To reorder it, drag a row by its handle, or use **Move to top**, **Move up**, or **Move down** in the row's menu. When you pick no account, a new session starts on the first account from the top with usage left. At a usage limit, Kepler moves to, or suggests, the first account from the top with usage left. To skip an account at a usage limit, clear **Use at a usage limit** in its menu. The row then reads **Skipped at a usage limit**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-accounts-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-accounts-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Claude Code card in Settings › Agents with two accounts, the default Claude Code CLI (Acme, Default) with the No color mark and Personal with a blue color swatch, each with Check usage and a row menu. Below them sit New sessions start in, Let artifact comments start turns, Artifacts in new sessions, and Program and data folder.">
  </a>
  <figcaption style="text-align:center; color:#888">2 Claude Code accounts in Settings → Agents.</figcaption>
</figure>

See [Several accounts for one agent](/kepler/agent-sessions#several-accounts-for-one-agent) for every account control.

***

## How to choose the account for a session

When an agent has 2 or more accounts, the **Agent** list shows 1 row per account, labeled with the account name. Pick the row in the **New task** window or in a new session tab, and the session runs under that account.

<figure style="text-align:center">
  <a href="/wp-content/uploads/account-multiple-selector-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/account-multiple-selector-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Agent list open in the New task composer, with Search options… at the top. Under a Claude Code heading sit two account rows: CLI, with the login alex.lee@example.com and an Acme badge, checked, and Personal. Below come Codex CLI (Not signed in), GitHub Copilot CLI (Not signed in), OpenCode, Pi and Auggie CLI (Not signed in), with more agents further down the list, then Add another account and Install another agent.">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent list, with 1 row per account.</figcaption>
</figure>

Each session runs under 1 account. Session tabs name the account, so you can see which account each session uses.

***

## How to move a conversation to another account

Move a Claude Code or Codex conversation to another account when an account reaches its usage limit, or when you started on the wrong account. The conversation stays the same.

1. Open the session's tab menu and select **Continue as**.
2. Pick the account. Kepler restarts the agent with the same conversation as that account and confirms **Continued as** *account*.

When an account reaches its usage limit, a bar on the session's composer says which limit and when it resets. The bar offers these choices:

- **Continue on** *account* picks up where the conversation stopped.
- A new session on another account reads this conversation first.
- **Wait** continues the conversation when the account resets.

You can also use the **Account** row in the composer's agent settings.

The move works only between accounts that share history with the CLI. An account that keeps its own history shows as **Separate history** in the list, because it cannot read the conversation. Sessions started outside Kepler cannot move to another account.

See [Moving a session to another account](/kepler/agent-sessions#moving-a-session-to-another-account).

***

## How to add an SSH host

1. Open **Settings → Remote environments** and click **Add machine**. To add a host that is already in your `~/.ssh/config`, click **Add** next to it under **Found on this machine** instead.
2. Enter the **Host**, and optionally the **Name**, **User**, and **Port**.
3. Choose how Kepler signs in: an existing key, your SSH agent or SSH config, a password, or a key Kepler generates for this host.
4. Check the host's fingerprint and click **Trust and continue**.
5. After Kepler tests the connection, click **Add**, then click **Connect** on the host.

Kepler installs itself on the host over SSH, so you do not need to set up Kepler there first. The agent is different: Claude Code or Codex must be installed on the host. In a window connected to the host, **Settings → Agents** lists the host's agents. If an agent shows **Not installed**, click **Install** to install it on the host, then sign in. The sign-in page opens in the browser on your own computer, and Kepler saves the sign-in on the host.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-new-host-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-new-host-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The first step of Add machine under Remote environments in Settings: its description, then a card with Name (optional) filled in from the host as dev.acme.example, Host dev.acme.example, Port 22 and User (optional) alex, with Cancel and Continue below the card.">
  </a>
  <figcaption style="text-align:center; color:#888">The first step of adding an SSH host.</figcaption>
</figure>

See [Add an SSH host](/kepler/remote-environments#add-an-ssh-host) for every step and sign-in option.

***

## Where your sessions run

In a window connected to an SSH host, the agent sessions, terminals, worktrees, and Git operations all run on the host. Your own computer runs only the Kepler window.

Sessions belong to the host, not to the window. If you close the window, lose the network, or put your laptop to sleep, the sessions keep running on the host. When you connect again, Kepler lists them, and you pick up where you left off.

See [What runs where](/kepler/remote-environments#what-runs-where).

***

## How to see all of it in one place

Each Kepler window shows 1 machine's tasks and sessions on its Dashboard, including which sessions need you. Use these to cover your computer and every server:

- **Switch machines from the title bar.** The chip after **New task**, at the left of the title bar, shows which machine the window works on, such as **Local** or a host name. Click it and pick a machine under **Switch to**.
- **Open a window per machine.** In the chip's menu, click the window icon next to a host to open it in a new window. Keep 1 window on your computer and 1 on each server.
- **Manage every machine in Settings.** **Settings → Remote environments** lists **Your machines**, whether each one is connected, and how many windows use it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-popover-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-popover-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The popover open under the dev-server chip, whose icon carries a green dot. The header shows dev-server over SSH as alex@dev.acme.example, Connected at 5 ms, the server and app version 0.15.0, and a gear, with Disconnect and the restart and stop server buttons. Below are Switch to with Local (Work on this machine) and its window icon, and Manage remote environments… with its Ctrl+Shift+R shortcut.">
  </a>
  <figcaption style="text-align:center; color:#888">Switch machines, or open one in a new window, from the title-bar chip.</figcaption>
</figure>

To keep track of which session needs you on each machine, see [Keep Track of Several Claude Code and Codex Sessions in Kepler](/kepler/kepler-track-multiple-agent-sessions).

***

## Common questions

### Can I use 2 Claude Code accounts at the same time?

Sessions on different accounts run side by side. Add both accounts in **Settings → Agents**, then pick a different account for each session.

### Can I run Claude Code on 1 account and Codex on another at the same time?

Each agent has its own accounts, and each session picks its own agent and account.

### Can I switch accounts when I hit a usage limit?

When an account reaches its limit, the bar on the session's composer offers **Continue on** another account. You can also use **Continue as** on the session's tab menu. For Claude Code and Codex, the conversation moves to the other account when both accounts share history with the CLI. Otherwise, the bar offers a new session on another account that reads this conversation first.

### Do I need to install anything on the SSH server?

Not for Kepler: it installs itself over SSH. The agent you want to run, such as Claude Code or Codex, must be installed on the server. Install it from **Settings → Agents** in a window connected to the server.

### Do my sessions stop when I disconnect from the server?

No. Sessions run on the server and keep running after you close the window or lose the connection. Connect again to pick them up.

### Does this work with WSL too?

On Windows, a WSL 2 distribution is a remote environment like an SSH host. See [WSL environments](/kepler/remote-environments#wsl-environments).

***

## Related pages

- [Agent Sessions](/kepler/agent-sessions)
- [Agent Integrations](/kepler/agent-integrations)
- [Remote Environments](/kepler/remote-environments)
- [Settings](/kepler/settings-environment)
- [Keep Track of Several Claude Code and Codex Sessions in Kepler](/kepler/kepler-track-multiple-agent-sessions)
- [Quick Answers](/kepler/quick-answers)
