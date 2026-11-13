---
title: Actions
description: Actions are editable named prompts you fire at a task, issue, or pull request. Learn the 4 built-in Actions, how to change them, how to write your own, and how to have a different agent review the code than the one that wrote it.
product: Kepler
feature: Actions
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, azure-devops]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode, grok, pi, antigravity]
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [actions, prompts, agents, tasks, issues, pull-requests, settings, customization]
taxonomy:
  category: kepler
custom_fields:
    entry_title: "Change the prompts, or write your own"
    entry_role: "Customize"
    entry_desc: "Edit the built-in Actions, or write your own named prompts"
    entry_order: 40
    nav_category: "kepler-core-concepts"
    nav_label: "Actions"
    nav_order: 30
    nav_parent: "kepler-core-concepts"
    page_type: "content"
    card_icon: "bolt"
    card_color: "purple"
    card_description: "Editable named prompts you fire at a task, issue or pull request"
---
<kbd>Last updated: November 2026</kbd>

An **Action** is a named prompt you fire at a task, issue, or pull request to start agent work.

<figure style="text-align:center">
  <a href="/wp-content/uploads/actions-drop-down.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/actions-drop-down.png" class="help-center-img img-bordered" alt="The Action split button on a Todo row, chevron open, showing Plan, Implement, a custom action, and Manage actions">
  </a>
  <figcaption style="text-align:center; color:#888">The Action split button, chevron open. One click runs the default; the chevron lists every applicable Action, including your own.</figcaption>
</figure>

You can change every Action's wording and agent, and choose which Action each kind of work suggests as its one-click default. An [automation](/kepler/automations) can also run an Action for you, on a schedule or when new GitHub or Jira activity matches its query.

***

## The four built-in Actions

Kepler comes with 4 Actions, and you can edit each of them.

| Action | What it asks the agent to do | Available on |
|---|---|---|
| **Plan** | Research the code first, write out the proposed approach, change nothing, and wait for your confirmation | Tasks, Issues, Pull requests |
| **Implement** | Read enough surrounding code to be confident, then make the changes directly rather than describing them | Tasks, Issues, Pull requests |
| **Review** | Review the pull request if one is attached, otherwise the uncommitted work in the worktree | Tasks, Pull requests |
| **Address Feedback** | Triage the review comments, apply what's worth applying, and push back on the rest instead of applying every suggestion blindly | Pull requests |

**Address Feedback** never appears on a task with no pull request.

You can edit and reset built-in Actions, but you cannot delete them.

<figure style="text-align:center">
  <a href="/wp-content/uploads/reset-action-to-default-aug-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/reset-action-to-default-aug-2026-v3@2x.png" class="help-center-img img-bordered" alt="The built-in Review Action's row in Settings › Actions after its prompt was edited: the edited prompt, Please review the code changes in this worktree. Check for bugs and missing tests…, over Available on tasks and pull requests, with a restore icon beside its chevron and no delete icon.">
  </a>
  <figcaption style="text-align:center; color:#888">An edited built-in Action's row: Restore default, no delete.</figcaption>
</figure>

***

## Where the Action button appears

You fire Actions from a **split button**. The left half runs the Action suggested for that surface; the chevron opens the full list.

<div class="table-center" markdown="1">

| Surface | Suggested Action comes from |
|---|---|
| A row in **Todo** (an issue or pull request) | the row's own kind of item |
| The side panel, on the selected item | the selected item's kind |

</div>

Firing an Action from a Todo row is also how an issue or pull request that is not tracked yet **becomes** a task in Kepler.

On a narrow card, the button shrinks to a play icon. On a phone, a row has a single **⋮** menu instead that lists every Action.

In the list of Actions, hover a row, or move focus to it, to read that Action's prompt.

<figure style="text-align:center">
  <a href="/wp-content/uploads/action-button-todo-row-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/action-button-todo-row-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="The right end of a Todo issue row: acme-web, Open, the age 3d, and the Plan Action button at rest as an outline, its chevron on the right opening the list of Actions.">
  </a>
  <figcaption style="text-align:center; color:#888">The split button on a Todo row: the row's kind of item decides which Action fills the left half.</figcaption>
