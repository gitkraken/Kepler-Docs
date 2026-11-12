---
title: Remote Environments
description: Run your agents on another machine over SSH or in WSL, switch environments from the title bar, manage machines in Settings, forward an SSH host's ports to this computer, and open this Kepler from another device, including your phone, with Remote Access.
product: Kepler
feature: Remote Environments
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: []
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [remote-environments, ssh, wsl, windows, port-forwarding, settings, remote-access, qr-pairing, gitkraken-dev, diagnostics, notifications]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

A **remote environment** runs your agents, worktrees, and terminals on another machine: a dev server, a cloud VM, or a WSL (Windows Subsystem for Linux) instance on Windows, while you work from this window. Kepler installs itself on the host over SSH (Secure Shell), so you do not need to pre-install anything there.

***

## Two remote features

Kepler has 2 remote features, and they work in opposite directions:

| Feature | Direction | Where it lives |
|---|---|---|
| **Remote environments** | Kepler on your desktop reaches **out** to another machine, and your work runs there | The title-bar chip, and **Settings → Remote environments** |
| **Remote Access** | Another device reaches **in** to this Kepler, and your work stays here | The **Remote Access** button in the title bar, and **Settings → Remote Access** |

Both sit at the right end of the title bar. The **Remote Access** button shows a monitor-and-phone icon.

<figure style="text-align:center">
  <a href="/wp-content/uploads/top-tool-bar-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/top-tool-bar-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The right end of the Kepler top bar: the Local environment chip, the Remote Access button's monitor-and-phone icon in green because Remote Access is on, the Ask button with Kep, Feedback, Settings, and the account avatar.">
  </a>
  <figcaption style="text-align:center; color:#888">The environment chip and the Remote Access button, in a local window.</figcaption>
</figure>

