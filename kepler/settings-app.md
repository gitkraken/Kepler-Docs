---
title: App Settings
description: Change how Kepler looks and behaves, including its language, default editor, sessions started outside Kepler, windows, themes, the Dashboard's views, chat and terminal settings, notifications, dictation and read aloud, and keyboard shortcuts.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: []
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [settings, language, send-key, windows, default-editor, external-sessions, notifications, phone-notifications, appearance, themes, chat, terminal, voice, dictation, read-aloud, keyboard-shortcuts]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Use these Settings pages to change how Kepler itself looks and behaves:

- [General](#general): language, the default editor, sessions started outside Kepler, and windows
- [Appearance](#appearance): light or dark appearance and themes, the Dashboard's views, and the code font and diff layout
- [Chat and terminal](#chat-and-terminal): the chat's send key, width, and scrolling, and the terminal's font, message box, and links
- [Notifications](#notifications): which agent events notify you, on the desktop, in Kepler, and on your phone
- [Voice](#voice): a check of your microphone and speaker, dictation with its models and vocabulary, and read aloud
- [Keyboard shortcuts](#keyboard-shortcuts): look up and change Kepler's keyboard shortcuts

***

## General

Use **General** to choose Kepler's language, which editor opens your files, whether Kepler lists agent sessions you start outside it, and how its windows open.

### Language

**Language** has 1 setting:

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Language** | The display language for Kepler's interface | English | English, Español |

The language also applies to Kepler's native dialogs.

### Default editor

**Default editor** has 1 setting:

| Setting | What it controls | Default |
|---|---|---|
| **Open files and folders in** | The app that **Open in** and **Ctrl/⌘ + Shift**-click on a file link use. The options are **Last used app**, each editor Kepler finds on this machine, and your system's default app | Last used app |

With your system's default app, files open without line numbers, and folders open in Finder, Explorer, or your file manager. If Kepler cannot open any editor from the window you are in, the setting says so.

### Sessions outside Kepler

To follow agent sessions you start in your own terminal, use this setting:

| Setting | What it controls | Default |
|---|---|---|
| **Show them in Kepler** | Lists the agent sessions you run without Kepler, such as Claude Code or Codex in your own terminal, so you can read them or continue them in a task | On |

The setting covers every agent Kepler can follow this way. See [Agent Sessions](/kepler/agent-sessions#sessions-started-outside-kepler).

If a running agent session stops reporting to Kepler, every window shows *Agent sessions aren't reporting to Kepler*, with a **Repair** button. **Repair** reinstalls the reporting configuration. Restart any session that still does not report. For another computer's sessions, repair from that computer.

### Windows

These settings set how windows and folder dialogs work on this machine:

| Setting | What it controls | Default |
|---|---|---|
| **Restore windows on launch** | *Reopens the windows you had open, with their size, page and connection. Turn off to start with one window.* | On |
| **Always use Kepler's folder picker** | Local windows open your system's folder dialog, and windows connected to another machine use Kepler's own folder picker, which can browse that machine. Turn this on to use Kepler's picker in every window | Off |

A change to **Restore windows on launch** takes effect the next time you start Kepler.

***

## Keep agents running

**Keep agents running** is a section of **Settings → Agents**: see [Keep agents running](/kepler/settings-agents#keep-agents-running).

### Idle agents

**Idle agents** is a section of **Settings → Agents**: see [Idle agents](/kepler/settings-agents#idle-agents).

***

## Appearance

Use **Appearance** to choose light or dark and a theme, and to set up the Dashboard's views, code text, and diffs. Kepler saves these settings on this machine.

### Theme

The **Theme** section has 2 parts: **Appearance**, which picks whether Kepler looks light or dark, and **Theme**, which picks the colors for each. Themes color the whole app, including code views, diffs, syntax, chat code blocks, and terminals.

**Appearance** has 3 options:

| Option | What it does |
|---|---|
| **System** | *Follows your system.* Kepler uses your dark theme when your OS is dark and your light theme when it's light, and switches when the OS does. **The default** |
| **Light** | *Always uses a light theme* |
| **Dark** | *Always uses a dark theme* |

Under **Theme**, each theme is a tile. The **Kepler** group holds the built-in themes:

- **Kepler**, which has a dark and a light version. It's the theme a fresh install uses for both.
- **Midnight**, a near-black theme that has only a dark version.

How you pick a tile depends on **Appearance**:

- On **System**, each tile has a moon and a sun. Click the moon to use the theme when your system is dark, or the sun to use it when your system is light. Click the tile itself to use it for both.
- On **Light** or **Dark**, click a tile to use it for that appearance.

The tile in use reads **In use now**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/appearance-theme-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/appearance-theme-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Theme section of Settings › Appearance at its defaults: Appearance set to System (Follows your system), and under Theme the Kepler tile in use, its preview split between dark and light with a moon and a sun under it, Midnight with a moon, and Your themes with Browse gallery and Create a theme.">
  </a>
  <figcaption style="text-align:center; color:#888">Appearance and Theme, at their defaults.</figcaption>
</figure>

Agent CLIs and other terminal programs that support it match your theme too.

#### Your themes

**Your themes** lists the themes you have added, with 2 more tiles, **Browse gallery** and **Create a theme**. **Open themes folder**, beside the heading, opens the folder that holds your themes, `~/.kepler/themes`. Each [profile](/kepler/kepler-profiles) other than the default keeps its own themes folder.

A theme file follows these rules:

- It is a `.json` or `.jsonc` file, so comments are allowed.
- A single file can hold a family of up to 8 themes, such as a dark and a light version.
- Each theme has an id and a name, and `extends` one of Kepler's base themes: `midnight`, `dark`, or `light`. The theme then overrides that base's colors, and can add code colors and a `terminal` block.
- The `terminal` block sets the terminal's background, foreground, cursor, selection, and 16 ANSI colors.

Kepler reads up to 64 theme files, and reloads a file each time you save it.

If Kepler cannot fully read a theme's file, its tile shows **Has problems** or **Has warnings**. To see what is wrong, click the badge. Each problem gives its line and column, or names the setting it is in, such as *themes.1.extends*.

A file with warnings still works. Kepler leaves out a theme that has errors, and still loads the other themes in its file. To fix a file, use one of these options below the list of problems:

- **Create a task to fix it** gives the file to an agent.
- In the desktop app, **Open file** opens the file in your editor, at the error's line when there is one. Changes apply when you save.

A tile's **More actions for *theme*** menu has **Show in folder** and **Move to Trash** (**Move to Recycle Bin** on Windows).

<figure style="text-align:center">
  <a href="/wp-content/uploads/theme-problems-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/theme-problems-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Your themes in Settings › Appearance with harbor.jsonc's problem badge open: Unable to load 1 theme from harbor.jsonc, because harbor-light has errors that must be fixed while the other themes in the file are not affected. It lists themes.1.extends: Invalid option and Unknown key &quot;accent&quot; was ignored, above Create a task to fix it.">
  </a>
  <figcaption style="text-align:center; color:#888">A theme file's problems, each named by the setting it's in.</figcaption>
</figure>

#### Theme gallery

**Browse gallery** opens the **Theme gallery** of community themes, each checked for contrast, which you can try before you install. The gallery needs an internet connection. It has the following controls:

- **Search themes**, which matches a theme's name, author, tags, or description.
- **Show**, which filters to **All**, **Dark**, or **Light** themes.
- **Sort:**, with **Featured**, **Newest**, or **Name**.

Click a theme to see its details card, with its author, its dark and light variants, its version, its license, and any contrast warnings. Then choose one of the following:

- **Install** adds the theme to **Your themes** without changing the theme on screen. The button then reads **Use**.
- **Try it** closes the gallery and paints the whole window in the theme, so you can open a diff or a terminal to judge it. In the bar at the bottom, click **Use *theme***, or **Done** to return to the gallery.

If a theme you already have uses the same id, Kepler asks before it replaces that file, and moves the old file to the Trash. A gallery theme you installed and have not edited offers **Update to *version*** on its tile when a newer version is published. The gallery's themes come from `gitkraken/kepler-themes` on GitHub, where you can also publish your own.

<figure style="text-align:center">
  <a href="/wp-content/uploads/theme-gallery-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/theme-gallery-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Theme gallery dialog: Search by name, author or color, the All / Dark / Light filter, Sort: Featured and 5 themes, and tiles for Amethyst, Blue Is the New Green, Third Impact, Quiet and Kepler Sky with their authors and a moon or sun for each variant. The selected Amethyst's details card shows Amethyst Dark by Eric Amodio with its description, Version, License and Updated, above Install and Try it.">
  </a>
  <figcaption style="text-align:center; color:#888">The Theme gallery, with one theme's details open.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/theme-gallery-try-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/theme-gallery-try-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Appearance painted in the Amethyst theme while trying it from the gallery, with the preview bar at the bottom: Trying Amethyst Dark, a Dark / Light switch, Use Amethyst and Done.">
  </a>
  <figcaption style="text-align:center; color:#888">Trying a gallery theme on the whole window before you use it.</figcaption>
</figure>

#### Create a theme

**Create a theme** opens the **New task** composer with a prompt already written for an agent, ending in *The theme I want:* for you to describe it. You do not need to attach the themes folder: the agent checks the theme's format and contrast, then saves it to **Your themes**. **Create a task to fix it**, on a broken theme file, starts the same kind of task with that file's problems listed.

<figure style="text-align:center">
  <a href="/wp-content/uploads/create-a-theme-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/create-a-theme-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The New task composer opened from Create a theme, its prompt asking the agent to read theme_get, check a draft with theme_save using dryRun, then save it, and ending in The theme I want. Add issue, Add PR and Add context sit above the prompt, and the agent picker, Start and Add repo or folder below it.">
  </a>
  <figcaption style="text-align:center; color:#888">The New task composer that Create a theme opens.</figcaption>
</figure>

#### Themes in a remote window

Themes and your choice of theme belong to this computer. Every window lists and installs themes in this computer's themes folder and gallery, including a window connected to a remote environment.

In a window connected to another machine, the picker adds an **On *host*** group with that machine's themes:

- A theme you do not have offers **Install *theme* on this computer**.
- A theme that differs from your copy offers to update or replace your copy, and is marked **Update to *version***, **Older than yours**, or **Differs from yours**.

Kepler asks before it updates or replaces your copy, and moves your copy to the Trash (the Recycle Bin on Windows). It never replaces your copy on its own.

### Dashboard

**Dashboard views** sets where the Dashboard's views sit and how they look:

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Views** | Where the Dashboard's views sit in the window | Top | Top, Left |
| **View style** | How views at the top look | Tabs | Tabs, Pills |
| **Size** | How big views along the left side are | Default | Default, Compact |
| **Counts on views** | Shows how many tasks match each view's filters | On | On, Off |

With **Left**, the **Settings** button moves to the bottom of the views.

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-appearance-dashboard-nov-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-appearance-dashboard-nov-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Dashboard views section of Settings › Appearance at its defaults: Views, with picture tiles for Top (chosen) and Left; View style, with Tabs chosen over Pills; Size, Default or Compact, marked Left side only; and Counts on views, ticked. Each row has its help line.">
  </a>
  <figcaption style="text-align:center; color:#888">The Dashboard views settings, at their defaults.</figcaption>
</figure>

### Code

These settings set how diffs and code look:

| Setting | What it controls | Default |
|---|---|---|
| **Diff layout** | The layout diffs open in: **Stacked** or **Split** | Stacked |
| **Font** › **Family** | The font for diffs, file views, and code in chat. Leave it empty to use the terminal's font | Empty |
| **Font** › **Size** | Text size in diffs and file views, from 10 to 24 | 13 |

To switch a single diff without changing the default, use the layout button on the file's header in the Changes overlay. See [Review What a Coding Agent Changed](/kepler/review-changes).

***

## Chat and terminal

Use **Chat and terminal** to set how a session's chat and terminal views look and behave. Kepler saves these settings on this machine. The top of the page shows which mode new sessions start in. To change it, click **Change in Agents**.

### Chat

**Send messages with** chooses the key that sends a message from the chat box: **Enter**, the default, or **Ctrl/⌘ + Enter**. With **Enter**, **Shift + Enter** starts a new line. With **Ctrl/⌘ + Enter**, **Enter** starts a new line. In the browser on a phone or tablet, **Enter** always starts a new line.

The other **Chat** settings set how wide a session's conversation grows and how it scrolls:

| Setting | What it controls | Default |
|---|---|---|
| **Conversation width** | How wide the conversation grows in a wide pane: **Narrow**, **Wide**, or **Full width** | Narrow |
| **Scrolling** › **While an agent replies** | **Follow new output** keeps the newest output in view until you scroll up. **Stay on my message** keeps your message in view | Follow new output |
| **Scrolling** › **Return to where I left off when I reopen a session** | Whether a session reopens where you left it | On |

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-send-key-nov-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-send-key-nov-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Chat section of Settings › Chat and terminal: Send messages with, set to Enter rather than Ctrl+Enter, with the hints that Shift+Enter starts a new line and that Enter always does in the browser on a phone or tablet; then Conversation width, with Narrow chosen over Wide and Full width, and Scrolling, with While an agent replies set to Follow new output and Return to where I left off when I reopen a session ticked.">
  </a>
  <figcaption style="text-align:center; color:#888">The Chat settings, at their defaults.</figcaption>
</figure>

### Terminal

These settings control Kepler's embedded terminals:

| Setting | What it controls | Default |
|---|---|---|
| **Font** › **Family** | *Separate fonts with commas. The terminal uses the first one installed on this machine.* | Empty, which uses your platform's standard monospace fonts |
| **Font** › **Size** | Terminal font size in pixels, from 8 to 32 | 13 |
| **Font** › **Line height** | Spacing between lines, from 1 to 2 | 1.2 |
| **Show the message box under terminal sessions** | Adds Kepler's message box, for attachments and voice, under an agent's terminal | Off |
| **Open links with a click** | Opens file, folder, and web links in a terminal without holding **Ctrl/⌘** | Off |

The grayed text in **Family** is an example, not the value in effect. If Kepler cannot find a font you name, the field says so, and the terminal uses the next name in your list. **Family** and **Size** save when you press **Enter** or leave the field. Code views use this family too, unless you set one under [Code](#code).

While the message box is hidden, a Terminal session's status bar has a microphone that dictates into the agent's own input. See [Dictation](#dictation).

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-terminal-links-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-terminal-links-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Terminal section of Settings › Chat and terminal: Font family, Size 13 and Line height 1.2 above a sample terminal, then Show the message box under terminal sessions and Open links with a click, both unticked. The help under Open links with a click says it opens file, folder and web links in terminals without holding Ctrl.">
  </a>
  <figcaption style="text-align:center; color:#888">The Terminal settings, at their defaults.</figcaption>
</figure>

#### Embedded terminals

Each Kepler terminal belongs to a worktree. Opening a terminal starts a shell in that worktree's folder, so you do not need to `cd` into it, and the shell loads your profile the same way an interactive login shell would. Use **Ctrl/⌘ + J** to show and hide the terminal panel, **New terminal** to open another terminal, and **Close terminal** to end one.

Use terminals for work next to an agent session: running tests while the agent writes code, checking Git state, or reproducing something the session did not show. A terminal starts in one worktree and stays there, so for work that spans several repositories, use a standalone terminal.

***

## Notifications

Use **Notifications** to choose which agent events Kepler tells you about, and where. **Desktop** notifications show while Kepler is in the background, and **In Kepler** alerts show while you are using it. A phone you open Kepler on can notify you too. Sessions started outside Kepler notify you only once they are on a task. Kepler saves these settings on this machine.

### What to notify you about

**What to notify you about** has a **Desktop** and an **In Kepler** box for each event. The following table lists the events and their defaults in the desktop app:

| Event | When it fires | Desktop | In Kepler |
|---|---|---|---|
| **Replies** | *An agent finished replying and it's your turn.* | Off | Off |
| **Questions** | *An agent asks you something and waits for your answer.* Also fires when a plan is ready for your review | On | On |
| **Permission requests** | *An agent wants permission to do something.* | On | On |
| **Approval requests** | *An agent asks to do something in Kepler only you can approve, like deleting a worktree or rewriting a branch.* See [Settings → Approvals](/kepler/settings-approvals) | On | On |
| **Errors** | *A session stops because something went wrong.* | On | On |
| **Usage limits** | *When an agent reaches an account's usage limit.* | On | On |
| **Offers** | *An agent offers to show you a task, session or note.* | Off | On |

In a browser connected to Kepler, every **Desktop** box starts off. Until you set **Approval requests** yourself, it follows **Permission requests**, and **Usage limits** follows **Errors** the same way. When you turn on the first **Desktop** box, Kepler sends a sample notification so your OS asks for permission. Once a phone has notifications turned on, the grid adds a **Phone** column.

These settings appear under the grid:

| Setting | What it controls | Default |
|---|---|---|
| **Play a sound with desktop notifications** | Whether a desktop notification makes the OS notification sound | On |
| **Notify even for the task you're looking at** | *Otherwise Kepler stays quiet about the task open in the window you're using.* | Off |
| **Show a count on the app icon** | *Shows how many tasks need you on the Dock icon or taskbar button.* Desktop app only | On |

To silence desktop notifications from one remote machine only, use **Mute notifications from *host*** on that machine in [Remote environments](/kepler/settings-environment#remote-environments).

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-settings-notifications-01-01-v5@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-settings-notifications-01-01-v5@2x.png" class="help-center-img img-bordered" alt="Settings › Notifications, What to notify you about, at the desktop app's defaults: Replies, Questions, Permission requests, Approval requests, Errors, Usage limits and Offers against Desktop and In Kepler, with every box ticked except both Replies boxes and Offers' Desktop box. Below the grid, Play a sound with desktop notifications and Show a count on the app icon are ticked, and Notify even for the task you're looking at is not.">
  </a>
  <figcaption style="text-align:center; color:#888">What to notify you about, at the desktop app's defaults.</figcaption>
</figure>

### Notifications on this phone

When you open Kepler on your phone through [Remote Access](/kepler/settings-environment#remote-access), its **Settings → Notifications** page adds **Notifications on this phone**. Turn on **Notify this phone**, and Kepler notifies the phone when a session needs you and you're away from your computer. To check that notifications arrive, tap **Send a test**.

Phone notifications need the Remote Access link. On an iPhone, add Kepler to your Home Screen from Safari's **Share** menu first, then turn notifications on from the Home Screen app. See [Approve Coding Agent Requests from Your Phone](/kepler/kepler-approve-agent-requests-from-your-phone).

***

## Voice

Use **Voice** to talk to your agents instead of typing, and to have their replies read aloud. Both run on this machine, so nothing you say or hear leaves it. Kepler saves these settings on this machine.

### Check your setup

**Check your setup** tests your devices with the speech model and voice picked on the page:

- Pick the **Microphone** dictation listens to, then click **Try dictation** to see your words as you speak.
- Pick the **Speaker** that Kokoro reads replies on, then click **Play a reply**.

Nothing you say in the test is sent to an agent. Each device you pick is saved for this window. If it is not connected later, Kepler uses the system default and tells you.

### Dictation

Dictation is the microphone in the chat prompt, and on a Terminal session's status bar. It turns on once a speech model is downloaded. To choose and download one, see [Set up dictation in Settings](/kepler/voice-input#set-up-dictation-in-settings).

| Setting | What it controls | Default |
|---|---|---|
| **Speech model** | The on-device model that dictates: **Qwen3-ASR 1.7B**, **Qwen3-ASR 0.6B**, **Parakeet TDT 0.6B v3**, or **Whisper**. Each row has **Download**, and **Remove…** once downloaded | None until you download one |
| **Dictation language** | With Qwen3-ASR, the language you speak. Parakeet detects it, and Whisper ignores it | Auto-detect |
| **Dictation mode** | **Type as you talk**, **Type when you stop**, or **Send when you stop** | Type as you talk |
| **Vocabulary** | The words dictation learned from your fixes, which **Manage** opens, with Qwen3-ASR only. See [Teach dictation your words](/kepler/voice-input#teach-dictation-your-words) | No words yet |

**Parakeet TDT 0.6B v3** understands English and 24 other European languages. Kepler offers it only on a graphics card with WebGPU and 16-bit float shader support.

To change the speech model, the dictation mode, or the dictation language from a Terminal session, right-click the microphone on its status bar.

### Read aloud

**Read aloud** reads agent replies to you from the chat, the terminal, or the title bar. To use it, see [Read aloud](/kepler/voice-input#read-aloud).

| Setting | What it controls | Default |
|---|---|---|
| **Speech model** | **System**, or **Kokoro**, natural English voices that need a download | System |
| **Voice** | The voice that reads | System default |
| **Speed** | How fast Kepler reads | 1x |

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-read-aloud-nov-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-read-aloud-nov-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Read aloud section of Settings › Voice at its defaults. Under Speech model, System (Built in) is picked and Kokoro (310 MB) offers Download and Licenses; Voice reads System default beside a play-sample button, and Speed is a slider at 1x between 0.5x and 2x.">
  </a>
  <figcaption style="text-align:center; color:#888">The Read aloud settings, at their defaults.</figcaption>
</figure>

***

## Keyboard shortcuts

Use **Keyboard shortcuts** to look up Kepler's shortcuts and choose your own keys. The page lists every command in 6 groups: **General**, **Navigation**, **Dashboard**, **Task page**, **Chat**, and **Changes and code views**. A command without a key shows **None**. Menu items and button tooltips show each command's keys, including the ones you set. For a few tab shortcuts that Settings does not list, such as reopening a closed tab and jumping to a tab by position, see [Task View](/kepler/task-view#keyboard).

### Change a shortcut

1. Find the command, or type its name in **Search shortcuts**.
2. Click the pencil (**Change shortcut**) on its row. If the command already has a key, a menu opens: choose **Change shortcut**, **Add another shortcut**, or **Remove** followed by the key.
3. Press the new keys. **Escape** cancels, and **Backspace** removes the shortcut.

You can also start from the command palette: a command's **Change shortcut** action opens this page at that command, ready for the new keys.

If the keys already belong to another command, Kepler names it, and **Replace** moves the keys to this command. Kepler refuses keys it needs elsewhere, such as the key that sends chat messages, and says why.

A changed row offers **Reset to default**. **Changed only** lists only the shortcuts you changed, and **Reset all shortcuts** puts every shortcut back to its default after you confirm. A row with a lock, such as **Copy the selection or the focused item** or **Dismiss / Cancel**, cannot be changed.

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-shortcuts-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-shortcuts-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="Settings › Keyboard shortcuts, under its description, with new task typed in Search shortcuts, beside Changed only, the count 1 of 112 shortcuts, and Reset all shortcuts, dimmed. The General section lists New task with its Ctrl+N key and a pencil button showing the tooltip Change shortcut.">
  </a>
  <figcaption style="text-align:center; color:#888">Searching the shortcuts, with a row's Change shortcut button.</figcaption>
</figure>

### Default shortcuts

The tables list the default keys.

#### General shortcuts

The **General** group holds app-wide shortcuts:

| Action | Shortcut |
|---|---|
| Open settings | Ctrl/⌘ + , |
| Toggle Ask Kepler chat | Ctrl/⌘ + K or Ctrl/⌘ + L |
| Toggle Ask Kepler terminal | Ctrl + ` |
| New Ask Kepler chat | Ctrl/⌘ + Shift + K or Ctrl/⌘ + Shift + L |
| New task | Ctrl/⌘ + N |
| Open quick launcher (global) | Shift + Alt/⌥ + N |
| New window | Ctrl/⌘ + Shift + N |
| Quit | Ctrl/⌘ + Q |
| Zoom in | Ctrl/⌘ + = |
| Zoom out | Ctrl/⌘ + - |
| Reset zoom | Ctrl/⌘ + 0 |
| Toggle full screen | F11, or ⌘ + ⌃ + F on macOS |
| Minimize | Ctrl/⌘ + M |
| Reload | Ctrl/⌘ + R |
| Hide Kepler | ⌘ + H (macOS only) |
| Hide others | ⌘ + ⌥ + H (macOS only) |
| Copy the selection or the focused item | Ctrl/⌘ + C |
| Close window | Ctrl/⌘ + Shift + W |
| Toggle terminal | Ctrl/⌘ + J |
| New session | Ctrl/⌘ + T |
| Rename task | F2 |
| Delete task | Ctrl/⌘ + Shift + Backspace |
| Manage remote environments | Ctrl/⌘ + Shift + R |
| Toggle side panel | Ctrl/⌘ + B |
| Open file | Ctrl/⌘ + O |
| Open folder | Ctrl/⌘ + Shift + O |
| Go to file | Ctrl/⌘ + P |
| Go to task or command | Ctrl/⌘ + Shift + P or F1 |
| Change search scope | Alt + S, or ⌘ + ⌥ + S on macOS |
| Dismiss / Cancel | Escape |

**Go to task or command** and **Open folder** are also in the app menu, as **View › Command Palette…** and **File › Open Folder…**.

#### Navigation shortcuts

The **Navigation** group moves you between tasks, tabs, and regions:

| Action | Shortcut |
|---|---|
| Go to next in Needs attention | None |
| Go to next in Unread | None |
| Go to what needs you next | F8 |
| Previous tab | Ctrl/⌘ + Shift + [, or Ctrl + PageUp on Windows and Linux |
| Next tab | Ctrl/⌘ + Shift + ], or Ctrl + PageDown on Windows and Linux |
| Move tab left | Ctrl/⌘ + Alt/⌥ + [, or Ctrl + Shift + PageUp on Windows and Linux |
| Move tab right | Ctrl/⌘ + Alt/⌥ + ], or Ctrl + Shift + PageDown on Windows and Linux |
| Focus next region | F6 |
| Focus previous region | Shift + F6 |
| Close tab or panel | Ctrl/⌘ + W, or Ctrl + F4 on Windows and Linux |
| Go back | Alt + ←, or ⌘ + [ on macOS |
| Go forward | Alt + →, or ⌘ + ] on macOS |

**Go to next in Needs attention** opens the next session waiting on you, and **Go to next in Unread** opens the next unread reply. **Go to what needs you next** (**F8**) does both, waiting sessions first, and skips what is already on screen. **F8** works even from a focused terminal.

#### Dashboard shortcuts

The **Dashboard** group works on the Dashboard's tasks and detail panels:

| Action | Shortcut |
|---|---|
| Move panel left | Ctrl/⌘ + Alt/⌥ + Shift + ← |
| Move panel right | Ctrl/⌘ + Alt/⌥ + Shift + → |
| Move panel up | Ctrl/⌘ + Alt/⌥ + Shift + ↑ |
| Move panel down | Ctrl/⌘ + Alt/⌥ + Shift + ↓ |
| Move task to the previous Progress stage | Ctrl/⌘ + Shift + ← |
| Move task to the next Progress stage | Ctrl/⌘ + Shift + → |
| Focus detail panel 1 to 8 | Ctrl/⌘ + 1 to Ctrl/⌘ + 8 |
| Focus last detail panel | Ctrl/⌘ + 9 |
| Previous item in list | Alt/⌥ + Shift + ↑ |
| Next item in list | Alt/⌥ + Shift + ↓ |
| Switch to older panel | Ctrl + Shift + Tab |
| Switch to newer panel | Ctrl + Tab |
| Solo detail panel | Ctrl/⌘ + Shift + M |
| Maximize panel terminals | Ctrl/⌘ + Shift + J |
| Toggle changes pane | Ctrl/⌘ + Shift + G |
| Toggle task list peek | Ctrl/⌘ + Shift + B |
| Toggle resources pane | Ctrl/⌘ + Shift + E |
| Find in dashboard | Ctrl/⌘ + F |
| Dashboard: Find from the list | / |
| Dashboard: Your groups | Shift + G |
| Dashboard: Next row | J |
| Dashboard: Previous row | K |
| Dashboard: Open task page | O |
| Dashboard: Star or unstar task | I |
| Dashboard: Mark task read or unread | U |
| Dashboard: Archive or restore task | E |
| Dashboard: Put task on hold or back to automatic | H |
| Dashboard: Set task progress | S |
| Dashboard: Add task to a group or change its group | G |
| Dashboard: Rename task | R |
| Dashboard: Open task actions | . |
| Dashboard: Add task to selection or remove it | X |
| Dashboard: Select tasks up to this one | Shift + X |
| Dashboard: Delete task | Delete or Backspace |

From **Dashboard: Next row** on, the keys act on the focused task row in a Tasks view, or on the selected tasks. **Dashboard: Find from the list** focuses the Dashboard's search. None of the **Dashboard:** keys can be changed.

#### Task page shortcuts

The **Task page** group works on a task's page:

| Action | Shortcut |
|---|---|
| Focus chat | Ctrl/⌘ + 1 |
| Focus changes | Ctrl/⌘ + 2 |
| Focus resources | Ctrl/⌘ + 3 |
| Switch sessions | Ctrl + Tab |
| Switch sessions, oldest first | Ctrl + Shift + Tab |
| Maximize terminal drawer | Ctrl/⌘ + Shift + J |
| Show or hide the preview in Add resources | Ctrl/⌘ + Alt/⌥ + P |

#### Chat shortcuts

The **Chat** group works in a session's conversation:

| Action | Shortcut |
|---|---|
| Find in conversation | Ctrl/⌘ + F |
| Previous message | Ctrl/⌘ + Alt/⌥ + ↑ |
| Next message | Ctrl/⌘ + Alt/⌥ + ↓ |
| Interrupt & send | Ctrl/⌘ + Shift + Enter |
| Send after this turn | Alt/⌥ + Enter |
| Switch between terminal and transcript | Ctrl/⌘ + Shift + X |
| Toggle dictation | Ctrl/⌘ + Shift + Space |
| Read the last reply aloud | None |

**Toggle dictation** starts or stops dictation in the focused session, in its message box or its terminal. **Read the last reply aloud** reads, or stops reading, the focused terminal session's last reply.

#### Changes and code view shortcuts

This group has 2 lists. The **Changes** list works in the Changes view:

| Action | Shortcut |
|---|---|
| Filter changed files | Ctrl/⌘ + P |
| Previous file | Alt/⌥ + ↑ |
| Next file | Alt/⌥ + ↓ |
| Next change | F7 |
| Previous change | Shift + F7 |
| Toggle changes sidebar | Ctrl/⌘ + B |
| Open all changes | Ctrl/⌘ + Shift + A |
| Comment on selection | Ctrl/⌘ + Shift + C |
| Edit working copy | Ctrl/⌘ + E |

The **Code views** list works in any code view, such as a diff or a file you have opened:

| Action | Shortcut |
|---|---|
| Find in file or diff | Ctrl/⌘ + F |
| Next match | F3, or ⌘ + G on macOS |
| Previous match | Shift + F3, or ⌘ + Shift + G on macOS |
| Match case | Alt + C, or ⌘ + ⌥ + C on macOS |
| Match whole word | Alt + W, or ⌘ + ⌥ + W on macOS |
| Use regular expression | Alt + R, or ⌘ + ⌥ + R on macOS |
| Find only in changes | Alt + L, or ⌘ + ⌥ + L on macOS |

### Shortcuts that depend on where you are

Some keys do different things depending on where you are:

- **Ctrl/⌘ + 1**, **Ctrl/⌘ + 2**, and **Ctrl/⌘ + 3** focus a detail panel on the Dashboard but a column on the task page.
- **Ctrl + Tab** switches detail panels on the Dashboard and sessions on the task page.
- **Ctrl/⌘ + Shift + [** and **Ctrl/⌘ + Shift + ]** step through the Dashboard's views on the Dashboard, and through a panel's tabs when the panel or the task page has focus. **Ctrl/⌘ + Alt/⌥ + [** and **Ctrl/⌘ + Alt/⌥ + ]** move the current view or tab.
- **Ctrl/⌘ + Shift + J** maximizes the panel's terminals on the Dashboard and the terminal drawer on the task page.
- **Ctrl/⌘ + B** shows or hides the changes panel in the Changes view. On the Dashboard it docks or hides the task list, and on the task page it docks or hides the context panel.
- **Ctrl/⌘ + P** filters changed files in the Changes view and opens **Go to file** elsewhere.
- **Ctrl/⌘ + F** finds in the Dashboard from its list or header, finds in a file or diff in a code view, and finds in the conversation elsewhere.
- **Ctrl/⌘ + Shift + G** shows or hides changes in a Dashboard detail panel, and, on macOS, moves to the previous match in a code view.
- **Ctrl/⌘ + C** on a focused row, chip, or link copies what it names, such as a task's Kepler link, a pull request link, an issue link, a file path, or a commit hash. In a text field, a terminal, or a text selection, it copies as usual.

**Previous item in list** and **Next item in list** work even while you type in the open panel's chat.

**Open quick launcher** works while Kepler is in the background. Its row has a **Global** badge. **Close tab or panel**, **Toggle full screen**, **Minimize**, and **Reload** work only in the desktop app.

On Windows and Linux, a focused terminal passes **Ctrl + W**, **Ctrl + L**, and **Ctrl + B** to the shell. To toggle the Ask Kepler chat from a terminal, press **Ctrl + K**: the shell does not keep that key. **Ctrl + `** always toggles the Ask Kepler terminal, even from a terminal.

Hold the **Go back** or **Go forward** key to keep moving through your history.

**Send feedback**, **Show release notes**, **Show About Kepler**, **Check for updates**, and **Clean up worktrees** have no default key, nor do commands such as **Open documentation**, **Appearance: Dark**, and **Dashboard layout: Board**. To use one from the keyboard, give it a key on this page.

***

---
