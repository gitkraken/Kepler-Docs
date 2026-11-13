---
title: Sessions Started Outside Kepler
description: Kepler finds agent conversations you started outside it, in a terminal or in an old transcript. Turn detection on, read one, and take it over into a task.
product: Kepler
feature: Agent Sessions
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot, cursor, auggie, opencode, grok, pi, antigravity]
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [external-sessions, detection, transcripts, adopt-session, terminal]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "kepler-working-in-kepler"
    nav_label: "Sessions Started Outside Kepler"
    nav_order: 50
    nav_parent: "kepler-working-in-kepler"
    page_type: "content"
    card_icon: "terminal-2"
    card_color: "blue"
    card_description: "Find, read and take over agent conversations started outside Kepler"
---
<kbd>Last updated: November 2026</kbd>

Kepler also finds agent conversations that it did not start. For example, you might run `claude` in a terminal, or return a week later to a transcript that is still on disk. Kepler lists both as agent sessions.

Kepler takes over a conversation only when you ask. It binds the conversation to a task, and it does not take control of the terminal that runs it.

## Turning detection on

Detection is on by default. To turn it on or off, use **Settings → Integrations → Your terminal → Show sessions started outside Kepler**.

The switch installs GitKraken hooks, so each agent's own CLI reports what it is doing to Kepler. The one switch covers every agent that Kepler can track this way: **Claude Code**, **Codex**, **Cursor**, **GitHub Copilot**, **OpenCode**, **Auggie**, **Grok Build**, and **Pi**. Kepler does not track Google Antigravity through hooks. Turning the switch off stops reporting from all of them.

Kepler follows **Terminal** sessions through the same hooks. If a live session stops reporting, Kepler warns that **Agent sessions aren't reporting to Kepler**, because its status and notifications may be out of date. Click **Repair**, then restart any session that still does not report. To repair sessions running on another computer, use Kepler on that computer.

Detection shows *live* outside sessions. Kepler also finds **past** sessions from the transcripts the agent writes to disk, including ones from before you turned detection on.

To find these sessions in Kepler, see [The Kepler Interface](/kepler/kepler-interface#external-sessions). To turn one into a task, see [Create a task](/kepler/create-task#from-a-session-you-already-started).

## Reading one

An outside session opens read-only, marked **(external)** and **External**, with its transcript labeled **Session transcript (read-only)**. Its context card shows a badge for its state and one sentence that says where the conversation lives and what you can do about it in Kepler.

| Badge | What it means |
|---|---|
| **Running** | Working on a turn, outside Kepler |
| **Waiting on you** | Blocked on a question or a permission request in its own interface |
| **Idle** | Connected and doing nothing |
| **Ended** | The process finished |
| **Not running** | Found on disk, with nothing running it anywhere |

For a waiting session, answer in your terminal. Kepler does not answer a prompt it does not own, but it notifies you that the session is waiting, whatever the agent.

Kepler reads the transcripts of **Claude Code**, **Codex**, **GitHub Copilot**, **Cursor**, **OpenCode**, **Auggie**, **Grok Build**, **Pi**, and the **Google Antigravity** CLI from each agent's own store on disk, without starting the agent. For Cursor, that includes chats from its terminal CLI.

<figure style="text-align:center">
  <a href="/wp-content/uploads/external-past-session-preview-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/external-past-session-preview-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The preview of a past Pi session started outside Kepler, marked Not running, with its folder, Import session and Create new task, and the replayed conversation: the prompt, the agent's replies, and its Read products.js call.">
  </a>
  <figcaption style="text-align:center; color:#888">A past Pi session, previewed read-only from its transcript on disk.</figcaption>
</figure>

Kepler replays an Antigravity conversation but does not follow it live.

If Kepler cannot read a transcript, it says which problem it hit instead of showing an empty conversation:

| What you see | What it means |
|---|---|
| **No transcript to show** | Kepler could not find the file. It may predate detection, the agent may store it somewhere Kepler does not look, or the agent never wrote one, as with a session that never ran a turn |
| **Kepler can't read this session's transcript** | The file exists, but Kepler could not open it. Check its permissions; Kepler keeps retrying |
| **Waiting for activity…** | The agent has not written anything yet |

If a live session goes quiet, Kepler flags that it may have ended without reporting it, instead of showing it as busy.

## Taking one over

You can take over an outside session in 2 ways. They differ in what happens to the terminal you started it in:

| Button | What it does |
|---|---|
| **Fork** | Copies the conversation into a new Kepler session, and your terminal keeps the original. Both continue independently |
| **Continue here** | Carries on the same conversation in Kepler |

Both buttons work only once the session is idle. If it waits on you, answer it in your terminal first.

If a terminal still owns the session, **Continue here** asks you to confirm. Close the conversation in your terminal first, because 2 programs writing the same conversation corrupt it.

When you take over a conversation from disk, the agent starts on your first message, not when you take it over. Adopting one costs nothing.

---
