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
last_verified: 2026-09
llms_include: true
tags: [arrangements, inbox, list, columns, grouping, filters, search, archive, cleanup]
taxonomy:
  category: kepler
---
<kbd>Last updated: September 2026</kbd>

Kepler has one interface rather than a set of views, so you shape it instead of switching away from it. Three controls do most of the work: the arrangement, the grouping, and the filters. Each segment remembers its own.

<figure style="text-align:center">
  <a href="/wp-content/uploads/arrange-work-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/arrange-work-sep-2026.png" class="help-center-img img-bordered" alt="The grouping, filter, and view controls above Kepler's list, grouped by Inbox">
  </a>
  <figcaption style="text-align:center; color:#888">The arrangement, grouping, and filter controls.</figcaption>
</figure>

This page assumes you know what's on screen; see [The Kepler Interface](/kepler/kepler-interface) for that.

***

## Two layouts

<figure style="text-align:center">
  <a href="/wp-content/uploads/view-options-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/view-options-sep-2026.png" class="help-center-img img-bordered" alt="The View control open, showing List and Columns as layout options">
  </a>
  <figcaption style="text-align:center; color:#888">The View control's layout options.</figcaption>
</figure>

The **View** control decides how Kepler draws the list.

| View | What you get | Best for |
|---|---|---|
| **List** | A dense list you read top to bottom | Scanning everything at once |
| **Columns** | The same list turned on its side, one column per group | Seeing how far along things are |

**List** is the default, and each segment remembers its own choice across restarts — Todo can stay a list while Tasks in progress stays a board. Both layouts respect the grouping and filters below.

**Columns** draws the sections of the *current* grouping as a horizontal board, so what the columns are is up to the **Group** control. Grouped by **Progress**, the columns are the lifecycle stages: **Exploration**, **In Development**, **In Review**, and **Done**. They stay put as work moves between them rather than appearing and vanishing under the pointer, and an empty one reads **Nothing here**. **Archived** is the exception: it appears only when something is filed there. On every other grouping, Kepler doesn't draw a section with nothing in it.

<div class="note" markdown="1">

**The Agent Graph is no longer a layout.** It's a segment of its own, beside **Todo** and **Tasks in progress**, because it replaces the list rather than arranging it. Selecting it hides **Group** and **View** and gives the graph's own controls the strip. See [The Agent Graph](/kepler/agent-graph).

</div>

***

## Group

The **Group** dropdown reorganizes the list.

<figure style="text-align:center">
  <a href="/wp-content/uploads/group-options-tasks-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/group-options-tasks-sep-2026.png" class="help-center-img img-bordered" alt="The Group dropdown open on Tasks in progress, showing Inbox checked as the default, then Progress, Activity, Repository, and None">
  </a>
  <figcaption style="text-align:center; color:#888">The Group dropdown on Tasks in progress.</figcaption>
</figure>

The available groupings differ by segment.

| Segment | Group by | Default |
|---|---|---|
| **Todo** | Type, Needs my attention, Your role, Provider, Repository, Status, None | Type |
| **Tasks in progress** | Inbox, Progress, Activity, Repository, None | Inbox |

### Inbox

**Inbox** is the default on Tasks in progress, and it is viewer-relative: it sorts by what each task is asking of *you*, not by where the work has got to. It reads top-down from what needs you toward what's filed away.

| Bucket | What lands there |
|---|---|
| **Unread** | A session finished a turn you haven't looked at |
| **Needs attention** | A session is blocked on a permission request or a question |
| **Running** | An agent is working on it |
| **Recent** | Moved in the last 24 hours |
| **Earlier** | Moved before that |
| **Done** | Finished, waiting only on the decision to archive it |
| **Archived** | Your own filing decision, which outranks everything else |

A session stays marked **unseen** until you actually look at it, so a turn that finished while you were elsewhere doesn't quietly clear itself.

**Inbox** is one of two axes where a task can appear twice: a task that is both unread *and* blocked on you is listed under **Unread** and **Needs attention**, because each bucket is a complete answer to its own question and leaving it out of either would make that list lie. **Running** is exclusive — a task already at the top doesn't need a second row saying it's busy too. So is **Done**, which stands in for the time bucket a task would otherwise get.

The 24-hour window is fixed rather than a setting: the axis is meant to be a quick daily sweep, not a tunable report.

### The other axes

**Progress** and **Activity** are two different questions about the same tasks. *Progress* is how far the work has got: **Exploration**, **In Development**, **In Review**, **Done**, **Archived**. *Activity* is what the task's agent sessions are doing right now, in the sessions' own words: **Waiting**, **Running**, **Ready**, **Spawning**, **Unread**, **Idle**, **Error**, **Disconnected**, and **Terminated**. Grouping by Activity also adds **No sessions** for a task nobody has started, then **Done**, and **Archived** last. Group by Progress to see the shape of the pipeline; group by Activity to see what needs a person.

**Repository** is the other axis that can list a task twice: a task bound to worktrees in several repositories appears under each of them, because the axis answers "what's happening in *this* repository" one repository at a time.

Tasks in progress has no Status grouping, because a task's status *is* its progress stage, a second axis under another name.

On Todo, **Needs my attention** is the viewer-relative axis: what each item is asking of you right now — **Changes requested**, **Needs my review**, **Re-review**, **Comments** — with **No action needed** last, where it can't push a real obligation below the fold. It's an axis rather than a pinned section so it obeys the same rules as every other grouping: one bucket per state, collapsible headers, and no row shown twice.

