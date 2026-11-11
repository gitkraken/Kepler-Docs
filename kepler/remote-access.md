---
title: Remote Access
description: Open this Kepler from another computer or your phone: turn on Remote Access, pair devices, use it on a phone, and manage sessions from gitkraken.dev.
product: Kepler
feature: Remote Access
content_type: how-to
audience: developer
plan_required: Pro
os_support: [Windows, macOS, Linux]
git_hosts: [n/a]
integrations: []
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [remote-access, phone, pairing, qr-code, gitkraken-dev, relay]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "configuration"
    nav_label: "Remote Access"
    nav_order: 30
    nav_parent: "configuration"
    page_type: "content"
    card_icon: "device-mobile"
    card_color: "amber"
    card_description: "Open this Kepler from another computer or your phone"
---
<kbd>Last updated: November 2026</kbd>

**Remote Access** works in the other direction from [remote environments](/kepler/remote-environments). It opens this Kepler window from another device, such as a second computer or a phone, through your GitKraken account. Your work still runs here; the other device only sees the interface.

Configure it in **Settings → Remote Access**, or from the **Remote Access** button in the title bar. The button's monitor-and-phone icon shows the status: green while active, amber while connecting, reconnecting, or waiting to reconnect, red on an error, and plain while off. Hover over it to open its popover, which works on the machine the window is on:

- **Use this machine anywhere**, or **Use *machine* anywhere** in a remote window, with how many devices are paired and online, or *No paired devices yet*.
- While active, a QR code captioned *Scan with your phone's camera to open this machine*, the link with **Copy link**, and *Works in any browser signed in to your GitKraken account.*
- **Turn on Remote Access** or **Turn off Remote Access**.
- **Manage Remote Access…**, which opens **Settings → Remote Access**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-access-popover-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-access-popover-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Remote Access popover open under the title bar's Remote Access button: Remote Access with an Active badge, Use this machine anywhere, No paired devices yet, a QR code captioned Scan with your phone's camera to open this machine, the gitkraken.dev/integrations?connect= link with Copy link, Works in any browser signed in to your GitKraken account, Turn off Remote Access, and Manage Remote Access….">
  </a>
  <figcaption style="text-align:center; color:#888">The Remote Access popover, with Remote Access on.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-access-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-access-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Remote Access while it is off: the Inactive badge and Turn on Remote Access, Your agents, wherever you are, the three steps of How it works, a note that only you can connect, Machines on your account with Manage machines on gitkraken.dev, and This machine stays awake while Remote Access is on, with Change in General.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings → Remote Access, before you turn it on.</figcaption>
</figure>

## Before you start

You need a GitKraken account signed in to Kepler, on a paid GitKraken plan. Remote Access is not available on the free Community plan.

When you sign out of Kepler, each remote machine your windows are connected to learns that you signed out, and turns its Remote Access off. A sign-in that expires on its own does not turn Remote Access off.

## Turning on Remote Access

1. Open **Settings → Remote Access**.
2. Click **Turn on Remote Access**.
3. In **Name this machine**, keep the name Kepler fills in, or enter a name you recognize. gitkraken.dev shows this name in your list of machines.

**Remote Access stays on until you turn it off.** Only you, a deliberate sign-out, or a different account signing in turns it off. When Kepler restarts, it turns Remote Access back on only for the account that turned it on. When the connection fails, Kepler retries quickly a few times. After that, the status reads **Waiting to reconnect**, with *Unable to connect* and the reason. *Kepler retries every 5 minutes.*, and **Retry now** tries at once. Paired devices stay paired through the wait. Remote Access also waits in these 2 cases:

- With no GitKraken sign-in, the status reads *Waiting for a GitKraken sign-in. Remote Access connects as soon as one is available.*
- When your account already has its limit of machines with Remote Access on, the status reads *Your account has reached its limit of machines with Remote Access on. Remove one you no longer use, then retry.*, with **Manage machines on gitkraken.dev**.

This machine stays awake while Remote Access is on, except while it waits to reconnect.

To turn it off, click **Turn off Remote Access** in Settings or in the popover. Kepler asks **Turn off Remote Access?**, because *Every paired device is disconnected.*

## Pairing another device

When Remote Access is active, a QR code and a link appear in Settings and in the popover.

- To pair a phone, scan the QR code (**Scan with your phone camera to open**). Otherwise, copy the link.
- The link opens **gitkraken.dev/integrations**, where you approve the connection with your GitKraken account.

