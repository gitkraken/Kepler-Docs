---
title: Agent Sessions
description: An agent session is one running conversation with a coding agent inside a Task. Learn how to start one, pick the agent and account, queue prompts, answer the agent's questions, and manage a session's lifecycle.
product: Kepler
feature: Agent Sessions
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode]
hosted_variant: both
status: GA
last_verified: 2026-08
llms_include: true
tags: [agent-sessions, sessions, prompts, queueing, accounts, models, modes, skills, notifications, voice-input]
taxonomy:
  category: kepler
---
<kbd>Last updated: August 2026</kbd>

An **agent session** is one running conversation with a coding agent, anchored to one working directory.

A Task can hold several. Two agents on the same worktree, one agent per worktree, a session for the task folder itself: all of it is normal, and all of it lives under the Task's **Sessions** group. For the screen those sessions open in, see [The Task View](/kepler/task-view).

This page covers the session itself: starting it, directing it, and its lifecycle. For reading the diff, staging, and committing what an agent produced, see [Review Changes](/kepler/review-changes).

<!-- TODO(screenshot): a running session in the task view's Sessions column — tab strip, transcript with a tool-call group, composer with the agent-settings pill. -->

***

## Starting a session

| From | How |
|---|---|
| A row in **Todo** | Fire an Action. See [Actions](/kepler/actions) |
| The side panel | The **Start a session** box — *Describe what to work on…* |
| The task view rail | **New session** on the **Sessions** group, or **New session here** on a worktree or folder row |
| An open session strip | **+** (*Start a new session*), or **Cmd/Ctrl+T** |

The **New session** menu lists one row per worktree and folder attached to the Task, and two rows of its own:

| Row | What it does |
|---|---|
| **Global** | Runs in the task folder rather than a repository worktree — *Runs in the task folder*. Always listed first |
| **In every worktree or folder** | One session of the chosen agent in each, with the count it will create |

With nothing attached yet, the menu reads **Attach a worktree or folder to start a session in.**

Every session sees the Task's attached resources regardless of where it runs, so what sets **Global** apart is only its working directory.

***

## Agent, model, mode, and effort

The composer carries an **Agent settings** pill. It holds the same four questions at launch and mid-session, and its trigger summarizes the current model and mode.

| Choice | Changeable mid-session | Notes |
|---|---|---|
| **Agent** | No | Fixed once the session exists. Changing agent means a new session |
| **Model** | Yes | The agent's own catalog. Models are per provider, so a model never moves to another agent |
| **Permission mode** | Yes | The agent's own modes |
| **Effort** | Yes | Reasoning or thinking depth, for agents that offer it |
| Other **Options** | Some | Options an agent can only read at spawn are editable at launch and nowhere else |

A change applies from your next message; it never interrupts the turn in flight. Rows read **Default** until you pick something, **Reset** appears once anything is overridden, and the pill reads **Checking agent options…** while Kepler probes an agent it has not seen recently.

Model and mode lists refresh in the background, so a newly released model appears without restarting Kepler.

To set what every new session starts with, use **Settings → Agents → Default agent**, which is preselected in the launcher and applied when you start a session inside a worktree. See [Settings](/kepler/settings).

### Which agents are available

Claude Code, Codex, Copilot CLI, Cursor, Auggie, and OpenCode, plus any custom server that speaks the Agent Client Protocol (ACP). Kepler offers only the agents you actually have installed. See [Agent Integrations](/kepler/agent-integrations).

***

## Several accounts for one agent

Claude Code, Codex, Copilot, and Auggie can each hold more than one signed-in account. Open **Settings → Agents**, expand the agent, and find **Accounts**:

> Run multiple Claude Code logins side by side. Each account keeps its own credentials and history but shares your skills, agents, commands and settings.

