---
title: Move from Conductor to Kepler
description: In Kepler, import your Conductor workspaces on macOS as tasks, in the same folders and branches, with their Claude Code and Codex chats ready to continue.
product: Kepler
feature: Tasks
content_type: how-to
audience: developer
plan_required: all
os_support: [macOS]
git_hosts: [generic]
integrations: [claude-code, codex-cli]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [conductor, import, migrate, switch, parallel-agents, workspaces, tasks, worktrees, claude-code, codex, orca, herdr, vibe-kanban]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Kepler by GitKraken imports your Conductor workspaces on a Mac as tasks, in the same folders and branches, with their Claude Code or Codex chats ready to continue. You pick the workspaces to bring over in **Import from another app**, and Kepler leaves your files and branches where they are.

## Requirements and limits

- Scope: Bringing the workspaces the Conductor app keeps on your Mac into Kepler as tasks
- Prerequisite: Conductor's workspaces on the Mac that runs Kepler
- Limits: Importing from Conductor works on macOS only, because Conductor runs only on macOS.
- Limits: Conductor's cloud workspaces are not imported. They have no folder on your Mac.
- Limits: Archived workspaces, and workspaces whose folder no longer exists, are not imported.
- Limits: Continue each chat in 1 app only. Conductor and Kepler write to the same chat history.

***

## Quick Start

1. On an empty **Tasks** list, click the import card, such as **Import from Conductor**. You can also choose **File → Import from Another App…**.
2. If Kepler found more than 1 app, click **Conductor**.
3. Tick the workspaces you want, and click **Import *N* workspaces**. Workspaces active in the last 30 days arrive ticked.
4. The import runs in the background. When the title bar chip reads **Imported *N***, click it, then click **View tasks**.
5. Open a new task in **Tasks** to pick its chat up where it left off.

After you install Kepler, the guided start also offers to import Conductor's workspaces when it finds them. See [Getting Started](/kepler/kepler-getting-started).

***

## How to import your Conductor workspaces

1. On an empty **Tasks** list, click the import card. It names the apps Kepler found, such as **Import from Conductor, Orca and 2 more**. You can also choose **File → Import from Another App…** at any time.

<figure style="text-align:center">
  <a href="/wp-content/uploads/import-card-nov-2026@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/import-card-nov-2026@2x.png" class="help-center-img img-bordered" alt="Two cards below an or divider: Import from Conductor, Orca and 2 more, reading Bring in your workspaces as tasks, with their branches and chats, and Open an external session.">
  </a>
  <figcaption style="text-align:center; color:#888">The import card names the apps Kepler found.</figcaption>
</figure>

2. If Kepler found more than 1 app, click **Conductor** in **Import from another app**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/import-choose-app-nov-2026@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/import-choose-app-nov-2026@2x.png" class="help-center-img img-bordered" alt="The Import from another app dialog, Choose the app to bring workspaces in from, listing Conductor, Orca, herdr and Vibe Kanban.">
  </a>
  <figcaption style="text-align:center; color:#888">Picking Conductor as the app to import from.</figcaption>
</figure>

3. In **Import from Conductor**, tick the workspaces you want, and click **Import *N* workspaces**. The workspaces are grouped by repository, and each row shows its branch and how long ago it was active. Workspaces active in the last 30 days arrive ticked, and older ones are folded under **Older**. To tick a whole repository, use its tick box. The count at the top, such as **9 of 14 selected**, shows how many you picked. To narrow a long list, type in **Filter workspaces**. To clear every tick, click **Select none**. A workspace you already imported is marked **Already a task:** and the task's name.

<figure style="text-align:center">
  <a href="/wp-content/uploads/import-workspaces-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/import-workspaces-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Import from Conductor dialog with 9 of 14 selected, Select none, and a Filter workspaces box above ticked workspaces grouped by repository, each row showing its branch and how long ago it was active. The 5 older workspaces are folded under Older, and Import 9 workspaces sits at the bottom.">
  </a>
  <figcaption style="text-align:center; color:#888">Choosing the Conductor workspaces to import.</figcaption>
</figure>

4. The dialog closes and the import runs in the background. A chip in the title bar shows its progress, such as **Importing 2 of 4**. Hover over or click the chip for its card, where **Stop** ends the import and **Retry** tries a failed workspace again. When the chip reads **Imported *N***, click **View tasks** on its card, or **Dismiss** to clear the chip.

