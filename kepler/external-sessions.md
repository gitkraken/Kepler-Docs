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
    nav_category: "working-in-kepler"
    nav_label: "Sessions Started Outside Kepler"
    nav_order: 50
    nav_parent: "working-in-kepler"
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

Kepler follows **Terminal** sessions through the same hooks. If a live session's hook events stop arriving, Kepler warns you so that status and notifications do not go out of date: **Agent sessions aren't reporting to Kepler**, *Session status and notifications may be out of date. Repair reinstalls the reporting configuration.* After you click **Repair**, restart any session that still does not report. A window that only views sessions running on another computer shows the warning without **Repair**: *To repair reporting, use Kepler on the computer running these sessions.*

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

The sentence matches the badge. A running session reads *Follow along here.* A waiting one reads *Answer it in your terminal.* Kepler does not answer a prompt it does not own, but it notifies you that the session is waiting, whatever the agent.

When you pick a live outside session from **Open an external session**, it always opens this way, read-only in its task. Picking it never takes the conversation over.

Kepler reads the transcripts of **Claude Code**, **Codex**, **GitHub Copilot**, **OpenCode**, **Auggie**, **Grok Build**, **Pi**, and the **Google Antigravity** CLI from each agent's own store on disk, without starting the agent. A few agents behave differently:

- A GitHub Copilot autopilot run ends with its completion summary, shown as the agent's answer.
- A GitHub Copilot session run in **Chat** has a transcript on disk once it has run a turn.
- A **Cursor** session still appears as a row and you can still adopt it, but it shows *Preview isn't available for {agent} sessions yet.* in place of the conversation.

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

## Taking one over

You can take over an outside session in 2 ways. They differ in what happens to the terminal you started it in:

| Button | What it does |
|---|---|
| **Fork** | *Copies this conversation into a new Kepler session. Your terminal keeps the original.* Both continue independently |
| **Continue here** | *Carries on this conversation in Kepler.* One conversation, now owned by Kepler |

Both buttons stay on screen while the session works, but they work only once it is idle. Hover a button to see why it is unavailable: *Available once it is idle.*, or *Answer it in your terminal first.* while the session waits on you.

If a terminal still owns the session, **Continue here** first asks **Continue this conversation here?** If 2 clients write the same conversation, they corrupt it: *If your terminal is still open, both will write to this conversation. Close it there first.* Once Kepler has the conversation, the view shows *Ready to continue here.*

When you take over a conversation from disk, the agent starts on your first message, not when you take it over. Adopting one costs nothing.

---
