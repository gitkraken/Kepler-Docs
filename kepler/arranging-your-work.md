---
title: Arranging Your Work
description: One interface means you shape it rather than switch away from it. Choose an arrangement, group and filter the list, fold what you're done with, and archive in bulk.
product: Kepler
feature: Kepler Interface
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
integrations: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops, jira, linear, trello]
hosted_variant: both
status: GA
last_verified: 2026-08
llms_include: true
tags: [arrangements, rows, columns, grouping, filters, search, archive, cleanup]
taxonomy:
  category: kepler
---
<kbd>Last updated: August 2026</kbd>

Kepler has one interface rather than a set of views, so you shape it instead of switching away from it. Three controls do most of the work: the arrangement, the grouping, and the filters. Each segment remembers its own.

<figure>
  <img src="/wp-content/uploads/arrange-work-aug-2026.png" class="help-center-img img-bordered" alt="The arrangement, grouping, and filter controls above Kepler's list">
  <figcaption style="text-align:center; color:#888">The arrangement, grouping, and filter controls.</figcaption>
</figure>

This page assumes you know what's on screen; see [The Kepler Interface](/kepler/kepler-interface) for that.

***

## Three arrangements

<figure>
  <img src="/wp-content/uploads/view-options-aug-2026.png" class="help-center-img img-bordered" alt="The View control open, showing Rows, Columns, and the graph as arrangement options">
  <figcaption style="text-align:center; color:#888">The View control's arrangement options.</figcaption>
</figure>

The **View** control decides how Kepler draws the list.

| View | What you get | Best for |
|---|---|---|
| **Rows** | A dense list you read top to bottom | Scanning everything at once |
| **Columns** | The same list turned on its side, one column per group | Seeing how far along things are |
| **Agent Graph** | A live visualization of every agent, turn, tool call, and file | Seeing what your agents are actually doing (see [The Agent Graph](/kepler/agent-graph)) |

**Rows** is the default, and Kepler remembers your choice across restarts. **Rows** and **Columns** both respect the grouping and filters below.

**Columns** draws the sections of the *current* grouping as a horizontal board, so what the columns are is up to the **Group** control. Grouped by **Progress** (the default on Tasks in progress), the columns are the lifecycle stages: **Exploration**, **In Development**, **In Review**, and **Done**. They stay put as work moves between them rather than appearing and vanishing under the pointer, and an empty one reads **Nothing here**. **Archived** is the exception: it appears only when something is filed there. On every other grouping, Kepler doesn't draw a section with nothing in it.

The **Agent Graph** replaces the list with the graph, narrowed to whatever your search and filters left. **Group** goes away while it's on, since the graph draws one tree per task. The graph's own controls take its place in the strip.

***

## Group

The **Group** dropdown reorganizes the list.

<figure>
  <img src="/wp-content/uploads/group-options-tasks-aug-2026.png" class="help-center-img img-bordered" alt="The Group dropdown open on Tasks in progress, showing Progress, Activity, Repository, and None">
  <figcaption style="text-align:center; color:#888">The Group dropdown on Tasks in progress.</figcaption>
</figure>

The available groupings differ by segment.

| Segment | Group by | Default |
|---|---|---|
| **Todo** | Type, Your role, Provider, Repository, Status, None | Type |
| **Tasks in progress** | Progress, Activity, Repository, None | Progress |

**Progress** and **Activity** are two different questions about the same tasks. *Progress* is how far the work has got: **Exploration**, **In Development**, **In Review**, **Done**, **Archived**. *Activity* is what the task's agent sessions are doing right now, in the sessions' own words: **Waiting**, **Running**, **Ready**, **Spawning**, **Unread**, **Idle**, **Error**, **Disconnected**, and **Terminated**. Grouping by Activity also adds **No sessions** for a task nobody has started, then **Done**, and **Archived** last. Group by Progress to see the shape of the pipeline; group by Activity to see what needs a person.

Tasks in progress has no Status grouping, because a task's status *is* its progress stage, a second axis under another name.

Items with no repository or provider collect under **No repository** and **No provider**. A pull request whose provider didn't say who authored it groups under **Unattributed**; an issue, which has no author-or-reviewer axis at all, groups under **Not applicable**.

### Fold a section

