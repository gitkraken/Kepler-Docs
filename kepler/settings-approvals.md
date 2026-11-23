---
title: Approval Settings
description: Manage the rules that approve your Kepler agents' actions for you, and remove a rule so that kind of action asks again.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot, cursor, antigravity, opencode, pi, auggie, grok]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [settings, approvals]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Use **Settings → Approvals** to manage the rules that approve your agents' actions for you. Some actions your agents take wait for your approval, and an action that no rule covers still asks.

When an agent uses Kepler's workspace tools to do something that needs your approval, such as deleting a worktree, sending a prompt to another session, or rewriting a branch, Kepler pins an approval card above that session's message box. To create a rule for that kind of action, choose **Always approve** from the card's **Approve** menu. For an action that can lose work, such as deleting a worktree, Kepler names what is at risk and asks you to confirm first.

Some actions always ask, so their menu has no **Always approve**. For example:

- Adopting a task into another agent's work
- Adding a Run command to a repository, or replacing one
- A setting change that Ask Kepler asks to make
- Starting a session in a more permissive mode

See [Agent Sessions](/kepler/agent-sessions#approval-requests).

## Always approved

**Always approved** lists each rule you create this way, with when and where you added it and how often it has run. **Remove** deletes the rule, so that kind of action asks again.

***

---
