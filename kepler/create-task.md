---
title: Create a task
description: Start a task from an issue, a pull request, or nothing at all, with the repository, branch, and context already attached.
product: Kepler
feature: Tasks
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
tags: [tasks, create-task, composer, worktrees, branches, folders, issues, pull-requests, actions, gitlens, gitkraken-desktop]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

You can start a task in 5 ways. The shortest starts from work that is already assigned to you:

| Start from | How |
|---|---|
| **Work assigned to you** | Run an Action on an issue or pull request in the **Todo** view of [the Kepler interface](/kepler/kepler-interface). One click starts the task with its context attached |
| **Something you're describing yourself** | **New task** opens the **New task** composer, where you write the prompt and attach what it needs |
| **A conversation you already started** | **Open an external session**, under the **New task** composer, wraps a task around an agent session you began in your own terminal |
| **Workspaces in another agent app** | **Import from another app** brings workspaces from Conductor, Orca, herdr, or Vibe Kanban in as tasks, with their branches and chats |
| **Another GitKraken app** | A link from GitLens or GitKraken Desktop opens Kepler on the work you were looking at |

***

## From an issue or pull request

<figure style="text-align:center">
  <a href="/wp-content/uploads/action-button-todo-row-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/action-button-todo-row-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="The right end of a Todo issue row: acme-web, Open, the age 3d, and the Plan Action button at rest as an outline, its chevron on the right opening the list of Actions.">
  </a>
  <figcaption style="text-align:center; color:#888">The Action button on a Todo row, at rest.</figcaption>
</figure>

Starting from an issue or pull request is the shortest path. Find the item in **Todo** and click its **Action** button. Kepler then does the following:

1. Creates the task.
2. Attaches the repository and the item.
3. Sets up a worktree.
4. Starts an agent with the context in place.

The default Action depends on the item:

- **Plan** for an issue.
- **Address Feedback** for a pull request you authored.
- **Review** for someone else's pull request.

You can edit all of these Actions. To read an Action's prompt, open the list under the button's chevron and hover the Action. See [Actions](/kepler/actions).

Kepler names tasks automatically from what you started them with. To rename a task, use **Rename task** in the **⋮** menu, whose field also has an **Auto-name** button that suggests a name from the task's prompt and resources. See [Tasks and Resources](/kepler/tasks-and-resources).

<div class="note" markdown="1">

**Nothing in Todo?** Set up your [issue tracker](/kepler/issue-tracker-integrations) and [pull request](/kepler/pull-request-integrations) integrations in **Settings** first. **Todo** shows work only from connected accounts.

</div>

***

## From the New task composer

Click **New task** or press **Cmd/Ctrl+N**. To start one without switching to Kepler first, press **Shift+Alt+N** to open the quick launcher from anywhere, including when Kepler is not the focused window.

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-button-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-button-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The New task button at the left end of the Kepler top bar, a single button with a plus sign, after the application menu, the window switcher and the Back and Forward buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">The New task button, available from anywhere in Kepler.</figcaption>
</figure>

The **New task** composer is a prompt box above a row of 4 buttons:

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-composer-add-buttons-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-composer-add-buttons-sep-2026.png" class="help-center-img img-bordered" alt="The New task composer's four buttons: Add repo or folder, Add issue, Add PR, and Add context">
  </a>
  <figcaption style="text-align:center; color:#888">The New task composer's four attach buttons.</figcaption>
</figure>

| Control | What it attaches |
|---|---|
| **Add repo or folder** | A repository to work in, or a plain folder |
| **Add issue** → **Issues** | Issues from your connected trackers. For Linear, pick a team or **Project** to list everyone's open issues, not just yours |
| **Add PR** → **PRs** | Pull requests from your connected hosts |
| **Add context** | Files and links the agent can read. A folder to work in goes through **Add repo or folder** |

Each picker lists what you have already attached of its kind, where you can also remove it.