Every group header is a fold toggle, with the section's count beside its name.

<figure>
  <img src="/wp-content/uploads/group-folds-aug-2026.png" class="help-center-img img-bordered" alt="A group header showing a fold toggle and the section's count">
  <figcaption style="text-align:center; color:#888">A group header, with its fold toggle and count.</figcaption>
</figure>

Folding one unmounts its rows, so a long **Done** list stops costing anything to keep around. **Archived** starts folded when you group by Activity, since it's the section that work is filed *into*. Folds last only for the current run; Kepler doesn't write them to disk.

***

## Filter

The **Filter** menu holds one flyout per facet.

<figure>
  <img src="/wp-content/uploads/filter-aug-2026.png" class="help-center-img img-bordered" alt="The Filter menu open, showing one flyout per facet">
  <figcaption style="text-align:center; color:#888">The Filter menu, with one flyout per facet.</figcaption>
</figure>

Kepler hides facets with nothing to offer, so a single-repo setup won't show a Repository facet at all.

| Segment | Facets |
|---|---|
| **Todo** | Type · Your role · Status · Provider · Repository · Assignee · Issue type · Label · Project · Linked work |
| **Tasks in progress** | Progress · Activity · Repository · Agent · Linked work |

**Issue type**, **Label**, and **Project** carry your provider's own vocabulary (a Jira issue type, your team's tags, a board name), not a Kepler-side translation of them.

**Linked work** filters by whether an item is connected to work on the other side: *Has a task* / *No task yet* in Todo, and *Has a PR or issue* / *No PR or issue* in Tasks in progress.

Once a search or a filter is narrowing the list, the strip reports the match as *{count} of {total}* and offers **Clear filters**, which drops the search text and the facets together. **Refresh** re-fetches the current segment from your providers.

***

## Search

The search box matches on **title, reference, or repository**: *Search title, ref, or repo…*.

<figure>
  <img src="/wp-content/uploads/search-aug-2026.png" class="help-center-img img-bordered" alt="The search box above Kepler's list, with a clear button">
  <figcaption style="text-align:center; color:#888">The search box, with the clear button.</figcaption>
</figure>

Click the **X** button to clear the search and return to the full list.

***

## What Kepler remembers

Each segment remembers its own search, grouping, and filters, since they differ enough that sharing them would be meaningless. Kepler restores the segment you left along with its view. Kepler also remembers which panels were open, but only for the length of a run, so a round trip to the other segment doesn't cost you the panel you were reading. A relaunch still opens on a plain list rather than a stale panel.

***

## Archive, restore, and clean up in bulk

**Archive task** files a task away. It leaves the live buckets for **Archived**, its rows and sessions survive, and Kepler stops only the agents whose checkout is about to disappear.

<figure>
  <img src="/wp-content/uploads/archive-aug-2026.png" class="help-center-img img-bordered" alt="The Archive task confirmation, offering to also delete worktrees and branches">
  <figcaption style="text-align:center; color:#888">The Archive task confirmation.</figcaption>
</figure>

The confirmation offers the same two cascades the delete does: **Also delete worktrees** and **Also delete branches**. This way, finishing with a task doesn't have to mean deleting it to clean it off the disk. Archiving outranks everything else, so a task you filed away can't climb back into a live section because a shell is still open on it.

**Restore task** brings it back to whatever section its work now belongs in. Nothing comes back on disk: a checkout the archive removed is gone from git.

For more than one at a time, every section header on **Tasks in progress** carries a quiet **Select**. Press it, and that corner of the header becomes a bar: a select-all box, **{count} selected**, and the batch verbs. The section's rows also grow checkboxes. One section selects at a time, and while you're selecting, a click ticks a row rather than opening its panel.

| Button | What it does |
|---|---|
| **Archive** | Archives every selected task that isn't already archived |
| **Restore** | Takes Archive's place when everything selected is already archived |
| **Delete** | Removes the selected tasks for good |
| **Cancel** | Leaves selection mode and drops the set |

Both **Archive** and **Delete** confirm, and both offer **Also delete worktrees** and **Also delete branches**. **Restore** takes no options: it removes nothing. The batch confirmation doesn't list what each individual checkout would lose; open a task's own **⋮** for that.

---
