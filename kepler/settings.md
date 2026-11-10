---
title: Settings
description: Open Kepler's Settings, find a setting by name, keep or discard unsaved changes, and change settings in a remote window.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, bitbucket-data-center, azure-devops, azure-devops-server]
integrations: [claude-code, codex, copilot, cursor, antigravity, opencode, pi, auggie, grok, github, gitlab, bitbucket, azure-devops, jira, jira-data-center, linear, trello]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [settings, configuration, keyboard-shortcuts, appearance, agents, tasks, notifications, updates, mcp-servers, actions, repositories, worktrees, terminal, voice-input, remote, remote-environments, remote-access, logs, gitkraken-dev, integrations, preferences]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Use Settings to change how Kepler, your agents, and your tasks work. Settings has 15 pages, and each one links to its own reference in [The Settings pages](#the-settings-pages).

To open Settings, click the gear icon in the top bar, or press **⌘ ,** (**Ctrl ,** on Windows and Linux). To close it, click the gear icon or press the same shortcut again.

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-general-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-general-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Settings open on Repositories. The Settings sidebar on the left starts with Search settings and Setup, then lists Account; Agents, Tasks, Repositories, Integrations and Actions; General, Notifications, Appearance, Voice input and Keyboard shortcuts; Remote environments and Remote Access; and Updates and Help, with Repositories' section links (Your repos and folders, Worktrees and branches, Projects) expanded under it.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings, open on Repositories.</figcaption>
</figure>

***

## The Settings pages

The Settings sidebar starts with a **Search settings** field and [**Setup**](/kepler/settings-setup-account#setup), a progress ring that reopens the first-run checklist. Below them, it lists these pages:

| Page | What it covers |
|---|---|
| [**Account**](/kepler/settings-setup-account#account) | Who you're signed in as, your organization, what your plan unlocks, and GitKraken AI credits |
| [**Agents**](/kepler/settings-agents) | Your agents, custom agents, MCP servers, agent tools, approvals, and usage limits |
| [**Tasks**](/kepler/settings-tasks) | How new tasks start, including the default agent, and how a task's page looks |
| [**Repositories**](/kepler/settings-repositories) | The repositories folder, your repos and folders, worktrees and branches, and Projects |
| [**Integrations**](/kepler/settings-integrations) | Issue tracker and Git host connections, and sessions started in your own terminal |
| [**Actions**](/kepler/settings-actions) | Suggested Actions per item kind, and the Action list |
| [**General**](/kepler/settings-app#general) | Language, windows, the default editor, keeping agents running, and usage insights |
| [**Notifications**](/kepler/settings-app#notifications) | Which agent events notify you, on the desktop and in Kepler |
| [**Appearance**](/kepler/settings-app#appearance) | Light or dark appearance and themes, the Dashboard's views, the chat, the terminal font, the code font, and diff layout |
| [**Voice input**](/kepler/settings-app#voice-input) | On-device speech-to-text, its transcription engine, and learned words |
| [**Keyboard shortcuts**](/kepler/settings-app#keyboard-shortcuts) | Kepler's keyboard shortcuts |
| [**Remote environments**](/kepler/settings-environment#remote-environments) | The machines your agents can run on, over SSH or WSL |
| [**Remote Access**](/kepler/settings-environment#remote-access) | Opening this Kepler from another device |
| [**Updates**](/kepler/settings-updates-help#updates) | The installed version and app updates |
| [**Help**](/kepler/settings-updates-help#help) | The docs, release notes, onboarding guides, and Kepler's logs |

The account menu also opens **Account**.

### Find a setting

To find a setting by name, start typing when Settings opens: **Search settings** already has focus. Search matches section titles, control labels, help text, and common synonyms, so a word like *theme* or *notifications* finds the right section.

When a search result or an Ask Kepler link takes you to a setting, Kepler highlights its control. If the setting is not shown, for example because it depends on something you have not set up yet, Kepler says why.

Ask Kepler can also search Kepler's settings, and change one when you ask. It names the setting as a link you can click. Some changes need your approval first. Settings that hold secrets, such as your account or integrations, can only be linked. See [Finding and changing settings](/kepler/ask-kepler#finding-and-changing-settings).

To jump to a section, use the section links the Settings sidebar shows under the page you have open. Under **Agents**, the sidebar also lists each supported agent below **Your agents**.

### Sub-pages and unsaved changes

When you open an item to edit it, such as a repository, a project, a custom agent, an MCP server, or an Action, it opens as a sub-page inside its Settings page, with a breadcrumb back to the page.

A sub-page form saves when you click **Save** in its footer. If a save fails, the footer shows why and keeps your edits on the form.

If you leave a sub-page with unsaved changes, however you leave, Kepler asks **Save your changes?** before it discards anything. A form with nothing to save yet, such as a step-by-step add flow, asks **Discard your changes?** instead.

Most fields outside those forms save themselves and show their status beside them. If a save fails, Kepler shows the reason, and names the setting if you have already left the page.

**Back**, or your mouse's back button, steps back through each page, sub-page, and search result you opened in Settings. To leave Settings in one click from any page or sub-page, use the back arrow in the Settings header, the gear icon, or **⌘ ,** (**Ctrl ,**). When the Dashboard's [views](/kepler/settings-app#dashboard) sit **Along the left side**, the back arrow sits at the top of the views column instead. Each one returns you to what you were doing before you opened Settings.

### Settings in a remote window

In a window connected to a remote environment, Settings shows that machine's settings, and its header names the machine. Under its title, each page says where its settings are saved:

- **Saved on {machine}**: on the remote machine.
- **Saved on this machine**: on your own computer, for every Kepler window on it.

A section that saves somewhere other than its page has its own badge. To change this machine's own settings from a remote window, click **Open this machine's settings** in the header. The same page opens in a local window.

Some settings are kept on your own computer, such as the language, the default editor, the themes, the terminal and code fonts, and the diff layout. If Ask Kepler in a remote window changes one of these, the change applies on your computer, and a notification names it, with **Undo**. See [Finding and changing settings](/kepler/ask-kepler#finding-and-changing-settings).

---
