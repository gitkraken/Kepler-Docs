---
title: Remote Environments
description: Run your agents on another machine over SSH or in WSL, switch environments from the title bar, manage machines in Settings, forward an SSH host's ports to this computer, and open this Kepler from another device with Remote Access.
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
last_verified: 2026-10
llms_include: true
tags: [remote-environments, ssh, wsl, windows, port-forwarding, settings, remote-access, qr-pairing, gitkraken-dev, diagnostics, notifications]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

A **remote environment** runs your agents, worktrees, and terminals on another machine: a dev server, a cloud VM, or a WSL (Windows Subsystem for Linux) instance on Windows, while you work from this window. Kepler installs itself on the host over SSH (Secure Shell), so you do not need to pre-install anything there.

***

## Two remote features

Kepler has two remote capabilities, and they work in opposite directions:

| Feature | Direction | Where it lives |
|---|---|---|
| **Remote environments** | Kepler on your desktop reaches **out** to another machine, and your work runs there | The title-bar chip, and **Settings → Remote environments** |
| **Remote Access** | Another device reaches **in** to this Kepler, and your work stays here | **Settings → Remote Access** |

Everything up to [Remote Access](#remote-access-reach-kepler-from-another-device) describes connecting *to* another machine.

<div class="note" markdown="1">

**Remote environments need a paid plan.** Every paid plan except Student includes it, with no limit on how many environments you can add. Other plans see a banner offering a free trial where one is available, and, when another organization you belong to already includes it, names that organization with **Switch to organization**. If you've just upgraded, **Already upgraded?** with **Check again** re-reads your plan; when nothing has changed, it says so briefly: *Still on {plan}*.
<!-- TODO(verify): Confirm with the product team that Student is the only paid plan without remote environments (src/ui/components/auth/plan.ts at v0.13.0 names Student alone). -->

</div>

***

## Switching environments from the title bar

Kepler binds each window to one environment at a time, and the title-bar chip shows which one. The chip leads with the environment's type icon, and a green dot on that icon means connected.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-chip-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-chip-oct-2026.png" class="help-center-img img-bordered" alt="The title-bar chip reading dev-server, tinted violet like the title bar behind it, with a green dot on its type icon. Below it, the popover header peeks on hover: dev-server, Connected, 5 ms, the versions, Disconnect, and the restart and stop server buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">The chip on a host colored Violet, with the popover header peeking on hover.</figcaption>
</figure>
<!-- TODO(screenshot): Replace — The title-bar chip at 0.13.0 on a connected machine tinted with its color, with the popover header peeking on hover: Connected, latency, the versions, Disconnect, and the restart and stop server buttons. -->

| Chip | What it means |
|---|---|
| **Local** | This window works on this machine |
| **Connecting to *machine*…**, or the current stage | A connect this window started, or a restart or update of its own server, is in flight |
| **Reconnecting…** | The connection degraded and Kepler is rebuilding it |
| Host name | Connected. The chip takes the host's [color](#host-details) when you have set one |
| Brand fill with an up-arrow | Connected, and a newer server build is ready for the host |
| Warning triangle | The app and the server disagree on version. The popover says which side to update |
| Radio-tower glyph | This window is [forwarding ports](#port-forwarding) from the host |
| Monitor-and-phone glyph | [Remote Access](#remote-access-reach-kepler-from-another-device) is on for this machine, tinted by its status |
| An error headline | The last attempt failed. The chip calms back down after a few seconds; the popover and the host's Settings page keep the full error |

**Hover the chip to peek.** After a short pause, the popover's header appears with its buttons live. Move the pointer into it and the rest of the popover grows in below. Click the chip, or focus it and press **Enter** or **Down Arrow**, to open the whole popover pinned.

Kepler hides the chip in a browser client, which cannot manage connections at all.

### The popover

The popover answers where you are and where else you can go, and hands anything heavier to Settings.

| Part | What it does |
|---|---|
| Header | The current machine, with its address, latency, and the server and app versions, or *Working locally* when the window is local. The gear (**Machine settings**) opens the machine's Settings page |
| **Restart server to update** | Appears when a newer server build is ready. The line beneath says what the update will stop, for example *Updating restarts the server and stops 2 running agents. Agent sessions can be resumed afterward.* |
| **Disconnect** | Releases this window only. The server keeps its sessions running |
| **Restart server** (circular arrow) | Restarts a connected server when no update is pending. See [Server controls](#server-controls) |
| **Stop server** | Stops the server on the machine. Every other window connected to it moves to the [recovery screen](#the-recovery-screen), and the server stays stopped until you start it again. See [When you stop a server](#when-you-stop-a-server) |
| Forwarded ports | *Port 3000 forwarded*, or a count followed by the ports, such as *2 ports forwarded 3000, 5173*. Opens the host's **Ports** list |
| **Switch to** | Every other saved host, plus **Local** (*Work on this machine*) when this window is on a remote |
| **Found on this machine** | WSL distributions found on this PC, offered for one-click connect while you have no saved hosts |
| **Remote Access** | Turns Remote Access on or off for the machine this window works on, and shows how many devices are connected. On a remote window, it reads **Use *machine* anywhere** |
| **Manage remote environments…** | Opens **Settings → Remote environments**. **⌘ ⇧ R** on macOS, **Ctrl + Shift + R** elsewhere |

When this app, rather than the server, is the side that is behind, the header offers this app's own update instead, and says that sessions on the host keep running.

Clicking a **Switch to** row moves this window. Hold **Cmd** (macOS) or **Ctrl** to open that host in a new window instead, leaving this window where it is. The trailing window icon on each row does the same thing with a single click. A host already open in another window is marked **Connected**, and clicking its row brings that window forward rather than opening a second connection.

A connect that a *different* window starts never takes over this window's chip.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-popover-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-popover-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The environment chip's popover in a local window: Working locally, Switch to dev-server (SSH, alex@dev.acme.example), Remote Access (Inactive) with Turn on Remote Access, and Manage remote environments… with its Ctrl+Shift+R shortcut.">
  </a>
  <figcaption style="text-align:center; color:#888">The popover, connected to a host.</figcaption>
</figure>

***

## Windows on a remote host

- **New Window opens on the same host.** **File → New Window** (**⌘ ⇧ N** on macOS, **Ctrl + Shift + N** elsewhere) from a remote window opens a second window on that host. A remote window also offers **File → New Local Window** when you want a local one. If the new window cannot reach the host, it opens on the [recovery screen](#the-recovery-screen) with the reason. A new window you open from the popover or the connection picker does the same when it fails to connect.
- **Windows on one SSH host share a connection.** They ride one SSH connection and one tunnel, so a second window opens without a fresh handshake, and every window on a host shares the same storage.
- **A host open in another window is reached through that window.** The popover and Settings show it as connected, offer **Show window**, and read its latency, versions, and sessions through that window's connection.
- **The last closed remote window reopens on its host.** With no window open, the dock, the tray, or launching Kepler again reconnects to the host the last window was on. Closing a window that was still waiting on an unreachable host leaves the next reopen local, and with **Restore windows on launch** off, a launch stays local.

***

## Managing machines in Settings

**Settings → Remote environments** is the full management surface. In a local window, **Your machines** lists your saved machines. Each row shows the host's type, **Connected** or *Not connected*, and *Open in N windows* when other windows already use it. **Connect** connects this window, the window icon connects in a new window, and **Show window** replaces **Connect** for a host open elsewhere. Click a row to drill into the host's page.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-environments-hosts-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-environments-hosts-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Settings › Remote environments: Add machine, Your machines with dev-server (SSH, not connected, alex@dev.acme.example) and Connect, Found on this machine listing build-box and staging-db from the SSH config with Add and hide buttons and Show hidden (1), and the Remote windows option.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings → Remote Environments, with a saved host.</figcaption>
</figure>

**Found on this machine** lists machines from your `~/.ssh/config` and WSL distributions you have not saved yet. **Add** saves one. On a plan without remote environments, it reads **Try free and add** where a trial is open, or **Upgrade to add**, which opens the plan page and saves nothing. Kepler shows three at first, with **Show *N* more** for the rest. The eye icon hides a machine you never want offered, and **Show hidden (*N*)** brings them back.

### Host details

A host's page puts its actions in a card at the top: **Connect** (**Cmd/Ctrl**-click for a new window; while a connect runs, the same button cancels it), or **Show window** and **Connect to *machine* in a new window** when another window already has it, plus **Stop server** and a red trash icon (**Remove *machine*…**). The pencil beside the name renames the saved connection; nothing on the host changes.

| Group | What it does |
|---|---|
| **Connection** | Edit the address in place: **Host**, **Port**, **User**, and **Identity file** for SSH, or **Distro** for WSL. **Save** keeps the same saved host. Disconnect first; a connected host's fields are locked |
| **Color** | **None**, **Rose**, **Amber**, **Lime**, **Cyan**, **Blue**, or **Violet**. Tints the host's chip, its rows, and the top bar of its windows |
| **Mute notifications from *machine*** | *Kepler won't show desktop notifications for sessions on machine. Alerts still appear inside its windows.* |
| **Sessions** | Labeled *survive disconnect, resumable anywhere*. Each row is a live agent session on that host, and clicking one opens it. For a host nobody is connected to, **Check** opens a short-lived connection to ask its server what is running |

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-host-page-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-host-page-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The dev-server machine's page in Settings › Remote environments, not connected: Connect, Stop server, the Connection fields (host dev.acme.example, port 22, user alex, identity file), Color, Mute notifications from dev-server, and Sessions with Check.">
  </a>
  <figcaption style="text-align:center; color:#888">A saved host's page.</figcaption>
</figure>

Changing the address of a host the SSH wizard created first fetches the new address's host key, under **New host key**. **Trust and save** pins that key and saves the host in one step, and every new host or port gets its own scan. Any address change notes that an install at the old address stays there.

**Kepler reads your own `~/.ssh/config` before it offers to write to it.** A host you have already configured (its user, port, identity file, jump host, whatever you set) is used as you configured it, and Kepler offers to edit the file only when there is genuinely nothing there to reuse. **Open in → VS Code** on an SSH environment opens through that same host alias, so VS Code's own Remote-SSH resolves it exactly the way your terminal does.

### Server controls

The restart and update controls act on the server a window is connected to, so they appear in the popover and in a remote window's Settings. **Stop server** is also on every host's page in a local window.

| Control | What it does |
|---|---|
| **Restart server to update** | Installs the newer server build and reconnects. Its line says what it stops |
| **Restart server** | Offered when no update is pending, for a stuck server. The confirmation says what restarting stops, such as *Stops 1 running agent. Agent sessions can be resumed afterward.*, and that *This window reconnects. Other windows connected to machine disconnect.* |
| **Stop server** | Stops the Kepler server on the host. The confirmation names how many agent sessions it terminates; *Every connected client loses the server, not just this window.* |
| **Auto-shutdown when idle** | Stops the server after *N* *minutes with no window connected and nothing running.* Off by default. The timeout defaults to 30 minutes |
| **Stop anyway after** | Stops the server after *N* *hours with no window connected, even if agents or terminal commands are running.* Defaults to 12 hours |

**Auto-shutdown when idle** counts an agent that is working, or a terminal that is running a command, as something running. A shell that waits at its prompt doesn't count. **Stop anyway after** caps how long running work can keep the server up, so a forgotten dev server doesn't keep it running forever. The hours count from when the last window disconnects, and start over when a window connects.

Kepler stores both settings on the machine, not locally, so they apply to every client of that server. You set them from a window connected to the machine. A local window shows *Idle shutdown is set from a window connected to machine.*

With **Keep agents and terminals running across restarts and updates** on in **Settings → General → Keep agents running** (experimental), running agents keep going through a restart or update, and the confirmation says so. **Stop server** ends them either way.

### When you stop a server

A server that you stop on purpose stays stopped. This applies whether you stop it from this window, another window, Settings, or another device. Kepler doesn't start it again on its own, even when an automatic reconnect, a launch, or reopening the last window would otherwise connect to it. Those windows land on the [recovery screen](#the-recovery-screen) with *The server on machine was stopped. Reconnect to start it again.*

The server starts again only when you choose one of these actions:

- **Reconnect**, **Connect**, or **Try again**
- **File → New Window** on that machine
- **Restart server to update**

The window that stops its own server, or that disconnects, goes local without the recovery screen.

### From a remote window

Settings in a window that is on a remote shows that host only: its connected card with the server controls, **Auto-shutdown when idle**, **Color** and mute, its **Ports** (SSH), and your other saved hosts to switch to. A remote window never sees the other hosts' addresses. Renaming, editing a connection, adding, and removing happen in a local window: **Open in a local window** takes you there. Switching to a host that needs a password does too: its row reads *Connect to machine from a local window*, with **Open in a local window**.

### Connection failures

A failed connect renders a **Couldn't connect to *machine*** alert with the raw SSH diagnostic as selectable text and a **Copy error** button, so it can go into a bug report unedited. When the failure is on a machine other than the one this window is connected to, Kepler adds *You're still connected to machine; this didn't drop it.*

Common SSH failures get a plain-language headline and a hint. Kepler recognizes:

- **Authentication rejected (publickey)**
- **Connection refused**
- **Machine unreachable**
- **Hostname could not be resolved**
- **Connection timed out**
- **Host key verification failed**
- **Update remote Kepler server**, when the host's server is too old to take your GitKraken sign-in. Update the Kepler install on the host and try again

A WSL distro that no longer exists reads *The {distro} distro wasn't found on this machine.*

The unedited diagnostic appears underneath either way.

When the failure happens while you're adding a host, the wizard shows it in place: *Something went wrong.*, the headline and hint, the **Diagnostic**, a **Copy** button for each, and **Try again**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-auth-rejected-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-auth-rejected-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Add machine wizard's failure step: Authentication rejected, The machine refused the credentials Kepler offered, a Diagnostic with Copy, and Cancel and Try again.">
  </a>
  <figcaption style="text-align:center; color:#888">A failed connection while adding a host.</figcaption>
</figure>

For Kepler's own log file, use **Settings → Help → Logs**.

### Removing a connection

**Remove *machine*…** deletes the saved entry on this desktop. When the SSH wizard created the entry, Kepler also offers to clean up after itself:

| Cleanup option | What it does | Default |
|---|---|---|
| **Remove scoped known_hosts file** | Deletes the host-key trust file Kepler created for this connection | On |
| **Remove generated local SSH key** | Deletes the key the wizard generated, and its `.pub` sibling | On when such a key exists |
| **Uninstall Kepler server on the machine** | Stops the server and removes its install folder on the machine | On, unless the server is in use |
| **Remove deployed key from remote authorized_keys** | Removes the key the wizard installed on the host | Off |

Removing a WSL host offers **Uninstall Kepler server on the machine** for the distro. A distro that no longer exists reads as nothing to uninstall.

If the server reports live sessions or connected clients, Kepler disables the uninstall until you select **Uninstall anyway, I understand sessions on this machine may be lost**. If the host is unreachable, or needs a password Kepler does not have, Kepler suppresses the host-side options, and the dialog states which of the two reasons applies.


***

## Add an SSH host

To add an SSH host, click **Add machine** in **Settings → Remote environments**. On Windows, choose **SSH** or **WSL** under **Machine type** first. To save a host already in your `~/.ssh/config`, use **Add** under **Found on this machine** instead.

A host taken from `~/.ssh/config` inherits your system SSH configuration, including its host-key trust. A host built in the wizard gets its own trust file, pinned at the fingerprint you accepted.

### The wizard

The SSH wizard walks five steps.

| Step | What you do |
|---|---|
| *Connect to a machine you reach over SSH…* | **Name** (optional, defaults to its address), **Host**, **User** (optional, defaults to the machine's `$USER`), **Port** |
| *Choose authentication.* | Pick a mode (see below) |
| *Verify the machine's fingerprint.* | Kepler fetches the host key and shows its algorithm and fingerprint. **Trust and continue** pins it |
| *Verifying the connection.* | Kepler makes a real connection before anything is saved |
| *Ready to save.* | **Add** saves the host and opens its page. Nothing connects until you press **Connect**; a password the wizard verified is reused for that first connect |

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-new-host-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-new-host-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The first step of the Add machine wizard in Settings › Remote environments: its description, Name (optional) filled in from the host as dev.acme.example, Host dev.acme.example, Port 22 and User alex, with Cancel and Continue.">
  </a>
  <figcaption style="text-align:center; color:#888">The first step of adding an SSH host.</figcaption>
</figure>

| Authentication mode | What it means |
|---|---|
| **Existing key** | Use one of the keys already in `~/.ssh`. Kepler counts what it finds; with exactly one candidate it preselects it. With none, it reads *No keys found in ~/.ssh* and can't be picked |
| **Password** | *Re-prompt every connect.* The password is never stored |
| **Generate key** | *Keyless after first connect.* Kepler uses the password once to install a fresh ed25519 key at `~/.ssh/id_ed25519_kepler_<hash>`. Your existing keys are never overwritten |

**Generate key** needs `ssh-keygen` on your machine; the chip reads **ssh-keygen missing** when ssh-keygen is absent.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-auth-mode-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-auth-mode-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Add machine wizard asking how Kepler should authenticate to dev.acme.example, with Existing key (1 key found) selected and its identity file /home/alex/.ssh/id_ed25519, beside Password and Generate key.">
  </a>
  <figcaption style="text-align:center; color:#888">Choosing how Kepler signs in to the host.</figcaption>
</figure>

If you pick **Password**, the wizard then offers **Set up a key for this machine?** **Generate and copy key** generates a fresh ed25519 key, copies it to the host, and uses it for future connects, so you don't need the password again. **Skip** keeps the host on password sign-in.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-key-offer-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-key-offer-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Add machine wizard asking Set up a key for this machine?: Kepler generates a fresh ed25519 key, copies it to dev.acme.example and uses it for future connects, with Cancel, Skip and Generate and copy key.">
  </a>
  <figcaption style="text-align:center; color:#888">The offer to replace a password with a key.</figcaption>
</figure>

If the host rejects a key-based connect, Kepler does not leave you stuck: the host's page opens a password row so you can retry with a password, and, when no key is saved for that host yet, offers to install one at the same time. A connect from the popover that needs a password opens a password dialog instead.

### SSH to a Windows machine

Kepler connects to Windows hosts over SSH as well as POSIX (Portable Operating System Interface) ones. It detects the target's operating system (OS) during the probe and switches to a PowerShell install path instead of the POSIX one, mapping the architecture to `win32-x64` or `win32-arm64`.

Nothing changes in the wizard. If the host authenticates but its shell rejects Kepler's commands, the diagnostic reads **Remote shell could not run the command**, and the hint points at the OpenSSH default shell. Windows 10 and 11 ship PowerShell, so a changed default shell is the usual cause.

The host-side cleanup offered by **Remove *machine*…** does not run on a Windows host; see **Known limitations** below.

***

## WSL environments

On Windows, a WSL 2 distro is a remote environment like any other, and the cheapest one to start with: no credentials, no fingerprint to verify.

- Kepler detects WSL by asking `wsl.exe` for its status, then lists your **version 2** distros. Kepler does not offer WSL 1 distros, or Docker Desktop's own `docker-desktop` and `docker-desktop-data` distros.
- Detected distros appear under **Found on this machine** in Settings, and in the popover while you have no saved hosts, one click from connected. Picking one in the popover saves the distro as a host and connects to it, so the connection survives a disconnect.
- To add one by hand, choose **Add machine**, then **WSL** under **Machine type**, and enter its **Distro** (and an optional **Name**). A WSL host is edited, checked, and removed exactly like an SSH one.
- WSL needs no tunnel. Kepler reaches the server inside the distro through Windows' localhost passthrough, and waits for the passthrough to catch up before the window loads.

***

## Port forwarding

When an agent or a terminal starts a dev server on an SSH host, its `http://localhost:3000` link points at the host, not at this computer. Kepler forwards that port over your SSH connection so the link opens here.

- **Click the link.** In an SSH window, **Cmd/Ctrl**-click a `localhost`, `127.0.0.1`, or `0.0.0.0` link in a terminal, or click one in the agent transcript. Kepler forwards the port to the host's `localhost`, then opens the local URL. If that port is already taken on this computer, Kepler picks a free one.
- **Open it from the task.** A `localhost` link attached to a task opens through forwarding too, from the task sidebar, the link's detail, or the Dashboard's resources list. Agents attach the URL of a dev server they start for you to open.
- **Add one by hand.** **Settings → Remote environments → Ports**, in the SSH window, lists this window's forwards as remote port → local URL. Enter a **Port** and click **Add**; **Stop** ends one, and **Stop all** appears when more than one is forwarded.

While anything is forwarded, the chip shows a radio-tower glyph and the popover adds a summary row that opens the **Ports** list.

Forwards belong to the window that made them. Disconnecting, closing, reconnecting, or switching hosts tears them down, and they are not restored. A forward that fails opens nothing rather than reaching a service on this computer. Local and WSL windows open `localhost` links unchanged, since WSL already passes localhost through.

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
| The interface itself | Served by the host's Kepler server, unless you opt in to serving it from this computer (below) |

**Agent sessions belong to the server, not to your window.** Close the window, lose the network, or put the laptop to sleep, and the sessions keep running. Reconnect (from this machine or a different one) and they are listed and resumable. If the server itself goes away, Kepler re-spawns the agent and re-attaches to the same conversation from the session Kepler saved.

Kepler runs agent sign-in on the host. Claude Code, Codex, and Auggie all sign in to a remote target: Kepler starts the flow on the host, the sign-in page opens in your *local* browser, and the resulting credential lands on the host. Claude Code and Auggie take back a code or a JSON blob you paste. Codex signs in with **ChatGPT (device code)**, which *works on any machine*, with an API key, or with **Import local Codex login**. See [Agent Integrations](/kepler/agent-integrations).

<div class="note" markdown="1">

**Experimental: serve the interface from this computer.** **Settings → Remote environments → Remote windows → Use this app's interface in remote windows** loads remote windows' interface from this app instead of from the host, so only your data crosses the connection. If the host runs a different version, its own interface is used. It is off by default, and takes effect the next time you connect to a host with no other window open on it.

</div>

***

## What you see while connecting

A first connect to an untouched host uploads the server bundle, so it takes minutes rather than seconds. The chip, the popover, and the host's Settings page all name the current stage, with a progress bar whenever the total is known.

| Stage | What it means |
|---|---|
| **Checking the machine** | Working out the host's OS and architecture |
| **Authenticating** | Negotiating SSH auth |
| **Checking the remote install** | Looking for an existing install and a live server |
| **Downloading remote server** | Fetching the matching server bundle to your machine |
| **Uploading remote server** | Sending it to the host |
| **Finishing the install on the machine** | Unpacking finished; the host is completing the install |
| **Starting the remote server** | Launching the server |
| **Updating the remote server** | Replacing an out-of-date server with the build this Kepler needs |
| **Waiting for another install to finish** | Another window or machine is installing or updating the same server. This is usually the fast path |
| **Opening the tunnel** | Forwarding a local port to the host |

**Cancel** stops the attempt, from the popover or from the host's own **Connect** button.

A warm reconnect skips most of this: the server is already installed and already running, so Kepler reads its details and opens a tunnel.

When Kepler launches straight onto a remote window, that window opens in place. It appears only if the connect takes more than a moment, as a *Connecting…* splash with the live stage and **Cancel**.

***

## Recovery after restart or sleep

Kepler expects connections to break and rebuilds them.

| Event | What Kepler does |
|---|---|
| **The connection degrades** | Health checks run every 10 seconds. Three consecutive failures flip the chip to **Reconnecting…** and start a rebuild: up to five attempts with backoff from 1 second to a 30-second ceiling |
| **The machine wakes from sleep** | Rather than waiting for health checks to accumulate, Kepler probes every bound window at once and rebuilds only the ones that are genuinely unreachable |
| **The connection is rebuilt to the same server** | The page stays as it was, with your drafts, scroll position, and terminal scrollback. Kepler reloads it only if the server itself changed |
| **The server restarts or updates** | The window reloads onto the view it was on, not a bare Dashboard. When another window updates or restarts the server, this window waits through the restart and reconnects as soon as the server is back. If the update fails, the window keeps its saved server, so it reopens on that machine after Kepler restarts |
| **Kepler restarts** | Kepler restores every window (geometry, route, and connection) so a remote window comes back on its remote |
| **A reconnect cannot finish** | Usually a host that needs interactive auth. The window shows the full-screen [recovery screen](#the-recovery-screen), and keeps its saved machine until it reconnects or you switch to local |

A rebuild is not cosmetic: Kepler tears down the dead tunnel, opens a new one, and re-propagates your GitKraken sign-in to the host, so the window comes back signed in rather than at a sign-in screen. SSH connections keep a stable local port per host, so a reconnect returns to the same origin and your interface preferences, drafts, and notification permission survive it.

### The recovery screen

When a window can't get back to its machine, it shows a full-screen recovery screen. The screen names what happened, shows the reason it failed, and offers one way back plus **Switch to local**. The window keeps its saved machine until it reconnects or you choose **Switch to local**.

The following table lists what the screen shows in each case. In each title, *machine* is the name of the saved machine:

| What happened | Title | Action |
|---|---|---|
| An automatic reconnect gave up | *Disconnected from machine* | **Reconnect** |
| The server was stopped from another window or device | *Disconnected from machine*, with *The server on machine was stopped. Reconnect to start it again.* | **Reconnect** |
| A server update failed | *Unable to finish updating machine* | **Try again** |
| A server restart failed | *Unable to restart machine* | **Try again** |
| A new window couldn't connect | *Unable to open machine in this window* | **Try again** |
| Kepler launched onto a remote window that couldn't connect | *Unable to connect to machine*, or *Not connected to machine* | **Connect** |
| The saved machine was removed, or was never saved | *machine is no longer saved*, or *machine isn't saved* | **Open Remote environments** |

A failed update or restart leaves the server stopped. **Try again** installs the update and starts the server. If the machine needs a password, the screen asks for it. If your plan doesn't include remote environments, the screen says *Your plan doesn't include remote environments.* and offers a trial or an upgrade instead.

<!-- TODO(screenshot): New — The full-screen remote recovery screen at 0.13.0, for example "Disconnected from dev-server" with the reason line, Reconnect, and Switch to local. -->

***

## Local conveniences that still work

Some things have to happen on the machine in front of you. Kepler routes those through the desktop app rather than executing them on the host.

| Feature | Behavior over a remote connection |
|---|---|
| **Open in…** and **Show in Finder** (**Show in Explorer** on Windows, **Show in file manager** on Linux) | Run on your desktop machine, not on the host. Kepler reports which of them can reach the current binding and hides the rest, so no buttons fail |
| **Desktop notifications** | Shown by your local desktop when an agent finishes, needs you, or errors. Clicking one focuses the window that asked for it. Two windows on one host alert once, and a muted host shows none |
| **Voice input** | Captured by the local app. See [Voice Input](/kepler/voice-input) |
| **Copying from Codex** | A copy Codex makes in a remote window lands on your local clipboard, not the host's |
| **Folder pickers** | Browse the host's filesystem, since that is where the work lives |

Four editors open a remote folder through their own remote extension, which is the only way a locally-installed editor can reach an SSH host's worktree:

| Editor | Authority Kepler passes |
|---|---|
| **VS Code** | `--remote wsl+<distro>` or `--remote ssh-remote+[user@]host[:port]` |
| **VS Code Insiders** | Same |
| **Cursor** | Same |
| **Windsurf** | Same |

The editor resolves the host and authenticates through its own machinery. For SSH that means your own SSH configuration, so a host Kepler reaches with a custom identity file may still prompt in the editor.

Other editors, and the file manager, rely on the path being reachable from Windows, which WSL provides, as `\\wsl$`, but an SSH host does not. When no route exists, the affordance does not appear.

***

## Remote server components

The desktop installer does not carry a server bundle for every architecture. Kepler fetches what it needs when you connect, and caches it per user.

The payload is not one tarball. Kepler splits it into four layers instead, each a separate archive with its own cache key:
<!-- TODO(verify): Agent Integrations says Kepler now runs your own Codex CLI instead of a bundled codex-acp engine. Confirm whether the remote server still ships a codex layer, and drop this row if not. -->

| Layer | What it holds |
|---|---|
| `node` | The vendored Node runtime |
| `codex` | The bundled Codex engine. Optional: a build without it ships three layers |
| `deps` | The server's dependencies |
| `app` | The server and the interface |

| Piece | Location |
|---|---|
| Published manifest and layers | `<channel>/<version>/remote-servers/<arch>/` |
| Per-user cache | `<userData>/remote-server-cache/<channel>/<version>/<arch>/` |
| On the host | `~/.kepler-server` |

The architecture token is one of `linux-x64`, `linux-arm64`, `darwin-x64`, `darwin-arm64`, `win32-x64`, `win32-arm64`.

**A connect downloads only the layers the host is actually missing.** Kepler reads the small manifest first (no payload bytes) and compares each layer's key against what the host has already installed. A version bump that changes only the app leaves your Node and Codex layers alone on both sides, so an upgrade pulls a fraction of what a first connect pulls. This holds on every transport: SSH to a POSIX host, SSH to a Windows host, and WSL.

Two cases still fetch everything. A host with no layer stamps at all (a first connect) has nothing to diff against. And when the missing layers come to three quarters or more of the payload, Kepler ships the whole thing rather than assembling a subset that saves little.

Kepler downloads each layer cache-first, retries with backoff, and writes it atomically, so an interrupted download is never mistaken for a cached layer. When a layer cannot be fetched at all, the connect fails with **Could not download the remote-server *version* for *arch*. Check your internet connection.**

The payload carries its own Node runtime, so the host needs nothing pre-installed beyond an SSH or WSL transport. Kepler couples desktop and server versions: your Kepler always knows which server build it needs. **Kepler never installs over a running server.** On connect, it replaces an out-of-date server on its own only when nobody would lose anything: no running agents, open terminals, or other connected windows. Otherwise the server keeps running and the chip offers **Restart server to update**. Only one client replaces a server at a time; the rest wait.

### When the server and the window disagree

A window whose page comes from a server on a different build shows a full-screen screen instead of the app: *This remote server is out of date*, or *This remote server is newer than this window*, with *Server {server}, this window {app}*. An out-of-date server offers **Update server**; retrying won't help until it's updated. Otherwise **Try again** loads the matching version; if the screen keeps coming back, restart the server. **Switch to local** moves the window back to this computer.

***

## Remote access: reach Kepler from another device

**Remote Access** is the other direction. It opens this Kepler window from another device, such as a second computer or a phone, over a secure tunnel relayed through your GitKraken account. Your work still runs here; the other device only sees the interface.

Configure it in **Settings → Remote Access**, or turn it on from the title-bar popover.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-access-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-access-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Settings › Remote Access while it is off: the Inactive badge and Turn on Remote Access, what it lets you do, the three steps of how it works, a note that only you can connect, and that this machine stays awake while Remote Access is on.">
  </a>
  <figcaption style="text-align:center; color:#888">Remote Access, active, in Settings → Remote Access.</figcaption>
</figure>

### Before you start

You need a GitKraken account signed in to Kepler, on a paid GitKraken plan. Remote Access is not available on the free Community edition.

### Turning on Remote Access

1. Open **Settings → Remote Access**.
2. Click **Turn on Remote Access**.
3. In **Name this machine**, keep the name Kepler fills in, or enter a name you recognize. gitkraken.dev shows this name in your list of machines.

Kepler generates a private key for this machine the first time you enable Remote Access. The key never leaves the machine; Kepler uses it to prove the machine's identity to GitKraken each time it reconnects.

### Pairing another device

Once Remote Access is active, a QR code and a link appear in Settings.

- **Scan with your phone camera to open** is the fast path. Otherwise, copy the link.
- The link opens **gitkraken.dev/integrations**, where you approve the connection with your GitKraken account.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-access-phone-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-access-phone-sep-2026.png" class="help-center-img img-bordered" alt="A paired phone's browser open on the Kepler tunnel URL, showing the connected session">
  </a>
  <figcaption style="text-align:center; color:#888">Once paired, the other device opens this Kepler session through the tunnel.</figcaption>
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
- Disable a machine to turn off its tunnel entirely, from anywhere.

<figure style="text-align:center">
  <a href="/wp-content/uploads/remote-access-options-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/remote-access-options-sep-2026.png" class="help-center-img img-bordered" alt="Expanded machine card showing each connected device with a Revoke button, and a menu with Disable machine">
  </a>
  <figcaption style="text-align:center; color:#888">Expand a machine to revoke one connection or disable the whole machine.</figcaption>
</figure>

You can also manage the current machine's connections locally, in **Settings → Remote Access → Connected devices**.

***

## Known limitations

| Limitation | Detail |
|---|---|
| **Commit and tag signing** | Signing does not work over a remote connection. Kepler says so rather than failing quietly: *Commit signing isn't available over a remote connection yet. Disable commit.gpgsign for this repo on the remote, or run the commit from a terminal there.* |
| **Remote-connection management in a browser client** | Inherently local. A browser client shows **Remote environments need the desktop app** and hides the title-bar chip, because adding hosts, connecting, and stopping servers all run through the desktop app |
| **Auto-update in a browser client** | A no-op. A browser cannot update itself; update the desktop app, or the host's server from a desktop window |
| **Port forwarding from a Windows client** | Each forward opens its own SSH connection, so a password host asks for the password again per forward. Only `localhost`, `127.0.0.1`, and `0.0.0.0` links forward |
| **Host-side cleanup on a Windows host** | Of the four options **Remove *machine*…** offers, two act on the host (**Uninstall Kepler server on the machine** and **Remove deployed key from remote authorized_keys**) and both run through a POSIX shell, so neither works on a Windows host. The two local options are unaffected. Delete `~/.kepler-server` and the `authorized_keys` entry on the host yourself |

***

## Related

- [Settings](/kepler/settings): the **Remote environments** and **Remote Access** pages, and the shortcut list
- [Agent Integrations](/kepler/agent-integrations): signing agents in, including on a remote target
- [Review Changes](/kepler/review-changes): reviewing and shipping the work a remote agent produced

---