To let another device reach this Kepler, rather than connecting *to* another machine, see [Remote Access](#remote-access-reach-kepler-from-another-device).

<div class="note" markdown="1">

**Remote environments need a paid plan.** Every paid plan except Student includes them, with no limit on how many environments you can add. On other plans, a banner offers a free trial when one is available. If another organization you belong to includes remote environments, the banner names that organization and offers **Switch to organization**. If you have just upgraded, click **Check again** under **Already upgraded?** to reload your plan.

</div>

***

## Switching environments from the title bar

Each window works on one environment at a time, and the title-bar chip shows which one. The chip leads with the environment's type icon, and a green dot on that icon means connected.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-chip-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-chip-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The right end of the title bar in a window connected to dev-server: the environment chip reads dev-server on the host's purple tint, with a green dot on its type icon, followed by the Remote Access button, the Ask button with Kep, Feedback, Settings and the account avatar.">
  </a>
  <figcaption style="text-align:center; color:#888">The chip on a host colored Purple, connected.</figcaption>
</figure>

| Chip | What it means |
|---|---|
| **Local** | This window works on this machine |
| **Connecting to *machine*…**, or the current stage | This window is connecting, or its server is restarting or updating |
| **Reconnecting…** | The connection dropped and Kepler is rebuilding it |
| Host name | Connected. The chip takes the host's [color](#host-details) when you have set one |
| Brand fill with an up-arrow | Connected, and a newer server build is ready for the host |
| Warning triangle | The app and the server disagree on version; the popover says which side to update |
| Radio-tower glyph | This window is [forwarding ports](#port-forwarding) from the host |
| An error headline | The last attempt failed; the host's Settings page keeps the full error |

**Hover over the chip to preview the popover.** To open the whole popover and keep it open, click the chip, or focus it and press **Enter** or **Down Arrow**.

In a browser client, Kepler hides the chip, because a browser client cannot manage connections.

### The popover

Use the popover to see which machine this window is on, switch to another machine, and open Settings to manage your machines.

| Part | What it does |
|---|---|
| Header | The current machine, with its address, latency, and versions, or this window's connection progress or failure |
| Gear (**Machine settings**) | Opens the machine's Settings page |
| **Restart server to update** | Appears when a newer server build is ready. See [Server controls](#server-controls) |
| **Disconnect** | Disconnects this window only. The server keeps its sessions running |
| **Restart server** (circular arrow) | Restarts a connected server when no update is pending. See [Server controls](#server-controls) |
| **Stop server** | Stops the server on the machine until you start it again. Every other window connected to it moves to the [recovery screen](#the-recovery-screen) ([When you stop a server](#when-you-stop-a-server)) |
| Forwarded ports | Lists the ports this window forwards, and opens the host's **Ports** list |
| **Switch to** | Every other saved host, plus **Local** (*Work on this machine*) when this window is on a remote |
| **Found on this machine** | WSL distributions found on this PC, offered for one-click connect while you have no saved hosts |
| **Manage remote environments…** | Opens **Settings → Remote environments**. **⌘ ⇧ R** on macOS, **Ctrl + Shift + R** elsewhere |

The line under **Restart server to update** says what the update will stop. When nothing would stop, the update starts at once. Otherwise, the **Update server?** confirmation names the agents and terminals that stop, or says that the server could not report them.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-update-confirm-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-update-confirm-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Update server? confirmation: Updating restarts the server on dev-server, a warning that Kepler is unable to check what is running on dev-server so agents and open terminals there may stop, and Cancel beside a red Update server button.">
  </a>
  <figcaption style="text-align:center; color:#888">The update confirmation when the server cannot report what is running.</figcaption>
</figure>

If this app is older than the server, the header offers an update for this app instead, and says that sessions on the host keep running.

To move this window to another host, click the host's row under **Switch to**. To open the host in a new window and leave this window where it is, hold **Cmd** (macOS) or **Ctrl** while you click, or click the window icon at the end of the row. A host already open in another window is marked **Connected**. Clicking its row brings that window to the front instead of opening a second connection.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-popover-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-popover-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The popover open under the dev-server chip, whose icon carries a green dot. The header shows dev-server over SSH as alex@dev.acme.example, Connected at 5 ms, the server and app version 0.15.0, and a gear, with Disconnect and the restart and stop server buttons. Below are Switch to with Local (Work on this machine) and its window icon, and Manage remote environments… with its Ctrl+Shift+R shortcut.">
  </a>
  <figcaption style="text-align:center; color:#888">The popover, connected to a host.</figcaption>
</figure>

***

## Windows on a remote host

- **New Window opens on the same host.** **File → New Window** (**⌘ ⇧ N** on macOS, **Ctrl + Shift + N** elsewhere) from a remote window opens a second window on that host. A remote window also offers **File → New Local Window** when you want a local one. A new window that cannot reach the host opens on the [recovery screen](#the-recovery-screen) with the reason.
- **Windows on one host share a connection,** so another window on it opens quickly.
- **A host open in another window shows as connected.** The popover and Settings offer **Show window**, and show its latency, versions, and sessions.
- **The last closed remote window reopens on its host.** With no window open, the dock, the tray, or launching Kepler again reconnects to the host the last window was on. If you close a window that was still waiting on an unreachable host, the next window opens locally. If **Restore windows on launch** is off, Kepler launches locally.
- **A link opens on its machine.** A task or session link copied in a window on a remote machine opens on that machine, in a new window if none is open there. A link copied in a local window opens in the window you used last. If a link cannot open on its machine, it opens on this computer instead, and starts nothing by itself. If the item is not found on that machine, the notice offers **Open on this computer**.

***

## Managing machines in Settings

Use **Settings → Remote environments** to add, connect, edit, and remove machines. In a local window, **Your machines** lists your saved machines. Each row shows the host's type, whether it is connected, and how many windows already use it. From a row, you can do the following:

- To connect this window, click **Connect**.
- To connect in a new window, click the window icon.
- To bring forward a host that is open in another window, click **Show window**, which replaces **Connect** for that host.
- To open the host's page, click the row.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-environments-hosts-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-environments-hosts-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Remote environments: Add machine, Your machines with dev-server (SSH, not connected, alex@dev.acme.example) and Connect, Found on this machine listing build-box and staging-db from the SSH config with Add and hide buttons and Show hidden (1), and Remote windows with the option Always use this app's interface, off.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings → Remote Environments, with a saved host.</figcaption>
</figure>

**Found on this machine** lists machines from your `~/.ssh/config` and WSL distributions you have not saved yet. To save one, click **Add**. If your plan does not include remote environments, **Add** reads **Try free and add** when a trial is available. Otherwise it reads **Upgrade to add**, which opens the plan page and saves nothing. To stop Kepler from offering a machine, click its eye icon to hide it. To bring hidden machines back, click **Show hidden (*N*)**.

### Host details

A host's page has a card of actions at the top:

- **Connect**. To connect in a new window, **Cmd/Ctrl**-click it. While a connection is in progress, the same button cancels it.
- **Show window** and **Connect to *machine* in a new window**, in place of **Connect**, when another window already has the host open.
- **Stop server**.
- **Remove *machine*…**, the red trash icon.

To rename the saved connection, click the pencil beside the name. Renaming changes nothing on the host.

| Group | What it does |
|---|---|
| **Connection** | Edits **Host**, **Port**, **User**, and **Identity file** for SSH, or **Distro** for WSL. Disconnect first: the fields are locked while the host is connected |
| **Color** | Tints the host's chip, its rows, and the top bar of its windows with one of the 12 task-group colors |
| **Mute notifications from *machine*** | Stops desktop notifications for sessions on the machine; alerts still appear inside its windows |
| **Sessions** | Lists the host's live agent sessions; click one to open it. For a host nobody is connected to, **Check** shows what is running there |

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-host-page-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-host-page-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The dev-server machine's page in Settings › Remote environments, not connected: Connect, Stop server, the Connection fields (host dev.acme.example, port 22, user alex, identity file), Color with None selected ahead of twelve swatches (gray, blue, pink, yellow, green, purple, cyan, orange, teal, indigo, brown and red), Mute notifications from dev-server, and Sessions with Check.">
  </a>
  <figcaption style="text-align:center; color:#888">A saved host's page.</figcaption>
</figure>

When you change the address of a host that the SSH wizard created, Kepler first fetches the new address's host key and shows it under **New host key**. **Trust and save** pins that key and saves the host in one step. When you change any address, Kepler notes that an install at the old address stays there.

**Kepler reads your own `~/.ssh/config` before it offers to write to it.** Kepler uses a host you have already configured exactly as you configured it, including its user, port, identity file, jump host, and any other settings. Kepler offers to edit the file only when it has nothing there to reuse. **Open in → VS Code** on an SSH environment uses that same host entry, so VS Code connects the way your terminal does.

### Server controls

The restart and update controls act on the server a window is connected to, so they appear in the popover and in a remote window's Settings. **Stop server** is also on every host's page in a local window.

| Control | What it does |
|---|---|
| **Restart server to update** | Installs the newer server build and reconnects. When something would stop, the **Update server?** confirmation lists it first |
| **Restart server** | Offered when no update is pending, for a stuck server. It always asks first |
| **Stop server** | Stops the Kepler server on the host for every connected window and device, and ends its agent sessions |
| **Auto-shutdown when idle** | Stops the server after a number of minutes with no window connected and nothing running. Off by default; the timeout defaults to 30 minutes |
| **Stop anyway after** | Stops the server after a number of hours with no window connected, even if work is running. Defaults to 12 hours |

**Auto-shutdown when idle** counts an agent that is working, or a terminal that is running a command, as something running. A shell that waits at its prompt does not count. **Stop anyway after** limits how long running work can keep the server up, so a dev server you forgot about does not keep it running indefinitely. The hours count from when the last window disconnects, and start over when a window connects.

Both settings belong to the machine, so they apply to every window and device connected to it. You set them from a window connected to the machine.

Both the **Update server?** and **Restart server?** confirmations list what a restart would stop, or say that running agents and terminals keep going. A restart reconnects this window and disconnects the other windows on the server. While an update or restart runs, the other server controls wait and say why.

**Keep agents and terminals running across restarts and updates**, in **Settings → General → Keep agents running**, is experimental and on by default. While it is on, running agents keep going through a restart or update. **Stop server** ends them either way.

### When you stop a server

A server that you stop on purpose stays stopped. This applies whether you stop it from this window, another window, Settings, or another device. Kepler does not start it again on its own, even when an automatic reconnect, a launch, or reopening the last window would otherwise connect to it. Those windows open on the [recovery screen](#the-recovery-screen), which says the server was stopped.

The server starts again only when you choose one of these actions:

- **Reconnect**, **Connect**, or **Try again**
- **File → New Window** on that machine
- **Restart server to update**

If a window stops its own server or disconnects, the window switches to local without showing the recovery screen.

### From a remote window

In a window that is on a remote, Settings shows only that host:

- Its connected card with the server controls
- **Auto-shutdown when idle**
- **Color** and mute
- Its **Ports** (SSH)
- Your other saved hosts to switch to

A remote window never shows the other hosts' addresses. To rename a host, edit a connection, or add or remove a host, click **Open in a local window**. You also need a local window to switch to a host that needs a password; its row offers **Open in a local window**.

### Connection failures

A failed connection shows an **Unable to connect to *machine*** alert with the SSH diagnostic and a **Copy error** button, so you can paste the diagnostic into a bug report. A failure on another machine does not drop this window's connection.

Common SSH failures, such as **Connection refused** or **Host key verification failed**, get a plain-language headline and a hint. **Update remote Kepler server** means the host's server is too old to take your GitKraken sign-in: update the Kepler install on the host and try again. On a WSL machine, Kepler says when the distro no longer exists, and reads **Connection failed** for anything else.

If the failure happens while you are adding a host, the wizard shows the headline, the hint, and the diagnostic in place, with **Try again**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-auth-rejected-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-auth-rejected-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Add machine wizard's failure step: Authentication rejected, The machine refused the credentials Kepler offered, and the Diagnostic open, reading alex@dev.acme.example: Permission denied (keyboard-interactive), each with Copy, above Cancel and Try again.">
  </a>
  <figcaption style="text-align:center; color:#888">A failed connection while adding a host.</figcaption>
</figure>

For Kepler's own log file, use **Settings → Help → Logs**.

### Removing a connection

**Remove *machine*…** deletes the saved entry on this desktop. If the SSH wizard created the entry, Kepler also offers to remove what the wizard set up:

| Cleanup option | What it does | Default |
|---|---|---|
| **Remove scoped known_hosts file** | Deletes the host-key trust file Kepler created for this connection | On |
| **Remove generated local SSH key** | Deletes the key the wizard generated, and its `.pub` sibling | On when such a key exists |
| **Uninstall Kepler server on the machine** | Stops the server and removes its install folder on the machine | On, unless the server is in use |
| **Remove deployed key from remote authorized_keys** | Removes the key the wizard installed on the host | Off |

Removing a WSL host offers **Uninstall Kepler server on the machine** for the distro. For a distro that no longer exists, Kepler shows nothing to uninstall.

If the server reports live sessions or connected clients, Kepler disables the uninstall until you select **Uninstall anyway, I understand sessions on this machine may be lost**. If the host is unreachable, or needs a password Kepler does not have, Kepler hides the host-side options, and the dialog states which of the two reasons applies.


***

## Add an SSH host

To add an SSH host, click **Add machine** in **Settings → Remote environments**. On Windows, choose **SSH** or **WSL** under **Machine type** first. To save a host already in your `~/.ssh/config`, use **Add** under **Found on this machine** instead.

A host taken from `~/.ssh/config` inherits your system SSH configuration, including its host-key trust. A host built in the wizard gets its own trust file, pinned at the fingerprint you accepted.

### The wizard

The SSH wizard has 5 steps:

| Step | What you do |
|---|---|
| *Connect to a machine you reach over SSH…* | **Name** (optional, defaults to its address), **Host**, **User** (optional, defaults to the machine's `$USER`), **Port** |
| *Choose authentication.* | Pick a mode (see below) |
| *Verify the machine's fingerprint.* | Kepler fetches the host key and shows its algorithm and fingerprint. **Trust and continue** pins it |
| *Verifying the connection.* | Kepler makes a real connection before anything is saved |
| *Ready to save.* | **Add** saves the host and opens its page. Nothing connects until you press **Connect**; a password the wizard verified is reused for that first connect |

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-new-host-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-new-host-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The first step of Add machine under Remote environments in Settings: its description, then a card with Name (optional) filled in from the host as dev.acme.example, Host dev.acme.example, Port 22 and User (optional) alex, with Cancel and Continue below the card.">
  </a>
  <figcaption style="text-align:center; color:#888">The first step of adding an SSH host.</figcaption>
</figure>

| Authentication mode | What it means |
|---|---|
| **Existing key** | Use one of the keys already in `~/.ssh`. Unavailable when Kepler finds none |
| **Password** | *Re-prompt every connect.* The password is never stored |
| **Generate key** | *Keyless after first connect.* Kepler uses the password once to install a fresh ed25519 key at `~/.ssh/id_ed25519_kepler_<hash>`. Your existing keys are never overwritten |

**Generate key** needs `ssh-keygen` on your machine; the chip reads **ssh-keygen missing** when ssh-keygen is absent.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-auth-mode-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-auth-mode-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Add machine wizard's Choose authentication step asking how Kepler should authenticate to dev.acme.example: Existing key (1 key found) is selected over Password and Generate key, the Identity file reads /home/alex/.ssh/id_ed25519, and Back, Cancel and Continue sit below the card.">
  </a>
  <figcaption style="text-align:center; color:#888">Choosing how Kepler signs in to the host.</figcaption>
</figure>

If you pick **Password**, the wizard then offers **Set up a key for this machine?** **Generate and copy key** generates a fresh ed25519 key, copies it to the host, and uses it for future connections, so you do not need the password again. **Skip** keeps the host on password sign-in.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-key-offer-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-key-offer-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Add machine wizard asking Set up a key for this machine?: Kepler generates a fresh ed25519 key, copies it to dev.acme.example and uses it for future connects, and never overwrites existing keys (the new key is named id_ed25519_kepler_ followed by a hash, in ~/.ssh), with Cancel, Skip and Generate and copy key.">
  </a>
  <figcaption style="text-align:center; color:#888">The offer to replace a password with a key.</figcaption>
</figure>

If the host rejects a key-based connection, the host's page shows a password row so you can retry with a password. If no key is saved for that host yet, the page also offers to install one at the same time. If a connection from the popover needs a password, Kepler opens a password dialog instead.

### SSH to a Windows machine

Kepler connects to Windows hosts over SSH as well as Linux and macOS ones. Kepler detects a Windows host and installs itself accordingly.

Nothing changes in the wizard. If the host authenticates but its shell rejects Kepler's commands, the diagnostic reads **Remote shell was unable to run the command**, and the hint points at the OpenSSH default shell. Windows 10 and 11 ship PowerShell, so a changed default shell is the usual cause.

The host-side cleanup offered by **Remove *machine*…** does not run on a Windows host. See [Known limitations](#known-limitations).

***

## WSL environments

On Windows, a WSL 2 distro is a remote environment like any other, and the simplest one to set up: it needs no credentials and no fingerprint check.

- Kepler detects WSL and lists your **version 2** distros. Kepler does not offer WSL 1 distros, or Docker Desktop's own `docker-desktop` and `docker-desktop-data` distros.
- Detected distros appear under **Found on this machine** in Settings, and in the popover while you have no saved hosts, where one click connects to it. Picking one in the popover saves the distro as a host and connects to it, so the connection survives a disconnect.
- To add one by hand, choose **Add machine**, then **WSL** under **Machine type**, and enter its **Distro** (and an optional **Name**). A WSL host is edited, checked, and removed exactly like an SSH one.

***

## Port forwarding

When an agent or a terminal starts a dev server on an SSH host, its `http://localhost:3000` link points at the host, not at this computer. Kepler forwards that port over your SSH connection so the link opens here.

- **Click the link.** In an SSH window, **Cmd/Ctrl**-click a `localhost`, `127.0.0.1`, or `0.0.0.0` link in a terminal, or click one in the agent transcript. Kepler forwards the port to the host's `localhost`, then opens the local URL. If that port is already taken on this computer, Kepler picks a free one.
- **Open it from the task.** A `localhost` link attached to a task opens through forwarding too, from the task's context panel, the link's detail, or the Dashboard's resources list. Agents attach the URL of a dev server they start for you to open.
- **Add one by hand.** **Settings → Remote environments → Ports**, in the SSH window, lists this window's forwards as remote port → local URL. To add a forward, enter a **Port** and click **Add**. **Stop** ends one forward, and **Stop all** appears when more than one is forwarded.

While anything is forwarded, the chip shows a radio-tower glyph and the popover adds a summary row that opens the **Ports** list.

Forwards belong to the window that made them. Disconnecting, closing, reconnecting, or switching hosts ends them, and Kepler does not restore them. A forward that fails opens nothing rather than reaching a service on this computer. Local and WSL windows open `localhost` links as they are, with no forward.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-ports-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-ports-oct-2026.png" class="help-center-img img-bordered" alt="The Ports list in an SSH window's Settings, with Stop all and two forwards, 3000 to http://localhost:51860 and 5173 to http://localhost:51873, each with Stop, above a Port field and Add.">
  </a>
  <figcaption style="text-align:center; color:#888">Two forwarded ports, each on a free local port.</figcaption>
</figure>
<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-ports-chip-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-ports-chip-oct-2026.png" class="help-center-img img-bordered" alt="The dev-server chip with a radio-tower glyph after its name, and its popover open with a row reading 2 ports forwarded 3000, 5173.">
  </a>
  <figcaption style="text-align:center; color:#888">The radio-tower glyph on the chip, and the forwarded-ports row in the popover.</figcaption>
</figure>

***

## What runs where

| Piece | Runs on |
|---|---|
| Kepler's window and its native capabilities | Your local machine |
| Git operations, worktrees, and repositories | The host |
| Agent and terminal sessions | The host |
| Provider and issue-tracker data | The host |
| The interface itself | Served by this computer when the host runs the same version of Kepler, otherwise by the host's Kepler server (below) |
| Themes, and your choice of theme | Your local machine |

**Agent sessions belong to the server, not to your window.** If you close the window, lose the network, or put the laptop to sleep, the sessions keep running. When you reconnect, from this machine or a different one, the sessions are listed and you can resume them. If the server itself goes away, you can still resume the conversation.

Kepler runs agent sign-in on the host. Claude Code, Codex, and Auggie all sign in to a remote target: Kepler starts the flow on the host, the sign-in page opens in your *local* browser, and Kepler saves the credential on the host. For Claude Code and Auggie, you paste back what the sign-in page gives you. Codex signs in with **ChatGPT (device code)**, which *works on any machine*, with an API key, or with **Import local Codex login**. See [Agent Integrations](/kepler/agent-integrations).

<div class="note" markdown="1">

**Remote windows use this app's interface.** When the host runs the same version of Kepler, a remote window shows this app's interface. Otherwise, it shows the host's own interface. To keep this app's interface even then, turn on **Settings → Remote environments → Remote windows → Always use this app's interface**, and Kepler offers to update the server or this app instead. It is off by default.

</div>

**Themes belong to this computer.** Every window, including one on a remote machine, lists and installs themes from this computer's themes folder and gallery. Every window opens in the theme you chose.

In a remote window, the theme picker adds an **On *machine*** group for themes the host has and this computer does not:

- To copy a theme to this computer, click **Install on this computer**.
- When this computer has its own copy of the same theme, the host's copy says how it compares, such as **Older than yours**. Installing it asks first, then moves your copy to the Trash (the Recycle Bin on Windows).
- Kepler never overwrites a copy you installed; it stays as it is until you update it yourself.

Kepler refuses a host theme that conflicts with a built-in theme or another theme on this computer, and refuses installs when the themes folder is full or you install too many at once. See [Themes in a remote window](/kepler/settings-app#themes-in-a-remote-window).

***

## What you see while connecting

The first connection to a host where Kepler is not installed sends the server to it, so it takes minutes rather than seconds. The chip, the popover, and the host's Settings page name the current stage, such as **Uploading remote server**, with a progress bar when the total is known. Reconnecting to a host whose server is already running is much faster.

**Cancel** stops the attempt, from the popover or from the host's own **Connect** button.

If Kepler launches directly into a remote window and connecting takes more than a moment, the window shows a *Connecting…* screen with the stage and **Cancel**. **Cancel** there stops the restore for that machine only.

***

## Recovery after restart or sleep

When a connection breaks, Kepler rebuilds it.

| Event | What Kepler does |
|---|---|
| **The connection drops** | The chip reads **Reconnecting…** and Kepler retries |
| **The machine wakes from sleep** | Kepler reconnects right away to any machine it lost |
| **The connection comes back to the same server** | The page stays as it was, with your drafts, scroll position, and terminal scrollback |
| **The server restarts or updates** | The window reconnects when the server is back, and reloads onto the view it was on |
| **Kepler restarts** | Every window comes back with its size, position, view, and machine |
| **A reconnect cannot finish** | The window shows the [recovery screen](#the-recovery-screen). A host that needs a password is the usual cause |

A rebuilt connection comes back signed in, with your drafts and preferences intact.

### The recovery screen

When a window cannot reconnect to its machine, it shows a full-screen recovery screen. The screen names what happened, shows the reason it failed, and offers one action to reconnect, plus **Switch to local**. The window keeps its saved machine until it reconnects or you choose **Switch to local**.

When any window reconnects to the machine, the other windows waiting on the recovery screen reconnect too.

The action depends on what happened:

| What happened | Action |
|---|---|
| A reconnect gave up, or the server was stopped from another window or device | **Reconnect** |
| A server update or restart failed, a new window could not connect, or the window kept failing to load | **Try again** |
| Kepler launched into a remote window that could not connect | **Connect** |
| The machine is no longer saved | **Open Remote environments** |

A failed update or restart leaves the server stopped. **Try again** installs the update and starts the server. If the machine needs a password, the screen asks for it.

**If your plan does not include remote environments**, the screen says so, and offers **Upgrade to *plan*** or a free trial when one is available. You can also switch to another organization marked *Includes remote environments*, sign out, or click **Check again** to re-read your plan. Once your plan allows it, the window connects by itself.

<!-- TODO(screenshot): Replace — ade-remote-recovery-plan-gate-01: the full-window recovery screen for dev-server on an account without remote environments, reading Your plan doesn't include remote environments, with Upgrade to plan, the signed-in account card, and Switch to local. -->
<!-- TODO(screenshot): New — The full-screen remote recovery screen at 0.15.0, for example "Disconnected from dev-server" with the reason line, Reconnect, and Switch to local. -->

***

## Local conveniences that still work

Some things have to happen on the machine in front of you. Kepler runs those through the desktop app rather than on the host.

| Feature | Behavior over a remote connection |
|---|---|
| **Open in…** and **Show in Finder** (**Show in Explorer** on Windows, **Show in file manager** on Linux) | Run on your desktop machine, not on the host. Kepler shows only the ones that work for this machine |
| **Desktop notifications** | Shown by your local desktop once per machine, or inside Kepler while you are in a window on that machine. A muted host shows none |
| **Dictation** | Captured by the local app. See [Dictation and Read Aloud](/kepler/voice-input) |
| **Copying from Codex** | A copy Codex makes in a remote window goes to your local clipboard, not the host's |
| **Pasting in a Windows host's terminal** | **Ctrl+V** pastes your local clipboard, even when this window runs on macOS or Linux |
| **Folder pickers** | Browse the host's filesystem, since that is where the work lives |

These 7 editors open a remote folder through their own remote extension:

| Editor | Opens remote folders on |
|---|---|
| **VS Code** | SSH and WSL |
| **VS Code Insiders** | SSH and WSL |
| **Cursor** | SSH and WSL |
| **Devin** (formerly Windsurf) | SSH and WSL |
| **Antigravity IDE** | SSH and WSL |
| **Trae** | SSH and WSL |
| **Kiro** | SSH only, not WSL |

The editor resolves the host and authenticates by itself. For SSH, the editor uses your own SSH configuration, so a host Kepler reaches with a custom identity file may still prompt in the editor.

Other editors, and the file manager, need a path that Windows can reach. WSL provides one, `\\wsl$`, but an SSH host does not. When no such path exists, Kepler does not show the option.

***

## How Kepler installs on a remote machine

The first connection to a machine downloads the Kepler server, so it takes minutes. Later updates download only what changed. The host needs nothing pre-installed beyond SSH or WSL, and Kepler installs itself to `~/.kepler-server`. If the download fails, check your internet connection and try again.

**Kepler never installs over a running server.** On connect, it replaces an out-of-date server on its own only when no running agents, open terminals, or other connected windows would be affected. Otherwise the server keeps running and the chip offers **Restart server to update**. With **Always use this app's interface** on, other connected windows and devices no longer hold the update back.

### When the server and the window disagree

When a remote window and its server run different versions, the window can show a full-screen message instead of the app:

- *This remote server is out of date*: click **Update server**.
- *This remote server is newer than this window*: update this app. If no newer version of the app is available, click **Replace server** to put this app's version on the server. Kepler asks first. If the server's data is newer than this app can read, Kepler refuses; update this app instead.
- Otherwise, **Try again** loads the matching version. If the message keeps coming back, restart the server.

**Switch to local** moves the window back to this computer.

***

## Remote access: reach Kepler from another device

**Remote Access** is the other direction. It opens this Kepler window from another device, such as a second computer or a phone, through your GitKraken account. Your work still runs here; the other device only sees the interface.

Configure it in **Settings → Remote Access**, or from the **Remote Access** button in the title bar. The button's icon is green while Remote Access is active, amber while it connects, and red on an error. Hover over it to open its popover, which acts on the machine the window is on:

- How many devices are paired and online.
- While active, a QR code and the link, with **Copy link**.
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

### Before you start

You need a GitKraken account signed in to Kepler, on a paid GitKraken plan. Remote Access is not available on the free Community plan.

When you sign out of Kepler, each remote machine your windows are connected to learns that you signed out, and turns its Remote Access off. A sign-in that expires on its own does not turn Remote Access off.

If Kepler on the computer is not signed in, a paired device shows **Sign in**. Only the GitKraken account that turned on Remote Access can sign the computer in from there. To use another account, sign in to Kepler on the computer itself.

### Turning on Remote Access

1. Open **Settings → Remote Access**.
2. Click **Turn on Remote Access**.
3. In **Name this machine**, keep the name Kepler fills in, or enter a name you recognize. gitkraken.dev shows this name in your list of machines.

**Remote Access stays on until you turn it off.** Only you, a deliberate sign-out, or a different account signing in turns it off. When Kepler restarts, it turns Remote Access back on only for the account that turned it on. When the connection fails, Kepler keeps retrying, and the status reads **Waiting to reconnect** with the reason. **Retry now** tries at once. Paired devices stay paired through the wait. Remote Access also waits in these 2 cases:

- With no GitKraken sign-in, it connects as soon as you sign in.
- When your account has reached its limit of machines with Remote Access on, remove one you no longer use with **Manage machines on gitkraken.dev**, then retry.

This machine stays awake while Remote Access is on, except while it waits to reconnect.

To turn it off, click **Turn off Remote Access** in Settings or in the popover, and confirm. Every paired device is disconnected.

### Pairing another device

When Remote Access is active, a QR code and a link appear in Settings and in the popover.

- To pair a phone, scan the QR code. Otherwise, copy the link.
- The link opens **gitkraken.dev/integrations**, where you approve the connection with your GitKraken account.

A pairing link works once and expires after 5 minutes. To pair after that, open a new link from the computer running Kepler.

You can bookmark the address a paired browser opens on. If that browser's connection has ended, opening the address again takes you to gitkraken.dev to sign in and pair it again.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-access-phone-sep-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-access-phone-sep-2026-v3@2x.png" class="help-center-img img-bordered" alt="Kepler's Dashboard in a phone's browser, on the Tasks view: one bar with Menu, the view picker showing Tasks with a chevron and an orange dot, Search, Options and New task, over the task list grouped into Needs attention (Add product search, In Development, Approval needed), Unread (Fix the cart total, In Review with its pull request and issue chips and Changes requested; Update checkout copy, On Hold, and Upgrade the payment SDK, In Review, each with New reply) and a folded Not started (1).">
  </a>
  <figcaption style="text-align:center; color:#888">Once paired, a phone opens this Kepler in its browser, in the phone layout.</figcaption>
</figure>

### Using Kepler on a phone

When you open Kepler in a phone's browser, it uses a phone layout: one bar at the top of each screen in place of the desktop top bar and headers. The phone layout applies to any browser window as narrow as a phone. The desktop app never uses it, at any window width. On a touch screen, Kepler also keeps the phone awake while you watch a working agent or a terminal printing output, so the connection does not drop. When the on-screen keyboard is open, Kepler fits the screen above it. In the composer, **Enter** starts a new line. To send, tap **Send**.

To open Kepler like an app, add it to your phone's home screen from the browser's menu, such as **Add to Home Screen**. The Kepler icon then opens Kepler full screen, without the browser's address bar and toolbars.

#### The menu

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

#### The Dashboard

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

#### A task

A task's bar has **Back**, the task's name, and one icon each for **Sessions**, **Changes**, **Terminal**, and **Resources**. A dot on **Back** means another task needs you.

- **Tap an icon** to go to what is waiting there first, or else the last thing you had open. Its list offers each row, an action to add one (**New session**, **New terminal**, or **Add resource**), and **Show everything in this task**.
- **Tap the task's name** to open **Switch task**, a sheet of every task in the Dashboard's order. Swipe sideways on the name to go back to the previous task.
- **Pull down on the bar** for a sheet of everything in the task: sessions, checkouts, terminals, and resources, with each row's actions.

Under the bar, a details row shows the task's stage and a summary. Expand it to see the checkout and the task's pull request and issue.

**Add resource** opens a sheet of resource kinds. Pick a kind to see what the task already holds, add more with its add control, such as **Add issues**, or use **Select** to archive or remove several at once.

**Changes** opens with one bar: **Close**, the file's name, and **Previous** and **Next**. Tap the name for the list of changed files. Everything else, from which changes to show to saving an edit, is in the bar's overflow menu.

#### Terminals

On a touch phone, every live terminal has a key row under it with the keys a phone keyboard lacks: **Esc**, **Ctrl**, **Tab**, the arrows, **Enter**, **Keyboard**, which shows or hides the phone keyboard, and **Hide keys**. Swipe up on a key, or hold **Esc**, **Ctrl**, **Tab**, or **Enter**, for the second action printed above it:

| Key | Second action |
|---|---|
| **Esc** | **Ctrl+C** |
| **Ctrl** | **Shift** |
| **Tab** | **Shift+Tab** |
| **Enter** | **New line** |
| Left and Right arrows | **Home** and **End** |
| Up and Down arrows | **Page up** and **Page down** |

Tap **Ctrl** once to hold it for the next key only, or double-tap it to lock it until you tap it again. Shift works the same way: swipe up on or hold **Ctrl** once to hold Shift for the next key, or twice quickly to lock it. With Shift on, the letters you type are capitals. Holding an arrow repeats it. **Hide keys** replaces the row with a **Show keys** button, and this device remembers the choice. The phone keyboard opens only when you tap the terminal or **Keyboard**, not on every scroll.

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

### Managing sessions from gitkraken.dev

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

***

## Known limitations

| Limitation | Detail |
|---|---|
| **Commit and tag signing** | Signing does not work over a remote connection. Turn off `commit.gpgsign` for the repository on the remote, or commit from a terminal there |
| **Remote-connection management in a browser client** | Desktop app only. A browser client hides the title-bar chip |
| **Auto-update in a browser client** | Does nothing, because a browser cannot update itself. Update the desktop app, or update the host's server from a desktop window |
| **Port forwarding from a Windows client** | A host that signs in with a password asks for it again for each forward. Only `localhost`, `127.0.0.1`, and `0.0.0.0` links forward |
| **Host-side cleanup on a Windows host** | **Uninstall Kepler server on the machine** and **Remove deployed key from remote authorized_keys** do not work on a Windows host. Delete `~/.kepler-server` and the `authorized_keys` entry on the host yourself |

***

## Related

- [Settings](/kepler/settings-environment): the **Remote environments** and **Remote Access** pages, and [the shortcut list](/kepler/settings-app#keyboard-shortcuts)
- [Agent Integrations](/kepler/agent-integrations): signing agents in, including on a remote target
- [Review Changes](/kepler/review-changes): reviewing and shipping the work a remote agent produced

---
