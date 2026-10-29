---
title: The Agent Graph
description: A live graph of everything your agents are doing - every task, session, turn, tool call, subagent, and file, drawn as it happens.
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

Running several agents at once is easy. Knowing what they're all doing is the hard part.

The **Agent Graph** draws it: every task, the sessions inside it, each turn, every tool call, every subagent, and the files the agents touch. It lays all of this out as a graph that updates live, with nodes appearing as the agents work. GitKraken has spent a decade drawing things developers otherwise hold in their heads. The commit graph did it for history, and the Agent Graph does it for agent work.

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-graph.gif" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-graph.gif" class="help-center-img img-bordered" alt="The Agent Graph animating as agents work, with turn, tool-call, and file nodes appearing, including one tool call in an error state">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent Graph, growing live as agents work.</figcaption>
</figure>

***

## Open it

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-graph-toggle-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-graph-toggle-sep-2026.png" class="help-center-img img-bordered" alt="The top-left control's three segments: Todo, Tasks in progress, and Agent Graph selected">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent Graph segment, beside Todo and Tasks in progress.</figcaption>
</figure>

The graph is a segment of its own, beside **Todo** and **Tasks in progress**, rather than a way of arranging the list, because it replaces the list instead of laying it out.

| Where | How |
|---|---|
| **The whole fleet** | The top-left control: switch to the **Agent Graph** segment. Kepler remembers your choice across restarts |
| **One session** | The task view's rail carries a per-session toggle on each session row, which docks that one session's graph beside its transcript |

See [Arranging Your Work](/kepler/arranging-your-work) for **Todo** and **Tasks in progress**, and for the **List** and **Board** layouts those two segments offer. The Agent Graph has no page of its own, but rather it's a segment of the main list and a pane within the task view.

When opened from the main list, the graph draws exactly what the list normally shows including your search and filter(s). Opened on a session, the graph starts fully expanded and grows downward (or to the right) with the conversation's tool calls and subagents.

The graph is a **visualization**, not a workspace. To work in a session, open the agent session from your Task. The graph's node details link straight through. To watch several agents at once and answer them, shift-click sessions to open them side by side instead; see [The Task View](/kepler/task-view).

***

## How to read it

<figure style="text-align:center">
  <a href="/wp-content/uploads/how-to-read-graph-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/how-to-read-graph-aug-2026.png" class="help-center-img img-bordered" alt="The Agent Graph for one task, read left to right: the task Fix the cart total and its session, both marked Needs you, then three turns. Turn 1 and Turn 2 are folded, each with a chevron and 3 hidden nodes (Turn 2 also shows one failed call); the latest turn is open on its tool calls, Read cart.test.js, Edit cart.js and Run npm test, with the files they touched, and a permission request marked Needs you.">
  </a>
  <figcaption style="text-align:center; color:#888">The graph's layers, from task to file, with past turns folded.</figcaption>
</figure>

The graph is layered. Depth grows away from the root.

| Layer | What it is |
|---|---|
| **Task** | The root. One per task. See [Tasks and Resources](/kepler/tasks-and-resources) |
| **Session** | Each agent session in that task, with its agent and model |
| **Turn** | One exchange: **Turn 1**, **Turn 2**, and so on |
| **Tool call** | What the agent did in that turn |
| **Subagent** | A subagent the agent spawned, with its own tool calls beneath it |
| **File** | The files a call touched: the bottom layer, and where you notice two sessions converging on the same file |

The graph draws only sessions that belong to a task. An external session Kepler observed but no task owns has nowhere to hang from, so the graph leaves it out.

### Past turns start folded

On the main list's graph, each session shows its latest turn open and folds every earlier one, so a long session reads as its current work. A folded card carries a chevron and the number of nodes beneath it, and its tooltip says how many nodes are folded away. Double-click a folded turn to unfold it. Double-click any card with children, such as a session, a turn, or a subagent, to fold what's beneath it again. A session's own graph pane starts with every turn open.

Two node kinds are worth spotting immediately, because nothing moves until you act: **Permission needed** and **Question for you**.

### What a node's state means

| State | What's happening |
|---|---|
| **Running a tool** | Working right now |
| **Waiting on the model** | Thinking |
| **Blocked** | Waiting on you |
| **Finished — unread** | Done, and you haven't looked |
| **Done** | Finished and seen |
| **Stopped** | You interrupted it |
| **Failed** | It errored |
| **Idle** | Nothing in flight |

Three states get a word on the card rather than a colour, because they're asking for something: **New**, **Needs you**, and **Error**.

### Tool calls are coloured by what they do

**Read · Edit · Delete · Move · Search · Execute · Think · Fetch · Switch mode · Other**

This is the fastest read on the graph. A task that's all **Read** is still orienting; a wall of **Edit** means it's committing to an approach.

