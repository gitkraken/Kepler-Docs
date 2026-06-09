---

title: Agent Sessions
description: Learn how to configure, direct, and review agent sessions in Kepler, including how to read diffs, stage changes, and commit agent output.
taxonomy:
    category: kepler

---

# Agent Sessions

An **agent session** is a running coding agent within a Task in Kepler, GitKraken's Agentic Development Environment (ADE). This page covers how to configure a session before it starts, how to direct the agent from the console, and how to review, stage, and commit the changes it produces.

---

## Configuring an agent session

Four settings are available when you start a session. Three of them can be overridden per message; one is fixed for the life of the session.

| Setting | What it controls | Default | Options |
|---|---|---|---|
| **Agent** | Which agent runtime executes the session | — | Claude Code, Codex CLI, Copilot CLI, Cursor, OpenCode |
| **Mode** | How the agent handles decisions | — | See [Modes](#modes) below |
| **Model** | The model powering the agent | Default (recommended) | Varies by agent |
| **Effort Level** | How thoroughly the agent reasons | — | See [Effort levels](#effort-levels) below |

**Agent** is set at session start and cannot be changed mid-session. For details on each supported agent runtime, see [Agent Integrations](agent-integrations.md).

**Mode**, **Model**, and **Effort Level** can all be changed on any individual message from the console input bar without restarting the session.

### Modes

**Mode** controls how the agent handles decisions during a session, from pausing at every decision point to running without interruption.

<!-- TODO: confirm with engineering — document the exact available modes and their names -->

### Effort levels

**Effort Level** controls how thoroughly the agent reasons before acting. Higher effort produces more thorough results but takes longer.

<!-- TODO: confirm with engineering — document the exact available effort levels and their names -->

---

## Using the console to direct agents

The console is where you send instructions and read agent output. Each session opens in its own tab.

### Session tabs

Each session has a tab at the top of the console showing its name (truncated if long). Click **×** to close a tab. Click **+** to open a new session tab. Multiple sessions per worktree can be open simultaneously.

### Reading agent output

- **User messages** appear as chat bubbles.
- **Agent responses** render as formatted markdown: bold text, inline code, lists, and tables.
- **Tool calls** (file reads, searches, shell commands) appear as collapsible rows, for example `find /path...`, with a **Completed** badge or an error state. Click **▶** to expand the full tool output.

### Input bar controls

The input bar at the bottom of the console has these controls:

| Control | What it does |
|---|---|
| 🎤 **Mic** | Voice input |
| 📎 **Attachment** | Attach a file for the agent to reference |
| **Mode** dropdown | Override the mode for this message only |
| **Model** dropdown | Override the model for this message only |
| **Effort** dropdown | Override the effort level for this message only |
| **↑ Send** | Submit the instruction |

<!-- TODO: confirm with engineering — document the "20%" indicator (likely token budget remaining or cost usage) -->

### How to course-correct

Send a follow-up instruction when you see unexpected output, a tool call error, or a **Needs Attention** or **Disconnected** status. You do not need to restart the session.

---

## Reviewing changes: diffs, staging, and commits

After the agent runs, open the diff view to inspect what changed, stage files, and commit.

### Opening the diff

Click a worktree in the **List view** sidebar. The diff opens in the center panel.

### Reading the diff

- **File path and +/- line stats** appear at the top of each file's diff.
- **Stacked vs. Split toggle**: Stacked shows changes top-to-bottom; Split shows them side-by-side.
- Unmodified sections are collapsed with a line count. Click to expand them.
- **Red** lines were removed; **green** lines were added.

<figure>
  <img src="" class="help-center-img img-bordered" alt="Diff view showing red removed lines and green added lines with stacked/split toggle" />
  <figcaption style="text-align: center; color: #888">The diff view with Stacked mode active. Click the toggle to switch to Split view.</figcaption>
</figure>

### Working changes panel

The **Working Changes** panel on the right shows uncommitted changes alongside the worktree's recent commit history.

Click any commit in the history to see:
- Full title and description
- Author name, email, and timestamp
- Full commit hash and branch tags
- Per-file +/- stats with change type (M / A / D)

### Staged files panel

The **STAGED (N)** panel lists files queued for the next commit, where N is the file count. Each entry shows the file path and a change type badge (**M**, **A**, or **D**).

- **Discard All**: discards all changes. <!-- TODO: confirm with engineering — document the confirmation prompt behavior -->
- **Unstage All**: moves all staged files back to unstaged.
- Click an individual file to view its diff. Per-file controls let you unstage or discard that file individually. <!-- TODO: confirm with engineering — confirm exact per-file interaction -->

### Committing

The commit message field is pre-populated by Kepler. Edit it if needed, then click **Commit** to commit the staged files.

**Push**, **Pull**, and **Fetch** are available from the diff view toolbar (top right) without leaving Kepler.

Click **Back to session** to close the diff and return to the agent session console.

---

## Optional agent features: AI Sync

**AI Sync** is an experimental feature (disabled by default) that gives agents tools to rebase or merge with automatic conflict resolution. Each operation can be rolled back.

To enable AI Sync, go to **Settings → Features** and toggle **AI Sync** on.

Once enabled, the agent can invoke rebase and merge operations with automatic conflict resolution.

For more on experimental features, see [Settings](settings.md#features).

---
