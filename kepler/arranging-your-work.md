---
title: Arranging Your Work
description: One interface means you shape it rather than switch away from it. Choose an arrangement, group, sort and filter the list, save a combination as a named view, set a task's progress, and archive in bulk.
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
last_verified: 2026-10
llms_include: true
tags: [arrangements, inbox, list, columns, grouping, sorting, filters, search, saved-views, progress, on-hold, archive, cleanup]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Kepler has one interface rather than a set of views, so you shape it instead of switching away from it. Four controls do most of the work: the grouping, the sort, the filters, and the layout. Each segment remembers its own, and a combination you come back to can be saved under a name.

<figure style="text-align:center">
  <a href="/wp-content/uploads/arrange-work-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/arrange-work-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The dashboard's arranging controls: the Saved views chip, Group: Inbox, Sort: Updated, Filter, Open all in panels, Panel layout, the List and Board view switch, and Refresh.">
  </a>
  <figcaption style="text-align:center; color:#888">The saved views, grouping, sort, filter, panel, and layout controls.</figcaption>
</figure>

This page assumes you know what's on screen; see [The Kepler Interface](/kepler/kepler-interface) for that.

Two more controls sit in the strip. **Open all** opens every listed row in panels, and **Panel layout** lays open panels out side by side (**Columns**) or in a **Grid**. See [Open a panel](/kepler/kepler-interface#open-a-panel). **Group** and **Sort** open as menus that grow to fit the window, so a long list of groupings is never cut off.

When the window is too narrow for the whole strip, **Group**, **Sort**, **Filter**, the layout switch, **Panel layout**, and **Open all** fold into a single **Options** button, followed by the saved views and finally the search box. A count on **Options** says how many searches and filters are still narrowing the list, so a narrowed list never hides behind a closed popover.

***

## Two layouts

<figure style="text-align:center">
  <a href="/wp-content/uploads/view-options-sep-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/view-options-sep-2026-v2@2x.png" class="help-center-img img-bordered" alt="The layout switch on the dashboard: List, selected, and Board.">
  </a>
  <figcaption style="text-align:center; color:#888">The View control's layout options.</figcaption>
</figure>

The **View** control decides how Kepler draws the list.

| View | What you get | Best for |
|---|---|---|
| **List** | A dense list you read top to bottom | Scanning everything at once |
| **Board** | The same list turned on its side, one column per group | Seeing how far along things are, and moving tasks between stages |

**List** is the default, and each segment remembers its own choice across restarts, so Todo can stay a list while Tasks in progress stays a board. Both layouts respect the grouping and filters below.

**Board** draws the sections of the *current* grouping as columns side by side, so what the columns are is up to the **Group** control. Grouped by **Progress**, the columns are the lifecycle stages: **Exploration**, **In Development**, **In Review**, and **Done**. They stay put as work moves between them rather than appearing and vanishing under the pointer, and an empty one reads **Nothing here**. **On hold** and **Archived** are the exceptions: each appears when something is filed there, and both appear while you drag a card so you can drop onto them. On every other grouping, Kepler doesn't draw a section with nothing in it.

Every column on the board shares one width. Drag the gap after any column to resize them all at once, or focus it and use the arrow keys, with **Home** and **End** for the narrowest and widest. Double-click the gap to return to the default width. Each segment remembers its own column width. When a column has more to load, **Load more** sits at its foot. From the keyboard, **←** and **→** cross to the nearest column with a card.

<div class="note" markdown="1">

**Columns** now names a panel layout, not this view. The board was called **Columns** before; the **Panel layout** control's **Columns** and **Grid** decide how open panels are arranged instead.

</div>

<figure style="text-align:center">
  <a href="/wp-content/uploads/columns-progress-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/columns-progress-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Tasks in progress list on the Board layout, grouped by Progress: the Exploration, In Development, In Review, On hold and Done columns side by side, each with its count, Open in panels and Select. Each task is a card with its title, age, session and progress glyphs, its waiting state (New reply, or Approval needed for Run npm test), and, for a task with a worktree, its repository and branch; Done reads Nothing here. The toolbar above shows Group: Progress and Board selected.">
  </a>
  <figcaption style="text-align:center; color:#888">The Board layout, grouped by Progress.</figcaption>
</figure>

The Progress board is also where you can move a task by hand. See [Set a task's progress](#set-a-tasks-progress).

<div class="note" markdown="1">

**The Agent Graph is a segment, not a layout.** It sits beside **Todo** and **Tasks in progress** and replaces the list rather than arranging it. Selecting it hides **Group** and **View** and gives the graph's own controls the strip. See [The Agent Graph](/kepler/agent-graph).

</div>

***

## Group

The **Group** dropdown reorganizes the list.

<figure style="text-align:center">
  <a href="/wp-content/uploads/group-options-tasks-sep-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/group-options-tasks-sep-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Group menu open under Group: Inbox on Tasks in progress, listing Inbox (checked), Progress, Activity, Repository and None.">
  </a>
  <figcaption style="text-align:center; color:#888">The Group dropdown on Tasks in progress.</figcaption>
</figure>

The available groupings differ by segment.

| Segment | Group by | Default |
|---|---|---|
| **Todo** | Type, Needs my attention, Priority, Age, Your role, Assignee, Provider, Repository, Status, None | Type |
| **Tasks in progress** | Inbox, Progress, Activity, Repository, None | Inbox |

### Inbox

**Inbox** is the default on Tasks in progress, and it is viewer-relative: it sorts by what each task is asking of *you*, not by where the work has got to. It reads top-down from what needs you toward what's filed away.

| Bucket | What lands there |
|---|---|
| **Unread** | A session finished a turn you haven't looked at |
| **Needs attention** | A session is blocked on a permission request or a question, a Kepler approval request is waiting for an answer, or a program in one of the task's terminals is waiting on you |
| **Running** | An agent is working on it |
| **Recent** | Moved in the last 24 hours |
| **Earlier** | Moved before that |
| **On hold** | You or an agent put it on hold. Starts folded |
| **Done** | Finished, waiting only on the decision to archive it |
| **Archived** | Your own filing decision, which outranks everything else |

A session stays marked **unseen** until you actually look at it, so a turn that finished while you were elsewhere doesn't quietly clear itself.

**Inbox** lists every task exactly once. A task that is both unread *and* blocked on you is listed under **Needs attention**, because what's blocked on you asks more of you than output you haven't read. **Running** is exclusive too: a task already at the top doesn't need a second row saying it's busy. So is **Done**, which stands in for the time bucket a task would otherwise get.

**Drop a card on an Inbox section.** You can drag a task's card onto another Inbox section to act on it:

| Drop on | What happens |
|---|---|
| **Unread** | Marks the task unread. Refused when it has no sessions, is archived, or is already waiting on you |
| **Recent** or **Earlier** | Marks an unread task read |
| **On hold** | Puts the task on hold. Refused when it's already done |
| **Done** | Marks the task done. Refused while an agent is still working |
| **Archived** | Opens the archive confirmation |
| **Needs attention** or **Running** | Refused: these clear when you respond, or show while an agent works |

See [Set a task's progress](#set-a-tasks-progress) for how a drag looks.

A task stays in **Running** for 10 seconds after its work stops, so it doesn't drop out between one prompt and the next, and running tasks keep the order they started in rather than trading places as they work. Moves into **Unread** and **Needs attention** are immediate, since those are news.

**On hold** is your "not now", so a held task stays there even while an agent works on it. News still brings it back up: an unread turn or a blocked prompt lists it under **Unread** or **Needs attention**.

The 24-hour window is fixed rather than a setting: the axis is meant to be a quick daily sweep, not a tunable report.

### The other axes

**Progress** and **Activity** are two different questions about the same tasks. *Progress* is how far the work has got: **Exploration**, **In Development**, **In Review**, **On hold**, **Done**, **Archived**. *Activity* is what the task's agent sessions are doing right now, in the sessions' own words: **Waiting**, **Running**, **Ready**, **Spawning**, **Unread**, **Idle**, **Error**, and **Ended**. Grouping by Activity also adds **No sessions** for a task nobody has started, then **Done**, and **Archived** last. Group by Progress to see the shape of the pipeline; group by Activity to see what needs a person.

**Repository** is the only axis that can list a task twice: a task bound to worktrees in several repositories appears under each of them, because the axis answers "what's happening in *this* repository" one repository at a time.

Tasks in progress has no Status grouping, because a task's status *is* its progress stage, a second axis under another name.

On Todo, **Needs my attention** is the viewer-relative axis: what each item is asking of you right now, most pressing first:

- **Ready to merge**
- **Changes requested**
- **Cannot merge yet**
- **Needs my review**
- **Re-review**
- **Approved, comments open**
- **Comments**
- **Assigned to me**
- **Filed by me, unassigned**
- **No action needed**, last, where it can't push a real obligation below the fold

Each section header carries a **?** button (**About {label}**) that explains what lands there. For example, **Ready to merge** is *Yours, approved, no open feedback and no blockers the provider can see. It only needs merging.* It's an axis rather than a pinned section so it obeys the same rules as every other grouping: one bucket per state, collapsible headers, and no row shown twice.

On Todo, **Priority** reads an item's priority from its labels: names such as *P0* to *P4*, a *priority:* prefix, or a bare *blocker*, *critical*, *urgent*, *highest*, or *lowest*, with the most urgent label winning. It groups into **Urgent**, **High**, **Medium**, **Low**, and **Unprioritised**; every pull request groups under **Not applicable**. Kepler doesn't read a tracker's own priority field, so an issue with no such label is **Unprioritised**.

**Age** groups by when an item was created: **Today**, **This week**, **This month**, **Older**, and **No date**. **Assignee** groups by who an item is assigned to on each provider, with **Unassigned** for the rest.

On Todo, **Status** groups issues by their tracker's own workflow state, such as a Linear *In Progress* or a Jira *To Verify*, rather than collapsing every open issue into one bucket.

Items with no repository or provider collect under **No repository** and **No provider**. A pull request whose provider didn't say who authored it groups under **Unattributed**; an issue, which has no author-or-reviewer axis at all, groups under **Not applicable**.

### Fold a section

Every group header is a fold toggle, with the section's count beside its name.

<figure style="text-align:center">
  <a href="/wp-content/uploads/group-folds-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/group-folds-sep-2026.png" class="help-center-img img-bordered" alt="A group header showing a fold toggle and the section's count">
  </a>
  <figcaption style="text-align:center; color:#888">A group header, with its fold toggle and count.</figcaption>
</figure>

Folding one unmounts its rows, so a long **Done** list stops costing anything to keep around. On the **Board** layout, a folded column shrinks to a narrow rail with its name and count, marked when it holds the open item; click the rail to expand it. **Archived** starts folded when you group by Activity or Inbox, since it's the section that work is filed *into*, and so does **On hold** in the Inbox. Folds last only for the current run; Kepler doesn't write them to disk.

***

## Sort

The **Sort** control orders the items inside each group without changing the order of the groups themselves.

| Segment | Sort by | Default |
|---|---|---|
| **Todo** | Updated, Created, Name, ID, Type | Updated |
| **Tasks in progress** | Updated, Created, Name, Manual | Updated |

Dates sort newest first; **Name** and **ID** sort ascending. **ID** compares references naturally, so *#9* comes before *#10*. **Type** puts pull requests before issues and keeps the recency order within each. Each segment remembers its own sort.

### Put tasks in your own order

**Manual** sorts **Tasks in progress** in an order you set yourself, inside each section, in any grouping, on **List** or **Board**. To move a task:

- Drag its row or card to a place in its own section. A line with a dot shows where it will land, and under **Manual** a row shows a drag grip on hover.
- Choose **Move up**, **Move down**, or **Move to top of {section}** from the task's **⋮** or right-click menu. These rows appear only while the list is sorted by **Manual**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/manual-sort-drag-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/manual-sort-drag-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Upgrade the payment SDK being dragged to the top of the Unread group: a green line with a dot sits above Fix the cart total where it will land, the lifted row floats beside it, its own row is dimmed in place, and the Mark as bar covers the controls strip with Read, Exploration, In Development, On hold, Done and Archive task.">
  </a>
  <figcaption style="text-align:center; color:#888">Dragging a task to a new place in its section.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/manual-sort-menu-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/manual-sort-menu-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Task actions menu of Update checkout copy, the middle row of Unread, with the list sorted by Manual: after Mark as read and Rename task come Move up, Move down and Move to top of Unread, then Copy task link, Copy task prompt, Add resource…, Refresh, Shut down all agents, Archive task and Delete task.">
  </a>
  <figcaption style="text-align:center; color:#888">The move rows in a task's menu, under the Manual sort.</figcaption>
</figure>

You don't have to switch to **Manual** first. Drop a task in a new place in its own section while the list is sorted another way, and Kepler saves the order you see, with your move, as the **Manual** order and switches the sort to **Manual**. Switching to **Manual** yourself also keeps the current order, so nothing jumps.

When you already have a saved **Manual** order, a drop under another sort would replace it, so Kepler asks first, in a popover beside the dropped task: *Replace your Manual order?* Choose **Switch and replace Manual** to keep the move, or **Cancel** (or press **Escape**, or click away) to put the task back.

<figure style="text-align:center">
  <a href="/wp-content/uploads/manual-sort-replace-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/manual-sort-replace-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Tasks in progress after Upgrade the payment SDK was dropped at the top of Unread while sorted by Updated: the toolbar already reads Sort: Manual, the dropped row shows its drag grip, and a popover beside it asks Replace your Manual order? Keeping this move switches the sort to Manual and saves the list in the order you see now, with Cancel and Switch and replace Manual.">
  </a>
  <figcaption style="text-align:center; color:#888">Kepler asks before a drop replaces your saved Manual order.</figcaption>
</figure>

If a move fails, Kepler says *Unable to move the task*, and puts the sort back if the move had switched it.

***

## Set a task's progress

A task's progress normally follows its git and pull-request evidence (see [Status](/kepler/kepler-interface)). Sometimes that evidence can't see what you know: a review was sent back, or the work landed somewhere Kepler can't tell. When that happens, set the stage yourself.

<figure style="text-align:center">
  <a href="/wp-content/uploads/progress-menu-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/progress-menu-oct-2026.png" class="help-center-img img-bordered" alt="The Progress menu open from a task's In Review control, with Automatic checked, then Exploration, In Development, In Review, On hold, and Done.">
  </a>
  <figcaption style="text-align:center; color:#888">The Progress menu.</figcaption>
</figure>

- **The progress control.** The stage word on a task row, in the preview header, and in the task page header opens a **Progress** menu: **Automatic** (*Updates as you work*), then **Exploration**, **In Development**, **In Review**, **On hold**, and **Done**. Where there's no room for the word, the control shrinks to the stage's icon rather than disappearing.
- **The task menus.** A task's **⋮** and right-click menus carry the same choices under a **Progress** submenu, plus **Reopen** while the task is Done. Its hint says where the task will land (*Moves it to In Review*).
- **Drag a card.** In any grouping, on **List** or **Board**, drag a task's card or row. Grouped by **Progress**, drop it on another stage. On touch, press and hold to pick it up. Escape changes nothing, and dropping it in its own section reorders it (see [Put tasks in your own order](#put-tasks-in-your-own-order)). You can't drag a task that Kepler is still preparing.
- **The Mark as bar.** While you drag, a **Mark as** bar floats over the controls strip with chips for what the card can become: **Read** or **Unread**, the stages, **Reopen** for a Done task, and **Archive task**, or only **Restore** for an archived one. Drop the card on a chip.
- **From the keyboard.** With a card focused on the **Board** grouped by **Progress**, **Cmd/Ctrl+Shift+←** and **Cmd/Ctrl+Shift+→** step it one column, stopping at **Exploration** and **Done**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/progress-drag-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/progress-drag-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Board grouped by Progress while Write the 2.4 release notes is dragged from Exploration into In Review: its card stays dimmed in Exploration, the lifted card hangs below Upgrade the payment SDK, In Review is filled and outlined as the drop target, the other columns (including Done and Archived, each reading Nothing here) have dashed outlines, and a Mark as bar over the toolbar offers In Development, In Review, On hold, Done and Archive task.">
  </a>
  <figcaption style="text-align:center; color:#888">Dragging a card to another stage, with the Mark as bar over the toolbar.</figcaption>
</figure>

While you drag, the card stays where it was, faded, and a line shows where it would land. Each section that takes the card has a dashed outline that goes solid under the card; sections that refuse it fade and say why when you hover them. On the **Board**, a folded column springs open after you hold the card over it for half a second.

<figure style="text-align:center">
  <a href="/wp-content/uploads/drag-drop-bar-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/drag-drop-bar-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Fix the cart total lifted off the Tasks in progress list. A Mark as bar covers the controls strip with Read, Exploration, In Review, On hold, Done and Archive task; the Unread and Recent groups have dashed outlines where the card can drop, Needs attention is faded, and the card's own row is dimmed in place.">
  </a>
  <figcaption style="text-align:center; color:#888">Dragging a task in the List grouped by Inbox, with the Mark as bar.</figcaption>
</figure>

The control's tooltip says whether the stage *Updates as you work* or was *Set manually*.

**How a manual stage meets the evidence.** A stage you set doesn't fight git; it waits for it.

- Set a stage *ahead* of the evidence (**Done** before the merge, **In Review** before the pull request), and it holds until the evidence reaches it.
- Set a stage *behind* the evidence (**Reopen**, or a review sent back to **In Development**), and it holds until the evidence changes at all, so a reopened task still follows its next pull request.
- Once the evidence has caught up or moved on, the task goes back to following it. Pick **Automatic** to hand it back sooner. Dropping a card on the column the evidence already shows does the same thing.

**Reopen** on a task you marked Done falls back to what git and the pull requests show. On a task the evidence finished, it sets **In Development**, and the task's next pull request carries it forward again.

**On hold** parks a task without saying anything about how far it got. It reads **On hold** where the stage would be, with a tooltip saying who held it and where it stood before. Picking any stage or **Automatic** lifts the hold, and so does the task reaching **Done**, so a merged pull request ends it on its own. A task already at Done can't be put on hold.

Dropping a card on **Archived** opens the archive confirmation, and dragging an archived card out restores it first. An archived task's control reads **Archived** as a plain label, with no menu.

Agents can set the stage too, and put a task on hold, through Kepler's workspace tools. An agent that lifts a hold you placed tells you so.

***

## Filter

The **Filter** menu holds one flyout per facet.

<figure style="text-align:center">
  <a href="/wp-content/uploads/filter-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/filter-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The dashboard's Filter menu, its chip reading In Development and the search box showing 3 hidden. Progress is open on In Development (ticked, 2), On hold, In Review and Exploration, with Exploration's exclude button hovered and its tooltip reading Exclude Exploration with Shift+Enter.">
  </a>
  <figcaption style="text-align:center; color:#888">The Filter menu, with a facet's flyout open.</figcaption>
</figure>
<figure style="text-align:center">
  <a href="/wp-content/uploads/filter-todo-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/filter-todo-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Filter menu on Todo, with Type, Status, Needs my attention, Priority, Age, Your role and Provider, then a GitHub section with Repository, Assignee and Label, each set to Any. The Provider flyout lists GitHub with its count of 5, and Manage integrations.">
  </a>
  <figcaption style="text-align:center; color:#888">The Filter menu on Todo. Each connected provider gets its own section, here GitHub.</figcaption>
</figure>

Kepler hides facets with nothing to offer, so a single-repo setup won't show a Repository facet at all.

| Segment | Facets |
|---|---|
| **Todo** | Type · Linked work · Status · Needs my attention · Priority · Age · Your role · Provider, then one section per connected provider with its own Repository · Assignee · Issue type · Label · Project · Iteration or Sprint |
| **Tasks in progress** | Progress · Activity · Repository · Agent · Session · Linked work |

**Issue type**, **Label**, **Project**, and **Iteration** carry your provider's own vocabulary (a Jira issue type, your team's tags, a board name), not a Kepler-side translation of them. Azure DevOps calls the last one **Iteration** and Jira calls it **Sprint**, so the facet uses each tracker's word.

**Linked work** filters by whether an item is connected to work on the other side: *Has a task* in Todo, and *Has a PR or issue* in Tasks in progress. **Session** offers *Has a session* and *Has a live session*. To find the items *without* one, exclude the value.

**Include or exclude any value.** Click a value to include it. Hover a value and press its minus button (or **Shift+Enter** from the keyboard) to exclude it instead; an excluded value reads *not {value}*. On Todo, excluding a provider's value only subtracts from that provider's items, so excluding a GitHub label never hides a Jira issue.

**Included values within one facet combine as a union.** Ticking GitHub *and* GitLab under **Provider** shows items from either, not items that are somehow both. Excluded values subtract: an item that matches any of them is dropped. A facet with nothing chosen reads **Any** and narrows nothing. The **Search filters…** box finds a facet value without scrolling, and the menu reports **{count} of {total}** as you narrow. The **Filter** button names one chosen value and counts the rest, included in blue and excluded in red.

**Refresh** re-fetches the current segment from your providers.

***

## Search

The search box matches on **title, reference, or repository**: *Search title, ref, or repo…*.

<figure style="text-align:center">
  <a href="/wp-content/uploads/search-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/search-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The search box holding the query the, with a 1 of 5 search pill and a 2 hidden filter pill, each with its own clear button, beside Saved views, Group: Inbox, Sort: Updated and the Filter chip reading In Development.">
  </a>
  <figcaption style="text-align:center; color:#888">The search box, with its search and filter pills.</figcaption>
</figure>

Once a search or a filter is narrowing the list, pills at the right end of the search box say by how much, and each one clears only itself:

| Pill | What it counts | Clicking it |
|---|---|---|
| The search pill | The rows on screen out of every row: *{count} of {total}* | Clears the search |
| The filter pill | The rows your filters hide: *{count} hidden* | Clears the filters |

While a search is on, the filter pill counts only hidden rows that match the search, so a search that seems to miss something shows the filters hiding it. On Todo, which loads in pages, the counts read *40+* or *7+ hidden* until everything has arrived.

When nothing matches, the empty list reads **Nothing matches your search** (or **Nothing matches these filters** when only filters are narrowing it) and offers a button named for what it resets: **Clear search**, **Clear filters**, or **Clear search and filters**.

Search covers the work already loaded. On Todo, that's the work related to you on each connected integration, so a miss there adds *Todo only searches work related to you.* See [Todo, Tasks in progress, and the Agent Graph](/kepler/kepler-interface#todo-tasks-in-progress-and-the-agent-graph) for what each integration lists.

***

## Saved views

The **Saved views** chip, just after the search box, keeps a combination you use often under a name and takes you back to it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/saved-views-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/saved-views-oct-2026.png" class="help-center-img img-bordered" alt="The Saved views menu open from the chip reading View: Kanban - Progress. The view is checked under Tasks in progress, above Save current view, Update saved view, Discard changes, Rename view, and Delete view.">
  </a>
  <figcaption style="text-align:center; color:#888">The Saved views menu, with a view applied.</figcaption>
</figure>

A view captures:

- The segment
- The search text
- The grouping
- The filters
- The layout (**List** or **Board**)

Picking a view restores all of it, including switching to its segment. The chip then reads **View:** and the view's name, and a checkmark marks it in the menu. Open preview panels aren't part of a view, so applying one never reopens a task or pull request that has since gone.

| Menu item | What it does |
|---|---|
| **Save current view…** | Names the current combination and saves it as a new view |
| **Update saved view** | Overwrites the applied view with your edits. Available only once you've changed something |
| **Discard changes** | Puts the applied view back the way it was saved |
| **Rename view…** | Renames the applied view |
| **Delete view…** | Removes the applied view, after a confirmation |

A dot on the chip means you've edited the applied view since you picked it. Views are shared by every window, and two views can't share a name: Kepler adds a number to a duplicate.

***

## What Kepler remembers

Each segment remembers its own search, grouping, sort, filters, and layout, since they differ enough that sharing them would be meaningless. Kepler restores the segment you left along with its view. Kepler also remembers which panels were open, but only for the length of a run, so a round trip to the other segment doesn't cost you the panel you were reading. Panel widths are remembered per window across reloads and restarts; the set of open panels is not, so a relaunch never opens a panel for a task since deleted.

Saved views are the exception to per-segment memory: they're stored, named, and shared across windows until you delete them.

***

## Archive, restore, and clean up in bulk

**Archive task** files a task away. It leaves the live buckets for **Archived**, its rows and sessions survive, and Kepler stops only the agents whose checkout is about to disappear.

<figure style="text-align:center">
  <a href="/wp-content/uploads/archive-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/archive-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Task actions menu open from a task row's ⋮ button: Open task page; Progress, In Development; Mark as read, Rename task, Copy task link, Copy task prompt, Add resource… and Refresh; Shut down all agents; then Archive task and Delete task.">
  </a>
  <figcaption style="text-align:center; color:#888">Archive task, in the row's ⋮ menu.</figcaption>
</figure>

When a task is settled at **Done**, none of its worktrees holds unpushed work, and no agent is working or waiting on you, the preview and task page headers suggest it: *Ready to archive?* with **Archive** beside it. **Archive** opens the usual confirmation; the **X** dismisses the suggestion for that task in every window.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ready-to-archive-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ready-to-archive-oct-2026.png" class="help-center-img img-bordered" alt="A Done task's preview header with the Ready to archive? suggestion below it, offering Archive and an X to dismiss. The task's worktree pill reads No changes, and its pull request #33 is merged.">
  </a>
  <figcaption style="text-align:center; color:#888">The Ready to archive? suggestion on a Done task.</figcaption>
</figure>

The confirmation offers the same cascades the delete does: **Also delete worktrees**, **Also delete branches** (once worktrees is ticked), and **Also delete the branch on the remote** (once branches is ticked). This way, finishing with a task doesn't have to mean deleting it to clean it off the disk. With **Also delete worktrees** ticked, the dialog lists each worktree, riskiest first, with what will happen to it (*Merged into main*, *2 uncommitted files*, *In open PR #42*). It also names the ones it keeps: the repository's main worktree, and worktrees another task still uses. A worktree that would lose work is kept unless you tick the extra box that names exactly what would be lost, and a row at risk can open its changes so you can judge first.

With **Also delete the branch on the remote** ticked, Kepler deletes each branch's remote copy after the local branch goes, unless a check says to keep it. A branch with no upstream, or a default branch, is kept without comment. Otherwise a *Kept a branch on the remote* toast says why, for example *it has an open pull request*, *it has commits that are not on the remote*, *the remote has commits this branch does not*, or *the remote branch changed after it was checked*.

Archiving outranks everything else, so a task you filed away can't climb back into a live section because a shell is still open on it.

**Restore task** takes the place of **Archive task** in an archived task's **⋮** menu, and is on the task page's own header too. It puts the task straight back. Only one active task can hold a given pull request, so if restoring would archive another task that holds the same one, Kepler names that task and asks first.

For more than one at a time, every section header on **Tasks in progress** carries a quiet **Select**. Press it, and that corner of the header becomes a bar: a select-all box, **{count} selected**, and the batch verbs as icon buttons, each named by its tooltip. The section's rows also grow checkboxes. One section selects at a time, and while you're selecting, a click ticks a row rather than opening its panel. A task that Kepler is still preparing has no checkbox, and select-all skips it.

| Button | What it does |
|---|---|
| **Archive** | Archives every selected task that isn't already archived |
| **Restore** | Takes Archive's place when everything selected is already archived |
| **Delete** | Removes the selected tasks for good |
| **Cancel** | Leaves selection mode and drops the set |

Both **Archive** and **Delete** confirm, with **Archive tasks** or **Delete tasks** as the confirm button, and both offer **Also delete worktrees**, **Also delete branches**, and **Also delete the branch on the remote**. Deleting can't be undone, and the confirmation says so. The single-task dialog remembers what you ticked last time; the batch confirmation always starts with all three unticked. The batch confirmation doesn't list each worktree's fate. Instead, any worktree that would lose work is kept, and a toast afterwards says which ones and why. Open a task's own **⋮** to see the list before you confirm.

To clean up worktrees and local branches rather than tasks, open **Manage worktrees and branches** in **Settings → Repositories**. The **Worktrees and branches** page lists every worktree and every local branch no worktree holds, filtered by **Safe to delete**, **Needs update**, **Conflicts**, **Stale**, or **All**. From it you can **Update** many worktrees at once, bringing each branch up to date with its base, and delete worktrees and branches, including their copies on the remote. See [Settings](/kepler/settings-repositories#worktrees-and-branches).

---
