---
title: Update and Help Settings
description: The Updates and Help pages of Kepler's Settings, covering the installed version and app updates, the docs, release notes, onboarding guides, and Kepler's logs.
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

## Updates

The Updates page has one section, shown without a heading. It's about the app itself:

| Row | What it does |
|---|---|
| **Current version** | The installed version, with **Release notes** beside it to open what's new in that release |
| **Check for updates** | Checks for a newer release and downloads it in the background. Reads **Up to date** when there's nothing newer, and becomes **Check again** |
| Download progress | While a release downloads: **Downloading** with a percentage, how much has arrived out of the total and the speed (*{done} of {total} at {rate}/s*), and the time left (*About {count} min left*). A **Verifying** step follows before it can install |
| **New version** | Appears once a release is ready, with **Restart to update** beside it, and how many running agents a restart would stop |

A ready update also shows as one chip in the top bar, on every screen, whose popover reads **Update ready to install** and says what a restart does to running work. If agents are mid-tool-call when you restart, Kepler shows *Preparing to restart. Finishing {count} active tool calls…* and waits up to 2 minutes. **Restart now** skips the wait.

**Check for updates** in the app menu answers where you are rather than opening this page. The top bar shows **Checking…**, then **Up to date** or the download. On the welcome screen, the version in the corner is itself the check, and a failure there reads **Unable to check for updates** with **Try again**.

After an update, the release notes open on their own in Kepler, once any guided start has ended. A release can lead with a highlights card, *Three things in {version} to try first:*, and each item jumps to its part of the notes.

The update controls only appear in the desktop app. In a browser window connected to Kepler, this page shows nothing to update.

***

***

## Help

*Docs, tips and logs for when something goes wrong.* The Help page has two sections: **Help** and **Logs**.

### Help

This section links out to the docs and release notes, and replays any tip you dismissed:

| Control | What it does |
|---|---|
| **Kepler documentation** | *Guides, keyboard shortcuts, and agent setup.* **Open docs** opens the Kepler docs site in your browser |
| **Release notes** | *See what changed in each version.* **Show release notes** opens them in Kepler, starting with the release's highlights when it has them. See [Updates](#updates) |
| **Show tips and guides again** | A disclosure, closed by default: *Kepler points out a few controls the first time they matter. Show any of those tips again here.* |

Inside the disclosure, each tip has a row that reads **Seen and dismissed** or **Not shown yet**, with its own **Show again** button. A tip that was shown but never dismissed still reads **Not shown yet**. The tips are the following:

- Actions callout
- Todo pointer
- Task page callout
- Panel layout callout

**Reset all onboarding and show everything again**, at the foot of the disclosure, clears every element's dismissed state in one action rather than one row at a time.

### Logs

*To report a problem, save the logs and attach the file.* The following table lists the section's controls:

| Control | What it does |
|---|---|
| **Copy path** | Copies the current log's path to your clipboard |
| **Show in Finder** | Opens the log's folder in your file manager (**Show in Explorer** on Windows, **Show in file manager** on Linux). Hidden where the machine can't open one |
| **Save logs…** | Saves Kepler's logs as a single zip file |
| **Clear log…** | Deletes the current and rotated log files, after a confirmation |

In a window connected to a remote environment, these are that machine's logs: *These are the logs on {machine}.* Saving them from there includes this machine's logs too, and **Show this machine's logs** opens your local ones.

Without opening Settings, **Help → Show Logs in Finder** (**Show Logs in Explorer**, **Show Logs in File Manager**) in the app menu reveals this computer's log.

---
