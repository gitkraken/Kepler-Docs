---
title: Agent Sessions
description: An agent session is one running conversation with a coding agent inside a task. Learn how to start one, pick the agent and account (including several accounts of the same agent), queue prompts, answer the agent's questions and permission requests, track usage limits, and keep sessions running through restarts.
product: Kepler
feature: Agent Sessions
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode, grok, pi, antigravity]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [agent-sessions, sessions, prompts, steering, queueing, accounts, models, modes, skills, notifications, voice-input, usage-limits, artifacts, session-recovery]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

An **agent session** is one running conversation with a coding agent, anchored to one working directory. Learn how to start a session, direct it with prompts, answer its questions, and manage it from start to archive.

A task can hold several sessions. For example, 2 agents can share one worktree, each agent can have its own worktree, or a session can run in the task folder itself. A task lists all of its sessions under its **Sessions** group. See [The Task View](/kepler/task-view).

Sessions vary in 2 ways:

| Property | Values | Details |
|---|---|---|
| **How it runs** | **Chat** or **Terminal** | [How a session runs](#how-a-session-runs) |
| **Where it started** | In Kepler, or outside Kepler and found by it | [Sessions started outside Kepler](#sessions-started-outside-kepler) |

Prompts, steering, permissions, status, and the session lifecycle work the same way for every session.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-session-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-session-aug-2026.png" class="help-center-img img-bordered" alt="A running session in the Sessions column, with a tab strip, a transcript showing a collapsed tool-call group, and the composer's agent-settings pill">
  </a>
  <figcaption style="text-align:center; color:#888">A session in the Sessions column: tabs, transcript, and composer.</figcaption>
</figure>

To read the changes an agent made, see [Review Changes](/kepler/review-changes).

***

## Starting a session

You can start a session from any of the following places:

| From | How |
|---|---|
| A row in **Todo** | Fire an Action. See [Actions](/kepler/actions) |
| The task page's context panel | **New session** on the **Sessions** group, or **New session here** on a worktree or folder row |
| An open session strip | **+** (**New session**), or **Cmd/Ctrl+T** |
| An existing session | **New session from this one** on its row menu |
| A message in a conversation | **New session from here** on the message's right-click menu |

For a quick question that does not belong to a task, use **Ask Kepler**, the chat in the top bar's side panel. Any agent that runs in **Chat** can answer there. To move the chat into a task, click **Continue in a new task**. On that task's session, **Open source session** reopens the chat in the panel. See [Ask Kepler](/kepler/ask-kepler).

### Draft session tabs

**New session** opens a draft tab, not a menu. Nothing starts until you send the first message, so you can write the prompt, attach files, and pick the agent first. The tab takes its name from the first line of your prompt. When the tab strip has room, the tab is marked **(draft)**. In the context panel, the same row reads **Draft**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-draft-session-target-picker-01-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-draft-session-target-picker-01-v2@2x.png" class="help-center-img img-bordered" alt="A task's side panel with a New session (draft) tab beside its first session. The draft's target picker is open over the composer: Search branches and folders, Attached to this task with kepler/fix-cart-total, and Branches listing kepler/checkout-copy, kepler/payment-sdk-v5, kepler/product-search and main, with the attached branch's submenu offering Use this branch and New branch from this.">
  </a>
  <figcaption style="text-align:center; color:#888">A draft session tab, with its target picker open.</figcaption>
</figure>

To choose where the session runs, open the draft's target picker. It offers the following:

| Part | What it does |
|---|---|
| **Search branches and folders** | Filters the list as you type |
| **Attached to this task** | The worktrees and folders already attached to the task, including **All worktrees and folders**: *Runs in the task folder and has access to all worktrees and folders* |
| **Branches** | Other branches of the task's repositories. Pick one to start the session on that branch |
| **New branch from this** | Starts the session on a new branch based on the branch you picked |

Every session sees the task's attached resources wherever it runs. **All worktrees and folders** changes only the session's working directory.

A session receives the task's shared context by default. To start a session that forms its own view of the work, untick the **Task context** chip in the draft composer's footer, beside **Attach a file** and the microphone. The chip's tooltip reads **Leave out the task context** while it is ticked and **Include the task context** while it is not: *Gives the agent the task's prompt and notes. Later changes reach it with your next message.*

Right-click a draft tab or its row in the context panel for these actions:

- **Discard draft**: removes the draft. If the draft holds text or attachments, Kepler asks first: **Discard new session?**
- **Move left** or **Move right**: moves the draft among the other tabs.

If **Show tabs on the task page** is on, the draft has a regular tab menu instead: **Pin tab** or **Unpin tab**, **Keep open** while the tab is a preview, and **Close tab**, the only way to close it. See [Task View](/kepler/task-view#tabs-and-groups).

### Branching and renaming a session

**New session from this one** starts a sibling session in the same task, worktree, agent, and account. The new agent can read the source conversation.

**New session from here** does the same, but the new agent reads the source only up to and including the message you picked. The command is available once that message has finished streaming. It is not available on a terminal or external session (*This conversation can't be branched at a message.*).

To go back to the original, choose **Open source session** on the new session's menu.

To give a session your own name, choose **Rename session** on its row menu. Agents can also name and rename the Chat sessions they start, through Kepler's workspace tools.

***

## Agent, model, mode, and effort

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-settings-from-composer-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-settings-from-composer-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Agent settings open above a new session's composer: Agent OpenCode, Start in with Chat selected beside Terminal, Model Docs Model, Permission mode Build or Plan, MCP servers (No servers) with Manage, and Use default agent. Below it, the composer footer holds a ticked Task context chip beside Attach a file and the microphone, then the Docs Model Build pill and Start.">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent settings pill, opened from the composer, with the Task context chip in the footer.</figcaption>
</figure>

To choose the agent, model, mode, and effort, use the **Agent settings** pill on the composer. The pill offers the same choices when you start a session and while it runs, and its label shows the current model and mode.

| Choice | Changeable mid-session | Notes |
|---|---|---|
| **Agent** | No | Fixed once the session exists. To use another agent, start a new session |
| **Start in** | No | **Chat** or **Terminal**, for an agent that offers both. To use the other mode, start a new session; see [How a session runs](#how-a-session-runs) |
| **Model** | Yes | Models are per provider, so each agent has its own catalog and a model never moves to another agent. At the default, the row reads **Default · {model}**, naming the model the default resolves to |
| **Mode** | Yes | The agent's own permission modes |
| **Effort** | Yes | Reasoning or thinking depth, for agents that offer it |
| Other **Options** | Some | You can set an option the agent reads only at startup when you launch the session, and nowhere else. A Terminal launch offers the CLI's own launch options; see [How a session runs](#how-a-session-runs) |

A change applies from your next message. It never interrupts the turn in progress.

The menu also shows its state:

- An option row reads **Agent decides** until you pick a value.
- **Reset** appears once you override anything.
- The pill reads **Loading {agent} options…** while Kepler checks an agent it has not seen recently.

If a session's model changes, for example because the default now resolves to a different model, the conversation shows *Model changed from {from} to {to}.*

Kepler refreshes the model and mode lists in the background, and again after you upgrade or sign in to an agent. A newly released model appears without restarting Kepler.

The same menu lists the MCP servers the agent loads for this repository. To change them, click **Manage**. See [MCP Servers](/kepler/mcp-servers).

When the menu cannot offer the usual choices, it shows one of these messages:

| The menu reads | When |
|---|---|
| **Loading your last agent choice…** | Kepler is restoring the agent you used last |
| **Connect an AI agent** | No agent is installed: *Install an agent CLI to start your first session.* Each agent has an **Install** row, with **See all {count} agents in Settings**, and **Installed one yourself?** with **Check again** |
| **Sign in to {agent} to start a session** | The chosen agent is installed but signed out |
| **{agent} didn't share its options** | Kepler could not read the agent's models and modes: *You can still start a session. It uses {agent}'s own model and mode.* with **Retry** |

If you have more than one account, the **Agent** list groups accounts under their agent. The list ends with **Add another account** and **Install another agent**.

By default, a new task, the Dashboard composer, and a new draft tab start with the agent, model, and mode you last picked. To always start with one agent instead:

1. Open **Settings → Tasks → New tasks**.
2. Set **Default agent**.
3. Set **New sessions start with** to **Default agent** (*Always the default agent above*) instead of **Last used agent** (*The agent, model and mode you last picked*).

To use the default agent for one session only, click **Use default agent** in the launcher. See [Settings](/kepler/settings-tasks#new-tasks).

### Which agents are available

Kepler supports Claude Code, Codex, GitHub Copilot, Cursor, Auggie, OpenCode, Grok Build, Pi, and Google Antigravity, plus any custom agent you add. Kepler offers only the agents you have installed. See [Agent Integrations](/kepler/agent-integrations).

***

## Several accounts for one agent

Claude Code, Codex, GitHub Copilot, Auggie, and Grok Build can each have more than one signed-in account. To manage an agent's accounts, open **Settings → Agents**, expand the agent, and find **Accounts**:

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-accounts-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-accounts-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Claude Code card in Settings › Agents with two accounts, the default Claude Code CLI (Acme, Default) with the No color mark and Personal with a blue colour swatch, each with Check usage and a row menu. Below them sit New sessions start in, Let artifact comments start turns, Artifacts in new sessions, and Program and data folder.">
  </a>
  <figcaption style="text-align:center; color:#888">The Accounts section, in Settings → Agents.</figcaption>
</figure>


> Run multiple Claude Code logins side by side. Each account keeps its own credentials and history but shares your skills, agents, commands and settings.

| Control | What it does |
|---|---|
| First row, badged **Default** | The agent's own login, in its normal config directory |
| **Add account** | Adds an isolated account with its own credentials and history |
| **Account name** | Rename a row in place. The name is what you pick from later |
| **Sign in** / **Sign out** | Authenticates or clears that account alone |
| **Check usage** | Reads that account's plan usage. Grayed out only when **Check plan usage with each agent's provider** is turned off in **Settings → Agents → Usage limits**: *To check this account's usage, turn on Check plan usage with each agent's provider in Usage limits.* |
| **Switch account…** | On a signed-in Claude Code account's row menu. Signs that account in with a different Claude login, after a confirmation (**Switch the account for {name}?**) that counts the running sessions using it |
| **Remove account** | Signs the account out and deletes its local data, but leaves your shared skills, agents, and settings alone. Sessions whose conversations are stored only in that account are deleted with it; see below |
| Color swatch | At the left of each added account's row (*Pick a color to tell agents on different accounts apart*): **Rose**, **Amber**, **Lime**, **Cyan**, **Blue**, **Violet**, or **No color**. *The default account stays uncolored*, so its picker shows the ⊘ **No color** mark; the mark does not mean the account is off |

An account's color tints the agent icon on session tabs, in the context panel, and on the terminal status bar. You can tell sessions on different accounts apart by their color.

**Switch account…** opens the same sign-in as **Add account**. If your browser is already signed in, choose a different account on the sign-in page. On the default row, the confirmation adds *This also changes the account the claude command uses in your own terminals.* When the sign-in completes, Kepler confirms *{name} is now signed in as {login}.*

**An added account can stop sharing your configuration.** An added account links to your own configuration instead of copying it. That configuration includes your settings, instructions, skills, agents, commands, plugins, rules, and hooks. If the agent saves a change to one of these while signed in to that account, the account gets its own copy and stops following yours. Kepler then shows **This account stopped sharing your {items}** under the account's row.

Expand the warning to see which file the account copied, with the paths of **This account's copy** and **Your {item}**. Then choose one of the following:

- **Share your {item} again**: links the account back to your file. Kepler first asks **Share your {item} with this account again?**: *Its own copy is saved as a backup next to it, so nothing is lost.*
- **Keep its own {item}**: keeps the account's copy. **Share your {item} again** then moves to the account's row menu.

<figure style="text-align:center">
  <a href="/wp-content/uploads/account-config-drift-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/account-config-drift-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Claude Code card in Settings › Agents with two accounts. Under the second account, Personal, an open warning reads This account stopped sharing your settings, names its own copy of settings.json and your /home/alex/.claude/settings.json, and offers Share your settings again and Keep its own settings.">
  </a>
  <figcaption style="text-align:center; color:#888">An added account that stopped sharing your settings.</figcaption>
</figure>

**Removing an account tells you what it will remove.** The **Remove {name}?** dialog works through it in steps:

- Kepler stops the running sessions on the account: *{count} running sessions will be stopped now*.
- Kepler would delete the sessions whose conversations are stored only in this account: *{count} sessions will be permanently deleted*. To keep them, first click **Move to CLI account** under **Keep these conversations**. The sessions stay in their tasks, and removing the account then deletes nothing.
- If you do not move them, **Continue to remove** asks once more: **Permanently delete {count} sessions?** To remove the account, tick *I understand that {count} sessions in {tasks} will be permanently deleted, and that this can't be undone.*

**How many accounts you can add depends on your GitKraken plan.** Pro and higher plans have no limit. If your plan stops covering an account that a running session uses, the session tells you instead of failing silently: *This session runs on a {name} account your plan doesn't cover. Switch it to another account, or upgrade to use this one again.*

### Choosing an account for a session

If 2 or more accounts are signed in, the **Agent** list shows one row per account, labeled with the account name. You pick the agent and the account in one click, in the **New task** composer or in a draft session tab.

<figure style="text-align:center">
  <a href="/wp-content/uploads/account-multiple-selector-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/account-multiple-selector-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Agent list open in the New task composer, grouped by agent. Under a Claude Code heading sit two account rows, CLI (alex.lee@example.com, Acme) with a check mark and Personal, followed by Codex CLI, GitHub Copilot CLI, Cursor, Antigravity, OpenCode and the other agents, then Add another account and Install another agent.">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent list, with one row per account.</figcaption>
</figure>

With one account, the agent keeps a single row, with that account shown beside its name.

A session starts on the account you picked. Later, you can move it to another signed-in account of the same agent and keep the conversation. When more than one account exists, session tabs name the account. If a tab's account has since been removed, the tab reads **(account missing)**.

Kepler reads usage figures from the account the session runs on, not from the first account in the list.

#### Moving a session to another account

To move a session to another account, use any of these:

- **Continue as** on the session's row or tab menu.
- The **Account** row in the composer's **Agent settings**: **Restart conversation as** on a live session, or **Resume as** on a dormant one.
- The agent and account part of a Terminal session's status bar.
- **Continue as {login}** on the usage-limit banner. See [When you hit a usage limit](#when-you-hit-a-usage-limit).
- The **Resume** or **Restart** split button on a dormant session, when another account could take the conversation.

Each list shows the agent's other accounts with their login, color, and usage, and checks the current one. When you pick an account, Kepler restarts the agent with this conversation as that account (*Restarts {name} with this conversation as {login}.*) and confirms **Continued as {login}**.

Some accounts look different in the list:

- An account that keeps its own history is grayed out as **Separate history**: *This account keeps its own history, so it can't read this conversation. Change that in Settings > Agents.*
- A signed-out account offers **Sign in…**.
- An account signed in with an API key or a token has no login name. It reads **Signed in**, and you can pick it like any other.

If the session is busy, with a turn running or work still going in the background, Kepler asks first: **Stop this session and continue as {login}?** **Stop and switch** stops the session and resumes the conversation on the new account. If the session is still restarting, Kepler asks you to try again in a moment.

<!-- TODO(screenshot): Replace — ade-continue-as-01: a live session's Agent settings with the Account row open on Restart conversation as, listing the agent's other signed-in account (needs two signed-in accounts of one agent). -->

***

## Signing in through your browser

Claude Code and Codex both sign in through your browser, without a terminal. To sign in, open **Settings → Agents**, click **Sign in**, and pick a method under **Choose how you want to authenticate.**

| Connection | Claude Code | Codex |
|---|---|---|
| Local | Kepler runs the sign-in, your browser opens, and Kepler shows a status line instead of a terminal | Browser sign-in with your ChatGPT account |
| Remote or SSH | **Sign in with browser**: *Open Claude sign-in in your local browser, then paste the code it returns. Signs in the remote target directly.* | **ChatGPT (device code)**: *Sign in with a one-time code in your browser. Works on any remote.* |

A local sign-in offers these controls:

- **Open sign-in in browser**: opens the sign-in page if the browser did not open on its own.
- **Sign-in link**, with **Copy link**: the same address, so you can open it in another browser or profile. The field stays after the browser opens, because a browser can open where you cannot see it.
- **Paste the code from your browser**, with **Paste from clipboard** and **Submit code**: appears if the callback cannot complete. A rejected code shows *That code was rejected. Copy the full code and try again.*

On a remote, the same button and **Sign-in link** field sit above the code. Codex shows a **One-time code** to enter there, and Claude Code shows a field for the code your browser returns. If your ChatGPT workspace turns off device sign-in, use **Import local Codex login** or an API key instead.

Auggie signs in the same way locally. On a remote target, Auggie asks you to paste the JSON it returns. GitHub Copilot uses a device code: click **Sign in with GitHub**, then enter a one-time code at `github.com/login/device`.

On a remote Codex target you can also **Import local Codex login** to copy your local auth cache to that target. See [Remote Environments](/kepler/remote-environments).

Kepler warns you before a login lapses: *{N} days left before your {agent} login expires. Sign in again to renew it.*

***

## How a session runs

A session runs in one of 2 modes. Most agents offer both; see the table of agents below.

| Mode | What it is |
|---|---|
| **Chat** (the default) | *{agent} built into Kepler, with replies, diffs and plans you can read, review and search.* Kepler drives the agent over the Agent Client Protocol (ACP) and renders the conversation itself |
| **Terminal** | *{agent}'s own command-line app, with its commands, shortcuts and settings, just as you use it today.* It runs in an embedded terminal inside the task |

<figure style="text-align:center">
  <a href="/wp-content/uploads/opens-in-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/opens-in-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Claude Code card in Settings › Agents, with the New sessions start in row ringed, set to Chat, and the help text You can pick the other one when you start a session.">
  </a>
  <figcaption style="text-align:center; color:#888">New sessions start in, on an agent's card in Settings → Agents.</figcaption>
</figure>


To set an agent's default mode, open **Settings → Agents → *your agent* → New sessions start in**. Each agent has its own default, so Claude Code can start in Chat while Codex starts in Terminal. To start one session in the other mode without changing the default, set **Start in** in the draft's **Agent settings**. In a menu that lists agents, such as **New session here** on a row in the context panel, an agent that offers both modes also has a **Start in Terminal** or **Start in Chat** button. An agent that offers only one mode shows no switch.

To move an existing session to the other mode, choose **Continue in Terminal** or **Continue in Chat** on its row or tab menu. Where the CLI can, the session resumes the same conversation in the other mode; where it cannot, the session starts fresh. Kepler confirms **Continued in Terminal** or **Continued in Chat**, or reports **Unable to switch this session**.

If the session is busy, with a turn running or work still going in the background, Kepler asks first: **Stop this session and continue in Terminal?** (or **in Chat?**). Moving to Terminal also warns you if the session has queued messages, because Kepler discards them. **Stop and switch** stops the session and resumes the conversation in the other mode.

2 limits apply. You must take over a session started outside Kepler before you can move it, and only a session on a task can move to Terminal.

<figure style="text-align:center">
  <a href="/wp-content/uploads/continue-in-terminal-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/continue-in-terminal-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The menu of a Chat session, opened from its row in the task page's context panel: Open, Show Agent Graph, Rename session, Copy session link, New session from this one, Continue in Terminal, Restart agent, Shut down agent, Archive session and Delete session.">
  </a>
  <figcaption style="text-align:center; color:#888">Continue in Terminal, on a Chat session's row menu.</figcaption>
</figure>

| Agent | Modes |
|---|---|
| Claude Code, Codex, GitHub Copilot, Cursor, OpenCode, Auggie, Grok Build | Chat or Terminal |
| Google Antigravity | Terminal by default. Chat runs Google's separate Antigravity ACP server, once it is installed and you pick **Chat** for the agent |
| Pi | Terminal only. Its CLI does not support ACP |
| Your own agent server | Whichever its command supports |

Kepler decides what Terminal mode offers for an agent from the CLI's own flags, not from a list of agent names. A custom agent therefore behaves like a built-in one: if the CLI has no flag for a control, Kepler hides the control instead of showing one that does nothing.

A Terminal launch offers the options each CLI accepts on its own command line:

| Agent | Launch options in Terminal |
|---|---|
| Claude Code | Effort |
| Codex | Approval mode and reasoning effort |
| GitHub Copilot | **Reasoning effort** and **Model**, besides the context size |
| Auggie | **Reasoning effort**, per model |
| Cursor | Plan or ask mode |
| Grok Build | Permission mode: **Default**, **Accept edits**, **Auto**, **Don't ask**, or **Plan** |
| Pi | **Thinking**, from **Off** to **Max** |
| OpenCode | Model and agent, for a new session only; a resumed session keeps its own |

If the installed version supports it, GitHub Copilot, Cursor, OpenCode, and Pi also take your first message on the command line, so the message reaches the CLI as it starts.

### What's different in Terminal

Terminal mode is a full session, not a fallback. Kepler adds what a bare terminal cannot give the running CLI:

- The task's shared context.
- Kepler's workspace tools, where the CLI can load them.
- Permission prompts that you answer in Kepler.
- A transcript that survives a restart.

A Terminal session's pane has 3 parts:

| Part | What it does |
|---|---|
| The terminal | The agent's real interface, keys and all |
| The status bar | The session at a glance, then your plan usage. See below |
| The composer | Kepler's own message box, with attachments, voice input, and the agent-settings pill |

<figure style="text-align:center">
  <a href="/wp-content/uploads/terminal-session-status-bar-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/terminal-session-status-bar-oct-2026.png" class="help-center-img img-bordered" alt="A Claude Code session running in Terminal mode, with the CLI's own prompt above Kepler's status bar. The bar shows a green status dot, the agent and account, Opus 5.5 at Medium effort in Auto mode, the context ring, the branch, the 5-hour usage meter, and Rich input.">
  </a>
  <figcaption style="text-align:center; color:#888">A Terminal session, with Kepler's status bar along the bottom.</figcaption>
</figure>
<!-- TODO(screenshot): Replace — ade-terminal-session-status-bar-01: a Claude Code Terminal session on v0.15 with the status bar showing the status dot, the agent and account unit, model, effort and mode, the context ring, the branch, the plan usage bars, and Rich input. -->

From left to right, the status bar shows the following:

| Part | What it shows |
|---|---|
| Status dot | The session's state and, once it is idle, how long since the model last replied |
| Agent and account | Tinted with the account's color when it has one, and drawn in a warning tone when the account's limit is spent. Click it for **Restart conversation as** to move the session to another account |
| Model, effort, and mode | What the *running* CLI reports, not what you picked at launch, so a change made inside the CLI shows here |
| Context ring | The share of the context window in use. Hover for tokens used, available, and total, the estimated cost at API rates, and the prompt cache |
| Branch | The session's branch, with a folder mark when the CLI reports working in a subfolder or outside the worktree. Outside the worktree, the tip's folder line reads **Outside this worktree** |
| Plan usage | 2 bars for the **5h** and **7d** windows, colored by pace. Hover for the full readout; see [Usage indicators](#usage-indicators) |
| **Rich input** | Shows or hides Kepler's message composer. Hide it to type straight into the CLI |
| **No Kepler tools** | Shown when the agent cannot use Kepler's workspace tools or inbox in a terminal. Its tip points to **Continue in Chat** on the session menu |
| **Idle detection** | Shown for an agent that Kepler does not receive hook events from: *Activity is inferred from the terminal going quiet, because Kepler doesn't receive status events from this agent.* |
| Program status | Shown in place of **Idle detection** when the program in the terminal reports its own status. See below |

For an agent that cannot tell Kepler it is waiting on you, the status dot's tip adds *{name} doesn't report when it's waiting on you, so check the terminal when it goes quiet.*

Hover any part to see its card, and click to pin the card open. When the bar is narrow, it hides the least important parts first and shows them again as soon as they fit.

Hover an idle session's status to see its **Last reply** and **Last prompt**. When the prompt cache is about to expire or has expired, the card also shows **Prompt cache**. Once the cache expires, an idle session's next prompt can re-read its whole context without telling you.

**Idle detection** tells you that Kepler's status for this agent is less precise. If an agent reports hook events, Kepler knows when a turn starts and ends. If it does not, Kepler infers the same thing from the terminal going quiet, which is less exact: a long pause mid-turn can read as idle.

Some terminal programs report their own status to Kepler through the OSC 7501 escape sequence. When a program does, the status bar names that status, with any message and progress the program sends. The hover card shows the following:

- The status, and how long the program has been in it.
- Progress as a bar (*{percent}% done*).
- Any sub-tasks, each with its own age and message.
- *Reported by {app}*, when the app is not already the tab's name.
- The next step, when a blocked or failed program gives no reason, such as *Approve it in the terminal.* or *No reason given. Check the terminal.*

The status sets the session's working, blocked, or done state without hooks:

| Status | Meaning |
|---|---|
| **Running** | The program is working |
| **Needs you** | The program is waiting for you |
| **Needs your approval** | The program is asking for a permission |
| **Needs your answer** | The program asked a question |
| **Needs you to sign in** | The program needs you to sign in |
| **Done** | The program finished its work |
| **Failed** | The program reported an error |
| **Idle** | The program is doing nothing |

If hook events arrive from the same process, the hooks take precedence.

A Terminal session tracked through hooks reports a failed turn too. When a Claude Code, GitHub Copilot, or OpenCode turn fails, for example on a usage limit, a rate limit, or a server error, the session shows **Error** with the CLI's own message once the turn stops. For a usage limit, that message usually says when the limit resets.

In a Terminal session, the composer's **Agent settings** pill shows the model, effort, and mode the session uses, but you cannot change them there. The pill's tooltip ends *Change these in the terminal*. Change them in the CLI itself. An effort or mode you change in the CLI survives a relaunch of the session.

Terminal sessions also differ in these ways:

- **Queued review comments wait in a bar** when the composer is hidden. The bar reads **{count} comments to send**, with the comments chip, **Add a message** to open the composer with the comments attached, and **Send comments** to send them on their own. **Send comments** waits while the terminal is starting (*Send once the terminal has started*), while another message is going out, and after the session exits (*Resume the session to send these comments*).
- **A pasted image reaches the agent as an image.** When you paste an image into a Claude Code or Codex terminal, Kepler hands it to the CLI the way a paste into the CLI's own terminal would. The agent reads it as an image, not as a path it has to open.
- **A terminal session's conversation is recorded**, so quitting Kepler, an idle shutdown, a restart, or a reboot does not lose it. Reopening reattaches to the same conversation with its scrollback intact, and the session keeps running through a context compaction.
- **A first message that Kepler cannot safely type at launch** waits in the composer as a ready-to-send draft instead: *Your message is ready to send. {name} starts without it, so send it once the terminal is ready.*
- **A first message that Kepler cannot confirm** is not silently resent. Kepler holds it, says why, and asks you to *Check the terminal before resending.* The reason reads, for example, *Kepler was unable to read {name}'s version, so it can't confirm {name} is ready.* or *The message was too long to pass to {name} at startup.*
- **Lost keystrokes are never resent.** If Kepler cannot tell whether your last keystrokes reached the terminal, it warns *Your last keystrokes may not have arrived* and asks you to *Check what the terminal shows before you go on.* Kepler never resends that input, now or later. Typing resumes on its own once the input in flight settles.
- **A terminal reattaches instead of restarting.** While it loads, it reads **Loading terminal…**. A short reconnect shows nothing. After a second, a **Reconnecting to the terminal…** strip appears, and the last screen stays readable and scrollable. Only after 5 seconds does a cover hide the terminal. If the terminal cannot reconnect, **Unable to restore this terminal** says *The terminal is still running. Retry to load its output again.*, with **Retry**.
- **What you type during a reconnect is held**, and sent once the terminal is back. If the program printed in the meantime, Kepler drops your typing instead of typing into a changed screen: **The terminal changed while reconnecting**, *Nothing you typed was sent. Type it again.* If your typing could never be sent, Kepler shows **Unable to send what you typed**.
- **One view types at a time.** A terminal that another view is driving, in another window or on a Remote Access device, reads **Another view is controlling this terminal**. Click **Take control** to type here and size the terminal to this view.
- **Fast output is trimmed, not queued.** A terminal printing faster than the connection can show reads **Showing the latest output**: *This terminal is printing faster than this connection can show, so older lines are skipped.*

<div class="note" markdown="1">

**A terminal session is not the same as a terminal.** A terminal session runs an *agent*, lives in the **Sessions** column, and carries the task's context. A plain terminal runs your shell, lives in the drawer beneath the columns, and carries none. See [The Task View](/kepler/task-view#the-terminal-drawer).

</div>

***

## Sessions started outside Kepler

Kepler also finds agent conversations that it did not start. For example, you might run `claude` in a terminal, or return a week later to a transcript that is still on disk. Kepler lists both as agent sessions.

Kepler takes over a conversation only when you ask. It binds the conversation to a task, and it does not take control of the terminal that runs it.

### Turning detection on

Detection is on by default. To turn it on or off, use **Settings → Integrations → Your terminal → Show sessions started outside Kepler**.

The switch installs GitKraken hooks, so each agent's own CLI reports what it is doing to Kepler. The one switch covers every agent that Kepler can track this way: **Claude Code**, **Codex**, **Cursor**, **GitHub Copilot**, **OpenCode**, **Auggie**, **Grok Build**, and **Pi**. Kepler does not track Google Antigravity through hooks. Turning the switch off stops reporting from all of them.

Kepler follows **Terminal** sessions through the same hooks. If a live session's hook events stop arriving, Kepler warns you so that status and notifications do not go out of date: **Agent sessions aren't reporting to Kepler**, *Session status and notifications may be out of date. Repair reinstalls the reporting configuration.* After you click **Repair**, restart any session that still does not report. A window that only views sessions running on another computer shows the warning without **Repair**: *To repair reporting, use Kepler on the computer running these sessions.*

Detection makes a *live* outside session visible. Kepler reads **past** sessions from the transcripts the agent already writes to disk, so it can find a conversation from before you turned detection on. Kepler just could not follow that conversation while it ran.

To find these sessions in Kepler, see [The Kepler Interface](/kepler/kepler-interface#external-sessions). To turn one into a task, see [Create a task](/kepler/create-task#from-a-session-you-already-started).

### Reading one

An outside session opens read-only, marked **(external)** and **External**, with its transcript labeled **Session transcript (read-only)**. Its context card shows a badge for its state and one sentence that says where the conversation lives and what you can do about it in Kepler.

| Badge | What it means |
|---|---|
| **Running** | Working on a turn, outside Kepler |
| **Waiting on you** | Blocked on a question or a permission request in its own interface |
| **Idle** | Connected and doing nothing |
| **Ended** | The process finished |
| **Not running** | Found on disk, with nothing running it anywhere |

The sentence matches the badge. A running session reads *Follow along here.* A waiting one reads *Answer it in your terminal.* Kepler does not answer a prompt it does not own, but it notifies you that the session is waiting, whatever the agent.

When you pick a live outside session from **Open an external session**, it always opens this way, read-only in its task. Picking it never takes the conversation over.

Kepler reads the transcripts of **Claude Code**, **Codex**, **GitHub Copilot**, **OpenCode**, **Auggie**, **Grok Build**, **Pi**, and the **Google Antigravity** CLI from each agent's own store on disk, without starting the agent. A few agents behave differently:

- A GitHub Copilot autopilot run ends with its completion summary, shown as the agent's answer.
- A GitHub Copilot session run in **Chat** has a transcript on disk once it has run a turn.
- A **Cursor** session still appears as a row and you can still adopt it, but it shows *Preview isn't available for {adapter} sessions yet.* in place of the conversation.

<figure style="text-align:center">
  <a href="/wp-content/uploads/external-past-session-preview-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/external-past-session-preview-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The preview of a past Pi session started outside Kepler, marked Not running, with its folder, Import session and Create new task, and the replayed conversation: the prompt, the agent's replies, and its Read products.js call.">
  </a>
  <figcaption style="text-align:center; color:#888">A past Pi session, previewed read-only from its transcript on disk.</figcaption>
</figure>

Kepler leaves some conversations out of the list: OpenCode's archived and subagent sessions, and Grok Build and Antigravity conversations with no messages yet. Kepler replays an Antigravity conversation but does not follow it live.

If Kepler cannot read a transcript, it says which problem it hit instead of showing an empty conversation:

| What you see | What it means |
|---|---|
| **No transcript to show** | Kepler could not find the file. It may predate detection, the agent may store it somewhere Kepler does not look, or the agent never wrote one, as with a session that never ran a turn |
| **Kepler can't read this session's transcript** | The file exists, but Kepler could not open it. Check its permissions; Kepler keeps retrying |
| **Waiting for activity…** | The agent has not written anything yet |

If a live session goes quiet, Kepler flags it instead of showing it as busy: *No activity for {minutes} minutes. The session may have ended without reporting it.*

### Taking one over

You can take over an outside session in 2 ways. They differ in what happens to the terminal you started it in:

| Button | What it does |
|---|---|
| **Fork** | *Copies this conversation into a new Kepler session. Your terminal keeps the original.* Both continue independently |
| **Continue here** | *Carries on this conversation in Kepler.* One conversation, now owned by Kepler |

Both buttons stay on screen while the session works, but they work only once it is idle. Hover a button to see why it is unavailable: *Available once it is idle.*, or *Answer it in your terminal first.* while the session waits on you.

If a terminal still owns the session, **Continue here** first asks **Continue this conversation here?** If 2 clients write the same conversation, they corrupt it: *If your terminal is still open, both will write to this conversation. Close it there first.* Once Kepler has the conversation, the view shows *Ready to continue here.*

When you take over a conversation from disk, the agent starts on your first message, not when you take it over. Adopting one costs nothing.

***

## Sending a prompt

To send a prompt, type it in the composer at the bottom of the session.

<figure style="text-align:center">
  <a href="/wp-content/uploads/sending-a-prompt-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/sending-a-prompt-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The session composer with a pasted image.png attached as a thumbnail chip and the draft @cart.js @README.md Does the check also cover these codes? Below the draft sit Attach a file and the microphone, then the Agent settings pill (Docs Model, Build, with its chevron), the context usage ring, and Send with its chevron.">
  </a>
  <figcaption style="text-align:center; color:#888">The composer, at the bottom of the session.</figcaption>
</figure>

The composer has these controls:

| Control | What it does |
|---|---|
| **Attach a file** | Attaches a file for the agent to read; you can also drag files onto the composer (*Drop files to attach*). On a remote connection, **Add a file from the remote** picks a file from the remote machine |
| Microphone | Voice input. See [Voice Input](/kepler/voice-input) |
| **Agent settings** | Agent, model, permission mode, effort, and options |
| Context usage | The share of the session's context window in use, drawn as a ring. Hover to see tokens used, available, and total, the estimated cost at API rates, and the prompt cache |
| Plan usage | Your provider plan's usage windows and when each resets. See [Usage indicators](#usage-indicators) |
| **Send** | Sends the prompt, and shows a sending state from the moment you click. The chevron holds **Send** and every applicable Action |

**Attaching a file sends a path, not a copy, wherever it can.** If the session's machine can already read the file, Kepler sends a path to it. That covers a file you drop, paste, or pick on the same machine, or pick from the remote in a remote window. The file's chip reads *File on this machine* or *File on the machine*. Kepler uploads any other file once into the task, and its chip reads *Copied to the task when you send*.

A send is all or nothing: if an upload fails, Kepler does not send the message (*Unable to upload {name}. Your message wasn't sent.*). Where the window can reach the file's machine, an attached file's card on the task page offers **Open in default app** and one of **Show in Finder** (macOS), **Show in Explorer** (Windows), or **Show in file manager** (Linux).

**A long paste becomes an attachment.** If you paste more than 32 KB of text, such as a long log, Kepler attaches it as a text file named for its length, such as `pasted-text-800-lines.txt`. Kepler puts the file name in your prompt where the text would have gone. To drop the attachment, remove the chip. Kepler refuses a paste larger than the attachment limit as too large, and pastes nothing. Long pastes work this way in every composer that takes attachments, including the **New task** composer and Ask Kepler.

<figure style="text-align:center">
  <a href="/wp-content/uploads/pasted-text-attachment-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/pasted-text-attachment-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task session's composer after pasting a long test log: the text became an attachment chip, pasted-text-800-lines.txt with a remove button, above the prompt Why does the cart test fail in this log? pasted-text-800-lines.txt, with the attach and microphone buttons, the Docs Model Build pill and Send.">
  </a>
  <figcaption style="text-align:center; color:#888">A long paste, attached as a text file.</figcaption>
</figure>

**A pasted pull request or issue link becomes a chip.** Paste the URL of a pull request or issue from a connected GitHub, GitLab, Bitbucket, or Azure DevOps host, self-hosted included, or of a Jira or Linear issue. In a task's session composer or the **New task** composer, Kepler turns the URL into a chip labeled with its number, such as **#49**, and puts the label in your text in its place. Hover the chip to see the title and the URL. When you send, Kepler attaches the link to the task. A prompt that is a slash command keeps the URL as typed.

<figure style="text-align:center">
  <a href="/wp-content/uploads/pasted-link-chip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/pasted-link-chip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task session's composer after pasting a pull request link: a chip with the pull request icon and #49 sits above the prompt Does this conflict with #49?, and its tooltip shows the pull request's title, Round prices through a shared roundCents helper, over its GitHub URL.">
  </a>
  <figcaption style="text-align:center; color:#888">A pasted pull request link, turned into a chip.</figcaption>
</figure>

**Review comments wait in a chip until you send.** Comments you queue for a session while you review its changes collect in one chip on its composer, such as **2 comments**. Click the chip to list them by file and line. Click a comment to open its place in the file, or click its **X** to remove it from the queue. The chip's own **X** removes all of them. Your next message sends the queued comments first, ahead of what you typed. You can also send them with an empty prompt. A slash command is sent alone, and the comments wait for the next message. See [Review Changes](/kepler/review-changes).

<figure style="text-align:center">
  <a href="/wp-content/uploads/queued-comments-chip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/queued-comments-chip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A session composer with the 2 comments chip open above it: the Queued comments list holds cart.js:3 over Clamp at zero so a discount larger than t… and cart.js:4 over Pull 100 into a CENTS constant; the sam…, each with an X to remove it from the queue. The chip has its own X to remove all comments from the queue; below it sit Type a message..., Attach, the microphone, the Docs Model and Build agent settings, and Send.">
  </a>
  <figcaption style="text-align:center; color:#888">Two review comments queued for the next message.</figcaption>
</figure>

A draft you have not sent survives a reload.

The composer works with these keys:

- **Enter** sends; **Shift+Enter** inserts a newline.
- **Tab** moves focus from the prompt to **Send**, then to its chevron.
- **Down Arrow** or **Alt+Down** on **Send** opens the chevron's menu. Closing the menu returns focus to **Send**.
- **Cmd/Ctrl+F** opens **Find in conversation**.
- To type a prompt, start typing anywhere in the session. The composer takes the keystroke, so you do not have to click into it first.

The agent pill sits beside **Send** in every composer, so the launcher and a live session look the same. The agent picker is a list of labeled rows. For agents with long option lists, the agent-settings menus have a **Search options…** box. Every control has a tooltip.

While a turn is running, the send button adds a stop segment: *Interrupt current work. Queued messages will be sent next.* **Send** stays available the whole time, because a message sent to a busy session steers it.

### Slash commands and skills, per repository

Type `/` to open the command menu. It lists the agent's built-in commands together with your commands and skills. A slash command sent as a session's first prompt runs as a real command, not as text.

In a Claude Code **Chat** session, `/design` and `/slides` work as they do in the CLI, and Claude can publish artifacts once **Artifacts** is on for the session. See [Claude artifacts](#claude-artifacts).

Codex marks its skills with a `$` sigil and invokes them that way, so `$` opens a skills-only menu. `/` also finds Codex skills, matched on the bare name, so you do not need to know the convention.

**Kepler finds skills and slash commands per repository, not per agent.** The catalog combines your home-directory skills and the repository or worktree's own. For Claude Code, that is `~/.claude/skills` plus `.claude/skills`. As a result:

- One project's skills never show up in another project's menu.
- A skill added in a worktree and not yet committed can appear in that session before it appears elsewhere.

Kepler reads the catalog when you pick a repository and refreshes it whenever a live session reports a change. A skill you add mid-session shows up without a restart.

### Mentioning files

Type `@` to search the working directory and insert a path. A session that runs in the task folder also lists the task's other worktrees and folders, under **Worktrees and folders** above **Files**. To search inside one, pick it, or type its name and `/`. A path with spaces goes in quotes (`@"…"`), and Kepler adds the quotes when you pick such a path. `@` also works in composers that do not belong to a session yet, where it searches the task's folders or the folder you chose. Kepler automatically approves files you paste into a chat for the agent to read.

***

## Steering a running turn

You do not have to wait for a turn to end. **If you send a message while the agent is working, the message steers the agent** instead of waiting until the turn is over.

When you send during a turn, the message goes into a visible queue. The placeholder changes to *Type a message to queue...*, and a banner above the composer counts what is waiting. Kepler then sends the queue as **one merged follow-up prompt** at the earliest safe moment:

| When it goes | Why |
|---|---|
| Immediately | The agent supports steering, and none of its own tool calls is running |
| At the next tool-call boundary | A tool call is running and cannot be interrupted partway through |
| At the end of the turn | The agent does not support steering |

A background subagent's tool call never delays your message; only the main turn's own calls do.

Kepler merges everything you send during one turn and delivers it together. 2 quick corrections arrive as a single instruction instead of 2 competing ones.

<figure style="text-align:center">
  <a href="/wp-content/uploads/firing-into-a-running-session-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/firing-into-a-running-session-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="A running session in a task's side panel: the agent's plan at 1 of 3, its turn still running on Run npm test, and below it 1 queued with Interrupt & send and Clear queue, holding the prompt Also cover gift card codes with surrounding spaces. The composer reads Type a message to queue….">
  </a>
  <figcaption style="text-align:center; color:#888">A prompt queued behind an agent's current work.</figcaption>
</figure>

| In the banner | What it does |
|---|---|
| **{count} queued** | How many prompts are waiting. It adds **Sending queue…** while the queue goes out and **Stopping…** while a stop is pending |
| A queued row | The prompt's text and its attachments, or a paperclip and filename when it is attachments only |
| *Sending at {time}, when the quota resets.* | The account hit a usage limit, so the queue waits for the reset instead of sending into the limit. See [Usage indicators](#usage-indicators) |
| **Send now** | Sends a queue held for a usage limit right away |
| **×** on a row | Removes that one prompt |
| **Clear queue** | Removes all of them |
| **Send queue** | Sends a queue left waiting on a session that is no longer working |
| **Interrupt & send** | Stops the current turn and delivers the queue immediately, in one step. **Cmd/Ctrl+Shift+Enter** does the same from the keyboard |

With subagents running, **Interrupt & send** names them: **Interrupt & send ({count} running)**. If the stop gets no answer, the button becomes **Force quit (drops {count} queued)**, which ends the agent and drops the queued prompts instead of sending them.

Queued prompts survive an interruption and a restart of Kepler. A **disconnect**, an expired token that forces **re-authentication**, and the **reconnect** afterwards also keep the queue. The rows stay on screen, nothing is dropped, and Kepler hands the prompts to the reconnected session in the same order, under the same identities. Canceling a turn promotes the next queued prompt instead of discarding it.

Each queued prompt picks up the task's shared context as it stands when the prompt runs, not as it stood when you typed it.

If a send fails, Kepler puts the text back: *Something went wrong. Your message is back in the composer — try again.* If you have since typed a newer draft, Kepler keeps the newer draft and offers **Restore message**.

### Stopping a turn

| What you do | What happens |
|---|---|
| **Escape** | Stops the running turn |
| The stop segment on the send button | Stops the running turn. Its tooltip says what happens to the queue |
| **Cmd/Ctrl+Shift+Enter** | **Interrupt & send**: stops the turn *and* delivers what you typed |
| **Force quit the agent** | Offered once a cancel has been pending too long. It does not wait for the agent to settle |

If a cancel takes too long, Kepler offers **Force quit the agent**, so you are not left with a button that seems to do nothing.

In **Terminal** mode, Kepler recognizes an interrupt whether it arrives as **Escape** or as **Ctrl+C**. The turn counts as canceled only once both the CLI's hooks and its output have gone quiet, so a stopped session no longer looks as though it is still working.

***

## Reading the conversation

A session's conversation shows your prompts, the agent's replies, and the agent's work:

- Your messages appear as chat bubbles. Right-click one to **Copy message**, **Quote**, **Ask**, or **New session from here**.
- Agent replies render as Markdown and stream as one continuous message, even when a tool runs mid-reply. Right-click a reply to act on its whole turn. While the menu is open, a band outlines the turn, and **Copy message** copies all of the main agent's text in that turn. Every message menu starts with the message's exact time.
- Each prompt, and the reply that closes each turn, has a copy button beneath it.
- Each message shows when it was sent, and a divider marks a long gap between messages.
- An agent's thinking shows as a collapsed **Thinking** block, for agents that send it.
- A file path an agent writes (a link, an inline-code path, or the file in a read or edit tool call) becomes a link once Kepler confirms the file exists. Click it, or **Cmd/Ctrl+click** it, to open the file in Kepler at the named line. A file inside a worktree opens in the Changes overlay's file view. **Cmd/Ctrl+Shift+click** opens the file in your default editor at that line, or in Kepler if no editor opens it; the link's tooltip says so (**+ Click to open in editor**). A middle-click works like a plain click.
- A Kepler task or session link in the conversation opens inside Kepler when you click or middle-click it. Hover it to see where it goes. Right-click it for **Open in Kepler** and **Copy link**.
- Images in replies and tool output open in a lightbox. You can save the image from the thumbnail or the lightbox with **Save as…**.
- Tool calls collapse into groups: **{count} tool uses**, with **{count} done**, **{count} running**, and **{count} failed** tallies. Expand a group to read any call's output. A failed call that the agent has already moved past stays folded inside the collapsed group, and the failed tally still counts it.
- A plan renders as **Plan {completed}/{total}**. A plan cut short by a stop is marked **Interrupted**.
- A context compaction shows as its own row: **Compacting the conversation…**, then **Conversation compacted**, **Unable to compact the conversation** with the error, or **Compaction stopped**. When the agent kept a summary of the conversation so far, the row expands to show it, and **Find in conversation** searches it.
- Each subagent has its own card, collapsed by default, with **Prompt**, **Operations**, and **Result** sections that fold independently. The card's header row shows the subagent type, the description it was given, how many operations it has run, the step a running subagent is on, and a status of **Running**, **Stopped**, **Completed**, or **Failed**. You can follow progress without expanding the card. Claude Code, GitHub Copilot, Cursor, and OpenCode Chat sessions all produce these cards. A subagent that was canceled or cut off reads **Stopped**, not **Failed**.
- A session that another session started shows **Started by** and the starting session in its header. Click it to open that session.
- A prompt that another session sent has a **From:** header naming the sending session. Click it to open that session.
- A turn that ended for a notable reason has a pill: **Reached token limit**, **Reached request limit**, **Refused to continue**, or **Cancelled**. A turn that ended normally shows no pill.

<figure style="text-align:center">
  <a href="/wp-content/uploads/compaction-row-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/compaction-row-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A Chat transcript in which, after the Read checkout.js call and the agent's note, a Conversation compacted row is open on the summary the agent kept of the conversation so far, followed by Edit checkout.js and the agent's next message.">
  </a>
  <figcaption style="text-align:center; color:#888">A compaction row, expanded to the summary the agent kept.</figcaption>
</figure>

Kepler keeps subagent work separate from the main thread:

- A subagent's own tool calls nest inside its card under **Operations**, not alongside the main agent's calls.
- A subagent's narration renders in an indented lane marked **Subagent**, so you can see where it starts and stops even when it interleaves with the main agent's text.
- A subagent can start subagents of its own. Their cards nest inside its card, and the outer card counts every permission request waiting anywhere beneath it. A request from a nested subagent shows on the outer card under a path of subagent names, such as **Parent › Child**.
- While a turn is running, that turn's subagent cards pin to the top of the session. They return to their place in the conversation when the turn ends. A card you expanded stays expanded for the rest of the turn.

To read a subagent's own transcript, click **Open subagent transcript** on its card or on its running chip above the composer. The transcript shows the subagent's prompt, then its narration and tool calls in the order they happened, then its result. The transcript updates live while the subagent runs, and the card and chip show the step in progress.

The pane's subtitle shows the current step on one line. When the step is longer, **Show full step** expands it and **Hide full step** folds it again. In a wide pane, the transcript docks beside the chat. In a narrow pane, it covers the chat, with **Back to {title}** to return. While the transcript is open, you answer a permission request raised inside the subagent in that pane.

In a Claude Code or Codex Chat session, you can also direct one subagent from its pane instead of the whole turn:

- **Message {name}**: sends the subagent a message through the main agent. The pane notes *Sent through the main agent*, or *Waiting for the main agent* while the main agent is busy. You cannot pass on a slash command. If the subagent has already finished, the pane reports *Unable to deliver the message to {name}, which may have finished*.
- **Stop** (Claude Code): ends that subagent alone. Codex offers **Ask to stop** instead, which asks the main agent to stop the subagent.

For other agents, the pane is marked **read-only**.

<!-- TODO(screenshot): Replace — ade-subagent-pane-01: a Claude Code Chat session with a running subagent's pane docked beside the chat, showing Stop, the current step, and the Message {name} box with Sent through the main agent. -->

A Claude Code session can keep **background tasks** running after its turn ends, such as a monitor or a backgrounded shell. In any Chat or Terminal session, the background tasks also include another agent's CLI that the session starts for its own work, such as a `claude` or `codex` run from the agent's shell. While that CLI is busy, the list shows it as the agent's name and the start of its prompt.

Background work affects the session's status in 2 ways:

- Work the turn still depends on, such as a subagent, a workflow, or a busy child agent, keeps the session **Running**.
- Work the agent left running on its own, such as a backgrounded shell or a monitor, does not. The turn ends, and the session is idle and reads **Background task running**.

A background task's card reads **Running in background**. To stop that one task without affecting the session, click **Stop background task** on the card or its chip.

Code blocks have a **line-wrap toggle**, so you can read a long line without scrolling sideways. They take their syntax colors from your Kepler theme. A code block longer than 15 lines folds to a 15-line preview with **Show {count} more lines** and **Show less**. A match from **Find in conversation** inside a folded block opens it. Numbered lists stay continuous instead of restarting at 1 after an interruption.

### Claude artifacts

You turn artifacts on or off for each Claude Code Chat session, because the artifact tools add about 12k tokens to the session's context. A new session starts with artifacts off unless **Settings → Agents → Claude Code → Artifacts in new sessions** is on.

To turn artifacts on for one session, tick **Artifacts** in its composer's **Agent settings**: *Lets the agent publish pages and designs. Adds about 12k tokens to the session's context. Turning it on in a running conversation restarts the session.* In a running conversation, Kepler asks first, **Turn on Artifacts?**: *The session restarts and resumes this conversation. The running turn, background shells and subagents, and queued messages end. Artifacts stay on for this conversation.* From then on, the row reads **On for this conversation**. While a session is still starting, the row reads **Available once the session has started**.

<!-- TODO(screenshot): Replace — ade-artifacts-toggle-01: a live Claude Code Chat session's Agent settings showing the Artifacts checkbox with its description (needs a signed-in Claude Code). -->

When a Claude Code Chat session with artifacts on publishes an artifact, including `/design` and `/slides` output, the artifact shows as a card instead of a tool call: title, version, **Private**, **Open**, **Copy link**, and **Preview**. A republish reads **Updated to v{seq}**. Kepler also attaches the artifact to the task as a link, so you can still reach it after the conversation moves on.

**Preview** opens the published page in a pane beside the chat, loaded from the local file the session published, with **Reload** and **Close preview**.

Approvals name what Claude is about to do instead of showing raw tool input, for example *Publish a new private page?*, *Update to a new version?*, or *Permanently delete?*

Anyone with edit access to a published artifact can comment on it. By default, a comment starts a turn in the session that published it, and the session posts a reply automatically. The first time a session publishes, the **Artifact comments can start turns** notice offers **Keep on** or **Turn off**. To change this later, use **Settings → Agents → Claude Code → Let artifact comments start turns**. Running sessions keep the value they started with, and the setting lists them with **Restart all** and **Restart selected ({count})**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/artifact-card-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/artifact-card-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A published artifact shown as a card in a session's chat: its icon, the title Acme gift cards with v1 beside it, a Private lock below, and Preview, Open and a copy link button.">
  </a>
  <figcaption style="text-align:center; color:#888">A published artifact's card in the chat.</figcaption>
</figure>
<!-- TODO(screenshot): New: The Artifact comments can start turns notice under a Claude Code Chat session's first artifact card, with Keep on and Turn off. -->

<figure style="text-align:center">
  <a href="/wp-content/uploads/artifact-chip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/artifact-chip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The artifact attached to the task as a link chip, Acme gift cards, under the task's worktree button, with its hover card open showing the artifact's title, its link, Open and Copy link.">
  </a>
  <figcaption style="text-align:center; color:#888">The published artifact, attached to the task as a link.</figcaption>
</figure>
<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-artifact-preview-01-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-artifact-preview-01-v2@2x.png" class="help-center-img img-bordered" alt="A session with an Acme gift cards artifact card (v1, Private, Preview, Open) in its chat, and the artifact's Preview pane docked beside the chat: the rendered gift-card landing page under a header with Local preview, Reload, Open and Close preview.">
  </a>
  <figcaption style="text-align:center; color:#888">An artifact's Preview pane, docked beside the chat.</figcaption>
</figure>

### Scrolling and where you left off

To change how the transcript scrolls and how wide it grows, open **Settings → Appearance → Chat**:

| Setting | What it does |
|---|---|
| **Chat auto-scroll**: **Auto-scroll to the end** | *Keeps the newest output in view. Scroll up to stop.* The default |
| **Chat auto-scroll**: **Stay on my message** | *Keeps your message in view. The transcript doesn't scroll on its own.* |
| **Conversation width** | *How wide the conversation grows in a wide pane. The message box keeps its width.* **Narrow** (the default), **Wide**, or **Full width** |
| **Remember scroll position** | *Return to where you left off when you come back to a session.* On by default |

***

## When the agent asks you something

When an agent needs a decision it cannot make on its own, Kepler pauses and asks you in one of these ways:

- A permission request before a risky tool call.
- A structured question when the agent wants your input mid-task.
- A plan review when the agent proposes a plan before it starts.
- An approval card when the agent asks Kepler itself to do something that needs your approval, such as deleting a worktree.

Reports from other agents arrive in a session's inbox and do not ask you anything; see [Reports from other agents](#reports-from-other-agents).

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-permission-request-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-permission-request-oct-2026.png" class="help-center-img img-bordered" alt="A permission request for a shell command, marked Needs approval, with the agent's reason, Contains brace with quote character, just above the Allow, Allow for this session, and Reject buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">A permission request, with the agent's reason above the buttons.</figcaption>
</figure>

### Permission requests

A permission request pins to the top of the session. It shows an amber shield, the tool being asked about as the heading, and the call's input beneath it. If the agent says why it is asking, the reason appears just above the buttons. For example, a Claude Code session in auto mode can still hit a safety check. A request to reach outside the agent's network sandbox says so in Kepler's own words, *Reaches outside the network sandbox.*, with the agent's reason when it gives one.

The buttons use Kepler's wording, not the agent's, so a request reads the same whichever agent raised it:

| Button | What it does |
|---|---|
| **Allow** | Approves this one call |
| **Allow for this session** | Approves this call, and approves matching follow-up calls automatically for the rest of the session. Kepler tells the agent only that you allowed the call once, so the agent writes no rule of its own |
| **Allow always** | Gives the agent a permanent approval, which the agent stores in its own settings |
| **Reject** | Refuses this call |
| **Reject always** | Refuses it permanently |

You see only the tiers the agent offers. **Allow for this session** is Kepler's own middle tier and appears only next to an **Allow**. A request that offers only a permanent approval, such as Claude Code's plan-exit prompt, has no one-time approval to extend, so it has no middle tier. If an agent offers several permanent choices, Kepler keeps the agent's labels instead of a single **Allow always**. A **RULE** line beneath the buttons spells out any `Tool(...)` pattern a rule would cover.

Kepler combines repeated requests. A command that fires many identical requests, such as an install that reaches the network again and again, asks once, and your answer settles the whole group.

A request raised by a subagent that another subagent started shows on the outermost subagent card, under the path of subagent names that leads to it (**Parent › Child**). See [Reading the conversation](#reading-the-conversation).

Answered requests stay in the transcript, showing the tier you picked: **Allowed for this session** for the middle one, otherwise the button's own label, falling back to **Approved** or **Denied**.

#### Requests that arrive through hooks

A session in **Terminal** mode and a session that Kepler **detected outside itself** both ask through the agent's own hooks instead of over ACP. You still answer in Kepler, without switching to the CLI's own prompt. The card comes from the agent, though, so it offers scopes instead of Kepler's tiers: **Deny**, **Allow once**, and one **Always allow** for each scope the hook suggests, narrowest first:

| Scope | Meaning |
|---|---|
| **this session** | Until this session ends |
| **this project (local)** | This project, your machine only |
| **this project (shared)** | This project, committed for your team |
| **all projects** | Everywhere |

Above the buttons, Kepler shows the rule each button would write. A rule with no command pattern is marked **(this tool)**, which means it covers every call to that tool, not one command.

Kepler never approves a hook request for you. If Kepler stops holding a request before you answer (the turn ends, the conversation moves elsewhere, or Kepler quits), it hands the request back to the CLI, which asks in its own dialog.

A Codex question asked through its hooks shows in Kepler as a question you can answer, with its options and their descriptions. Cursor has no permission or notification hook, so a Cursor Terminal or outside session cannot tell Kepler that it is waiting on you. The session reads **Running** until it stops, and you answer in the terminal.

### Multiple-choice and multi-select questions

Agents can ask you structured questions instead of guessing. The form renders in the conversation at the point where the agent asked. In Chat, Claude Code, Codex, and Cursor questions all arrive in this form. A Cursor question that takes several answers works as a multi-select.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-session-multiple-choice-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-session-multiple-choice-aug-2026.png" class="help-center-img img-bordered" alt="A multiple-choice question form in the conversation, with numbered options, Chat about this, Cancel, and Submit">
  </a>
  <figcaption style="text-align:center; color:#888">A structured question, rendered in the conversation.</figcaption>
</figure>

| Kind | How it behaves |
|---|---|
| Multiple choice | Radio-style. One option is the answer |
| Multi-select | Checkbox-style, hinted **Select all that apply**. Every ticked option is sent |

Both kinds work the same way otherwise:

- Options show a label and, when the agent supplied one, a description.
- Press **1** to **9** to pick an option by the number shown on it.
- **Other...** opens a free-text field (*Type your answer...*). For a single-choice question, your text is the whole answer. On a multi-select, it joins the ticked options. For Codex, this field replaces Codex's own **None of the above** option.
- Several questions arrive as steps, with a **{current}/{total}** counter and a tab strip. You can submit only once every question has an answer. Until then, you see **{count} questions still unanswered**.
- **Chat about this** declines the form so you can answer in your own words in the chat. It does not cancel the session.
- If the agent set a deadline, the form counts down (**{count} seconds remaining**). A form that was never answered is recorded as **Left unanswered** instead of staying on screen as if you had submitted it.

A restored session shows the question and the answers you gave as a read-only record.

### Reviewing a plan

When an agent in plan mode proposes a plan, Kepler opens it for review in a **Plan** panel beside the chat, with **Preview** and **Edit** tabs. The transcript shows the plan with **Open plan**. Claude Code, Codex, GitHub Copilot, Cursor, and OpenCode Chat sessions offer plan review. Cursor holds its plan request open while you review it, so the session waits with the reason **Plan review**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/plan-review-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/plan-review-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A Chat session with its Plan panel open beside the transcript for the plan Fix the discount order in the cart total. Step 2, Round once, at the end, to two decimal places, is highlighted and carries a comment under Comments (1), with Request changes (1) and a greyed Approve & implement at the foot.">
  </a>
  <figcaption style="text-align:center; color:#888">A plan under review, with a comment on one step.</figcaption>
</figure>

To review the plan, use these controls:

| Control | What it does |
|---|---|
| A comment on a passage | Select text in the plan and say what should change (*What should change?*). Comments collect under **Comments ({count})** |
| **Request changes ({count})** | Sends your comments back so the agent revises the plan. Kepler keeps each revision, so you can go back to an earlier one |
| **Approve** or **Approve & implement** | Accepts the plan, and the agent leaves plan mode to carry it out. The chevron lists any other ways the agent offers to approve |

While comments are pending, you cannot approve the plan: *Submit or delete your comments before approving.*

Auggie shows its plan as a task checklist instead. **Hide these tasks** clears the checklist.

### Approval requests

Some actions that an agent asks Kepler itself to do, through Kepler's workspace tools, wait for your approval. For example:

- Sending a prompt or a message to another session, or stopping, renaming, or archiving one.
- Editing or deleting a task note, changing another task or its links, detaching files, or archiving a task.
- Deleting a worktree.
- Starting a session in a more permissive mode than the asking session's own.
- Syncing a branch with its target, or rewriting its commits.
- Overwriting a theme file.
- Changing a Kepler setting that affects your accounts, your privacy, other tools, what runs, or where files go. Only **Ask Kepler** can change settings. See [Ask Kepler](/kepler/ask-kepler#finding-and-changing-settings).

Kepler tells the agent that the request is waiting, and the agent can keep working; your answer reaches the agent's inbox later. Meanwhile, the session reads **Approval needed** or **Approval needed, destructive**.

The request is pinned above that session's composer as a card. The card names the action, such as **Delete worktree {worktree} and its branch**, and shows what is at stake (*At risk: {loss}*), with **Approve** and **Deny**. A card for an action that can lose work is amber; other cards are blue. If several requests are waiting, page through them with **{index} of {count}**. A setting change reads **Change the setting {setting}**, with **From {from} to {to}** beneath, or **To {to}, on your computer** for a setting kept on your own computer.

<figure style="text-align:center">
  <a href="/wp-content/uploads/approval-card-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/approval-card-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="An amber approval card pinned above the session composer, Delete worktree acme-web@kepler/cart-total-spike and its branch, At risk: 2 uncommitted files, with the Approve menu open on Approve all worktree deletes from this session and a greyed Always approve worktree deletes.">
  </a>
  <figcaption style="text-align:center; color:#888">An approval card for deleting a worktree, with the Approve menu open.</figcaption>
</figure>

The **Approve** chevron offers 2 broader answers:

- **Approve all {label} from this session**: approves this kind of request for the rest of the session.
- **Always approve {label}**: adds a standing rule. It is not offered for an action that can lose work (*Not offered for actions that can lose work.*) or for starting a session.

A setting change offers neither answer; each setting change asks on its own.

Before Kepler carries out an approved request, it checks that the request still applies. The request then shows **Running** while Kepler carries it out. A request that fails shows **Not done: {summary}**, with **Dismiss**. A waiting request expires when its session is archived.

To review your standing rules, open **Settings → Agents → Approvals**: *Some actions your agents take wait for your approval. These rules approve them for you; anything not covered still asks.* Each rule under **Always approved** says when and where it was added and how often it has been used, with **Remove**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-approvals-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-approvals-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Approvals section of Settings › Agents, with one Always approved rule, Changes to other tasks, added from the Discount codes break the cart total session on Fix the cart total and not used yet, and Remove.">
  </a>
  <figcaption style="text-align:center; color:#888">Standing approval rules, in Settings → Agents → Approvals.</figcaption>
</figure>

### Reports from other agents

Agents that work together report to each other through Kepler. Each session has an inbox, which collects the following:

- Reports and messages other agents send to the session.
- A change in the state of a session this one started.
- The answer to one of its approval requests.

When an item arrives for an idle session, Kepler wakes the session to read its inbox, and the conversation shows a row such as **2 new items to read**. Kepler wakes a busy session once its turn ends.

A session with unread reports shows a reports badge with a count on its tab and on its row in the context panel (*{agent} hasn't read {count} reports from other agents*). The band above its composer offers **Have it read them**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-reports-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-reports-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The task page for Fix the cart total, where the Discount codes break the cart total session carries a reports badge with 3 beside the reviewer it started. Its conversation shows a 2 new items to read row, and above the composer OpenCode hasn't read 3 reports from other agents, with Have it read them.">
  </a>
  <figcaption style="text-align:center; color:#888">A session with unread reports from other agents.</figcaption>
</figure>

To stop agents from waking each other without end, Kepler pauses wakes after 20 turns in a row that agents started without a prompt from you. The band then reads **Reports from other agents are paused**: *They no longer wake this session on their own. Resume to let them wake it again.* To let reports wake the session again, click **Resume reports** or send your next prompt.

In Terminal mode, Kepler can wake only Claude Code, Pi, and OpenCode 2 sessions to read their inbox. Any other Terminal agent shows **No Kepler tools** on its status bar: *{name} can't use Kepler's workspace tools or inbox in a terminal.*

***

## Usage indicators

Kepler shows 2 usage readouts, and they measure different things.

<figure style="text-align:center">
  <a href="/wp-content/uploads/usage-indicators-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/usage-indicators-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Context window card open above the composer's context ring, which sits between the Agent settings pill (Docs Model, Build) and Send: 68%, with 136K tokens Used, 64K Available and 200K Total, and the Estimated cost at API rates, $0.42.">
  </a>
  <figcaption style="text-align:center; color:#888">The Context window card, from the context ring.</figcaption>
</figure>

| Readout | What it shows | Availability |
|---|---|---|
| **Context window** | How much of *this session's* context window is used, as a ring. Hover to see tokens used, available, and total, the **Estimated cost at API rates**, and the **Prompt cache**: when it expires, and how much of the session's input came from it (*{percent}% cached*) | Whenever the agent reports it |
| **Plan usage** | Your provider plan's windows (**5h** and **7d**) as **Used** and **Resets** columns, plus whatever else the provider reports about the plan | Claude Code and Codex sessions report their own 5-hour and 7-day limits. The full readout, Auggie, and GitHub Copilot need **Check plan usage with each agent's provider**, which is on by default |

While a session is idle, the context ring warns about the prompt cache on its own. It shows an hourglass with the time the cache has left, or **Expiring** or **Expired**. The context card then shows the cache first and warns *The next message re-reads most of the context.* If there is no context reading, the ring is a dashed circle, and its card still shows the cost when the agent reports one.

**Check plan usage with each agent's provider** fetches the full readout, including per-model limits and extra usage, from each agent's provider. It is on by default, in **Settings → Agents → Usage limits**:

<figure style="text-align:center">
  <a href="/wp-content/uploads/show-token-usage-aug-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/show-token-usage-aug-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Usage limits section of Settings › Agents: Check plan usage with each agent's provider, ticked, with its help text on what Kepler asks the provider for and what it shows when off, and Resume after the usage limit resets, unticked.">
  </a>
  <figcaption style="text-align:center; color:#888">Check plan usage with each agent's provider, in Settings → Agents → Usage limits.</figcaption>
</figure>

> Kepler asks each agent's provider for your plan usage, per-model limits and extra usage, using the agent's own sign-in. The sign-in goes nowhere else and is never changed. When off, Kepler shows only what agents report, and a message queued at a usage limit is sent automatically only if the agent says when the limit resets.

With the setting off, Kepler makes no request to any provider. A Claude Code or Codex session still reports its own **5h** and **7d** readings as it runs, and Kepler shows those. A card based only on those readings says so: *Reported by the agent. Turn on {setting} in {section} to also see per-model limits and extra usage.*

The meter shows the shortest window. If the provider reports a balance that cannot be shown as a percentage, the meter shows the remaining plan balance instead. Hover the meter to open the detail. A spent window reads **Limit reached until {time}**. Every reading says how old it is (**Updated {when}**), with **Refresh** to fetch it again.

Kepler judges a usage bar by pace: the share of the window you have used, compared with the share of the window that has passed. The detail reads **On pace** or **Ahead of pace**. When you are ahead, it estimates when you will use up the window, for example *Runs out in ~{duration} at this rate*. The bar's color follows these rules:

- Amber once your use is more than 15 points ahead of pace, and red past 30 points.
- Always at least amber at 90% used, and red at 100%.
- Below 10% used, or when there is no pace to judge, fixed bands apply instead: amber above 75% and red above 90%.

| Provider | What its popover shows |
|---|---|
| **Claude Code** | The **5h** and **7d** windows, and an **Extra usage** pool with credits used against any monthly limit |
| **Codex** | The same 2 windows, plus **Usage limit resets**: earned resets that clear an active limit early, each with its expiry |
| **Auggie** | No windows, only the plan's credit balance: a plan line naming the plan with what is left of it, *{remaining} / {included} credits left*, or *{remaining} credits left* on an unmetered plan |
| **GitHub Copilot** | The plan's monthly **Premium**, **Chat**, and **Completions** quotas, each with when it resets (an unlimited one is left out), and **{count} credits used** on token-based billing. A spent premium quota reads **Premium quota exhausted** with a warning mark and when it resets, or **Premium quota status unknown** once that reset has passed |

An account on a third-party Claude provider shows no usage. If Kepler cannot fetch the figures, the meter says which problem it hit instead of showing an old number. For example: *Sign in to {agent} to see usage data.*, *Sign in to Copilot through Kepler to see usage data.*, or *This agent doesn't expose usage data.* Where it applies, the meter adds *Your sessions aren't affected.*

### When you hit a usage limit

Kepler does not keep sending prompts into a spent limit. As soon as the account's usage reading or the agent's own report shows the limit is spent, Kepler holds the prompts you queue until the limit resets. It does not wait for a turn to fail first. The queue banner reads *Sending at {time}, when the quota resets.*

The prompts go out on their own shortly after the reset, even with no Kepler window open and across a restart. To release one session's queue early, click **Send now**. A spent limit on one model does not hold prompts for the account's other models. With **Check plan usage with each agent's provider** off, a queued prompt waits only if the agent itself says when its limit resets.

<!-- TODO(screenshot): New: The queue banner holding a prompt until the quota resets (*Sending at {time}, when the quota resets.*) with **Send now**. -->

If a turn hits the limit before the agent produced anything, the turn is not lost: Kepler sends the same prompt again after the reset. If the limit cuts off a turn after the agent started replying, and nothing is queued, the session waits for you. To have Kepler continue on its own, turn on **Settings → Agents → Usage limits → Resume after the usage limit resets**: *When a turn is cut off by your account usage limit and nothing is queued, Kepler queues a "continue" message that is sent shortly after the limit resets.* This setting is off by default. You can send the queued message early or remove it, like any other queued message.

When a session's account reaches its limit, a banner shows **{login} reached its usage limit**, with *Available again at {time}.* To keep working now, click **Continue as {login}**, which moves the conversation to the account with the most usage left. The button's menu lists your other accounts. See [Moving a session to another account](#moving-a-session-to-another-account). If no other account can take the conversation, the banner suggests *Add another account to keep going.*

Kepler handles usage limits this way for the agents it can read usage for: Claude Code, Codex, and Auggie.

***

## Voice input

Every session's composer has a microphone. Click it to record, then speak, and the transcript appears in the prompt. Transcription runs on your device. Voice input is off until you turn it on and download a model.

<figure style="text-align:center">
  <a href="/wp-content/uploads/start-voice-input-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/start-voice-input-aug-2026.png" class="help-center-img img-bordered" alt="The composer's microphone icon, with its Start voice input tooltip">
  </a>
  <figcaption style="text-align:center; color:#888">The composer's microphone icon.</figcaption>
</figure>
<!-- TODO(screenshot): Replace — ade-start-voice-input-01: the composer microphone hovered with a Qwen3-ASR engine ready, tooltip Start voice input · Qwen3-ASR 1.7B (needs the voice model downloaded). -->

When a Qwen engine is dictating, the microphone's tooltip names it, for example **Start voice input · Qwen3-ASR 1.7B**. When voice input cannot start, the tooltip says why and links to the engine's settings. For example, a graphics card might not be responding, or a model might need WebGPU. See [Voice Input](/kepler/voice-input).

***

## Session status

Each session has a status, shown as a colored dot on its tab and rows.

| Status | Meaning |
|---|---|
| **Spawning** | Starting up |
| **Ready** | Connected, nothing sent yet |
| **Running** | Working on a turn |
| **Waiting** | Blocked on you, and it says on what: **Permission**, **Question**, **Plan review**, or **Prompt not sent**. A pending Kepler approval also counts, as **Approval needed** or **Approval needed, destructive**, even while the agent keeps working |
| **Unread** | Finished a turn you have not looked at |
| **Idle** | Connected, nothing running |
| **Background task running** | The turn ended, but work the agent left running on its own, such as a backgrounded shell or a monitor, is still going. Shown as idle, a gray dot with a green ring that does not pulse, and it does not keep the machine awake |
| **Reconnecting** | Kepler is reattaching to a session that kept running while Kepler restarted |
| **Error** | The turn or the process failed. A live session whose last turn failed on a rate limit, an exhausted quota, or an overloaded provider reads **Error** too |
| **Ended** | The agent process is not running. Kepler keeps the conversation, and a dormant session shows its last state as *{state} (ended)* until your next message starts it again |

When Kepler has to show one status for several sessions, the most urgent wins. **Waiting** and **Error** outrank live work, and **Unread** ranks above **Idle**, so you do not miss a finished turn.

Outside the session itself, these statuses combine into 5 broader levels: attention, active, idle, errored, and inactive. [The main list](/kepler/kepler-interface)'s row and preview indicators show these levels, and the levels decide where an [Action](/kepler/actions) fires. *Attention* covers both a waiting session and a session with an unanswered permission request, question, or approval request.

Task and session rows add a line that says what a session needs from you, most pressing first: **Approval needed for {tool}**, **Asking: {question}**, **Waiting for you**, **Terminal waiting for you**, or **New reply**.

***

## Tabs, archiving, and restoring

Open sessions appear in a tab strip. Each tab shows the agent, the account when more than one exists, and a status dot. Drafts sit in the same strip, marked **(draft)** when the strip has room.

To see a session's card, hover its tab, its row in the context panel, or a Terminal session's status bar. Below the account, the card can show these lines:

- **Running in the background**, with **and {count} more**, for background tasks still running.
- **Continued from {name}**, for a session started from another.
- **Rate limited · Resets {time}**, when the account's limit is spent.
- **Context {percent}%**, the share of the context window in use.

You can do the following with tabs:

| Action | Result |
|---|---|
| **Cmd/Ctrl+T** or **+** | Opens a draft tab for a new session. See [Draft session tabs](#draft-session-tabs) |
| **Alt+1** to **Alt+9** | Jumps to a tab by position |
| **Cmd/Ctrl+Shift+[** / **]** | Previous or next tab |
| **×** on a tab in the Sessions column (**Archive session**) | Archives the session |
| **Archive** on a session's row in the context panel | Archives the session |
| **Restore** | Brings an archived session back into the strip |
| **Shut down agent** | Ends the process without archiving the session |
| **Restart agent** | Shuts it down, then reconnects |
| Drag a tab | On the Dashboard, reorders session and terminal tabs |

**In the Sessions column, closing a tab archives the session.** Kepler stops the agent process, saves the conversation and its resume handle, and removes the tab from the strip. Nothing is deleted. If **Show tabs on the task page** is on, a tab's **×** is **Close tab** instead. It only hides the tab, and the session keeps running. See [Task View](/kepler/task-view#tabs-and-groups).

### Shutting down and restarting an agent

Ending a session's agent and archiving the session are separate actions. A live session's row menu offers these:

- **Shut down agent** cancels the turn, waits a limited time for it to settle, saves the conversation at a turn boundary, and then ends the process. The session stays listed, and you can resume it.
- **Restart agent** does the same and then reconnects, so the session comes back on the agent version installed *now*. Use it to pick up an agent you just updated without losing the conversation. A restart also re-reads your login shell. An environment variable you added, changed, or removed in your shell's startup files reaches the restarted agent without restarting Kepler.

A restart shows its progress instead of a blank session. A session you shut down before its first prompt stays listed as dormant instead of disappearing.

### Dormant and archived sessions

A **dormant** session (one restored from disk, or stopped before it ever ran) shows its transcript, with the session's title at the top of its context card. It does not start an agent until you send the first message, so restoring many old sessions costs nothing.

You can read an **archived** session without restoring it. It opens read-only, labeled *Read-only. Restore it to keep working.*, with **Restore this session and open it live** and **Permanently delete this saved session** beside it.

Archived sessions are listed under a **{count} archived** fold below the live ones in the context panel. On the Dashboard, the session strip's **Archived sessions** button searches them (*Find an archived session…*). Restoring puts the session back in the list, and the session reconnects when you open it.

Some agents can store one conversation more than once. If a session has more than one saved copy, it resumes the newest copy it can run, without asking. To pick another copy, choose **Use another copy…** on the session's menu: *Kepler found more than one saved copy of this conversation. Pick the one to continue when you resume it.* Each copy lists when it was updated and how many messages it holds.

Deleting a task or removing its repository ends that task's live sessions.

### Pointing an agent at another session

To copy a Kepler link to a session, such as `kepler://session/<id>`, choose **Copy session link** on the session's row or tab menu, or press **Cmd/Ctrl+C** on a focused row. **Copy task link** on a task's menu does the same for a task. When you paste the link into a prompt, the agent can read that conversation through the workspace tools. For example, you can ask an agent to read what another agent concluded and continue from there. See [Tasks and Resources](/kepler/tasks-and-resources).

An agent that cannot use Kepler's workspace tools gets a copy instead. Kepler attaches a Markdown snapshot of each task or session linked in the prompt, up to 5 per prompt. The same happens when you paste a link into such an agent's terminal. A snapshot is a copy taken when you send, not a live view.

### Keeping agents running through a restart

**Settings → General → Keep agents running → Keep agents and terminals running across restarts and updates** is on by default, though the setting is still marked experimental: *Agent sessions and terminals stay alive while Kepler restarts or updates, and reconnect afterwards. Experimental.* A change to the setting applies to new sessions. If your build cannot keep agents running, the switch is off and grayed out.

<!-- TODO(screenshot): New: A session showing the *Reconnecting to the agent…* overlay after Kepler restarts. -->

| Event | Switch on (the default) | Switch off |
|---|---|---|
| **Quit** | Agent sessions keep running, and Kepler reattaches to them when it comes back. Shell tabs end, as they do when you quit any terminal app | Asks first when sessions are running or still have live work, such as a busy subagent or a dev server left running, and warns that each one will stop. Busy *terminals* are counted too |
| **Updating Kepler** | Warns only about agents the update would interrupt. Shell tabs keep running and come back after the restart | Warns how many agent sessions the restart will stop |
| **Quit & End Sessions** | In the app and tray menus, including when only shell tabs are open. Ends the sessions as Kepler quits, asking first only if one is mid-turn or still has live work (**End Sessions and Quit**); you can continue each session again from its task | Not applicable |

While Kepler reattaches, an overlay covers the session, and the session offers no actions until it is back. The overlay reads *Reconnecting to the agent…*, then *Restoring conversation history…*. If the reattach fails, the session falls back to its saved conversation: *Unable to reconnect to the agent. Resume to pick up from the saved conversation.* If a session's background process stops, the session also keeps its conversation instead of starting a new one.

If Kepler never comes back to a session left running after a quit, the session ends on its own after an hour without any output from the agent. An agent still mid-task keeps producing output, so it finishes its work first.

A Terminal session kept running this way also keeps its keyboard and paste modes across the restart. If a reboot ends the session, you can still resume it.

A session kept running this way can stop accepting output if it reaches a storage or log limit. It then shows **Agent output paused**: *Kepler stopped accepting agent output after reaching a storage or log limit. Your draft is preserved while output is paused.*

Kepler keeps your computer awake while agents work. While any session is spawning, running, or waiting on you, Kepler prevents sleep, and it stops as soon as the last session settles. This is on by default. To turn it off, clear **Settings → General → Keep agents running → Keep this machine awake while agents work**. See [Settings](/kepler/settings-app#keep-agents-running).

***

## When a session drops

If a session cannot continue, its context card says so with a badge, one sentence, and only the recovery step that applies:

| Badge | What happened | What to do |
|---|---|---|
| **Ended** | The process is gone; the conversation is not | **Resume** |
| **Exited** | *{name} exited on its own. Restart it to continue from the saved conversation.* | Restart the agent |
| **Can't resume** | *{name} no longer has this conversation, so it can't continue. You can still read it below.* | **Archive session**, or **Start new conversation** |
| **Sign-in failed** | *{name} was unable to sign in. Sign in again to continue this conversation.* | Sign in again |
| **Can't start** | *{name} isn't installed or can't run*, or *The installed {name} can't run this session.* | Fix the install or path in agent settings, then restart |
| **Folder missing** | *The folder this conversation ran in was removed or moved.* | **Recreate worktree and resume** or **Recreate folder and resume** |
| **Disconnected** | *Kepler lost its connection to this session and ended it. Restart to pick up where it left off.* | Restart the agent |
| **Unable to resume** | *Another {name} is still running this conversation. Close it, then try again.* | Close the other copy, then resume |

If a card has more detail, it shows **Details**, which opens the **Diagnostics** behind it, with **Copy** for a bug report.

An **Agent error** banner names the cause, such as *{name} binary is missing or not executable.*, *Agent authentication failed.*, or *Agent process exited on its own.* Depending on the cause, the banner offers **Reconnect**, **Authenticate**, **Compact**, or **Dismiss**. A usage limit reads **{login} reached its usage limit**, or **{adapter} reached its session limit**, with *Available again at {time}.* See [When you hit a usage limit](#when-you-hit-a-usage-limit). A Codex turn that the provider could not serve reads **Codex was unable to complete this turn**: *OpenAI reported a capacity problem, not a usage limit. Reconnect to this conversation, then retry in a moment or switch models.*

A Chat turn that fails on the provider's side says which kind of failure it hit and what to do:

- *{name} hit a rate limit. Wait a moment, then send your message again.*
- *{name} is out of quota or has a billing problem. Check your plan or billing, then try again.*
- *{name} is overloaded right now. Try again shortly.*

While the agent retries a failed turn on its own, the session shows **Retrying** with the reason, such as *{name} hit a rate limit and is retrying.*, the attempt (*Attempt {attempt}.*), and *Next try at {time}.*

In Terminal mode, a process that has exited reads **Terminal exited. Resume to reattach to this conversation.**

If a session fails to start after you launch it, the task page and the Dashboard panel show **{agent} was unable to start** with the agent's message. Click **Retry** to try again, or **Open agent settings** to fix the agent's setup. **Dismiss** hides the notice in that window.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-task-start-failed-notice-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-task-start-failed-notice-01-v3@2x.png" class="help-center-img img-bordered" alt="The top of the task page for Fix the cart total with the OpenCode was unable to start notice: the message Session not initialized, Retry, Open agent settings, and a close button that dismisses it.">
  </a>
  <figcaption style="text-align:center; color:#888">A session that couldn't start, on the task page.</figcaption>
</figure>

Sessions recover on their own where they can. If an authentication token expires mid-session, Kepler renews it so the session continues. Remote connections reconnect after a restart or sleep.

***

## Notifications

Kepler notifies you when a session replies, needs you, or fails. Each notification has one of these statuses:

| Status | When |
|---|---|
| **Replied** | An agent finished replying, and it is your turn |
| **Asked a question** | The agent asks you something and waits for your answer |
| **Needs permission** | The agent wants permission to do something |
| **Approval needed** | An agent asks Kepler to do something only you can approve, like deleting a worktree. A destructive request reads **Approval needed for a destructive action** |
| **Error** | The session stopped because something went wrong |

A Terminal or external session blocked on a prompt in its own CLI also notifies you, for every agent. Sessions started outside Kepler notify you only once they are on a task.

A notification's title reads **{status}: {task}**, with the agent and the repository or branch beneath (*{adapter} on {repo}/{branch}*). Click the notification to go to the session. Kepler opens it in the window that already shows that session or its task, or else in the window you used last. An approval notification's title is its status alone. Beneath it are the action, what a destructive action would put at risk, and *Asked by {session}*.

You can answer an approval request from its alert. The in-app alert has **Approve** and **Deny** for every request, destructive ones included, followed by **View**, which opens the request in its session. On macOS, the desktop notification also has **Approve** and **Deny** buttons, which answer the request without opening a window. Windows and Linux notifications have no buttons. If the request was already answered elsewhere, pressing a button does nothing.

<figure style="text-align:center">
  <a href="/wp-content/uploads/approval-alert-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/approval-alert-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="An in-app alert with an amber edge and shield, Approval needed for a destructive action, for the task Fix the cart total: Delete worktree acme-web@kepler/cart-total-spike and its branch, At risk: 2 uncommitted files, and Asked by Discount codes break the cart total on Fix the cart total, with Approve, Deny and View buttons and a close button.">
  </a>
  <figcaption style="text-align:center; color:#888">An approval alert, answered in place with Approve or Deny.</figcaption>
</figure>

By default, Kepler sends no notification for the task open in the window you are using. To be notified about that task too, turn on **Notify even for the task you're looking at**.

While you are working in any Kepler window on a computer, that computer posts no desktop notifications. The window you are in shows them in Kepler instead, and several windows on one computer post a single alert. A canceled turn and a session that is reconnecting do not count as completions, so neither sends a notification.

To choose which events notify you, and whether each one appears as a **Desktop** notification, **In Kepler**, or both, open **Settings → Notifications**. The same page has **Play a sound with desktop notifications**. In the desktop app, every event except **Replies** notifies on the desktop until you change it. In a browser, desktop notifications start off. After your first session starts, the desktop app sends a one-time **Notifications are on** notification. Click it to open **Settings → Notifications**. See [Settings](/kepler/settings-app#notifications).

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-settings-notifications-01-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-settings-notifications-01-01-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Notifications, What to notify you about, at the desktop app's defaults: a grid of Replies, Questions, Permission requests, Approval requests and Errors against Desktop and In Kepler, with every box ticked except both Replies boxes; below it Play a sound with desktop notifications is ticked and Notify even for the task you're looking at is not.">
  </a>
  <figcaption style="text-align:center; color:#888">What to notify you about, in Settings → Notifications, at the desktop app's defaults.</figcaption>
</figure>

### Notifications from terminal programs

A plain terminal can also notify you. When the program in a terminal waits on you, or finishes or fails after working, Kepler sends a notification that names the terminal and its task. For example:

- *Approve it in {terminal}*
- *Answer it in {terminal}*
- *Sign in from {terminal}*
- *Finished in {terminal}*
- *Failed in {terminal}*

Click **View** to open that terminal. Terminal notifications follow the same **Settings → Notifications** choices as agent sessions. Kepler skips a terminal notification only while that terminal is on screen in the focused window.

In-app notifications show a close button when you hover them, and **Clear all ({count})** dismisses all of them.

***

## Reviewing what the agent changed

To read the diff an agent produced and sync its branch, see [Review Changes](/kepler/review-changes).

---
