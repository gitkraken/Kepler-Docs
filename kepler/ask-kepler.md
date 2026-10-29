---
title: Ask Kepler
description: "Ask Kepler is a chat and a terminal in a panel beside whatever you're looking at. Ask what needs you, have it check on your tasks and sessions, hand a chat on to a new task, or open a quick shell that belongs to no task."
product: Kepler
feature: Ask Kepler
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode, grok, antigravity]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [ask-kepler, chat, assistant, terminal, side-panel, keyboard, agent-sessions]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

**Ask Kepler** is a panel with two sections: a **Chat** with an agent that can see what's on your screen and check on your tasks and sessions, and a **Terminal** of quick shells that belong to no task. Use it for a question that doesn't deserve a task of its own, or to find out what needs you without leaving the page you're on.

This page covers opening and arranging the panel, the chat, and the panel's terminals. For the agent sessions that run inside a task, see [Agent Sessions](/kepler/agent-sessions).

<figure style="text-align:center">
  <a href="/wp-content/uploads/ask-kepler-chat-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ask-kepler-chat-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Ask Kepler panel open on the right of the Dashboard, under the top bar. Its header holds New chat with a chevron for past chats, the New chat button, Terminal, Move to the left and Close. Kep, the planet mascot, sits over Ask Kepler anything and the line Ask a quick question, or have Kepler check on and manage your tasks and sessions, with the starters What needs me right now? and What changed across my tasks today?, and the Ask anything composer at the bottom with the agent pill.">
  </a>
  <figcaption style="text-align:center; color:#888">Ask Kepler, open on a new chat over the Dashboard.</figcaption>
</figure>

***

## Open and close the panel

You can open **Ask Kepler** from anywhere in Kepler in one of these ways:

| How | Opens |
|---|---|
| The **Ask Kepler** button (the Kepler mark) in the top bar | The panel, on the section you used last |
| **Cmd/Ctrl+L** (**Toggle Ask Kepler chat**) | The **Chat** section |
| **Ctrl+&#96;** on every platform, macOS included (**Toggle Ask Kepler terminal**) | The **Terminal** section, starting a shell if none is open |

Press the same shortcut again while focus is still inside the panel to put it away. On Windows and Linux, a focused shell keeps **Ctrl+L** for itself, so press it outside the terminal to toggle the chat.

The panel floats as a card over the left or right edge of the page, under the top bar. Nothing dims behind it, so the page underneath stays usable. Its header holds the open section, a button for the other section, and the panel's own controls:

- **Move to the left** or **Move to the right** docks the panel to the other edge of the window.
- **Close Ask Kepler** puts it away.

**Resize.** Drag the panel's inner edge (**Resize Ask Kepler**) to change its width, or focus the edge and use the arrow keys. Double-click the edge to return to the default width. The panel is never narrower than 360 pixels or wider than 60% of the window. Kepler remembers the width and the side on this computer, for every window.

**Escape** also closes the panel, unless the key means something else where you are: a text field that holds a draft, a find bar, a shell (where the program owns the key), or a chat whose agent is still answering, where **Escape** stops the turn instead.

Closing only hides the panel. A half-typed question, the open chat, and every shell's scrollback are still there the next time you open it.

***

## The chat

The **Chat** section is a conversation with an agent that works for you across Kepler rather than inside one task. A new chat opens on **Ask Kepler anything**, *Ask a quick question, or have Kepler check on and manage your tasks and sessions.*, and a composer that reads *Ask anything*. Pick the agent from the pill in the composer, type your question, and send it.

### Starter prompts

A new chat offers starting points you can send with one click:

- **What needs me right now?**
- **Summarize this task**, only while you're on a task's page
- **What changed across my tasks today?**

A starter goes out as the chat's first message and leaves anything you already typed in the composer alone.

### What the chat knows

The chat keeps up with what you have on screen. With each message, Kepler tells the agent where you are when that has changed since its last message:

- The page you're on: the Dashboard, a task, Settings, or somewhere else
- The task you're looking at, and its checkouts
- The sessions on screen

So a question such as *what's this one stuck on?* reads against the task in front of you. Kepler also tells it which sessions are waiting on you, such as approvals, permission requests, questions, and failed or unread sessions, and asks it to bring these up only when you ask. Ask **What needs me right now?** to get that list.

The agent can read your tasks and sessions and act on them through Kepler's own tools. Before it starts a session on a task that it didn't create, Kepler asks you first. When it mentions a task or a session, it names it as a link you can click.

### Which agents can answer

A panel chat always runs over the **Agent Client Protocol** (**ACP**), so the agent pill lists only agents that Kepler can drive over ACP. An agent that runs only in a terminal, such as Pi, can't answer in the panel. See [Agent Integrations](/kepler/agent-integrations) for which agents run in **Chat**.

### Past chats and new chats

The chat's title in the panel header is also a picker of your chats. Open it to find the following:

- **New chat**, which returns the section to a fresh chat
- **Continue in a new task**, for the chat that's open
- **Past chats**, newest activity first, each with when it was last active. Click one to open it again, or use **Archive {title}** beside it to put it away. With none yet, the list reads **No past chats yet**.

The **New chat** button beside the title does the same as the picker's first row.

### Continue in a new task

When an answer turns out to be the start of real work, choose **Continue in a new task**. It sits under the chat's latest reply and in the past-chats picker. It opens the Task Composer with the prompt *Pick up where the chat left off.*, the chat attached as the session the task continues from, and the same agent, account, model, and mode the chat used. Edit anything you like before you start the task. See [Create a Task](/kepler/create-task).

A panel chat belongs to no task, so when a task's session links back to the chat it continued from, the chat opens in the panel. A notification from a panel chat also opens the panel on that chat.

***

## Quick terminals

<figure style="text-align:center">
  <a href="/wp-content/uploads/ask-kepler-terminal-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ask-kepler-terminal-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Ask Kepler panel on the right of the Dashboard, open on its Terminal section: the header strip holds Chat, the Terminal 1 tab with its menu and close buttons, and New terminal, then Move to the left and Close. The shell runs in the home folder and shows a git log of acme-web's last three commits.">
  </a>
  <figcaption style="text-align:center; color:#888">The Terminal section, with one shell in the home folder.</figcaption>
</figure>

The **Terminal** section holds shells that belong to no task, in the same tab strip a task page's terminal drawer uses. The first time you open the section, Kepler starts a shell so that the strip is never empty. Press **Ctrl+&#96;** with no shell open and Kepler starts one, the way the same key does in VS Code. After you close the last shell, the strip stays empty until you ask for another.

Where a new shell opens depends on where you are:

- On a task's page, a new shell opens in one of that task's checkouts.
- Anywhere else, or on a task with no checkouts, it opens in your **Home folder**.

The panel's shells stay the panel's own. They never join a task's terminal drawer, and they keep running when you move between pages or close the panel. While the **Terminal** section is open, its tab strip doubles as the panel header, with **Chat** as a button at its leading edge.

---
