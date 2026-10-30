---
title: The Agent Graph
description: Use the Agent Graph to see what your agents are doing as they work, with every task, session, turn, tool call, subagent and file in one live graph.
product: Kepler
feature: Agent Graph
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot, cursor, auggie, opencode, grok, pi, antigravity]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [agent-graph, dashboard, sessions, subagents, tool-calls, monitoring]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

When several agents run at once, use the **Agent Graph** to see what each one is doing. The graph shows every task, the sessions in each task, each turn, every tool call, every subagent, and the files the agents touch. It updates live, and new nodes appear as the agents work. The Agent Graph shows agent work the way the Commit Graph in GitKraken Desktop shows a repository's history.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-graph.gif" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-graph.gif" class="help-center-img img-bordered" alt="The Agent Graph animating as agents work, with turn, tool-call, and file nodes appearing, including one tool call in an error state">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent Graph, growing live as agents work.</figcaption>
</figure>

***

## Open the Agent Graph

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-graph-toggle-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-graph-toggle-sep-2026.png" class="help-center-img img-bordered" alt="The top-left control's three segments: Todo, Tasks in progress, and Agent Graph selected">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent Graph segment, beside Todo and Tasks in progress.</figcaption>
</figure>

You can open the Agent Graph for all your agents or for a single session. It has no page of its own:

| To see | Do this |
|---|---|
| **All your agents** | In the control at the top left, switch to the **Agent Graph** segment, beside **Todo** and **Tasks in progress**. Kepler remembers your choice across restarts |
| **One session** | On the task page, open the menu of the session's row in the context panel and choose **Show Agent Graph**. The session's graph opens beside its transcript, and **Hide Agent Graph** closes it |

The Agent Graph is a segment, not a layout of the list, because it replaces the list instead of arranging it. To learn about **Todo**, **Tasks in progress**, and their **List** and **Board** layouts, see [Arranging Your Work](/kepler/arranging-your-work).

When you open the graph from the main list, it shows exactly what the list would show, including your search and filters. When you open it on a session, the graph starts fully expanded, and grows downward (or to the right) as the conversation adds tool calls and subagents.

The graph is for viewing, not for working. To work in a session, open the session from its task. The node details in the graph link directly to it. To watch several agents at once and answer them, **Shift**-click sessions to open them side by side. See [the task page](/kepler/task-view).

***

## How to read the graph

<figure style="text-align:center">
  <a href="/wp-content/uploads/how-to-read-graph-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/how-to-read-graph-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Agent Graph for one task, read left to right: the task Fix the cart total and its session, both marked Needs you, then three turns. Turn 1 and Turn 2 are folded, each with a chevron and 3 hidden nodes (Turn 2 also shows one failed call); the latest turn is open on its tool calls, Read cart.test.js, Edit cart.js and Run npm test, with the files they touched, and a permission request marked Needs you.">
  </a>
  <figcaption style="text-align:center; color:#888">The graph's layers, from task to file, with past turns folded.</figcaption>
</figure>

The graph has layers. Each layer is one level further from the root:

| Layer | What it is |
|---|---|
| **Task** | The root, 1 for each task. See [Tasks and Resources](/kepler/tasks-and-resources) |
| **Session** | Each agent session in that task, with its agent and model |
| **Turn** | One exchange: **Turn 1**, **Turn 2**, and so on |
| **Tool call** | What the agent did in that turn |
| **Subagent** | A subagent the agent started, with its own tool calls beneath it |
| **File** | The files a call touched. This is the bottom layer, where you can see when 2 sessions work on the same file |

The graph shows only sessions that belong to a task. Kepler leaves out an external session that it can see but that no task owns, because the session has no task to attach to.

### Past turns start folded

On the main list's graph, each session shows its latest turn unfolded and folds every earlier turn, so a long session shows its current work first. A folded card has a chevron and the number of nodes beneath it, and its tooltip says how many nodes are folded. To unfold a folded turn, double-click it. To fold what is beneath any card with children, such as a session, a turn or a subagent, double-click the card. A session's own graph starts with every turn unfolded.

