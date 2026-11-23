---
title: Settings
description: Open Kepler's Settings over the page you are on or in its own window, find a setting by name, keep or discard unsaved changes, and change settings in a remote window.
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
tags: [settings, configuration, keyboard-shortcuts, appearance, agents, tasks, notifications, updates, mcp-servers, agent-tools, approvals, chat, actions, repositories, worktrees, terminal, voice, dictation, read-aloud, remote, remote-environments, remote-access, logs, gitkraken-dev, integrations, preferences]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Use Settings to change how Kepler, your agents, and your tasks work.

To open Settings, click the gear icon in the top bar, or press **Ctrl/⌘ + ,**. Settings opens over the page you are on. To close it, click **Close**, click outside it, or press **Escape**. The gear icon and **Ctrl/⌘ + ,** close it too.

To make Settings taller or shorter, drag its top or bottom edge. In the desktop app, **Open in new window** in its header moves Settings into a window of its own.

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-general-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-general-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="Settings open on Repositories. The Settings sidebar on the left starts with Search settings and Setup, then lists Account; Agents, Tasks, Repositories, Integrations and Actions; General, Notifications, Appearance, Voice and Keyboard shortcuts; Remote environments and Remote Access; and Updates and Help, with Repositories' section links (Your repos and folders, Worktrees and branches, Projects) expanded under it.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings, open over the Dashboard on Agents.</figcaption>
</figure>

***

## The Settings pages

The Settings sidebar starts with a **Search settings** field and [**Setup**](/kepler/settings-setup-account#setup), a progress ring that reopens the first-run checklist. Below them, it lists these pages:

| Page | What it covers |
|---|---|
| [**Account**](/kepler/settings-setup-account#account) | Who you're signed in as, your organization, and GitKraken AI credits |
| [**Profiles**](/kepler/kepler-profiles) | The profiles on this computer, each with its own tasks, settings, and sign-ins. Desktop app only |
| [**Agents**](/kepler/settings-agents) | Your agents, the agent and mode new sessions start with, custom agents, agent presets, keeping agents running, and idle agents |
| [**Tasks**](/kepler/settings-tasks) | How new tasks start, where tasks open, how a task's page and Dashboard panels look, and task groups |
| [**Repositories**](/kepler/settings-repositories) | Where repositories and worktrees go and how branches are named, your repos and folders, worktrees and branches, and Projects |
| [**Integrations**](/kepler/settings-integrations) | Issue tracker and Git host connections |
| [**Actions**](/kepler/settings-actions) | Suggested Actions per item kind, and the Action list |
| [**Agent tools**](/kepler/settings-agent-tools) | MCP servers, and Kepler's built-in tools your agents can use |
| [**Approvals**](/kepler/settings-approvals) | The rules that approve your agents' actions for you |
| [**General**](/kepler/settings-app#general) | Language, the default editor, sessions started outside Kepler, and windows |
| [**Appearance**](/kepler/settings-app#appearance) | Light or dark appearance and themes, the Dashboard's views, the code font, and diff layout |
| [**Chat and terminal**](/kepler/settings-app#chat-and-terminal) | The chat's send key, width, and scrolling, and the terminal's font, message box, and links |
| [**Notifications**](/kepler/settings-app#notifications) | Which agent events notify you, on the desktop, in Kepler, and on a phone |
| [**Voice**](/kepler/settings-app#voice) | A check of your microphone and speaker, dictation with its models and vocabulary, and read aloud, all on this device |
| [**Keyboard shortcuts**](/kepler/settings-app#keyboard-shortcuts) | Kepler's keyboard shortcuts, and the keys you choose for them |
| [**Remote environments**](/kepler/settings-environment#remote-environments) | The machines your agents can run on, over SSH or WSL |
| [**Remote Access**](/kepler/settings-environment#remote-access) | Opening this Kepler from another device |
| [**Updates**](/kepler/settings-updates-help#updates) | The installed version, app updates, and agent updates |
| [**Help**](/kepler/settings-updates-help#help) | The docs, release notes, onboarding guides, and Kepler's logs |

The account menu also opens **Account**.

### Find a setting

To find a setting by name, start typing when Settings opens: **Search settings** already has focus. Results include single settings, and clicking one opens Settings at its control. Search also matches help text and common synonyms, so a word like *theme* or *notifications* finds the right setting. Type an agent's name to open its page.

When a search result or an Ask Kepler link takes you to a setting, Kepler highlights its control. If the setting is not shown, for example because it depends on something you have not set up yet, Kepler says why.

Ask Kepler can also search Kepler's settings, and change one when you ask. It names the setting as a link you can click. Some changes need your approval first. Settings that hold secrets, such as your account or integrations, can only be linked. See [Finding and changing settings](/kepler/ask-kepler#finding-and-changing-settings).

To jump to a section, use the section links the Settings sidebar shows under the page you have open.

### Sub-pages and unsaved changes

When you open an item to edit it, such as a repository, a project, a custom agent, an MCP server, or an Action, it opens as a sub-page inside its Settings page, with a breadcrumb back to the page.

A sub-page form saves when you click **Save** in its footer. If a save fails, the footer shows why and keeps your edits on the form.

If you leave a sub-page with unsaved changes, however you leave, Kepler asks whether to save them before it discards anything.

Most fields outside those forms save themselves and show their status beside them. If a save fails, Kepler shows the reason, and names the setting if you have already left the page.

**Go back**, or your mouse's back button, closes Settings from any page or sub-page, and returns you to what you were doing before you opened it. To move between Settings pages, use the sidebar or a sub-page's breadcrumb.

### Settings in a remote window

In a window connected to a remote environment, Settings shows that machine's settings, and its header names the machine. Under its title, each page says where its settings are saved:

- **Saved on *machine***: on the remote machine.
- **Saved on this machine**: on your own computer, for every Kepler window on it.

A section that saves somewhere other than its page has its own badge. To change this machine's own settings from a remote window, click **Open this machine's settings** in the header. The same page opens in a local window.

Some settings are kept on your own computer, such as the language, the default editor, the themes, the terminal font, the code font, and the diff layout. If Ask Kepler in a remote window changes one of these, the change applies on your computer, and a notification names it, with **Undo**. See [Finding and changing settings](/kepler/ask-kepler#finding-and-changing-settings).

---
