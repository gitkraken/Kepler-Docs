---
title: Actions
description: Actions are editable named prompts you fire at a task, issue, or pull request. Learn the four built-in Actions, how to change them, and how to write your own.
product: Kepler
feature: Actions
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode]
hosted_variant: both
status: GA
last_verified: 2026-08
llms_include: true
tags: [actions, prompts, agents, tasks, issues, pull-requests, settings, customization]
taxonomy:
  category: kepler
---
<kbd>Last updated: August 2026</kbd>

An **Action** is a named prompt you fire at a task, issue, or pull request to start agent work.

<figure>
  <a href="/wp-content/uploads/actions-drop-down.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/actions-drop-down.png" class="help-center-img img-bordered" alt="The Action split button on a Todo row, chevron open, showing Plan, Implement, a custom action, and Manage actions">
  </a>
  <figcaption style="text-align:center; color:#888">The Action split button, chevron open. One click runs the default; the chevron lists every applicable Action, including your own.</figcaption>
</figure>

Every Action is yours to configure. You pick the wording, you pick the agent, and you pick which Action is the one-click default for each kind of work.

***

## The four built-in Actions

Kepler ships with four Actions. Every one of them is editable.

| Action | What it asks the agent to do | Offered on |
|---|---|---|
| **Plan** | Research the code first, write out the proposed approach, change nothing, and wait for your confirmation | Tasks, Issues, Pull requests |
| **Implement** | Read enough surrounding code to be confident, then make the changes directly rather than describing them | Tasks, Issues, Pull requests |
| **Review** | Review the pull request if one is attached, otherwise the uncommitted work in the worktree | Tasks, Pull requests |
| **Address Feedback** | Triage the review comments, apply what's worth applying, and push back on the rest instead of applying every suggestion blindly | Pull requests |

**Kepler deliberately offers Review on plain tasks.** Reviewing your own uncommitted work before you push is the obvious thing to want from a worktree. One flexible Review covers both cases, rather than splitting the list into "review a pull request" and "review my changes."

Every Action declares **what it can be aimed at**, which is why **Address Feedback** never appears on a task with no pull request.

You can edit and reset built-in Actions, but you can't delete them. What an Action applies to already controls where it shows up, so deleting one would be a weaker version of the same control.

<figure>
  <a href="/wp-content/uploads/reset-action-to-default-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/reset-action-to-default-aug-2026.png" class="help-center-img img-bordered" alt="The built-in Plan Action's row in Settings, with reset and edit icons but no delete icon">
  </a>
  <figcaption style="text-align:center; color:#888">A built-in Action's row: reset and edit, no delete.</figcaption>
</figure>

***

## Where the Action button appears

You fire Actions from a **split button**. The left half runs your preferred Action for that surface; the chevron opens the full list.

<div class="table-center" markdown="1">

| Surface | Preferred Action comes from |
|---|---|
| A row in **Todo** (an issue or pull request) | the row's own kind of item |
| The side panel, on the selected item | the selected item's kind |

</div>

Firing an Action from a Todo row is also how an issue or pull request that isn't tracked yet **becomes** a task in Kepler.

<figure>
  <a href="/wp-content/uploads/action-button-todo-row-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/action-button-todo-row-aug-2026.png" class="help-center-img img-bordered" alt="The Action split button, closed, on a Todo row">
  </a>
  <figcaption style="text-align:center; color:#888">The split button on a Todo row: the row's kind of item decides which Action fills the left half.</figcaption>
</figure>

Inside a task, Actions live under the **chevron on the composer's send button** rather than on a split button of their own: type a refinement, then pick the Action to fire it with. See [Create a Task](/kepler/create-task).

<figure>
  <a href="/wp-content/uploads/inside-task-actions-button-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/inside-task-actions-button-aug-2026.png" class="help-center-img img-bordered" alt="The composer's send button inside a task, with its chevron open to the list of Actions">
  </a>
  <figcaption style="text-align:center; color:#888">The Actions chevron on the composer's send button.</figcaption>
