---
title: App Settings
description: The app pages of Kepler's Settings, covering General (language, windows, default editor, keeping agents running), Notifications, Appearance (themes, chat, terminal, code, diff view), Voice input, and Keyboard shortcuts.
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
last_verified: 2026-10
llms_include: true
tags: [settings, language, windows, default-editor, keep-awake, notifications, appearance, themes, voice-input, keyboard-shortcuts]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

The third group of the Settings rail holds the pages about how Kepler itself behaves. This page covers all five, in rail order:

- [General](#general): language, windows, the default editor, and keeping agents running
- [Notifications](#notifications): which agent events notify you, on the desktop and in Kepler
- [Appearance](#appearance): light or dark appearance and themes, the chat, the terminal font, code font size, and diff layout
- [Voice input](#voice-input): on-device speech-to-text, its transcription engine, and learned words
- [Keyboard shortcuts](#keyboard-shortcuts): Kepler's keyboard shortcuts

***

## General

The General page has four sections: **Language**, **Windows**, **Default editor**, and **Keep agents running**.

### Language

**Language** has one setting:

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Language** | The display language for Kepler's interface | English | English, Español |

The choice also applies to native dialogs, not only the in-app interface.

### Windows

This section holds this machine's window preferences:

| Setting | What it controls | Default |
|---|---|---|
| **Restore windows on launch** | *Reopens the windows you had open, with their size, page and connection. Turn off to start with one window.* | On |
| **Always use the custom folder picker** | Local windows open your system's folder dialog, and windows connected to another machine use Kepler's own folder picker, which can browse that machine. Turn this on to use Kepler's picker in every window | Off |

Kepler reads **Restore windows on launch** during cold start, so a change takes effect on the next launch.

### Default editor

**Default editor** has one setting:

| Setting | What it controls | Default |
|---|---|---|
| **Open files and folders in** | The app that **Open in** and **⌘ ⇧**-click (**Ctrl + Shift**-click on Windows and Linux) on a file link use. The options are **Last used app**, each editor Kepler finds on this machine, and your system's default app | Last used app |

With your system's default app, files open without line numbers, folders open in Finder, Explorer, or your file manager, and programs open in your last used editor. If no editor can be opened from the window you're in, the setting reads *No editors can be opened from this window*.

### Keep agents running

This section keeps agent work alive when the machine would otherwise stop it. It applies to the machine the agents run on, which on a remote connection is that machine:

| Setting | What it controls | Default |
|---|---|---|
| **Keep this machine awake while agents work** | Blocks sleep and standby while an agent session is starting, running, or waiting for your input, and while Remote Access is on, except while it's waiting to reconnect, because sleeping would drop the connection. The screen can still turn off | On |
| **Keep agents and terminals running across restarts and updates** | *Agent sessions and terminals stay alive while Kepler restarts or updates, and reconnect afterwards. Experimental.* | On |

Kepler holds the machine awake through the platform's own mechanism: `caffeinate` on macOS, an execution-state assertion on Windows, and `systemd-inhibit` on Linux. Where that isn't possible, the setting says so under the switch. For example, it reads *Can't stay awake: there is no sleep-blocking mechanism available on this platform.* On Linux, it can say that the system's polkit policy is refusing the request, with a rule an administrator can install. The setting counts Claude Code sessions detected outside Kepler alongside Kepler's own. Kepler releases the machine as soon as the last such session settles.

**Keep agents and terminals running across restarts and updates** applies from the next session you start. With it on, a ready update's popover says *Running agents and open terminals keep going through the restart.* On a build that doesn't include the runtime it needs, the switch shows off, is disabled, and says so: *This build can't keep agents running across restarts.*

***

***

## Notifications

*Choose how Kepler tells you what your agents are doing. Desktop notifications show while Kepler is in the background, In Kepler alerts while you're using it. Sessions started outside Kepler notify only once they're on a task.*

The Notifications page has one section, **What to notify you about**. Its settings are saved on this machine.

### What to notify you about

The section is a grid. Each row is an event, and each column is a place Kepler can notify you: **Desktop** or **In Kepler**. The following table lists the events and their defaults in the desktop app:

| Event | When it fires | Desktop | In Kepler |
|---|---|---|---|
| **Replies** | *An agent finished replying and it's your turn.* | Off | Off |
| **Questions** | *An agent asks you something and waits for your answer.* | On | On |
| **Permission requests** | *An agent wants permission to do something.* | On | On |
| **Approval requests** | *An agent asks to do something in Kepler only you can approve, like deleting a worktree or rewriting a branch.* See [Approvals](/kepler/settings-agents#approvals) | On | On |
| **Errors** | *A session stops because something went wrong.* | On | On |

In a browser connected to Kepler, every **Desktop** box starts off. **Replies** stays off on the desktop unless you turned on system notifications in an earlier version of Kepler. Until you set **Approval requests** yourself, it follows **Permission requests**. When you turn on the first **Desktop** box, Kepler sends a sample notification so your OS asks for permission.

After your first session starts, the desktop app sends one notification to say *Notifications are on*: *Kepler will notify you here when an agent needs you. Change this in Settings › Notifications.* Clicking it opens this page. Kepler skips it if every **Desktop** box is off.

Two more settings sit under the grid:

| Setting | What it controls | Default |
|---|---|---|
| **Play a sound with desktop notifications** | Whether a desktop notification makes the OS notification sound | On |
| **Notify even for the task you're looking at** | *Otherwise Kepler stays quiet about the task open in the window you're using.* | Off |

To silence desktop notifications from one remote machine only, use **Mute notifications from {host}** on that machine in [Remote environments](/kepler/settings-environment#remote-environments).

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-settings-notifications-01-01-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-settings-notifications-01-01-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Notifications, What to notify you about, at the desktop app's defaults: a grid of Replies, Questions, Permission requests, Approval requests and Errors against Desktop and In Kepler, with every box ticked except both Replies boxes; below it Play a sound with desktop notifications is ticked and Notify even for the task you're looking at is not.">
  </a>
  <figcaption style="text-align:center; color:#888">What to notify you about, at the desktop app's defaults.</figcaption>
</figure>

***

***

## Appearance

The Appearance page has five sections: **Theme**, **Chat**, **Terminal**, **Code**, and **Diff view**. Its settings are saved on this machine.

### Theme

The **Theme** section has two parts: **Appearance**, which picks whether Kepler looks light or dark, and **Theme**, which picks the colors for each. Themes color the whole app, including code views, diffs, syntax, chat code blocks, and terminals.

**Appearance** has three options:

| Option | What it does |
|---|---|
| **System** | *Follows your system.* Kepler uses your dark theme when your OS is dark and your light theme when it's light, and switches when the OS does. **The default** |
| **Light** | *Always uses a light theme* |
| **Dark** | *Always uses a dark theme* |

Under **Theme**, each theme is a tile. The **Kepler** group holds the built-in themes:

- **Kepler**, which has a dark and a light version. It's the theme a fresh install uses for both.
- **Midnight**, a near-black theme that has only a dark version.

How you pick a tile depends on **Appearance**:

- On **System**, each tile has a moon and a sun. Click the moon to *Use {name} when your system is dark*, or the sun to *Use {name} when your system is light*. Click the tile itself to *Use {name} for both dark and light*.
- On **Light** or **Dark**, click a tile to use it for that appearance.

The tile in use reads **In use now**. If you used **Midnight** in an earlier version of Kepler, Kepler switches **Appearance** to **Dark** and keeps **Midnight** as your dark theme.

<figure style="text-align:center">
  <a href="/wp-content/uploads/appearance-theme-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/appearance-theme-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Theme section of Settings › Appearance at its defaults: Appearance set to System (Follows your system), and under Theme the Kepler tile in use, its preview split between dark and light with a moon and a sun under it, Midnight with a moon, and Your themes with Browse gallery and Create a theme.">
  </a>
  <figcaption style="text-align:center; color:#888">Appearance and Theme, at their defaults.</figcaption>
</figure>

Terminals follow the theme too. A terminal program that asks, such as an agent's own command-line app, is told the terminal's background color as it starts, so it draws a palette that suits the theme you're on. One that asks to follow theme changes is redrawn when you switch, while it runs.

#### Your themes

**Your themes** lists the themes you've added, with two more tiles, **Browse gallery** and **Create a theme**. **Open themes folder**, beside the heading, opens the folder they live in, `~/.kepler/themes`.

A theme file is a `.json` or `.jsonc` file, so comments are allowed. One file can hold a family of up to 8 themes, such as a dark and a light version. Each theme has an id and a name, and `extends` one of Kepler's base themes, `midnight`, `dark`, or `light`. It then overrides that base's colors, and can add code colors and a `terminal` block. The `terminal` block sets the terminal's background, foreground, cursor, selection, and 16 ANSI colors. Kepler reads up to 64 theme files and reloads a file each time you save it.

A tile whose file Kepler can't fully read shows **Has problems** or **Has warnings**. Click the badge to see what's wrong. A file that isn't valid JSON shows *Line {line}, column {column}: {message}*; a problem with a theme's values names the setting it's in, such as *themes.1.extends*. Below the list, **Create a task to fix it** hands the file to an agent, and in the desktop app **Open file** opens it in your editor, at the error's line when there is one. *Changes apply when you save.* A file with warnings still works. A theme that has errors is left out, and the other themes in its file still load. A tile's **More actions for {name}** menu has **Show in folder** and **Move to Trash** (**Move to Recycle Bin** on Windows).

<figure style="text-align:center">
  <a href="/wp-content/uploads/theme-problems-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/theme-problems-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Your themes in Settings › Appearance with harbor.jsonc's problem badge open: Unable to load 1 theme from harbor.jsonc, because harbor-light has errors that must be fixed while the other themes in the file are not affected. It lists themes.1.extends: Invalid option and Unknown key &quot;accent&quot; was ignored, above Create a task to fix it.">
  </a>
  <figcaption style="text-align:center; color:#888">A theme file's problems, each named by the setting it's in.</figcaption>
</figure>

#### Theme gallery

**Browse gallery** opens the **Theme gallery**: *Themes from the community, each checked for contrast. Try one on Kepler before you install it.* The gallery needs an internet connection. It has the following controls:

- **Search themes**, which matches a theme's name, author, tags, or description.
- **Show**, which filters to **All**, **Dark**, or **Light** themes.
- **Sort:**, with **Featured**, **Newest**, or **Name**.

Click a theme to see its details card, drawn in the theme's own colors. The card shows its author, its dark and light variants, **Version**, **License**, and **Updated**, and any contrast warnings in your version of Kepler. Then choose one of the following:

- **Install** adds the theme to **Your themes** without changing the theme on screen. The button then reads **Use**, or **Use for dark and light** for a theme with both.
- **Try it** closes the gallery and paints the whole window in the theme, so you can open a diff or a terminal to judge it. A bar at the bottom reads **Trying {name}**, with **Use {name}** and **Done**, which returns you to the gallery.

If a theme you already have uses the same id, Kepler asks before it replaces that file, and moves the old file to the Trash. A gallery theme you installed and haven't edited offers **Update to {version}** on its tile when a newer version is published. The gallery's themes come from `gitkraken/kepler-themes` on GitHub, where you can also publish your own.

<figure style="text-align:center">
  <a href="/wp-content/uploads/theme-gallery-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/theme-gallery-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Theme gallery dialog: Search by name, author or color, the All / Dark / Light filter, Sort: Featured and 5 themes, and tiles for Amethyst, Blue Is the New Green, Third Impact, Quiet and Kepler Sky with their authors and a moon or sun for each variant. The selected Amethyst's details card shows Amethyst Dark by Eric Amodio with its description, Version, License and Updated, above Install and Try it.">
  </a>
  <figcaption style="text-align:center; color:#888">The Theme gallery, with one theme's details open.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/theme-gallery-try-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/theme-gallery-try-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Settings › Appearance painted in the Amethyst theme while trying it from the gallery, with the preview bar at the bottom: Trying Amethyst Dark, a Dark / Light switch, Use Amethyst and Done.">
  </a>
  <figcaption style="text-align:center; color:#888">Trying a gallery theme on the whole window before you use it.</figcaption>
</figure>

#### Create a theme

**Create a theme** opens the new task launcher with a prompt already written for an agent, ending in *The theme I want:* for you to describe it. The agent reads and saves themes through Kepler's `theme_get` and `theme_save` tools, so it doesn't need the themes folder attached. Before `theme_save` saves a theme, it checks the file's format and that its colors reach the minimum contrast Kepler requires, and reports any problem back to the agent. **Create a task to fix it**, on a broken theme file, starts the same kind of task with that file's problems listed.

<figure style="text-align:center">
  <a href="/wp-content/uploads/create-a-theme-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/create-a-theme-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The New task launcher opened from Create a theme, its prompt asking the agent to read theme_get, check a draft with theme_save using dryRun, then save it, and ending in The theme I want. Add issue, Add PR and Add context sit above the prompt, and the agent picker, Start and Add repo or folder below it.">
  </a>
  <figcaption style="text-align:center; color:#888">The launcher that Create a theme opens.</figcaption>
</figure>

#### Themes in a remote window

Themes belong to this computer, as your choice of theme does. Every window, including one connected to a remote environment, lists and installs themes in this computer's themes folder and gallery. In a window connected to another machine, the picker adds an **On {host}** group with that machine's themes that this computer doesn't have. Each one offers **Install {name} on this computer**, or **Update {name} from {host}** for a copy you installed from it earlier.

### Chat

This section sets how a session's conversation scrolls and how wide it grows:

| Setting | What it controls | Default |
|---|---|---|
| **Chat auto-scroll** | **Auto-scroll to the end** *keeps the newest output in view. Scroll up to stop.* **Stay on my message** *keeps your message in view. The transcript doesn't scroll on its own.* | Auto-scroll to the end |
| **Conversation width** | *How wide the conversation grows in a wide pane. The message box keeps its width.* **Narrow**, **Wide**, or **Full width** | Narrow |
| **Remember scroll position** | *Return to where you left off when you come back to a session.* | On |

Neither scrolling mode fights you: once you scroll up, the transcript stays where you put it. The conversation stays centered at every width, and an agent's answers span its full width.

<figure style="text-align:center">
  <a href="/wp-content/uploads/appearance-chat-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/appearance-chat-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Chat section of Settings › Appearance: Auto-scroll to the end, Conversation width with Narrow selected beside Wide and Full width, and Remember scroll position ticked.">
  </a>
  <figcaption style="text-align:center; color:#888">The Chat settings, at their defaults.</figcaption>
</figure>

### Terminal

This section controls Kepler's embedded terminals:

| Setting | What it controls | Default |
|---|---|---|
| **Font family** | *Separate fonts with commas. The terminal uses the first one installed on this machine.* | Empty, which falls back to your platform's monospace stack |
| **Font size** | Terminal font size in pixels. Values outside 8–32 are clamped | 13 |
| **Line height** | Vertical spacing between lines, to one decimal place. Values outside 1–2 are clamped | 1.2 |
| **Show the message box under terminal sessions** | *Adds Kepler's message box under an agent's terminal, for attachments and voice. You can also switch it from the terminal's status bar.* | Off |

The greyed text in the **Font family** field (`Fira Code, JetBrains Mono, Menlo`) is an example of the format, not the value in effect. If you name a font Kepler can't find on this machine, the field says so and keeps your text. The terminal falls through to the next name in your list. **Font family** and **Font size** save when you press **Enter** or **Escape**, or leave the field, and show their save status.

#### Embedded terminals

Kepler scopes its terminals to a worktree. Opening one starts a shell in that worktree's folder, so you don't need to `cd` into it, and the shell sources your profile the same way an interactive login shell would. Use **⌘ J** to show and hide the terminal panel, **New terminal** to open another, and **Close terminal** to end one.

Terminals are for the work that sits alongside an agent session: running tests while the agent writes code, checking Git state, or reproducing something the session didn't surface. A terminal starts in one worktree and stays there, so work that spans several repositories is usually easier in a standalone terminal.

### Code

**Code** has one setting:

| Setting | What it controls | Default |
|---|---|---|
| **Font size** | *Size of text in diffs and file views.* A value below 10 or above 24 is clamped, and the field says the size can be 10 to 24 | 13 |

### Diff view

**Diff view** has one setting:

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Diff view** | The layout diffs open in | Stacked | Stacked, Split |

This setting is what the layout starts on. A per-diff **Stacked** / **Split** toggle also sits on the Changes overlay's viewer header, so you can switch a single diff without changing the default. See [Review changes](/kepler/review-changes).

***

***

## Voice input

*Talk to your agents instead of typing. Speech is transcribed on this machine and never leaves it.* The Voice input page has four sections: **Voice input**, **Transcription engine**, **When you stop talking**, and **Learned words**. Its settings are saved on this machine.

### Voice input

The first section has one switch, **Use voice input in the chat prompt**, which shows the microphone in the chat prompt. *Turn this off to pause voice input. The downloaded models stay on this computer.* Installing a model turns it on.

### Transcription engine

*Every engine runs on this computer and nothing you say leaves it. Qwen3-ASR gives better results than Whisper: it reads what you are writing, so it gets developer terms like Jira, rebase or pull request right far more often.* The section offers three engines:

| Engine | What it's best at |
|---|---|
| **Qwen3-ASR 1.7B** | *The most accurate, especially with developer terms and mixed languages. Needs a recent graphics card.* |
| **Qwen3-ASR 0.6B** | *Better than Whisper with technical terms, and lighter on memory. For graphics cards with less memory.* |
| **Whisper** | *Works on any machine, including without a compatible graphics card. Less accurate with technical terms.* |

Both Qwen3-ASR engines need a graphics card with WebGPU. On a new device, Kepler selects the Qwen3-ASR size that suits its graphics card and marks it **Recommended**. It selects Whisper instead when the machine has no WebGPU, or when a Whisper model is already installed. Each card shows its approximate download size. **Download and set up ({size})** installs a Qwen3-ASR model, and the card then reads *Ready on this computer.* Until the engine you selected is downloaded, dictation keeps using one that is. **Remove Qwen3-ASR models** deletes every downloaded Qwen3-ASR model after a confirmation. If you use Whisper, a one-time card suggests **Switch to Qwen3-ASR ({size})**, with **Not now**.

When a newer version of an installed Qwen3-ASR model ships, the card says *A newer version of this model is available. Dictation keeps using the installed one until you update.*, with **Update ({size})**. Kepler also tells you once, in a notification with **Update**.

With a Qwen3-ASR engine, **Dictation language** sets *The language you speak.* **Auto-detect**, the default, picks among your system's preferred languages and the app language, or among all languages when those name fewer than two. Over time it leans toward the languages this device has reliably dictated in. Choose a language to always dictate in it. Whisper ignores this setting.

#### Whisper

With **Whisper** selected, the section continues as a guided sequence. It shows one step at a time, and each step appears only once it can do something:

| Step | What it is |
|---|---|
| **Set up voice input** | *Takes a minute: Kepler checks what this machine can run, then downloads a model.* **Get started** begins setup |
| Hardware check | A one-time measurement of how fast this machine transcribes: *Checking what this machine can run…* It runs once. Later quality changes skip it |
| **Choose transcription quality** | Picks a model, with the check's recommendation marked **Suggested**. **Download and set up** installs it |
| Ready | The installed model and its size on disk, with **Change quality**, **Remove Whisper**, and **Technical details** |

Whisper offers four quality levels:

| Option | What it's best at |
|---|---|
| **Fast** | Short prompts in a quiet room, transcribed almost instantly on any machine. The best place to start |
| **Balanced** | Longer sentences and technical words, still quick on most machines |
| **Accurate** | Accents, names, and background noise. Expect a short pause after speaking on machines without a modern graphics card |
| **Most accurate** | The best quality available, including for languages other than English. Worth it on Apple Silicon or a recent graphics card, and slow on anything older |

Each option shows its approximate download size, calculated for the runtime your hardware check measured, so the number you read before installing is the one you download. Downloads continue if you leave the page, and Kepler notifies you when the model is ready.

Once a Whisper model is installed, these controls manage it:

| Control | What it does |
|---|---|
| **Change quality** | Reopens the quality picker |
| **Remove Whisper** | Removes the Whisper model and frees up its local storage. If Whisper is what dictates, the chat microphone turns off |
| **Technical details** | Shows the model's revision, and the backend and data type it runs on |

### When you stop talking

This section appears once a model is installed. It chooses what happens when you stop recording:

| Option | What it does |
|---|---|
| **Insert the text so you can edit it** | Puts the transcript in the prompt for you to review. The default |
| **Send the prompt** | Sends the prompt automatically |
| **Keep listening, transcribing each phrase as you pause** | Keeps the microphone open and transcribes each phrase as you pause |

### Learned words

*Qwen3-ASR learns the spelling of words you fix in dictated text before sending, one word at a time. A word fixed in two sends is suggested, and used once you approve it. Only the words are stored, on this device only, and they are kept after sign-out.*

When a fix becomes a suggestion, a notification says *A dictated word fix is ready to review*, with **Review**, which opens this section. The section has two lists:

- **Suggested words**: *Fixes you made in two sends. Dictation uses a word only after you approve it.* Each word reads **Heard as {heard}**, with **Approve** and **Dismiss**. Kepler never suggests a dismissed fix again.
- **Learned words**: the words dictation uses, each marked **In use** or **Added by you**, with **Remove {term}**. While Qwen3-ASR dictates, **Add a word** adds one yourself.

**Forget learned words** removes every word Qwen3-ASR learned or suggested, and every word you added, on this device, after a confirmation.

Kepler downloads each model from the internet once. Transcription then runs entirely on your device, and your audio is never uploaded. See [Voice Input](/kepler/voice-input).

***

***

## Keyboard shortcuts

*These shortcuts can't be changed yet.* The Keyboard shortcuts page lists Kepler's shortcuts in six sections: **General**, **Navigation**, **Dashboard**, **Task page**, **Chat**, and **Changes and code views**. Kepler also shows each shortcut in the menu items and button tooltips it belongs to. A few tab shortcuts that Settings doesn't list, such as reopening a closed tab and jumping to a tab by position, are in [Task View](/kepler/task-view#keyboard).

Mac symbols are shown first. On Windows and Linux, **⌘** is **Ctrl** and **⌥** is **Alt**, and **⌃** is **Ctrl** on every platform.

### General

The **General** group holds app-wide shortcuts:

| Action | Mac | Windows / Linux |
|---|---|---|
| Open settings | ⌘ , | Ctrl + , |
| Toggle Ask Kepler chat | ⌘ L | Ctrl + L |
| Toggle Ask Kepler terminal | ⌃ ` | Ctrl + ` |
| New task | ⌘ N | Ctrl + N |
| Open quick launcher (global) | ⇧ ⌥ N | Shift + Alt + N |
| New window | ⌘ ⇧ N | Ctrl + Shift + N |
| Quit | None | Ctrl + Q |
| Zoom in | ⌘ = | Ctrl + = |
| Zoom out | ⌘ – | Ctrl + – |
| Reset zoom | ⌘ 0 | Ctrl + 0 |
| Copy the selection or the focused item | ⌘ C | Ctrl + C |
| Close window | ⌘ ⇧ W | Ctrl + Shift + W |
| New session | ⌘ T | Ctrl + T |
| Rename task | F2 | F2 |
| Manage remote environments | ⌘ ⇧ R | Ctrl + Shift + R |
| Open file | ⌘ O | Ctrl + O |
| Go to file | ⌘ P | Ctrl + P |
| Dismiss / Cancel | Escape | Escape |
| Back | ⌘ [ | Alt + ← |
| Forward | ⌘ ] | Alt + → |

### Navigation

The **Navigation** group moves you between tabs and regions:

| Action | Mac | Windows / Linux |
|---|---|---|
| Previous tab | ⌘ ⇧ [ | Ctrl + Shift + [ or Ctrl + PageUp |
| Next tab | ⌘ ⇧ ] | Ctrl + Shift + ] or Ctrl + PageDown |
| Move tab left | ⌘ ⌥ [ | Ctrl + Alt + [ or Ctrl + Shift + PageUp |
| Move tab right | ⌘ ⌥ ] | Ctrl + Alt + ] or Ctrl + Shift + PageDown |
| Close tab or panel | ⌘ W | Ctrl + W or Ctrl + F4 |
| Toggle terminal | ⌘ J | Ctrl + J |
| Next region | F6 | F6 |
| Previous region | ⇧ F6 | Shift + F6 |

### Dashboard

The **Dashboard** group works on the Dashboard's tasks and detail panels:

| Action | Mac | Windows / Linux |
|---|---|---|
| Move panel left | ⌘ ⌥ ⇧ ← | Ctrl + Alt + Shift + ← |
| Move panel right | ⌘ ⌥ ⇧ → | Ctrl + Alt + Shift + → |
| Move panel up | ⌘ ⌥ ⇧ ↑ | Ctrl + Alt + Shift + ↑ |
| Move panel down | ⌘ ⌥ ⇧ ↓ | Ctrl + Alt + Shift + ↓ |
| Move task to the previous Progress stage | ⌘ ⇧ ← | Ctrl + Shift + ← |
| Move task to the next Progress stage | ⌘ ⇧ → | Ctrl + Shift + → |
| Focus detail panel 1–8 | ⌘ 1–8 | Ctrl + 1–8 |
| Focus last detail panel | ⌘ 9 | Ctrl + 9 |
| Switch detail panels | ⌃ Tab | Ctrl + Tab |
| Switch detail panels, oldest first | ⌃ ⇧ Tab | Ctrl + Shift + Tab |
| Maximize detail panel | ⌘ ⇧ M | Ctrl + Shift + M |
| Maximize panel terminals | ⌘ ⇧ J | Ctrl + Shift + J |
| Show or hide changes in detail panel | ⌘ ⇧ G | Ctrl + Shift + G |
| Switch detail panels between columns and grid | ⌘ ⇧ L | Ctrl + Shift + L |
| Show or hide resources in detail panel | ⌘ ⇧ E | Ctrl + Shift + E |
| Find in dashboard | ⌘ F | Ctrl + F |

The earlier **Move panel left** and **Move panel right** keys, **⌘ ⌥ ←** and **⌘ ⌥ →**, still work but aren't listed.

### Task page

The **Task page** group works on a task's page:

| Action | Mac | Windows / Linux |
|---|---|---|
| Focus chat | ⌘ 1 | Ctrl + 1 |
| Focus changes | ⌘ 2 | Ctrl + 2 |
| Focus resources | ⌘ 3 | Ctrl + 3 |
| Switch sessions | ⌃ Tab | Ctrl + Tab |
| Switch sessions, oldest first | ⌃ ⇧ Tab | Ctrl + Shift + Tab |
| Maximize terminal drawer | ⌘ ⇧ J | Ctrl + Shift + J |

### Chat

The **Chat** group works in a session's conversation:

| Action | Mac | Windows / Linux |
|---|---|---|
| Find in conversation | ⌘ F | Ctrl + F |
| Previous message | ⌘ ⌥ ↑ | Ctrl + Alt + ↑ |
| Next message | ⌘ ⌥ ↓ | Ctrl + Alt + ↓ |
| Interrupt & send | ⌘ ⇧ ⏎ | Ctrl + Shift + ⏎ |

### Changes and code views

This section has two lists. The **Changes** list works in the Changes view:

| Action | Mac | Windows / Linux |
|---|---|---|
| Filter changed files | ⌘ P | Ctrl + P |
| Previous file | ⌥ ↑ | Alt + ↑ |
| Next file | ⌥ ↓ | Alt + ↓ |
| Next change | F7 | F7 |
| Previous change | ⇧ F7 | Shift + F7 |
| Show or hide changes panel | ⌘ B | Ctrl + B |
| Open all changes | ⌘ ⇧ A | Ctrl + Shift + A |
| Comment on selection | ⌘ ⇧ C | Ctrl + Shift + C |

The **Code views** list works in any code view, such as a diff or a file you've opened:

| Action | Mac | Windows / Linux |
|---|---|---|
| Find in file or diff | ⌘ F | Ctrl + F |
| Next match | F3 or ⌘ G | F3 |
| Previous match | ⇧ F3 or ⌘ ⇧ G | Shift + F3 |
| Match case | ⌘ ⌥ C | Alt + C |
| Match whole word | ⌘ ⌥ W | Alt + W |
| Use regular expression | ⌘ ⌥ R | Alt + R |

### Shortcuts that depend on where you are

Some keys do different things depending on where you are:

- **⌘ 1**, **⌘ 2**, and **⌘ 3** focus a detail panel on the Dashboard but a column on the task page.
- **⌃ Tab** switches detail panels on the Dashboard and sessions on the task page.
- **⌘ ⇧ J** maximizes the panel's terminals on the Dashboard and the terminal drawer on the task page.
- **⌘ P** filters changed files in the Changes view and opens **Go to file** elsewhere.
- **⌘ F** finds in the Dashboard from its list or header, finds in a file or diff in a code view, and finds in the conversation elsewhere.
- **⌘ ⇧ G** shows or hides changes in a Dashboard detail panel, and, on macOS, moves to the previous match in a code view.
- **⌘ C** copies what a focused row, chip, or link names, such as a task's Kepler link, a pull request or issue link, a file path, or a commit hash, without opening a menu. In a text field, the message box, a terminal, or a text selection, it copies as usual.

Kepler registers **Open quick launcher** with the OS, so it works while Kepler is in the background. Its row carries a **Global** badge. **Quit**, **Ctrl + F4**, and the **PageUp** / **PageDown** tab keys are Windows and Linux shortcuts only. Kepler hides those rows on macOS, which quits through the native **⌘ Q** menu role. **Close tab or panel** works only in the desktop app.

On Windows and Linux, a focused terminal keeps **Ctrl + W** and **Ctrl + L** for the shell. **Ctrl + `** always toggles the Ask Kepler terminal, even from a terminal.

**Back** and **Forward** are split by platform on purpose. **Alt + ←** is the Windows and Linux convention but moves by word on macOS, and **⌘ [** is the macOS convention (Safari, Finder) but not the Windows one. Holding either walks the history.

**Send feedback**, **Show release notes**, **Show About**, **Check for updates**, and **Clean up worktrees** have no default key, so they don't appear in this list. Reach the first four from the app menu.

***

---
