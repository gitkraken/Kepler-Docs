---
title: Settings
description: An overview of Kepler's Settings, covering the 15 Settings pages and where each is documented, finding a setting by name or id, sub-pages and unsaved changes, settings in a remote window, and deep links, setting anchors and kepler://settings links.
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
last_verified: 2026-10
llms_include: true
tags: [settings, configuration, keyboard-shortcuts, appearance, agents, tasks, notifications, updates, mcp-servers, actions, repositories, worktrees, terminal, voice-input, remote, remote-environments, remote-access, logs, gitkraken-dev, integrations, preferences]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Settings has 15 pages, each with its own sections. These docs follow the rail's groups: one page for Setup and Account, one for each page of the work group, one for the app pages, one for the environment pages, and one for Updates and Help. Each describes what every setting controls, what it defaults to, and what changes when you change it. This page covers what the pages share.

Open Settings from the gear icon in the top bar, or with **⌘ ,** (**Ctrl ,** on Windows and Linux). The same shortcut closes Settings again, the way the gear button does.

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-general-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-general-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Settings open on Repositories. The left rail starts with Search settings and Setup, then lists Account; Agents, Tasks, Repositories, Integrations and Actions; General, Notifications, Appearance, Voice input and Keyboard shortcuts; Remote environments and Remote Access; and Updates and Help, with Repositories' section links expanded under it.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings, open on Repositories.</figcaption>
</figure>

***

## The Settings pages

