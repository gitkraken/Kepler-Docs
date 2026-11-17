---
title: Review an AI-Written Pull Request Before Your Teammates Do, in Kepler
description: In Kepler, review an AI agent's work yourself before you open a pull request. Read every line, comment, get a second agent's review, then open it.
product: Kepler
feature: Review Changes
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, azure-devops]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode, grok, pi, antigravity]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [review, self-review, pull-requests, ai-pull-request, code-review, review-comments, second-opinion, actions, agents, claude-code, codex]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Kepler by GitKraken gives you a review step between an agent's work and your teammates. You read every changed line in the Changes overlay, send review comments back to the agent, have a second agent review the work, and only then open the pull request. The work stays in the task's worktree, so you can review what Claude Code, Codex, or any other agent wrote before you open the pull request.

**Requirements and limits**
- Scope: Reviewing an agent's uncommitted or committed work in a Kepler task before you open a pull request
- Prerequisite: A task whose agent has made changes in its worktree. See [Create a task](/kepler/create-task).
- Limits: Kepler has no button that creates a pull request. The agent opens it, or you open it yourself.
- Limits: Review comments you write in Kepler go to the agent. Kepler does not post them to your Git host.
- Limits: A second agent's review is a report, not an approval. You still decide what to change.

***

## Quick Start

| Self-review step | What you do in Kepler |
|---|---|
| 1. Restate the problem | Ask the agent for a summary of what it changed and what it did not test, with an Action you create from the **Prepare for review** example |
| 2. Read every changed line | Open the task's worktree and read the diff in the **Changes** overlay |
| 3. Send fixes back | Comment on the lines that need work, then click **Send comments (*n*)** |
| 4. Prove it works | Ask the agent to run the tests in the session, and read the commands and results it reports |
| 5. Get a second opinion | Run the built-in **Review** Action with a different agent, such as Codex for work Claude Code wrote |
| 6. Open the pull request | Commit, then open the pull request yourself or with an Action you create from the **Open a pull request** example |

***

## How to restate what the change does