**Paste a link to attach it.** Paste a pull request or issue URL into the prompt, from a connected host or from Jira or Linear, and it becomes a chip naming the item. The chip attaches the item the same way **Add issue** or **Add PR** would, along with its repository, so a pull request from another repository launches in that repository, on its branch. If the repository is not in Kepler yet, Kepler clones it when the task starts.

A repository you pick yourself takes precedence over the link's. If Kepler cannot read a link, the composer says so, and the agent gets the link to continue from.

In a window connected to another machine, picking a file through **Add context** also offers **Upload from this machine**. Uploads are saved into the task's own folder when it starts.

**Repositories and folders share 1 list**, with the places you use most at the top.

You can attach as much or as little context as you want. To create a task from the composer, follow these steps:

1. Write the prompt: *Describe a task or ask a question…*
2. Attach what the prompt needs. You can also attach nothing.
3. If you attached a repository, configure it. See [Configuring a repository](#configuring-a-repository).
4. Click the primary button, such as **Start**.

**The composer remembers the repositories you last started a task with** and stages them again the next time you open it. The branch and worktree settings reset to their defaults.

**The composer also remembers an unsent draft.** If you close the dialog with a prompt half written, the prompt is still there when you reopen it. Kepler asks before it discards a draft.

**Kepler also remembers which repository you pick for a tracker project.** When you pick a Jira, Linear, or Azure issue, its **Repository** chip holds the repository you used for that project before. To use another repository, or **No repository**, choose it from the chip's menu.

The primary button runs the Action that matches what you've attached, exactly as it would from a Todo row. A linked pull request resolves to **Address Feedback** or **Review**, depending on who wrote it; a linked issue resolves to **Plan**. With nothing attached, the button reads **Start** and starts the task with your prompt as written.

To keep **Start** when you link an issue or pull request, turn the switching off: click **Turn off** in the note the composer shows the first time it switches, or turn off **Suggest automatically** in [Settings → Actions](/kepler/settings-actions).

The chevron beside the primary button lists the other choices: **Prepare**, which creates the session without starting work yet, and every Action that applies to what you've attached. Picking one there does not run it. Instead, it relabels the primary button, and an Action that names its own agent puts that agent in the agent pill. You can then check or change what will run before you press the button. To pick an Action and run it at once, hold Cmd/Ctrl as you click it. The Action sends its prompt, with anything you typed added as a refinement.

**Shift+Tab** in the prompt cycles the primary button through the same list.

A task that has its prompt but no session yet, such as one an agent created for you, opens a draft session tab. To send the task's prompt as written, press **Start** on the empty box.

The task appears in the list as soon as you press **Start**, with a **Preparing** pill until setup finishes. The task's panel and the task page show each launch step. **Cancel** stops a launch while Kepler is reading a link or cloning a repository.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ade-task-preparing-row-01-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ade-task-preparing-row-01-v2@2x.png" class="help-center-img img-bordered" alt="The Recent group of the Tasks view: Write the 2.4 release notes, then a new task, Add a gift-card field to checkout, with acme-web, the Preparing pill and its spinner.">
  </a>
  <figcaption style="text-align:center; color:#888">A new task in the list while Kepler prepares it.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/task-launch-kep-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/task-launch-kep-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The side panel of a task that is starting, Add a gift-card field to checkout, marked Preparing. Kep, the Kepler mascot, sits above the line Making your worktree. So your other work stays put. Below it, the launch steps list Setting up worktrees… (current), Starting OpenCode with your prompt and Opening the chat.">
  </a>
  <figcaption style="text-align:center; color:#888">Kep narrating a task's launch in its panel.</figcaption>
</figure>

If setup fails, the row's pill reads **Failed** and the panel shows the error. To change the task and try again, click **Edit and retry**, or **Dismiss** to clear it. If it failed because a repository or folder is not trusted, the panel says so: click **Trust and retry**. A task that starts without some of its repositories warns you which ones it left out. When they were left out because they are not trusted, the warning offers **Trust**. See [Trust a repository](/kepler/settings-repositories#trust-a-repository).

If the task starts but its agent session does not, the task page and the Dashboard panel say that the agent was unable to start, with **Retry**. See [Agent Sessions](/kepler/agent-sessions#when-a-session-drops).

### Configuring a repository

Each attached repository gets a chip with 3 segments:

<figure style="text-align:center">
  <a href="/wp-content/uploads/composer-repo-chip-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/composer-repo-chip-sep-2026.png" class="help-center-img img-bordered" alt="Two repository chips, each with its base branch, an editable branch name, and the Isolated worktree checkbox">
  </a>
  <figcaption style="text-align:center; color:#888">A repository chip, with its base branch and Isolated worktree controls.</figcaption>
</figure>

- **Base branch**: by default, the task gets a new branch from **the repository's remote default branch**. Open the segment to branch off a different branch, to work directly on an existing one, or to take the repository's **current** branch in place.
- **Branch name**: the new branch's name, suggested from your prompt as you type. Click it to edit it. See [Naming the branch](#naming-the-branch).
- **Isolated worktree**: an on/off toggle, on by default, that gives the task its own working copy. Turn it off to have the task share your repository folder, so a branch switch there moves your checkout. See [Tasks and Resources](/kepler/tasks-and-resources#worktrees-and-working-in-place).

**What a newly attached repository starts on is a setting.** The 3 segments start from **Settings → Tasks → New tasks → Where new tasks make changes**: **Isolated worktree** (the default), **New branch**, or **Current branch**. The setting changes only the starting point. You can still change every segment for each repository in each task. See [Settings](/kepler/settings-tasks#where-new-tasks-make-changes).

Picking **New branch** or **Current branch** means the task runs in the repository's own checkout rather than an isolated one, so only 1 task can use that checkout at a time. If another task already has it, the chip says **Another task is working here** and names it. Click **Create a worktree for this task** to put this repository in an isolated worktree instead.

### Naming the branch

Kepler names a task's branch from what the task is about, rather than from the task's name alone:

- **The name is suggested from your prompt** and appears on the chip as you type. Click it to edit it: **Enter** keeps your name, and **Esc** restores the suggestion.
- **An issue identifier leads the name** when the task came from one, such as `KEP-421-fix-the-import-path`.
- **Automatic names are namespaced under `kepler/`.**
- **A name you type is yours verbatim.** The prefix applies to automatic names only.
- **Kepler applies your repository's own branch-naming policy** where the host publishes one.

You can set the prefix in 2 places: **Settings → Tasks → New tasks → Branch prefix** for the app, and per repository in **Settings → Repositories**, on the repository's own page. The repository's page offers **Default (*prefix*)**, **None**, or **Custom**, and shows an example branch name. Leave the app setting empty for no prefix at all.

A repository linked to a pull request always opens in its own isolated working copy, and the toggle is locked. Kepler never overwrites a local branch that has commits the pull request does not: it starts the task on a new branch that tracks the pull request.

When the task starts, Kepler clones a repository you have not cloned yet into your **Repositories folder**. Until then, you cannot pick its branch.

Attaching the same repository twice gives the task 2 independent worktrees on it, for example to compare 2 approaches. Two chips that would end up in the *same* worktree are marked **Duplicate worktree**, and Kepler creates only 1 of them.

***

## From a session you already started

If you started work with an agent in your own terminal, you can track that conversation in a task. Under the **New task** composer, and on an empty tasks list, **Open an external session** switches the composer to a list of every agent conversation Kepler can see. **Start a new task** switches back. **Open an external session** appears only while external session detection is on.

<figure style="text-align:center">
  <a href="/wp-content/uploads/continue-external-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/continue-external-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The New task launcher flipped to Open an external session: a Find an external session… search field over Past sessions, listing the Pi session Why do product search results miss items tagged in uppercase? in …/repositories/acme-web, highlighted with Continue. Below the panel, Start a new task switches back to the composer.">
  </a>
  <figcaption style="text-align:center; color:#888">Opening an external session from the New task composer.</figcaption>
</figure>

| Part | What it does |
|---|---|
| **Live now** | Sessions live in a terminal right now |
| **Past sessions** | Conversations found on disk, from any time |
| **Find an external session…** | Searches across both groups |

Pick a conversation to continue it in a new task:

- A past conversation resumes.
- A live conversation opens read-only in its task, so you can follow it while it keeps running in your terminal. Once the conversation is idle, close it in your terminal, then click **Continue here** in the session to continue it in Kepler.

### When a task already covers that folder

When the conversation's folder already belongs to a task, Kepler asks under the list. **Add it to that task** adds the conversation to that task, and **Make a new task** creates a new one anyway.

Starting a task from an external session anywhere else, such as from a Kepler link, asks the same question in the **Add to existing task?** dialog. **Add to task** adds the conversation to the task you pick, and **Create a new task** creates a new one anyway. When several tasks include the folder, the dialog marks the **closest**.

For what happens to the conversation once it's on a task, including forking, continuing, and what Kepler will and will not answer on its behalf, see [Agent Sessions](/kepler/agent-sessions#sessions-started-outside-kepler).

***

## From another agent app

If you work in Conductor, Orca, herdr, or Vibe Kanban, you can bring its workspaces into Kepler as tasks. Each workspace becomes a task in the same folder, on the same branch, and its chats continue as the task's sessions. From Conductor, Kepler imports the workspaces the Conductor app keeps on your Mac, not Conductor Cloud workspaces.

To import workspaces from Conductor, take the following steps:

1. On an empty **Tasks** list, click the import card. It names the apps Kepler found, such as **Import from Conductor, Orca and 2 more**. You can also choose **File → Import from Another App…**.
2. If Kepler finds more than 1 app, click **Conductor**.
3. Tick the workspaces you want, and click **Import *N* workspaces**. A workspace you already imported is marked **Already a task**.
4. When **Import finished** shows what came over, click **Done**.
5. Find the new tasks in **Tasks**. Open one to pick its chat up where it left off.

<figure style="text-align:center">
  <a href="/wp-content/uploads/import-card-nov-2026@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/import-card-nov-2026@2x.png" class="help-center-img img-bordered" alt="Two cards below an or divider: Import from Conductor, Orca and 2 more, reading Bring in your workspaces as tasks, with their branches and chats, and Open an external session.">
  </a>
  <figcaption style="text-align:center; color:#888">Step 1: the import card names the apps Kepler found.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/import-choose-app-nov-2026@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/import-choose-app-nov-2026@2x.png" class="help-center-img img-bordered" alt="The Import from another app dialog, Choose the app to bring workspaces in from, listing Conductor, Orca, herdr and Vibe Kanban.">
  </a>
  <figcaption style="text-align:center; color:#888">Step 2: picking the app to import from.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/import-workspaces-nov-2026@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/import-workspaces-nov-2026@2x.png" class="help-center-img img-bordered" alt="The Import from Conductor dialog, Choose the workspaces to bring in as tasks, listing 4 ticked workspaces grouped by repository: Checkout redesign and Gift card support under acme-web, Order search endpoint under acme-api, and Apple Pay on mobile under acme-mobile, each with its branch and number of chats. The note to continue each chat in one app only sits above Back to apps and Import 4 workspaces.">
  </a>
  <figcaption style="text-align:center; color:#888">Step 3: choosing the Conductor workspaces to import.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/import-finished-nov-2026@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/import-finished-nov-2026@2x.png" class="help-center-img img-bordered" alt="The Import finished dialog for Import from Conductor, reading 4 workspaces became tasks and 6 chats resumed, with Back to apps and Done buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">Step 4: the import is finished.</figcaption>
</figure>

<figure style="text-align:center">
  <a href="/wp-content/uploads/import-tasks-nov-2026@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/import-tasks-nov-2026@2x.png" class="help-center-img img-bordered" alt="The Tasks view listing the 4 imported tasks under Recent: Apple Pay on mobile, Order search endpoint, Gift card support and Checkout redesign, each with its repository and In development status.">
  </a>
  <figcaption style="text-align:center; color:#888">Step 5: the imported workspaces in Tasks.</figcaption>
</figure>

Continue each chat in one app only: both apps write to the same chat history.

***

## From a folder, or from nothing at all

**A task does not need a repository.** Attach a plain folder from **Add repo or folder**, and the agent works on it in place, with no branch, no worktree, and no Git at all. A folder of notes or a scratch directory works as a normal task.

When you browse for a folder in a window connected to another machine, Kepler opens its own folder picker. To use this picker everywhere, turn on **Always use the custom folder picker** in **Settings → General**. When you type a path into it, Kepler checks the path and, for a path close to an existing folder, offers **Did you mean** with the closest folder.

You can also attach nothing at all: no repository, no folder, and no issue. Use a task like this to ask a question or explore an idea, and attach the real work later, once it's worth tracking. See [The Task View](/kepler/task-view).

<figure style="text-align:center">
  <a href="/wp-content/uploads/new-task-composer-sep-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/new-task-composer-sep-2026.png" class="help-center-img img-bordered" alt="The New task composer with a prompt typed in and Add issue, Add PR, Add context, and Add repo or folder buttons, nothing attached yet">
  </a>
  <figcaption style="text-align:center; color:#888">The New task composer, ready to attach a repo, issue, pull request, or other context.</figcaption>
</figure>

***

## From another GitKraken app

You can open Kepler from other GitKraken products, such as GitLens and GitKraken Desktop. A link from one of them can do the following:

- Open the **New task** composer already filled in with the issue, pull request, or repository you were looking at.
- Open a task or session you already have.
- Put a prompt and an Action in the composer.
- Start a new session on a task you already have.
- Start right away rather than waiting for you to press **Start**.

For an item that a task already holds, Kepler offers **Open task** instead. If the repository is not on this machine, Kepler clones it when the task starts. A link that Kepler cannot fully resolve still opens, with a warning about what Kepler could not use.

### Which window a link opens in

Kepler sends each link to the window that can use it:

- A link for a task opens in the window already showing that task.
- A link that names a saved remote machine opens in a window on that machine. If none is open, Kepler opens one.
- Any other link goes to the window you used last.

If a link cannot open on the machine it names, it opens on this computer instead, a notice says so, and nothing it asked to start runs on its own. In a window on a remote machine, a link for something that is not there offers **Open on this computer**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/deeplink-offhost-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/deeplink-offhost-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Kepler after a link meant for dev-server opened on this computer: the New task composer is open with the prompt Fix the cart total rounding, and a notice at the top right reads Unable to open on dev-server, It opened on this computer instead.">
  </a>
  <figcaption style="text-align:center; color:#888">A link for a remote machine that opened on this computer instead.</figcaption>
</figure>

***

## After the task starts

The task appears in the **Tasks** view right away, with the **Preparing** pill until its setup finishes. Click it to open its side panel, or double-click it to open [the task page](/kepler/task-view).

<figure style="text-align:center">
  <a href="/wp-content/uploads/full-task-view-oct-2026-v2.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/full-task-view-oct-2026-v2.png" class="help-center-img img-bordered" alt="The task page, its header holding the task name, the ⋮ menu, the In Development progress control, and Terminal at the right edge. The context panel lists Sessions, Changes, Pull requests, and Notes led by Prompt, and a session on the right is waiting on a command approval.">
  </a>
  <figcaption style="text-align:center; color:#888">The task page, with the context panel beside an open session.</figcaption>
</figure>

From there you can add more sessions, attach more resources, and review what the agent changed. See [Agent Sessions](/kepler/agent-sessions) and [Review Changes](/kepler/review-changes).

### Context: what gets handed to the agent

Starting from **Todo** and starting from the **New task** composer send the same Action prompt, but they attach different amounts of detail:

| Started from | What the agent receives |
|---|---|
| **A row in Todo** | The full issue or pull request body, attached as shared context |
| **The New task composer** | A reference (identifier, title, and URL) which the agent fetches the detail from itself |

Either way, Kepler saves each linked issue's description as a note titled with the issue's identifier and title; long descriptions are shortened with a link to the issue. Kepler does not save pull request descriptions this way.

---