</figure>

Task rows don't carry an Action button. A task's own operations live behind the **⋮** menu on the row instead.

A task row has no **Resume** button. Clicking the row selects it and shows its sessions, the way to look at running work without sending anything. Firing an Action on live work takes you to the session that Action landed in instead.

***

## Firing an Action

An Action fires immediately unless Kepler is unclear on where to run the action.

### The left half: one click

The left half of the button runs your preferred Action straight away, in the current session if one exists. It only stops to ask when the task has **two or more worktrees**.

The number of issues or pull requests attached to the task doesn't change what the Action does. An Action's prompt is its own content, word for word, and every attached item ships to the agent as shared context. All of it is the work. If you want the agent to look at one thing first, say so in the prompt box or in the chat; that's one sentence, and it's better in your own words.

### The chevron: the deliberate path

Picking an Action from the chevron list always goes on to ask where to run it, whenever there is anything at all to choose, including new-session-vs-current on a task with a single worktree, which the left half answers silently.

At the bottom of the list, **Manage actions…** opens **Settings → Actions**.

### Choosing where it runs

The **Run in** view asks two independent questions, and both have small answers.

<figure>
  <a href="/wp-content/uploads/run-in-view-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/run-in-view-aug-2026.png" class="help-center-img img-bordered" alt="The Run in view, asking which session and which worktree to use">
  </a>
  <figcaption style="text-align:center; color:#888">The Run in view.</figcaption>
</figure>

**New session, or a current one?** A two-way toggle between **New session** and **Current session**. *Current session* lists every reusable session with its worktree, so clicking a row queues the Action into that exact session.

**Which worktree?** In *New session*, the rows are **All N worktrees**, **A new worktree**, and then one row per branch. In *Current session*, individual sessions replace branches that already have sessions.

Clicking any row **runs the Action** immediately, with no separate confirm step.

Two things worth knowing:

- **A worktree with no session open still runs** under *Current session*. It starts one there, so *all worktrees* always means all of them.
- **Kepler navigates to the first destination you picked**, not to whichever session happened to start first.

Worktree choices are resolved against worktrees that actually exist on disk, so a task that still names a worktree you've since removed won't silently run somewhere else.

### Firing into a running session

Firing into a live session **queues** the prompt behind whatever the agent is currently doing. Nothing is dropped and nothing is cancelled, and Kepler takes you to the session the prompt went into.

<figure>
  <a href="/wp-content/uploads/firing-into-a-running-session-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/firing-into-a-running-session-aug-2026.png" class="help-center-img img-bordered" alt="A prompt queued behind an agent's current work in a running session">
  </a>
  <figcaption style="text-align:center; color:#888">A prompt queued into a running session.</figcaption>
</figure>

***

## Set your preferred Actions

Open **Settings → Actions → Preferred actions**. 

<figure>
  <a href="/wp-content/uploads/preferred-actions-settings-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/preferred-actions-settings-aug-2026.png" class="help-center-img img-bordered" alt="The Preferred actions settings, with a row per item kind and its default Action">
  </a>
  <figcaption style="text-align:center; color:#888">The Preferred actions settings.</figcaption>
</figure>

Each row sets the Action that the left half of the button runs for that kind of item.

<div class="table-center" markdown="1">

| Setting | Default |
|---|---|
| **Tasks** | Implement |
| **Issues** | Plan |
| **Pull requests I authored** | Address Feedback |
| **Pull requests from others** | Review |

</div>

Pull requests split by **who wrote them**, not by what you want to do with them. Kepler works out review-vs-address-feedback from authorship, so the settings name the *kind of pull request* rather than the intent. When you want the other one, it's one click away in the chevron.

Any slot can be set to **None**. This simplifies the action button to only display the chevron icon.

