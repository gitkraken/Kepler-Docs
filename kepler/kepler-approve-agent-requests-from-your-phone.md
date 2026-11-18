---
title: Approve Coding Agent Requests from Your Phone with Kepler
description: In Kepler, turn on Remote Access and pair your phone to see what Claude Code, Codex and other agents are doing and answer their permission requests.
product: Kepler
feature: Remote Access
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode, grok, pi, antigravity]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [phone, mobile, remote-access, permissions, permission-requests, approve, approvals, away-from-desk, coding-agents, claude-code, codex, qr-code, plan-review]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Kepler by GitKraken lets you see what your coding agents are doing and approve their requests from your phone. Turn on Remote Access in Kepler on your computer, scan its QR code with your phone, and answer each permission request from Claude Code, Codex, or any other agent in your phone's browser, with the same choices as on your desktop.

## Requirements and limits

- Scope: Watching agent sessions and answering permission requests, questions, plan reviews, and approval requests from a phone
- Prerequisite: Kepler running on your computer, signed in to your GitKraken account. Your agents keep running on the computer, and the phone shows its interface
- Prerequisite: A phone browser signed in to the same GitKraken account
- Limits: Kepler sends no push notifications to your phone. Requests appear on the phone only while Kepler is open there, as an alert and in the waiting task

***

## Quick Start

1. In Kepler on your computer, open **Settings → Remote Access** and click **Turn on Remote Access**.
2. In **Name this machine**, keep the name or enter your own, then click **Turn on Remote Access** in the dialog.
3. Scan the QR code with your phone's camera, and sign in with your GitKraken account.
4. In your phone's browser menu, choose the option that adds the page to your home screen, such as Add to Home Screen, to open Kepler like an app.
5. When an agent stops to ask, open Kepler on your phone, tap the task that waits on you, and answer the request with **Allow**, **Allow for this session**, **Allow always**, **Reject** or **Reject always**.

***

## How to turn on Remote Access

Remote Access opens this Kepler from another device, such as your phone, through your GitKraken account. Your agents, worktrees, and terminals stay on your computer.

1. On your computer, open **Settings → Remote Access**, or hover over the **Remote Access** button in the title bar.
2. Click **Turn on Remote Access**.
3. In **Name this machine**, keep the name Kepler fills in, or enter a name you recognize, then click **Turn on Remote Access** in the dialog.