</figure>

Inside a task, Actions are under the **chevron on the composer's send button**: type a refinement, then pick the Action to fire it with. In a composer that starts something new, such as the **New task** composer or a panel's draft, picking an Action does not fire it. It sets the main button to that Action, and the agent pill shows the Action's own agent, if it names one. See [Create a task](/kepler/create-task#from-the-new-task-composer).

<figure style="text-align:center">
  <a href="/wp-content/uploads/inside-task-actions-button-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/inside-task-actions-button-aug-2026.png" class="help-center-img img-bordered" alt="The composer's send button inside a task, with its chevron open to the list of Actions">
  </a>
  <figcaption style="text-align:center; color:#888">The Actions chevron on the composer's send button.</figcaption>
</figure>

Task rows do not carry an Action button. A task's own operations are in the **⋮** menu on its row.

***

## Firing an Action

An Action runs at once, unless Kepler needs you to choose where it runs.

### The left half: one click

The left half of the button runs the suggested Action straight away, in the current session if one exists. It stops to ask only when the task has **2 or more worktrees**.

The number of issues or pull requests attached to the task does not change what the Action does. Kepler sends the Action's prompt word for word, and every attached item reaches the agent as shared context. To have the agent look at one item first, say so in the prompt box or in the chat.

### The chevron: the deliberate path

An Action you pick from the chevron list asks where to run it whenever there is a choice, even between a new session and the current one.

At the bottom of the list, **Manage Actions…** opens **Settings → Actions**.

From the keyboard, the two halves are separate **Tab** stops, the Action first. **Down Arrow** or **Alt+Down** on the Action opens the list too, and closing the list puts focus back on the Action. Every split button in Kepler (**Send**, **Open in**, **Run**) works the same way.

### Choosing where it runs

The **Run in** view asks 2 separate questions.

<figure style="text-align:center">
  <a href="/wp-content/uploads/run-in-view-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/run-in-view-aug-2026.png" class="help-center-img img-bordered" alt="The Run in view, asking which session and which worktree to use">
  </a>
  <figcaption style="text-align:center; color:#888">The Run in view.</figcaption>
</figure>

**New session, or a current one?** A two-way toggle between **New session** and **Current session**. *Current session* lists every reusable session with its worktree, so clicking a row queues the Action into that exact session.

**Which worktree?** In *New session*, the rows are **All N worktrees**, **A new worktree**, and then one row per branch. In *Current session*, individual sessions replace branches that already have sessions.

Clicking any row **runs the Action** immediately, with no separate confirm step.

When an Action runs on several worktrees, Kepler takes you to the first one you picked. Under *Current session*, a worktree with no open session gets a new one, so **All N worktrees** always means all of them.

A task with no worktree runs the Action in a folder attached to it, or else in the task's own folder. With neither, Kepler tells you it has nowhere to start a session.

### Firing into a running session

Firing into a live session **queues** the prompt behind whatever the agent is currently doing. Nothing is dropped and nothing is canceled, and Kepler takes you to the session the prompt went into.

<figure style="text-align:center">
  <a href="/wp-content/uploads/firing-into-a-running-session-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/firing-into-a-running-session-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="A running session in a task's side panel: the agent's plan at 1 of 3, its turn still running on Run npm test, and below it 1 queued with Interrupt & send and Clear queue, holding the prompt Also cover gift card codes with surrounding spaces. The composer reads Type a message to queue….">
  </a>
  <figcaption style="text-align:center; color:#888">A prompt queued into a running session.</figcaption>
</figure>

***

## Set your suggested Actions

