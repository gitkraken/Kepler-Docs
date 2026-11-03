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

- The search box finds items in the list. See [Search](#search).
- The **View** button opens the **View** menu. The menu sets the layout (**List**, **Board**, or **Graph**), what the list is grouped and sorted by, and the filters. The button shows the layout's icon, the grouping, the sort, and how many filters are on.
- **Panel layout** arranges open panels side by side (**Columns**) or in a **Grid**. See [Open a panel](/kepler/kepler-interface#open-a-panel).
- **Refresh** fetches the view's items from your providers again.

Each choice in the **View** menu saves itself in the view you are on, so the menu has no **Save** button. To learn what each part of the screen is, see [The Kepler Interface](/kepler/kepler-interface).

<figure style="text-align:center">
  <a href="/wp-content/uploads/arrange-work-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/arrange-work-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Dashboard's arranging controls: the row of views (Todo, Tasks selected, Agent Graph, New view), and under it the list toggle, the search box reading Search title, ref, or repo…, the View button showing the List glyph, Inbox and Updated, then Panel layout and Refresh at the right. Tasks and Agent Graph carry the orange mark of a task waiting on you.">
  </a>
  <figcaption style="text-align:center; color:#888">The views, and the search, View, panel and refresh controls under them.</figcaption>
</figure>

To open several tasks at once, use the open button on a section header, or **Open group** on one of [your groups](#your-groups). The toolbar has no button that opens every row in the list.

If the window is too narrow for the whole toolbar, the **View** button drops the sort first and then the grouping, but it always keeps the layout's icon and the filter count. Next the search box narrows, and last it becomes a search icon, **Search the list**. A dot on the icon means a search is on. Click the icon, or press **Cmd/Ctrl+F**, to open the search box.

***

## Views

Each view lists one kind of work:

- A **Todo** view lists pull requests and issues from your connected providers.
- A **Tasks** view lists your tasks.

Kepler starts you with a **Todo** view and a **Tasks** view, and an **Agent Graph** view, which is a Tasks view drawn in the **Graph** layout (see [Layouts](#layouts)). The views appear on every page. Click a view to show it. On another page, clicking a view opens the Dashboard on it.

A view keeps its own layout, grouping, sort, and filters, and a Todo view also keeps its scope (see [Choose what a Todo view lists](#choose-what-a-todo-view-lists)). Every window shares the same views.

<figure style="text-align:center">
  <a href="/wp-content/uploads/saved-views-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/saved-views-oct-2026.png" class="help-center-img img-bordered" alt="The Tasks view's menu open from its tab in the Dashboard's row of views (Todo, Tasks, Agent Graph, New view), where Tasks and Agent Graph carry the orange mark of a task waiting on you: Rename with F2, Change icon showing Rocket, Show counts on views ticked, View options, Duplicate view highlighted, Move left, Move right, Views position, and Delete view.">
  </a>
  <figcaption style="text-align:center; color:#888">A view's menu.</figcaption>
</figure>

**A view's menu.** Click the view you are on, or right-click any view, to open its menu:

| Menu item | What it does |
|---|---|
| **Rename** (**F2**) | Edits the view's name in place. Double-clicking the name does the same |
| **Change icon** | Picks the view's icon. See [Change a view's icon](#change-a-views-icon) |
| **Show counts on views** | Turns task counts on or off for every view. See [Status and counts on views](#status-and-counts-on-views) |
| **View options** | Opens the **View** menu for this view |
| **Duplicate view** | Adds a copy of the view, named *{name} copy*, with the same settings and the same Manual order |
| **Move left**, **Move right** | Moves the view 1 place. Along the left side of the window, these read **Move up** and **Move down** |
| **Views position** | Sets where all the views sit. See [Where the views sit](#where-the-views-sit) |
| **Delete view** | Removes the view after a confirmation |

**Delete view** asks *Delete {name}?*, because *Its layout, grouping, sort and filters are removed from every window.* You cannot delete your last Todo view or your last Tasks view (*Unable to delete the last view of this type*).

**Add a view.** Click **New view** after the views, or right-click the empty space beside them and point to **New view**. Choose **Todo** or **Tasks** for a new view of that type, or **Duplicate current view** to copy the view you are on. **Repository** is listed but not available yet (*Coming with the commit graph*). A new view opens with its name ready to edit, then a **Set up {name}** menu with an **Icon** row and the **View** menu's choices. Choose **Done** to close it.

**Reorder the views.** Drag a view to a new place with a mouse, or use **Move left** and **Move right** in its menu. On the Dashboard, you can also use these keys:

| Keys | What they do |
|---|---|
| **Cmd/Ctrl+Shift+[**, **Cmd/Ctrl+Shift+]** | **Previous tab**, **Next tab**: show the previous or next view. On Windows and Linux, **Ctrl+PageUp** and **Ctrl+PageDown** also work |
| **Cmd+Option+[**, **Cmd+Option+]** (**Ctrl+Alt+[**, **Ctrl+Alt+]** on Windows and Linux) | **Move tab left**, **Move tab right**: move the view you are on. On Windows and Linux, **Ctrl+Shift+PageUp** and **Ctrl+Shift+PageDown** also work |

When focus is in a panel that has its own tabs, these keys act on the panel's tabs instead. Inside the row of views, the arrow keys move between views, **F2** renames the focused view, and **Shift+F10** opens its menu. See [Keyboard shortcuts](/kepler/settings-app#keyboard-shortcuts).

If the views have no room left, they fold into 1 button that names the view you are on. Click it to see every view, **New view**, and the shown view's actions.

### Change a view's icon

Each view type has its own icon. To pick another, open the view's menu and point to **Change icon**. The picker has a **Search icons** field over a grid of icons. Its first icon is the type's own, marked **Default, {name}** at the foot of the picker, which names whichever icon you point to. The **Set up {name}** menu of a new view has the same picker under **Icon**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/dashboard-view-icon-picker-nov-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/dashboard-view-icon-picker-nov-2026.png" class="help-center-img img-bordered" alt="The Tasks view's menu open from its tab, with Change icon, Rocket, highlighted and its picker open beside it: a Search icons field over a grid of six rows of icons, the rocket first and outlined, and a footer reading Default, Rocket.">
  </a>
  <figcaption style="text-align:center; color:#888">The icon picker, from a view's Change icon row.</figcaption>
</figure>

### Where the views sit

The views sit in a row below the title bar. To move them, choose **Views position** in any view's menu, then one of these:

- **Title bar**: in the title bar, after **New task**.
- **Below title bar**: in a row of their own. This is the default.
- **Left side**: down the left side of the window. **New view** follows the views, and **Settings** moves to the foot of the column.

Along the left side, the views start as icons. To show their names, click **Expand views** at the foot of the column, or drag the column's edge. Dragging the edge moves through **Icons only**, **Icons and counts**, and names. **Collapse views** returns to icons. Right-click the empty space in the column for **New view**, **Views position**, **Views size** (**Default** or **Compact**), **Show counts**, and **Show names**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/dashboard-views-side-rail-nov-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/dashboard-views-side-rail-nov-2026.png" class="help-center-img img-bordered" alt="The Dashboard with its views along the left side, expanded to show names: Todo, Tasks (selected), Agent Graph and New view at the top, Settings and the Collapse views button at the foot. Tasks and Agent Graph carry the orange mark of a task waiting on you. The top bar keeps New task, Ask, Feedback and the account but no Settings button, and the Tasks list fills the rest of the window under its toolbar.">
  </a>
  <figcaption style="text-align:center; color:#888">The views along the left side of the window, with their names shown.</figcaption>
</figure>

**Settings → Appearance → Dashboard** has the same choices, and also **View style**, which draws the views in or below the title bar as **Tabs** (the default) or **Pills**. See [Dashboard settings](/kepler/settings-app#dashboard).

### Status and counts on views

A Tasks view shows its agents' most urgent state as a mark on its icon, using the same levels as the [tray icon](/kepler/kepler-interface#the-tray-icon): **Needs your answer**, **Failed, unread**, **Finished, unread**, or **Working**. Only the tasks that the view's filters keep count, and archived tasks never do. A view scrolled out of sight shows its state as a dot at the edge of the row. When the views fold into 1 button, a dot on the button says that another view needs you, for example *Another view needs your answer*.

A view with filters also shows how many tasks match them. To hide the counts, turn off **Show counts on views** in any view's menu, or **Counts on views** in **Settings → Appearance → Dashboard**.

Hover a view to see its card: the view's name, its state, its task count, and its filters.

<figure style="text-align:center">
  <a href="/wp-content/uploads/dashboard-view-status-badges-nov-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/dashboard-view-status-badges-nov-2026.png" class="help-center-img img-bordered" alt="The Dashboard's row of views with the Tasks view filtered: its tab shows a count of 2 beside its name and an orange mark on its icon, and Agent Graph has the same mark. Hovering Tasks opens its card: Tasks, Needs your answer, 2 tasks, and its filter chip, Progress In Development.">
  </a>
  <figcaption style="text-align:center; color:#888">A filtered view's count and status mark, with its card.</figcaption>
</figure>

### Choose what a Todo view lists

A Todo view's **View** menu has a **Scope** switch under the layout switch:

- **Mine**, the default, lists work that is *Created by you, assigned to you, mentioning you, or awaiting your review*, in every organization.
- **All** lists *Everything open in Kepler's repos, plus your work elsewhere*.

Under **All**, **Repos** chooses **All repos in Kepler** or **Custom** repositories, and **Updated** chooses **Last 7 days**, **Last 30 days**, **Last 90 days** (the default), or **Last year**. Under **All**, the **Your role** filter and grouping also offer **Not mine**. For what each provider adds, and which very large repositories **All repos in Kepler** skips, see [The Dashboard's views](/kepler/kepler-interface#the-dashboards-views).

***

## Layouts

<figure style="text-align:center">
  <a href="/wp-content/uploads/view-options-sep-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/view-options-sep-2026-v2@2x.png" class="help-center-img img-bordered" alt="The top of the View menu, open under the View button (List glyph, Inbox, Updated): its layout switch with List selected, then Board and Graph.">
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

**Board** shows the sections of the *current* grouping as columns side by side, so **Group by** sets what the columns are. When you group by **Progress**, the columns are the stages: **Exploration**, **In Development**, **In Review**, and **Done**. These columns stay in place as tasks move between them, and an empty column reads **Nothing here**. **On hold**, **Later**, and **Archived** are exceptions: each appears when it holds a task, and all 3 appear while you drag a card so you can drop the card on them. On every other grouping, Kepler hides empty sections, except your own groups, which stay so you can drop tasks into them.

When **Your groups** is on and another grouping is chosen, the **Board** becomes a grid. Each group is a row (a lane), and the grouping's sections are columns across every lane. See [Your groups](#your-groups).

All columns on the board have the same width. To resize them, use one of these methods:

- Drag the gap after any column. All columns resize at once.
- Focus the gap and press the arrow keys. **Home** sets the narrowest width and **End** the widest.
- Double-click the gap to return to the default width.

Each view remembers its own column width. When a column has more tasks to load, **Load more** appears at the bottom of the column. From the keyboard, **←** and **→** move to the nearest column that has a card.

<div class="note" markdown="1">

**Columns** in the **Panel layout** control is not the **Board** layout. **Columns** and **Grid** set how open panels are arranged, not how the list is drawn.

</div>

<figure style="text-align:center">
  <a href="/wp-content/uploads/columns-progress-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/columns-progress-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Tasks view on the Board layout, grouped by Progress: the Exploration, In Development, In Review, On hold and Done columns side by side, each with its count, Open in panels and Select. Each task is a card with its title, age, session and progress glyphs, its waiting state (New reply, or Approval needed for Run npm test), and, for a task with a worktree, its repository and branch; Done reads Nothing here. Above, the toolbar holds the search box and the View button showing the Board glyph, Progress and Updated.">
  </a>
  <figcaption style="text-align:center; color:#888">The Board layout, grouped by Progress.</figcaption>
</figure>

On the board grouped by **Progress**, you can also move a task to another stage by hand. See [Set a task's progress](#set-a-tasks-progress).

**Graph** replaces the list instead of arranging it. While it is chosen, the **View** menu shows the graph's own controls, such as **Detail depth**, **Direction**, and **Zoom**, in place of **Group by** and **Sort by**, and its **Filters** add **Sessions** (**Active**). Each view in the **Graph** layout keeps its own graph settings. See [The Agent Graph](/kepler/agent-graph).

***

## Group

**Group by** in the **View** menu divides the list into sections.

<figure style="text-align:center">
  <a href="/wp-content/uploads/group-options-tasks-sep-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/group-options-tasks-sep-2026-v3@2x.png" class="help-center-img img-bordered" alt="The View menu open under the View button, which reads Your groups › Inbox and Updated: the List, Board and Graph switch, the Your groups switch on with Shows Inbox within each group under it, and Group by open on its submenu of Inbox (checked), Progress, Activity, Repository (highlighted) and None. Below come Sort by, Updated, and the Filters section: Progress, Activity, Repository, Agent, Session, Group and Linked work, each Any.">
  </a>
  <figcaption style="text-align:center; color:#888">Group by in the View menu of a Tasks view.</figcaption>
</figure>

Each type of view has its own groupings:

| View | Group by | Default |
|---|---|---|
| **Todo** | Type, Needs my attention, Priority, Age, Your role, Assignee, Provider, Repository, Status, None | Type |
| **Tasks** | Inbox, Progress, Activity, Repository, None, and the **Your groups** switch above them | Inbox |

On a Tasks view, the **Your groups** switch above **Group by** divides the list by groups you make yourself, either alone or with another grouping inside each group. See [Your groups](#your-groups).

### Inbox

**Inbox** is the default on Tasks views. It groups tasks by what each task needs from *you*, not by how far the work has progressed. Sections that need you come first, and the sections for work you have put away come last:

| Section | What it holds |
|---|---|
| **Needs attention** | Something waits on you: a permission request, a question, a Kepler approval request, or a program in one of the task's terminals. Also a failed turn (**Turn failed**), failing CI on the task's open pull request (**CI failing**), a new review that requests changes (**Changes requested**), or a hold that lifted on bad news |
| **Unread** | A session finished a turn you have not looked at, or a hold lifted for another reason (*Back from hold: CI passed*) |
| **Running** | An agent is working on it |
| **Important** | A task you starred, with **Star** in its menu |
| **Recent** | Moved in the last 24 hours |
| **On hold** | You or an agent put it on hold. Starts folded |
| **Earlier** | Moved more than 24 hours ago. Starts folded |
| **Done** | Finished, waiting only on the decision to archive it |
| **Not started** | No session has started in it yet, and it is still at **Exploration**. Starts folded |
| **Later** | You or an agent set it aside for later. Starts folded |
| **Archived** | Tasks you archived, which list here before any other section. Starts folded |

A finished turn stays unread until you look at it, even when it finished while you were away.

**Inbox** lists every task exactly once:

- A task that is both unread *and* blocked on you appears under **Needs attention**.
- A task under **Running** appears only there, not also in a time section. A failed turn is the exception: it lists the task under **Needs attention** even while another of its agents works.
- A task under **Done** appears only there, instead of in the time section it would otherwise get.
- A starred task lists under **Important** unless it needs you, is unread, is held, is running, or is done.

**Drop a card on an Inbox section.** To act on a task, drag its card onto another Inbox section:

| Drop on | What happens |
|---|---|
| **Unread** | Marks the task unread. Refused when it has no sessions, is archived, or is already waiting on you |
| **Recent** or **Earlier** | Marks an unread task read |
| **Important** | Stars the task. Refused while it is on hold or set aside for later (*Take it off hold or Later to list it as Important*), working, done, or waiting on you |
| **On hold** or **Later** | Puts the task on hold, or sets it aside for later. Refused when it is already done or waiting on you |
| **Done** | Marks the task done. Refused while an agent is still working |
| **Archived** | Opens the archive confirmation |
| **Needs attention**, **Running**, or **Not started** | Refused: these clear when you respond, show while an agent works, or list only tasks with no sessions yet |

To see what a drag looks like, see [Set a task's progress](#set-a-tasks-progress).

A task stays in **Running** briefly between turns, so it does not jump between sections. Running tasks keep the order they started in, instead of changing places as they work. Moves into **Unread** and **Needs attention** happen at once, because they mean something changed.

**On hold** and **Later** are for tasks you do not want to work on now, so a held task stays there even while an agent works on it. A held task still moves up when something needs you: an unread turn or a blocked prompt lists it under **Unread** or **Needs attention**.

### The other groupings

**Progress** and **Activity** group the same tasks in 2 different ways:

- **Progress** shows how far the work has progressed: **Exploration**, **In Development**, **In Review**, **On hold**, **Later**, **Done**, **Archived**. Group by Progress to see where each task is in your workflow.
- **Activity** shows what the task's agent sessions are doing now, using the sessions' own states, most urgent first: **Waiting**, **Error**, **Unread**, **Running**, **Starting**, **Ready**, **Idle**, and **Ended**. A task lists under the state of its most urgent session. Grouping by Activity also adds **No sessions** for a task with no sessions started, then **Done**, and **Archived** last. Group by Activity to see what needs a person.

**Repository** is the only grouping that can list a task twice. A task with worktrees in several repositories appears under each repository.

Tasks views have no Status grouping. A task's status is its progress stage, so group by **Progress** instead.

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

Each section header has a **?** button (**About {label}**) that explains what the section holds. For example, **Ready to merge** is *Yours, approved, no open feedback and no blockers the provider can see. It only needs merging.*

On Todo, **Priority** reads an item's priority from its labels: names such as *P0* to *P4*, a *priority:* prefix, or a bare *blocker*, *critical*, *urgent*, *highest*, or *lowest*. When an item has several, the most urgent label counts. The sections are **Urgent**, **High**, **Medium**, **Low**, and **Unprioritised**, and every pull request goes under **Not applicable**. Kepler does not read a tracker's own priority field, so an issue with no priority label is **Unprioritised**.

**Age** groups by when an item was created: **Today**, **This week**, **This month**, **Older**, and **No date**. **Assignee** groups by who an item is assigned to on each provider, with **Unassigned** for the rest. A pull request whose provider did not say who is assigned goes under **Assignee unknown** instead of **Unassigned**.

On Todo, **Status** groups issues by their tracker's own workflow state, such as a Linear *In Progress* or a Jira *To Verify*, instead of putting every open issue in one section.

Items with no repository or provider go under **No repository** and **No provider**. A pull request whose provider did not report its author goes under **Unattributed**. An issue goes under **Not applicable**, because issues have no author or reviewer role to group by.

### Your groups

The other groupings arrange tasks by what Kepler can see. A group is one you make yourself: a name and a color you give to tasks that belong together, such as the tasks for one feature or one release. A task can be in 1 group at a time, and groups are available only on Tasks views.

**Create a group.** The **New group** form asks for a **Group name** and a **Color**. The 12 colors are **Gray**, **Blue**, **Pink**, **Yellow**, **Green**, **Purple**, **Cyan**, **Orange**, **Teal**, **Indigo**, **Brown**, and **Red**. The form starts on the color your groups use least, but never on **Red**, so a new group looks different from your other groups unless you choose otherwise. Choose **Create group** to save the group. These rules apply:

- A group needs a name (*Give the group a name*).
- Each active group needs its own name, regardless of capitalization (*A group with this name already exists*). You can reuse an archived group's name.
- What you type stays in the form if you press **Escape** or click away, until you close the window. Only **Cancel** or saving clears it.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-group-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-group-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The New group form: Search typed in the Group name field, the Color row of twelve swatches in two rows with purple chosen, and the Cancel and Create group buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">The New group form.</figcaption>
</figure>

**Put tasks in a group.** You can add tasks to a group in 4 ways:

- **From a task's menu.** A task's **⋮** and right-click menus, on the Dashboard and on the task page, have **Add to group**. Its submenu lists your groups with their colors, with the task's current group checked. Below them, **New group…** opens the form with this task already in it, and **Remove from group** appears for a task that has a group. A task with sub-tasks also offers **Group with its {count} sub-tasks**, which opens the form with the task's name and with the task and its sub-tasks in it.
- **By dragging one task onto another.** Hold a dragged task over another task for half a second, and a pill appears on the task underneath: **Create group** when that task has no group, or **Add to {group}** in its group's color. Drop the task on the pill. **Create group** opens the form with both tasks in it and the other task's title as the name. The pill needs a pointer. From the keyboard, use the menu.
- **From a selection.** Right-click inside a selection of 2 or more tasks and choose **New group with {count} tasks…**, **Add {count} tasks to group**, or **Remove {count} tasks from group**. See [Act on several tasks at once](#act-on-several-tasks-at-once).
- **By dropping into a group's section.** With the list grouped by your groups, drag a task into another group's section to move it there, or onto **Ungrouped** to remove it from its group.

To add an archived task to a group, restore the task first.

<figure style="text-align:center">
  <a href="/wp-content/uploads/add-to-group-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/add-to-group-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Task actions menu of Fix the cart total with Add to group open: its submenu lists Checkout, with a blue swatch and checked, and Payments, with a green swatch, then New group… and Remove from group. The menu runs Open task page; Progress, In Development, Mark as read and Star; Rename task and Add to group; Manage resources and Refresh; Copy task link and Copy task prompt; then Shut down all agents, Archive task and Delete task. In the list behind, Fix the cart total and Update checkout copy carry a blue bar for Checkout and Upgrade the payment SDK a green bar for Payments.">
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

**Group the list by your groups.** Turn on the **Your groups** switch in the **View** menu. The line under the switch describes the result:

- **With None chosen** (*Shows a section per group*), each group is a section, in your own order whatever the sort, followed by **Ungrouped** for tasks without a group. Each group's archived tasks are in an **Archived** section just after the group, folded at first. A group with no tasks still has its section, so you can drop tasks into it.
- **With another grouping chosen** (*Shows {axis} within each group*), the **View** button reads, for example, **Your groups › Inbox**, and each group has its own **Inbox** sections, which you can fold separately. On the **Board**, each group becomes a lane, and the grouping's sections become columns across every lane.

Until you have a group, the switch says *Drag a task onto another to group them*.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-groups-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-groups-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Tasks grouped by your groups: the Checkout section, marked blue, holds Fix the cart total and Update checkout copy; the Payments section, marked green, holds Upgrade the payment SDK; and the Ungrouped section holds Add product search and Write the 2.4 release notes. Each group's header shows its color, name, task count and its tasks' session dots, with Open in panels, Select and a ⋮ menu at its end.">
  </a>
  <figcaption style="text-align:center; color:#888">A Tasks view, grouped by your groups.</figcaption>
</figure>

**A group's header.** Each group's header shows the group's color and name, then its count of active tasks and a dot for each state its tasks' sessions are in. A folded group therefore still shows whether something in it needs you. **Select** on a group header selects every task in the group. As the header gets narrower, it hides the session dots first, then shortens **Select** to an icon, so the name stays readable.

To open the group's menu, right-click the header or click its **⋮**. The menu acts on the group, never on its tasks:

| Item | What it does |
|---|---|
| **Edit group…** | Renames the group or changes its color, in the same form |
| **Move group to top**, **Move group up**, **Move group down**, **Move group to bottom** | Moves the group in your order. **Move group to top** and **Move group to bottom** appear only when they would move the group more than 1 place |
| **Manage groups…** | Opens **Settings → Tasks → Groups**, which lists every group (below) |
| **Archive group** | Archives the group. Offered only when every task in it is archived |
| **Delete group…** | Removes the group after a confirmation, *Its {count} tasks stay, ungrouped.* |

You can also drag a group's header to move the group before or after another group. **Ungrouped**, and the sections inside a group, cannot be moved.

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-group-menu-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-group-menu-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Tasks grouped by your groups, with the menu of the Search group's header open from its ⋮ button: Edit group…, then Move group up and Move group down, Manage groups…, and Delete group…. Behind it, the yellow Search section holds Add product search, the green Payments section Upgrade the payment SDK, and Ungrouped Write the 2.4 release notes.">
  </a>
  <figcaption style="text-align:center; color:#888">A group header's menu.</figcaption>
</figure>

**Archive or delete a group.** When a group's work is done and every task in it is archived, archive the group. The group leaves the Dashboard, and you can reuse its name. If you restore one of its tasks, the group comes back too, and the task stays in it. Deleting a group never deletes its tasks. They stay where they are, without a group.

**Manage every group in Settings.** **Settings → Tasks → Groups** lists every group, including archived groups and groups a filter hides. Each row shows the group's color, its name, its task count, and a **⋮** menu. Click a group's name to edit it. To reorder groups, drag a row's grip, or focus the grip and press **Alt+Up** or **Alt+Down**. Archived groups are listed under **Archived**, where their menu offers **Restore group** and **Delete group…**. **New group** makes a group. See [Groups](/kepler/settings-tasks#groups).

Agents can put tasks into groups too, through Kepler's workspace tools. See [What an agent can do with a task's resources](/kepler/tasks-and-resources#what-an-agent-can-do-with-a-tasks-resources).

### Fold a section

To fold or unfold a section, click its header. The header shows the section's count beside its name.

<figure style="text-align:center">
  <a href="/wp-content/uploads/group-folds-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/group-folds-sep-2026.png" class="help-center-img img-bordered" alt="A group header showing a fold toggle and the section's count">
  </a>
  <figcaption style="text-align:center; color:#888">A group header, with its fold toggle and count.</figcaption>
</figure>

On the **Board** layout, a folded column shrinks to a narrow strip with its name and count, and is marked when it holds the open item. Click the strip to expand the column.

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

Dates sort newest first. **Name** and **ID** sort in ascending order. **ID** compares numbers by value, so *#9* comes before *#10*. **Type** puts pull requests before issues, with the most recent first within each. On a Tasks view, starred tasks come first within each section under **Updated**, **Created**, and **Name**. Each view remembers its own sort.

### Put tasks in your own order

**Manual** sorts a Tasks view in an order you set yourself, inside each section, in any grouping, on **List** or **Board**. Each Tasks view keeps its own Manual order, and a duplicated view starts with the order of the view it copies. To move a task, use one of these methods:

- Drag its row or card to a place in its own section. A line with a dot shows where it will land. Under **Manual**, a row shows a drag grip when you hover over it.
- Choose **Move up**, **Move down**, or **Move to top of {section}** from the task's **⋮** or right-click menu. These items appear only while the list is sorted by **Manual**.
- Drag one task of a selection to move all the selected tasks together. They land as one block, in the order they were listed. See [Act on several tasks at once](#act-on-several-tasks-at-once).

<figure style="text-align:center">
  <a href="/wp-content/uploads/manual-sort-drag-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/manual-sort-drag-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Upgrade the payment SDK being dragged to the top of the Unread group under the Manual sort: a green line with a dot sits above Fix the cart total where it will land, Fix the cart total shows a Create group pill for dropping the card onto it instead, the lifted row floats beside it, its own row is dimmed in place, and the Mark as bar covers the toolbar with Read, Exploration, In Development, On hold, Later, Done and Archive task.">
  </a>
  <figcaption style="text-align:center; color:#888">Dragging a task to a new place in its section.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/manual-sort-menu-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/manual-sort-menu-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Task actions menu of Update checkout copy, an on-hold task with a New reply, a drag handle and its Star button, under the Manual sort: Open task page; Progress, On hold, Mark as read and Star; Rename task and Add to group; the move rows the Manual sort adds, Move up, Move down and Move to top of Unread; Manage resources and Refresh; Copy task link and Copy task prompt; then Shut down all agents, Archive task and Delete task.">
  </a>
  <figcaption style="text-align:center; color:#888">The move rows in a task's menu, under the Manual sort.</figcaption>
</figure>

You do not have to switch to **Manual** first. If you drop a task in a new place in its own section while the list is sorted another way, Kepler saves the order you see, including your move, as the view's **Manual** order, and switches the sort to **Manual**. If you switch to **Manual** yourself, Kepler also keeps the current order, so no task changes place.

If the view already has a saved **Manual** order, a drop under another sort would replace it. Kepler asks first, in a popover beside the dropped task: *Replace your Manual order?* To keep the move, choose **Switch and replace Manual**. To put the task back, choose **Cancel**, press **Escape**, or click away.

<figure style="text-align:center">
  <a href="/wp-content/uploads/manual-sort-replace-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/manual-sort-replace-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Tasks view after Upgrade the payment SDK was dropped at the top of Unread while sorted by Updated: the View button already reads Inbox and Manual, the dropped row shows its drag grip and Star button, and a popover beside it asks Replace your Manual order? Keeping this move switches the sort to Manual and saves the list in the order you see now, with Cancel and Switch and replace Manual.">
  </a>
  <figcaption style="text-align:center; color:#888">Kepler asks before a drop replaces your saved Manual order.</figcaption>
</figure>

While Kepler reads a view's Manual order, the list reads *Loading your Manual order…*, and a drop is refused with *Unable to reorder until this view's order loads*. If the order cannot be read, Kepler says *Unable to load this view's order* (*Dropped tasks go back until it loads.*), with **Retry**.

If a move fails, Kepler shows *Unable to move the task*, and restores the previous sort if the move had changed it.

***

## Set a task's progress

By default, Kepler sets a task's progress stage from its Git branches and pull requests (see [Status](/kepler/kepler-interface#status)). Sometimes Git and the pull requests do not show what you know. For example, a review was sent back, or the work was merged somewhere Kepler cannot see. In those cases, set the stage yourself.

<figure style="text-align:center">
  <a href="/wp-content/uploads/progress-menu-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/progress-menu-oct-2026.png" class="help-center-img img-bordered" alt="The Progress menu open from Fix the cart total's In Review control, beside its #51 and #38 chips and Changes requested: Automatic, Updates as you work, checked, then Exploration, In Development, In Review, On hold with its submenu arrow, Later, and Done.">
  </a>
  <figcaption style="text-align:center; color:#888">The Progress menu.</figcaption>
</figure>

You can set the stage in these ways:

- **The progress control.** Click the stage name on a task row, in the preview header, or in the task page header to open the **Progress** menu: **Automatic** (*Updates as you work*), then **Exploration**, **In Development**, **In Review**, **On hold**, **Later**, and **Done**. When there is no room for the stage name, the control shows only the stage's icon.
- **The task menus.** A task's **⋮** and right-click menus have the same choices under a **Progress** submenu, plus **Reopen** while the task is Done. Each item's hint says where the task will go (*Moves it to In Review*).
- **Drag a card.** In any grouping, on **List** or **Board**, drag a task's card or row. When grouped by **Progress**, drop it on another stage. On a touch screen, press and hold the card to pick it up. Press **Escape** to cancel the drag. If you drop the card in its own section, Kepler reorders it (see [Put tasks in your own order](#put-tasks-in-your-own-order)). You cannot drag a task that Kepler is still preparing. If you hold the card over another task, Kepler offers to group the 2 tasks (see [Your groups](#your-groups)). If you drag a task that is part of a selection, you drag the whole selection.
- **The Mark as bar.** While you drag, a **Mark as** bar appears over the toolbar with chips for what the card can become: **Read** or **Unread**, the stages, **On hold** and **Later**, **Reopen** for a Done task, and **Archive task**. For an archived task, it shows only **Restore**. Drop the card on a chip.
- **From the keyboard.** When a card has focus on the **Board** grouped by **Progress**, press **Cmd/Ctrl+Shift+←** or **Cmd/Ctrl+Shift+→** to move it 1 column. The card stops at **Exploration** and **Done**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/progress-drag-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/progress-drag-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Board grouped by Progress while Write the 2.4 release notes is dragged from Exploration into In Review: its card stays dimmed in Exploration, the lifted card hangs below Upgrade the payment SDK, In Review is filled and outlined as the drop target, and the other columns, including Later and Done (each reading Nothing here), have dashed outlines. A Mark as bar over the toolbar offers In Development, In Review, On hold, Later, Done and Archive task.">
  </a>
  <figcaption style="text-align:center; color:#888">Dragging a card to another stage, with the Mark as bar over the toolbar.</figcaption>
</figure>

While you drag, the card stays faded in its original place, and a line shows where it would land. Each section that accepts the card has a dashed outline, which becomes solid when the card is over it. Sections that do not accept the card fade, and say why when you hover over them. On the **Board**, a folded column opens after you hold the card over it for half a second.

<figure style="text-align:center">
  <a href="/wp-content/uploads/drag-drop-bar-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/drag-drop-bar-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Fix the cart total lifted off the Tasks view's list. A Mark as bar covers the toolbar with Read, Exploration, In Review, On hold, Later, Done and Archive task; the Unread group has a dashed outline where the card can drop, the card's own row is dimmed in place, and the lifted card floats near the bottom of the list.">
  </a>
  <figcaption style="text-align:center; color:#888">Dragging a task in the List grouped by Inbox, with the Mark as bar.</figcaption>
</figure>

The control's tooltip says whether the stage *Updates as you work* or was *Set manually*.

**How a stage you set works with Git.** Kepler keeps a stage you set until Git and the pull requests catch up with it or change. Then Kepler sets the stage from them again:

- If you set a stage *ahead* of Git and the pull requests (**Done** before the merge, or **In Review** before the pull request), the stage stays until they reach it.
- If you set a stage *behind* them (**Reopen**, or a review sent back to **In Development**), the stage stays until they change in any way. A reopened task therefore still follows its next pull request.
- To return the task to automatic stages sooner, choose **Automatic**, or drop its card on the column that Git and the pull requests already show.

**Reopen** on a task you marked Done returns it to the stage that Git and the pull requests show. If Git and the pull requests show the task as finished, **Reopen** sets **In Development**, and the task's next pull request moves it forward again.

Dropping a card on **Archived** opens the archive confirmation. Dragging an archived card to another section restores the task first. An archived task's control reads **Archived** as a plain label, with no menu.

Agents can also set the stage, put a task on hold until a condition, or set it aside for later, through Kepler's workspace tools. If an agent lifts a hold you placed, it tells you.

### Hold a task, or set it aside for later

**On hold** and **Later** both put a task aside without changing its stage. The task reads **On hold** or **Later** where the stage would be, with a tooltip that says who held it and what its stage was before. Choosing any stage or **Automatic** lifts either one. The task reaching **Done** also lifts it, so a merged pull request ends the hold. A task at **Done** offers neither.

- **On hold** is a pause. The task's agents keep running, and the hold can lift by itself when something happens.
- **Later** sets the task aside with no plan to come back soon. It stops the task's running agents, and keeps their sessions so you can resume them. If an agent is still working, Kepler asks first, *Set aside for later?*, with **Stop and set aside**. **Later** never lifts by itself.

**Hold until something happens.** **On hold** in the **Progress** menu opens a submenu:

| Choice | The hold lifts |
|---|---|
| **Indefinitely** | Only when you lift it |
| **Until CI finishes** | When CI on the task's open pull request finishes. Offered while CI is running on it (otherwise *CI is not running on this pull request.*) |
| **Until a review arrives** | When someone reviews the pull request |
| **Until the pull request merges or closes** | When the pull request is merged or closed |
| **Until another task is done** | When the task you pick from its list (**Search tasks**) reaches **Done** |
| **For 1 hour**, **For 3 hours** | After that long. Each row shows the time it lifts |
| **Until tomorrow**, **Until next week** | At 9:00 the next morning, or at 9:00 next Monday |
| **Until a custom date...** | At the date and time you choose in **Hold until a date and time**, then **Hold task**. The time must be in the future and no more than a year away |

The pull request rows need an open or draft pull request linked to the task. Without one, the menu reads *Link an open pull request to wait on its CI, reviews or merge.* When the task has several, each row names its pull request, for example **Until CI finishes on #51**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/hold-until-menu-nov-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/hold-until-menu-nov-2026.png" class="help-center-img img-bordered" alt="Fix the cart total's Progress menu, opened from its In Review control beside the #51 and #38 chips and Changes requested, with On hold open on its submenu: Indefinitely; Until CI finishes (dimmed), Until a review arrives and Until the pull request merges or closes; Until another task is done; For 1 hour (3:30 PM), For 3 hours (5:30 PM), Until tomorrow (Tue 9:00 AM), Until next week (Mar 9, 9:00 AM); and Until a custom date…. The Progress menu lists Automatic (checked), Exploration, In Development, In Review, On hold, Later and Done.">
  </a>
  <figcaption style="text-align:center; color:#888">The On hold submenu, with the conditions a hold can wait for.</figcaption>
</figure>

While a task waits, its row says what for, for example *On hold until CI finishes on #51*. When the hold lifts, the row says why, for example *Back from hold: CI passed*. The reasons are **CI passed**, **CI failed**, **Approved**, **Changes requested**, **Reviewed**, **Merged**, **Closed**, **Task done**, **Time reached**, and **Condition no longer applies**. A hold that lifts on bad news (**CI failed**, **Changes requested**, or **Closed**) lists the task under **Needs attention**, and any other reason lists it under **Unread**. If the condition is met while Kepler is closed, the hold lifts the next time Kepler checks.

***

## Filter

The **Filters** section at the end of the **View** menu has a submenu for each facet, such as **Progress** or **Provider**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/filter-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/filter-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The View menu's Filters section with Progress open on In Development (ticked, 2), and Exploration (1), In Review (1), On hold (1), Later, Done and Archived (each 0), every value listed with its count. Exploration's exclude button is hovered, and its tooltip reads Exclude Exploration with Shift+Enter. The View button counts 1 filter, the search box shows a 3 hidden pill, and the list behind holds Add product search and Fix the cart total.">
  </a>
  <figcaption style="text-align:center; color:#888">The Filters section, with a facet's flyout open.</figcaption>
</figure>
<figure style="text-align:center">
  <a href="/wp-content/uploads/filter-todo-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/filter-todo-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The View menu on Todo, under the View button reading Type, Updated and Mine: the List and Board switch, the Mine and All scope switch with Mine chosen and Your work, in every org under it, Group by Type and Sort by Updated, then Filters: Needs my attention, Your role, Type, Linked work, Status, Priority, Age and Provider, then a GitHub section with Repository, Assignee and Label, each set to Any. The Provider flyout lists GitHub with its count of 5, and Manage integrations.">
  </a>
  <figcaption style="text-align:center; color:#888">The View menu on Todo. Each connected provider gets its own section, here GitHub.</figcaption>
</figure>

Each type of view has these facets:

| View | Facets |
|---|---|
| **Todo** | Needs my attention · Your role · Type · Linked work · Status · Priority · Age · Provider, then one section per connected provider with its own Repository · Assignee · Issue type · Label · Project · Iteration or Sprint |
| **Tasks** | Progress · Activity · Repository · Agent · Session · Group · Linked work |

Some facets have a fixed set of values that Kepler defines: **Progress**, **Activity**, **Session**, and **Linked work** on Tasks views, and **Type**, **Linked work**, **Needs my attention**, **Priority**, and **Age** on Todo views. Their submenus always list every value, with a count of 0 for a value nothing matches. The other facets list only the values in your work, and Kepler hides a facet that has no values to choose from. For example, if you work in a single repository, the menu has no Repository facet.

**Issue type**, **Label**, **Project**, and **Iteration** use your provider's own values (a Jira issue type, your team's labels, a board name), not Kepler's own names for them. Azure DevOps calls the last one **Iteration** and Jira calls it **Sprint**, so the facet uses each tracker's word.

**Linked work** filters by whether an item is connected to work in the other type of view:

- In Todo, it filters each pull request or issue by its task history: *Has an active task*, *Archived tasks only* (worked on before, but every task is archived), or *No tasks ever*.
- In Tasks, it offers *Has a PR or issue*.

**Activity** matches a task when *any* of its sessions is in that state, so a task with one running session and one unread session matches both **Running** and **Unread**. A task whose terminal program is waiting on you counts as **Waiting**. Its values are **Waiting**, **Error**, **Unread**, **Running**, **Ready**, **Idle**, **Ended**, **Done**, and **Archived**.

**Session** offers *Has a session* and *Has a live session*. To find tasks *without* a pull request, issue, or session, exclude the value.

**Group** lists each of [your groups](#your-groups), including empty ones, and **Ungrouped** for tasks without a group. If a filter still names a group that was deleted or archived, the facet shows it as **Removed group**. When the list is grouped by your groups, the facet also limits which group sections appear.

**Include or exclude any value.** Click a value to include it. To exclude a value instead, hover over it and click its minus button, or press **Shift+Enter** from the keyboard. An excluded value reads *not {value}*. On Todo, excluding a provider's value removes only that provider's items, so excluding a GitHub label never hides a Jira issue.

**Values you include in one facet are combined.** If you tick GitHub *and* GitLab under **Provider**, the list shows items from either provider. Excluded values remove items: Kepler hides an item that matches any of them. A facet with nothing chosen reads **Any** and does not narrow the list.

To find a value in a long facet without scrolling, type in its **Search filters…** box. The menu shows **{count} of {total}** as you narrow the list. The **View** button counts the filters that are on. Hover over the button to see each filter as a chip, with included values in blue and excluded values in red.

To fetch the current view from your providers again, click **Refresh**.

***

## Search

The search box finds items by **title, reference, or repository**. Its placeholder reads *Search title, ref, or repo…*. To find one task, paste its link (**Copy task link**) into the search box. A session's link (**Copy session link**) finds the task that holds the session, including an archived task. While Kepler looks for it, the list reads *Searching...*.

<figure style="text-align:center">
  <a href="/wp-content/uploads/search-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/search-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The search box holding the query the, with a 1 of 5 search pill and a 2 hidden filter pill, each with its own clear button, beside the View button reading Inbox and Updated with 1 filter, and the list toggle at the left.">
  </a>
  <figcaption style="text-align:center; color:#888">The search box, with its search and filter pills.</figcaption>
</figure>

The search box grows as you type, to show what you typed. To have it fill the free space in the toolbar instead, set **Search box** to **Full width** in [Settings → Appearance → Dashboard](/kepler/settings-app#dashboard). In the narrowest window, the search box becomes the **Search the list** icon.

When a search or a filter narrows the list, pills at the right end of the search box show how many rows are left or hidden. Each pill clears only its own search or filters:

| Pill | What it counts | Clicking it |
|---|---|---|
| The search pill | The rows on screen out of every row: *{count} of {total}* | Clears the search |
| The filter pill | The rows your filters hide: *{count} hidden* | Clears the filters |

While a search is on, the filter pill counts only hidden rows that match the search. If a search seems to miss something, the filter pill shows whether your filters are hiding it. Todo loads in pages, so its counts read *40+* or *7+ hidden* until everything has loaded.

When nothing matches, the empty list reads **Nothing matches your search**, or **Nothing matches these filters** when only filters narrow it. It offers a button named for what it resets: **Clear search**, **Clear filters**, or **Clear search and filters**.

Search covers only the work the view has already loaded. On a Todo view, that is the work its scope lists (see [Choose what a Todo view lists](#choose-what-a-todo-view-lists)), so when a search on Todo finds nothing, the list adds *Todo only searches work related to you.* To learn what each integration lists, see [The Dashboard's views](/kepler/kepler-interface#the-dashboards-views).

***

## What Kepler remembers

Each view keeps its layout, grouping, sort, filters, and, on Todo, its scope, in every window and across restarts. Kepler also remembers, for each view in each window:

- **The search text.**
- **Which panels were open**, including pinned panels. If you switch to another view and back, the panels you were reading are still open. A pin stays with the view you pinned the panel in.
- **The panel layout**, panel widths, the list's width, and whether the list is hidden.
- **Folded sections**, for each grouping, across restarts.
- **Where you scrolled to.**

After a restart, each window reopens on the view it was showing, with that view's panels and their widths. The window's other views start with no panels open.

***

## Archive, restore, and clean up in bulk

**Archive task** puts a task away. The task moves from its current section to **Archived**, its sessions and resources are kept, and Kepler stops its running agents. Their sessions are kept, so you can resume them later. When archiving would stop an agent that is working or waiting on you, the confirmation says so: *Stops {count} running agents. Their sessions are kept.* With **Also delete worktrees** ticked, archiving ends every agent of the task, and the confirmation reads *Ends {count} running agents.*

<figure style="text-align:center">
  <a href="/wp-content/uploads/archive-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/archive-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Task actions menu open from Fix the cart total's ⋮ button, beside the task list and the row's Star button: Open task page; Progress, In Development, Mark as read and Star; Rename task and Add to group; Manage resources and Refresh; Copy task link and Copy task prompt; then Shut down all agents, Archive task and Delete task.">
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

To archive, restore or delete several tasks at once, click **Select** on a section header in a Tasks view. That part of the header becomes a bar with a select-all box, **{count} selected**, and icon buttons for the actions, each named in its tooltip. The section's rows show checkboxes. You can select in 1 section at a time, and while you select, clicking a row ticks it instead of opening its panel. A task that Kepler is still preparing has no checkbox, and select-all skips it.

The bar has these buttons:

| Button | What it does |
|---|---|
| **Archive** | Archives every selected task that is not already archived |
| **Restore** | Replaces **Archive** when every selected task is already archived |
| **Delete** | Deletes the selected tasks permanently |
| **Cancel** | Ends selection and clears the selection |

**Archive** and **Delete** both ask you to confirm, with **Archive tasks** or **Delete tasks** as the confirm button. Both offer **Also delete worktrees**, **Also delete branches**, and **Also delete the branch on the remote**. Deleting cannot be undone, and the confirmation says so. Like the single-task dialog, the batch **Archive** confirmation says how many running agents the archive stops (*Stops {count} running agents. Their sessions are kept.*), or, with **Also delete worktrees** ticked, how many it ends (*Ends {count} running agents.*). The batch confirmation differs from the single-task dialog in 2 ways:

- The single-task dialog remembers what you ticked last time. The batch confirmation always starts with all 3 boxes unticked.
- The batch confirmation does not list what will happen to each worktree. Instead, Kepler keeps any worktree that would lose work, and a message afterwards says which ones and why. To see the list before you confirm, use the task's own **⋮** menu.

### Act on several tasks at once

The tasks you open with **Shift**-click or **Cmd/Ctrl**-click (see [Open a panel](/kepler/kepler-interface#open-a-panel)) are also a selection you can act on. While 2 or more tasks are selected, right-clicking or dragging any one of them acts on all of them. Right-clicking or dragging a task outside the selection acts on that task only. A row's **⋮** always acts on its own row.

Right-clicking inside the selection opens a selection menu instead of the task menu. Each item shows how many tasks it acts on: **New group with {count} tasks…**, **Add {count} tasks to group**, **Remove {count} tasks from group**, **Archive {count} tasks**, **Restore {count} tasks**, and **Delete {count} tasks**. Kepler leaves out items with nothing to act on, and the group items skip archived tasks. While the menu is open, the rows it acts on are outlined. **Archive**, **Restore**, and **Delete** open the same batch confirmation as a section's **Select** bar, including the line about running agents.

Dragging a selected task drags the whole selection. Each drop target says how many of the tasks it accepts (*2 of 3 tasks*). After the drop, Kepler reports how many tasks moved and how many stayed where they were. Under the **Manual** sort, the tasks land together as one block.

To clean up worktrees and local branches instead of tasks, open **Settings → Repositories** and choose **Manage worktrees and branches**. The **Worktrees and branches** page lists every worktree, and every local branch that no worktree has checked out. You can filter the list by **Safe to delete**, **Needs update**, **Conflicts**, **Stale**, or **All**. On this page, you can:

- **Update** several worktrees at once, which brings each branch up to date with its base.
- Delete worktrees and branches, including their copies on the remote.

See [Settings](/kepler/settings-repositories#worktrees-and-branches).

---
