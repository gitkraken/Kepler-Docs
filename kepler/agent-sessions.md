---
title: Agent Sessions
description: An agent session is one running conversation with a coding agent inside a Task. Learn how to start one, pick the agent and account (including several accounts of the same agent), queue prompts, answer the agent's questions and permission requests, track usage limits, and keep sessions running through restarts.
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

An **agent session** is one running conversation with a coding agent, anchored to one working directory.

A Task can hold several. Two agents on the same worktree, one agent per worktree, a session for the task folder itself: all of it is normal, and all of it lives under the Task's **Sessions** group. See [The Task View](/kepler/task-view) to learn more.

This page covers the session itself: starting it, directing it, and its lifecycle.

Every session is an agent session, but two things about one vary, and both are properties of the session rather than different kinds of thing:

| | Values | Covered in |
|---|---|---|
| **How it runs** | **Chat** or **Terminal** | [How a session runs](#how-a-session-runs) |
| **Where it came from** | Started in Kepler, or found running outside it | [Sessions started outside Kepler](#sessions-started-outside-kepler) |

Everything else on this page (prompts, steering, permissions, status, lifecycle) is the same whichever of those a session happens to be.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-session-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-session-aug-2026.png" class="help-center-img img-bordered" alt="A running session in the Sessions column, with a tab strip, a transcript showing a collapsed tool-call group, and the composer's agent-settings pill">
  </a>
  <figcaption style="text-align:center; color:#888">A session in the Sessions column: tabs, transcript, and composer.</figcaption>
</figure>

For reading what an agent produced, see [Review Changes](/kepler/review-changes).

***

## Starting a session

You can start a session from any of the following places:

| From | How |
|---|---|
| A row in **Todo** | Fire an Action. See [Actions](/kepler/actions) |
| The task view rail | **New session** on the **Sessions** group, or **New session here** on a worktree or folder row |
| An open session strip | **+** (**New session**), or **Cmd/Ctrl+T** |
| An existing session | **New session from this one** on its row menu |
| A message in a conversation | **New session from here** on the message's right-click menu |

A quick question that belongs to no task goes to **Ask Kepler** instead, the chat in the top bar's side panel. Any agent that runs in **Chat** can answer there, and **Continue in a new task** hands the chat on to a new task. **Open source session** on that task's session reopens the chat in the panel. See [Ask Kepler](/kepler/ask-kepler).

### Draft session tabs

**New session** opens a draft tab rather than a menu. Nothing starts until you send the first message, so you can write the prompt, attach files, and pick the agent first. The tab takes its name from the first line of your prompt and is marked **(draft)** when the tab strip has room. In the task rail, the same row reads **Draft**.

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
| **Attached to this task** | The worktrees and folders already attached to the Task, including **All worktrees and folders**: *Runs in the task folder and has access to all worktrees and folders* |
| **Branches** | Other branches of the Task's repositories. Pick one to start the session on that branch |
| **New branch from this** | Starts the session on a new branch based on the branch you picked |

Every session sees the Task's attached resources regardless of where it runs, so what sets **All worktrees and folders** apart is only its working directory.

A session receives the Task's shared context by default. To start a session that forms its own view instead, untick the **Task context** chip in the draft composer's footer, beside **Attach a file** and the microphone. Its tooltip reads **Leave out the task context** while it's ticked and **Include the task context** while it's not: *Gives the agent the task’s prompt and notes. Later changes reach it with your next message.*

Right-click a draft tab or its rail row for these actions:

- **Discard draft**, which asks first if the draft holds text or attachments: **Discard new session?**
- **Move left** or **Move right**, to reorder the draft among the other tabs.

With **Show tabs on the task page** turned on, the draft's menu is a tab's instead: **Pin tab** or **Unpin tab**, **Keep open** while it's a preview, and **Close tab**, which is its only close. See [Task View](/kepler/task-view#tabs-and-groups).

**New session from this one** starts a sibling session in the same task, worktree, agent, and account, and the new agent can read the source conversation. **New session from here** does the same, but the new agent reads the source only up to and including the message you picked. It's available once that message has finished streaming, and not on a terminal or external session (*This conversation can't be branched at a message.*). **Open source session** on the new session's menu takes you back to where it came from.

**Rename session**, on a session's row menu, gives a session a name of your own. Agents can also name and rename the Chat sessions they start, through Kepler's workspace tools.

***

## Agent, model, mode, and effort

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-settings-from-composer-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-settings-from-composer-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Agent settings open above a new session's composer: Agent OpenCode, Start in with Chat selected beside Terminal, Model Docs Model, Permission mode Build or Plan, MCP servers (No servers) with Manage, and Use default agent. Below it, the composer footer holds a ticked Task context chip beside Attach a file and the microphone, then the Docs Model Build pill and Start.">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent settings pill, opened from the composer, with the Task context chip in the footer.</figcaption>
</figure>

The composer carries an **Agent settings** pill. It holds the same set of questions at launch and mid-session, and its trigger summarizes the current model and mode.

| Choice | Changeable mid-session | Notes |
|---|---|---|
| **Agent** | No | Fixed once the session exists. Changing agent means a new session |
| **Start in** | No | **Chat** or **Terminal**, for an agent that offers both. Fixed once the session starts. To use the other mode, start a new session. See [How a session runs](#how-a-session-runs) |
| **Model** | Yes | The agent's own catalog. Models are per provider, so a model never moves to another agent. Left at the default, the row reads **Default · {model}**, naming the model the default resolves to |
| **Mode** | Yes | The agent's own permission modes |
| **Effort** | Yes | Reasoning or thinking depth, for agents that offer it |
| Other **Options** | Some | Options an agent can only read at spawn are editable at launch and nowhere else. A Terminal launch offers the CLI's own launch options; see [How a session runs](#how-a-session-runs) |

A change applies from your next message; it never interrupts the turn in flight. Option rows read **Agent decides** until you pick something, **Reset** appears once anything is overridden, and the pill reads **Loading {agent} options…** while Kepler probes an agent it has not seen recently.

When the model a session runs on changes, for example because the default now resolves to a different model, the conversation says so: *Model changed from {from} to {to}.*

Model and mode lists refresh in the background, and again after you upgrade or sign in to an agent, so a newly released model appears without restarting Kepler.

The same menu lists the MCP servers the agent loads for this repository, with **Manage** to change them. See [MCP Servers](/kepler/mcp-servers).

The menu says when it can't offer a normal choice:

| The menu reads | When |
|---|---|
| **Loading your last agent choice…** | Kepler is restoring the agent you used last |
| **Connect an AI agent** | No agent is installed: *Install an agent CLI to start your first session.* Each agent has an **Install** row, with **See all {count} agents in Settings**, and **Installed one yourself?** with **Check again** |
| **Sign in to {agent} to start a session** | The chosen agent is installed but signed out |
| **{agent} didn't share its options** | Kepler couldn't read the agent's models and modes: *You can still start a session. It uses {agent}'s own model and mode.* with **Retry** |

With more than one account, the **Agent** list groups accounts under their agent and ends with **Add another account** and **Install another agent**.

By default, a new task, the Dashboard composer, and a new draft tab start with the agent, model, and mode you last picked. To always start with one agent instead, open **Settings → Tasks → New tasks**, set **Default agent**, and set **New sessions start with** to **Default agent** (*Always the default agent above*) rather than **Last used agent** (*The agent, model and mode you last picked*). **Use default agent** in the launcher picks the default agent for one session. See [Settings](/kepler/settings-tasks#new-tasks).

### Which agents are available

Claude Code, Codex, Copilot CLI, Cursor, Auggie, OpenCode, Grok Build, Pi, and Google Antigravity, plus any custom agent you add. Kepler offers only the agents you actually have installed. See [Agent Integrations](/kepler/agent-integrations).

***

## Several accounts for one agent

Claude Code, Codex, GitHub Copilot, Auggie, and Grok Build can each hold more than one signed-in account. Open **Settings → Agents**, expand the agent, and find **Accounts**:

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
| **Check usage** | Reads that account's plan usage. Greyed out only when **Check plan usage with each agent's provider** is turned off in **Settings → Agents → Usage limits**: *To check this account's usage, turn on Check plan usage with each agent's provider in Usage limits.* |
| **Switch account…** | On a signed-in Claude Code account's row menu. Signs that account in with a different Claude login, after a confirmation (**Switch the account for {name}?**) that counts the running sessions using it |
| **Remove account** | Signs the account out and deletes its local data. Your shared skills, agents, and settings are untouched. Sessions whose conversations are stored only in that account are deleted with it; see below |
| Colour swatch | At the left of each added account's row: *Pick a color to tell agents on different accounts apart*. **Rose**, **Amber**, **Lime**, **Cyan**, **Blue**, **Violet**, or **No color**. *The default account stays uncolored*: its picker shows the ⊘ **No color** mark, which doesn't mean the account is off |

An account's colour tints the agent icon on session tabs, the task rail, and the terminal status bar, so sessions on different accounts are told apart at a glance.

**Switch account…** opens the same sign-in as **Add account**. If your browser is already signed in, choose a different account on the sign-in page. On the default row, the confirmation adds *This also changes the account the claude command uses in your own terminals.* When the sign-in completes, Kepler confirms *{name} is now signed in as {login}.*

**An added account can stop sharing your configuration.** An added account links to your own configuration, such as your settings, instructions, skills, agents, commands, plugins, rules, and hooks, rather than copying it. If the agent saves a change to one of these while signed in to that account, the account gets its own copy and stops following yours. Kepler flags this under the account's row: **This account stopped sharing your {items}**. Expand the warning to see which file the account copied, with the paths of **This account's copy** and **Your {item}**, and choose one of the following:

- **Share your {item} again** links the account back to your file, after **Share your {item} with this account again?**: *Its own copy is saved as a backup next to it, so nothing is lost.*
- **Keep its own {item}** keeps the account's copy. **Share your {item} again** then moves to the account's row menu.

<figure style="text-align:center">
  <a href="/wp-content/uploads/account-config-drift-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/account-config-drift-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Claude Code card in Settings › Agents with two accounts. Under the second account, Personal, an open warning reads This account stopped sharing your settings, names its own copy of settings.json and your /home/alex/.claude/settings.json, and offers Share your settings again and Keep its own settings.">
  </a>
  <figcaption style="text-align:center; color:#888">An added account that stopped sharing your settings.</figcaption>
</figure>

**Removing an account counts what it takes with it.** **Remove {name}?** walks through it in steps:

- Running sessions on the account are stopped: *{count} running sessions will be stopped now*.
- Sessions whose conversations are stored only in this account would be deleted: *{count} sessions will be permanently deleted*. To keep them, **Move to CLI account** first under **Keep these conversations**; the sessions stay in their tasks, and removing the account then deletes nothing.
- Otherwise **Continue to remove** asks once more, **Permanently delete {count} sessions?**, and you tick *I understand that {count} sessions in {tasks} will be permanently deleted, and that this can't be undone.* before the account goes.

**How many accounts you can add depends on your GitKraken plan**, and Pro and above are unlimited. A session already running on an account your plan stops covering says so rather than failing silently: *This session runs on a {name} account your plan doesn't cover. Switch it to another account, or upgrade to use this one again.*

### Choosing an account for a session

With two or more accounts signed in, the **Agent** list expands to one row per account, labelled with the account name, so you pick the agent and the account in one click. This is true in the task composer and in a draft session tab.

<figure style="text-align:center">
  <a href="/wp-content/uploads/account-multiple-selector-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/account-multiple-selector-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Agent list open in the New task composer, grouped by agent. Under a Claude Code heading sit two account rows, CLI (alex.lee@example.com, Acme) with a check mark and Personal, followed by Codex CLI, GitHub Copilot CLI, Cursor, Antigravity, OpenCode and the other agents, then Add another account and Install another agent.">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent list, with one row per account.</figcaption>
</figure>

With one account, the agent keeps a single row, with that account shown beside its name.

A session starts on the account you picked, and you can move it to another signed-in account of the same agent later, keeping the conversation. Session tabs name the account when more than one exists, and a tab whose account has since been removed reads **(account missing)**.

Kepler reads usage figures from the account the session is running on, not from whichever account happens to be first.

#### Moving a session to another account

To move a session to another account, use whichever of these is nearest:

- **Continue as** on the session's row or tab menu.
- The **Account** row in the composer's **Agent settings**: **Restart conversation as** on a live session, or **Resume as** on a dormant one.
- The agent and account part of a Terminal session's status bar.
- **Continue as {login}** on the usage-limit banner. See [When you hit a usage limit](#when-you-hit-a-usage-limit).
- The **Resume** or **Restart** split button on a dormant session, when another account could take the conversation.

Each list shows the agent's other accounts with their login, colour, and usage, and checks the current one. Picking one restarts the agent with this conversation as that account (*Restarts {name} with this conversation as {login}.*), and Kepler confirms **Continued as {login}**. An account that keeps its own history is greyed out as **Separate history**: *This account keeps its own history, so it can't read this conversation. Change that in Settings > Agents.* An account with no login offers **Sign in…**, and the accounts are locked while a turn is running.

<!-- TODO(screenshot): Replace — ade-continue-as-01: a live session's Agent settings with the Account row open on Restart conversation as, listing the agent's other signed-in account (needs two signed-in accounts of one agent). -->

***

## Signing in through your browser

Claude Code and Codex both sign in through a browser without dropping you into a terminal. In **Settings → Agents**, click **Sign in** and pick a method: the modal reads **Choose how you want to authenticate.**

| Connection | Claude Code | Codex |
|---|---|---|
| Local | Kepler runs the sign-in, your browser opens, and Kepler shows a status line instead of a terminal | Browser sign-in with your ChatGPT account |
| Remote or SSH | **Sign in with browser**: *Open Claude sign-in in your local browser, then paste the code it returns. Signs in the remote target directly.* | **ChatGPT (device code)**: *Sign in with a one-time code in your browser. Works on any remote.* |

Locally, **Open sign-in in browser** is there if the browser did not open on its own; if the callback cannot complete, Kepler reveals **Paste the code from your browser** with **Paste from clipboard** and **Submit code**. A rejected code says so: *That code was rejected. Copy the full code and try again.* On a remote, Codex shows the link and a **One-time code** to enter there; if your ChatGPT workspace turns device sign-in off, use **Import local Codex login** or an API key instead.

Auggie signs in the same way locally, and on a remote target asks you to paste the JSON it returns. Copilot uses a device code: **Sign in with GitHub**, then enter a one-time code at `github.com/login/device`.

On a remote Codex target you can also **Import local Codex login** to copy your local auth cache to that target. See [Remote Environments](/kepler/remote-environments).

Kepler warns you before a login lapses: *{N} days left before your {agent} login expires. Sign in again to renew it.*

***

## How a session runs

A session runs one of two ways, and the choice is no longer Claude Code's alone.

| Mode | What it is |
|---|---|
| **Chat** | *{agent} built into Kepler, with replies, diffs and plans you can read, review and search.* Kepler drives the agent over the Agent Client Protocol (ACP) and renders the conversation itself. The default |
| **Terminal** | *{agent}'s own command-line app, with its commands, shortcuts and settings, just as you use it today.* It runs in an embedded terminal inside the task |

<figure style="text-align:center">
  <a href="/wp-content/uploads/opens-in-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/opens-in-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Claude Code card in Settings › Agents, with the New sessions start in row ringed, set to Chat, and the help text You can pick the other one when you start a session.">
  </a>
  <figcaption style="text-align:center; color:#888">New sessions start in, on an agent's card in Settings → Agents.</figcaption>
</figure>


**Settings → Agents → *your agent* → New sessions start in** sets the default per agent, so Claude Code can default to Chat while Codex defaults to Terminal. To start one session the other way without changing the default, set **Start in** in the draft's **Agent settings**. Where a menu lists agents, such as **New session here** on a rail row, an agent that offers both modes also has a **Start in Terminal** or **Start in Chat** button. An agent that offers only one mode shows no switch at all.

To move a session that already exists, choose **Continue in Terminal** or **Continue in Chat** on its row or tab menu. The session resumes the same conversation in the other mode where the CLI can, and starts fresh where it can't. Kepler confirms **Continued in Terminal** or **Continued in Chat**, or reports **Unable to switch this session**. The item is locked while a turn runs (*This session is mid-turn. Wait for it to finish, or stop it first.*). A session started outside Kepler must be taken over first, and only a session on a task can move to Terminal.

<figure style="text-align:center">
  <a href="/wp-content/uploads/continue-in-terminal-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/continue-in-terminal-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The menu of a Chat session, opened from its row on the task page rail: Open, Show Agent Graph, Rename session, Copy session link, New session from this one, Continue in Terminal, Restart agent, Shut down agent, Archive session and Delete session.">
  </a>
  <figcaption style="text-align:center; color:#888">Continue in Terminal, on a Chat session's row menu.</figcaption>
</figure>

| Agent | Modes |
|---|---|
| Claude Code, Codex, GitHub Copilot, Cursor, OpenCode, Auggie, Grok Build | Chat or Terminal |
| Google Antigravity | Terminal by default. Chat runs Google's separate Antigravity ACP server, once it's installed and you pick **Chat** for the agent |
| Pi | Terminal only. Its CLI doesn't speak ACP |
| Your own agent server | Whichever its command supports |

Kepler works out what terminal mode can offer for an agent from the CLI's own flags rather than from a list of agent names, so a custom agent degrades the same way a built-in one does: a control an agent has no flag for is hidden rather than shown doing nothing.

A Terminal launch offers the options each CLI accepts on its own command line:

| Agent | Launch options in Terminal |
|---|---|
| Claude Code | Effort |
| Codex | Approval mode and reasoning effort |
| GitHub Copilot | **Reasoning effort** and **Model**, besides the context size |
| Auggie | **Reasoning effort**, per model |
| Cursor | Plan or ask mode |
| Grok Build | Permission mode: Default, Accept edits, Auto, Don't ask, or Plan |
| Pi | **Thinking**, from **Off** to **Max** |
| OpenCode | Model and agent, for a new session only; a resumed session keeps its own |

GitHub Copilot, Cursor, OpenCode, and Pi also take your first message on the command line when the installed version supports it, so it reaches the CLI as it starts.

### What's different in Terminal

Terminal mode is not a fallback. Kepler wraps the running CLI with the things a bare terminal has no way to give it: the task's shared context, Kepler's workspace tools where the CLI can load them, permission prompts you answer from here, and a transcript that survives a restart. What changes is the middle of the pane.

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

The status bar leads with the session and ends with its usage, left to right:

| Part | What it shows |
|---|---|
| Status dot | The session's state and, once it's idle, how long since the model last replied |
| Agent and account | Tinted with the account's colour when it has one, and drawn in a warning tone when the account's limit is spent. Click it for **Restart conversation as** to move the session to another account |
| Model, effort, and mode | What the *running* CLI reports rather than the picks you launched with, so a change made inside the CLI shows here |
| Context ring | The share of the context window in use. Hover for tokens used, available, and total, the estimated cost at API rates, and the prompt cache |
| Branch | The session's branch, with a folder mark when the CLI reports working in a subfolder or outside the worktree. Outside the worktree, the tip's folder line reads **Outside this worktree** |
| Plan usage | Two bars for the **5h** and **7d** windows, coloured by pace. Hover for the full readout; see [Usage indicators](#usage-indicators) |
| **Rich input** | Shows or hides Kepler's message composer. Hide it to type straight into the CLI |
| **No Kepler tools** | Shown when the agent can't use Kepler's workspace tools or inbox in a terminal. Its tip points to **Continue in Chat** on the session menu |
| **Idle detection** | Shown for an agent Kepler doesn't receive hook events from: *Activity is inferred from the terminal going quiet, because Kepler doesn't receive status events from this agent.* |
| Program status | Shown in place of **Idle detection** when the program in the terminal reports its own status. See below |

For an agent that can't tell Kepler it's waiting on you, the status dot's tip adds *{name} doesn't report when it's waiting on you, so check the terminal when it goes quiet.*

Hover any part for its card; a click pins the card open. A narrow bar sheds the least important parts first and brings them back as soon as they fit. Hovering an idle session's status shows its **Last reply**, its **Last prompt**, and, when the prompt cache is about to lapse or has, its **Prompt cache**: an idle session's next prompt can quietly re-read its whole context once the cache expires.

**Idle detection** is a statement about precision. Where an agent reports hook events, Kepler knows when a turn starts and ends. Where it doesn't, Kepler infers the same thing from the terminal going quiet, which is coarser: a long pause mid-turn can read as idle.

Some terminal programs report their own status to Kepler (through the OSC 7501 escape sequence). When the program does, the status bar names that status, with any message and progress the program sends. The hover card leads with the status and how long the program has been in it, shows progress as a bar (*{percent}% done*), and lists any sub-tasks with their own age and message. It adds *Reported by {app}* when the app isn't already the tab's name. When a blocked or failed program gives no reason, the card offers the next step, such as *Approve it in the terminal.* or *No reason given. Check the terminal.* The status drives the session's working, blocked, or done state without hooks:

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

A Terminal session tracked through hooks reports a failed turn too. When a Claude Code, GitHub Copilot, or OpenCode turn fails, for example on a usage limit, a rate limit, or a server error, the session shows **Error** with the CLI's own message once it comes to rest. For a usage limit, that message usually says when the limit resets.

The composer's **Agent settings** pill reports the model, effort, and mode the terminal session is using, but doesn't change them: its tooltip ends *Change these in the terminal*. Change them in the CLI itself; an effort or mode you change there survives the session relaunching.

More differences worth knowing:

- **Paste an image** into a Claude Code or Codex terminal and Kepler hands it to the CLI the way a paste into its own terminal would, so the agent reads it as an image rather than as a path it has to go and open.
- **A terminal session's conversation is recorded**, so quitting Kepler, an idle shutdown, a restart, or a reboot doesn't lose it. Reopening reattaches to the same conversation with its scrollback intact, and the session keeps running through a context compaction.
- **A first message Kepler can't type in safely at launch** waits in the composer as a ready-to-send draft instead: *Your message is ready to send. {name} starts without it, so send it once the terminal is ready.*
- **A first message Kepler can't confirm** isn't silently resent. Kepler holds it, says why, and asks you to *Check the terminal before resending.* The reason reads, for example, *Kepler was unable to read {name}'s version, so it can't confirm {name} is ready.* or *The message was too long to pass to {name} at startup.*
- **Lost keystrokes are never resent.** If Kepler can't tell whether your last keystrokes reached the terminal, it warns *Your last keystrokes may not have arrived* and asks you to *Check what the terminal shows before you go on.* Kepler never resends or late-sends that input. Typing resumes on its own once the input in flight settles.
- **A terminal reattaches rather than restarting.** While it loads it reads **Loading terminal…**. A short reconnect shows nothing; after a second a **Reconnecting to the terminal…** strip appears and leaves the last screen readable and scrollable, and only after five seconds does a cover hide the terminal. If it can't reconnect, **Unable to restore this terminal** says *The terminal is still running. Retry to load its output again.*, with **Retry**.
- **What you type during a reconnect is held**, and sent once the terminal is back. If the program printed in the meantime, Kepler drops it rather than typing into a changed screen: **The terminal changed while reconnecting**, *Nothing you typed was sent. Type it again.* Typing that never could be sent reads **Unable to send what you typed**.
- **One view types at a time.** A terminal another view is driving, in another window or on a Remote Access device, reads **Another view is controlling this terminal**: **Take control** to type here and size the terminal to this view.
- **Fast output is trimmed, not queued.** A terminal printing faster than the connection can show reads **Showing the latest output**: *This terminal is printing faster than this connection can show, so older lines are skipped.*

<div class="note" markdown="1">

**A terminal session is not the same as a terminal.** A terminal session runs an *agent*, lives in the **Sessions** column, and carries the task's context. A plain terminal runs your shell, lives in the drawer beneath the columns, and carries none. See [The Task View](/kepler/task-view#the-terminal-drawer).

</div>

***

## Sessions started outside Kepler

Not every conversation starts here. You run `claude` in a terminal, or you come back to something a week later from a transcript still sitting on disk. Kepler finds both and treats them as what they are: agent sessions it didn't start.

Nothing is taken over without you asking. Kepler binds a conversation to a task; it doesn't seize the terminal that's running it.

### Turning detection on

**Settings → Integrations → Your terminal → Show sessions started outside Kepler** is the one switch, and it is **on out of the box**.

It installs GitKraken hooks so the agent's own command-line interface reports what it's doing back to Kepler. One switch covers every agent Kepler can track this way: **Claude Code**, **Codex**, **Cursor**, **GitHub Copilot**, **OpenCode**, **Auggie**, **Grok Build**, and **Pi**. Google Antigravity isn't tracked through hooks. Turning the switch off silences all of them.

The same hooks are how Kepler follows a **Terminal** session. If a live session's hook events stop arriving, Kepler warns you rather than letting status and notifications drift: **Agent sessions aren't reporting to Kepler**, *Session status and notifications may be out of date. Repair reinstalls the reporting configuration.* After **Repair**, restart any session that still doesn't report. A window that only views sessions running on another computer gets the warning without **Repair**: *To repair reporting, use Kepler on the computer running these sessions.*

Detection is what makes a *live* outside session visible. **Past** sessions are read from the transcripts the agent already writes to disk, so a conversation from before you turned detection on can still be found. Kepler just had no way to watch it while it ran.

For where these sessions surface, and for turning one into a task, see [The Kepler Interface](/kepler/kepler-interface#external-sessions) and [Create a Task](/kepler/create-task#from-a-session-you-already-started).

### Reading one

An outside session opens read-only, marked **(external)** and **External**, with its transcript labelled **Session transcript (read-only)**. Its context card carries a badge for its state and one sentence saying where the conversation lives and what you can do about it from here.

| Badge | What it means |
|---|---|
| **Running** | Working on a turn, outside Kepler |
| **Waiting on you** | Blocked on a question or a permission request in its own interface |
| **Idle** | Connected and doing nothing |
| **Ended** | The process finished |
| **Not running** | Found on disk, with nothing running it anywhere |

The sentence follows the badge. A running session reads *Follow along here. You can fork it or continue it here once it goes idle.* A waiting one reads *It's asking you something in the terminal where it's running. Answer it there.* Kepler will not answer a prompt it doesn't own, but it does notify you that the session is waiting, whichever agent it is.

Kepler reads the transcripts of **Claude Code**, **Codex**, **GitHub Copilot**, **OpenCode**, **Auggie**, **Grok Build**, **Pi**, and the **Google Antigravity** CLI from each agent's own store on disk, without starting the agent. A **Cursor** row still appears and can still be adopted, with *Preview isn't available for {adapter} sessions yet.* in place of the conversation.

<figure style="text-align:center">
  <a href="/wp-content/uploads/external-past-session-preview-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/external-past-session-preview-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The preview of a past Pi session started outside Kepler, marked Not running, with its folder, Import session and Create new task, and the replayed conversation: the prompt, the agent's replies, and its Read products.js call.">
  </a>
  <figcaption style="text-align:center; color:#888">A past Pi session, previewed read-only from its transcript on disk.</figcaption>
</figure>

Some conversations are left out of the list: OpenCode's archived and subagent sessions, and Grok Build and Antigravity conversations with no messages yet. An Antigravity conversation is replayed but not followed live. A transcript Kepler can't read says which problem it hit rather than showing an empty conversation:

| What you see | What it means |
|---|---|
| **No transcript to show** | Kepler couldn't find the file. It may predate detection, or the agent stores it somewhere Kepler doesn't know to look, or never wrote one, as with a GitHub Copilot session started in Chat mode |
| **Kepler can't read this session's transcript** | The file exists but couldn't be opened. Check its permissions; Kepler keeps retrying |
| **Waiting for activity…** | Nothing has been written yet |

A live session that goes quiet is flagged rather than left looking busy: *No activity for {minutes} minutes. The session may have ended without reporting it.*

### Taking one over

Two verbs, and they differ in what happens to the terminal you started it in.

| Verb | What it does |
|---|---|
| **Fork** | *Copies this conversation into a new Kepler session. Your terminal keeps the original.* Both carry on independently |
| **Continue here** | *Picks up this conversation in Kepler where your terminal left off.* One conversation, now Kepler's |

On a session a terminal still owns, **Continue here** first asks **Continue this conversation in Kepler?**, because two clients writing the same conversation corrupts it: *Close it in your terminal first, or two clients will write the same conversation.* Both verbs unlock once the session goes idle; neither is offered mid-turn.

A conversation picked up from disk starts the agent on your first message rather than the moment you take it, so adopting one costs nothing.

***

## Sending a prompt

The composer sits at the bottom of the session.

<figure style="text-align:center">
  <a href="/wp-content/uploads/sending-a-prompt-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/sending-a-prompt-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The session composer with a pasted image.png attached as a thumbnail chip and the draft @cart.js @README.md Does the check also cover these codes? Below the draft sit Attach a file and the microphone, then the Agent settings pill (Docs Model, Build, with its chevron), the context usage ring, and Send with its chevron.">
  </a>
  <figcaption style="text-align:center; color:#888">The composer, at the bottom of the session.</figcaption>
</figure>

| Control | What it does |
|---|---|
| **Attach a file** | Attaches a file for the agent to read. Drag onto the composer works too: *Drop files to attach*. On a remote connection, **Add a file from the remote** picks from the remote machine |
| Microphone | Voice input. See [Voice Input](/kepler/voice-input) |
| **Agent settings** | Agent, model, permission mode, effort, and options |
| Context usage | The share of the session's context window in use, drawn as a ring. Hover for tokens used, available, and total, the estimated cost at API rates, and the prompt cache |
| Plan usage | Your provider plan's usage windows and when each lifts. See [Usage indicators](#usage-indicators) |
| **Send** | Sends the prompt, and shows a sending state from the moment you click. The chevron holds **Send** and every applicable Action |

**Attaching a file sends a path, not a copy, wherever it can.** A file the session's machine can already read (one you drop, paste, or pick on the same machine, or pick from the remote in a remote window) goes as a pointer, and its chip reads *File on this machine* or *File on the machine*. Anything else is uploaded once into the task and its chip reads *Copied to the task when you send*. A send is all or nothing: if an upload fails, the message isn't sent (*Unable to upload {name}. Your message wasn't sent.*). An attached file's card on the task page offers **Open in default app** and **Show in Finder** (macOS), **Show in Explorer** (Windows), or **Show in file manager** (Linux), where the window can reach that machine.

**A pasted pull request or issue link becomes a chip.** Paste the URL of a pull request or issue from a connected GitHub, GitLab, Bitbucket, or Azure DevOps host, self-hosted included, or of a Jira or Linear issue. In a task's session composer or the new-task composer, Kepler turns the URL into a chip labelled with its number, such as **#49**, and puts the label in your text in its place. Hover the chip for the title and the URL. When you send, Kepler attaches the link to the task. A prompt that is a slash command keeps the URL as typed.

<figure style="text-align:center">
  <a href="/wp-content/uploads/pasted-link-chip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/pasted-link-chip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task session's composer after pasting a pull request link: a chip with the pull request icon and #49 sits above the prompt Does this conflict with #49?, and its tooltip shows the pull request's title, Round prices through a shared roundCents helper, over its GitHub URL.">
  </a>
  <figcaption style="text-align:center; color:#888">A pasted pull request link, turned into a chip.</figcaption>
</figure>

**Tab** moves from the prompt to **Send**, then to its chevron, and a draft you haven't sent survives a reload. **Down Arrow** or **Alt+Down** on **Send** opens the chevron's menu too, and closing the menu returns focus to **Send**.

The agent pill sits beside **Send** on every surface that has a composer, so the launcher and a live session read the same way. The agent picker is a list of labelled rows, and the agent-settings menus have a **Search options…** box for agents with long option lists. Every control carries a real tooltip.

**Enter** sends; **Shift+Enter** inserts a newline. **Cmd/Ctrl+F** opens **Find in conversation**. **Start typing anywhere in a session** and the composer takes the keystroke, so you don't have to click into it first.

While a turn is running the send button grows a stop segment: *Interrupt current work. Queued messages will be sent next.* Send stays live throughout, because a busy session steers.

### Slash commands and skills, per repository

Type `/` to open the command menu. It lists the agent's built-in commands together with your commands and skills. A slash command sent as a session's first prompt runs as a real command, not as text.

In a Claude Code **Chat** session, `/design` and `/slides` work as they do in the CLI, and Claude can publish artifacts once **Artifacts** is on for the session. See [Claude artifacts](#claude-artifacts). Codex reports its skills with a `$` sigil and invokes them that way, so `$` opens a skills-only menu, but `/` still finds them, matched on the bare name, so you do not have to know the convention.

**Skills and slash commands are discovered per repository, not per agent.** The catalog is the union of your home-directory skills and the repository or worktree's own: for Claude Code, `~/.claude/skills` plus `.claude/skills`. Two consequences:

- One project's skills never show up in another project's menu.
- A skill added in a worktree and not yet committed can appear in that session before it appears elsewhere.

Kepler probes the catalog when you pick a repository and refreshes it whenever a live session reports a change, so a skill you add mid-session shows up without a restart.

### Mentioning files

Type `@` to search the working directory and insert a path. A session that runs in the task folder also lists the task's other worktrees and folders, under **Worktrees and folders** above **Files**; pick one, or type its name and `/`, to search inside it. A path with spaces goes in quotes (`@"…"`), and Kepler adds them when you pick such a path. `@` also works in composers that don't belong to a session yet, where it searches the task's folders or the folder you chose. Kepler automatically approves files you paste into a chat for the agent to read.

***

## Steering a running turn

You do not have to wait for a turn to end. **Send while the agent is working and your message steers it** rather than sitting until the turn is over.

Send during a turn and the message parks in a visible queue: the placeholder changes to *Type a message to queue...* and a banner above the composer counts what is waiting. The queue then leaves as **one merged follow-up prompt** at the earliest moment that is actually safe:

| When it goes | Why |
|---|---|
| Immediately | The agent supports steering and no tool call of its own is in flight |
| At the next tool-call boundary | A tool call is running and can't be interrupted mid-flight |
| At the end of the turn | The agent supports no steering at all |

A background subagent's tool call never holds your message back; only the main turn's own calls do.

Everything you send during one turn is merged and handed over together, so two quick corrections arrive as one instruction rather than two competing ones.

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
| *Sending at {time}, when the quota resets.* | The account hit a usage limit. The queue waits for the reset instead of sending into the limit. See [Usage indicators](#usage-indicators) |
| **Send now** | Releases a queue held for a usage limit straight away |
| **×** on a row | Removes that one prompt |
| **Clear queue** | Removes all of them |
| **Send queue** | Sends a queue left waiting on a session that is no longer working |
| **Interrupt & send** | Stops the current turn and delivers the queue immediately, in one act. **Cmd/Ctrl+Shift+Enter** is the same thing from the keyboard: the send combo, escalated. With subagents running it names them: **Interrupt & send ({count} running)**. If the stop goes unanswered, the button becomes **Force quit (drops {count} queued)**: it ends the agent and the queued prompts are dropped rather than sent |

Queued prompts survive interruption, and a restart of Kepler. A **disconnect**, an expired token that forces **re-authentication**, and the **reconnect** afterwards all keep the queue: the rows stay on screen, nothing is dropped, and the prompts are handed to the reconnected session in the same order, under the same identities. Cancelling a turn promotes the next queued prompt rather than discarding it.

Each queued prompt picks up the Task's shared context as it stands when the prompt actually runs, not as it stood when you typed it.

If a send genuinely fails, Kepler puts the text back: *Something went wrong. Your message is back in the composer — try again.* If you have since typed a newer draft, it keeps that one and offers **Restore message**.

### Stopping a turn

| What you do | What happens |
|---|---|
| **Escape** | Stops the running turn |
| The stop segment on the send button | The same thing, with a pointer at what it does to the queue |
| **Cmd/Ctrl+Shift+Enter** | **Interrupt & send**: stops the turn *and* delivers what you typed |
| **Force quit the agent** | Offered once a cancel has been pending too long. It does not wait for the agent to settle |

A cancel that is taking too long escalates rather than leaving you with a button that appears to have done nothing.

In **Terminal** mode an interrupt is recognised whether it arrives as **Escape** or as **Ctrl+C**, and the turn counts as cancelled only once both the CLI's hooks and its output have gone quiet, so a stopped session stops reading as though it were still working.

***

## Reading the conversation

- Your messages appear as chat bubbles. Right-click one to **Copy message**, **Quote**, **Ask**, or **New session from here**.
- Agent replies render as markdown, and stream as one continuous message even when a tool runs mid-reply. Right-click a reply to act on its whole turn: a band outlines the turn while the menu is open, and **Copy message** copies all of the main agent's text in that turn. Every message menu starts with the message's exact time.
- Each prompt, and the reply that closes each turn, has a copy button beneath it.
- Each message shows when it was sent, and a long gap between messages gets a divider.
- An agent's thinking shows as a collapsed **Thinking** block, for agents that send it.
- A file path an agent writes (a link, an inline-code path, or the file in a read or edit tool call) becomes a link once Kepler confirms the file exists. Click it, or **Cmd/Ctrl+click** it, to open the file in Kepler at the named line; a file inside a worktree opens in the Changes overlay's file view. **Cmd/Ctrl+Shift+click** opens it in your default editor at that line, or in Kepler when no editor takes it, and the link's tooltip says so (**+ Click to open in editor**). A middle-click acts as a plain click.
- A Kepler task or session link in the conversation opens inside Kepler when you click or middle-click it. Hover it to see where it goes; right-click it for **Open in Kepler** and **Copy link**.
- Images in replies and tool output open in a lightbox, and both the thumbnail and the lightbox can save the image with **Save as…**.
- Tool calls collapse into groups: **{count} tool uses**, with **{count} done**, **{count} running**, and **{count} failed** tallies. Expand a group to read any call's output. A failed call that the agent has already moved past stays folded inside the collapsed group, and the failed tally still counts it.
- A plan renders as **Plan {completed}/{total}**, and a plan cut short by a stop is marked **Interrupted**.
- A context compaction shows as its own row: **Compacting the conversation…**, then **Conversation compacted**, **Unable to compact the conversation** with the error, or **Compaction stopped**. When the agent kept a summary of the conversation so far, the row expands to show it, and **Find in conversation** searches it.
- Subagents get their own card, collapsed by default, holding **Prompt**, **Operations**, and **Result** sections that fold independently. Its trigger row carries the subagent type, the description it was given, how many operations it has run, the step a running subagent is on, and a status of **Running**, **Stopped**, **Completed**, or **Failed**, so a card that is still shut shows progress. Claude Code, GitHub Copilot, Cursor, and OpenCode Chat sessions all produce these cards, and a subagent that was cancelled or cut off reads **Stopped** rather than **Failed**.
- A session that another session started shows **Started by** and the starting session in its header. Click it to open that session.
- A prompt that another session sent carries a **From:** header naming the sending session. Click it to open that session.
- A turn that ended for a reason worth knowing carries a pill: **Reached token limit**, **Reached request limit**, **Refused to continue**, or **Cancelled**. A healthy turn shows nothing.

<figure style="text-align:center">
  <a href="/wp-content/uploads/compaction-row-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/compaction-row-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A Chat transcript in which, after the Read checkout.js call and the agent's note, a Conversation compacted row is open on the summary the agent kept of the conversation so far, followed by Edit checkout.js and the agent's next message.">
  </a>
  <figcaption style="text-align:center; color:#888">A compaction row, expanded to the summary the agent kept.</figcaption>
</figure>

Subagent work is attributed rather than mixed into the main thread. A subagent's own tool calls nest inside its card under **Operations** instead of appearing flat alongside the main agent's, and its narration renders in an indented lane of its own, marked **Subagent**, so you can see where it starts and stops even when it interleaves with the main agent's text. A subagent can start subagents of its own: their cards nest inside it, the outer card counts every permission request waiting anywhere beneath it, and a request from a nested subagent shows on the outer card under a path of subagent names, such as **Parent › Child**. While a turn is running, that turn's subagent cards pin to the top of the session and drop back into the conversation when the turn ends; a card you expanded stays expanded for the rest of the turn.

**Open subagent transcript** on a subagent card, or on its running chip above the composer, opens that subagent's own transcript: its prompt, then its narration and tool calls in the order they happened, then its result. It updates live while the subagent runs, and the card and chip show the step in progress. In a wide pane it docks beside the chat; in a narrow one it covers the chat, with **Back to {title}** to return. A permission request raised inside the subagent is answered in that pane while it's open.

In a Claude Code or Codex Chat session, you can also direct one subagent from its pane rather than the whole turn:

- **Message {name}** sends the subagent a message through the main agent, and the pane notes *Sent through the main agent*, or *Waiting for the main agent* while the main agent is busy. A slash command can't be passed on, and a subagent that has already finished reports *Unable to deliver the message to {name}, which may have finished*.
- **Stop** (Claude Code) ends that subagent alone. Codex offers **Ask to stop** instead, which asks the main agent to stop it.

For other agents, the pane is marked **read-only**.

<!-- TODO(screenshot): Replace — ade-subagent-pane-01: a Claude Code Chat session with a running subagent's pane docked beside the chat, showing Stop, the current step, and the Message {name} box with Sent through the main agent. -->

A Claude Code session can keep **background tasks** running after its turn ends, such as a monitor or a backgrounded shell. In any Chat or Terminal session, another agent's CLI that the session starts for its own work, such as a `claude` or `codex` run from the agent's shell, is listed among its background tasks while it's busy, as the agent's name and the start of its prompt. While one runs, the session reads **Working in background** rather than **Idle**, the task's card reads **Running in background**, and **Stop background task** on the card or its chip stops that one task without touching the session.

Code blocks carry a **line-wrap toggle**, so a long line can be read without scrolling sideways, and take their syntax colours from your Kepler theme. A code block longer than 15 lines folds to a 15-line preview with **Show {count} more lines** and **Show less**; a match from **Find in conversation** inside it opens it. Numbered lists stay continuous rather than restarting at 1 after an interruption.

### Claude artifacts

Artifacts are a switch on each Claude Code Chat session, because the artifact tools add about 12k tokens to the session's context. A new session starts with them off unless **Settings → Agents → Claude Code → Artifacts in new sessions** is on. To turn them on for one session, tick **Artifacts** in its composer's **Agent settings**: *Lets the agent publish pages and designs. Adds about 12k tokens to the session's context. Turning it on in a running conversation restarts the session.* In a running conversation, Kepler asks first, **Turn on Artifacts?**: *The session restarts and resumes this conversation. The running turn, background shells and subagents, and queued messages end. Artifacts stay on for this conversation.* From then on the row reads **On for this conversation**, and while a session is still starting it reads **Available once the session has started**.

<!-- TODO(screenshot): Replace — ade-artifacts-toggle-01: a live Claude Code Chat session's Agent settings showing the Artifacts checkbox with its description (needs a signed-in Claude Code). -->

When a Claude Code Chat session with artifacts on publishes an artifact, including `/design` and `/slides` output, it shows as a card rather than a tool call: title, version, **Private**, **Open**, **Copy link**, and **Preview**. A republish reads **Updated to v{seq}**. The artifact is also attached to the task as a link, so it stays reachable after the conversation scrolls on.

**Preview** opens the published page in a pane beside the chat, loaded from the local file the session published, with **Reload** and **Close preview**.

Approvals name what Claude is about to do rather than showing raw tool input, for example *Publish a new private page?*, *Update to a new version?*, or *Permanently delete?*

Anyone with edit access to a published artifact can comment on it, and by default a comment starts a turn in the session that published it, with a reply posted automatically. The first time a session publishes, the **Artifact comments can start turns** notice offers **Keep on** or **Turn off**. The standing setting is **Settings → Agents → Claude Code → Let artifact comments start turns**; running sessions keep the value they started with, and the setting lists them with **Restart all** and **Restart selected ({count})**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/artifact-card-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/artifact-card-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A published artifact shown as a card in a session's chat: its icon, the title Acme gift cards with v1 beside it, a Private lock below, and Preview, Open and a copy link button.">
  </a>
  <figcaption style="text-align:center; color:#888">A published artifact's card in the chat.</figcaption>
</figure>
<!-- TODO(screenshot): New: The Artifact comments can start turns notice under a Claude Code Chat session's first artifact card, with Keep on and Turn off. -->

<figure style="text-align:center">
  <a href="/wp-content/uploads/artifact-chip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/artifact-chip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The artifact attached to the task as a link chip, Acme gift cards, under the task's worktree pill, with its hover card open showing the artifact's title, its link, Open and Copy link.">
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

**Settings → Appearance → Chat** controls how the transcript scrolls and how wide it grows:

| Setting | What it does |
|---|---|
| **Chat auto-scroll**: **Auto-scroll to the end** | *Keeps the newest output in view. Scroll up to stop.* The default |
| **Chat auto-scroll**: **Stay on my message** | *Keeps your message in view. The transcript doesn't scroll on its own.* |
| **Conversation width** | *How wide the conversation grows in a wide pane. The message box keeps its width.* **Narrow** (the default), **Wide**, or **Full width** |
| **Remember scroll position** | *Return to where you left off when you come back to a session.* On by default |

Sessions you started in your own terminal appear too, marked **(external)**, read-only. See [Sessions started outside Kepler](#sessions-started-outside-kepler) above.

***

## When the agent asks you something

Kepler pauses and asks you directly when an agent needs a decision it can't make on its own. It does this in the following ways:

- A permission request before a risky tool call.
- A structured question when the agent wants your input mid-task.
- A plan review when the agent proposes a plan before it starts.
- An approval card when the agent asks Kepler itself to do something that needs your say, such as deleting a worktree.

Reports from other agents arrive in a session's inbox rather than asking you anything; see [Reports from other agents](#reports-from-other-agents).

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-permission-request-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-permission-request-oct-2026.png" class="help-center-img img-bordered" alt="A permission request for a shell command, marked Needs approval, with the agent's reason, Contains brace with quote character, just above the Allow, Allow for this session, and Reject buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">A permission request, with the agent's reason above the buttons.</figcaption>
</figure>

### Permission requests

A request pins to the top of the session: an amber shield, the tool being asked about as the heading, and the call's input beneath it. When the agent says why it's asking (for example, a Claude Code session in auto mode that still hits a safety check), that reason sits just above the buttons. A request to reach outside the agent's network sandbox says so in Kepler's own words, *Reaches outside the network sandbox.*, with the agent's reason when it gives one. The buttons are Kepler's own wording rather than the agent's, so a request reads the same whichever agent raised it.

| Button | What it does |
|---|---|
| **Allow** | Approves this one call |
| **Allow for this session** | Approves this call, and auto-approves matching follow-ups for the rest of the session. The agent is told only that you allowed it once, so it writes no rule of its own |
| **Allow always** | Hands the agent a permanent approval, which the agent stores in its own settings |
| **Reject** | Refuses this call |
| **Reject always** | Refuses it permanently |

You get the tiers the agent actually offers. **Allow for this session** is Kepler's own middle tier and appears only next to an **Allow**. A request that offers nothing but a permanent approval, as Claude Code's plan-exit prompt does, has no one-shot decision to widen. Where an agent draws its own distinction between several permanent choices, its labels are kept instead of a single **Allow always**, and any `Tool(...)` pattern a rule would cover is spelled out on a **RULE** line beneath the buttons.

Kepler coalesces repeats. A command that fires many identical requests (an install reaching the network over and over) asks once, and your answer settles the whole group.

A request raised by a subagent that another subagent started surfaces on the outermost subagent card, under the path of subagent names that leads to it (**Parent › Child**). See [Reading the conversation](#reading-the-conversation).

Answered requests stay in the transcript, showing the tier you picked: **Allowed for this session** for the middle one, otherwise the button's own label, falling back to **Approved** or **Denied**.

#### Requests that arrive through hooks

A session running in **Terminal** mode, and one Kepler **detected outside itself**, both ask through the agent's own hooks rather than over ACP. You still answer in Kepler either way, without switching to the CLI's own prompt to reply. The card is the agent's, though, so it carries scopes instead of Kepler's tiers: **Deny**, **Allow once**, and one **Always allow** per scope the hook suggests, narrowest first.

| Scope | Meaning |
|---|---|
| **this session** | Until this session ends |
| **this project (local)** | This project, your machine only |
| **this project (shared)** | This project, committed for your team |
| **all projects** | Everywhere |

Kepler prints the rule each button would write above them. A rule with no command pattern is annotated **(this tool)**, meaning it covers every call to that tool rather than one command.

Kepler never approves a hook request on your behalf. If it stops holding one without your answer (the turn ends, the conversation moves elsewhere, or Kepler quits), it hands the request back to the CLI, which asks in its own dialog.

A Codex question asked through its hooks shows in Kepler as a question you can answer, with its options and their descriptions. Cursor has no permission or notification hook, so a Cursor Terminal or outside session can't tell Kepler that it's waiting on you: it reads **Running** until it stops, and you answer in the terminal.

### Multiple-choice and multi-select questions

Agents can ask you structured questions instead of guessing. The form renders in the conversation at the point the agent asked. In Chat, Claude Code, Codex, and Cursor questions all arrive in this form, and a Cursor question that takes several answers works as a multi-select.

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
- Press **1**–**9** to pick an option by the number shown on it.
- **Other...** opens a free-text field (*Type your answer...*), which becomes the answer on its own for a single-choice question, and joins the ticked options on a multi-select. For Codex, this field takes the place of its own **None of the above** option.
- Several questions arrive as steps with a **{current}/{total}** counter and a tab strip; submit is enabled only once nothing is outstanding, and until then you see **{count} questions still unanswered**.
- **Chat about this** declines the form so you can answer in your own words in the chat. It does not cancel the session.
- If the agent set a deadline, the form counts down (**{count} seconds remaining**), and a form that was never answered is recorded as **Left unanswered** rather than left on screen as if it had been submitted.

A restored session shows the question and the answers you gave as a read-only record.

### Reviewing a plan

When an agent in plan mode proposes a plan, Kepler opens it for review in a **Plan** panel beside the chat, with **Preview** and **Edit** tabs, and the transcript shows the plan with **Open plan**. Claude Code, Codex, GitHub Copilot, Cursor, and OpenCode Chat sessions offer plan review. Cursor holds its plan request open while you review it, so the session waits with the reason **Plan review**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/plan-review-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/plan-review-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A Chat session with its Plan panel open beside the transcript for the plan Fix the discount order in the cart total. Step 2, Round once, at the end, to two decimal places, is highlighted and carries a comment under Comments (1), with Request changes (1) and a greyed Approve & implement at the foot.">
  </a>
  <figcaption style="text-align:center; color:#888">A plan under review, with a comment on one step.</figcaption>
</figure>

To review the plan, use the following:

| Control | What it does |
|---|---|
| A comment on a passage | Select text in the plan and say what should change (*What should change?*). Comments collect under **Comments ({count})** |
| **Request changes ({count})** | Sends your comments back so the agent revises the plan. Each revision is kept, so you can step back to an earlier one |
| **Approve** or **Approve & implement** | Accepts the plan, and the agent leaves plan mode to carry it out. The chevron lists any other ways the agent offers to approve |

While comments are pending, approving is blocked: *Submit or delete your comments before approving.* Auggie shows its plan as a task checklist instead, and **Hide these tasks** clears it.

### Approval requests

Some things an agent asks Kepler itself to do, through Kepler's workspace tools, wait for your approval, for example:

- Sending a prompt or a message to another session, or stopping, renaming, or archiving one.
- Editing or deleting a task note, changing another task or its links, detaching files, or archiving a task.
- Deleting a worktree.
- Starting a session in a more permissive mode than the asking session's own.
- Syncing a branch with its target, or rewriting its commits.
- Overwriting a theme file.

The agent is told the request is waiting and can carry on; your answer reaches its inbox later. Meanwhile the session reads **Approval needed**, or **Approval needed, destructive**. The request is pinned above that session's composer as a card naming the action, such as **Delete worktree {worktree} and its branch**, with what's at stake (*At risk: {loss}*), **Approve**, and **Deny**. A card for an action that can lose work is amber; other cards are blue. Several requests page through with **{index} of {count}**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/approval-card-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/approval-card-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="An amber approval card pinned above the session composer, Delete worktree acme-web@kepler/cart-total-spike and its branch, At risk: 2 uncommitted files, with the Approve menu open on Approve all worktree deletes from this session and a greyed Always approve worktree deletes.">
  </a>
  <figcaption style="text-align:center; color:#888">An approval card for deleting a worktree, with the Approve menu open.</figcaption>
</figure>

The **Approve** chevron offers two wider answers:

- **Approve all {label} from this session** approves this kind of request for the rest of the session.
- **Always approve {label}** adds a standing rule. It isn't offered for an action that can lose work (*Not offered for actions that can lose work.*) or for starting a session.

An approved request shows **Running** while Kepler carries it out, after checking that it still applies. One that fails shows **Not done: {summary}**, with **Dismiss**. A waiting request expires when its session is archived.

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

When an item arrives for an idle session, Kepler wakes the session to read its inbox, and the conversation shows a row such as **2 new items to read**. A busy session is woken once its turn ends.

A session with unread reports carries a reports badge with a count on its tab and rail row (*{agent} hasn't read {count} reports from other agents*), and the band above its composer offers **Have it read them**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-reports-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-reports-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The task page for Fix the cart total, where the Discount codes break the cart total session carries a reports badge with 3 beside the reviewer it started. Its conversation shows a 2 new items to read row, and above the composer OpenCode hasn't read 3 reports from other agents, with Have it read them.">
  </a>
  <figcaption style="text-align:center; color:#888">A session with unread reports from other agents.</figcaption>
</figure>

So that agents can't keep waking each other indefinitely, wakes pause after 20 turns in a row that agents started without a prompt from you. The band then reads **Reports from other agents are paused**: *They no longer wake this session on their own. Resume to let them wake it again.* **Resume reports**, or your next prompt, lets them wake it again.

In Terminal mode, only Claude Code, Pi, and OpenCode 2 sessions can be woken to read their inbox. Another Terminal agent shows **No Kepler tools** on its status bar: *{name} can't use Kepler's workspace tools or inbox in a terminal.*

***

## Usage indicators

Two different readouts, and they measure different things.

<figure style="text-align:center">
  <a href="/wp-content/uploads/usage-indicators-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/usage-indicators-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Context window card open above the composer's context ring, which sits between the Agent settings pill (Docs Model, Build) and Send: 68%, with 136K tokens Used, 64K Available and 200K Total, and the Estimated cost at API rates, $0.42.">
  </a>
  <figcaption style="text-align:center; color:#888">The Context window card, from the context ring.</figcaption>
</figure>

| Readout | What it shows | Availability |
|---|---|---|
| **Context window** | How much of *this session's* context window is used, as a ring. Hover for tokens used, available, and total, the **Estimated cost at API rates**, and the **Prompt cache**: when it expires, and how much of the session's input came from it (*{percent}% cached*) | Whenever the agent reports it |
| **Plan usage** | Your provider plan's windows (**5h** and **7d**) as **Used** and **Resets** columns, plus whatever else the provider reports about the plan | Claude Code and Codex sessions report their own 5-hour and 7-day limits. The full readout, and Auggie, need **Check plan usage with each agent's provider**, which is on by default |

While a session rests, the context ring warns about the prompt cache on its own: an hourglass with the time the cache has left, or **Expiring** or **Expired**. The context card then leads with the cache and warns *The next message re-reads most of the context.* With no context reading, the ring is drawn as a dashed circle, and its card still shows the cost when the agent reports one.

**Check plan usage with each agent's provider** fetches the full readout, including per-model limits and extra usage, from each agent's provider. It's on by default, in **Settings → Agents → Usage limits**:

<figure style="text-align:center">
  <a href="/wp-content/uploads/show-token-usage-aug-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/show-token-usage-aug-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Usage limits section of Settings › Agents: Check plan usage with each agent's provider, ticked, with its help text on what Kepler asks the provider for and what it shows when off, and Resume after the usage limit resets, unticked.">
  </a>
  <figcaption style="text-align:center; color:#888">Check plan usage with each agent's provider, in Settings → Agents → Usage limits.</figcaption>
</figure>

> Kepler asks each agent's provider for your plan usage, per-model limits and extra usage, using the agent's own sign-in. The sign-in goes nowhere else and is never changed. When off, Kepler shows only what agents report, and a message queued at a usage limit is sent automatically only if the agent says when the limit resets.

With the setting off, Kepler makes no request to any provider, but a Claude Code or Codex session still reports its own **5h** and **7d** readings as it runs, and those show. A card drawn from those readings alone says so: *Reported by the agent. Turn on {setting} in {section} to also see per-model limits and extra usage.*

The meter previews the shortest window, or the remaining plan balance where the provider reports a balance but no expressible percentage; hovering opens the detail. A spent window reads **Limit reached until {time}**, and every reading says how old it is (**Updated {when}**), with **Refresh** to ask again.

A usage bar is judged by pace: the share of the window you've used against the share of the window that has passed. Its detail reads **On pace** or **Ahead of pace**, and when you're ahead it estimates when the window runs dry, for example *Runs out in ~{duration} at this rate*. The bar turns amber once your use is more than 15 points ahead of pace, and red past 30 points; 90% used is always at least amber, and 100% is red. Below 10% used, or when there's no pace to judge, fixed bands apply instead: amber above 75% and red above 90%.

| Provider | What its popover carries |
|---|---|
| **Claude Code** | The **5h** and **7d** windows, and an **Extra usage** pool with credits used against any monthly limit |
| **Codex** | The same two windows, plus **Usage limit resets**: earned resets that clear an active limit early, each with its expiry |
| **Auggie** | No windows, only the plan's credit balance: a plan line naming the plan with what is left of it, *{remaining} / {included} credits left*, or *{remaining} credits left* on an unmetered plan |

An account on a third-party Claude provider shows no usage. If the figures cannot be fetched, the meter says which problem it hit rather than showing a stale number, for example *Sign in to {agent} to see usage data.* or *This agent doesn't expose usage data.* It adds *Your sessions aren't affected.* where that applies.

### When you hit a usage limit

A session doesn't keep sending into a spent limit. As soon as the account's usage reading, or the agent's own report, shows its limit spent, Kepler holds prompts you queue until it lifts, rather than waiting for a turn to fail first. The queue banner reads *Sending at {time}, when the quota resets.* The prompts go out on their own shortly after the reset, even with no Kepler window open and across a restart. **Send now** releases one session's queue early. A spent limit on one model doesn't hold prompts for the account's other models. With **Check plan usage with each agent's provider** off, a queued prompt waits only if the agent itself says when its limit resets.

<!-- TODO(screenshot): New: The queue banner holding a prompt until the quota resets (*Sending at {time}, when the quota resets.*) with **Send now**. -->

A turn that hits the limit before the agent produced anything isn't lost: Kepler sends the same prompt again after the reset. If a turn is cut off by the limit after the agent had started replying, with nothing queued, the session stays put unless you turn on **Settings → Agents → Usage limits → Resume after the usage limit resets**: *When a turn is cut off by your account usage limit and nothing is queued, Kepler queues a "continue" message that is sent shortly after the limit resets.* It's off by default, and the queued message can be sent early or removed like any other.

When a session's account reaches its limit, a banner says so, **{login} reached its usage limit**, with *Available again at {time}.* To keep going now, **Continue as {login}** moves the conversation to the account with the most room left, and its menu lists your other accounts. See [Moving a session to another account](#moving-a-session-to-another-account). With no other account to take the conversation, the banner suggests *Add another account to keep going.*

This applies to agents Kepler can read usage for: Claude Code, Codex, and Auggie.

***

## Voice input

Every session's composer has a microphone. Click to record, speak, and the transcript lands in the prompt; transcription runs on your device. Voice input is off until you enable it and download a model.

<figure style="text-align:center">
  <a href="/wp-content/uploads/start-voice-input-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/start-voice-input-aug-2026.png" class="help-center-img img-bordered" alt="The composer's microphone icon, with its Start voice input tooltip">
  </a>
  <figcaption style="text-align:center; color:#888">The composer's microphone icon.</figcaption>
</figure>
<!-- TODO(screenshot): Replace — ade-start-voice-input-01: the composer microphone hovered with a Qwen3-ASR engine ready, tooltip Start voice input · Qwen3-ASR 1.7B (needs the voice model downloaded). -->

When a Qwen engine is dictating, the microphone's tooltip names it, for example **Start voice input · Qwen3-ASR 1.7B**. When voice input can't start, the tooltip says why, such as a graphics card that isn't responding or a model that needs WebGPU, and links to the engine's settings. See [Voice Input](/kepler/voice-input).

***

## Session status

Each session carries a state, shown as a coloured dot on its tab and rows.

| Status | Meaning |
|---|---|
| **Spawning** | Starting up |
| **Ready** | Connected, nothing sent yet |
| **Running** | Working on a turn |
| **Waiting** | Blocked on you, and it says on what: **Permission**, **Question**, **Plan review**, or **Prompt not sent**. A pending Kepler approval also counts, as **Approval needed** or **Approval needed, destructive**, even while the agent keeps working |
| **Unread** | Finished a turn you have not looked at |
| **Idle** | Connected, nothing running |
| **Working in background** | The turn ended, but a Claude Code background task is still running. Shown like **Running**, and it keeps the machine awake |
| **Reconnecting** | Kepler is reattaching to a session that kept running while Kepler restarted |
| **Error** | The turn or the process failed. A live session whose last turn failed on a rate limit, an exhausted quota, or an overloaded provider reads **Error** too |
| **Ended** | The agent process isn't running. The conversation is kept, and a dormant session reads *{state} (ended)*, its last state, until your next message starts it again |

When Kepler has to show one status for several sessions, the most urgent wins: **Waiting** and **Error** outrank live work, and **Unread** sits above **Idle** so a finished turn is not buried.

Away from the session itself those states collapse into a coarser ramp of five (attention, active, idle, errored, inactive), which is what [the main list](/kepler/kepler-interface)'s row and preview indicators read, and what decides where an [Action](/kepler/actions) fires. *Attention* covers both a waiting session and one holding an unanswered permission request, question, or approval request.

Task and session rows add one line saying what a session needs from you, most pressing first: **Approval needed for {tool}**, **Asking: {question}**, **Waiting for you**, **Terminal waiting for you**, or **New reply**.

***

## Tabs, archiving, and restoring

Open sessions form a tab strip. Each tab shows the agent, the account when more than one exists, and a status dot. Drafts sit in the same strip, marked **(draft)** when the strip has room.

Hover a session's tab, its rail row, or a Terminal session's status bar for its card. Under the account, the card can add the following lines:

- **Running in the background**, with **and {count} more**, for background tasks still running.
- **Continued from {name}**, for a session started from another.
- **Rate limited · Resets {time}**, when the account's limit is spent.
- **Context {percent}%**, the share of the context window in use.

The following table lists what you can do with tabs:

| Action | Result |
|---|---|
| **Cmd/Ctrl+T** or **+** | Opens a draft tab for a new session. See [Draft session tabs](#draft-session-tabs) |
| **Alt+1**–**Alt+9** | Jumps to a tab by position |
| **Cmd/Ctrl+Shift+[** / **]** | Previous or next tab |
| **×** on a tab in the Sessions column (**Archive session**) | Archives the session |
| **Archive** on a rail row | The same thing |
| **Restore** | Brings an archived session back into the strip |
| **Shut down agent** | Ends the process without archiving the session |
| **Restart agent** | Shuts it down, then reconnects |
| Drag a tab | On the Dashboard, reorders session and terminal tabs |

**In the Sessions column, closing a tab and archiving are one operation.** Kepler stops the agent process, saves the conversation and its resume handle, and takes the tab out of the strip. Nothing is deleted. With **Show tabs on the task page** turned on, a tab's **×** is **Close tab** instead: it only hides the tab, and the session keeps running. See [Task View](/kepler/task-view#tabs-and-groups).

### Shutting down and restarting an agent

Ending a session and filing it away are separate acts, on a live session's row menu:

- **Shut down agent** cancels the turn, waits a bounded grace for it to settle, saves the conversation at a turn boundary, and then ends the process. The session stays listed and stays resumable.
- **Restart agent** does that and reconnects, so the session comes back on whichever agent build is installed *now*. That's how you pick up an agent you just updated without losing the conversation. A restart also re-reads your login shell, so an environment variable you added, changed, or removed in your shell's startup files reaches the restarted agent without restarting Kepler.

Restart shows its progress rather than going blank. A session you shut down before its first prompt stays listed as dormant rather than disappearing.

### Dormant and archived sessions

A **dormant** session (one restored from disk, or stopped before it ever ran) shows its transcript, with the session's title leading its context card. It doesn't spawn an agent until you send the first message, so restoring a pile of old sessions costs nothing.

An **archived** session can be read without being restored: it opens read-only, labelled *Read-only. Restore it to keep working.*, with **Restore this session and open it live** and **Permanently delete this saved session** beside it.

Some agents can store one conversation more than once. A session with more than one saved copy resumes the newest one it can run without asking. To pick another, choose **Use another copy…** on the session's menu: *Kepler found more than one saved copy of this conversation. Pick the one to continue when you resume it.* Each copy lists when it was updated and how many messages it holds.

### Pointing an agent at another session

**Copy session link**, on a session's row or tab menu (or **Cmd/Ctrl+C** on a focused row), copies a Kepler link to the session, such as `kepler://session/<id>`. **Copy task link** on a task's menu does the same for a task. Paste the link into a prompt and the agent can read that conversation through the workspace tools. That's useful for "read what the other agent concluded and carry on". See [Tasks and Resources](/kepler/tasks-and-resources).

An agent that can't use Kepler's workspace tools gets a copy instead. Kepler attaches a Markdown snapshot of each task or session linked in the prompt, up to five per prompt, and the same happens to a link you paste into such an agent's terminal. A snapshot is a copy taken when you send, not a live view.

Archived sessions collect under a **{count} archived** fold beneath the live ones in the task rail. On the Dashboard, the session strip's **Archived sessions** button searches them (*Find an archived session…*). Restoring puts the session back in the list; it reconnects when you open it.

Deleting a task or removing its repository ends that task's live sessions.

### Keeping agents running through a restart

**Settings → General → Keep agents running → Keep agents and terminals running across restarts and updates** is on by default, though the setting still marks it experimental: *Agent sessions and terminals stay alive while Kepler restarts or updates, and reconnect afterwards. Experimental.* New sessions pick up a change to it. A build that can't keep agents running shows the switch off and greyed out.

<!-- TODO(screenshot): New: A session showing the *Reconnecting to the agent…* overlay after Kepler restarts. -->

| | Switch on (the default) | Switch off |
|---|---|---|
| **Quit** | Agent sessions keep running, and Kepler reattaches to them when it comes back. Shell tabs end, as they do when you quit any terminal app | Asks first when sessions are running, and warns that each one will stop. Busy *terminals* are counted too |
| **Updating Kepler** | Warns only about agents the update would actually interrupt. Shell tabs keep running and come back after the restart | Warns how many agent sessions the restart will stop |
| **Quit & End Sessions** | In the app and tray menus, including when only shell tabs are open. Ends the sessions on the way out; asks first only if one is mid-turn (**End Sessions and Quit**). Each can be continued again from its task | Not applicable |

While Kepler reattaches, an overlay covers the session, and the session offers no actions until it's back. The overlay reads *Reconnecting to the agent…*, then *Restoring conversation history…*. If the reattach fails, the session falls back to its saved conversation: *Unable to reconnect to the agent. Resume to pick up from the saved conversation.* A session whose background process dies keeps its conversation the same way, rather than starting a new one.

A session left running after a quit, with Kepler never coming back to it, is ended on its own after an hour without any output from the agent. An agent still mid-task keeps producing output, so it finishes first.

A terminal session kept running this way also keeps its keyboard and paste modes across the restart, and a reboot that ends it still leaves it resumable.

A session kept running this way can stop taking output if it reaches a storage or log limit. It then shows **Agent output paused**: *Kepler stopped accepting agent output after reaching a storage or log limit. Your draft is preserved while output is paused.*

Your computer will not go to sleep out from under a running agent. While any session is spawning, running, or waiting on you, Kepler holds the machine awake, and lets go as soon as the last one settles. It is on out of the box and turned off in **Settings → General → Keep agents running → Keep this machine awake while agents work**. See [Settings](/kepler/settings-app#keep-agents-running).

***

## When a session drops

A session that can't carry on says so on its context card, with a badge, one sentence, and only the recovery that applies.

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

A card that has more to say carries **Details**, which opens the **Diagnostics** behind it with **Copy**, for a bug report.

An **Agent error** banner names the cause: *{name} binary is missing or not executable.*, *Agent authentication failed.*, *Agent process exited on its own.* It offers **Reconnect**, **Authenticate**, **Compact**, or **Dismiss** as the cause warrants. A usage limit reads **{login} reached its usage limit**, or **{adapter} reached its session limit**, with *Available again at {time}.* See [When you hit a usage limit](#when-you-hit-a-usage-limit). A Codex turn the provider couldn't serve reads **Codex was unable to complete this turn**: *OpenAI reported a capacity problem, not a usage limit. Reconnect to this conversation, then retry in a moment or switch models.*

A Chat turn that fails on the provider's side says which kind of failure it hit and what to do:

- *{name} hit a rate limit. Wait a moment, then send your message again.*
- *{name} is out of quota or has a billing problem. Check your plan or billing, then try again.*
- *{name} is overloaded right now. Try again shortly.*

While the agent retries a failed turn by itself, the session shows **Retrying** with the reason, such as *{name} hit a rate limit and is retrying.*, the attempt (*Attempt {attempt}.*), and *Next try at {time}.*

In Terminal mode a dead process reads **Terminal exited. Resume to reattach to this conversation.**

If a session fails to start after you launch it, the task page and the Dashboard panel show **{agent} was unable to start** with the agent's message. Click **Retry** to try again, or **Open agent settings** to fix the agent's setup. **Dismiss** hides the notice in that window.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-task-start-failed-notice-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-task-start-failed-notice-01-v3@2x.png" class="help-center-img img-bordered" alt="The top of the task page for Fix the cart total with the OpenCode was unable to start notice: the message Session not initialized, Retry, Open agent settings, and a close button that dismisses it.">
  </a>
  <figcaption style="text-align:center; color:#888">A session that couldn't start, on the task page.</figcaption>
</figure>

Sessions recover on their own where they can: Kepler renews an authentication token that expires mid-session so the session continues, and remote connections re-establish after a restart or sleep.

***

## Notifications

Kepler tells you when a session replies, needs you, or fails. Each notification uses one of the following statuses:

| Status | When |
|---|---|
| **Replied** | An agent finished replying and it's your turn |
| **Asked a question** | The agent asks you something and waits for your answer |
| **Needs permission** | The agent wants permission to do something |
| **Approval needed** | An agent asks Kepler to do something only you can approve, like deleting a worktree. A destructive request reads **Approval needed for a destructive action** |
| **Error** | The session stopped because something went wrong |

A Terminal or external session blocked on a prompt in its own CLI notifies you too, for every agent. Sessions started outside Kepler notify only once they're on a task.

Titles read **{status}: {task}**, with the agent and the repository or branch beneath (*{adapter} on {repo}/{branch}*), and clicking one takes you to the session. Kepler shows it in the window already showing that session or its task, or else in the window you used last. An approval notification is titled with its status alone, with the action and *Asked by {session}* beneath.

By default, Kepler stays quiet about the work you are already watching: it sends no notification for the task open in the window you're using. To change that, turn on **Notify even for the task you're looking at**. While you're working in any Kepler window on a computer, that computer posts no desktop notifications; the window you're in shows them in Kepler instead, and several windows on one computer post a single alert. A cancelled turn is not a completion, and a session reconnecting is not a completion either, so neither notifies.

To choose which events notify you, and whether each one appears as a **Desktop** notification, **In Kepler**, or both, open **Settings → Notifications**. The same page has **Play a sound with desktop notifications**. In the desktop app, every event except **Replies** notifies on the desktop until you change it; in a browser, desktop notifications start off. After your first session starts, the desktop app sends a one-time **Notifications are on** notification, and clicking it opens **Settings → Notifications**. See [Settings](/kepler/settings-app#notifications).

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-settings-notifications-01-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-settings-notifications-01-01-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Notifications, What to notify you about, at the desktop app's defaults: a grid of Replies, Questions, Permission requests, Approval requests and Errors against Desktop and In Kepler, with every box ticked except both Replies boxes; below it Play a sound with desktop notifications is ticked and Notify even for the task you're looking at is not.">
  </a>
  <figcaption style="text-align:center; color:#888">What to notify you about, in Settings → Notifications, at the desktop app's defaults.</figcaption>
</figure>

### Notifications from terminal programs

A plain terminal can notify you too. When the program in a terminal blocks on you, or finishes or fails after working, Kepler sends a notification that names the terminal and its task, for example:

- *Approve it in {terminal}*
- *Answer it in {terminal}*
- *Sign in from {terminal}*
- *Finished in {terminal}*
- *Failed in {terminal}*

Click **View** to open that terminal. Terminal notifications follow the same **Settings → Notifications** choices as agent sessions, and Kepler stays quiet only while that terminal is on screen in the focused window.

In-app toasts carry a close button on hover, and **Clear all ({count})** dismisses the lot.

***

## Reviewing what the agent changed

Reading the diff and syncing the branch are covered on their own page. See [Review Changes](/kepler/review-changes).

---