Start from what the change is supposed to do, so you can judge the diff against it. Kepler does not ship an Action for this. The [Actions](/kepler/actions#example-prepare-for-review) page has an example, **Prepare for review**, that you create once and then run on any task.

To create it:

1. Go to **Settings → Actions** and click **New Action**.
2. For **Title**, type `Prepare for review`.
3. For **Prompt**, paste the example prompt from [Example: Prepare for review](/kepler/actions#example-prepare-for-review). It asks the agent what the change does, which files it changed and why, which tests it ran, and what it did not test, and tells it to change no files.
4. Under **Available on**, tick **Tasks**.
5. Click **Save**.

To run it, open the task and pick **Prepare for review** from the chevron on the composer's send button. The summary is the agent's own account. Check each point against the diff before you trust it.

***

## How to read every changed line

The agent makes its changes in the task's worktree. To read them:

1. Open the task, and open the worktree from the **Changes** group in the context panel.
2. Click a file, or choose **Open changes** from the worktree's menu, to open the **Changes** overlay.
3. Read each file's diff. The file tree beside it lists every file the agent touched.

<figure style="text-align:center">
  <a href="/wp-content/uploads/changes-overlay-maximize-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/changes-overlay-maximize-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Changes overlay for kepler/fix-cart-total open over the task page, listing the 2 changed files beside the diff of cart.js.">
  </a>
  <figcaption style="text-align:center; color:#888">The Changes overlay lists every changed file beside its diff.</figcaption>
</figure>

See [Review Changes](/kepler/review-changes#the-changes-overlay) for the overlay's views, layouts, and keyboard controls.

***

## How to send fixes back to the agent

When a line needs work, comment on it instead of fixing it yourself or retyping the location in the chat.

1. In the **Changes** overlay, hover a line and click the **+** beside its line number. To comment on a range, **Shift**-click the last line.
2. Type your note.
3. Click **Add comment** to queue it, or **Send now** to send it to the agent at once.
4. When you finish the file, click **Send comments (*n*)** in the overlay's header to send every queued comment.

<figure style="text-align:center">
  <a href="/wp-content/uploads/review-comment-draft-oct-2026-v6@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/review-comment-draft-oct-2026-v6@2x.png" class="help-center-img img-bordered" alt="A review comment draft under lines 3 and 4 of cart.js in the Changes overlay, with Cancel, Add comment and Send now.">
  </a>
  <figcaption style="text-align:center; color:#888">A review comment draft, under the lines it is about.</figcaption>
</figure>

Each comment reaches the agent with its file, lines, the code, and your note. The agent can reply to each comment, and you resolve the comment when it is handled. See [Review comments](/kepler/review-changes#review-comments).

***

## How to prove the change works

A diff that reads well can still fail. Ask the agent in the task's session to run the tests and tell you the commands and the results. If you created **Prepare for review**, its summary already lists the commands the agent ran and what it did not test. Ask for tests for anything on the "not tested" list before you move on.

***

## How to get a second agent's review

An agent that did not write the code is less likely to repeat the author's mistakes. Kepler ships a built-in **Review** Action. It reviews the uncommitted work in the worktree, or the attached pull request if there is one.

By default **Review** runs on your default agent. To have a different agent review, set its agent once:

1. Go to **Settings → Actions**, and click **Review** under **All Actions**.
2. In the **Agent** field, pick a preset for a different agent from the one that writes your code, or choose **Custom agent settings** and pick that agent.
3. Click **Save**.

Then open the task and pick **Review** from the chevron on the composer's send button. To use a different reviewer only once, pick the agent when you run **Review**. See [Review with a different agent](/kepler/actions#review-with-a-different-agent).

The review is a report. Read it in the session, and send the agent that wrote the code the changes you agree with.

***

## How to open the pull request

When you are satisfied, commit the work. In the **Changes** overlay, click **Commit…** to stage and commit it. See [Staging and committing](/kepler/review-changes#staging-and-committing).

Then open the pull request in one of these ways:

- **Write it yourself.** Push the branch and open the pull request on your Git host's website, or with a command in the worktree's terminal. Writing the description yourself is the last check that you understand the change.
- **Have the agent open it.** Kepler does not ship an Action for this. Create one from the [Open a pull request](/kepler/actions#example-open-a-pull-request) example in **Settings → Actions**, then run it on the task. The example tells the agent to stop if the worktree has uncommitted changes, and to end the description with a line that says an AI coding agent helped write the change and a person reviewed it.

When the agent publishes the pull request, Kepler attaches it to the task. A pull request you open yourself can be attached from **Manage resources**. See [Opening a pull request](/kepler/review-changes#opening-a-pull-request).

***

## Common questions

### How do I review an AI-written PR myself before I send it to a teammate?

In Kepler, read every changed line in the task's **Changes** overlay, send review comments back to the agent, ask it to run the tests, and run the built-in **Review** Action with a second agent. Open the pull request only after that.

### Can a different AI agent review the code that Claude Code wrote?

Yes. Set the **Agent** field of the built-in **Review** Action to Codex or another agent in **Settings → Actions**, or pick the agent when you run **Review**.

### Does Kepler post my review comments to GitHub?

No. Review comments in Kepler go to the agent in the task's session. Your teammates see only the pull request you open.

### Is there a "Prepare for review" or "Open a pull request" button in Kepler?

No. Both are examples on the [Actions](/kepler/actions) page. You create each one once as your own Action in **Settings → Actions**, and then it appears in the list of Actions on every task.

### Can I mark the pull request as AI-assisted?

Yes. Write it in the description yourself, or use an Action created from the **Open a pull request** example, which ends the description with a line that says an AI coding agent helped write the change and a person reviewed it.

***

## Related pages

- [Review What a Coding Agent Changed in Kepler](/kepler/review-changes)
- [Actions](/kepler/actions)
- [Create a task](/kepler/create-task)
- [Agent Sessions](/kepler/agent-sessions)
- [Pull Request Integrations](/kepler/pull-request-integrations)
- [The Task View](/kepler/task-view)
- [Kepler Quick Answers: Running Coding Agents](/kepler/quick-answers)