Remote Access stays on until you turn it off, including after Kepler restarts. By default, Kepler keeps your computer awake while Remote Access is on, so your agents keep working while you are away. To change this, use **Keep this machine awake while agents work** in **Settings → General**. See [Remote Environments](/kepler/remote-environments#turning-on-remote-access).

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-access-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-access-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Remote Access while it is off: the Inactive badge and Turn on Remote Access, Your agents, wherever you are, the 3 steps of How it works, a note that only you can connect, Machines on your account with Manage machines on gitkraken.dev, and This machine stays awake while Remote Access is on, with Change in General.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings → Remote Access, before you turn it on.</figcaption>
</figure>

***

## How to pair your phone

When Remote Access is active, Kepler shows a QR code and a link in **Settings → Remote Access** and in the **Remote Access** popover.

1. Scan the QR code with your phone's camera. To pair another browser instead, click **Copy link** and open the link there.
2. The link opens gitkraken.dev. Sign in with the GitKraken account you use in Kepler.
3. Kepler opens in your phone's browser, in a layout made for phones.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-access-popover-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-access-popover-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Remote Access popover open under the title bar's Remote Access button: Remote Access with an Active badge, Use this machine anywhere, No paired devices yet, a QR code captioned Scan with your phone's camera to open this machine, the gitkraken.dev/integrations?connect= link with Copy link, Works in any browser signed in to your GitKraken account, Turn off Remote Access, and Manage Remote Access….">
  </a>
  <figcaption style="text-align:center; color:#888">Scan the QR code in the Remote Access popover to pair your phone.</figcaption>
</figure>

Only your GitKraken account can connect. To disconnect one device, use **Connected devices** in **Settings → Remote Access**. To disconnect every device, click **Turn off Remote Access**.

***

## How to add Kepler to your home screen

To open Kepler like an app, add it to your phone's home screen from the browser's menu, such as Add to Home Screen. The Kepler icon then opens Kepler full screen, without the browser's address bar and toolbars.

***

## How to find what waits on you

Kepler marks every task and session that waits on you, so you can find a request as soon as you open Kepler on your phone:

- **An alert.** While Kepler is open on the phone, a new permission request, question, plan review or approval request shows as an alert. A permission alert has **Allow** and **Deny** for a one-time answer, and **View**, which opens the request in its session.
- **The menu.** Tap **Menu**. Under **Recent tasks**, a dot marks each task that waits on you.
- **The task list.** On the Dashboard, a Tasks view grouped by **Inbox** lists the tasks that wait on you under **Needs attention**.
- **Inside a task.** Tap **Sessions** to go to the session that waits on you. A dot on the back arrow means another task needs you.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-access-phone-sep-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-access-phone-sep-2026-v3@2x.png" class="help-center-img img-bordered" alt="Kepler's Dashboard in a phone's browser, on the Tasks view: one bar with Menu, the view picker showing Tasks with a chevron and an orange dot, Search, Options and New task, over the task list grouped into Needs attention (Add product search, In Development, Approval needed), Unread (Fix the cart total, In Review with its pull request and issue chips and Changes requested; Update checkout copy, On Hold, and Upgrade the payment SDK, In Review, each with New reply) and a folded Not started (1).">
  </a>
  <figcaption style="text-align:center; color:#888">The Tasks view on a phone, with a task that needs approval at the top.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/phone-drawer-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/phone-drawer-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The phone menu open over the Dashboard: Kepler with Close at the top, then Views listing Todo (type Todo, highlighted as the current view), Tasks (type Tasks) and Agent Graph (type Tasks), the last two with an orange needs-you mark on their icons. Recent tasks lists Fix the cart total, Add product search, Update checkout copy, Upgrade the payment SDK and Write the 2.4 release notes with their status dots, above the Feedback, Settings and Help buttons and Alex Lee (Enterprise).">
  </a>
  <figcaption style="text-align:center; color:#888">The phone menu, with a dot on each recent task that waits on you.</figcaption>
</figure>

> **Note:** When Kepler is closed on the phone, nothing tells you that an agent is waiting. Open Kepler on the phone to check. On your computer, Kepler's desktop notifications still work as usual.

***

## How to answer a permission request

A permission request pins to the top of its session. It names the tool the agent wants to use and shows the call, such as the shell command. Tap one of the buttons:

| Button | What it does |
|---|---|
| **Allow** | Approves this one call |
| **Allow for this session** | Approves this call and matching calls for the rest of the session |
| **Allow always** | Gives the agent a permanent approval, stored in the agent's own settings |
| **Reject** | Refuses this call |
| **Reject always** | Refuses it permanently |

You see only the choices the agent offers. A session in Terminal mode offers **Allow once**, **Always allow**, and **Deny** instead. The agent continues as soon as you answer. If you already answered on another device, Kepler says **Already answered**. See [Agent Sessions](/kepler/agent-sessions#permission-requests).

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-permission-request-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-permission-request-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A permission request for a shell command, marked Needs approval and headed Run the search tests, the agent's description of the command, with the command itself, npm test -- --run search, in a box beneath it, above the Allow, Allow for this session, Allow always and Reject buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">A permission request, shown here on the desktop. The phone shows the same buttons.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/phone-permission-request-nov-2026@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/phone-permission-request-nov-2026@2x.png" class="help-center-img img-bordered" alt="A task page in a phone-width browser for Add product search, In Development, with its plan (1 of 3 steps done). Below the request Add product search to the product list and the agent's reply, a permission request for Run npm test, marked Needs approval, sits above the Allow, Allow for this session, Allow always and Reject buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">A permission request on a phone, with every answer available.</figcaption>
</figure>

***

## How to answer plans, questions, and approval requests

Other requests wait in the session the same way, and you answer them on the phone as you do on your computer:

- **A plan review.** Read the agent's plan, then **Approve** it or comment and tap **Request changes (*n*)**. See [Reviewing a plan](/kepler/agent-sessions#reviewing-a-plan).
- **A question.** Pick an option, or type your own answer, and submit. See [Multiple-choice and multi-select questions](/kepler/agent-sessions#multiple-choice-and-multi-select-questions).
- **An approval request**, when an agent asks Kepler itself to do something, such as delete a worktree. Tap **Approve** or **Deny**. See [Approval requests](/kepler/agent-sessions#approval-requests).

To see what an agent did while you were away, open its session and read the conversation, or tap **Changes** to read the changed files.

***

## Common questions

Short answers about approving agent requests from a phone with Kepler.

### Will my phone notify me when an agent needs permission?

No. Kepler sends no push notifications to your phone. A request shows on the phone as an alert, and in its task, only while Kepler is open there. Add Kepler to your home screen so you can check it in one tap.

### Do I need to install an app on my phone?

No. Kepler opens in your phone's browser. To open it like an app, add it to your home screen from the browser's menu.

### Does my computer need to stay on?

Yes. Your agents run on your computer, and the phone shows that computer's Kepler. By default, Kepler keeps the computer awake while Remote Access is on, with the setting **Keep this machine awake while agents work**.

### Does this work with Claude Code and Codex?

Yes. In a Chat session, a permission request shows the same buttons whichever agent raised it, including Claude Code, Codex, and GitHub Copilot. A session in Terminal mode offers **Allow once**, **Always allow**, and **Deny**, and you answer those from the phone too.

### Can someone else open my Kepler from their phone?

No. Only your GitKraken account can connect. You can disconnect any single device in **Connected devices**, or every device with **Turn off Remote Access**.

***

## Related pages

- [Remote Environments: Remote access](/kepler/remote-environments#remote-access-reach-kepler-from-another-device)
- [Remote Environments: Using Kepler on a phone](/kepler/remote-environments#using-kepler-on-a-phone)
- [Agent Sessions: When the agent asks you something](/kepler/agent-sessions#when-the-agent-asks-you-something)
- [Agent Sessions: Notifications](/kepler/agent-sessions#notifications)
- [Kepler Quick Answers: Running Coding Agents](/kepler/quick-answers)
