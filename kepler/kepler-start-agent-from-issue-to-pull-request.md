---
title: Start a Coding Agent from a Jira or GitHub Issue and Take It to a Pull Request in Kepler
description: In Kepler, start a coding agent from a Jira, GitHub, or Linear issue with the ticket attached, then take the work to a pull request without copying the ticket.
product: Kepler
feature: Tasks
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, azure-devops]
integrations: [jira, linear, trello, asana, github, github-enterprise, gitlab, gitlab-self-managed, azure-devops, claude-code, codex-cli]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [issues, jira, github-issues, linear, issue-to-pull-request, start-agent-from-issue, tasks, actions, pull-requests, agents, claude-code, codex]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "kepler-agent-workflows"
    nav_label: "From Issue to Pull Request"
    nav_order: 70
    nav_parent: "kepler-agent-workflows"
    page_type: "content"
    card_icon: "git-pull-request-draft"
    card_color: "red"
    card_description: "Start an agent from a Jira, GitHub or Linear issue and take the work to a pull request"
---
<kbd>Last updated: November 2026</kbd>

Kepler by GitKraken starts a coding agent from a GitHub or GitLab issue in 1 click, or from a Jira issue once you add its repository, with the ticket already attached, and takes the work to a pull request. You connect your tracker once, then click the **Action** button on the issue's row in **Todo**. Kepler creates a task, sets up a worktree by default, and starts Claude Code, Codex, or your default agent with the issue's details in place, so you never paste the ticket into a chat.

## Requirements and limits

- Scope: Going from an issue in a connected tracker to an agent's pull request, inside 1 Kepler task
- Prerequisite: A GitKraken account signed in to Kepler, and a connected issue tracker. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations).
- Supported trackers: Jira, Jira Server / Data Center, Linear, Trello, Asana, GitHub, GitHub Enterprise, GitLab, GitLab Self-Hosted, Azure DevOps, and Azure DevOps Server.
- Limits: Kepler has no button that creates a pull request. The agent opens it, or you open it yourself. Kepler then attaches it to the task.

***

## Quick Start

1. Go to **Settings → Integrations**, find your tracker, such as **Jira** or **GitHub**, under **Issues and pull requests**, and click **Connect**.
2. Open **Todo** and find the issue.
3. Click the issue's **Action** button. The default for an issue is **Plan**. To start coding straight away, pick **Implement** from the chevron.
4. For a GitHub or GitLab issue, Kepler creates the task, attaches the repository and the issue, sets up a worktree by default, and starts the agent. For a Jira, Trello, Asana, or Azure DevOps issue, the issue's panel opens: add the repository, then send.
5. Review the agent's changes and commit them.
6. Have the agent open the pull request with an Action you create from the **Open a pull request** example, or open it yourself. Kepler attaches the pull request to the task.

***

## How to connect your issue tracker

You connect a tracker once, and its issues appear in **Todo** from then on.

1. Open **Settings → Integrations**.
2. Under **Issues and pull requests**, find the provider and click **Connect**.
3. Authorize Kepler on GitKraken's website, which opens in your browser.
4. Return to Kepler, where the provider shows a **Connected** badge.

<figure style="text-align:center">
  <a href="/wp-content/uploads/provider-integrations-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/provider-integrations-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Issues and pull requests section of Settings › Integrations, with GitHub and Azure DevOps Connected and Jira, Jira Server / Data Center, Linear and Trello offering Connect.">
  </a>
  <figcaption style="text-align:center; color:#888">Issues and pull requests, in Settings → Integrations.</figcaption>
</figure>

