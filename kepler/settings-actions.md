---
title: Action Settings
description: The Actions page of Kepler's Settings, covering preferred Actions per kind of item and the Action list, with a link to the full Actions guide.
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

*Start agent work without retyping prompts: save the ones you use often and run them on a task, issue or pull request.* An **Action** is an editable named prompt. The Actions page has two sections:

| Section | What it holds |
|---|---|
| **Preferred Actions** | *Pick which Action runs when you press the Action button on a task, issue or pull request.* One picker per kind of item: **Tasks**, **Issues**, **Pull requests I authored**, and **Pull requests from others**. Any slot can be **None** |
| **All Actions** | The shipped Actions under **Built in** and yours under **Custom**. Click a row to edit it. A row also offers **Restore default** where you have edited it, and **Delete** on a custom row |

The **All Actions** section header has **New Action**, which creates an Action, and **Restore all defaults**, which discards every edit. An Action you create or edit opens as a sub-page.

Kepler ships four default Actions:

- **Tasks** default to **Implement**.
- **Issues** default to **Plan**.
- Pull requests you authored default to **Address Feedback**.
- Pull requests from others default to **Review**.

For what the built-in Actions ask an agent to do, how the editor's **Title**, **Prompt**, **Applies to**, and **Agent** fields behave, and how an Action picks the agent it runs on, see [Actions](/kepler/actions).

***

---
