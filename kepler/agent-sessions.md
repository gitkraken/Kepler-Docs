---
title: Agent Sessions
description: An agent session is one conversation with a coding agent in a task. Start one, pick the agent and model, send and steer prompts, and manage its lifecycle.
product: Kepler
feature: Agent Sessions
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode, grok, pi, antigravity]
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [agent-sessions, sessions, prompts, steering, queueing, models, modes, dictation, read-aloud, session-recovery]
taxonomy:
  category: kepler
custom_fields:
    entry_title: "Direct an agent mid-session"
    entry_role: "Direct"
    entry_desc: "Start a session, pick the agent and model, and send and steer prompts"
    entry_order: 20
    nav_category: "kepler-working-in-kepler"
    nav_label: "Agent Sessions"
    anchor_map:
        - "several-accounts-for-one-agent|kepler-agent-accounts#several-accounts-for-one-agent"
        - "choosing-an-account-for-a-session|kepler-agent-accounts#choosing-an-account-for-a-session"
        - "moving-a-session-to-another-account|kepler-agent-accounts#moving-a-session-to-another-account"
        - "signing-in-through-your-browser|kepler-agent-accounts#signing-in-through-your-browser"
        - "sessions-started-outside-kepler|kepler-external-sessions"
        - "turning-detection-on|kepler-external-sessions#turning-detection-on"
        - "reading-one|kepler-external-sessions#reading-one"
        - "taking-one-over|kepler-external-sessions#taking-one-over"
        - "when-the-agent-asks-you-something|kepler-agent-requests"
        - "permission-requests|kepler-agent-requests#permission-requests"
        - "requests-that-arrive-through-hooks|kepler-agent-requests#requests-that-arrive-through-hooks"
        - "multiple-choice-and-multi-select-questions|kepler-agent-requests#multiple-choice-and-multi-select-questions"
        - "reviewing-a-plan|kepler-agent-requests#reviewing-a-plan"
        - "approval-requests|kepler-agent-requests#approval-requests"
        - "reports-from-other-agents|kepler-agent-requests#reports-from-other-agents"
        - "usage-indicators|kepler-agent-accounts#usage-indicators"
        - "when-you-hit-a-usage-limit|kepler-agent-accounts#when-you-hit-a-usage-limit"
        - "notifications|kepler-agent-requests#notifications"
        - "notifications-from-terminal-programs|kepler-agent-requests#notifications-from-terminal-programs"
    nav_order: 20
    nav_parent: "kepler-working-in-kepler"
    page_type: "content"
    card_icon: "message-chatbot"
    card_color: "blue"
    card_description: "Start, direct and manage a running conversation with a coding agent"
---
<kbd>Last updated: November 2026</kbd>

An **agent session** is one running conversation with a coding agent, anchored to one working directory. Learn how to start a session, direct it with prompts, answer its questions, and manage it from start to archive.

A task can hold several sessions. For example, 2 agents can share one worktree, each agent can have its own worktree, or a session can run in the task folder itself. A task lists all of its sessions under its **Sessions** group. See [The Task View](/kepler/task-view).

Sessions vary in 2 ways:

| Property | Values | Details |
|---|---|---|
| **How it runs** | **Chat** or **Terminal** | [How a session runs](#how-a-session-runs) |
| **Where it started** | In Kepler, or outside Kepler and found by it | [Sessions started outside Kepler](/kepler/kepler-external-sessions) |

Prompts, steering, permissions, status, and the session lifecycle work the same way for every session.

Answering the agent's requests and notifications, accounts and usage, and sessions started outside Kepler each have their own page: [Answering Your Agent](/kepler/kepler-agent-requests), [Agent Accounts and Usage](/kepler/kepler-agent-accounts), and [Sessions Started Outside Kepler](/kepler/kepler-external-sessions).

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

A session receives the task's shared context by default. To start a session that forms its own view of the work, untick the **Task context** chip in the draft composer's footer, beside **Attach a file** and the microphone. The task context is the task's prompt and notes, and later changes to it reach the agent with your next message.

Right-click a draft tab or its row in the context panel for these actions:

- **Discard draft**: removes the draft. If the draft holds text or attachments, Kepler asks first: **Discard new session?**
- **Move left** or **Move right**: moves the draft among the other tabs.

If **Show tabs on the task page** is on, the draft has a regular tab menu instead: **Pin tab** or **Unpin tab**, **Keep open** while the tab is a preview, and **Close tab**, the only way to close it. See [Task View](/kepler/task-view#tabs-and-groups).

### Branching and renaming a session

**New session from this one** starts a sibling session in the same task, worktree, agent, and account. The new agent can read the source conversation.

**New session from here** does the same, but the new agent reads the source only up to and including the message you picked. The command is available once that message has finished streaming, and not on a terminal or external session.

To go back to the original, choose **Open source session** on the new session's menu.

To give a session your own name, choose **Rename session** on its row menu. Agents can also name and rename the Chat sessions they start, through Kepler's workspace tools.

***

## Agent, model, mode, and effort

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-settings-from-composer-oct-2026-v5@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-settings-from-composer-oct-2026-v5@2x.png" class="help-center-img img-bordered" alt="Agent settings open above a new session's composer: Agent OpenCode, Preset No preset, Start in with Chat selected beside Terminal, Model Docs Model, Permission mode Build or Plan, MCP servers (No servers) with Manage, and the agent settings gear with Save preset. Below it, the composer footer holds Attach a file, the microphone and a ticked Task context chip, then the Docs Model Build pill and Start.">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent settings pill, opened from the composer, with the Task context chip in the footer.</figcaption>
</figure>

To choose the agent, model, mode, and effort, use the **Agent settings** pill on the composer, when you start a session or while it runs.

An **agent preset** is a saved set of one agent's model, mode, effort, and options. To save the current settings as a preset, click **Save preset** at the bottom of the menu. To create or edit presets, click **Manage presets** in the **Preset** list. See [Settings](/kepler/settings-agents#agent-presets).

| Choice | Changeable mid-session | Notes |
|---|---|---|
| **Agent** | No | Fixed once the session exists. To use another agent, start a new session |
| **Preset** | Yes | **No preset**, or one of this agent's presets, once it has any. A preset you change reads **{name} (unsaved)** |
| **Start in** | No | **Chat** or **Terminal**, for an agent that offers both. To use the other mode, start a new session; see [How a session runs](#how-a-session-runs) |
| **Model** | Yes | Models are per provider, so each agent has its own catalog and a model never moves to another agent. At the default, the row reads **Default · {model}**, naming the model the default resolves to |
| **Mode** | Yes | The agent's own permission modes |
| **Effort** | Yes | Reasoning or thinking depth, for agents that offer it |
| **Options** | Some | The agent's on/off options, such as **Artifacts**, ticked in one menu |
| Startup options | No | Set when you launch the session. A Terminal launch offers the CLI's own options; see [How a session runs](#how-a-session-runs) |

A change applies from your next message. It never interrupts the turn in progress.

The menu also shows its state:

- An option row reads **Agent default** until you pick a value.
- **{name} settings changed** appears when a session's preset was edited after the session started. Click **Apply** to use the new settings.

If a session's model changes, for example because the default now resolves to a different model, the conversation shows *Model changed from {from} to {to}.*

The model and mode lists update on their own, so a newly released model appears without restarting Kepler.

The same menu lists the MCP servers the agent loads for this repository. To change them, click **Manage**. See [MCP Servers](/kepler/mcp-servers).

When the menu cannot offer the usual choices, it shows one of these messages:

| The menu reads | When |
|---|---|
| **Loading your last agent choice…** | Kepler is restoring the agent you used last |
| **Set up a coding agent** | No agent is set up. See below |
| **Sign in to {agent} to start a session** | The chosen agent is installed but signed out |
| **{agent} didn't share its options** | Kepler could not read the agent's models and modes. You can still start a session on the agent's own model and mode, or click **Retry** |

To set one up from **Set up a coding agent**, click **Install or locate {name}** for an agent. If you installed an agent yourself, click **Rescan**. If your agents are on another machine, click **Choose** to open **Settings → Remote environments**.

If you have more than one account, the **Agent** list groups accounts under their agent. The list ends with **Add another account** and **Install another agent**.

By default, a new task, the Dashboard composer, and a new draft tab start with the agent, model, and mode you last picked. To always start with one agent instead, open **Settings → Tasks → New tasks**, pick the agent and its settings in **New sessions start with**, and clear **Start each session on the agent you used last**. To start one session with other settings, change them in the draft's **Agent settings**. See [Settings](/kepler/settings-tasks#default-agent).

### Which agents are available

Kepler supports Claude Code, Codex, GitHub Copilot, Cursor, Auggie, OpenCode, Grok Build, Pi, and Google Antigravity, plus any custom agent you add. Kepler offers only the agents you have installed. See [Agent Integrations](/kepler/agent-integrations).

***

## How a session runs

A session runs in one of 2 modes. Most agents offer both; see the table of agents below.

| Mode | What it is |
|---|---|
| **Chat** (the default) | Kepler shows the conversation itself, with replies, diffs, and plans you can read, review, and search |
| **Terminal** | The agent's own command-line app, with its commands, shortcuts, and settings, in a terminal inside the task |

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
| Google Antigravity | Terminal by default. Chat needs Antigravity CLI 1.5.0 or newer |
| Pi | Terminal only |
| Your own agent server | Whichever its command supports |

Kepler hides any control the agent's CLI does not support.

A Terminal launch offers these options for each CLI:

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
| Google Antigravity | Model, mode, and effort, with Antigravity CLI 1.5.3 or newer |

If the installed version supports it, GitHub Copilot, Cursor, OpenCode, Pi, Grok Build, and Google Antigravity receive your first message as they start.

### What's different in Terminal

Terminal mode is a full session. Kepler adds what a bare terminal cannot give the running CLI:

- The task's shared context.
- Kepler's workspace tools, where the CLI can load them.
- Permission prompts that you answer in Kepler.
- A transcript that survives a restart.

A Terminal session's pane has 3 parts:

| Part | What it does |
|---|---|
| The terminal | The agent's real interface, keys and all |
| The status bar | The session at a glance, then your plan usage. See below |
| The composer | Kepler's own message box, with attachments, dictation, and the agent-settings pill |

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
| Branch | The session's branch, with a folder mark when the CLI works in a subfolder or outside the worktree |
| Plan usage | 2 bars for the **5h** and **7d** windows, colored by pace. Hover for the full readout; see [Usage indicators](/kepler/kepler-agent-accounts#usage-indicators) |
| **Rich input** | Shows or hides Kepler's message composer. Hide it to type straight into the CLI |
| **Read last reply** | Reads the agent's last reply aloud. See [Read aloud](/kepler/voice-input#read-aloud) |
| **No Kepler tools** | Shown when the agent cannot use Kepler's workspace tools or inbox in a terminal. Its tip points to **Continue in Chat** on the session menu |
| **Idle detection** | Shown for an agent that does not report its status to Kepler. Kepler judges activity from the terminal going quiet, so a long pause mid-turn can read as idle |
| Program status | Shown in place of **Idle detection** when the program in the terminal reports its own status. See below |

For an agent that cannot tell Kepler it is waiting on you, check the terminal when it goes quiet; the status dot's tip says so.

Hover any part to see its card, and click to pin the card open.

Hover an idle session's status to see its **Last reply** and **Last prompt**. When the prompt cache is about to expire or has expired, the card also shows **Prompt cache**. Once the cache expires, an idle session's next prompt can re-read its whole context without telling you.

Some terminal programs report their own status to Kepler. When a program does, the status bar names that status, such as **Running**, **Needs your approval**, **Done**, or **Failed**, and the session reads as working, waiting on you, or done to match. Hover the status to see any message, progress, and sub-tasks the program sends.

A Terminal session tracked through hooks reports a failed turn too. When a Claude Code, GitHub Copilot, or OpenCode turn fails, for example on a usage limit, a rate limit, or a server error, the session shows **Error** with the CLI's own message once the turn stops.

In a Terminal session, the composer's **Agent settings** pill shows the model, effort, and mode the session uses, but you cannot change them there. Change them in the CLI itself. An effort or mode you change in the CLI survives a relaunch of the session.

Terminal sessions also differ in these ways:

- **Queued review comments wait in a bar** when the composer is hidden. Click **Add a message** to open the composer with the comments attached, or **Send comments** to send them on their own once the terminal is running.
- **A pasted image reaches the agent as an image.** When you paste an image into a Claude Code or Codex terminal, the agent reads it as an image, not as a path it has to open.
- **A terminal session's conversation is recorded**, so quitting Kepler, an idle shutdown, a restart, or a reboot does not lose it. Reopening reattaches to the same conversation with its scrollback intact.
- **A first message that Kepler cannot safely type at launch** waits in the composer as a ready-to-send draft. Send it once the terminal is ready.
- **Lost keystrokes are never resent.** If Kepler cannot tell whether your last keystrokes reached the terminal, it warns *Your last keystrokes may not have arrived*. Check what the terminal shows before you go on.
- **A terminal reattaches instead of restarting.** During a reconnect, the last screen stays readable. If the terminal cannot reconnect, click **Retry** under **Unable to restore this terminal**.
- **One view types at a time.** A terminal that another window or a Remote Access device is driving reads **Another view is controlling this terminal**. Click **Take control** to type here.

> **Note:** **A terminal session is not the same as a terminal.** A terminal session runs an *agent*, lives in the **Sessions** column, and carries the task's context. A plain terminal runs your shell, lives in the drawer beneath the columns, and carries none. See [The Task View](/kepler/task-view#the-terminal-drawer).

***

## Sending a prompt

To send a prompt, type it in the composer at the bottom of the session.

<figure style="text-align:center">
  <a href="/wp-content/uploads/sending-a-prompt-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/sending-a-prompt-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The session composer with a pasted image.png attached as a thumbnail chip with its remove button, and a draft holding the file chips cart.js and README.md, each with its file icon, then Does the check also cover these codes? Below the draft sit Attach a file and the crossed-out microphone, then the Agent settings pill (Docs Model, Build, with its chevron), the context usage ring, and Send with its chevron.">
  </a>
  <figcaption style="text-align:center; color:#888">The composer, at the bottom of the session.</figcaption>
</figure>

The composer has these controls:

| Control | What it does |
|---|---|
| **Attach a file** | Attaches a file for the agent to read; you can also drag files onto the composer (*Drop files to attach*). On a remote connection, **Add a file from the remote** picks a file from the remote machine |
| **Dictate** | The microphone: speak, and Kepler types what you say. See [Dictation](#dictation) |
| **Agent settings** | Agent, model, permission mode, effort, and options |
| Context usage | The share of the session's context window in use, drawn as a ring. Hover to see tokens used, available, and total, the estimated cost at API rates, and the prompt cache |
| Plan usage | Your provider plan's usage windows and when each resets. See [Usage indicators](/kepler/kepler-agent-accounts#usage-indicators) |
| **Send** | Sends the prompt, and shows a sending state from the moment you click. The chevron holds **Send** and every applicable Action |

**Attaching a file sends a path, not a copy, wherever it can.** If the session's machine can already read the file, including a Windows file in a window connected to a WSL distro on the same computer, Kepler sends its path. Kepler copies any other file into the task when you send, up to 200 MB. A message can carry at most 20 attachments, and Kepler tells you if it left a file out.

If an upload fails, or the message is too large for the agent, Kepler does not send the message. Where the window can reach the file's machine, an attached file's card on the task page offers **Open in default app** and one of **Show in Finder** (macOS), **Show in Explorer** (Windows), or **Show in file manager** (Linux).

**A long paste becomes an attachment.** If you paste more than 32 KB of text, such as a long log, Kepler attaches it as a text file, such as `pasted-text-800-lines.txt`, and puts the file name in your prompt. To drop the attachment, remove the chip. This works in every composer that takes attachments.

<figure style="text-align:center">
  <a href="/wp-content/uploads/pasted-text-attachment-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/pasted-text-attachment-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task session's composer after pasting a long test log: the text became an attachment chip, pasted-text-800-lines.txt with a remove button, above the prompt Why does the cart test fail in this log? pasted-text-800-lines.txt, with the attach and microphone buttons, the Docs Model Build pill and Send.">
  </a>
  <figcaption style="text-align:center; color:#888">A long paste, attached as a text file.</figcaption>
</figure>

**A pasted pull request or issue link becomes a chip.** Paste the URL of a pull request or issue from a connected GitHub, GitLab, Bitbucket, or Azure DevOps host, self-hosted included, or of a Jira or Linear issue. In a task's session composer or the **New task** composer, Kepler turns the URL into a chip labeled with its number, such as **#49**, and puts the label in your text in its place. Hover the chip to see the title and the URL. When you send, Kepler attaches the link to the task.

<figure style="text-align:center">
  <a href="/wp-content/uploads/pasted-link-chip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/pasted-link-chip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task session's composer after pasting a pull request link: a chip with the pull request icon and #49 sits above the prompt Does this conflict with #49?, and its tooltip shows the pull request's title, Round prices through a shared roundCents helper, over its GitHub URL.">
  </a>
  <figcaption style="text-align:center; color:#888">A pasted pull request link, turned into a chip.</figcaption>
</figure>

**Review comments wait in a chip until you send.** Comments you queue for a session while you review its changes collect in one chip on its composer, such as **2 comments**. Click the chip to list them by file and line. Click a comment to open its place in the file, or click its **X** to remove it from the queue. The chip's own **X** removes all of them. Your next message sends the queued comments first, ahead of what you typed. You can also send them with an empty prompt. See [Review Changes](/kepler/review-changes).

<figure style="text-align:center">
  <a href="/wp-content/uploads/queued-comments-chip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/queued-comments-chip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A session composer with the 2 comments chip open above it: the Queued comments list holds cart.js:3 over Clamp at zero so a discount larger than t… and cart.js:4 over Pull 100 into a CENTS constant; the sam…, each with an X to remove it from the queue. The chip has its own X to remove all comments from the queue; below it sit Type a message..., Attach, the microphone, the Docs Model and Build agent settings, and Send.">
  </a>
  <figcaption style="text-align:center; color:#888">Two review comments queued for the next message.</figcaption>
</figure>

**Replies to your review comments show on the session.** When the agent replies to a comment you left in Changes, its composer shows a chip such as **1 new reply**, and the session's tab shows the count. Click the chip to list the replies under **Replies**. Click a reply to open its comment in Changes, or click **Mark all read**. In a Terminal session with the composer hidden, the chip sits in the bar under the terminal. The reply itself also appears in the conversation; see [Reading the conversation](#reading-the-conversation).

<figure style="text-align:center">
  <a href="/wp-content/uploads/unread-replies-chip-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/unread-replies-chip-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="A session composer with its 1 new reply chip open: the Replies popover, with Mark all read, lists cart.js:3 over the start of the agent's reply, Agreed. I'll clamp it with Math.max(0, subtotal -. The popover covers the message box; Docs Model, Build and Send sit to its right.">
  </a>
  <figcaption style="text-align:center; color:#888">An unread reply to a review comment, listed from the composer.</figcaption>
</figure>

A draft you have not sent survives a reload.

The composer works with these keys:

- **Enter** sends; **Shift+Enter** inserts a newline. To send with **Cmd/Ctrl+Enter** instead, and have **Enter** start a new line, change **Send messages with** in **Settings → General → Chat**.
- **Tab** moves focus from the prompt to **Send**, then to its chevron.
- **Down Arrow** or **Alt+Down** on **Send** opens the chevron's menu. Closing the menu returns focus to **Send**.
- **Cmd/Ctrl+F** opens **Find in conversation**.
- To type a prompt, start typing anywhere in the session. The composer takes the keystroke, so you do not have to click into it first.

For agents with long option lists, the **Agent settings** menus have a **Search options…** box.

While a turn is running, the send button adds a stop segment: *Interrupt current work. Queued messages will be sent next.* **Send** stays available the whole time, because a message sent to a busy session steers it.

### Slash commands and skills, per repository

Type `/` to open the command menu. It lists the agent's built-in commands together with your commands and skills. A slash command sent as a session's first prompt runs as a real command, not as text.

In a Claude Code **Chat** session, `/design` and `/slides` work as they do in the CLI, and Claude can publish artifacts once **Artifacts** is on for the session. See [Claude artifacts](#claude-artifacts).

In a Codex session, `$` opens a menu of skills only. `/` also finds Codex skills by name.

**Kepler finds skills and slash commands per repository, not per agent.** The catalog combines your home-directory skills and the repository or worktree's own. For Claude Code, that is `~/.claude/skills` plus `.claude/skills`. As a result:

- One project's skills never show up in another project's menu.
- A skill added in a worktree and not yet committed can appear in that session before it appears elsewhere.

A skill you add mid-session shows up without a restart.

### Mentioning files

Type `@` to search the working directory and insert a path. A path you pick from the menu shows as a chip with the file's icon and name; hover it to see the full path. A session that runs in the task folder also lists the task's other worktrees and folders, under **Worktrees and folders** above **Files**. To search inside one, pick it, or type its name and `/`. `@` also works in composers that do not belong to a session yet, where it searches the task's folders or the folder you chose. Kepler automatically approves files you paste into a chat for the agent to read.

***

## Steering a running turn

You do not have to wait for a turn to end. **If you send a message while the agent is working, the message steers the agent** instead of waiting until the turn is over.

When you send during a turn, the message goes into a queue, and a banner above the composer counts what is waiting. Kepler sends the queue as **one merged follow-up prompt** as soon as the agent can take it: right away, after the tool call that is running, or at the end of the turn for an agent that does not support steering. 2 quick corrections arrive as a single instruction instead of 2 competing ones.

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
| *Sending at {time}, when the quota resets.* | The account hit a usage limit, so the queue waits for the reset instead of sending into the limit. See [Usage indicators](/kepler/kepler-agent-accounts#usage-indicators) |
| **Send now** | Sends a queue held for a usage limit right away |
| **×** on a row | Removes that one prompt |
| **Clear queue** | Removes all of them |
| **Send queue** | Sends a queue left waiting on a session that is no longer working |
| **Not sent — too large ({size} of {limit})** | The queued messages are too large for the agent |
| **Not sent — the agent was unavailable** | The agent could not take the queued messages |
| **Back to composer** | Puts messages that were not sent back in the composer, so you can edit and resend them |
| **Interrupt & send** | Stops the current turn and delivers the queue immediately, in one step. **Cmd/Ctrl+Shift+Enter** does the same from the keyboard |

With subagents running, **Interrupt & send** names them: **Interrupt & send ({count} running)**. If the stop gets no answer, the button becomes **Force quit (drops {count} queued)**, which ends the agent and drops the queued prompts instead of sending them.

Queued prompts survive an interruption, a restart of Kepler, a disconnect, and a sign-in that expires. Kepler sends them to the reconnected session in the same order. Canceling a turn sends the next queued prompt instead of discarding it.

Each queued prompt picks up the task's shared context as it stands when the prompt runs, not as it stood when you typed it.

If a send fails, Kepler puts the text back in the composer so you can try again.

### Stopping a turn

| What you do | What happens |
|---|---|
| **Escape** | Stops the running turn |
| The stop segment on the send button | Stops the running turn. Its tooltip says what happens to the queue |
| **Cmd/Ctrl+Shift+Enter** | **Interrupt & send**: stops the turn *and* delivers what you typed |
| **Force quit the agent** | Offered once a cancel has been pending too long. It does not wait for the agent to settle |

In **Terminal** mode, Kepler recognizes an interrupt whether it arrives as **Escape** or as **Ctrl+C**, and the session shows as stopped once the CLI has stopped.

***

## Reading the conversation

A session's conversation shows your prompts, the agent's replies, and the agent's work:

- Your messages appear as chat bubbles. Right-click one to **Copy message**, **Quote**, **Ask**, or **New session from here**.
- Agent replies render as Markdown and stream as one continuous message, even when a tool runs mid-reply. Right-click a reply to act on its whole turn. While the menu is open, a band outlines the turn, and **Copy message** copies all of the main agent's text in that turn. Every message menu starts with the message's exact time.
- Each prompt, and the reply that closes each turn, has a copy button beneath it.
- A reply has a **Read aloud** button beneath it. To read on through the replies that follow, right-click a message, in the chat or in a terminal, and choose **Read aloud from here**. To stop, click **Stop reading** in the top bar. See [Read aloud](/kepler/voice-input#read-aloud).
- When the agent replies to one of your review comments, the reply shows as a card with your comment beneath **Replied on** and the file and line. Click **Open in Changes** to go to the comment.
- Your latest prompt and the latest reply show how long ago they were sent. Every earlier finished reply shows the time it was sent. A divider marks a long gap between messages.
- An agent's thinking shows as a collapsed **Thinking** block, for agents that send it.
- A file path an agent writes (a link, an inline-code path, or the file in a read or edit tool call) becomes a link once Kepler confirms the file exists. Click it, or **Cmd/Ctrl+click** it, to open the file in Kepler at the named line. A file inside a worktree opens in the Changes overlay's file view. **Cmd/Ctrl+Shift+click** opens the file in your default editor at that line.
- A Kepler task or session link in the conversation opens inside Kepler when you click or middle-click it. Hover it to see where it goes. Right-click it for **Open in Kepler** and **Copy link**.
- Images in replies and tool output open in a lightbox. You can save the image from the thumbnail or the lightbox with **Save as…**.
- Tool calls collapse into groups: **{count} tool uses**, with **{count} done**, **{count} running**, and **{count} failed** tallies. Expand a group to read any call's output.
- A plan renders as **Plan {completed}/{total}**. A plan cut short by a stop is marked **Interrupted**.
- A context compaction shows as its own row: **Compacting the conversation…**, then **Conversation compacted**, **Unable to compact the conversation** with the error, or **Compaction stopped**. When the agent kept a summary of the conversation so far, the row expands to show it, and **Find in conversation** searches it.
- Each subagent has its own card, collapsed by default, with **Prompt**, **Operations**, and **Result** sections that fold independently. The card's header row shows the subagent type, the description it was given, how many operations it has run, the step a running subagent is on, and a status of **Running**, **Stopped**, **Completed**, or **Failed**. You can follow progress without expanding the card. Claude Code, GitHub Copilot, Cursor, and OpenCode Chat sessions all produce these cards.
- A session that another session started shows **Started by** and the starting session in its header. Click it to open that session.
- A prompt that another session sent has a **From:** header naming the sending session. Click it to open that session.
- A turn that ended for a notable reason has a pill: **Reached token limit**, **Reached request limit**, **Refused to continue**, or **Cancelled**. A turn that ended normally shows no pill.

<figure style="text-align:center">
  <a href="/wp-content/uploads/compaction-row-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/compaction-row-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A Chat transcript in which, after the Read checkout.js call and the agent's note, a Conversation compacted row is open on the summary the agent kept of the conversation so far, followed by Edit checkout.js and the agent's next message.">
  </a>
  <figcaption style="text-align:center; color:#888">A compaction row, expanded to the summary the agent kept.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/review-reply-card-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/review-reply-card-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="A reply card in the agent's conversation: Replied on cart.js:3 with a New badge and Open in Changes, then You: Clamp the discounted subtotal at zero so a large discount cannot make the total negative, and the agent's reply, Agreed. I'll clamp it with Math.max(0, subtotal - discount) and add a test for a discount larger than the order.">
  </a>
  <figcaption style="text-align:center; color:#888">The agent's reply to a review comment, in its conversation.</figcaption>
</figure>

**Quote a passage to ask about it.** Select text in a message, right-click it, and choose **Quote**. The passage goes into the composer as a quote block, and Kepler tints its source in the conversation. Click the quote block to scroll to its source, or click the tinted passage to go back to the quote. In a sent message, a long quote folds, with **Show more** and **Show less**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/composer-quote-block-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/composer-quote-block-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="A session on Fix the cart total: the agent's sentence, The total applied the discount after tax, so discounted orders were overcharged by the tax on the discount, is tinted in the conversation, and the composer below holds the same sentence as a quote block, with the question Does the same apply to gift cards? typed under it.">
  </a>
  <figcaption style="text-align:center; color:#888">A quote in the composer, with its source tinted in the conversation.</figcaption>
</figure>

**A long conversation opens on its latest turns.** To read further back, click **Show earlier messages** at the top of the transcript. Each click loads the part before it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/transcript-earlier-messages-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/transcript-earlier-messages-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task's Chat session reopened on its latest turn: under the prompt strip (2/2 Unify the button label on every step.), Show earlier messages heads the transcript, above Today 2:30 PM, the prompt Unify the button label on every step., an Edit templates/checkout/step-3.html tool row and the reply Done: every step now says &quot;Place order&quot;, and &quot;basket&quot; is &quot;cart&quot; throughout., each with its copy button and time.">
  </a>
  <figcaption style="text-align:center; color:#888">A long conversation, opened on its latest turn.</figcaption>
</figure>

Until earlier messages are loaded, **Find in conversation** searches only the loaded ones. To search the whole conversation, click **Search earlier messages**.

Kepler keeps subagent work separate from the main thread:

- A subagent's own tool calls nest inside its card under **Operations**, not alongside the main agent's calls.
- A subagent's narration renders in an indented lane marked **Subagent**, so you can see where it starts and stops even when it interleaves with the main agent's text.
- A subagent can start subagents of its own. Their cards nest inside its card, and the outer card counts every permission request waiting anywhere beneath it. A request from a nested subagent shows on the outer card under a path of subagent names, such as **Parent › Child**.
- While a turn is running, that turn's subagent cards pin to the top of the session. They return to their place in the conversation when the turn ends. A card you expanded stays expanded for the rest of the turn.

To read a subagent's own transcript, click **Open subagent transcript** on its card or on its running chip above the composer. The transcript shows the subagent's prompt, then its narration and tool calls in the order they happened, then its result. The transcript updates live while the subagent runs, and the card and chip show the step in progress.

The pane's subtitle shows the current step on one line. When the step is longer, **Show full step** expands it and **Hide full step** folds it again. In a wide pane, the transcript docks beside the chat. In a narrow pane, it covers the chat, with **Back to {title}** to return. While the transcript is open, you answer a permission request raised inside the subagent in that pane.

In a Claude Code or Codex Chat session, you can also direct one subagent from its pane instead of the whole turn:

- **Message {name}**: sends the subagent a message through the main agent. The pane notes *Sent through the main agent*, or *Waiting for the main agent* while the main agent is busy. You cannot pass on a slash command. If the subagent has already finished, the pane reports *Unable to deliver the message to {name}, which may have finished*.
- **Stop**: ends that subagent alone. A Codex subagent that cannot be stopped directly offers **Ask to stop** instead, which asks the main agent to stop it.

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

To turn artifacts on for one session, open its composer's **Agent settings** and tick **Artifacts** in the **Options** menu. In a running conversation, Kepler asks first, because the session restarts and resumes the conversation: the running turn, background shells and subagents, and queued messages end. Artifacts then stay on for the conversation. You can tick **Artifacts** once the session has started.

<!-- TODO(screenshot): Replace — ade-artifacts-toggle-01: a live Claude Code Chat session's Agent settings with the Options menu open on the Artifacts checkbox and its description (needs a signed-in Claude Code). -->

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
| **Conversation width** | How wide the conversation grows in a wide pane: **Narrow** (the default), **Wide**, or **Full width** |
| **Scrolling** → **While an agent replies**: **Follow new output** | Follows the newest output until you scroll up. The default |
| **Scrolling** → **While an agent replies**: **Stay on my message** | Keeps your message in view |
| **Return to where I left off when I reopen a session** | On by default |

***

## Dictation

Every session's composer has a microphone, **Dictate**. Click it, then speak, and the transcript appears in the prompt. Transcription runs on your device. Dictation works once you download a model in **Settings → Voice**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/start-voice-input-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/start-voice-input-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="The New task composer: Add issue, Add PR and Add context above the empty prompt, then the attach button and the microphone button with its Dictate tooltip below it, and the agent pill with a warning sign and Start on the right.">
  </a>
  <figcaption style="text-align:center; color:#888">The composer's microphone, with its Dictate tooltip.</figcaption>
</figure>

When dictation cannot start, such as before you download a model, the microphone's tooltip says why and links to Settings. See [Dictation and Read Aloud](/kepler/voice-input).

***

## Session status

Each session has a status, shown as a colored dot on its tab and rows.

| Status | Meaning |
|---|---|
| **Starting** | Starting up |
| **Ready** | Connected, nothing sent yet |
| **Running** | Working on a turn |
| **Waiting** | Blocked on you, and it says on what: **Permission**, **Question**, **Plan review**, or **Prompt not sent**. A pending Kepler approval also counts, as **Approval needed** or **Approval needed, destructive**, even while the agent keeps working |
| **Unread** | Finished a turn you have not looked at |
| **Idle** | Connected, nothing running |
| **Background task running** | The turn ended, but work the agent left running on its own, such as a backgrounded shell or a monitor, is still going. Shown as idle, and it does not keep the machine awake |
| **Asleep** or **Asleep, unread reply** | An idle Chat session that Kepler put to sleep until your next message. See [Dormant and archived sessions](#dormant-and-archived-sessions) |
| **Reconnecting** | Kepler is reattaching to a session that kept running while Kepler restarted |
| **Error** | The turn or the process failed. A live session whose last turn failed on a rate limit, an exhausted quota, or an overloaded provider reads **Error** too |
| **Ended** | The agent process is not running. Kepler keeps the conversation, and a dormant session shows its last state as *{state} (ended)* until your next message starts it again |

When Kepler shows one status for several sessions, such as on a task row, the most urgent wins: **Waiting**, then **Error**, then **Unread**, then **Running**.

Rows in [the main list](/kepler/kepler-interface) show the most urgent session's state.

Task and session rows add a line that says what a session needs from you, most pressing first, such as **Approval needed for {tool}**, **Asking: {question}**, **Plan ready for review: {plan}**, or **New reply**. When several requests are waiting, the line shows the oldest first.

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

**In the Sessions column, closing a tab archives the session.** Kepler stops the agent process, saves the conversation, and removes the tab from the strip. Nothing is deleted. If **Show tabs on the task page** is on, a tab's **×** is **Close tab** instead. It only hides the tab, and the session keeps running. See [Task View](/kepler/task-view#tabs-and-groups).

### Shutting down and restarting an agent

Ending a session's agent and archiving the session are separate actions. A live session's row menu offers these:

- **Shut down agent** cancels the turn, saves the conversation, and then ends the process. The session stays listed, and you can resume it.
- **Restart agent** does the same and then reconnects, so the session comes back on the agent version installed *now*. Use it to pick up an agent you just updated without losing the conversation. A restart also re-reads your login shell. An environment variable you added, changed, or removed in your shell's startup files reaches the restarted agent without restarting Kepler.

A restart shows its progress instead of a blank session. A session you shut down before its first prompt stays listed as dormant instead of disappearing.

### Dormant and archived sessions

A **dormant** session (one restored from disk, or stopped before it ever ran) shows its transcript, with the session's title at the top of its context card. It does not start an agent until you send the first message, so restoring many old sessions costs nothing.

**An idle Chat session goes to sleep.** When no window shows a Chat session and it has been quiet for the time set in **Settings → General → Keep agents running → Put idle agents to sleep** (**After 15 minutes** by default), Kepler stops its agent to free the process. The session reads **Asleep**, and your next message wakes it with the conversation intact. A session that is working or waiting on you stays awake, and a Terminal session never sleeps. See [Settings](/kepler/settings-app#keep-agents-running).

You can read an **archived** session without restoring it. It opens read-only, with **Restore this session and open it live** and **Permanently delete this saved session** beside it.

Archived sessions are listed under a **{count} archived** fold below the live ones in the context panel. On the Dashboard, the session strip's **Archived sessions** button searches them. Restoring puts the session back in the list, and the session reconnects when you open it.

Some agents can store one conversation more than once. If a session has more than one saved copy, it resumes the newest copy it can run, without asking. To pick another copy, choose **Use another copy…** on the session's menu. Each copy lists when it was updated and how many messages it holds.

Deleting a task or removing its repository ends that task's live sessions.

### Pointing an agent at another session

To copy a Kepler link to a session, such as `kepler://session/<id>`, choose **Copy session link** on the session's row or tab menu, or press **Cmd/Ctrl+C** on a focused row. **Copy task link** on a task's menu does the same for a task. When you paste the link into a prompt, the agent can read that conversation through the workspace tools. For example, you can ask an agent to read what another agent concluded and continue from there. See [Tasks and Resources](/kepler/tasks-and-resources).

An agent that cannot use Kepler's workspace tools gets a copy instead. Kepler attaches a Markdown snapshot of each task or session linked in the prompt, up to 5 per prompt. The same happens when you paste a link into such an agent's terminal. A snapshot is a copy taken when you send, not a live view.

### Keeping agents running through a restart

**Settings → General → Keep agents running → Keep agents and terminals running across restarts and updates** is on by default, though the setting is still marked experimental. Sessions and terminals stay alive while Kepler restarts or updates, and reconnect afterwards. A change to the setting applies to new sessions. If your build cannot keep agents running, the switch is off and grayed out.

<!-- TODO(screenshot): New: A session showing the *Reconnecting to the agent…* overlay after Kepler restarts. -->

| Event | Switch on (the default) | Switch off |
|---|---|---|
| **Quit** | Agent sessions keep running, and Kepler reattaches to them when it comes back. Shell tabs end, as they do when you quit any terminal app | Asks first when sessions are running or still have live work, such as a busy subagent or a dev server left running, and warns that each one will stop. Busy *terminals* are counted too |
| **Updating Kepler** | Warns only about agents the update would interrupt. Shell tabs keep running and come back after the restart | Warns how many agent sessions the restart will stop |
| **Quit & End Sessions** | In the app and tray menus, including when only shell tabs are open. Ends the sessions as Kepler quits, asking first only if one is mid-turn or still has live work (**End Sessions and Quit**); you can continue each session again from its task | Not applicable |

While Kepler reattaches, an overlay covers the session, and the session offers no actions until it is back. If the reattach fails, click **Resume** to pick up from the saved conversation. If a session's background process stops, the session also keeps its conversation instead of starting a new one.

If Kepler never comes back to a session left running after a quit, the session ends on its own after an hour without any output from the agent. An agent still mid-task keeps producing output, so it finishes its work first.

A Terminal session kept running this way also keeps its keyboard and paste modes across the restart. If a reboot ends the session, you can still resume it.

A session kept running this way can stop accepting output if it reaches a storage or log limit. It then shows **Agent output paused**, and your draft is kept.

By default, Kepler keeps your computer awake while any session is starting, running, or waiting on you. To turn this off, clear **Settings → General → Keep agents running → Keep this machine awake while agents work**. See [Settings](/kepler/settings-app#keep-agents-running).

***

## When a session drops

If a session cannot continue, its context card says so with a badge, one sentence, and only the recovery step that applies:

| Badge | What happened | What to do |
|---|---|---|
| **Ended** | The process is gone; the conversation is not | **Resume**. In a Chat session, a message you send also continues it |
| **Exited** | *{name} exited on its own. Restart it to continue from the saved conversation.* | Restart the agent |
| **Can't resume** | *{name} no longer has this conversation, so it can't continue. You can still read it below.* | **Archive session**, or **Start new conversation** |
| **Sign-in failed** | *{name} was unable to sign in. Sign in again to continue this conversation.* | Sign in again |
| **Can't start** | *{name} isn't installed or can't run*, or *The installed {name} can't run this session.* | Fix the install or path in agent settings, then restart |
| **Folder missing** | *The folder this conversation ran in was removed or moved.* | **Recreate worktree and resume** or **Recreate folder and resume** |
| **Disconnected** | *Kepler lost its connection to this session's background process. Restart to pick up where it left off.* | Restart the agent |
| **Unable to resume** | *Another {name} is still running this conversation. Close it, then try again.* | Close the other copy, then resume |

If a card has more detail, it shows **Details**, which opens the **Diagnostics** behind it, with **Copy** for a bug report.

An **Agent error** banner names the cause, such as *{name} binary is missing or not executable.*, *Agent authentication failed.*, or *Agent process exited on its own.* Depending on the cause, the banner offers **Reconnect**, **Authenticate**, **Compact**, or **Dismiss**. A usage limit reads **{login} reached its usage limit**, or **{agent} reached its session limit**, with *Available again at {time}.* See [When you hit a usage limit](/kepler/kepler-agent-accounts#when-you-hit-a-usage-limit). A Codex turn that the provider could not serve reads **Codex was unable to complete this turn**: *OpenAI reported a capacity problem, not a usage limit. Reconnect to this conversation, then retry in a moment or switch models.*

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
  <figcaption style="text-align:center; color:#888">A session that could not start, on the task page.</figcaption>
</figure>

Sessions recover on their own where they can. If an authentication token expires mid-session, Kepler renews it so the session continues. Remote connections reconnect after a restart or sleep.

***

## Reviewing what the agent changed

To read the diff an agent produced and sync its branch, see [Review Changes](/kepler/review-changes).

---
