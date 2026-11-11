---
title: Answering Your Agent
description: Answer your agents' permission requests, questions, plan reviews, and approval cards, read reports from other agents, and choose which notifications you get.
product: Kepler
feature: Agent Sessions
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot, cursor, auggie, opencode, pi]
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [permissions, approvals, questions, plan-review, agent-reports, notifications, hooks]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "kepler-working-in-kepler"
    nav_label: "Answering Your Agent"
    nav_order: 30
    nav_parent: "kepler-working-in-kepler"
    page_type: "content"
    card_icon: "bell"
    card_color: "blue"
    card_description: "Answer permission requests, questions, plan reviews and approvals, and get notified"
---
<kbd>Last updated: November 2026</kbd>

When an agent needs a decision it cannot make on its own, Kepler pauses and asks you in one of these ways:

- A permission request before a risky tool call.
- A structured question when the agent wants your input mid-task.
- A plan review when the agent proposes a plan before it starts.
- An approval card when the agent asks Kepler itself to do something that needs your approval, such as deleting a worktree.

Reports from other agents arrive in a session's inbox and do not ask you anything; see [Reports from other agents](#reports-from-other-agents).

You can answer a request from any window that shows it, or from its notification. If another window answered it first, Kepler says **Already answered**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-permission-request-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-permission-request-oct-2026.png" class="help-center-img img-bordered" alt="A permission request for a shell command, marked Needs approval, with the agent's reason, Contains brace with quote character, just above the Allow, Allow for this session, and Reject buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">A permission request, with the agent's reason above the buttons.</figcaption>
</figure>

## Permission requests

A permission request pins to the top of the session. It shows an amber shield, the tool being asked about as the heading, and the call's input beneath it. If the agent says why it is asking, the reason appears just above the buttons. For example, a Claude Code session in auto mode can still hit a safety check. A request to reach outside the agent's network sandbox says so in Kepler's own words, *Reaches outside the network sandbox.*, with the agent's reason when it gives one.

The buttons read the same whichever agent raised the request:

| Button | What it does |
|---|---|
| **Allow** | Approves this one call |
| **Allow for this session** | Approves this call, and approves matching follow-up calls automatically for the rest of the session. The agent saves no permanent rule |
| **Allow always** | Gives the agent a permanent approval, which the agent stores in its own settings |
| **Reject** | Refuses this call |
| **Reject always** | Refuses it permanently |

You see only the tiers the agent offers. **Allow for this session** is Kepler's own middle tier and appears only next to an **Allow**. A request that offers only a permanent approval, such as Claude Code's plan-exit prompt, has no one-time approval to extend, so it has no middle tier. If an agent offers several permanent choices, Kepler keeps the agent's labels instead of a single **Allow always**. A **RULE** line beneath the buttons spells out any `Tool(...)` pattern a rule would cover.

Kepler combines repeated requests. A command that fires many identical requests, such as an install that reaches the network again and again, asks once, and your answer settles the whole group.

