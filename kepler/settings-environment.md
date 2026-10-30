---
title: Environment Settings
description: Save the machines your Kepler agents run on over SSH or WSL, choose how remote windows load, and open Kepler from a browser or your phone with Remote Access.
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
tags: [settings, remote-environments, ssh, wsl, remote-access, gitkraken-dev]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Use **Settings → Remote environments** to save the machines your agents can run on over SSH or WSL, and to choose how remote windows load. Use **Settings → Remote Access** to open this computer's Kepler from a browser or your phone. To learn how to work in a remote environment day to day, see [Remote Environments](/kepler/remote-environments).

***

## Remote environments

*Run your agents on another machine, like a dev server or cloud VM, while you work from here. Kepler installs itself over SSH, so there's nothing to set up on that machine first.* On Windows, you can also use a WSL distro, with nothing extra to install.

To open this page from anywhere, press **⌘ ⇧ R**, or click **Manage remote environments…** in the remote chip's popover. Kepler saves the machine list on this computer, whichever machine a window is connected to.

The Remote environments page has 3 sections:

| Section | What it holds |
|---|---|
| **Your machines** | Your saved machines. Each row shows whether the machine is connected and how many windows have it open |
| **Found on this machine** | *Machines from your SSH config and WSL that you haven't added yet.* The section appears only while Kepler finds one |
| **Remote windows** | How a window connected to another machine loads its interface. See [Remote windows](#remote-windows) |

In **Your machines**, you can do the following:

- To open a machine in this window, click **Connect**. To open it in a new window, click the button next to **Connect** (*Connect to {name} in a new window*).
- To add a machine by hand, click **Add machine**. On Windows, choose **SSH** or **WSL** in **Machine type**. A WSL machine takes a **Distro** and an optional **Name**.

In **Found on this machine**, you can do the following:

- To save a machine, click **Add**.
- To move a machine out of the list, click **Hide**. Hidden machines appear under **Show hidden ({count})**.

If your plan does not include remote environments, **Add** reads **Try free and add** when a trial is available. Otherwise it reads **Upgrade to add**, which opens the plan page and saves nothing.

To open a saved machine's page, click the machine:

| Control | What it does |
|---|---|
| Name | Rename the machine. You can rename a machine only from a local window |
| **Latency**, **Live sessions** | The connection's current state |
| **Color** | Tints the machine's chip, its popover, and a connected window's top strip, so you can tell machines apart. **None** removes the tint |
| **Mute notifications from {host}** | *Kepler won't show desktop notifications for sessions on {host}. Alerts still appear inside its windows.* |
| **Connection** | Edit the SSH or WSL address. If you enter a new SSH address, Kepler asks you to trust its host key with **Trust and save** |
| **Remove {name}…** | Deletes the saved machine |

To edit the connection of a machine you are connected to, disconnect from it first.

In a window connected to an SSH machine, a **Ports** list shows the ports forwarded from that machine to this computer. You can do the following:

- To forward another port, enter its number.
- To stop forwarding a port, click **Stop**.
- To stop every forwarded port, click **Stop all**. This button appears when more than one port is forwarded.

A window connected to a machine shows the other machines read-only, with the message *To add, edit, or remove machines, open Remote environments in a local window.* To make changes, click **Open in a local window**.

If a window cannot reconnect to its machine, it shows a full-screen recovery screen instead of this page. See [The recovery screen](/kepler/remote-environments#the-recovery-screen).

### Remote windows

The following setting is saved on this machine:

| Setting | What it controls | Default |
|---|---|---|
| **Use this app's interface in remote windows** | *Windows connected to another machine load their interface from this app instead of from that machine, so only your data crosses the connection. If that machine runs a different version of Kepler, its own interface is used.* Experimental, desktop app only | On |

A change to this setting takes effect the next time you connect to a machine that has no other window open.

To learn how to connect, forward ports, and how sessions behave on a machine, see [Remote environments](/kepler/remote-environments).

***

## Remote Access

*Use this machine from any browser or your phone, through a secure GitKraken relay.* You do not need to open a port or set up a tunnel. Remote Access requires a paid GitKraken plan and is not available on the Community plan.

Under **How it works**, the page lists 3 steps:

1. Turn it on and name this machine.
2. Scan the QR code or open the link that appears here, on your phone or any browser.
3. Sign in with your GitKraken account, and this machine's tasks and sessions are there.

### Turning Remote Access on and off

To turn on Remote Access, do the following:

1. Click **Turn on Remote Access**.
2. Enter a name in **Name this machine**.

A status badge shows the connection state: **Connecting…**, **Active**, **Reconnecting…**, **Waiting to reconnect**, **Error**, or **Inactive**. While Remote Access is on, the page shows a QR code (*Scan with your phone camera to open*) and **Copy URL**. The page also shows *This machine stays awake while Remote Access is on.*, with **Change in General**, which opens [Keep agents running](/kepler/settings-app#keep-agents-running).

Remote Access stays on until you turn it off, sign out, or another account signs in.

To turn off Remote Access, click the switch. Kepler asks **Turn off Remote Access?** first, because *Every paired device is disconnected.*

### Reconnecting after a dropped connection

If Remote Access loses the connection, Kepler first retries quickly. It then shows **Waiting to reconnect** and the reason, under **Unable to connect**, with *Kepler retries every 5 minutes.* To retry at once, click **Retry now**. Paired devices stay paired.

These 2 reasons tell you how to fix them:

- *Waiting for a GitKraken sign-in. Remote Access connects as soon as one is available.*
- *Your account has reached its limit of machines with Remote Access on. Remove one you no longer use, then retry.* This message has a **Manage machines on gitkraken.dev** button.

### Managing machines and devices

**Machines on your account** shows *See every machine on your account with Remote Access on, and remove the ones you no longer use.* Its **Manage machines on gitkraken.dev** button appears even while Remote Access is off.

**Connected devices** lists each device that has connected. It marks **This device** and shows when each device was **Last seen**. You can do the following:

- To disconnect one device, click **Revoke**.
- To reload the list, click **Refresh**.

The section notes: *Only you can connect, signed in to your GitKraken account. Turning Remote Access off disconnects every device, and you can revoke any single device under Connected devices.*

A pairing link works once and expires after 5 minutes. A used link shows *This pairing link no longer works*. To pair again, open a new link from the computer running Kepler. To learn about prerequisites, pairing, and managing sessions from gitkraken.dev, see [Remote environments](/kepler/remote-environments).

***

---