The left rail starts with a **Search settings** field and [**Setup**](/kepler/settings-setup-account#setup), a progress ring that reopens the first-run checklist. Below them, the rail lists the pages in five unlabeled groups, separated by thin lines. The following table lists the pages in rail order:

| Page | What it covers |
|---|---|
| [**Account**](/kepler/settings-setup-account#account) | Who you're signed in as, your organization, what your plan unlocks, and GitKraken AI credits |
| [**Agents**](/kepler/settings-agents) | Your agents, custom agents, MCP servers, agent tools, approvals, and usage limits |
| [**Tasks**](/kepler/settings-tasks) | How new tasks start, including the default agent and the agent new sessions start with, and how a task's page looks |
| [**Repositories**](/kepler/settings-repositories) | The repositories folder, your repos and folders, worktrees and branches, and Projects |
| [**Integrations**](/kepler/settings-integrations) | Issue tracker and Git host connections, and sessions started in your own terminal |
| [**Actions**](/kepler/settings-actions) | Preferred Actions per item kind, and the Action list |
| [**General**](/kepler/settings-app#general) | Language, windows, the default editor, and keeping agents running |
| [**Notifications**](/kepler/settings-app#notifications) | Which agent events notify you, on the desktop and in Kepler |
| [**Appearance**](/kepler/settings-app#appearance) | Light or dark appearance and themes, the chat, the terminal font, code font size, and diff layout |
| [**Voice input**](/kepler/settings-app#voice-input) | On-device speech-to-text, its transcription engine, and learned words |
| [**Keyboard shortcuts**](/kepler/settings-app#keyboard-shortcuts) | Kepler's keyboard shortcuts |
| [**Remote environments**](/kepler/settings-environment#remote-environments) | The machines your agents can run on, over SSH or WSL |
| [**Remote Access**](/kepler/settings-environment#remote-access) | Opening this Kepler from another device |
| [**Updates**](/kepler/settings-updates-help#updates) | The installed version and app updates |
| [**Help**](/kepler/settings-updates-help#help) | The docs, release notes, onboarding guides, and Kepler's logs |

**Account** is first because it's the only page about the *person* rather than the app, and it's where the account menu hands off to.

### Find a setting

To find a setting by name, type in **Search settings**. Search matches section titles, control labels, help text, and common synonyms, so a word like *theme* or *notifications* finds the right section. With no match, the results read *No settings match "{query}"*.

To go straight to one setting, type `@id:` followed by its id, such as `@id:terminal.font-size`. The id is matched in any case. The results show that one setting, named under its page and section, and choosing it opens the page on that control. An id this version doesn't have reads *No setting has that id.* Setting ids are the same ones [settings links](#deep-links-and-section-anchors) use.

<figure style="text-align:center">
  <a href="/wp-content/uploads/settings-search-id-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/settings-search-id-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Settings rail's Search settings field holding @id:terminal.font-size beside its Clear search button, with a single result in place of the page list: Font size, under Appearance › Terminal.">
  </a>
  <figcaption style="text-align:center; color:#888">Finding one setting by its id.</figcaption>
</figure>

Ask Kepler and your agents can search Kepler's settings too, and change one when you ask. They link you to a setting with a [settings link](#deep-links-and-section-anchors). Some changes ask for your approval first, and settings that hold secrets, such as your account or integrations, can only be linked. See [Finding and changing settings](/kepler/ask-kepler#finding-and-changing-settings).

Under the page you have open, the rail lists that page's main sections so you can jump to one. Under **Agents**, the rail also lists each supported agent below **Your agents**. A page with fewer than two listed sections shows no list.

### Sub-pages and unsaved changes

Item editors open as sub-pages inside their Settings page, with a breadcrumb back to the page. Examples include a repository, a project, a custom agent, an MCP server, and an Action.

If you leave a sub-page with unsaved changes, Kepler asks before it discards anything. It asks on every way out: **Escape**, **Back**, the form's own **Cancel**, a page in the Settings rail, or a link elsewhere in the app:

- A form that can save asks **Save your changes?**, with **Cancel**, **Don't save**, and **Save**.
- A form that has nothing to save yet, such as a step-by-step add flow, asks **Discard your changes?**, with **Keep editing** and **Discard**.

A form with a **Save** button keeps it in a footer with **Cancel**. While you have unsaved edits, the footer reads *Unsaved changes*. If a save fails, the footer shows why and keeps your edits on the form. A save that succeeds confirms with *Saved {name}*.

Most fields outside those forms save themselves. Each one shows its own status beside it: **Saving**, **Saved**, or **Unable to save** with the reason. A switch shows only **Saving** and a failure. If a save fails after you've left the page, Kepler tells you which setting it was: *Unable to save {label}*.

Each page, sub-page, or search result you open in Settings is a step of its own, so **Back**, or your mouse's back button, walks back through the pages you visited. To leave Settings in one click from any page or sub-page, use the back arrow in the Settings header, the gear icon, or **⌘ ,** (**Ctrl ,**). Each returns you to whatever you were doing before you opened Settings.

### Settings in a remote window

In a window connected to a remote environment, Settings shows that machine's settings, and its header names the machine. Each page states under its title where its settings are saved: **Saved on {machine}** or **Saved on this machine**. A section that saves somewhere other than its page carries its own badge. The **Saved on this machine** tooltip reads *Applies to every Kepler window on this machine, whichever machine it's connected to.* To change this machine's own settings from such a window, click **Open this machine's settings** in the header: it opens the same page in a local window.

Some settings are kept on your own computer, such as the language, the default editor, the themes, the terminal and code fonts, and the diff layout. When Ask Kepler or an agent in a remote window changes one of these, the window applies the change on your computer, the same as its Settings page would. A notification names the change, with **Undo**. See [Finding and changing settings](/kepler/ask-kepler#finding-and-changing-settings).

### Deep links and section anchors

Every section has a stable anchor id. A link of the form `/settings/<page>#<section-id>` opens that page and scrolls to the section.

A bare `/settings` opens the last page that window had open, or **Agents** if there's none. Legacy links of the form `/settings#<section-id>` still work: Kepler resolves the id to the page that owns that section and keeps the hash. An id that no page owns anymore, such as `general`, `windows-and-notifications`, `keyboard-shortcuts`, or `features`, opens **Agents**.

The following table lists each page's path with its section anchors, in page order:

| Page path | Section anchors, in page order |
|---|---|
| `/settings/account` | `account`, `plan-features`, `ai-credits` |
| `/settings/agents` | `agents`, `ask-kepler`, `custom-agents`, `mcp-servers`, `agent-git-tools`, `approvals`, `usage-limits` |
| `/settings/tasks` | `new-tasks`, `default-agent`, `task-page` |
| `/settings/repositories` | `repositories-root`, `repositories`, `worktrees`, `projects` |
| `/settings/integrations` | `provider-integrations`, `agent-options` |
| `/settings/actions` | `preferred-actions`, `action-list` |
| `/settings/general` | `language`, `windows`, `default-editor`, `keep-running` |
| `/settings/notifications` | `system-notifications` |
| `/settings/appearance` | `appearance`, `transcript`, `terminal`, `code`, `diff-view` |
| `/settings/voice` | `voice`, `voice-engine`, `voice-dictation`, `voice-learned` |
| `/settings/keyboard-shortcuts` | `shortcuts-general`, `shortcuts-navigation`, `shortcuts-dashboard`, `shortcuts-task-page`, `shortcuts-chat`, `shortcuts-changes` |
| `/settings/remote-environments` | `remote-environments`, `found-machines`, `remote-windows` |
| `/settings/remote-access` | `remote-access` |
| `/settings/updates` | `updates` |
| `/settings/help` | `onboarding-help`, `logs` |

`default-agent` sits inside **New tasks** rather than being a section of its own. From the rail or search, `worktrees` opens the **Worktrees and branches** sub-page instead of scrolling to its row. Each agent also gets its own anchor on the Agents page, `agent-<agent-id>`, for example `agent-claude-code`, and each custom agent gets `custom-agent-row-<id>`.

Likewise, `ask-kepler` isn't a section of its own: it marks the default agent picker for Ask Kepler at the top of the [Agents page](/kepler/settings-agents).

Each setting's control has an anchor of its own, `setting-<id>`, where `<id>` is the setting's id, for example `/settings/appearance#setting-terminal.font-size`.

When search, a link, or a pointer on another page sends you to one setting, Kepler waits for its control to load, marks it as you arrive, then fades the mark, and moves focus to it. If the control sits in a collapsed part of the page, such as an agent's program and data folder, Kepler opens that part first. If the control doesn't appear, Kepler explains why instead:

- An agent setting the agent's card doesn't show reads *This agent shows that setting only when it is turned on and supports it.*
- A setting that depends on something else reads *This setting appears once what it depends on is set up.*
- Otherwise, Kepler fills **Search settings** with `@id:<id>`, so you can see where the setting lives.

#### Settings links

A `kepler://` link opens Settings from anywhere: another app, a terminal, or an agent's reply in Kepler, where it's clickable.

| Link | Opens |
|---|---|
| `kepler://settings` | Settings |
| `kepler://settings/<id>` | Settings on one setting's control, for example `kepler://settings/terminal.font-size` |

A setting id is a list of lowercase words separated by dots, and a link matches it in any case. A settings link only opens Settings: it never changes a setting, and a value added to the link is ignored. A link to an id this version of Kepler doesn't have opens Settings with *That setting isn't in this version of Kepler.*

---