Repeated calls of the same kind fold into one node badged **Group**, which keeps the kind as its name and reports the count and how many distinct files it spans. That way, a **Read** node reading *9 calls · 4 files* doesn't read as the same file nine times. Double-click a group to unfold it, and double-click again to fold it back up. A single click only selects a node, so inspecting a group never reshuffles the graph.

***

## Click any node for detail

<figure style="text-align:center">
  <a href="/wp-content/uploads/node-details-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/node-details-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Agent Graph with the Edit cart.js tool-call node of Fix the cart total selected and its chain highlighted (the task, its session, Turn 1, Edit cart.js and cart.js), and the node's details panel open beside the graph: Tool call, Done, Edit cart.js, the path Fix the cart total › its session › Turn 1, Last activity just now, Status Done and the file it touched, cart.js.">
  </a>
  <figcaption style="text-align:center; color:#888">A node's details, open beside the graph.</figcaption>
</figure>

Selecting a node opens details beside the graph. What you see depends on what you clicked:

- **Session**: the agent, state, model, mode, context used, cost, where it's running, and its stop reason.
- **Tool call**: the tool, the exact input, the files and paths it touched, how long it took, and how many calls failed.
- **Subagent**: its type, its prompt, and its own calls.
- **Task**: its status (**Active**, **On hold**, or **Archived**), its sessions, and its resources.
- **File**: a preview of the file. For a large file, the preview reads only its beginning.

A node with children also gets a fold button in the details header, **Collapse what is under this node** or **Expand what is under this node**, which does the same as double-clicking the card. The stats rail keeps counting the whole graph, folded nodes included.

<figure style="text-align:center">
  <a href="/wp-content/uploads/graph-collapse-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/graph-collapse-oct-2026.png" class="help-center-img img-bordered" alt="The Agent Graph with the folded Turn 2 node selected, showing the failed call mark and a chevron with 3 hidden nodes, while the rest of the graph dims. Its details panel shows Turn, Done, Turn 2, the path Fix the cart total › Discount codes break the cart…, 1 failed call, Tool calls 2 and the prompt Add a test for the discount, with the back, Expand what is under this node and close buttons in its header.">
  </a>
  <figcaption style="text-align:center; color:#888">A folded turn selected, with Expand what is under this node in its details header.</figcaption>
</figure>

**Duration is only shown when Kepler actually watched the call happen.** Replayed history can't tell you how long something took, so the graph leaves it out rather than estimating.

From the details you can **Open task** or **Open session** to jump into the work, and **Copy** any input or prompt.

***

## The stats rail

A rail down the right-hand side of the graph, reading top to bottom.

<figure style="text-align:center">
  <a href="/wp-content/uploads/stat-rails-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/stat-rails-2026.png" class="help-center-img img-bordered" alt="The stats rail down the right-hand side of the Agent Graph">
  </a>
  <figcaption style="text-align:center; color:#888">The stats rail.</figcaption>
</figure>

It's the fleet's numbers rather than its shape, drawn from the same snapshot the canvas draws, so the two can never disagree. On the dashboard the rail steps aside when you have a panel open.

### The counters

Six tiles, two across, at the top of the rail:

| Counter | What it counts |
|---|---|
| **Working** | Sessions mid-turn with a tool actually executing |
| **Blocked** | Sessions that can't move without you |
| **Thinking** | Sessions mid-turn with nothing executing: waiting on the model |
| **Unread** | Sessions that finished a turn you haven't looked at |
| **Subagents** | Subagents in flight right now |
| **Failed calls** | Tool calls that errored, across the drawn graph |

**Working** and **Thinking** are split on purpose: a fleet that's entirely waiting on the model is a different situation from one that's entirely running commands, and a single "busy" number can't tell you which you have. **Blocked** and **Unread** are the two that should pull you somewhere. Everything else is context.

### Needs attention

Directly under the counters, and only when there's something in it: everything asking for you, most urgent first, tagged **Needs you**, **Error**, or **New**. Each row jumps to its node, which is the point, because at three hundred nodes no per-node marker is findable.

### Throughput

A trace of the fleet's activity over time, and under it:

| Reading | What it tells you |
|---|---|
| **Tasks** / **Sessions** | How much is drawn |
| **Tools** | Tool calls in flight right now |
| **Files touched** | How many distinct files the drawn graph has reached |
| **Context** | How much context window your sessions have consumed, as a total and a percentage. Only sessions that report usage count, and the row is absent when none do |
| **Cost** | What the work has cost so far, in the currency your sessions agreed on. Absent when they report none, or report several |

### Tool spectrum

The calls broken down by kind, with a bar and a count each: the fastest read on whether the fleet is reading, editing, or executing. Kinds with no calls yet don't appear, and until any do the panel reads **No tool activity yet**.

