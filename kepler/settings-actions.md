---
title: Action Settings
description: Choose which Action runs on each kind of item in Kepler, and create, edit, restore, or delete the Actions in your list.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: []
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [settings, actions, suggested-actions]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "kepler-configuration"
    nav_label: "Action Settings"
    nav_order: 50
    nav_parent: "kepler-behavior-and-integration-settings"
    page_type: "content"
    card_icon: "bolt"
    card_color: "amber"
    card_description: "Pick the Action for each kind of item, and manage your Actions"
---
<kbd>Last updated: November 2026</kbd>

Use **Settings → Actions** to save the prompts you use often and run them on a task, issue, or pull request without typing them again. An **Action** is an editable named prompt. The page has these sections:

| Section | What it holds |
|---|---|
| **Suggested Actions** | The Action that the button on each kind of item suggests: **Tasks**, **Issues**, **Pull requests I authored**, and **Pull requests from others** |
| **All Actions** | The built-in Actions under **Built in** and yours under **Custom**, each with what it does and where it is available |

Under **Suggested Actions**:

- Set a picker to **None** to leave only the menu on that kind of item.
- **Suggest automatically** switches a new task's button to the suggested Action when you link an issue or pull request to it. Turn it off to keep **Start**.

Under **All Actions**, click a row to edit it, use **Restore default** on a row you have edited, or use **Delete** on a custom row. To delete an Action that an [automation](/kepler/kepler-automations) runs, delete the automation first.

An Action can run with one of your [agent presets](/kepler/settings-agents#agent-presets), and the preset picks the agent. If the Action's preset no longer exists, its row shows **Preset unavailable for this agent** and the Action runs without it. To fix it, choose another preset in the Action's editor.

To create an Action, click **New Action** in the **All Actions** section header. **Restore all defaults**, beside it, discards every edit. An Action you create or edit opens as a sub-page.

Kepler has 4 built-in Actions, and each one is the default suggested Action for one kind of item:

- **Tasks** default to **Implement**.
- **Issues** default to **Plan**.
- Pull requests you authored default to **Address Feedback**.
- Pull requests from others default to **Review**.

For what the built-in Actions ask an agent to do, how the editor's **Title**, **Prompt**, **Available on**, and **Agent** fields behave, and how an Action picks the agent it runs on, see [Actions](/kepler/actions).

***

---