| Control | What it does |
|---|---|
| First row, badged **Default** | The agent's own login, in its normal config directory |
| **Add account** | Adds an isolated account with its own credentials and history |
| **Account name** | Rename a row in place. The name is what you pick from later |
| **Sign in** / **Sign out** | Authenticates or clears that account alone |
| **Remove account** | Signs the account out and deletes its local data. Your shared skills, agents, and settings are untouched |

### Choosing an account for a session

With two or more accounts signed in, the **Agent** list expands to one row per account, labelled with the account name, so you pick the agent and the account in one click. This is true in the task composer and in the task view's **New session** menu.

With one account, no account rows appear at all.

A running session stays on the account it started with. Session tabs name the account when more than one exists, and a tab whose account has since been removed reads **(account missing)**.

Kepler reads usage figures from the account the session is running on, not from whichever account happens to be first.

<!-- TODO(screenshot): Settings → Agents → Claude Code → Accounts with two accounts, one signed in. -->

***

## Signing in through your browser

Claude Code and Codex both sign in through a browser without dropping you into a terminal. In **Settings → Agents**, click **Sign in** and pick a method — the modal reads **Choose how you want to authenticate.**

| Connection | Claude Code | Codex |
|---|---|---|
| Local | Kepler runs the sign-in, your browser opens, and Kepler shows a status line instead of a terminal | Browser sign-in with your ChatGPT account |
| Remote or SSH | **Sign in with browser** — *Open Claude sign-in in your local browser, then paste the code it returns. Signs in the remote target directly.* | The same ChatGPT flow, with the callback bridged over SSH |

Both flows have the same shape. **Open sign-in in browser** is there if the browser did not open on its own; if the callback cannot complete, Kepler reveals **Paste the code from your browser** with **Paste from clipboard** and **Submit code**. A rejected code says so — *That code was rejected. Copy the full code and try again.*

Auggie signs in the same way locally, and on a remote target asks you to paste the JSON it returns. Copilot uses a device code: **Sign in with GitHub**, then enter a one-time code at `github.com/login/device`.

On a remote Codex target you can also **Import local Codex login** to copy your local auth cache to that target. See [Remote Environments](/kepler/remote-environments).

Kepler warns you before a login lapses: *{N} days left before your {agent} login expires. Sign in again to renew it.*

***

## Claude Code: Rich chat and Terminal

Claude Code runs two ways, chosen in **Settings → Agents → Claude Code → Default mode for new sessions**.

| Mode | What it is |
|---|---|
| **Rich chat** | *The full visual experience — plans, model and effort controls, richer input.* The default |
| **Terminal** | Runs Claude as a command-line session in an embedded terminal, the same as the Claude Code CLI |

The picker is labelled **Default mode for new sessions**, and its hint adds **You can switch modes anytime within a session.** A switch restarts the agent process under the other mode and resumes the same conversation, carrying your model, mode, effort, and shared context across.

Terminal mode keeps the full chat composer: attach images by paste or drag-and-drop, pick model, mode, and effort, use slash commands, and mention files with `@`. Two things differ from Rich chat:

- Claude's own terminal interface queues your input while it is busy, so Kepler's queue banner does not appear.
- Changing model, mode, or effort restarts the session via resume to pick the change up: *Changes to model, mode, or effort apply on your next message — the session restarts via resume to pick them up, so your current turn is never interrupted.*

In Terminal mode with **Detect Claude Code sessions started outside Kepler** off, Kepler warns you that it cannot track those sessions.

<!-- TODO(verify): still unresolved at main @ 7c31af83e (package version 0.8.1). The billing framing for these two modes: the v0.6.5 changelog describes the choice as how Claude Code is billed — your subscription in CLI mode, your credits pool in ACP mode — and says new sessions default to subscription billing. The shipped UI (src/ui/components/settings/ClaudeModeSection.tsx, en.ts `settings.agents.claudeMode.*`) still names the modes Terminal and Rich chat with no billing wording anywhere, and `CLAUDE_ACP_MODE_KEY` still defaults to true, i.e. Rich chat/ACP. Confirm the launch wording and the actual default before publishing this section. -->