A pairing link works once and expires after 5 minutes. A used or expired link shows *This pairing link no longer works*. To pair, open a new link from the computer running Kepler.

You can bookmark the address a paired browser opens on. If that browser's connection has ended, opening the address again takes you to gitkraken.dev to sign in and pair it again.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-access-phone-sep-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-access-phone-sep-2026-v3@2x.png" class="help-center-img img-bordered" alt="Kepler's Dashboard in a phone's browser, on the Tasks view: one bar with Menu, the view picker showing Tasks with a chevron and an orange dot, Search, Options and New task, over the task list grouped into Needs attention (Add product search, In Development, Approval needed), Unread (Fix the cart total, In Review with its pull request and issue chips and Changes requested; Update checkout copy, On Hold, and Upgrade the payment SDK, In Review, each with New reply) and a folded Not started (1).">
  </a>
  <figcaption style="text-align:center; color:#888">Once paired, a phone opens this Kepler in its browser, in the phone layout.</figcaption>
</figure>

## Using Kepler on a phone

When you open Kepler in a phone's browser, it uses a phone layout: one bar at the top of each screen in place of the desktop top bar and headers. The phone layout applies to any browser window as narrow as a phone; the desktop app never uses it. On a touch screen, Kepler also keeps the phone awake while you watch an agent that is working without needing you, or a terminal that is printing output, because a phone that locks drops the connection. When the on-screen keyboard is open, Kepler fits the screen above it.

### The menu

**Menu**, the first button in the bar, opens the **Kepler** drawer:

- **Views**: your Dashboard views, each with its count. Tap a view to show it, or press and hold it for its menu
- **Recent tasks**: the 5 most recently active tasks, each with a dot when it is waiting on you
- **Feedback**, **Settings**, and **Help**
- Your account row, with your plan or the days left in a trial

<figure style="text-align:center">
  <a href="/wp-content/uploads/phone-drawer-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/phone-drawer-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The phone menu open over the Dashboard: Kepler with Close at the top, then Views listing Todo (type Todo, highlighted as the current view), Tasks (type Tasks) and Agent Graph (type Tasks), the last two with an orange needs-you mark on their icons. Recent tasks lists Fix the cart total, Add product search, Update checkout copy, Upgrade the payment SDK and Write the 2.4 release notes with their status dots, above the Feedback, Settings and Help buttons and Alex Lee (Enterprise).">
  </a>
  <figcaption style="text-align:center; color:#888">The phone menu, listing your Dashboard views.</figcaption>
</figure>

### The Dashboard

The Dashboard's bar holds **Menu**, a view picker, **Search**, **Options**, and **New task**. The view picker switches between your Dashboard views and has **New view**. **Search** expands in the bar. **Options** opens a sheet with **Refresh** and the view's settings, such as its grouping, sort and filters.

<figure style="text-align:center">
  <a href="/wp-content/uploads/phone-dashboard-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/phone-dashboard-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Kepler's Dashboard in a phone-width browser: one bar with Menu, the view picker showing the Todo view with a chevron and an orange dot, Search, Options and New task, above the Todo list grouped into PR (two pull requests marked Changes requested, #51 with a Task badge) and Issue (three issues, one marked Mentioned and #38 with a Task badge) for acme-web.">
  </a>
  <figcaption style="text-align:center; color:#888">The Dashboard's one bar on a phone, over the Todo list.</figcaption>
</figure>

Tapping an item opens it full screen, with a **Back to list** arrow at the left of the bar. A pull request or issue shows its title as a chip in the bar, with its own actions beside it. Tap the title to open **Switch item**, a sheet that lists every pull request and issue in your Todo list, in the same groups and order, with the current one checked. Tap another to open it in place.

<figure style="text-align:center">
  <a href="/wp-content/uploads/phone-dashboard-switch-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/phone-dashboard-switch-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A pull request open full screen in a phone-width browser, dimmed behind the Switch item sheet. The bar above shows Back and the title chip for #51 Apply discounts before tax in the cart total. The sheet repeats the title with Open and More actions and lists the Todo items in their groups: PR with #51 checked and #49, and Issue with #42, #38 and #45.">
  </a>
  <figcaption style="text-align:center; color:#888">Switching to another Todo item without going back to the list.</figcaption>
</figure>

### A task

A task's bar has **Back**, the task's name, and one icon each for **Sessions**, **Changes**, **Terminal**, and **Resources**. A dot on **Back** means another task needs you.