<figure>
  <a href="/wp-content/uploads/set-to-none-action-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/set-to-none-action-aug-2026.png" class="help-center-img img-bordered" alt="A preferred-action slot set to None, showing only the chevron on that surface">
  </a>
  <figcaption style="text-align:center; color:#888">A slot set to None, leaving only the chevron.</figcaption>
</figure>

<figure>
  <a href="/wp-content/uploads/chevron-set-to-none-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/chevron-set-to-none-aug-2026.png" class="help-center-img img-bordered" alt="A row's Action button showing only the chevron, with no preferred Action set">
  </a>
  <figcaption style="text-align:center; color:#888">The chevron-only button on a row with no preferred Action.</figcaption>
</figure>

***

## Edit an Action

In **Settings → Actions**, click the **Edit** (pencil) icon on any Action.

<figure>
  <a href="/wp-content/uploads/actions-settings-built-in-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/actions-settings-built-in-aug-2026.png" class="help-center-img img-bordered" alt="The Actions settings, with the Edit pencil icon on an Action row">
  </a>
  <figcaption style="text-align:center; color:#888">The Edit icon on an Action row in Settings.</figcaption>
</figure>

Built-in Actions appear under **Built in**; your own appear under **Custom**.

| Field | What it does |
|---|---|
| **Title** | The name shown on the button and in the chevron list |
| **Prompt** | Sent to the agent word for word. Point it at a skill you already maintain if you'd rather not paste a prompt |
| **Applies to** | **Tasks**, **Issues**, **Pull requests**: controls where the Action is offered |
| **Agent** | Which agent runs it. See below |

### Create your own

Click **New action**.

<figure>
  <a href="/wp-content/uploads/new-custom-action-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-custom-action-aug-2026.png" class="help-center-img img-bordered" alt="The New action editor for creating a custom Action">
  </a>
  <figcaption style="text-align:center; color:#888">The New action editor.</figcaption>
</figure>

Custom Actions work exactly like the built-in ones, and they're the point of the feature: if you'd do something more than once (backport a fix, write the migration, audit a dependency bump), it should be a button rather than a prompt you retype.

<figure>
  <a href="/wp-content/uploads/new-custom-action-config-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-custom-action-config-aug-2026.png" class="help-center-img img-bordered" alt="A custom Action's configuration, with its title, prompt, and applies-to settings">
  </a>
  <figcaption style="text-align:center; color:#888">A custom Action's configuration.</figcaption>
</figure>

### Restore defaults

**Restore default** on a row, or **Restore all defaults** at the bottom of the list.

Kepler stores **only what you changed**, not a copy of the whole Action. This creates the following considerations when restoring defaults:

- An Action you've never edited picks up improved wording in a future Kepler release.
- **Restore default** works by forgetting your edit. Editing an Action back to its original wording has the same effect.

Deleting a custom Action that a preferred-Action slot points to is the same as setting it to **None**. You will see rows with only the chevron, instead of the preferred-Action + the chevron. Revisit the Actions setting to set a new preference. 

***

## Setting an Action's agent

By default an Action runs on your **default agent**, configured in **Settings → Agents**. The **Agent** field in the Action editor reads **Inherit** until you name one.

<figure>
  <a href="/wp-content/uploads/inherit-default-agent-setting-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/inherit-default-agent-setting-aug-2026.png" class="help-center-img img-bordered" alt="The Agent field in the Action editor, reading Inherit">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent field, reading Inherit.</figcaption>
</figure>

Naming an agent is an **all-or-nothing override**: it pins the provider, account, model, mode, and options together, rather than changing one of them and inheriting the rest. This is what makes per-Action cost tuning work: a cheap, fast model for triage and review, a heavier one for implementation.

Three rules govern which agent actually runs:

- A model belongs to its provider, so a pinned model never runs on a different agent.
- If an Action names an agent you don't have installed, the override falls back **whole** to your default agent.
- **An agent you pick explicitly at the point of firing beats an Action's override.**

---