<!-- TODO(verify): the mid-session switch this section describes. The setting's own hint promises it and the backend supports it — `switchSessionStrategy` in src/backend/agent/agent.ts, exposed through src/backend/api/agent-port.ts and src/shared/transport/api-agent.ts — but at main @ 7c31af83e there is still no caller anywhere in src/ui, so Settings remains the only surface that changes the mode and it governs new sessions only. The one-time first-use billing prompt from the v0.6.5 changelog is also still absent (`OnboardingPromptContext` in src/ui/data/onboarding.ts has no such context). Confirm which surfaces ship in v0.9. -->

***

## Sending a prompt

The composer sits at the bottom of the session.

| Control | What it does |
|---|---|
| **Attach a file** | Attaches a file for the agent to read. Drag onto the composer works too — *Drop files to attach*. On a remote connection, **Add a file from the remote** picks from the remote machine |
| Microphone | Voice input. See [Voice Input](/kepler/voice-input) |
| **Agent settings** | Agent, model, permission mode, effort, and options |
| Context usage | The share of the session's context window in use. Hover for tokens used, the window size, and cost so far |
| **Token usage** | Your provider plan's usage windows and, where the provider reports one, your plan balance. Off until you enable it — see below |
| **Send** | Sends the prompt. The chevron holds **Send** and every applicable Action |

**Enter** sends; **Shift+Enter** inserts a newline. **Cmd/Ctrl+F** opens **Find in conversation**.

While a turn is running the send button grows a stop segment — **Stop agent** — and *Interrupt current work. Queued messages will be sent next.* Send stays live throughout, because a busy session queues.

### Slash commands and skills, per repository

Type `/` to open the command menu. It lists the agent's built-in commands together with your commands and skills. Codex reports its skills with a `$` sigil and invokes them that way, so `$` opens a skills-only menu, but `/` still finds them, matched on the bare name, so you do not have to know the convention.

**Skills and slash commands are discovered per repository, not per agent.** The catalog is the union of your home-directory skills and the repository or worktree's own: for Claude Code, `~/.claude/skills` plus `.claude/skills`. Two consequences:

- One project's skills never show up in another project's menu.
- A skill added in a worktree and not yet committed can appear in that session before it appears elsewhere.

Kepler probes the catalog when you pick a repository and refreshes it whenever a live session reports a change, so a skill you add mid-session shows up without a restart.

### Mentioning files

Type `@` to search the working directory and insert a path. Kepler automatically approves files you paste into a chat for the agent to read.

***

## Queueing prompts while the agent is busy

You do not have to wait for a turn to end. Send while the agent is working and the prompt is queued behind it — the placeholder changes to *Type a message to queue...* and a banner above the composer counts what is waiting.

| In the banner | What it does |
|---|---|
| **{count} queued** | How many prompts are waiting |
| A queued row | The prompt's text, or a paperclip and filename when it is attachments only |
| **×** on a row | Removes that one prompt |
| **Clear queue** | Removes all of them |
| **Interrupt & send** | Stops the current turn so the queue starts immediately |

Queued prompts survive interruption. A **disconnect**, an expired token that forces **re-authentication**, and the **reconnect** afterwards all keep the queue: the rows stay on screen, nothing is dropped, and the prompts are handed to the reconnected session in the same order, under the same identities. Cancelling a turn promotes the next queued prompt rather than discarding it.

Each queued prompt picks up the Task's shared context as it stands when the prompt actually runs, not as it stood when you typed it.

If a send genuinely fails, Kepler puts the text back: *Something went wrong. Your message is back in the composer — try again.* If you have since typed a newer draft, it keeps that one and offers **Restore message**.

<!-- TODO(screenshot): the queue banner with two queued prompts, Interrupt & send and Clear queue visible. -->

***

## Reading the conversation