For a self-hosted tracker, such as Jira Server / Data Center or GitHub Enterprise, you connect with its address and a personal access token. See [Connect a self-hosted tracker](/kepler/issue-tracker-integrations#connect-a-self-hosted-tracker).

***

## How to start the agent from the issue

1. Open **Todo**. It lists your issues from every connected tracker.
2. Find the issue's row, and click its **Action** button.

<figure style="text-align:center">
  <a href="/wp-content/uploads/action-button-todo-row-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/action-button-todo-row-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="The right end of a Todo issue row: acme-web, Open, the age 3d, and the Plan Action button with its chevron.">
  </a>
  <figcaption style="text-align:center; color:#888">The Action button on an issue's row in Todo.</figcaption>
</figure>

The left half of the button runs the issue's suggested Action. For an issue, that is **Plan**, which has the agent research the code and propose an approach, then wait for your confirmation before it changes anything. The chevron lists the Actions available on issues, such as **Plan** and **Implement**, which has the agent make the changes directly.

For a GitHub or GitLab issue, Kepler uses your local copy of the repository, or clones it, and then does the following:

1. Creates the task.
2. Attaches the repository and the issue.
3. Sets up a worktree by default, so the agent works on its own branch.
4. Starts an agent with the issue's description attached as context.

A Jira issue names no repository, so Kepler cannot pick the code to work on. The same applies to Trello, Asana, and Azure DevOps issues. When you click **Action**, the issue's panel opens, ready to start a new task, and Kepler shows **Add a repository to start**. Add the repository in the panel, then send. If you started work from the same tracker project before, the panel can fill in that repository for you. A Linear issue gets its repository from the GitHub issue it is synced with.

Kepler also saves the issue's description as a note on the task, titled with the issue's key and title. Long descriptions are shortened, with a link to the issue.

From the issue's row, the agent is your default agent, or the agent the Action names. To use another agent, choose the Action in the **New task** window and change the agent before you send. See [Setting an Action's agent](/kepler/actions#setting-an-actions-agent).

***

## How to take the work to a pull request

When the agent finishes, you review and commit its work, open the pull request, and Kepler attaches the pull request to the task.

### Review and commit

When the agent finishes, open the task's worktree and read its changes in the **Changes** overlay. Send fixes back as review comments, then click **Commit…** to stage and commit. See [Review an AI-Written Pull Request Before Your Teammates Do](/kepler/kepler-review-ai-pull-request-before-sharing) and [Review What a Coding Agent Changed](/kepler/review-changes).

### Open the pull request

Kepler does not ship a "create pull request" Action. To have the agent open the pull request, create an Action once from the example on the Actions page:

1. Go to **Settings → Actions** and click **New Action**.
2. For **Title**, type `Open a pull request`.
3. For **Prompt**, paste the prompt from [Example: Open a pull request](/kepler/actions#example-open-a-pull-request). It tells the agent to push the branch, open a pull request against its base branch, write the title and description, and stop if the worktree has uncommitted changes.
4. Under **Available on**, tick **Tasks**.
5. Click **Save**.

Then open the task and pick **Open a pull request** from the chevron on the composer's send button. The agent opens the pull request with the tools it has, such as your Git host's command-line tool.

You can also push the branch and open the pull request yourself, on your Git host's website or from the worktree's terminal.

### Kepler attaches the pull request

When the agent publishes the pull request on one of the worktree's remotes, Kepler attaches it to the task. The task then holds the issue and its pull request together. A pull request you opened yourself can be attached from **Manage resources** at the bottom of the task's context panel. See [Opening a pull request](/kepler/review-changes#opening-a-pull-request).

With the pull request attached, the **Address Feedback** Action is available on the task. When your teammates leave review comments, run it to have the agent work through each one.

***

## How to start agents on new issues automatically

To have Kepler start the agent for you, set up an [automation](/kepler/kepler-automations). An automation runs an Action on a schedule, or when new GitHub or Jira activity matches its query.

***

## Common questions

Short answers about starting a coding agent from an issue in Kepler.

### Can I start a coding agent straight from a Jira issue?

Yes. Connect Jira in **Settings → Integrations**, then click **Action** on the issue's row in **Todo**, add the repository in the issue's panel, then send. Kepler starts the agent with the issue's description attached as context.

### Which issue trackers does Kepler support?

Jira, Jira Server / Data Center, Linear, Trello, Asana, GitHub, GitHub Enterprise, GitLab, GitLab Self-Hosted, Azure DevOps, and Azure DevOps Server. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

### Do I have to copy the ticket into the chat?

No. Starting from the issue's row in **Todo** attaches the issue's description as context, and Kepler saves it as a note on the task.

### Can the agent open the pull request by itself?

Yes. Create an Action from the **Open a pull request** example on the [Actions](/kepler/actions#example-open-a-pull-request) page and run it on the task. Kepler attaches the pull request when the agent publishes it.

### Which agent does the work?

Your default agent, such as Claude Code or Codex, unless the Action names another agent. To use another agent, choose the Action in the **New task** window and change the agent before you send.

***

## Related pages

- [Create a task](/kepler/create-task)
- [Issue Tracker Integrations](/kepler/issue-tracker-integrations)
- [Actions](/kepler/actions)
- [Review What a Coding Agent Changed](/kepler/review-changes)
- [Pull Request Integrations](/kepler/pull-request-integrations)
- [Automations](/kepler/kepler-automations)
- [Kepler Quick Answers: Running Coding Agents](/kepler/quick-answers)