A request raised by a subagent that another subagent started shows on the outermost subagent card, under the path of subagent names that leads to it (**Parent › Child**). See [Reading the conversation](/kepler/agent-sessions#reading-the-conversation).

Answered requests stay in the transcript, showing the tier you picked: **Allowed for this session** for the middle one, otherwise the button's own label, falling back to **Approved** or **Denied**.

### Requests that arrive through hooks

A session in **Terminal** mode and a session that Kepler **detected outside itself** both ask through the agent's own hooks. You still answer in Kepler, without switching to the CLI's own prompt. The card comes from the agent, though, so it offers scopes instead of Kepler's tiers: **Deny**, **Allow once**, and one **Always allow** for each scope the hook suggests, narrowest first:

| Scope | Meaning |
|---|---|
| **this session** | Until this session ends |
| **this project (local)** | This project, your machine only |
| **this project (shared)** | This project, committed for your team |
| **all projects** | Everywhere |

Above the buttons, Kepler shows the rule each button would write. A rule with no command pattern is marked **(this tool)**, which means it covers every call to that tool, not one command.

Kepler never approves a hook request for you. If Kepler stops holding a request before you answer (the turn ends, the conversation moves elsewhere, or Kepler quits), it hands the request back to the CLI, which asks in its own dialog.

A Codex question asked through its hooks shows in Kepler as a question you can answer, with its options and their descriptions. Cursor has no permission or notification hook, so a Cursor Terminal or outside session cannot tell Kepler that it is waiting on you. The session reads **Running** until it stops, and you answer in the terminal.

## Multiple-choice and multi-select questions

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

## Reviewing a plan

When an agent in plan mode proposes a plan, Kepler opens it for review in a **Plan** panel beside the chat, with **Preview** and **Edit** tabs. The transcript shows the plan with **Open plan**. Claude Code, Codex, GitHub Copilot, Cursor, and OpenCode Chat sessions offer plan review. Cursor holds its plan request open while you review it, so the session waits with the reason **Plan review**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/plan-review-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/plan-review-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A Chat session with its Plan panel open beside the transcript for the plan Fix the discount order in the cart total. Step 2, Round once, at the end, to two decimal places, is highlighted and carries a comment under Comments (1), with Request changes (1) and a grayed-out Approve & implement at the foot.">
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

## Approval requests

Some actions that an agent asks Kepler itself to do, through Kepler's workspace tools, wait for your approval. For example:

- Sending a prompt or a message to another session, or stopping, renaming, or archiving one.
- Editing or deleting a task note, changing another task or its links, detaching files, archiving or restoring another task's resources, or archiving a task.
- Deleting a worktree.
- Starting a session in a more permissive mode than the asking session's own.
- Syncing a branch with its target, or rewriting its commits.
- Overwriting a theme file.
- Changing a Kepler setting that affects your accounts, your privacy, other tools, what runs, or where files go. Only **Ask Kepler** can change settings. See [Ask Kepler](/kepler/ask-kepler#finding-and-changing-settings).

Kepler tells the agent that the request is waiting, and the agent can keep working; your answer reaches the agent's inbox later. Meanwhile, the session reads **Approval needed** or **Approval needed, destructive**.

The request is pinned above that session's composer as a card. The card names the action, such as **Delete worktree {worktree} and its branch**, and shows what is at stake (*At risk: {loss}*), with **Approve** and **Deny**. A card for an action that can lose work is amber; other cards are blue. If several requests are waiting, page through them with **{index} of {count}**. A setting change reads **Change the setting {setting}**, with **From {from} to {to}** beneath, or **To {to}, on your computer** for a setting kept on your own computer.

Other cards say what they would do in the same way, such as **Archive resources on {task}** or **Hold until {pr} merges or closes**. A card for an action that would stop agents names them.

<figure style="text-align:center">
  <a href="/wp-content/uploads/approval-card-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/approval-card-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="An amber approval card pinned above the session composer, Delete worktree acme-web@kepler/cart-total-spike and its branch, At risk: 2 uncommitted files, with the Approve menu open on Approve all worktree deletes from this session and a grayed-out Always approve worktree deletes.">
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

## Reports from other agents

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

## Notifications

Kepler notifies you when a session replies, needs you, or fails. Each notification has one of these statuses:

| Status | When |
|---|---|
| **Replied** | An agent finished replying, and it is your turn |
| **Asked a question** | The agent asks you something and waits for your answer |
| **Needs permission** | The agent wants permission to do something |
| **Plan ready for review** | The agent proposed a plan and waits for your review. It follows your **Questions** choices in **Settings → Notifications** |
| **Approval needed** | An agent asks Kepler to do something only you can approve, like deleting a worktree. A destructive request reads **Approval needed for a destructive action** |
| **Error** | The session stopped because something went wrong |

A Terminal or external session blocked on a prompt in its own CLI also notifies you, for every agent. Sessions started outside Kepler notify you only once they are on a task.

A notification's title reads **{status}: {task}**, with the agent and the repository or branch beneath (*{agent} on {repo}/{branch}*). Click the notification to go to the session. Kepler opens it in the window that already shows that session or its task, or else in the window you used last. An approval notification's title is its status alone. Beneath it are the action, what a destructive action would put at risk, and *Asked by {session}*.

You can answer an approval request from its alert. The in-app alert has **Approve** and **Deny** for every request, destructive ones included, followed by **View**, which opens the request in its session. On macOS, the desktop notification also has **Approve** and **Deny** buttons, which answer the request without opening a window. Windows and Linux notifications have no buttons.

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

---