- Your messages appear as chat bubbles. Right-click one to **Copy message**, **Quote**, or **Ask**.
- Agent replies render as markdown, and stream as one continuous message even when a tool runs mid-reply.
- Tool calls collapse into groups: **{count} tool uses**, with **{count} done**, **{count} running**, and **{count} failed** tallies. Expand a group to read any call's output.
- A plan renders as **Plan {completed}/{total}**, and a plan cut short by a stop is marked **Interrupted**.
- Subagents get their own card, collapsed by default, holding **Prompt**, **Operations**, and **Result** sections that fold independently. Its trigger row carries the subagent type, the description it was given, how many operations it has run, and a status of **Running**, **Stopped**, **Completed**, or **Failed**, so a card that is still shut shows progress.
- A turn that ended for a reason worth knowing carries a pill: **Reached token limit**, **Reached request limit**, **Refused to continue**, or **Cancelled**. A healthy turn shows nothing.

Subagent work is attributed rather than mixed into the main thread. A subagent's own tool calls nest inside its card under **Operations** instead of appearing flat alongside the main agent's, and its narration renders in an indented lane of its own, marked **Subagent**, so you can see where it starts and stops even when it interleaves with the main agent's text. While a turn is running, that turn's subagent cards pin to the top of the session and drop back into the conversation when the turn ends; a card you expanded stays expanded for the rest of the turn.

Sessions you started in your own terminal appear too, marked **(external)** and **From outside Kepler**, once you turn on **Detect Claude Code sessions started outside Kepler**.

***

## When the agent asks you something

Kepler pauses and asks you directly when an agent needs a decision it can't make on its own. It does this in two ways: a permission request before a risky tool call, and a structured question when the agent wants your input mid-task.

### Permission requests

A request pins to the top of the session: an amber shield, the tool being asked about as the heading, and the call's input beneath it. The buttons are Kepler's own wording rather than the agent's, so a request reads the same whichever agent raised it.

| Button | What it does |
|---|---|
| **Allow** | Approves this one call |
| **Allow for this session** | Approves this call, and auto-approves matching follow-ups for the rest of the session. The agent is told only that you allowed it once, so it writes no rule of its own |
| **Allow always** | Hands the agent a permanent approval, which the agent stores in its own settings |
| **Reject** | Refuses this call |
| **Reject always** | Refuses it permanently |

You get the tiers the agent actually offers. **Allow for this session** is Kepler's own middle tier and appears only next to an **Allow**. A request that offers nothing but a permanent approval, as Claude Code's plan-exit prompt does, has no one-shot decision to widen. Where an agent draws its own distinction between several permanent choices, its labels are kept instead of a single **Allow always**, and any `Tool(...)` pattern a rule would cover is spelled out on a **RULE** line beneath the buttons.

Kepler coalesces repeats. A command that fires many identical requests (an install reaching the network over and over) asks once, and your answer settles the whole group.

Answered requests stay in the transcript, showing the tier you picked: **Allowed for this session** for the middle one, otherwise the button's own label, falling back to **Approved** or **Denied**.

#### Claude Code sessions from your own terminal

Sessions Kepler detects outside itself ask through Claude Code's hooks instead, and that card is the one that carries scopes: **Deny**, **Allow once**, and one **Always allow** per scope the hook suggests, narrowest first.

| Scope | Meaning |
|---|---|
| **this session** | Until this session ends |
| **this project (local)** | This project, your machine only |
| **this project (shared)** | This project, committed for your team |
| **all projects** | Everywhere |

Kepler prints the rule each button would write above them. A rule with no command pattern is annotated **(this tool)**, meaning it covers every call to that tool rather than one command.

### Multiple-choice and multi-select questions

Agents can ask you structured questions instead of guessing. The form renders in the conversation at the point the agent asked.

| Kind | How it behaves |
|---|---|
| Multiple choice | Radio-style. One option is the answer |
| Multi-select | Checkbox-style, hinted **Select all that apply**. Every ticked option is sent |

