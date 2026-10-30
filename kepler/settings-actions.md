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
status: GA
last_verified: 2026-10
llms_include: true
tags: [settings, actions, preferred-actions]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Use **Settings → Actions** to save the prompts you use often and run them on a task, issue, or pull request without typing them again. An **Action** is an editable named prompt. The page has these sections:

| Section | What it holds |
|---|---|
| **Preferred Actions** | Which Action runs when you press the Action button on a task, issue, or pull request: one picker each for **Tasks**, **Issues**, **Pull requests I authored**, and **Pull requests from others**. Any picker can be **None** |
| **All Actions** | The built-in Actions under **Built in**, and yours under **Custom**. Click a row to edit it, use **Restore default** on a row you have edited, or use **Delete** on a custom row |

To create an Action, click **New Action** in the **All Actions** section header. **Restore all defaults**, beside it, discards every edit. An Action you create or edit opens as a sub-page.

Kepler has 4 built-in Actions, and each one is the default preferred Action for one kind of item:

- **Tasks** default to **Implement**.
- **Issues** default to **Plan**.
- Pull requests you authored default to **Address Feedback**.
- Pull requests from others default to **Review**.

For what the built-in Actions ask an agent to do, how the editor's **Title**, **Prompt**, **Applies to**, and **Agent** fields behave, and how an Action picks the agent it runs on, see [Actions](/kepler/actions).

***

---