Look out for 2 kinds of node, because the agent cannot continue until you respond: **Permission needed** and **Question for you**.

### What a node's state means

| State | What is happening |
|---|---|
| **Running a tool** | Working now |
| **Waiting on the model** | Thinking |
| **Blocked** | Waiting on you |
| **Finished — unread** | Done, and you have not looked at it yet |
| **Done** | Finished, and you have looked at it |
| **Stopped** | You interrupted it |
| **Failed** | It ended with an error |
| **Idle** | Doing nothing |

For 3 states that need your attention, the card shows a word instead of a color: **New**, **Needs you**, and **Error**.

### Tool calls are colored by what they do

Each tool call has a color for its kind:

**Read · Edit · Delete · Move · Search · Execute · Think · Fetch · Switch mode · Other**

The colors are the quickest way to see what an agent is doing. A task with only **Read** calls is still exploring the code. Many **Edit** calls mean the agent has chosen an approach and is making changes.

Repeated calls of the same kind fold into one node marked **Group**. The node keeps the kind as its name and shows the number of calls and how many different files they touch. For example, a **Read** node that reads *9 calls · 4 files* did not read the same file 9 times. To unfold a group, double-click it. Double-click it again to fold it. A single click only selects a node, so selecting a group never rearranges the graph.

***

## Click any node for detail

<figure style="text-align:center">
  <a href="/wp-content/uploads/node-details-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/node-details-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Agent Graph with the Edit cart.js tool-call node of Fix the cart total selected and its chain highlighted (the task, its session, Turn 1, Edit cart.js and cart.js), and the node's details panel open beside the graph: Tool call, Done, Edit cart.js, the path Fix the cart total › its session › Turn 1, Last activity just now, Status Done and the file it touched, cart.js.">
  </a>
  <figcaption style="text-align:center; color:#888">A node's details, open beside the graph.</figcaption>
</figure>

When you select a node, its details open beside the graph. The details depend on the kind of node:

- **Session**: the agent, state, model, mode, context used, cost, where it is running, and its stop reason.
- **Tool call**: the tool, the exact input, the files and paths it touched, how long it took, and how many calls failed.
- **Subagent**: its type, its prompt, and its own calls.
- **Task**: its status (**Active**, **On hold**, or **Archived**), its sessions, and its resources.
- **File**: a preview of the file. For a large file, the preview reads only its beginning.

For a node with children, the details header also has a fold button, **Collapse what is under this node** or **Expand what is under this node**. It does the same as double-clicking the card. The stats column still counts the whole graph, including folded nodes.

<figure style="text-align:center">
  <a href="/wp-content/uploads/graph-collapse-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/graph-collapse-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Agent Graph with the folded Turn 2 node selected, showing the failed call mark and a chevron with 3 hidden nodes, while the rest of the graph dims. Its details panel shows Turn, Done, Turn 2, the path Fix the cart total › Discount codes break the cart…, 1 failed call, Tool calls 2 and the prompt Add a test for the discount, with the back, Expand what is under this node and close buttons in its header.">
  </a>
  <figcaption style="text-align:center; color:#888">A folded turn selected, with Expand what is under this node in its details header.</figcaption>
</figure>

**The graph shows a call's duration only when Kepler watched the call happen.** Replayed history does not record how long a call took, so the graph leaves the duration out instead of estimating it.

From the details, click **Open task** or **Open session** to go to the work, or **Copy** to copy any input or prompt.

***

## The stats column

The stats column, on the right side of the graph, shows numbers about all your agents' work. Read it from top to bottom.

<figure style="text-align:center">
  <a href="/wp-content/uploads/stat-rails-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/stat-rails-2026.png" class="help-center-img img-bordered" alt="The stats column down the right-hand side of the Agent Graph">
  </a>
  <figcaption style="text-align:center; color:#888">The stats column.</figcaption>
