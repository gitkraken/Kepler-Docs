---
title: Environment Settings
description: The Remote environments and Remote Access pages of Kepler's Settings, covering the machines your agents can run on over SSH or WSL, remote windows, and opening this Kepler from another device.
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

The fourth group of the Settings rail is about where Kepler runs: on other machines, and from other devices. For how to work in a remote environment day to day, see [Remote Environments](/kepler/remote-environments).

***

## Remote environments

*Run your agents on another machine, like a dev server or cloud VM, while you work from here. Kepler installs itself over SSH, so there's nothing to set up on that machine first.* On Windows, a WSL distro works too, and needs nothing extra.

**⌘ ⇧ R** opens this page from anywhere, and so does **Manage remote environments…** in the remote chip's popover. The saved machine list lives on this computer, whichever machine a window is connected to.

The Remote environments page has three sections:

| Section | What it holds |
|---|---|
| **Your machines** | Your saved machines, each row showing whether it's connected and how many windows have it open. **Connect** opens it here, and the second button opens it in a new window. **Add machine** adds one by hand. On Windows, **Machine type** chooses **SSH** or **WSL**. A WSL machine takes a **Distro** and an optional **Name** |
| **Found on this machine** | *Machines from your SSH config and WSL that you haven't added yet.* Each has **Add**, or **Hide** to tuck it under **Show hidden ({count})**. On a plan without remote environments, **Add** reads **Try free and add** where a trial is open, or **Upgrade to add**, which opens the plan page and saves nothing. Shown only while something is found |
| **Remote windows** | How a window connected to another machine loads its interface. See below |

Click a saved machine to open its page:

| Control | What it does |
|---|---|
| Name | Rename the machine. Renaming is only possible from a local window |
| **Latency**, **Live sessions** | The connection's current state |
| **Color** | Tints the machine's chip, its popover, and a connected window's top strip, so you can tell machines apart. **None** leaves it plain |
| **Mute notifications from {host}** | *Kepler won't show desktop notifications for sessions on {host}. Alerts still appear inside its windows.* |
| **Connection** | Edit the SSH or WSL address. A new SSH address asks you to trust its host key, with **Trust and save**. Disconnect first to edit a machine you're connected to |
| **Remove {name}…** | Deletes the saved machine |

In a window connected to an SSH machine, a **Ports** list shows the ports forwarded from that machine to this computer. Forward another by number, **Stop** one, or **Stop all** when more than one is forwarded.

A window connected to a machine lists the others read-only: *To add, edit, or remove machines, open Remote environments in a local window.* Use **Open in a local window** to do so.

If a window can't get back to its machine, it shows a full-screen recovery screen instead of opening this page. See [The recovery screen](/kepler/remote-environments#the-recovery-screen).

### Remote windows

The following setting is saved on this machine:

| Setting | What it controls | Default |
|---|---|---|
| **Use this app's interface in remote windows** | *Windows connected to another machine load their interface from this app instead of from that machine, so only your data crosses the connection. If that machine runs a different version of Kepler, its own interface is used.* Experimental. Desktop app only | On |

The setting applies the next time you connect to a machine with no other window open on it.

See [Remote environments](/kepler/remote-environments) for connecting, port forwarding, and how sessions behave on a machine.

***

***

## Remote Access

*Use this machine from any browser or your phone, through a secure GitKraken relay.* No open port and no tunnel to set up yourself. Remote Access requires a paid GitKraken plan and isn't available on the Community plan.

The page explains **How it works** in three steps:

1. Turn it on and name this machine.
2. Scan the QR code or open the link that appears here, on your phone or any browser.
3. Sign in with your GitKraken account, and this machine's tasks and sessions are there.

To turn it on, click **Turn on Remote Access**, then enter a name in **Name this machine**. A status badge shows its state: **Connecting…**, **Active**, **Reconnecting…**, **Waiting to reconnect**, **Error**, or **Inactive**. While it's on, the page shows a QR code (*Scan with your phone camera to open*) and **Copy URL**. *This machine stays awake while Remote Access is on.* links to [Keep agents running](/kepler/settings-app#keep-agents-running) with **Change in General**.

Remote Access stays on until you turn it off, sign out, or another account signs in. If it loses the connection, Kepler retries quickly, then shows **Waiting to reconnect** with the reason, under **Unable to connect**. *Kepler retries every 5 minutes.* **Retry now** tries at once, and paired devices stay paired. Two cases name their own fix:

- *Waiting for a GitKraken sign-in. Remote Access connects as soon as one is available.*
- *Your account has reached its limit of machines with Remote Access on. Remove one you no longer use, then retry.*, with **Manage machines on gitkraken.dev**.

To turn it off, use the switch. Kepler asks **Turn off Remote Access?** first, because *Every paired device is disconnected.*

**Machines on your account**: *See every machine on your account with Remote Access on, and remove the ones you no longer use.* Its **Manage machines on gitkraken.dev** button shows even while Remote Access is off.

**Connected devices** lists each device that has connected, marking **This device** and when each was **Last seen**, with **Revoke** to disconnect one device and **Refresh** to reload the list. *Only you can connect, signed in to your GitKraken account. Turning Remote Access off disconnects every device, and you can revoke any single device under Connected devices.*

A pairing link works once and expires after 5 minutes. A spent one reads *This pairing link no longer works*, so open a new link from the computer running Kepler. See [Remote environments](/kepler/remote-environments) for prerequisites, pairing, and managing sessions from gitkraken.dev.

***

---
