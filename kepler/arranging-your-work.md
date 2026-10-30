---
title: Arranging Your Work
description: Choose a layout for the task list, group, sort and filter it, put tasks in your own groups, save a combination as a named view, set a task's progress, and archive tasks in bulk.
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
tags: [arrangements, inbox, list, columns, grouping, task-groups, multi-select, sorting, filters, search, saved-views, progress, on-hold, archive, cleanup]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Arrange the lists on the dashboard so they show the work you need to see. Use these controls in the toolbar above the list:

- **Group** divides the list into sections.
- **Sort** orders the tasks inside each section.
- **Filter** hides what you do not need.
- **View** shows the list as a **List** or a **Board**.

Each segment remembers its own settings. To come back to a combination later, save it as a named view. To learn what each part of the screen is, see [The Kepler Interface](/kepler/kepler-interface).

<figure style="text-align:center">
  <a href="/wp-content/uploads/arrange-work-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/arrange-work-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The dashboard's arranging controls: the Saved views chip, Group: Inbox, Sort: Updated, Filter, Panel layout, the List and Board view switch, and Refresh.">
  </a>
  <figcaption style="text-align:center; color:#888">The saved views, grouping, sort, filter, panel, and layout controls.</figcaption>
</figure>

The toolbar has these other controls:

- **Panel layout** arranges open panels side by side (**Columns**) or in a **Grid**. See [Open a panel](/kepler/kepler-interface#open-a-panel).
- **Saved views** and the search box. See [Saved views](#saved-views) and [Search](#search).

To open several tasks at once, use the open button on a section header, or **Open group** on one of [your groups](#your-groups). The toolbar has no button that opens every row in the list. **Group** and **Sort** open as menus that grow to fit the window, so a long list of groupings is never cut off.

If the window is too narrow for the whole toolbar, **Group**, **Sort**, **Filter**, the layout switch and **Panel layout** move into a single **Options** button. If the window is narrower still, the saved views move into it next, and then the search box. A count on **Options** shows how many searches and filters are narrowing the list, so you can see that the list is narrowed while the menu is closed.

***

## Two layouts

<figure style="text-align:center">
  <a href="/wp-content/uploads/view-options-sep-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/view-options-sep-2026-v2@2x.png" class="help-center-img img-bordered" alt="The layout switch on the dashboard: List, selected, and Board.">
  </a>
  <figcaption style="text-align:center; color:#888">The View control's layout options.</figcaption>
</figure>

The **View** control sets how Kepler shows the list:

| View | What you get | Use it to |
|---|---|---|
| **List** | A compact list you read from top to bottom | Scan everything at once |
| **Board** | One column per section of the list | See how far along tasks are, and move tasks between stages |

**List** is the default. Each segment remembers its own choice across restarts, so Todo can show a list while Tasks in progress shows a board. Both layouts use the current grouping and filters.

**Board** shows the sections of the *current* grouping as columns side by side, so the **Group** control sets what the columns are. When you group by **Progress**, the columns are the stages: **Exploration**, **In Development**, **In Review**, and **Done**. These columns stay in place as tasks move between them, and an empty column reads **Nothing here**. **On hold** and **Archived** are exceptions: each appears when it holds a task, and both appear while you drag a card so you can drop the card on them. On every other grouping, Kepler hides empty sections, except your own groups, which stay so you can drop tasks into them.

When **Your groups** is on and another grouping is chosen, the **Board** becomes a grid. Each group is a row (a lane), and the grouping's sections are columns across every lane. See [Your groups](#your-groups).

All columns on the board have the same width. To resize them, use one of these methods:

- Drag the gap after any column. All columns resize at once.
- Focus the gap and press the arrow keys. **Home** sets the narrowest width and **End** the widest.
- Double-click the gap to return to the default width.

Each segment remembers its own column width. When a column has more tasks to load, **Load more** appears at the bottom of the column. From the keyboard, **←** and **→** move to the nearest column that has a card.

<div class="note" markdown="1">

**Columns** now names a panel layout, not this view. The board used to be called **Columns**. Now **Columns** and **Grid** in the **Panel layout** control set how open panels are arranged.

</div>

<figure style="text-align:center">
  <a href="/wp-content/uploads/columns-progress-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/columns-progress-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Tasks in progress list on the Board layout, grouped by Progress: the Exploration, In Development, In Review, On hold and Done columns side by side, each with its count, Open in panels and Select. Each task is a card with its title, age, session and progress glyphs, its waiting state (New reply, or Approval needed for Run npm test), and, for a task with a worktree, its repository and branch; Done reads Nothing here. The toolbar above shows Group: Progress and Board selected.">
  </a>
  <figcaption style="text-align:center; color:#888">The Board layout, grouped by Progress.</figcaption>
</figure>

On the board grouped by **Progress**, you can also move a task to another stage by hand. See [Set a task's progress](#set-a-tasks-progress).

<div class="note" markdown="1">

**The Agent Graph is a segment, not a layout.** It is next to **Todo** and **Tasks in progress**, and it replaces the list instead of arranging it. When you select it, **Group** and **View** are hidden and the toolbar shows the graph's own controls. See [The Agent Graph](/kepler/agent-graph).

</div>

***

## Group

The **Group** menu divides the list into sections.

<figure style="text-align:center">
  <a href="/wp-content/uploads/group-options-tasks-sep-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/group-options-tasks-sep-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Group menu open under Group: Your groups on Tasks in progress: the Your groups switch, on, with &quot;Shows a section per group&quot; under it, then Inbox, Progress, Activity, Repository and None, with None checked.">
  </a>
  <figcaption style="text-align:center; color:#888">The Group dropdown on Tasks in progress.</figcaption>
</figure>

Each segment has its own groupings:

| Segment | Group by | Default |
|---|---|---|
| **Todo** | Type, Needs my attention, Priority, Age, Your role, Assignee, Provider, Repository, Status, None | Type |
| **Tasks in progress** | Inbox, Progress, Activity, Repository, None, and the **Your groups** switch above them | Inbox |

On **Tasks in progress**, the **Your groups** switch at the top of the menu divides the list by groups you make yourself, either alone or with another grouping inside each group. See [Your groups](#your-groups).

### Inbox

**Inbox** is the default on Tasks in progress. It groups tasks by what each task needs from *you*, not by how far the work has progressed. Sections that need you come first, and the sections for work you have put away come last:

| Section | What it holds |
|---|---|
| **Unread** | A session finished a turn you have not looked at |
| **Needs attention** | A session is blocked on a permission request or a question, a Kepler approval request is waiting for an answer, or a program in one of the task's terminals is waiting on you |
| **Running** | An agent is working on it |
| **Recent** | Moved in the last 24 hours |
| **Earlier** | Moved before that |
| **On hold** | You or an agent put it on hold. Starts folded |
| **Done** | Finished, waiting only on the decision to archive it |
| **Archived** | Tasks you archived. This section takes priority over all the others |

A session stays marked **unseen** until you look at it, so a turn that finished while you were away is not marked as read without you.

**Inbox** lists every task exactly once:

- A task that is both unread *and* blocked on you appears under **Needs attention**, because a blocked task needs you more than output you have not read.
- A task under **Running** appears only there, not also in a time section.
- A task under **Done** appears only there, instead of in the time section it would otherwise get.

**Drop a card on an Inbox section.** To act on a task, drag its card onto another Inbox section:

| Drop on | What happens |
|---|---|
| **Unread** | Marks the task unread. Refused when it has no sessions, is archived, or is already waiting on you |
| **Recent** or **Earlier** | Marks an unread task read |
| **On hold** | Puts the task on hold. Refused when it is already done |
| **Done** | Marks the task done. Refused while an agent is still working |
| **Archived** | Opens the archive confirmation |
| **Needs attention** or **Running** | Refused: these clear when you respond, or show while an agent works |

To see what a drag looks like, see [Set a task's progress](#set-a-tasks-progress).

A task stays in **Running** for 10 seconds after its work stops, so it does not leave the section between one prompt and the next. Running tasks keep the order they started in, instead of changing places as they work. Moves into **Unread** and **Needs attention** happen at once, because they mean something changed.

**On hold** is for tasks you do not want to work on now, so a held task stays there even while an agent works on it. A held task still moves up when something needs you: an unread turn or a blocked prompt lists it under **Unread** or **Needs attention**.

The 24-hour window for **Recent** is fixed, not a setting, because the Inbox grouping is meant for a quick daily review.

### The other groupings

**Progress** and **Activity** group the same tasks in 2 different ways:

- **Progress** shows how far the work has progressed: **Exploration**, **In Development**, **In Review**, **On hold**, **Done**, **Archived**. Group by Progress to see where each task is in your workflow.
- **Activity** shows what the task's agent sessions are doing now, using the sessions' own states: **Waiting**, **Running**, **Ready**, **Spawning**, **Unread**, **Idle**, **Error**, and **Ended**. Grouping by Activity also adds **No sessions** for a task with no sessions started, then **Done**, and **Archived** last. Group by Activity to see what needs a person.

**Repository** is the only grouping that can list a task twice. A task bound to worktrees in several repositories appears under each repository, because this grouping shows what is happening in each repository separately.

Tasks in progress has no Status grouping, because a task's status is its progress stage, which **Progress** already shows.

On Todo, **Needs my attention** groups each item by what it needs from you now, most urgent first:

- **Ready to merge**
- **Changes requested**
- **Cannot merge yet**
- **Needs my review**
- **Re-review**
- **Approved, comments open**
- **Comments**
- **Assigned to me**
- **Filed by me, unassigned**
- **No action needed**, last, so it never pushes items that need you further down the list

Each section header has a **?** button (**About {label}**) that explains what the section holds. For example, **Ready to merge** is *Yours, approved, no open feedback and no blockers the provider can see. It only needs merging.* **Needs my attention** is a grouping rather than a pinned section, so it follows the same rules as every other grouping: one section per state, collapsible headers, and no row shown twice.

On Todo, **Priority** reads an item's priority from its labels: names such as *P0* to *P4*, a *priority:* prefix, or a bare *blocker*, *critical*, *urgent*, *highest*, or *lowest*. When an item has several, the most urgent label counts. The sections are **Urgent**, **High**, **Medium**, **Low**, and **Unprioritised**, and every pull request goes under **Not applicable**. Kepler does not read a tracker's own priority field, so an issue with no priority label is **Unprioritised**.

**Age** groups by when an item was created: **Today**, **This week**, **This month**, **Older**, and **No date**. **Assignee** groups by who an item is assigned to on each provider, with **Unassigned** for the rest.

On Todo, **Status** groups issues by their tracker's own workflow state, such as a Linear *In Progress* or a Jira *To Verify*, instead of putting every open issue in one section.

Items with no repository or provider go under **No repository** and **No provider**. A pull request whose provider did not report its author goes under **Unattributed**. An issue goes under **Not applicable**, because issues have no author or reviewer role to group by.

### Your groups

The other groupings arrange tasks by what Kepler can see. A group is one you make yourself: a name and a color you give to tasks that belong together, such as the tasks for one feature or one release. A task can be in 1 group at a time, and groups are available only in the **Tasks in progress** segment.

**Create a group.** The **New group** form asks for a **Group name** and a **Color**. The 8 colors are **Gray**, **Blue**, **Pink**, **Yellow**, **Green**, **Purple**, **Cyan**, and **Orange**. The form starts on the color your groups use least, so a new group looks different from your other groups unless you choose otherwise. Choose **Create group** to save the group. These rules apply:

- A group needs a name (*Give the group a name*).
- Each active group needs its own name, regardless of capitalization (*A group with this name already exists*). You can reuse an archived group's name.
- What you type stays in the form if you press **Escape** or click away, until you close the window. Only **Cancel** or saving clears it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-group-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-group-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The New group form: Search typed in the Group name field, the Color row of eight swatches with purple chosen, and the Cancel and Create group buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">The New group form.</figcaption>
</figure>

**Put tasks in a group.** You can add tasks to a group in 4 ways:

- **From a task's menu.** A task's **⋮** and right-click menus, on the dashboard and on the task page, have **Add to group**. Its submenu lists your groups with their colors, with the task's current group checked. Below them, **New group…** opens the form with this task already in it, and **Remove from group** appears for a task that has a group. A task with sub-tasks also offers **Group with its {count} sub-tasks**, which opens the form with the task's name and with the task and its sub-tasks in it.
- **By dragging one task onto another.** Hold a dragged task over another task for half a second, and a pill appears on the task underneath: **Create group** when that task has no group, or **Add to {group}** in its group's color. Drop the task on the pill. **Create group** opens the form with both tasks in it and the other task's title as the name. The pill needs a pointer. From the keyboard, use the menu.
- **From a selection.** Right-click inside a selection of 2 or more tasks and choose **New group with {count} tasks…**, **Add {count} tasks to group**, or **Remove {count} tasks from group**. See [Act on several tasks at once](#act-on-several-tasks-at-once).
- **By dropping into a group's section.** With the list grouped by your groups, drag a task into another group's section to move it there, or onto **Ungrouped** to remove it from its group.

To add an archived task to a group, restore the task first.

<figure style="text-align:center">
  <a href="/wp-content/uploads/add-to-group-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/add-to-group-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Task actions menu of Fix the cart total with Add to group open: its submenu lists Checkout, with a blue swatch and checked, and Payments, with a green swatch, then New group… and Remove from group. In the list behind, Fix the cart total and Update checkout copy carry a blue bar for Checkout and Upgrade the payment SDK a green bar for Payments.">
  </a>
  <figcaption style="text-align:center; color:#888">Add to group, in a task's menu.</figcaption>
</figure>

**See a task's group.** Under any grouping, a task in a group shows its group's color: a bar on the left edge of a **List** row, or a chip with the group's name after a **Board** card's title. Hover over the bar or chip to see the group's name and a summary (*3 tasks: 1 needs you, 2 unread*). Click it to open the group's menu without opening the task:

| Item | What it does |
|---|---|
| **Open group** | Opens every active task in the group in panels. Offered when the group has more than 1 |
| **Show only this group** | Sets the **Group** filter to this group |
| **Group by your groups** | Turns on the **Your groups** switch, keeping the current grouping inside each group |
| **Remove from group** | Takes this task out of the group |
| **Edit group…**, **Archive group**, **Delete group…** | Act on the group itself, as from its header (below) |

**Group the list by your groups.** Turn on the **Your groups** switch in the **Group** menu. The line under the switch describes the result:

- **With None chosen** (*Shows a section per group*), each group is a section, in your own order whatever the sort, followed by **Ungrouped** for tasks without a group. Each group's archived tasks are in an **Archived** section just after the group, folded at first. A group with no tasks still has its section, so you can drop tasks into it.
- **With another grouping chosen** (*Shows {axis} within each group*), the control reads, for example, **Your groups › Inbox**, and each group has its own **Inbox** sections, which you can fold separately. On the **Board**, each group becomes a lane, and the grouping's sections become columns across every lane.

Until you have a group, the switch says *Drag a task onto another to group them*.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-groups-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-groups-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Tasks in progress grouped by your groups: the Checkout section, marked blue, holds Fix the cart total and Update checkout copy; the Payments section, marked green, holds Upgrade the payment SDK; and the Ungrouped section holds Add product search and Write the 2.4 release notes. Each group's header shows its color, name, task count and its tasks' session dots, with Open in panels, Select and a ⋮ menu at its end.">
  </a>
  <figcaption style="text-align:center; color:#888">Tasks in progress, grouped by your groups.</figcaption>
</figure>

**A group's header.** Each group's header shows the group's color and name, then its count of active tasks and a dot for each state its tasks' sessions are in. A folded group therefore still shows whether something in it needs you. **Select** on a group header selects every task in the group. As the header gets narrower, it hides the session dots first, then shortens **Select** to an icon, so the name stays readable.

To open the group's menu, right-click the header or click its **⋮**. The menu acts on the group, never on its tasks:

| Item | What it does |
|---|---|
| **Edit group…** | Renames the group or changes its color, in the same form |
| **Change group color** | Picks one of the 8 colors directly |
| **Move group up**, **Move group down** | Moves the group one place in your order |
| **Archive group** | Archives the group. Offered only when every task in it is archived |
| **Delete group…** | Removes the group after a confirmation, *Its {count} tasks stay, ungrouped.* |

You can also drag a group's header to move the group before or after another group. **Ungrouped**, and the sections inside a group, cannot be moved.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-group-menu-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-group-menu-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Tasks in progress grouped by your groups, with the menu of the Search group's header open from its ⋮ button: Edit group…, Change group color, Move group up, Move group down and Delete group…. Below the yellow Search header with Add product search come the green Payments section with Upgrade the payment SDK and the Ungrouped section with Write the 2.4 release notes.">
  </a>
  <figcaption style="text-align:center; color:#888">A group header's menu.</figcaption>
</figure>

**Archive or delete a group.** When a group's work is done and every task in it is archived, archive the group. The group disappears from every view, and you can reuse its name. If you restore one of its tasks, the group comes back too, and the task stays in it. Deleting a group never deletes its tasks. They stay where they are, without a group.

Agents can put tasks into groups too, through Kepler's workspace tools. See [What an agent can do with a task's resources](/kepler/tasks-and-resources#what-an-agent-can-do-with-a-tasks-resources).

### Fold a section

To fold or unfold a section, click its header. The header shows the section's count beside its name.

<figure style="text-align:center">
  <a href="/wp-content/uploads/group-folds-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/group-folds-sep-2026.png" class="help-center-img img-bordered" alt="A group header showing a fold toggle and the section's count">
  </a>
  <figcaption style="text-align:center; color:#888">A group header, with its fold toggle and count.</figcaption>
</figure>

A folded section does not draw its rows, so a long **Done** list does not slow Kepler down. On the **Board** layout, a folded column shrinks to a narrow strip with its name and count, and is marked when it holds the open item. Click the strip to expand the column.

Some sections start folded:

- **Archived**, when you group by Activity or Inbox, because it holds work you have put away.
- **On hold**, in the Inbox grouping.

Under **Your groups**, folding a group hides the sections inside it, and you can fold each of those sections separately too.

Kepler remembers folds across restarts, for each segment and grouping. A section you folded stays folded, and a section you unfolded, such as **Archived**, stays open.

***

## Sort

The **Sort** control orders the items inside each section. It does not change the order of the sections, with 2 exceptions:

- **Repository** sections follow the sort, and each section's place depends on its first task.
- Your own groups always keep the order you gave them.

Each segment has its own sort options:

| Segment | Sort by | Default |
|---|---|---|
| **Todo** | Updated, Created, Name, ID, Type | Updated |
| **Tasks in progress** | Updated, Created, Name, Manual | Updated |

Dates sort newest first. **Name** and **ID** sort in ascending order. **ID** compares numbers by value, so *#9* comes before *#10*. **Type** puts pull requests before issues, with the most recent first within each. Each segment remembers its own sort.

### Put tasks in your own order

**Manual** sorts **Tasks in progress** in an order you set yourself, inside each section, in any grouping, on **List** or **Board**. To move a task, use one of these methods:

- Drag its row or card to a place in its own section. A line with a dot shows where it will land. Under **Manual**, a row shows a drag grip when you hover over it.
- Choose **Move up**, **Move down**, or **Move to top of {section}** from the task's **⋮** or right-click menu. These items appear only while the list is sorted by **Manual**.
- Drag one task of a selection to move all the selected tasks together. They land as one block, in the order they were listed. See [Act on several tasks at once](#act-on-several-tasks-at-once).

<figure style="text-align:center">
  <a href="/wp-content/uploads/manual-sort-drag-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/manual-sort-drag-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Upgrade the payment SDK being dragged to the top of the Unread group: a green line with a dot sits above Fix the cart total where it will land, the lifted row floats beside it, its own row is dimmed in place, and the Mark as bar covers the toolbar with Read, Exploration, In Development, On hold, Done and Archive task.">
  </a>
  <figcaption style="text-align:center; color:#888">Dragging a task to a new place in its section.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/manual-sort-menu-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/manual-sort-menu-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Task actions menu of Update checkout copy, an on-hold task with a New reply and a drag handle, including the move rows the Manual sort adds: Open task page; Progress, On hold; Mark as read and Rename task; Move up, Move down and Move to top of Unread; then Add to group, Copy task link, Copy task prompt, Add resource…, Refresh, Shut down all agents, Archive task and Delete task.">
  </a>
  <figcaption style="text-align:center; color:#888">The move rows in a task's menu, under the Manual sort.</figcaption>
</figure>

You do not have to switch to **Manual** first. If you drop a task in a new place in its own section while the list is sorted another way, Kepler saves the order you see, including your move, as the **Manual** order, and switches the sort to **Manual**. If you switch to **Manual** yourself, Kepler also keeps the current order, so no task changes place.

If you already have a saved **Manual** order, a drop under another sort would replace it. Kepler asks first, in a popover beside the dropped task: *Replace your Manual order?* To keep the move, choose **Switch and replace Manual**. To put the task back, choose **Cancel**, press **Escape**, or click away.

<figure style="text-align:center">
  <a href="/wp-content/uploads/manual-sort-replace-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/manual-sort-replace-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Tasks in progress after Upgrade the payment SDK was dropped at the top of Unread while sorted by Updated: the toolbar already reads Sort: Manual, the dropped row shows its drag grip, and a popover beside it asks Replace your Manual order? Keeping this move switches the sort to Manual and saves the list in the order you see now, with Cancel and Switch and replace Manual.">
  </a>
  <figcaption style="text-align:center; color:#888">Kepler asks before a drop replaces your saved Manual order.</figcaption>
</figure>

If a move fails, Kepler shows *Unable to move the task*, and restores the previous sort if the move had changed it.

***

## Set a task's progress

Kepler normally sets a task's progress stage from its Git branches and pull requests (see [Status](/kepler/kepler-interface)). Sometimes Git and the pull requests do not show what you know. For example, a review was sent back, or the work was merged somewhere Kepler cannot see. In those cases, set the stage yourself.

<figure style="text-align:center">
  <a href="/wp-content/uploads/progress-menu-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/progress-menu-oct-2026.png" class="help-center-img img-bordered" alt="The Progress menu open from a task's In Review control, with Automatic checked, then Exploration, In Development, In Review, On hold, and Done.">
  </a>
  <figcaption style="text-align:center; color:#888">The Progress menu.</figcaption>
</figure>

You can set the stage in these ways:

- **The progress control.** Click the stage name on a task row, in the preview header, or in the task page header to open the **Progress** menu: **Automatic** (*Updates as you work*), then **Exploration**, **In Development**, **In Review**, **On hold**, and **Done**. When there is no room for the stage name, the control shows only the stage's icon.
- **The task menus.** A task's **⋮** and right-click menus have the same choices under a **Progress** submenu, plus **Reopen** while the task is Done. Each item's hint says where the task will go (*Moves it to In Review*).
- **Drag a card.** In any grouping, on **List** or **Board**, drag a task's card or row. When grouped by **Progress**, drop it on another stage. On a touch screen, press and hold the card to pick it up. Press **Escape** to cancel the drag. If you drop the card in its own section, Kepler reorders it (see [Put tasks in your own order](#put-tasks-in-your-own-order)). You cannot drag a task that Kepler is still preparing. If you hold the card over another task, Kepler offers to group the 2 tasks (see [Your groups](#your-groups)). If you drag a task that is part of a selection, you drag the whole selection.
- **The Mark as bar.** While you drag, a **Mark as** bar appears over the toolbar with chips for what the card can become: **Read** or **Unread**, the stages, **Reopen** for a Done task, and **Archive task**. For an archived task, it shows only **Restore**. Drop the card on a chip.
- **From the keyboard.** When a card has focus on the **Board** grouped by **Progress**, press **Cmd/Ctrl+Shift+←** or **Cmd/Ctrl+Shift+→** to move it 1 column. The card stops at **Exploration** and **Done**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/progress-drag-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/progress-drag-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Board grouped by Progress while Write the 2.4 release notes is dragged from Exploration into In Review: its card stays dimmed in Exploration, the lifted card hangs below Upgrade the payment SDK, In Review is filled and outlined as the drop target, the other columns (including Done and Archived, each reading Nothing here) have dashed outlines, and a Mark as bar over the toolbar offers In Development, In Review, On hold, Done and Archive task.">
  </a>
  <figcaption style="text-align:center; color:#888">Dragging a card to another stage, with the Mark as bar over the toolbar.</figcaption>
</figure>

While you drag, the card stays faded in its original place, and a line shows where it would land. Each section that accepts the card has a dashed outline, which becomes solid when the card is over it. Sections that do not accept the card fade, and say why when you hover over them. On the **Board**, a folded column opens after you hold the card over it for half a second.

<figure style="text-align:center">
  <a href="/wp-content/uploads/drag-drop-bar-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/drag-drop-bar-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Fix the cart total lifted off the Tasks in progress list. A Mark as bar covers the toolbar with Read, Exploration, In Review, On hold, Done and Archive task; the Unread and Recent groups have dashed outlines where the card can drop, Needs attention is faded, and the card's own row is dimmed in place.">
  </a>
  <figcaption style="text-align:center; color:#888">Dragging a task in the List grouped by Inbox, with the Mark as bar.</figcaption>
</figure>

The control's tooltip says whether the stage *Updates as you work* or was *Set manually*.

**How a stage you set works with Git.** Kepler keeps a stage you set until Git and the pull requests catch up with it or change. Then Kepler sets the stage from them again:

- If you set a stage *ahead* of Git and the pull requests (**Done** before the merge, or **In Review** before the pull request), the stage stays until they reach it.
- If you set a stage *behind* them (**Reopen**, or a review sent back to **In Development**), the stage stays until they change in any way. A reopened task therefore still follows its next pull request.
- To return the task to automatic stages sooner, choose **Automatic**, or drop its card on the column that Git and the pull requests already show.

**Reopen** on a task you marked Done returns it to the stage that Git and the pull requests show. If Git and the pull requests show the task as finished, **Reopen** sets **In Development**, and the task's next pull request moves it forward again.

**On hold** pauses a task without changing its stage. The task reads **On hold** where the stage would be, with a tooltip that says who put it on hold and what its stage was before. Choosing any stage or **Automatic** lifts the hold. The task reaching **Done** also lifts it, so a merged pull request ends the hold. You cannot put a task on hold when it is already at Done.

Dropping a card on **Archived** opens the archive confirmation. Dragging an archived card to another section restores the task first. An archived task's control reads **Archived** as a plain label, with no menu.

Agents can also set the stage, and put a task on hold, through Kepler's workspace tools. If an agent lifts a hold you placed, it tells you.

***

## Filter

The **Filter** menu has a submenu for each facet, such as **Progress** or **Provider**.

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

Kepler hides facets that have no values to choose from. For example, if you work in a single repository, the menu has no Repository facet. Each segment has these facets:

| Segment | Facets |
|---|---|
| **Todo** | Type · Linked work · Status · Needs my attention · Priority · Age · Your role · Provider, then one section per connected provider with its own Repository · Assignee · Issue type · Label · Project · Iteration or Sprint |
| **Tasks in progress** | Progress · Activity · Repository · Agent · Session · Linked work · Group |

**Issue type**, **Label**, **Project**, and **Iteration** use your provider's own values (a Jira issue type, your team's labels, a board name), not Kepler's own names for them. Azure DevOps calls the last one **Iteration** and Jira calls it **Sprint**, so the facet uses each tracker's word.

**Linked work** filters by whether an item is connected to work in the other segment:

- In Todo, it filters each pull request or issue by its task history: *Has an active task*, *Archived tasks only* (worked on before, but every task is archived), or *No tasks ever*.
- In Tasks in progress, it offers *Has a PR or issue*.

**Session** offers *Has a session* and *Has a live session*. To find tasks *without* a pull request, issue, or session, exclude the value.

**Group** lists each of [your groups](#your-groups), including empty ones, and **Ungrouped** for tasks without a group. If a filter still names a group that was deleted or archived, the facet shows it as **Removed group**. When the list is grouped by your groups, the facet also limits which group sections appear.

**Include or exclude any value.** Click a value to include it. To exclude a value instead, hover over it and click its minus button, or press **Shift+Enter** from the keyboard. An excluded value reads *not {value}*. On Todo, excluding a provider's value removes only that provider's items, so excluding a GitHub label never hides a Jira issue.

**Values you include in one facet are combined.** If you tick GitHub *and* GitLab under **Provider**, the list shows items from either provider. Excluded values remove items: Kepler hides an item that matches any of them. A facet with nothing chosen reads **Any** and does not narrow the list.

To find a facet value without scrolling, type in the **Search filters…** box. The menu shows **{count} of {total}** as you narrow the list. The **Filter** button names 1 chosen value and counts the rest, with included values in blue and excluded values in red.

To fetch the current segment from your providers again, click **Refresh**.

***

## Search

The search box finds items by **title, reference, or repository**. Its placeholder reads *Search title, ref, or repo…*.

<figure style="text-align:center">
  <a href="/wp-content/uploads/search-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/search-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The search box holding the query the, with a 1 of 5 search pill and a 2 hidden filter pill, each with its own clear button, beside Saved views, Group: Inbox, Sort: Updated and the Filter chip reading In Development.">
  </a>
  <figcaption style="text-align:center; color:#888">The search box, with its search and filter pills.</figcaption>
</figure>

When a search or a filter narrows the list, pills at the right end of the search box show how many rows are left or hidden. Each pill clears only its own search or filters:

| Pill | What it counts | Clicking it |
|---|---|---|
| The search pill | The rows on screen out of every row: *{count} of {total}* | Clears the search |
| The filter pill | The rows your filters hide: *{count} hidden* | Clears the filters |

While a search is on, the filter pill counts only hidden rows that match the search. If a search seems to miss something, the filter pill shows whether your filters are hiding it. Todo loads in pages, so its counts read *40+* or *7+ hidden* until everything has loaded.

When nothing matches, the empty list reads **Nothing matches your search**, or **Nothing matches these filters** when only filters narrow it. It offers a button named for what it resets: **Clear search**, **Clear filters**, or **Clear search and filters**.

Search covers only the work already loaded. On Todo, that is the work related to you on each connected integration, so when a search on Todo finds nothing, the list adds *Todo only searches work related to you.* To learn what each integration lists, see [Todo, Tasks in progress, and the Agent Graph](/kepler/kepler-interface#todo-tasks-in-progress-and-the-agent-graph).

***

## Saved views

To save a combination you use often, and return to it later, use the **Saved views** chip after the search box.

<figure style="text-align:center">
  <a href="/wp-content/uploads/saved-views-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/saved-views-oct-2026.png" class="help-center-img img-bordered" alt="The Saved views menu open from the chip reading View: Kanban - Progress. The view is checked under Tasks in progress, above Save current view, Update saved view, Discard changes, Rename view, and Delete view.">
  </a>
  <figcaption style="text-align:center; color:#888">The Saved views menu, with a view applied.</figcaption>
</figure>

A view captures:

- The segment
- The search text
- The grouping, including whether **Your groups** is on
- The filters
- The layout (**List** or **Board**)

When you choose a view, Kepler restores all of these settings and switches to the view's segment. The chip then reads **View:** and the view's name, and a checkmark marks the view in the menu. Open preview panels are not part of a view, so applying a view never reopens a task or pull request that no longer exists.

The menu has these items:

| Menu item | What it does |
|---|---|
| **Save current view…** | Names the current combination and saves it as a new view |
| **Update saved view** | Overwrites the applied view with your edits. Available only after you change something |
| **Discard changes** | Puts the applied view back the way it was saved |
| **Rename view…** | Renames the applied view |
| **Delete view…** | Removes the applied view, after a confirmation |

A dot on the chip means you edited the applied view after you chose it. Every window shares the same views. Each view needs its own name, so Kepler adds a number to a duplicate name.

***

## What Kepler remembers

Each segment remembers its own search, grouping, sort, filters, layout, and folded sections, because the segments list different kinds of work. Kepler also remembers:

- **The segment you left**, which it restores along with that segment's settings.
- **Which panels were open**, until you quit Kepler. If you switch to the other segment and back, the panel you were reading is still open.
- **Panel widths**, for each window, across reloads and restarts.

Kepler does not remember the set of open panels across restarts, so a relaunch never opens a panel for a task that was deleted.

Saved views work differently from these per-segment settings. Kepler stores them by name and shares them across windows until you delete them.

***

## Archive, restore, and clean up in bulk

**Archive task** puts a task away. The task moves from its current section to **Archived**, its rows and sessions are kept, and Kepler stops only the agents whose checkout is about to be deleted.

<figure style="text-align:center">
  <a href="/wp-content/uploads/archive-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/archive-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Task actions menu open from Fix the cart total's ⋮ button, beside the task list: Open task page; Progress, In Development; Mark as read, Rename task, Add to group, Copy task link, Copy task prompt, Add resource… and Refresh; Shut down all agents; then Archive task and Delete task.">
  </a>
  <figcaption style="text-align:center; color:#888">Archive task, in the row's ⋮ menu.</figcaption>
</figure>

When a task meets all of these conditions, the preview header and the task page header suggest archiving it, with *Ready to archive?* and an **Archive** button:

- The task is at **Done**.
- None of its worktrees has unpushed work.
- No agent is working or waiting on you.
- No session is running background work, such as a dev server.

**Archive** opens the usual confirmation. The **X** dismisses the suggestion for that task in every window.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ready-to-archive-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ready-to-archive-oct-2026.png" class="help-center-img img-bordered" alt="A Done task's header in the side panel, with the Ready to archive? suggestion below it, offering Archive and an X to dismiss. The task's worktree button reads No changes, and its pull request #33 is merged.">
  </a>
  <figcaption style="text-align:center; color:#888">The Ready to archive? suggestion on a Done task.</figcaption>
</figure>

The confirmation offers the same options as deleting a task: **Also delete worktrees**, **Also delete branches** (after you tick **Also delete worktrees**), and **Also delete the branch on the remote** (after you tick **Also delete branches**). You can therefore remove a finished task's worktrees and branches from disk without deleting the task. With **Also delete worktrees** ticked, the dialog lists each worktree, riskiest first, with what will happen to it (*Merged into main*, *2 uncommitted files*, *In open PR #42*). It also names the worktrees it keeps: the repository's main worktree, and worktrees that another task still uses. Kepler keeps a worktree that would lose work unless you tick the extra box that names exactly what would be lost. To check before you decide, open the changes from the row of a worktree at risk.

With **Also delete the branch on the remote** ticked, Kepler deletes each branch's remote copy after it deletes the local branch, unless a check says to keep it. Kepler keeps a branch with no upstream, or a default branch, without a message. For any other branch it keeps, a *Kept a branch on the remote* message says why, for example *it has an open pull request*, *it has commits that are not on the remote*, *the remote has commits this branch does not*, or *the remote branch changed after it was checked*.

**Archived** takes priority over every other section, so an archived task stays in **Archived** even if a shell is still open on it.

**Restore task** replaces **Archive task** in an archived task's **⋮** menu, and also appears in the task page's header. It restores the task at once, without asking, even when another active task holds the same pull request (several tasks can share one). A restored task stays in its group, and if that group was archived, Kepler restores the group too.

To archive, restore or delete several tasks at once, click **Select** on a section header in **Tasks in progress**. That part of the header becomes a bar with a select-all box, **{count} selected**, and icon buttons for the actions, each named in its tooltip. The section's rows show checkboxes. You can select in 1 section at a time, and while you select, clicking a row ticks it instead of opening its panel. A task that Kepler is still preparing has no checkbox, and select-all skips it.

The bar has these buttons:

| Button | What it does |
|---|---|
| **Archive** | Archives every selected task that is not already archived |
| **Restore** | Replaces **Archive** when every selected task is already archived |
| **Delete** | Deletes the selected tasks permanently |
| **Cancel** | Ends selection and clears the selection |

**Archive** and **Delete** both ask you to confirm, with **Archive tasks** or **Delete tasks** as the confirm button. Both offer **Also delete worktrees**, **Also delete branches**, and **Also delete the branch on the remote**. Deleting cannot be undone, and the confirmation says so. The batch confirmation differs from the single-task dialog in 2 ways:

- The single-task dialog remembers what you ticked last time. The batch confirmation always starts with all 3 boxes unticked.
- The batch confirmation does not list what will happen to each worktree. Instead, Kepler keeps any worktree that would lose work, and a message afterwards says which ones and why. To see the list before you confirm, use the task's own **⋮** menu.

### Act on several tasks at once

The tasks you open with **Shift**-click or **Cmd/Ctrl**-click (see [Open a panel](/kepler/kepler-interface#open-a-panel)) are also a selection you can act on. While 2 or more tasks are selected, right-clicking or dragging any one of them acts on all of them. Right-clicking or dragging a task outside the selection acts on that task only. A row's **⋮** always acts on its own row.

Right-clicking inside the selection opens a selection menu instead of the task menu. Each item shows how many tasks it acts on: **New group with {count} tasks…**, **Add {count} tasks to group**, **Remove {count} tasks from group**, **Archive {count} tasks**, **Restore {count} tasks**, and **Delete {count} tasks**. Kepler leaves out items with nothing to act on, and the group items skip archived tasks. While the menu is open, the rows it acts on are outlined. **Archive**, **Restore**, and **Delete** open the same batch confirmation as a section's **Select** bar.

Dragging a selected task drags the whole selection. Each drop target says how many of the tasks it accepts (*2 of 3 tasks*). After the drop, Kepler reports how many tasks moved and how many stayed where they were. Under the **Manual** sort, the tasks land together as one block.

To clean up worktrees and local branches instead of tasks, open **Settings → Repositories** and choose **Manage worktrees and branches**. The **Worktrees and branches** page lists every worktree, and every local branch that no worktree has checked out. You can filter the list by **Safe to delete**, **Needs update**, **Conflicts**, **Stale**, or **All**. On this page, you can:

- **Update** several worktrees at once, which brings each branch up to date with its base.
- Delete worktrees and branches, including their copies on the remote.

See [Settings](/kepler/settings-repositories#worktrees-and-branches).

---