</figure>

The stats column uses the same data as the graph, so its numbers always match what the graph shows. On the dashboard, the stats column hides while a panel is open.

### The counters

The top of the stats column has 6 tiles, 2 across:

| Counter | What it counts |
|---|---|
| **Working** | Sessions in a turn, with a tool running |
| **Blocked** | Sessions that cannot continue without you |
| **Thinking** | Sessions in a turn with no tool running, waiting on the model |
| **Unread** | Sessions that finished a turn you have not looked at |
| **Subagents** | Subagents running now |
| **Failed calls** | Tool calls that ended with an error, across the graph shown |

**Working** and **Thinking** are separate counters because they describe different situations. Agents that are all waiting on the model need something different from agents that are all running commands, and a single "busy" number cannot tell you which you have. **Blocked** and **Unread** are the counters that tell you to act.

### Needs attention

The **Needs attention** list appears under the counters when something needs you. It lists everything that is waiting for you, most urgent first, tagged **Needs you**, **Error**, or **New**. Click a row to go to its node. In a graph with 300 nodes, this list is the reliable way to find the nodes that need you.

### Throughput

The **Throughput** section shows a trace of your agents' activity over time, with these readings under it:

| Reading | What it tells you |
|---|---|
| **Tasks** / **Sessions** | How many the graph shows |
| **Tools** | Tool calls running now |
| **Files touched** | How many different files the calls in the graph have touched |
| **Context** | How much context window your sessions have used, as a total and a percentage. Only sessions that report usage count, and the row does not appear when none do |
| **Cost** | What the work has cost so far, in the currency your sessions report. The row does not appear when sessions report no cost, or report it in several currencies |

### Tool spectrum

The **Tool spectrum** section shows the calls by kind, with a bar and a count for each kind. It shows whether your agents are mostly reading, editing or running commands. Kinds with no calls do not appear, and until there are calls, the section reads **No tool activity yet**.

### Usage windows

The **Usage windows** section shows your agent subscription windows, with 1 bar for each window of each agent, and the share of the window you have used. The section appears when it has something to show:

- With **Check plan usage with each agent's provider** on (the default, in **Settings → Agents → Usage limits**), Kepler asks each agent's provider for your usage.
- With it off, the section shows only readings that your agents report themselves, dimmed when they are out of date. The section stays hidden until an agent reports a reading.