<figure style="text-align:center">
  <a href="/wp-content/uploads/import-run-chip-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/import-run-chip-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="The title bar after an import ran in the background: the Imported 3 chip, with a check, sits left of the inbox, Ask, feedback, Settings and account buttons, and hovering it opens its card, Import finished, 3 tasks created, with Dismiss and View tasks.">
  </a>
  <figcaption style="text-align:center; color:#888">The finished import in the title bar, with its card open.</figcaption>
</figure>

5. Find the new tasks in **Tasks**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/import-tasks-nov-2026@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/import-tasks-nov-2026@2x.png" class="help-center-img img-bordered" alt="The Tasks view listing the 4 imported tasks under Recent, each with its repository and In Development status.">
  </a>
  <figcaption style="text-align:center; color:#888">The imported workspaces, now tasks.</figcaption>
</figure>

If Conductor is not in the list, Kepler did not find Conductor's workspaces on this Mac.

***

## What carries over from Conductor

| From Conductor | In Kepler |
|---|---|
| A workspace | A task, named after the workspace |
| The workspace's folder | The task's worktree, or the repository folder for a workspace on the main checkout. Kepler uses the same folder and does not copy or move your files |
| The workspace's branch | The same branch, in that worktree |
| The workspace's chats | The task's sessions. Open one to continue the chat where it left off |
| The workspace's notes | A note on the task, titled **Notes from Conductor** |
| The workspace's target branch | The worktree's merge target |

A chat continues only if its agent's history is on your Mac and Kepler supports that agent. The workspace list marks a chat that Kepler cannot continue. If a workspace fails to import, the title bar chip counts it, and its card offers **Retry**.

After the import, continue each chat in Kepler or in Conductor, not both. Both apps write to the same chat history.

***

## What to do next in Kepler

- **Start new work from your issues.** Connect your tracker and start tasks from the **Todo** view, with the issue attached. See [Start a Coding Agent from a Jira or GitHub Issue](/kepler/kepler-start-agent-from-issue-to-pull-request).
- **Run Actions.** Run **Plan**, **Implement**, **Review**, or your own Actions on a task instead of retyping prompts. See [Actions](/kepler/actions).
- **Review each task's changes.** Read the diff in the **Changes** overlay, send comments back to the agent, and commit. See [Review Changes](/kepler/review-changes).
- **Set up new worktrees.** Run a setup command each time Kepler creates a worktree with **Run on worktree creation**, and copy git-ignored files such as `.env` with a `.worktreeinclude` file. See [Repository Settings](/kepler/settings-repositories) and [Tasks and Resources](/kepler/tasks-and-resources).

***

## Common questions

### Can I move my Conductor workspaces to Kepler?

On macOS, choose **File → Import from Another App…**, pick **Conductor**, tick the workspaces, and click **Import *N* workspaces**. Each workspace becomes a task in the same folder and on the same branch.

### Do my Conductor chats come with me?

A chat comes with you when its agent history is on your Mac and Kepler supports its agent, such as Claude Code and Codex. Each chat becomes a session on the task, and you continue it where it left off.

### Can I import from Conductor on Windows or Linux?

Kepler imports Conductor workspaces only on a Mac, because Conductor runs only on macOS.

### Does importing change anything in Conductor?

Kepler reads Conductor's workspaces and does not move your files. Both apps then point at the same folders, branches, and chat history, so continue each chat in 1 app only.

### Which other apps can Kepler import from?

Kepler can also import workspaces from Orca, herdr, and Vibe Kanban, in the same **Import from another app** dialog. See [From another agent app](/kepler/create-task#from-another-agent-app).

***

## Related pages

- [Create a task](/kepler/create-task#from-another-agent-app)
- [Tasks and Resources](/kepler/tasks-and-resources)
- [Agent Sessions](/kepler/agent-sessions)
- [Actions](/kepler/actions)
- [Review What a Coding Agent Changed in Kepler](/kepler/review-changes)
- [Getting Started with Kepler](/kepler/kepler-getting-started)
- [Kepler Quick Answers: Running Coding Agents](/kepler/quick-answers)