Both kinds work the same way otherwise:

- Options show a label and, when the agent supplied one, a description.
- Press **1**–**9** to pick an option by the number shown on it.
- **Other...** opens a free-text field — *Type your answer...* — which becomes the answer on its own for a single-choice question, and joins the ticked options on a multi-select.
- Several questions arrive as steps with a **{current}/{total}** counter and a tab strip; submit is enabled only once nothing is outstanding, and until then you see **{count} questions still unanswered**.
- **Chat about this** declines the form so you can answer in your own words in the chat. It does not cancel the session.
- If the agent set a deadline, the form counts down — **{count} seconds remaining** — and a form that was never answered is recorded as **Left unanswered** rather than left on screen as if it had been submitted.

A restored session shows the question and the answers you gave as a read-only record.

<!-- TODO(screenshot): a multi-select question form with the "Select all that apply" hint and two options ticked. -->

***

## Usage indicators

Two different readouts, and they measure different things.

| Readout | What it shows | Availability |
|---|---|---|
| **Context Usage** | How much of *this session's* context window is used, as a percentage. Hover for tokens used, the window size, and cost so far | Whenever the agent reports it |
| **Token usage** | Your provider plan's windows — **5h**, **7d**, and **Cycle** — as a percentage used, with when each resets, plus whatever else the provider reports about the plan | Claude Code, Codex, and Auggie, and only after you opt in |

Turn the second one on in **Settings → Agents → Agent options → Show token usage → Enable**. It is off by default, and the setting says why:

> Kepler will read your Claude Code, Codex and Augment access tokens from disk and call the providers' private usage APIs. These endpoints are undocumented and may change without notice. Tokens are never sent anywhere except to their respective provider.

What the chip shows depends on the provider. The trigger previews the shortest window as a donut, or the remaining plan balance where the provider reports a balance but no expressible percentage; hovering opens the detail.

| Provider | What its popover carries |
|---|---|
| **Claude Code** | The **5h** and **7d** windows, and an **Extra usage** pool with credits used against any monthly limit |
| **Codex** | The same two windows, plus **Usage limit resets**: earned resets that clear an active limit early, each with its expiry |
| **Auggie** | A **Cycle** window for the current billing period, and a plan line naming the plan with what is left of it — *{remaining} / {included} credits left*, or *{remaining} credits left* on an unmetered plan |

If the figures cannot be fetched, the chip says which problem it hit rather than showing a stale number — *Sign in to {agent} to see usage data.*, *Usage API rate-limited. Retrying in a few minutes.*, *This agent doesn't expose usage data.*

***

## Voice input

Every session's composer has a microphone. Click to record, speak, and the transcript lands in the prompt; transcription runs on your device. Voice input is off until you enable it and download a model.

See [Voice Input](/kepler/voice-input).

***

## Session status

Each session carries a state, shown as a coloured dot on its tab and rows.

| Status | Meaning |
|---|---|
| **Spawning** | Starting up |
| **Ready** | Connected, nothing sent yet |
| **Running** | Working on a turn |
| **Waiting** | Blocked on you: a permission request or a question |
| **Unread** | Finished a turn you have not looked at |
| **Idle** | Connected, nothing running |
| **Disconnected** | Dormant. The conversation is kept and can be resumed |
| **Error** | The turn or the process failed |
| **Terminated** | Ended for good |

When Kepler has to show one status for several sessions, the most urgent wins: **Waiting** and **Error** outrank live work, and **Unread** sits above **Idle** so a finished turn is not buried.

Away from the session itself those states collapse into a coarser ramp of five (attention, active, idle, errored, inactive), which is what [the main list](/kepler/kepler-interface)'s row and preview indicators read, and what decides where an [Action](/kepler/actions) fires. *Attention* covers both a waiting session and one holding an unanswered permission request or question.

***

## Tabs, archiving, and restoring

Open sessions form a tab strip. Each tab shows the agent, the account when more than one exists, and a status dot.

