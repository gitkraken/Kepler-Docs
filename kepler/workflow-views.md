---
title: Workflow Views
description: Understand Kepler's three workflow views (List, Kanban, and Console) and when to use each one.
taxonomy:
    category: kepler
---

# Workflow Views

Kepler, GitKraken's **Agentic Development Environment** (**ADE**), has three views for managing **Tasks**, **worktrees**, and **agent sessions**. Switch between them using the top navigation bar.

## Choosing a View

Choose based on what you're doing.

| View | Best for |
|------|----------|
| **List** | Reviewing diffs, commits, and file history on one worktree |
| **Kanban** | Tracking work status across all Tasks |
| **Console** | Monitoring multiple agent sessions and sending instructions |

---

## List View

List view shows a single worktree's changes, agent session, and commit history.

### Layout

List view is divided into three panels:

- **Left sidebar** — Task and worktree navigation
- **Center panel** — Diff or agent session
- **Right panel** — Git history

### Left Sidebar

The sidebar lists all Tasks and their associated worktrees. The **Tasks N** header shows the total Task count.

Tasks appear at the top level. Each Task expands to show its worktrees, labeled with the branch name and repository. A dot indicator on a worktree means it **Needs Attention**.

Use the **Filter/search bar** to narrow the list by Task or worktree name.

Click a worktree to open its diff and commit history in the center and right panels. The breadcrumb at the top of the center panel shows **Task name → worktree name**.

### Center Panel — Diff View

The diff panel shows the file changes for the selected worktree.

Each file shows its path and `+/-` line stats. Use the **Stacked/Split** toggle to switch between unified and side-by-side diff layouts. Unmodified sections are collapsed by default; click to expand them. Added lines appear in green; removed lines appear in red.

To return to the agent session from the diff view, click **Back to session** (×).

### Right Panel — Git History

The right panel shows **Working changes** at the top, followed by a list of recent commits.

Click any commit to see its full detail: title, description, author, email, timestamp, hash, branch tags, and a file list with `+/-` stats and `M` / `A` / `D` change indicators.

### Push, Pull, and Fetch

**Push**, **Pull**, and **Fetch** buttons appear in the top-right corner of List view. Use them to sync the current worktree's branch with its remote.

### Create Command

The **Create command...** dropdown in the top navigation is for creating saved command templates.

<!-- TODO: confirm with engineering — exact behavior and availability of "Create command..." -->

---

## Kanban View

Kanban view shows every worktree as a card on a board, organized by development stage.

### Board Layout

Worktrees move across four columns as work progresses:

1. **Exploration**
2. **In Development**
3. **In Review**
4. **Done**

Each column header displays the number of worktrees currently in that stage.

### Card Anatomy

Each card represents one worktree and shows:

- Branch name
- External link (↗) to open the branch in your source host
- Task name
- Repository name
- Session status badge
- **Open chat** button
- Archive icon
- Agent indicator — agent initial, last context snippet, and time since last activity
- **+ New session** button

If no agent session has been started yet, the card shows a **No sessions yet** state. Use **+ New session** to start one.

### Search and Filters

Use the **Search** bar to find worktrees by branch name or Task name.

Use the **Filters** panel to narrow the board by:

- **Status** — Needs Attention, Active, Idle, Errored, Inactive. All statuses are enabled by default.
- **Repos** — limit to one or more specific repositories.
- **Tasks** — filter by Task name. Select **No task** to show worktrees that are not associated with any Task.
- **Agent** — filter by agent runtime (for example, Claude Code, Codex).

<figure>
  <img src="/_images/kanban-status.png" class="help-center-img img-bordered" alt="Kanban view with the Status filter dropdown open, showing checkboxes for Needs Attention, Active, Idle, Errored, and Inactive" />
  <figcaption style="text-align: center; color: #888">The Status filter in Kanban view</figcaption>
</figure>

<figure>
  <img src="/_images/task-filter.png" class="help-center-img img-bordered" alt="Kanban view with the Tasks filter dropdown open, listing task names as checkboxes with a No task option at the bottom" />
  <figcaption style="text-align: center; color: #888">The Tasks filter in Kanban view</figcaption>
</figure>

Use the **Sort** control to order cards (for example, **Newest first**).

---

## Console View

Console view shows all active agent sessions side by side.

### Session Column Layout

Each session appears as a column. The Task header shows the session name and a count of active sessions.

Each column header includes:

- Session name (truncated)
- Repository name
- Controls: external link (↗), expand, add (+), close (×)
- Status bar with keyboard shortcut indicator (⌨1, ⌨2, ⌨3)
- Status badge
- Repository name
- Task name
- Time since last activity

<!-- TODO: confirm with engineering — exact keyboard shortcut format for ⌨1/2/3 navigation -->

### CHANGES Section

Each session column contains a collapsible **CHANGES N** section, where N is the total number of changed files.

Expand it to see **STAGED** and **UNSTAGED** sub-sections. Each file is listed with its path and a change indicator (`M`, `A`, or `D`).

Use this section to check staged and unstaged changes without leaving Console view. For the full diff or staging controls, switch to List view.

### Conversation Format

Each session column displays the conversation between you and the agent:

- Your messages appear as chat bubbles.
- Agent responses appear as formatted markdown.
- Tool calls appear as collapsible rows with a **Completed** badge or an error state.

<figure>
  <img src="/_images/course-correct.png" class="help-center-img img-bordered" alt="Console view showing three agent sessions side by side. The middle session displays tool calls with error states. The right session shows a formatted commit summary as an agent response." />
  <figcaption style="text-align: center; color: #888">Console view with multiple active sessions, showing tool call errors and an agent response with commit history</figcaption>
</figure>

### Input Bar

The input bar at the bottom of each session column includes:

- Microphone (🎤) for voice input
- Attachment button
- **Mode** selector
- **Model** selector (**Default** recommended)
- **Effort** selector
- A usage indicator
- **Send** button (↑)

You can change Mode, Model, and Effort on a per-message basis.

<!-- TODO: confirm with engineering — what the "20%" usage indicator represents -->

### Disconnected Sessions

If a session loses connection to its runtime, it appears as disconnected in the column.

<!-- TODO: confirm with engineering — cause of disconnected sessions and steps to reconnect -->

### Notifications

When a Task completes or needs attention, a toast notification appears with a **View** button. Click **View** to open the Task.

---