### Usage windows

Your agent subscription windows, one bar per window per agent, each with the share used. The panel appears once there's something to show. With **Check plan usage with each agent's provider** on, which is the default in **Settings → Agents → Usage limits**, Kepler asks each agent's provider for your usage. With it off, the panel shows only readings your agents report themselves, dimmed once they're out of date, and stays hidden until an agent reports one. See [Settings](/kepler/settings).

The bars here show only how much of each window you've used. Whether you're on pace for a window, and when it runs out at your current rate, shows in a session's usage meter. See [Usage indicators](/kepler/agent-sessions#usage-indicators).

### What was folded away

At the foot of the rail, a note counts what the readability rules removed from the canvas:

- Tool calls grouped.
- Sessions filtered out.
- Sessions Kepler can see but not trace.
- Tasks with no session.

Kepler reports this instead of staying silent, because a graph that quietly hides half the calls reads as "that's all that happened".

***

## Finding things in a busy graph

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-graph-header-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-graph-header-sep-2026.png" class="help-center-img img-bordered" alt="The Agent Graph's header, with the search box, and the Options menu open showing Layout, Zoom to selection, Compact stats, and Group repeated tool calls">
  </a>
  <figcaption style="text-align:center; color:#888">The graph's header controls, with the Options menu open.</figcaption>
</figure>

The graph's header carries a search box, an **Options** menu, the depth slider, and the freeze control. Zooming lives on the canvas itself.

| Control | Where | What it does |
|---|---|---|
| *Filter tasks, sessions, agents…* | Header | Narrows the graph by name, across all three |
| **Layout** | Options | Grow the tree **Left to right** or **Top to bottom** |
| **Zoom to selection** | Options | Frames a picked node with its tree, ancestors, and siblings; holds still when it's already in view. Two nested settings say when the camera may move again: **Follow the tree as it grows** (zooms out as far as it takes rather than stopping once cards get too small to make out) and **Re-frame when the space changes** (reframes when a panel opens beside the graph or the window resizes) |
| **Compact stats** | Options | Same numbers in half the room: circular meters and denser tiles, for a smaller window |
| **Group repeated tool calls** | Options | On by default. Off draws every call as its own node |
| **Only active sessions** | Options | Hide sessions that have ended, while idle ones stay. On by default on the main list, where the **Options** badge counts it once you turn it off, and off by default in a session's own graph pane |
| **Agent** / **Repo** | Options | Narrow to one agent or repository. Not offered on the main list, whose own facets already do it |
| **Detail depth** | Header | How many layers deep the graph draws: up to five, four by default |
| **Zoom in** / **Zoom out** / **Fit to view** | Canvas | Move around. You can also pan by dragging, and press Escape to drop a selection |

Kepler remembers depth and layout per surface, so narrowing the graph on the main list doesn't change what a session pane opens at.

### Freeze it

A live graph moves while you're trying to read it. **Freeze the graph** holds it still so you can inspect a node without it shifting. A chip beside the graph reads **Live** while it's updating (with the moment of the last sample, so "live" is demonstrably live) and **Frozen** until you **Resume live updates**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/freeze-button-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/freeze-button-aug-2026.png" class="help-center-img img-bordered" alt="The Freeze the graph button">
  </a>
  <figcaption style="text-align:center; color:#888">The Freeze the graph button.</figcaption>
</figure>

***

## What it doesn't show

Worth knowing, so you don't read precision into it that isn't there:

- **No per-turn token counts.** Agents report a context-window total, not tokens in and out per turn. The graph shows context fill and cost instead.
- **No timings for calls it didn't watch.** See above.
- **No cost or latency per subagent.** No agent reports it.
- **External and terminal sessions have no activity branch.** Kepler can see that they exist but not what they're doing, so they draw as leaves with a badge rather than looking idle.
- **Transcripts don't survive a Kepler restart.** A session's history is held in memory for the life of the backend, so a restart empties the branches beneath a session even though the session itself remains.

With nothing running at all, the graph reads **Nothing running yet**, with the hint *Start an agent session and its activity appears here in real time.* Once sessions exist but your filters exclude every one of them, the hint changes to *No sessions match the current filters.*

***

## Early days

The Agent Graph is new, and a lot about it will change. It's worth opening next to the agents you're already running, and we'd like to know whether it actually helps. **Feedback**, in the top bar, opens **Send feedback**:

1. Pick a **Type**: **Feature request**, **Bug report**, or **General feedback**.
2. Write a **Message**.
3. Send it.

Alternatively, share feedback to the public issue board at [github.com/gitkraken/gk-ade/issues](https://github.com/gitkraken/gk-ade/issues).

---
