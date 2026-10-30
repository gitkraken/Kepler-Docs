---
title: Quick Answers
description: Short answers to common Kepler questions, each linked to the full page. Run agents on Windows, in WSL, or on another machine, use several accounts of one agent, check on agents from your phone, set up every new worktree automatically, and have a second agent review the work.
product: Kepler
feature: Quick Answers
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode, grok, pi, antigravity]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [quick-answers, windows, wsl, ssh, accounts, remote-access, phone, worktrees, setup-commands, permissions, review, actions, pull-requests]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

**Quick Answers** collects the questions people ask most about Kepler, answers each in a sentence or two, and links to the section with the full detail. Start here when you know what you want to do but not which page covers it.

***

## Run agents where you work

Kepler runs agents on your computer, in WSL, or on another machine. Remote environments, which include WSL distros and SSH hosts, need a paid plan, and the number of accounts you can add for one agent depends on your GitKraken plan. The following table answers questions about where and how your agents run:

| What you want to do | Short answer | Full details |
|---|---|---|
| Run several agents at once without their changes colliding | Give each Task a **worktree**, a private Git working copy. Agents change files there, so several can run at once without touching each other's work or your own checkout. | [Tasks and Resources → Worktrees](/kepler/tasks-and-resources#worktrees-and-when-you-dont-need-one) |
| Run Kepler on Windows | Kepler installs natively on Windows 10 and later, on 64-bit and ARM64. It also runs on macOS 12 and later, and on Linux. | [Getting Started → Install Kepler](/kepler/kepler-getting-started#install-kepler) |
| Run agents in Windows Subsystem for Linux (WSL) | Kepler treats a WSL 2 distro as a remote environment. It finds your version 2 distros and lists them under **Found on this machine** in Settings. | [Remote Environments → WSL environments](/kepler/remote-environments#wsl-environments) |
| Run agents on another machine | Add the machine as an SSH host. Kepler installs itself on the host over SSH, so you don't need to install anything there first. | [Remote Environments → Add an SSH host](/kepler/remote-environments#add-an-ssh-host) |
| Use several accounts of the same agent | Claude Code, Codex, GitHub Copilot, Auggie, and Grok Build can each hold more than one signed-in account. To add one, open **Settings → Agents**, expand the agent, and click **Add account**. | [Agent Sessions → Several accounts for one agent](/kepler/agent-sessions#several-accounts-for-one-agent) |

***

## Start work

You can start a Task from an issue in your tracker or from nothing at all. The following table covers starting work, giving agents your rules, and getting each new worktree ready:

| What you want to do | Short answer | Full details |
|---|---|---|
| Start an agent from a Jira, Linear, or GitHub issue | Connect your tracker, then fire an Action from the issue's row. The issue becomes a Task, and Kepler attaches what it read, so the agent starts with that context. | [Issue Tracker Integrations](/kepler/issue-tracker-integrations), [Actions](/kepler/actions) |
| Start without an issue | Click **New task** or press **Cmd/Ctrl+N**, then write a prompt. You can attach nothing at all and turn the Task into real work later. | [Getting Started → Start something that is not tracked yet](/kepler/kepler-getting-started#start-something-that-is-not-tracked-yet) |
| Give every agent on a Task your team's rules | Attach a **Note** to the Task with the rule, constraint, or decision. Every session on the Task gets it, including sessions you start later. | [Tasks and Resources → Notes](/kepler/tasks-and-resources#notes-are-how-you-give-standing-instructions) |
| Install dependencies or copy `.env` files into every new worktree | Add a per-repository command and turn on **Run on worktree creation**. For example, `pnpm install` installs dependencies, and `cp "<SOURCE_PATH>/.env" .env` copies your `.env` file from the main repository. | [Settings → Per-repository commands](/kepler/settings#per-repository-commands) |
| Keep agents in different worktrees from colliding on ports or databases | A worktree separates files, not ports, databases, or caches. Use a command that runs on worktree creation to give each worktree its own settings, such as its own port or database name. | [Tasks and Resources → What a worktree doesn't separate](/kepler/tasks-and-resources#what-a-worktree-doesnt-separate) |

***

## Keep track of your agents

Kepler shows you what your agents are doing and when they need you, on your computer or your phone. Remote Access, which opens Kepler on a phone, needs a paid plan. The following table covers watching and answering your agents:

| What you want to do | Short answer | Full details |
|---|---|---|
| See what every agent is doing | The **Agent Graph** draws every Task, session, turn, tool call, subagent, and file the agents touch. It updates live as they work. | [The Agent Graph](/kepler/agent-graph) |
| Find out what needs you | Open **Ask Kepler** and ask. Its chat can see what's on your screen and check on your Tasks and sessions. | [Ask Kepler](/kepler/ask-kepler) |
| Answer an agent's permission request | The request pins to the top of the session. Choose **Allow**, **Allow for this session**, **Allow always**, **Reject**, or **Reject always**. | [Agent Sessions → Permission requests](/kepler/agent-sessions#permission-requests) |
| Check on your agents from your phone | Turn on **Remote Access** and scan its QR code with your phone's camera. Kepler opens in your phone's browser, and your work keeps running on your computer. | [Remote Environments → Using Kepler on a phone](/kepler/remote-environments#using-kepler-on-a-phone) |

***

## Review and ship

An agent finishing isn't the same as work that's ready to ship. The following table covers reviewing an agent's work and getting it merged:

| What you want to do | Short answer | Full details |
|---|---|---|
| Have the agent prepare its work for review | Create an Action that asks the agent to summarize what it changed, what it tested, and what it didn't test. The example **Prepare for review** Action shows the prompt. | [Actions → Example: Prepare for review](/kepler/actions#example-prepare-for-review) |
| Read what an agent changed | Open the Task's worktree and read the diff in the **Changes** overlay. From there you can comment, stage, and commit. | [Review Changes](/kepler/review-changes) |
| Undo an agent's change to a file | Use **Discard changes**, which asks first. Your current version goes to the Trash (the Recycle Bin on Windows), so you can get it back. | [Review Changes → Staging and committing](/kepler/review-changes#staging-and-committing) |
| Have a different agent review the work | Set the **Review** Action to a different agent from the one that wrote the code. | [Actions → Review with a different agent](/kepler/actions#review-with-a-different-agent) |
| Apply the review comments on a pull request | Fire **Address Feedback** on the pull request. It triages the comments, applies what's worth applying, and pushes back on the rest. | [Actions → The four built-in Actions](/kepler/actions#the-four-built-in-actions) |
| Open a pull request | Kepler has no "create pull request" button, so the agent or you open it, and Kepler attaches it to the Task once it exists. The example **Open a pull request** Action has the agent open it, with a note that an agent helped write the change. | [Review Changes → Opening a pull request](/kepler/review-changes#opening-a-pull-request), [Actions → Example: Open a pull request](/kepler/actions#example-open-a-pull-request) |

---