See [Settings](/kepler/settings-agents#usage-limits).

These bars show only how much of each window you have used. To see whether you are on pace for a window, and when it runs out at your current rate, check a session's usage meter. See [Usage indicators](/kepler/agent-sessions#usage-indicators).

### What was folded away

At the bottom of the stats column, a note counts what Kepler left out of the graph to keep it readable:

- Tool calls grouped.
- Sessions filtered out.
- Sessions Kepler can see but not trace.
- Tasks with no session.

Kepler shows this note so that you know the graph is not showing everything.

***

## Finding things in a busy graph

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-graph-header-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-graph-header-sep-2026.png" class="help-center-img img-bordered" alt="The Agent Graph's header, with the search box, and the Options menu open showing Layout, Zoom to selection, Compact stats, and Group repeated tool calls">
  </a>
  <figcaption style="text-align:center; color:#888">The graph's header controls, with the Options menu open.</figcaption>
</figure>

The graph's header has a search box, an **Options** menu, and the depth slider. The zoom controls are on the graph itself, and the timeline is under it (see [Pause and replay the graph](#pause-and-replay-the-graph)):

| Control | Where | What it does |
|---|---|---|
| *Filter tasks, sessions, agents…* | Header | Narrows the graph by task, session or agent name |
| **Layout** | Options | Draws the tree **Left to right** or **Top to bottom** |
| **Zoom to selection** | Options | Zooms to a selected node with its tree, ancestors and siblings, and does not move when the node is already in view. 2 nested settings set when the view can move again: **Follow the tree as it grows** zooms out as far as needed instead of stopping when cards get too small to read, and **Re-frame when the space changes** zooms again when a panel opens beside the graph or the window changes size |
| **Compact stats** | Options | Shows the same numbers in half the space, with circular meters and smaller tiles, for a smaller window |
| **Group repeated tool calls** | Options | On by default. When off, every call is its own node |
| **Only active sessions** | Options | Hides sessions that have ended, but keeps idle ones. On by default on the main list, where the **Options** badge counts it when you turn it off, and off by default in a session's own graph |
| **Agent** / **Repo** | Options | Narrows the graph to 1 agent or repository. Not offered on the main list, because the list's own filters do this |
| **Detail depth** | Header | How many layers deep the graph goes: up to 5, and 4 by default |
| **Zoom in** / **Zoom out** / **Fit to view** | Graph | Moves the view. You can also drag to pan, and press **Escape** to clear a selection |

Kepler remembers the depth and layout separately for the main list and for each session's graph, so changing them on the main list does not change how a session's graph opens.

### Pause and replay the graph

A live graph changes while you read it. To hold the picture still, or to look back at what just happened, use the timeline under the graph:

| Control | What it does |
|---|---|
| Play/pause button | From live, holds the picture on screen. While you hold a frame, plays the recording forward from it, or pauses it again |
| **Previous frame** / **Next frame** | Steps back or forward 1 frame. From live, **Previous frame** shows the moment just before the latest one |
| Scrubber | Moves to any point in the recording. Drag it, click it, or use the arrow keys |
| Readout | While you hold a frame, how far behind live the picture is, such as *-12s*. While the graph is live, how much history you can move back through |
| **Live** / **Back to live** | Reads **Live** while the graph follows your agents, and **Back to live** while you hold a frame. Click **Back to live** to return to live |

The play/pause button's tooltip says what it does next: *Hold this moment on screen*, *Play the recording from here*, or *Pause the replay*. To see the time of the last update, hover over **Live**.

Your agents keep working while you hold a frame, and Kepler keeps recording, so the readout shows the picture falling further behind. Kepler records only while something is happening: a session is running or thinking, or a tool call or subagent is running. While every agent is idle, the graph has nothing to replay, and the timeline's controls are unavailable.

<figure style="text-align:center">
  <a href="/wp-content/uploads/freeze-button-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/freeze-button-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Agent Graph with its replay timeline held on a frame: under the graph's nodes, Play, Previous frame, Next frame, the scrubber, a -0s readout, and Back to live in place of the Live pill.">
  </a>
  <figcaption style="text-align:center; color:#888">The timeline under the graph, holding a frame.</figcaption>
</figure>

***

## What the graph does not show

The graph does not show everything about your agents' work:

- **No token counts per turn.** Agents report a total for the context window, not the tokens in and out of each turn. The graph shows how full the context window is, and the cost, instead.
- **No durations for calls Kepler did not watch.** See [Click any node for detail](#click-any-node-for-detail).
- **No cost or time per subagent.** No agent reports them.
- **No activity for external and terminal sessions.** Kepler can see that these sessions exist but not what they are doing, so the graph shows each one as a single node with a badge, instead of showing it as idle.
- **No history after Kepler restarts.** Kepler keeps a session's history in memory only while it runs, so after a restart the nodes beneath a session are empty, though the session node remains.

When nothing is running, the graph reads **Nothing running yet**, with the hint *Start an agent session and its activity appears here in real time.* When sessions exist but your filters exclude all of them, the hint changes to *No sessions match the current filters.*

***

## Send feedback

The Agent Graph is new, and it will change. To tell the Kepler team whether it helps you, click **Feedback** in the top bar to open **Send feedback**, then follow these steps:

1. Pick a **Type**: **Feature request**, **Bug report**, or **General feedback**.
2. Write a **Message**.
3. Send it.

You can also post feedback on the public issue board at [github.com/gitkraken/gk-ade/issues](https://github.com/gitkraken/gk-ade/issues).

---