- **Tap an icon** to go to what is waiting there first, or else the last thing you had open. Its list offers each row, an action to add one (**New session**, **New terminal**, or **Add resource**), and **Show everything in this task**.
- **Tap the task's name** to open **Switch task**, a sheet of every task in the Dashboard's order. Swipe sideways on the name to go back to the previous task.
- **Pull down on the bar** for a sheet of everything in the task: sessions, checkouts, terminals, and resources, with each row's actions.

Under the bar, a details row shows the task's stage and a summary. Expand it to see the checkout and the task's pull request and issue. The row collapses while a terminal or the changes fill the screen.

**Add resource** opens as a sheet that lists the kinds of resource, and steps into one at a time, with **Back to resource types** to step out. Each kind lists what the task already holds, with that kind's add control, such as **Add issues**, and **Select** to archive or remove several at once. Each item is added as soon as you pick it.

**Changes** opens with one bar: **Close**, the file's name, and **Previous** and **Next**. Tap the name for the list of changed files. Everything else, from which changes to show to saving an edit, is in the bar's overflow menu.

### Terminals

On a touch phone, every live terminal has a key row under it with the keys a phone keyboard lacks: **Esc**, **Ctrl**, **Tab**, the arrows, **Enter**, **Keyboard**, which shows or hides the phone keyboard, and **Hide keys**. Swipe up on a key, or hold **Esc**, **Tab**, or **Enter**, for the second action printed above it:

| Key | Second action |
|---|---|
| **Esc** | **Ctrl+C** |
| **Tab** | **Shift+Tab** |
| **Enter** | **New line** |
| Left and Right arrows | **Home** and **End** |
| Up and Down arrows | **Page up** and **Page down** |

Tap **Ctrl** once to hold it for the next key only, or double-tap it to lock it until you tap it again. Holding an arrow repeats it. **Hide keys** replaces the row with a **Show keys** button, and this device remembers the choice. The phone keyboard opens only when you tap the terminal or **Keyboard**, not on every scroll.

<figure style="text-align:center">
  <a href="/wp-content/uploads/terminal-key-row-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/terminal-key-row-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task terminal in a phone-width browser after git status, with the terminal key row under it: Esc (Ctrl+C above it), Ctrl, Tab, the Left and Right arrows (Home and End above), Up and Down (PgUp and PgDn above), Enter, Keyboard, and the Hide keys chevron.">
  </a>
  <figcaption style="text-align:center; color:#888">The key row under a terminal on a phone.</figcaption>
</figure>

To select text, long-press a word, and drag before you lift to extend the selection. A pill offers **Open** when you pressed a link or a file path, plus **Copy**, **Paste**, and **Select all**. A long press on blank space offers **Paste** and **Select all**. In a program that tracks the mouse, such as a menu in an agent's terminal app, a tap clicks.

<figure style="text-align:center">
  <a href="/wp-content/uploads/terminal-touch-select-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/terminal-touch-select-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="A task terminal in a phone-width browser after ls, with cart.js long-pressed: the word is highlighted and a pill under it offers Open, Copy, Paste and Select all. The terminal key row sits at the bottom.">
  </a>
  <figcaption style="text-align:center; color:#888">Text selected with a long press, and its actions.</figcaption>
</figure>

## Managing sessions from gitkraken.dev

Go to **gitkraken.dev → Integrations → Remote Access** to manage every machine with Remote Access turned on, across all your devices.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-access-security-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-access-security-sep-2026.png" class="help-center-img img-bordered" alt="gitkraken.dev Integrations page showing the Remote Access (Beta) section with this machine listed">
  </a>
  <figcaption style="text-align:center; color:#888">gitkraken.dev → Integrations → Remote Access, listing this machine.</figcaption>
</figure>

- Expand a machine to see its active connections.
- Revoke a single connection to sign out one paired device without affecting the others.
- Disable a machine to turn off its Remote Access entirely, from anywhere.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-access-options-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-access-options-sep-2026.png" class="help-center-img img-bordered" alt="Expanded machine card showing each connected device with a Revoke button, and a menu with Disable machine">
  </a>
  <figcaption style="text-align:center; color:#888">Expand a machine to revoke one connection or disable the whole machine.</figcaption>
</figure>

You can also manage the current machine's connections locally, in **Settings → Remote Access → Connected devices**. **Machines on your account**, on the same page even while Remote Access is off, opens the machine list on gitkraken.dev with **Manage machines on gitkraken.dev**, so you can remove machines you no longer use.

---
