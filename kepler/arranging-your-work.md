---
title: Arranging Your Work
description: Add and arrange the Dashboard's views, choose a layout for each list, group, sort and filter it, put tasks in your own groups, set a task's progress or hold it until something happens, and archive tasks in bulk.
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
last_verified: 2026-11
llms_include: true
tags: [arrangements, views, inbox, list, columns, grouping, task-groups, multi-select, sorting, filters, search, progress, on-hold, later, archive, cleanup]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Arrange the Dashboard so it shows the work you need to see. The Dashboard is a set of views, such as **Todo** and **Tasks**, and each view keeps its own arrangement. Above a view's list, the toolbar has these controls:

- **View** opens a menu that sets the layout (**List**, **Board**, or **Graph**), the grouping, the sort, and the filters.
- The search box finds items in the list, and also takes filters. See [Search](#search).
- **Panel layout** arranges open panels side by side in 1 row, or in a grid of several rows. See [Lay panels out in a grid](/kepler/kepler-interface#lay-panels-out-in-a-grid).
- **Refresh** fetches the view's items from your providers again.

What you choose in the **View** menu is saved to the view at once. To learn what each part of the screen is, see [The Kepler Interface](/kepler/kepler-interface).

<figure style="text-align:center">
  <a href="/wp-content/uploads/arrange-work-oct-2026-v7@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/arrange-work-oct-2026-v7@2x.png" class="help-center-img img-bordered" alt="The Dashboard's arranging controls: the row of views (Todo and Tasks with Kepler's own Todo and Task icons, Tasks selected, Agent Graph, New view, and Automations at the right), and under it the list toggle, the View button showing the List glyph and Inbox, the search box reading Search, or filter like activity:waiting across the toolbar, then Panel layout (Auto × 1) and Refresh at the right. Tasks and Agent Graph carry the orange mark of a task waiting on you.">
  </a>
  <figcaption style="text-align:center; color:#888">The views, and the search, View, panel and refresh controls under them.</figcaption>
</figure>

To open several tasks at once, use the open button on a section header, or **Open group** on one of [your groups](#your-groups).

In a narrow window, the search box becomes a search icon. Click it, or press **Cmd/Ctrl+F**, to open the search box.

***

## Views

Each view lists one kind of work:

- A **Todo** view lists pull requests and issues from your connected providers.
- A **Tasks** view lists your tasks.

Kepler starts you with a **Todo** view, a **Tasks** view, and an **Agent Graph** view, which is a Tasks view in the **Graph** layout (see [Layouts](#layouts)). The views appear on every page. Click a view to open the Dashboard on it.

A view keeps its own layout, grouping, sort, filters, and search text, and every window shares the same views. See [What Kepler remembers](#what-kepler-remembers).

<figure style="text-align:center">
  <a href="/wp-content/uploads/saved-views-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/saved-views-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Tasks view's menu open from its tab in the Dashboard's row of views (Todo, Tasks, Agent Graph, New view), where Tasks and Agent Graph carry the orange mark of a task waiting on you: Rename with F2, Change icon showing Task, Show counts on views ticked, View options, Duplicate view highlighted, Move left, Move right, Views position, and Delete view.">
  </a>
  <figcaption style="text-align:center; color:#888">A view's menu.</figcaption>
</figure>

**A view's menu.** Click the view you are on, or right-click any view, to open its menu:

| Menu item | What it does |
|---|---|
| **Rename** (**F2**) | Renames the view. Double-clicking the name does the same |
| **Change icon** | Picks the view's icon |
| **Show counts on views** | Shows or hides task counts on every view |
| **View options** | Opens the **View** menu |
| **Duplicate view** | Adds a copy of the view with the same settings |
| **Move left**, **Move right** | Moves the view 1 place |
| **Views position** | Sets where the views sit |
| **Delete view** | Removes the view after a confirmation |

You cannot delete your last Todo view or your last Tasks view.

**Add a view.** Click **New view** after the views, then choose **Todo**, **Tasks**, **Agent Graph**, or **Duplicate current view**. Name the new view, set it up in the menu that opens, and choose **Done**.

**Reorder the views.** Drag a view to a new place, or use **Move left** and **Move right** in its menu. On the Dashboard, **Cmd/Ctrl+Shift+[** and **Cmd/Ctrl+Shift+]** show the previous or next view, and **Cmd+Option+[** and **Cmd+Option+]** (**Ctrl+Alt+[** and **Ctrl+Alt+]** on Windows and Linux) move the view you are on. See [Keyboard shortcuts](/kepler/settings-app#keyboard-shortcuts).

If the views run out of room, they fold into 1 button. Click it to see every view.

### Change a view's icon

To pick another icon for a view, open the view's menu and point to **Change icon**. Search for an icon or choose one from the grid. The first icon is the view type's default.

<figure style="text-align:center">
  <a href="/wp-content/uploads/dashboard-view-icon-picker-nov-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/dashboard-view-icon-picker-nov-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Tasks view's menu open from its tab, with Change icon, Task, highlighted and its picker open beside it: a Search icons field over a grid of icons, Kepler's Task icon first and outlined, and a footer reading Default, Task.">
  </a>
  <figcaption style="text-align:center; color:#888">The icon picker, from a view's Change icon row.</figcaption>
</figure>

### Where the views sit

By default, the views sit in a row below the title bar. To move them, choose **Views position** in any view's menu, then **Title bar**, **Below title bar**, or **Left side**. On the left side, **Settings** moves to the foot of the column.

Along the left side, the views start as icons. To show their names, click **Expand views** at the foot of the column, or drag the column's edge. **Collapse views** returns to icons.

<figure style="text-align:center">
  <a href="/wp-content/uploads/dashboard-views-side-rail-nov-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/dashboard-views-side-rail-nov-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Dashboard with its views along the left side, expanded to show names: Todo and Tasks with Kepler's own Todo and Task icons, Tasks selected, then Agent Graph and New view at the top, Settings and the Collapse views button at the foot. Tasks and Agent Graph carry the orange mark of a task waiting on you. The top bar keeps New task, Ask, Feedback and the account but no Settings button, and the Tasks list fills the rest of the window under its toolbar.">
  </a>
  <figcaption style="text-align:center; color:#888">The views along the left side of the window, with their names shown.</figcaption>
</figure>

**Settings → Appearance → Dashboard** has the same choices, and also **View style**: **Tabs** or **Pills**. See [Dashboard settings](/kepler/settings-app#dashboard).

### Status and counts on views

A Tasks view shows its agents' most urgent state as a mark on its icon, using the same levels as the [tray icon](/kepler/kepler-interface#the-tray-icon), such as **Needs your answer**. Only the tasks that the view's filters keep count.

A view with filters also shows how many tasks match them. To hide the counts, turn off **Show counts on views** in any view's menu.

Hover a view to see its state, its task count, and its filters.

<figure style="text-align:center">
  <a href="/wp-content/uploads/dashboard-view-status-badges-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/dashboard-view-status-badges-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Dashboard's row of views with the Tasks view filtered: its tab shows a count of 2 beside its name and an orange mark on its icon, and Agent Graph has the same mark. Hovering Tasks opens its card: Tasks, Needs your answer, 2 tasks, and its filter chip, Progress In Development.">
  </a>
  <figcaption style="text-align:center; color:#888">A filtered view's count and status mark, with its card.</figcaption>
</figure>

### Choose what a Todo view lists

A Todo view's **View** menu has a **Scope** switch:

- **Mine**, the default, lists work created by you, assigned to you, mentioning you, or awaiting your review.
- **All** lists everything open in Kepler's repos, plus your work elsewhere.

Under **All**, **Repos** and **Updated** choose which repositories and how recent the work is. See [The Dashboard's views](/kepler/kepler-interface#the-dashboards-views).

***

## Layouts

<figure style="text-align:center">
  <a href="/wp-content/uploads/view-options-sep-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/view-options-sep-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Dashboard toolbar with the View button, reading Inbox, beside the search box, and the top of its menu open below it: the layout switch with List selected, then Board and Graph, above the Your groups toggle, Group by (Inbox) and Sort by (Updated).">
  </a>
  <figcaption style="text-align:center; color:#888">The layout switch at the top of the View menu.</figcaption>
</figure>

The layout switch at the top of the **View** menu sets how Kepler shows the view:

| Layout | What you get | Use it to |
|---|---|---|
| **List** | A compact list you read from top to bottom | Scan everything at once |
| **Board** | One column per section of the list | See how far along tasks are, and move tasks between stages |
| **Graph** | The Agent Graph of the view's tasks. Tasks views only | See what every agent is doing. See [The Agent Graph](/kepler/agent-graph) |

**List** is the default. Each view remembers its own layout, so a Todo view can show a list while a Tasks view shows a board. **List** and **Board** both use the view's grouping and filters.

**Board** shows the sections of the *current* grouping as columns side by side, so **Group by** sets what the columns are. When you group by **Progress**, the columns are the stages, from **Exploration** to **Done**, and they stay in place even when empty.

When **Your groups** is on and another grouping is chosen, the **Board** becomes a grid. Each group is a row (a lane), and the grouping's sections are columns across every lane. See [Your groups](#your-groups).

All columns on the board have the same width. To resize them, use one of these methods:

- Drag the gap after any column. All columns resize at once.
- Focus the gap and press the arrow keys. **Home** sets the narrowest width and **End** the widest.
- Double-click the gap to return to the default width.

Each view remembers its own column width. When a column has more tasks to load, **Load more** appears at the bottom of the column. From the keyboard, **←** and **→** move to the nearest column that has a card.

<div class="note" markdown="1">

**Panel layout** arranges the panels you open, not the list. Its **Auto columns** are not the **Board** layout's columns.

</div>

<figure style="text-align:center">
  <a href="/wp-content/uploads/columns-progress-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/columns-progress-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Tasks view on the Board layout, grouped by Progress: the Exploration, In Development, In Review, On hold and Done columns side by side, each with its count, and Open in panels and Select on every column that has tasks. Each task is a card with its title, age, session and progress glyphs, its waiting state (New reply, or Approval needed for Run npm test), and, for a task with a worktree, its repository and branch; Done reads Nothing here. Above, the toolbar holds the View button showing the Board glyph and Progress, then the search box reading Search, or filter like activity:waiting.">
  </a>
  <figcaption style="text-align:center; color:#888">The Board layout, grouped by Progress.</figcaption>
</figure>

On the board grouped by **Progress**, you can also move a task to another stage by hand. See [Set a task's progress](#set-a-tasks-progress).

**Graph** replaces the list instead of arranging it. While it is chosen, the **View** menu shows the graph's own controls in place of **Group by** and **Sort by**. See [The Agent Graph](/kepler/agent-graph).

***

## Group

**Group by** in the **View** menu divides the list into sections.

<figure style="text-align:center">
  <a href="/wp-content/uploads/group-options-tasks-sep-2026-v5@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/group-options-tasks-sep-2026-v5@2x.png" class="help-center-img img-bordered" alt="The View menu open under the View button, which reads Your groups › Inbox: the List, Board and Graph switch, the Your groups switch on with Shows Inbox within each group under it, and Group by open on its submenu of Inbox (checked), Progress, Activity, Repository (highlighted) and None. Below come Sort by, Updated, and the Filters section: Progress, Activity, Repository, Agent, Session, Group and Linked work, each Any.">
  </a>
  <figcaption style="text-align:center; color:#888">Group by in the View menu of a Tasks view.</figcaption>
</figure>

Each type of view has its own groupings:

| View | Group by | Default |
|---|---|---|
| **Todo** | Type, Needs my attention, Priority, Age, Your role, Assignee, Provider, Repository, Milestone, Status, None | Type |
| **Tasks** | Inbox, Progress, Activity, Repository, None, and the **Your groups** switch above them | Inbox |

On a Tasks view, the **Your groups** switch above **Group by** divides the list by groups you make yourself, either alone or with another grouping inside each group. See [Your groups](#your-groups).

### Inbox

**Inbox** is the default on Tasks views. It groups tasks by what each task needs from *you*, not by how far the work has progressed. Sections that need you come first, and the sections for work you have put away come last:

| Section | What it holds |
|---|---|
| **Needs attention** | Something waits on you, such as a question, an approval request, a failed turn, failing CI, or a review that requests changes |
| **Unread** | A session finished a turn you have not looked at, or a hold lifted |
| **Running** | An agent is working on it |
| **Important** | A task you starred with **Star** in its menu |
| **Recent** | Moved in the last 24 hours |
| **On hold** | You or an agent put it on hold. Starts folded |
| **Earlier** | Moved more than 24 hours ago. Starts folded |
| **Done** | Finished, waiting only on the decision to archive it |
| **Not started** | No session has started in it yet. Starts folded |
| **Later** | You or an agent set it aside for later. Starts folded |
| **Archived** | Tasks you archived. Starts folded |

A finished turn stays unread until you look at it.

To step through the tasks that need you in Inbox order, use **Go to next task needing attention**, **Go to next unread task**, or **Go to next task needing attention or unread**. Run them from the palette's **Commands** tab, or give them a key in [Keyboard shortcuts](/kepler/settings-app#keyboard-shortcuts). They have no key by default.

**Inbox** lists every task exactly once:

- A task that is both unread *and* blocked on you appears under **Needs attention**.
- A task under **Running** or **Done** appears only there, not also in a time section.
- A starred task lists under **Important** unless it needs you, is unread, is held, is running, or is done.

**Drop a card on an Inbox section.** To act on a task, drag its card onto another Inbox section:

| Drop on | What happens |
|---|---|
| **Unread** | Marks the task unread |
| **Recent** or **Earlier** | Marks an unread task read |
| **Important** | Stars the task |
| **On hold** or **Later** | Puts the task on hold, or sets it aside for later |
| **Done** | Marks the task done. Refused while an agent is still working |
| **Archived** | Opens the archive confirmation |

A section that refuses the card fades, and says why when you hover over it. To see what a drag looks like, see [Set a task's progress](#set-a-tasks-progress).

**On hold** and **Later** are for tasks you do not want to work on now, so a held task stays there even while an agent works on it. A held task still moves up when something needs you: an unread turn or a blocked prompt lists it under **Unread** or **Needs attention**.

### The other groupings

**Progress** and **Activity** group the same tasks in 2 different ways:

- **Progress** shows how far the work has progressed: **Exploration**, **In Development**, **In Review**, **On hold**, **Later**, **Done**, **Archived**. Group by Progress to see where each task is in your workflow.
- **Activity** shows what the task's agent sessions are doing now, from **Waiting** and **Error** down to **Idle** and **Ended**. A task lists under its most urgent session's state, or under **No sessions**, **Done**, or **Archived**. Group by Activity to see what needs a person.

**Repository** is the only grouping that can list a task twice. A task with worktrees in several repositories appears under each repository.

Tasks views have no Status grouping. A task's status is its progress stage, so group by **Progress** instead.

On Todo, **Needs my attention** groups each item by what it needs from you now, most urgent first, from **Ready to merge** and **Changes requested** down to **No action needed**. Each section header has a **?** button that explains what the section holds.

On Todo, **Priority** reads an item's priority from its labels, such as *P0* to *P4* or *urgent*. Kepler does not read a tracker's own priority field, so an issue with no priority label is **Unprioritised**, and every pull request goes under **Not applicable**.

**Age** groups by when an item was created: **Today**, **This week**, **This month**, **Older**, and **No date**. **Assignee** groups by who an item is assigned to on each provider, with **Unassigned** for the rest.

On Todo, **Milestone** groups items by their milestone, with open milestones before closed ones. Items with no milestone go under **No milestone**.

On Todo, **Status** groups issues by their tracker's own workflow state, such as a Linear *In Progress* or a Jira *To Verify*, instead of putting every open issue in one section.

Items with no repository or provider go under **No repository** and **No provider**. A pull request whose provider did not report its author goes under **Unattributed**. An issue goes under **Not applicable**, because issues have no author or reviewer role to group by.

### Your groups

The other groupings arrange tasks by what Kepler can see. A group is one you make yourself: a name and a color you give to tasks that belong together, such as the tasks for one feature or one release. A task can be in 1 group at a time, and groups are available only on Tasks views.

**Create a group.** The **New group** form asks for a **Group name** and a **Color**. Choose **Create group** to save the group. Each active group needs its own name.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-group-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-group-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The New group form: Search typed in the Group name field, the Color row of twelve swatches in two rows with purple chosen, and the Cancel and Create group buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">The New group form.</figcaption>
</figure>

**Put tasks in a group.** You can add tasks to a group in 4 ways:

- **From a task's menu.** A task's **⋮** and right-click menus, on the Dashboard and on the task page, have **Add to group**. Its submenu lists your groups with their colors, with the task's current group checked. Below them, **New group…** opens the form with this task already in it, and **Remove from group** appears for a task that has a group. A task with sub-tasks also offers **Group with its {count} sub-tasks**, which opens the form with the task's name and with the task and its sub-tasks in it.
- **By dragging one task onto another.** Hold a dragged task over another task until a pill appears: **Create group**, or **Add to {group}** when that task has a group. Drop the task on the pill. **Create group** opens the form with both tasks in it. From the keyboard, use the menu.
- **From a selection.** Right-click inside a selection of 2 or more tasks and choose **New group with {count} tasks…**, **Add {count} tasks to group**, or **Remove {count} tasks from group**. See [Act on several tasks at once](#act-on-several-tasks-at-once).
- **By dropping into a group's section.** With the list grouped by your groups, drag a task into another group's section to move it there, or onto **Ungrouped** to remove it from its group.

To add an archived task to a group, restore the task first.

<figure style="text-align:center">
  <a href="/wp-content/uploads/add-to-group-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/add-to-group-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Task actions menu of Fix the cart total with Add to group open: its submenu lists Checkout, with a blue swatch and checked, and Payments, with a green swatch, then New group… and Remove from group. The menu runs Open task page; Progress, In Development, Mark as read and Star; Rename task and Add to group; Manage resources and Refresh; Copy task link and Copy task prompt; then Shut down all agents, Archive task and Delete task. In the list behind, Fix the cart total and Update checkout copy carry a blue bar for Checkout and Upgrade the payment SDK a green bar for Payments.">
  </a>
  <figcaption style="text-align:center; color:#888">Add to group, in a task's menu.</figcaption>
</figure>

**See a task's group.** Under any grouping, a task in a group shows its group's color: a bar on the left edge of a **List** row, or a chip with the group's name after a **Board** card's title. Hover over the bar or chip to see the group's name and a summary of its tasks. Click it to open the group's menu without opening the task:

| Item | What it does |
|---|---|
| **Open group** | Opens every active task in the group in panels. Offered when the group has more than 1 |
| **Show only this group** | Sets the **Group** filter to this group |
| **Group by your groups** | Turns on the **Your groups** switch, keeping the current grouping inside each group |
| **Remove from group** | Takes this task out of the group |
| **Edit group…**, **Archive group**, **Delete group…** | Act on the group itself, as from its header (below) |

**Group the list by your groups.** Turn on the **Your groups** switch in the **View** menu:

- **With None chosen**, each group is a section, in your own order whatever the sort, followed by **Ungrouped** for tasks without a group. Each group's archived tasks are in a folded **Archived** section just after the group. A group with no tasks still has its section, so you can drop tasks into it.
- **With another grouping chosen**, such as **Inbox**, each group has its own sections of that grouping. On the **Board**, each group becomes a lane, and the grouping's sections become columns across every lane.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-groups-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-groups-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Tasks grouped by your groups: the Checkout section, marked blue, holds Fix the cart total and Update checkout copy; the Payments section, marked green, holds Upgrade the payment SDK; and the Ungrouped section holds Add product search and Write the 2.4 release notes. Each group's header shows its color, name, task count and its tasks' session dots, with Open in panels, Select and a ⋮ menu at its end.">
  </a>
  <figcaption style="text-align:center; color:#888">A Tasks view, grouped by your groups.</figcaption>
</figure>

**A group's header.** Each group's header shows the group's color and name, then its count of active tasks and a dot for each state its tasks' sessions are in. A folded group therefore still shows whether something in it needs you. **Select** on a group header selects every task in the group.

To open the group's menu, right-click the header or click its **⋮**. The menu acts on the group, never on its tasks:

| Item | What it does |
|---|---|
| **Edit group…** | Renames the group or changes its color, in the same form |
| **Move group to top**, **Move group up**, **Move group down**, **Move group to bottom** | Moves the group in your order |
| **Manage groups…** | Opens **Settings → Tasks → Groups** (below) |
| **Archive group** | Archives the group. Offered only when every task in it is archived |
| **Delete group…** | Removes the group after a confirmation. Its tasks stay, ungrouped |

You can also drag a group's header to move the group before or after another group.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-group-menu-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-group-menu-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Tasks grouped by your groups, with the menu of the Search group's header open from its ⋮ button: Edit group…, then Move group up and Move group down, Manage groups…, and Delete group…. Behind it, the yellow Search section holds Add product search, the green Payments section Upgrade the payment SDK, and Ungrouped Write the 2.4 release notes.">
  </a>
  <figcaption style="text-align:center; color:#888">A group header's menu.</figcaption>
</figure>

**Archive or delete a group.** When a group's work is done and every task in it is archived, archive the group. The group leaves the Dashboard, and you can reuse its name. If you restore one of its tasks, the group comes back too, and the task stays in it. Deleting a group never deletes its tasks. They stay where they are, without a group.

**Manage every group in Settings.** **Settings → Tasks → Groups** lists every group, including archived groups. There you can create, edit, reorder, restore, and delete groups. See [Groups](/kepler/settings-tasks#groups).

Agents can put tasks into groups too, through Kepler's workspace tools. See [What an agent can do with a task's resources](/kepler/tasks-and-resources#what-an-agent-can-do-with-a-tasks-resources).

### Fold a section

To fold or unfold a section, click its header. The header shows the section's count beside its name.

<figure style="text-align:center">
  <a href="/wp-content/uploads/group-folds-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/group-folds-sep-2026.png" class="help-center-img img-bordered" alt="A group header showing a fold toggle and the section's count">
  </a>
  <figcaption style="text-align:center; color:#888">A group header, with its fold toggle and count.</figcaption>
</figure>

On the **Board** layout, a folded column shrinks to a narrow strip with its name and count. Click the strip to expand the column.

Some sections start folded:

- **Archived**, when you group by Activity or Inbox, because it holds work you have put away.
- **On hold**, **Earlier**, **Not started**, and **Later**, in the Inbox grouping.

Under **Your groups**, folding a group hides the sections inside it, and you can fold each of those sections separately too.

Kepler remembers folds across restarts, for each view and grouping. A section you folded stays folded, and a section you unfolded, such as **Archived**, stays open.

***

## Sort

**Sort by** in the **View** menu orders the items inside each section. It does not change the order of the sections, with 2 exceptions:

- **Repository** sections follow the sort, and each section's place depends on its first task.
- Your own groups always keep the order you gave them.

Each type of view has its own sort options:

| View | Sort by | Default |
|---|---|---|
| **Todo** | Updated, Created, Name, ID, Type | Updated |
| **Tasks** | Updated, Created, Name, Manual | Updated |

Dates sort newest first. **Name** and **ID** sort in ascending order. **Type** puts pull requests before issues, with the most recent first within each. On a Tasks view, starred tasks come first in each section, except under **Manual**. Each view remembers its own sort.

### Put tasks in your own order

**Manual** sorts a Tasks view in an order you set yourself, inside each section, in any grouping, on **List** or **Board**. Each Tasks view keeps its own Manual order. To move a task, use one of these methods:

- Drag its row or card to a place in its own section. A line with a dot shows where it will land. Under **Manual**, a row shows a drag grip when you hover over it.
- Choose **Move up**, **Move down**, or **Move to top of {section}** from the task's **⋮** or right-click menu. These items appear only while the list is sorted by **Manual**.
- Drag one task of a selection to move all the selected tasks together. They land as one block, in the order they were listed. See [Act on several tasks at once](#act-on-several-tasks-at-once).

<figure style="text-align:center">
  <a href="/wp-content/uploads/manual-sort-drag-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/manual-sort-drag-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Upgrade the payment SDK being dragged to the top of the Unread group under the Manual sort: a green line sits above Fix the cart total where it will land, with the dot at its start ringed in purple, the lifted row floats beside it, its own row is dimmed in place, and the Mark as bar covers the toolbar with Read, Exploration, In Development, On hold, Later, Done and Archive task.">
  </a>
  <figcaption style="text-align:center; color:#888">Dragging a task to a new place in its section.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/manual-sort-menu-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/manual-sort-menu-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Task actions menu of Update checkout copy, an on-hold task with a New reply, under the Manual sort, with Move up highlighted: Open task page; Progress, On hold, Mark as read and Star; Rename task and Add to group; the move rows the Manual sort adds, Move up, Move down and Move to top of Unread; Manage resources and Refresh; Copy task link and Copy task prompt; then Shut down all agents, Archive task and Delete task.">
  </a>
  <figcaption style="text-align:center; color:#888">The move rows in a task's menu, under the Manual sort.</figcaption>
</figure>

You do not have to switch to **Manual** first. If you drop a task in a new place in its own section while the list is sorted another way, Kepler saves the order you see, including your move, as the view's **Manual** order, and switches the sort to **Manual**. If you switch to **Manual** yourself, Kepler also keeps the current order, so no task changes place.

If the view already has a saved **Manual** order, a drop under another sort would replace it, so Kepler asks first. To keep the move, choose **Switch and replace Manual**. To put the task back, choose **Cancel**, press **Escape**, or click away.

<figure style="text-align:center">
  <a href="/wp-content/uploads/manual-sort-replace-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/manual-sort-replace-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Tasks view after Upgrade the payment SDK was dropped at the top of Unread while sorted by Updated: the dropped row shows its drag grip and Star button, and a popover under it asks Replace your Manual order? Keeping this move switches the sort to Manual and saves the list in the order you see now, with Cancel and Switch and replace Manual.">
  </a>
  <figcaption style="text-align:center; color:#888">Kepler asks before a drop replaces your saved Manual order.</figcaption>
</figure>

***

## Set a task's progress

By default, Kepler sets a task's progress stage from its Git branches and pull requests (see [Status](/kepler/kepler-interface#status)). Sometimes Git and the pull requests do not show what you know. For example, a review was sent back, or the work was merged somewhere Kepler cannot see. In those cases, set the stage yourself.

<figure style="text-align:center">
  <a href="/wp-content/uploads/progress-menu-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/progress-menu-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Progress menu open from Fix the cart total's In Review control, beside its #51 and #38 chips and Changes requested: Automatic, Updates as you work, checked, then Exploration, In Development, In Review, On hold with its submenu arrow, Later, and Done.">
  </a>
  <figcaption style="text-align:center; color:#888">The Progress menu.</figcaption>
</figure>

You can set the stage in these ways:

- **The progress control.** Click the stage name on a task row, in the panel header, or in the task page header to open the **Progress** menu: **Automatic**, then each stage, **On hold**, and **Later**.
- **The task menus.** A task's **⋮** and right-click menus have the same choices under a **Progress** submenu, plus **Reopen** while the task is Done.
- **Drag a card.** In any grouping, on **List** or **Board**, drag a task's card or row. When grouped by **Progress**, drop it on another stage. On a touch screen, press and hold the card to pick it up. Press **Escape** to cancel the drag. If you drop the card in its own section, Kepler reorders it (see [Put tasks in your own order](#put-tasks-in-your-own-order)).
- **The Mark as bar.** While you drag, a **Mark as** bar appears over the toolbar with chips for what the card can become: **Read** or **Unread**, the stages, **On hold** and **Later**, **Reopen** for a Done task, and **Archive task**. For an archived task, it shows only **Restore**. Drop the card on a chip.
- **From the keyboard.** When a card has focus on the **Board** grouped by **Progress**, press **Cmd/Ctrl+Shift+←** or **Cmd/Ctrl+Shift+→** to move it 1 column.

<figure style="text-align:center">
  <a href="/wp-content/uploads/progress-drag-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/progress-drag-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Board grouped by Progress while Write the 2.4 release notes is dragged from Exploration into In Review: its card stays dimmed in Exploration, the lifted card hangs below Upgrade the payment SDK, In Review is filled and outlined as the drop target, and the other columns, including Later and Done (each reading Nothing here), have dashed outlines. A Mark as bar over the toolbar offers In Development, In Review, On hold, Later, Done and Archive task.">
  </a>
  <figcaption style="text-align:center; color:#888">Dragging a card to another stage, with the Mark as bar over the toolbar.</figcaption>
</figure>

While you drag, each section that accepts the card has a dashed outline. Sections that do not accept it fade, and say why when you hover over them. On the **Board**, a folded column opens when you hold the card over it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/drag-drop-bar-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/drag-drop-bar-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="Fix the cart total lifted off the Tasks view's list. A Mark as bar covers the toolbar with Read, Exploration, In Review, On hold, Later, Done and Archive task; the Unread group has a dashed outline where the card can drop, the card's own row is dimmed in place, and the lifted card floats just below the Not started group.">
  </a>
  <figcaption style="text-align:center; color:#888">Dragging a task in the List grouped by Inbox, with the Mark as bar.</figcaption>
</figure>

The control's tooltip says whether the stage *Updates as you work* or was *Set manually*.

**How a stage you set works with Git.** Kepler keeps a stage you set until Git and the pull requests catch up with it or change. Then Kepler sets the stage from them again:

- If you set a stage *ahead* of Git and the pull requests (**Done** before the merge, or **In Review** before the pull request), the stage stays until they reach it.
- If you set a stage *behind* them (**Reopen**, or a review sent back to **In Development**), the stage stays until they change in any way. A reopened task therefore still follows its next pull request.
- To return the task to automatic stages sooner, choose **Automatic**, or drop its card on the column that Git and the pull requests already show.

**Reopen** on a task you marked Done returns it to the stage that Git and the pull requests show. If Git and the pull requests show the task as finished, **Reopen** sets **In Development**, and the task's next pull request moves it forward again.

Dropping a card on **Archived** opens the archive confirmation. Dragging an archived card to another section restores the task first.

Agents can also set the stage, put a task on hold until a condition, or set it aside for later, through Kepler's workspace tools. If an agent lifts a hold you placed, it tells you.

### Hold a task, or set it aside for later

**On hold** and **Later** both put a task aside without changing its stage. Choosing any stage or **Automatic** lifts either one, and so does the task reaching **Done**.

- **On hold** is a pause. The task's agents keep running, and the hold can lift by itself when something happens.
- **Later** sets the task aside for longer. It stops the task's running agents but keeps their sessions, so you can resume them. **Later** never lifts by itself.

**Hold until something happens.** **On hold** in the **Progress** menu opens a submenu:

| Choice | The hold lifts |
|---|---|
| **Indefinitely** | Only when you lift it |
| **Until CI finishes** | When CI on the task's pull request finishes |
| **Until a review arrives** | When someone reviews the pull request |
| **Until the pull request merges or closes** | When the pull request is merged or closed |
| **Until another task is done** | When the task you pick reaches **Done** |
| **For 1 hour**, **For 3 hours** | After that long |
| **Until tomorrow**, **Until next week** | At 9:00 the next morning, or at 9:00 next Monday |
| **Until a custom date...** | At the date and time you choose, up to a year away |

The pull request rows need an open or draft pull request linked to the task. When the task has several, each pull request row opens a submenu: wait on **All running pull requests** for CI, or **Any pull request** for a review or a merge, or pick one pull request.

<figure style="text-align:center">
  <a href="/wp-content/uploads/hold-until-menu-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/hold-until-menu-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="Fix the cart total's Progress menu, opened from its In Review control beside the #51 and #38 chips and Changes requested, with On hold open on its submenu: Indefinitely; Until CI finishes (dimmed), Until a review arrives and Until the pull request merges or closes; Until another task is done; For 1 hour (3:30 PM), For 3 hours (5:30 PM), Until tomorrow (Tue 9:00 AM), Until next week (Mar 9, 9:00 AM); and Until a custom date…. The Progress menu lists Automatic (checked), Exploration, In Development, In Review, On hold, Later and Done.">
  </a>
  <figcaption style="text-align:center; color:#888">The On hold submenu, with the conditions a hold can wait for.</figcaption>
</figure>

While a task waits, its row says what for, such as *On hold until CI finishes on #51*. When the hold lifts, the row says why, such as *Back from hold: CI passed*. A hold that lifts on bad news, such as failed CI, lists the task under **Needs attention**. Any other reason lists it under **Unread**.

***

## Filter

The **Filters** section at the end of the **View** menu has a submenu for each facet, such as **Progress** or **Provider**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/filter-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/filter-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The View menu, open under the View button (List glyph and Inbox): the List, Board and Graph switch, Your groups, Group by Inbox and Sort by Updated, then Filters with Progress set to In Development and Activity, Repository, Agent, Session, Group and Linked work at Any, and Clear filters. Progress's flyout lists Exploration (1), In Development (ticked, 2), In Review (1), On hold (1), Later, Done and Archived (each 0); Archived's exclude button is hovered, and its tooltip reads Exclude Archived with Shift+Enter. Above, the search box reads progress:development with a 3 hidden pill at its end, and behind the menu the two In Development tasks show their repository and status.">
  </a>
  <figcaption style="text-align:center; color:#888">The Filters section, with a facet's flyout open.</figcaption>
</figure>
<figure style="text-align:center">
  <a href="/wp-content/uploads/filter-todo-oct-2026-v6@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/filter-todo-oct-2026-v6@2x.png" class="help-center-img img-bordered" alt="The View menu on Todo, under the View button reading Type and Mine: the List and Board switch, the Mine and All scope switch with Mine chosen and Your work, in every org under it, Group by Type and Sort by Updated, then Filters: Needs my attention, Review requests, Your role, Type, Linked work, Status, Priority, Age and Provider, then a GitHub section with Repository, Assignee, Author, Reviewer, Label and Milestone, each set to Any. The Milestone flyout lists Release 2.4 and Release 2.5 with their counts, and No milestone.">
  </a>
  <figcaption style="text-align:center; color:#888">The View menu on Todo. Each connection gets its own section, here GitHub.</figcaption>
</figure>

Each type of view has these facets:

| View | Facets |
|---|---|
| **Todo** | Needs my attention · Review requests · Your role · Type · Linked work · Status · Priority · Age · Provider, then one section per connection with its own Repository · Assignee · Author · Reviewer · Issue type · Label · Project · Milestone · Iteration or Sprint |
| **Tasks** | Progress · Activity · Repository · Agent · Session · Group · Linked work |

Facets with a fixed set of values, such as **Progress** or **Priority**, always list every value, even one that nothing matches. Other facets list only the values in your work, and Kepler hides a facet that has no values to choose from.

GitHub Enterprise and GitLab Self-Hosted get sections of their own. **Milestone** appears for providers that have milestones, such as GitHub, GitLab, and Linear.

**Issue type**, **Label**, **Project**, and **Iteration** use your provider's own values (a Jira issue type, your team's labels, a board name), not Kepler's own names for them. Azure DevOps calls the last one **Iteration** and Jira calls it **Sprint**, so the facet uses each tracker's word.

**Linked work** filters by whether an item is connected to work in the other type of view:

- In Todo, it filters each pull request or issue by its task history: *Has an active task*, *Archived tasks only* (worked on before, but every task is archived), or *No tasks ever*.
- In Tasks, it offers *Has a PR or issue*.

**Activity** matches a task when *any* of its sessions is in that state, so a task with one running session and one unread session matches both **Running** and **Unread**.

**Session** offers *Has a session* and *Has a live session*. To find tasks *without* a pull request, issue, or session, exclude the value.

**Group** lists each of [your groups](#your-groups), including empty ones, and **Ungrouped** for tasks without a group. When the list is grouped by your groups, the facet also limits which group sections appear.

**Include or exclude any value.** Click a value to include it. To exclude a value instead, hover over it and click its minus button, or press **Shift+Enter** from the keyboard. An excluded value reads *not {value}*. On Todo, excluding a provider's value removes only that provider's items, so excluding a GitHub label never hides a Jira issue.

**Values you include in one facet are combined.** If you tick GitHub *and* GitLab under **Provider**, the list shows items from either provider. Excluded values remove items: Kepler hides an item that matches any of them. A facet with nothing chosen reads **Any** and does not narrow the list.

To find a value in a long facet, type in its **Search filters…** box. The filters you choose also show in the search box, and you can type them there instead. See [Filter from the search box](#filter-from-the-search-box). When a narrow window folds the search box into an icon, the **View** button counts the filters instead. Hover over the button to see them.

***

## Search

The search box finds items by **title, reference, or repository**, and finds tasks by their branch names too. Each word you type matches on its own, in any order, so *login kepler* finds a *Fix login* task in the kepler repository. Put a word or phrase in quotes to match whole words only: *"log"* leaves out *login*.

To find one task, paste its link (**Copy task link**) into the search box. A session's link (**Copy session link**) finds the task that holds the session.

The search box fills the free space in the toolbar. To have it grow only as you type, set **Search box** to **Grows as you type** in [Settings → Appearance → Dashboard](/kepler/settings-app#dashboard).

When a search or a filter narrows the list, pills at the right end of the search box show how many rows are left or hidden. Each pill clears only its own search or filters:

| Pill | What it counts | Clicking it |
|---|---|---|
| The search pill | The rows on screen out of every row: *{count} of {total}* | Clears the search |
| The filter pill | The rows your filters hide: *{count} hidden* | Clears the filters |

While a search is on, the filter pill counts only hidden rows that match the search. If a search seems to miss something, the filter pill shows whether your filters are hiding it. On Todo, a count such as *40+* means more items are still loading.

When nothing matches, the empty list offers a button that clears the search, the filters, or both.

Search covers only the work the view has already loaded. On a Todo view, that is the work its scope lists. See [Choose what a Todo view lists](#choose-what-a-todo-view-lists).

### Filter from the search box

The search box also takes the view's filters, written as qualifiers such as `activity:waiting` or `type:pr`, beside your search words. As you type, it suggests filters, then their values with their counts. A filter you set in the **View** menu appears in the box as a qualifier, and a qualifier you type sets the filter. When you type a qualifier:

- Put **-** before a qualifier to exclude its value, such as `-progress:done`.
- Put a name with spaces in quotes, such as `group:"Release work"`.
- On a Tasks view, `branch:` filters by branch name.

A qualifier that can match nothing is underlined. Hover over it to see why, such as a group name that does not exist.

<figure style="text-align:center">
  <a href="/wp-content/uploads/search-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/search-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The search box holding progress:, with a suggestions list under it: Exclude progress, then the Progress stages Exploration, In Development, In Review, On hold, Later, Done and Archived, each with its count of tasks. The View button, showing the List glyph and Inbox, sits to the left of the box, and the task list shows behind the suggestions.">
  </a>
  <figcaption style="text-align:center; color:#888">The search box suggesting the values of a filter.</figcaption>
</figure>

***

## What Kepler remembers

Each view keeps its layout, grouping, sort, filters, search text, and, on Todo, its scope, in every window and across restarts. In each window, each view also remembers its open panels and their layout, its folded sections, and where you scrolled to. If you switch to another view and back, the panels you were reading are still open.

After a restart, each window reopens on the view it was showing, with that view's panels.

***

## Archive, restore, and clean up in bulk

**Archive task** puts a task away. The task moves from its current section to **Archived**, and Kepler stops its running agents. Its sessions and resources are kept, so you can resume them later. With **Also delete worktrees** ticked, archiving ends the task's agents instead, and closes the Kepler terminals open in those worktrees.

<figure style="text-align:center">
  <a href="/wp-content/uploads/archive-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/archive-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Task actions menu open from Fix the cart total's ⋮ button, beside the task list, with Archive task highlighted: Open task page; Progress, In Development, Mark as read and Star; Rename task and Add to group; Manage resources and Refresh; Copy task link and Copy task prompt; then Shut down all agents, Archive task and Delete task.">
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

The confirmation offers the same options as deleting a task: **Also delete worktrees**, **Also delete branches** (after you tick **Also delete worktrees**), and **Also delete the branch on the remote** (after you tick **Also delete branches**). You can therefore remove a finished task's worktrees and branches from disk without deleting the task. With **Also delete worktrees** ticked, the dialog lists each worktree with what will happen to it, such as *2 uncommitted files*, and names the worktrees it keeps, such as the repository's main worktree. Kepler keeps a worktree that would lose work unless you tick the extra box that names what would be lost. To check before you decide, open the changes from the row of a worktree at risk.

With **Also delete the branch on the remote** ticked, Kepler also deletes each branch's remote copy, unless that would lose work, such as a branch with an open pull request or commits that are not on the remote. A message says which branches it kept, and why.

**Restore task** replaces **Archive task** in an archived task's **⋮** menu, and also appears in the task page's header. It restores the task at once, without asking. A restored task stays in its group, and if that group was archived, Kepler restores the group too.

To archive, restore or delete several tasks at once, click **Select** on a section header in a Tasks view. The header becomes a bar with a select-all box and the actions, and the section's rows show checkboxes. You can select in 1 section at a time, and while you select, clicking a row ticks it instead of opening its panel.

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

Right-clicking inside the selection opens a selection menu instead of the task menu, and each item counts the tasks it acts on. With it you can set the progress of every selected task, mark them read or unread, star or unstar them, group or ungroup them, shut down their agents, and archive, restore or delete them. **Shut down agents** asks first while an agent is still working. The group and **Progress** items skip archived tasks. **Archive**, **Restore**, and **Delete** open the same batch confirmation as a section's **Select** bar. For the full menu, see [Task rows](/kepler/kepler-interface#task-rows).

Dragging a selected task drags the whole selection. Each drop target says how many of the tasks it accepts. After the drop, Kepler reports how many tasks moved and how many stayed where they were. Under the **Manual** sort, the tasks land together as one block.

To clean up worktrees and local branches instead of tasks, open **Settings → Repositories** and choose **Manage worktrees and branches**. The **Worktrees and branches** page lists every worktree, and every local branch that no worktree has checked out. You can filter the list by **Safe to delete**, **Needs update**, **Conflicts**, **Stale**, or **All**. On this page, you can:

- **Update** several worktrees at once, which brings each branch up to date with its base.
- Delete worktrees and branches, including their copies on the remote.

See [Settings](/kepler/settings-repositories#worktrees-and-branches).

---
