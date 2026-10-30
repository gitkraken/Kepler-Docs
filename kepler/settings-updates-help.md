---
title: Update and Help Settings
description: Check your Kepler version and install updates, open the docs and release notes, show onboarding tips again, and save Kepler's logs to report a problem.
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
tags: [settings, updates, help, release-notes, onboarding, logs]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Use **Updates** to see which version of Kepler you have and to install a new one. Use **Help** to open the docs and release notes, see dismissed tips again, and save Kepler's logs when you need to report a problem.

## Updates

The **Updates** page has these rows:

| Row | What it does |
|---|---|
| **Current version** | The installed version, with **Release notes** beside it to open what's new in that release |
| **Check for updates** | Checks for a newer release and downloads it in the background. Reads **Up to date** when there is nothing newer, and becomes **Check again** |
| Download progress | While a release downloads: **Downloading** with a percentage, how much has arrived out of the total and the speed (*{done} of {total} at {rate}/s*), and the time left (*About {count} min left*). A **Verifying** step follows before it can install |
| **New version** | Appears once a release is ready, with **Restart to update** beside it, and how many running agents a restart would stop |

When an update is ready, a chip also appears in the top bar on every screen. Its popover reads **Update ready to install** and says what a restart does to running work. If agents are in the middle of a tool call when you restart, Kepler shows *Preparing to restart. Finishing {count} active tool calls…* and waits up to 2 minutes. To skip the wait, click **Restart now**.

**Check for updates** in the app menu shows its result where you are, without opening Settings. The top bar shows **Checking…**, then **Up to date** or the download. On the welcome screen, click the version in the corner to check. If that check fails, it reads **Unable to check for updates** with **Try again**.

After an update, the release notes open in Kepler by themselves, once any guided start has ended. A release can start with a highlights card, *Three things in {version} to try first:*, and each item opens its part of the notes.

The update controls appear only in the desktop app. In a browser window connected to Kepler, the **Updates** page has nothing to update.

***

## Help

Use **Help** to find the docs and release notes, see tips again, and save logs when something goes wrong.

### Help

The **Help** section links to the docs and release notes, and shows again any tip you dismissed:

| Control | What it does |
|---|---|
| **Kepler documentation** | *Guides, keyboard shortcuts, and agent setup.* **Open docs** opens the Kepler docs site in your browser |
| **Release notes** | *See what changed in each version.* **Show release notes** opens them in Kepler, starting with the release's highlights when it has them. See [Updates](#updates) |
| **Show tips and guides again** | A disclosure, closed by default: *Kepler points out a few controls the first time they matter. Show any of those tips again here.* |

Inside the disclosure, each tip has a row that reads **Seen and dismissed** or **Not shown yet**, with its own **Show again** button. A tip that Kepler showed but you never dismissed still reads **Not shown yet**. The tips are the following:

- **Actions callout**
- **Todo pointer**
- **Task page callout**
- **Panel layout callout**

To show every tip again at once, instead of 1 row at a time, click **Reset all onboarding and show everything again** at the bottom of the disclosure.

### Logs

To report a problem, save the logs and attach the file. The **Logs** section has these controls:

| Control | What it does |
|---|---|
| **Copy path** | Copies the current log's path to your clipboard |
| **Show in Finder** | Opens the log's folder in your file manager (**Show in Explorer** on Windows, **Show in file manager** on Linux). Hidden where the machine cannot open a file manager |
| **Save logs…** | Saves Kepler's logs as a single zip file |
| **Clear log…** | Deletes the current and rotated log files, after a confirmation |

In a window connected to a remote environment, the section shows the remote machine's logs: *These are the logs on {machine}.* Saving them from there includes this machine's logs too. To open your local logs, click **Show this machine's logs**.

To find this computer's log without opening Settings, use **Help → Show Logs in Finder** (**Show Logs in Explorer**, **Show Logs in File Manager**) in the app menu.

---
