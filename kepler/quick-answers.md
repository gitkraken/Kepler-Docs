---
title: "Kepler Quick Answers: Running Coding Agents"
description: In Kepler, run coding agents on Windows, in WSL or over SSH, use several accounts, answer agents from your phone, prepare each worktree and review the work.
product: Kepler
feature: Quick Answers
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
tags: [quick-answers, windows, wsl, ssh, accounts, remote-access, phone, worktrees, setup-commands, automations, permissions, review, actions, pull-requests]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

In Kepler, find a short answer to a common question about running coding agents such as Claude Code and Codex, then follow its link for the full details. Start here when you know what you want to do but not where to find it.

***

## Run agents where you work

Kepler runs agents on your computer, in WSL, or on another machine.

Common questions about where and how your agents run:

| What you want to do | Short answer | Full details |
|---|---|---|
| Run several agents at once without their changes colliding | In Kepler, each task gets a **worktree**, a private Git working copy. Agents change files there, so several can run at once without touching each other's work or your own checkout. | [Tasks and Resources → Worktrees](/kepler/tasks-and-resources#worktrees-and-working-in-place) |
| Run Kepler on Windows | Kepler installs natively on Windows 10 and later, on 64-bit and ARM64. It also runs on macOS 12 and later, and on Linux. | [Getting Started → Install Kepler](/kepler/kepler-getting-started#install-kepler), [Run Coding Agents in Parallel on Windows](/kepler/kepler-run-coding-agents-in-parallel-on-windows) |
| Run agents in Windows Subsystem for Linux (WSL) | In Kepler, a WSL 2 distro is a remote environment. Kepler finds your version 2 distros and lists them under **Found on this machine** in Settings. | [Remote Environments → WSL environments](/kepler/remote-environments#wsl-environments), [Manage Sessions Across Accounts and SSH Hosts](/kepler/kepler-manage-agents-across-accounts-and-ssh-hosts) |
| Run agents on another machine | In Kepler, add the machine as an SSH host. Kepler installs itself on the host over SSH, so you do not need to install anything there first. | [Remote Environments → Add an SSH host](/kepler/remote-environments#add-an-ssh-host), [Manage Sessions Across Accounts and SSH Hosts](/kepler/kepler-manage-agents-across-accounts-and-ssh-hosts) |
| Use several accounts of the same agent | In Kepler, Claude Code, Codex, GitHub Copilot, Auggie, and Grok Build can each hold more than one signed-in account. To add one, open **Settings → Agents**, expand the agent, and click **Add account**. | [Agent Sessions → Several accounts for one agent](/kepler/agent-sessions#several-accounts-for-one-agent), [Manage Sessions Across Accounts and SSH Hosts](/kepler/kepler-manage-agents-across-accounts-and-ssh-hosts) |

***

## Start work

You can start a task from an issue in your tracker or from nothing at all.

Common questions about starting work, giving agents your rules, preparing each new worktree, and running agents on their own:

| What you want to do | Short answer | Full details |
|---|---|---|
| Start an agent from a Jira, Linear, or GitHub issue | In Kepler, connect your tracker, then run an Action from the issue's row. The issue becomes a task, and Kepler attaches what it read, so the agent starts with that context. For a Jira issue, or a Linear issue not synced with GitHub, add a repository in its panel first. | [Issue Tracker Integrations](/kepler/issue-tracker-integrations), [Actions](/kepler/actions), [Start an Agent from an Issue and Take It to a Pull Request](/kepler/kepler-start-agent-from-issue-to-pull-request) |
| Start without an issue | In Kepler, click **New task** or press **Cmd/Ctrl+N**, then write a prompt. You can attach nothing at all and turn the task into real work later. | [Getting Started → Start something that is not tracked yet](/kepler/kepler-getting-started#start-something-that-is-not-tracked-yet) |
| Move my work over from Conductor | In Kepler on macOS, click the import card on an empty **Tasks** list, or choose **File → Import from Another App…**. Each Conductor workspace becomes a task, and its chats continue in Kepler. | [Create a task → From another agent app](/kepler/create-task#from-another-agent-app), [Move from Conductor to Kepler](/kepler/kepler-move-from-conductor) |
| Give every agent on a task your team's rules | In Kepler, attach a **Note** to the task with the rule, constraint, or decision. Every session on the task gets it, including sessions you start later. | [Tasks and Resources → Notes](/kepler/tasks-and-resources#notes-are-how-you-give-standing-instructions) |
| Copy `.env` files into every new worktree | In Kepler, list them in a `.worktreeinclude` file at the repository's root, in `.gitignore` syntax. Kepler copies the matching Git-ignored files into each new worktree. | [Tasks and Resources → Make a new worktree ready to build](/kepler/tasks-and-resources#make-a-new-worktree-ready-to-build), [Set Up Every New Agent Worktree Automatically](/kepler/kepler-set-up-agent-worktrees-automatically) |
| Install dependencies in every new worktree | In Kepler, add a per-repository command, such as `pnpm install`, and turn on **Run on worktree creation**. | [Settings → Per-repository commands](/kepler/settings-repositories#per-repository-commands), [Set Up Every New Agent Worktree → Install dependencies](/kepler/kepler-set-up-agent-worktrees-automatically#how-to-install-dependencies-in-each-new-worktree) |
| Keep agents in different worktrees from colliding on ports or databases | In Kepler, a worktree separates files, not ports, databases, or caches. Use a command that runs on worktree creation to give each worktree its own settings, such as its own port or database name. | [Tasks and Resources → What a worktree does not separate](/kepler/tasks-and-resources#what-a-worktree-does-not-separate), [Set Up Every New Agent Worktree → Own port or database](/kepler/kepler-set-up-agent-worktrees-automatically#give-each-worktree-its-own-port-or-database) |
| Run an agent on a schedule, or when an issue or pull request changes | In Kepler, click **Automations** on the Dashboard and create an automation. It runs an Action or your own prompt on a schedule, or when new GitHub or Jira activity matches its query. | [Automations](/kepler/kepler-automations) |

***

## Keep track of your agents

Kepler shows you what your agents are doing and when they need you, on your computer or your phone.

Common questions about watching and answering your agents:

| What you want to do | Short answer | Full details |
|---|---|---|
| See what every agent is doing | In Kepler, the **Agent Graph** draws every task, session, turn, tool call, subagent, and file the agents touch. It updates live as they work. | [The Agent Graph](/kepler/agent-graph), [Keep Track of Several Agent Sessions](/kepler/kepler-track-multiple-agent-sessions) |
| Find out what needs you | In Kepler, open **Ask Kepler** and ask. Its chat can see what is on your screen and check on your tasks and sessions. | [Ask Kepler](/kepler/ask-kepler), [Keep Track of Several Agent Sessions → See which session needs you](/kepler/kepler-track-multiple-agent-sessions#how-to-see-which-session-needs-you) |
| Answer an agent's permission request | In Kepler, the request pins to the top of the session. Choose **Allow**, **Allow for this session**, **Allow always**, **Reject**, or **Reject always**. | [Agent Sessions → Permission requests](/kepler/agent-sessions#permission-requests), [Approve Agent Requests from Your Phone → Answer a permission request](/kepler/kepler-approve-agent-requests-from-your-phone#how-to-answer-a-permission-request) |
| Check on your agents from your phone | In Kepler, turn on **Remote Access** and scan its QR code with your phone's camera. Kepler opens in your phone's browser, and your work keeps running on your computer. | [Remote Environments → Using Kepler on a phone](/kepler/remote-environments#using-kepler-on-a-phone), [Approve Agent Requests from Your Phone](/kepler/kepler-approve-agent-requests-from-your-phone) |

***

## Review and ship

When an agent finishes, its work is not necessarily ready to ship.

Common questions about reviewing an agent's work and getting it merged:

| What you want to do | Short answer | Full details |
|---|---|---|
| Have the agent prepare its work for review | In Kepler, create an Action that asks the agent to summarize what it changed, what it tested, and what it did not test. The example **Prepare for review** Action shows the prompt. | [Actions → Example: Prepare for review](/kepler/actions#example-prepare-for-review), [Review an AI-Written Pull Request Before Sharing It](/kepler/kepler-review-ai-pull-request-before-sharing) |
| Read what an agent changed | In Kepler, open the task's worktree and read the diff in the **Changes** overlay. From there you can comment, stage, and commit. | [Review Changes](/kepler/review-changes) |
| Undo an agent's change to a file | In Kepler, use **Discard changes**, which asks first. Your current version goes to the Trash (the Recycle Bin on Windows), so you can get it back. | [Review Changes → Staging and committing](/kepler/review-changes#staging-and-committing) |
| Have a different agent review the work | In Kepler, set the **Review** Action to a different agent from the one that wrote the code. | [Actions → Review with a different agent](/kepler/actions#review-with-a-different-agent), [Review an AI-Written Pull Request Before Sharing It](/kepler/kepler-review-ai-pull-request-before-sharing) |
| Apply the review comments on a pull request | In Kepler, run **Address Feedback** on the pull request. The agent works through each comment, applies the changes it agrees with, pushes back on the rest, and replies to each comment. | [Actions → The four built-in Actions](/kepler/actions#the-four-built-in-actions) |
| Open a pull request | In Kepler, you or the agent opens the pull request, and Kepler attaches it to the task once it exists. The example **Open a pull request** Action has the agent open it for you. | [Review Changes → Opening a pull request](/kepler/review-changes#opening-a-pull-request), [Actions → Example: Open a pull request](/kepler/actions#example-open-a-pull-request), [Start an Agent from an Issue and Take It to a Pull Request](/kepler/kepler-start-agent-from-issue-to-pull-request) |

---