Items with no repository or provider collect under **No repository** and **No provider**. A pull request whose provider didn't say who authored it groups under **Unattributed**; an issue, which has no author-or-reviewer axis at all, groups under **Not applicable**.

### Fold a section

Every group header is a fold toggle, with the section's count beside its name.

<figure style="text-align:center">
  <a href="/wp-content/uploads/group-folds-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/group-folds-sep-2026.png" class="help-center-img img-bordered" alt="A group header showing a fold toggle and the section's count">
  </a>
  <figcaption style="text-align:center; color:#888">A group header, with its fold toggle and count.</figcaption>
</figure>

Folding one unmounts its rows, so a long **Done** list stops costing anything to keep around. **Archived** starts folded when you group by Activity or Inbox, since it's the section that work is filed *into*. Folds last only for the current run; Kepler doesn't write them to disk.

***

## Filter

The **Filter** menu holds one flyout per facet.

<figure style="text-align:center">
  <a href="/wp-content/uploads/filter-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/filter-sep-2026.png" class="help-center-img img-bordered" alt="The Filter menu open, showing one flyout per facet">
  </a>
  <figcaption style="text-align:center; color:#888">The Filter menu, with one flyout per facet.</figcaption>
</figure>

Kepler hides facets with nothing to offer, so a single-repo setup won't show a Repository facet at all.

| Segment | Facets |
|---|---|
| **Todo** | Type · Your role · Status · Provider · Repository · Assignee · Issue type · Label · Project · Linked work |
| **Tasks in progress** | Progress · Activity · Repository · Agent · Linked work |

**Issue type**, **Label**, and **Project** carry your provider's own vocabulary (a Jira issue type, your team's tags, a board name), not a Kepler-side translation of them.

**Linked work** filters by whether an item is connected to work on the other side: *Has a task* / *No task yet* in Todo, and *Has a PR or issue* / *No PR or issue* in Tasks in progress.

**Values within one facet combine as a union.** Ticking GitHub *and* GitLab under **Provider** shows items from either, not items that are somehow both. A facet with nothing ticked reads **Any** and narrows nothing. The **Search filters…** box finds a facet value without scrolling, and the menu reports **{count} of {total}** as you narrow.

External sessions stay listed under a filter that has no way to answer for them, rather than vanishing because a facet couldn't classify them.

Once a search or a filter is narrowing the list, the strip reports the match as *{count} of {total}* and offers **Clear filters**, which drops the search text and the facets together. **Refresh** re-fetches the current segment from your providers.

***

## Search

The search box matches on **title, reference, or repository**: *Search title, ref, or repo…*.

<figure style="text-align:center">
  <a href="/wp-content/uploads/search-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/search-sep-2026.png" class="help-center-img img-bordered" alt="The search box above Kepler's list, with a clear button">
  </a>
  <figcaption style="text-align:center; color:#888">The search box, with the clear button.</figcaption>
</figure>

Click the **X** button to clear the search and return to the full list.

***

## What Kepler remembers

Each segment remembers its own search, grouping, and filters, since they differ enough that sharing them would be meaningless. Kepler restores the segment you left along with its view. Kepler also remembers which panels were open, but only for the length of a run, so a round trip to the other segment doesn't cost you the panel you were reading. A relaunch still opens on a plain list rather than a stale panel.

***

## Archive, restore, and clean up in bulk

**Archive task** files a task away. It leaves the live buckets for **Archived**, its rows and sessions survive, and Kepler stops only the agents whose checkout is about to disappear.

<figure style="text-align:center">
  <a href="/wp-content/uploads/archive-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/archive-sep-2026.png" class="help-center-img img-bordered" alt="The row's ⋮ menu open, with Archive task highlighted among Open in new window, Mark as unread, Rename task, Add resource, and Delete task">
  </a>
  <figcaption style="text-align:center; color:#888">Archive task, in the row's ⋮ menu.</figcaption>
</figure>

The confirmation offers the same two cascades the delete does: **Also delete worktrees** and **Also delete branches**. This way, finishing with a task doesn't have to mean deleting it to clean it off the disk. Archiving outranks everything else, so a task you filed away can't climb back into a live section because a shell is still open on it.

**Restoring a task takes an extra step: filter first.** An archived task's row doesn't offer **Restore task** while it's mixed in with everything else. Filter **Activity** to **Archived** (see [Filter](#filter) above), and the **⋮** menu on a row in that filtered list swaps **Archive task** for **Restore task**, which puts it straight back. **Restore task** is also on the task page's own header as soon as the task is archived, with no filtering needed.

For more than one at a time, every section header on **Tasks in progress** carries a quiet **Select**. Press it, and that corner of the header becomes a bar: a select-all box, **{count} selected**, and the batch verbs. The section's rows also grow checkboxes. One section selects at a time, and while you're selecting, a click ticks a row rather than opening its panel.

| Button | What it does |
|---|---|
| **Archive** | Archives every selected task that isn't already archived |
| **Restore** | Takes Archive's place when everything selected is already archived. Only appears once you've filtered the list to **Activity: Archived** |
| **Delete** | Removes the selected tasks for good |
| **Cancel** | Leaves selection mode and drops the set |

Both **Archive** and **Delete** confirm, and both offer **Also delete worktrees** and **Also delete branches**. Kepler remembers what you ticked, per dialog, so a habit doesn't have to be re-entered every time. The batch confirmation doesn't list what each individual checkout would lose; open a task's own **⋮** for that.

---