To choose the Action each kind of item suggests, open **Settings → Actions → Suggested Actions**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/preferred-actions-settings-sep-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/preferred-actions-settings-sep-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Suggested Actions section of Settings › Actions with its description: Tasks (Tasks you create in Kepler), Issues (Issues from your connected trackers), Pull requests I authored (Pull requests you opened) and Pull requests from others (Pull requests someone else opened, like ones you're asked to review), each with its Action picked, then the Suggest automatically switch and its help.">
  </a>
  <figcaption style="text-align:center; color:#888">The Suggested Actions settings.</figcaption>
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

Pull requests split by **who wrote them**, not by what you want to do with them. When you want the other Action, it is one click away in the chevron.

To show only the chevron on the button for a kind of item, set its slot to **None**.

**Suggest automatically**, below the pickers, is on by default. When you link an issue or pull request to a new task, the composer's button switches to that item's suggested Action, and anything you type is added to the Action's prompt. Turn it off to keep **Start**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/set-to-none-action-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/set-to-none-action-aug-2026.png" class="help-center-img img-bordered" alt="A suggested-Action slot set to None, showing only the chevron on that surface">
  </a>
  <figcaption style="text-align:center; color:#888">A slot set to None, leaving only the chevron.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/chevron-set-to-none-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/chevron-set-to-none-aug-2026.png" class="help-center-img img-bordered" alt="A row's Action button showing only the chevron, with no suggested Action set">
  </a>
  <figcaption style="text-align:center; color:#888">The chevron-only button on a row with no suggested Action.</figcaption>
</figure>

***

## Edit an Action

To edit an Action, go to **Settings → Actions** and click the Action's row under **All Actions**. The editor opens as its own page.

<figure style="text-align:center">
  <a href="/wp-content/uploads/actions-settings-built-in-sep-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/actions-settings-built-in-sep-2026-v3@2x.png" class="help-center-img img-bordered" alt="The All Actions list in Settings › Actions with New Action and Restore all defaults, in Built in and Custom groups: Plan, Implement, the edited Review and Address Feedback, then the custom Write Tests, each row with what the Action does and where it is available, such as Available on tasks, issues and pull requests.">
  </a>
  <figcaption style="text-align:center; color:#888">The All Actions list. Click a row to edit that Action.</figcaption>
</figure>

Each row shows what the Action does and where it is available. Once you have a custom Action, the list splits into **Built in** and **Custom**.

The editor has these fields:

| Field | What it does |
|---|---|
| **Title** | Required. The name shown on the button and in the chevron list |
| **Prompt** | Required. Sent to the agent word for word, and can be or start with one of your skills: type **/** (or **$** for Codex) to pick one |
| **Available on** | Where the Action is offered: **Tasks**, **Issues**, **Pull requests**, or several. Pick at least one |
| **Agent** | Which agent runs it. See below |

### Create your own

To create an Action, click **New Action** in **Settings → Actions**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-custom-action-aug-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-custom-action-aug-2026-v3@2x.png" class="help-center-img img-bordered" alt="The New Action sub-page in Settings › Actions, under the breadcrumb Actions › New Action: an empty Title field, focused, an empty Prompt field, Available on with Tasks ticked and Issues and Pull requests not, the Agent field's Preset reading Use default agent (Uses your default agent configuration), and Cancel and Save.">
  </a>
  <figcaption style="text-align:center; color:#888">The New Action editor.</figcaption>
</figure>

Custom Actions work exactly like the built-in ones. Make one for any prompt you would otherwise retype, such as backporting a fix, writing a migration, or auditing a dependency bump.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-custom-action-config-aug-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-custom-action-config-aug-2026-v3@2x.png" class="help-center-img img-bordered" alt="A custom Action being created: Title Backport a fix, the prompt Run the skill /backport, Available on with Tasks and Pull requests ticked, and the Agent field's Preset reading Use default agent (Uses your default agent configuration).">
  </a>
  <figcaption style="text-align:center; color:#888">A custom Action's configuration.</figcaption>
</figure>

#### Example: Prepare for review

This Action asks the agent to gather the evidence a reviewer needs before you read the diff, so you start from what the agent did and what it did not check. To create it, click **New Action** in **Settings → Actions** and fill in the following fields:

| Field | Value |
|---|---|
| **Title** | Prepare for review |
| **Available on** | **Tasks** |
| **Agent** | **Use default agent**, or a preset for a different agent from the one that wrote the code |

Use the following text for **Prompt**:

```text
Before I review this work, write a review summary in this session. Include:
- What the change is supposed to do, in one or two sentences
- Each file you changed, and why
- The commands you ran to test the change, and their results
- What you didn't test, and anything you're unsure about
Don't change any files.
```

The summary is the agent's own account. Check it against the diff in [Review Changes](/kepler/review-changes) before you commit.

#### Example: Open a pull request

Kepler has no "create pull request" button, so the agent or you open one. This Action has the agent open it, with a note in the description that an agent helped write the change. Fire it after you've reviewed and committed the work. To create it, click **New Action** in **Settings → Actions** and fill in the following fields:

| Field | Value |
|---|---|
| **Title** | Open a pull request |
| **Available on** | **Tasks** |
| **Agent** | **Use default agent** |

Use the following text for **Prompt**:

```text
Push this worktree's branch and open a pull request against its base branch.
Write a title and a description that say what changed and why.
End the description with this line:
"An AI coding agent helped write this change, and a person reviewed it."
If the worktree has uncommitted changes, stop and tell me.
```

The agent opens the pull request with the tools it has, such as your Git host's command-line tool. When it publishes the pull request, Kepler attaches it to the task. See [Review Changes](/kepler/review-changes#opening-a-pull-request).

### Restore defaults

To undo your edits to one Action, click **Restore default** on its row. The row shows **Restore default** only after you edit the Action. To undo your edits to every Action at once, click **Restore all defaults** in the **All Actions** section header.

An Action you have never edited picks up new default wording when Kepler updates. **Restore default** discards your edit.

Deleting a custom Action that a suggested-Action slot points to sets that slot to **None**, so its rows show only the chevron. To pick a new suggested Action, go back to **Settings → Actions → Suggested Actions**.

You cannot delete an Action that an automation runs. Delete the automation first; see [Automations](/kepler/automations#manage-an-automation).

***

## Setting an Action's agent

By default an Action runs on your **default agent**, configured in **Settings → Tasks → New tasks → Default agent**. To change it, open the **Preset** list in the editor's **Agent** field and pick one of the following:

| Choice | What the Action runs on |
|---|---|
| **Use default agent** | Your default agent configuration |
| A preset, shown as **{preset} · {agent}** | That preset's agent, with its model, mode, and options. If that agent has more than 1 account, pick the account below the list |
| **Custom agent settings** | The agent, model, and mode you set for this Action alone |

<figure style="text-align:center">
  <a href="/wp-content/uploads/inherit-default-agent-setting-aug-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/inherit-default-agent-setting-aug-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Agent field in the Action editor with its Preset list open: Use default agent (selected), Quick fix · Claude Code, Careful review · Claude Code, Quick fix · Codex, Docs pass · OpenCode, and Custom agent settings.">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent field's Preset list: the default agent, your presets, or custom settings.</figcaption>
</figure>

You save agent presets in **Settings → Agents → Agent presets**; see [Settings](/kepler/settings-agents#agent-presets). For example, pick a cheap, fast preset for triage and review, and a heavier one for implementation. If an Action's preset no longer exists, the Action shows **Preset unavailable for this agent**.

An [automation](/kepler/automations) runs its Action unattended, on issue and pull request text that other people write. If an automation uses the Action, choose a mode that acts without asking only if you trust everyone who can open or comment on those items.

**Custom agent settings** is an **all-or-nothing override**: it pins the provider, account, model, mode, and options together, rather than changing one of them and inheriting the rest.

Three rules govern which agent actually runs:

- A model belongs to its provider, so a pinned model never runs on a different agent.
- If an Action names an agent you do not have installed, the override falls back **whole** to your default agent.
- **An agent you pick explicitly at the point of firing beats an Action's override.**

### Review with a different agent

You can have one agent write the code and a different agent review it. A reviewer that did not write the code is less likely to repeat the author's mistakes.

To give **Review** its own agent, take the following steps:

1. Go to **Settings → Actions**, and click **Review** under **All Actions**.
2. In the **Agent** field, pick a preset for a different agent from the one that writes your code, or choose **Custom agent settings** and pick that agent. **Implement** uses your default agent unless you've changed it.
3. Click **Save**.

**Review** now runs on that agent, whether you fire it at a task's uncommitted work or at an attached pull request, with the model and mode you chose for it.

To use a different reviewer just once, pick the agent when you fire **Review**. An agent you pick at that point beats the Action's override.

The review is a report, not an approval. You read it in the session and decide what to change before you commit.

---