| Action | Result |
|---|---|
| **Cmd/Ctrl+T** or **+** | Starts a new session in this working copy |
| **Alt+1**–**Alt+9** | Jumps to a tab by position |
| **Cmd/Ctrl+Shift+[** / **]** | Previous or next tab |
| **×** on a tab (**Close session**) | Archives the session |
| **Archive** on a rail row | The same thing |
| **Restore** | Brings an archived session back into the strip |

**Closing a tab and archiving are one operation.** Kepler stops the agent process, saves the conversation and its resume handle, and takes the tab out of the strip. Nothing is deleted.

Archived sessions collect under a **{count} archived** fold beneath the live ones in the task rail, and the **+** picker offers **Restore a session** with **Search sessions…** across them. Restoring puts the session back in the list; it reconnects when you open it. A worktree with nothing open reads **No active sessions in this worktree.**

Deleting a task or removing its repository ends that task's live sessions. Quitting Kepler with sessions running asks first, and warns that each one will stop.

Your computer will not go to sleep out from under a running agent. While any session is spawning, running, or waiting on you, Kepler holds the machine awake, and lets go as soon as the last one settles. It is on out of the box and turned off in **Settings → General → App behavior → Prevent sleep while agent sessions are active**. See [Settings](/kepler/settings).

***

## When a session drops

Kepler distinguishes three failure shapes, and each offers only the recovery that applies.

| What you see | What happened | What to do |
|---|---|---|
| **Session disconnected** — *The agent went offline. Reconnect to continue the conversation.* | The process is gone; the conversation is not | **Resume session** |
| **Session can no longer be resumed** — *Claude can no longer find this conversation. Close the saved session to remove it from this worktree.* | The agent no longer holds the transcript | **Close session** and start a new one |
| **Session ended** — *This session has been terminated. Start a new task to keep working in this worktree.* | Terminated for good | Start a new session |

An **Agent error** banner names the cause — *Agent binary is missing or not executable.*, *Agent authentication failed.*, *Agent process exited on its own.* — and offers **Reconnect**, **Authenticate**, **Compact**, or **Dismiss** as the cause warrants.

In Terminal mode a dead process reads **Terminal exited. Resume to reattach to this conversation.**, or, when it crashed, **Agent process ended unexpectedly** — *The agent process exited on its own. Your conversation is preserved — restart to reattach and continue.*

Sessions recover on their own where they can: Kepler renews an authentication token that expires mid-session so the session continues, and remote connections re-establish after a restart or sleep.

***

## Notifications

Kepler tells you when a session finishes or needs you.

| Notification | When |
|---|---|
| **Task completed** | A turn ended. Sent only as a desktop notification, since it is useful only when you are away from Kepler |
| **Needs attention** | The agent is blocked on a permission request or a question. Also shown in-app |
| **Error** | The session errored. Also shown in-app |

Titles read **{status}: {task}**, with the agent and the repository or branch beneath — *{adapter} on {repo}/{branch}* — and clicking one takes you to the session.

Kepler stays quiet about the work you are already watching: it sends no notification for the session on screen in a focused window. A cancelled turn is not a completion, and a session reconnecting is not a completion either, so neither notifies.

Two settings in **Settings → General → App behavior** control the rest:

| Setting | What it does | Default |
|---|---|---|
| **Enable system notifications** | Desktop notifications when an agent finishes, needs your attention, or errors while Kepler is in the background. Turning it on sends a sample so you can allow notifications for Kepler | Off |
| **Notify for external terminal tasks** | Notifications for Claude tasks running in your own terminal. Turn it off to silence those while keeping Kepler's own. Disabled while system notifications are off | On |

In-app toasts carry a close button on hover, and **Clear all ({count})** dismisses the lot.

***

## Reviewing what the agent changed

Reading the diff, staging, committing, and pushing are covered on their own page — see [Review Changes](/kepler/review-changes).

---
