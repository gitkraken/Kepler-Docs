---
title: Kepler 0.x
description: View the latest features, improvements, and fixes shipping in the current version of Kepler.
product: Kepler
feature: Release Notes
content_type: release-notes
audience: all
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [release-notes, changelog, whats-new, upgrades, version-history]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Kepler is GitKraken's **Agentic Development Environment (ADE)**: one place to direct coding agents across every issue and pull request assigned to you, in as many repositories as you need, at the same time. You bring the agent; Kepler attaches the context and carries the result through to a reviewed, mergeable change.

This release notes page tracks what's new and changing in the current version of Kepler, including new features, improvements, bug fixes, and breaking changes. Use it to see what shipped in the most recent release, confirm when a capability became available, or review changes before upgrading.

**Requirements and limits**

- This page covers the current version line of Kepler, 0.x. Archived version pages will be listed here as later lines ship.
- Each entry applies only to the specific release listed under its version heading.
- Kepler is in public preview. A free GitKraken account is all you need to run it, though a few capabilities, such as [Remote Access](/kepler/remote-environments), require a paid GitKraken plan.
- Kepler updates itself. You're prompted to restart when a new version is published, and **Check for Updates** in the app menu asks straight away.

<a href="https://www.gitkraken.com/kepler/download?source=help_center" target="_blank" class="button button--basic ">Download Current Version Now</a>

New to Kepler? [Getting Started with Kepler](/kepler/kepler-getting-started) takes you from install to your first agent-run task.

***

<a id="v0-12-0"></a>
## Version 0.12.0

<kbd>Wednesday, October 7th, 2026</kbd>

### Highlights

- **More issue tracking and pr integrations.** Jira Server and Data Center join the Bitbucket and Azure DevOps servers added in 0.11.0. Bitbucket and Azure DevOps pull requests waiting on your review now show up, and Jira descriptions render with their images and wiki markup.
- **Save your Dashboard views.** Save a combination of segment, search, grouping, filters and layout under a name, and switch back to it from the Saved views chip next to the search box.
- **Manually update task progress.** Drag a task between Exploration, In Development, In Review and Done, or put it On hold. Kepler moves a task to Done only once its branches have landed, including rebase- and squash-merged ones, and your agents can set the stage too.
- **Review, edit, commit and resolve conflicts in Kepler.** Leave review comments on diff lines, then drop them all into your agent's prompt in one step. Amend the last commit, resolve merge conflicts from the file tree, and change a branch's merge target or compare against a different one.
- **Control your agents' MCP servers.** Kepler lists the MCP servers each agent loads. Add or remove servers, sign in or out, and turn a server or a single tool on or off for one repository from the composer's agent menu. Set the defaults for every repository in Settings › Agents › MCP servers.
- **Pick up where you left off after a usage limit.** Sessions resume and send queued prompts on their own when a usage limit resets. The usage meter shows each session's 5-hour and 7-day limits and when they lift.
- **Open any file from a task.** A new file viewer opens code at a line, renders Markdown, images and SVG, and updates when the file changes on disk. Open a file path an agent writes straight from the chat, and upload files from your computer to a task.

### Features

#### Task progress

- Set a task's stage yourself: drag its card between Progress columns, move it from the keyboard, or pick a stage from the progress control and task menus.
- Put a task On hold, with its own Inbox group. The hold lifts when the task reaches Done, and archived tasks show in the Progress view.
- A task's pull requests and issues refresh on their own when an agent ends a turn, a branch is pushed or a pull request is published.
- Kepler suggests archiving a finished task, and the archive dialog shows what happens to each worktree, keeping risky ones unless you confirm.

#### Files

- Open any file in a new file viewer from File › Open File… and Go to File…, or as a tab on the task page: code at a line, Markdown with Preview and Source, images and SVG.
- An open file updates in place when it changes on disk, and can show what changed since you opened it.
- Open a file path an agent writes straight from the conversation.
- Upload files from this computer in Add resources. Uploads belong to the task, show in Files with a Delete action, and can be saved to disk.
- The folder picker was rebuilt around a path bar that checks what you type.

#### Changes and commits

- Comment on diff lines and files, and send the comments to the composer.
- Amend the last commit from the commit box, which now looks like the prompt composer, waits for staging and shows hook output.
- Resolve merge conflicts and delete files from the file tree. Deleted and discarded files go to the Trash first.
- Change a branch's merge target from its chip or the task menu, or compare against a temporary target in the Changes overlay and worktree panel.
- Kepler notices a branch that landed in its target without a pull request, and picks up merge targets changed in GitLens.
- Large untracked folders show as one entry with a file count.

#### Chat

- Copy a prompt or a reply, start a new session from any message, and save images from thumbnails and the lightbox.
- Each message shows when it was sent, with dividers for long gaps.
- Agent thinking shows as a collapsed block, and permission prompts say why the agent is asking.
- Preview a published Claude artifact beside the chat, and choose whether artifact comments start new turns.
- See Claude Code background tasks in idle sessions and stop one from its card.

#### Usage limits

- Sessions resume and send queued prompts on their own when a usage limit resets.
- The usage meter shows a session's own 5-hour and 7-day limits, when a limit lifts and how old the reading is, with a Refresh button.
- See a session's prompt-cache expiry and hit rate, and how long it has been since the model last replied.
- The terminal status bar was reworked around the session and its usage.

#### Remote

- Forward an SSH remote's ports to this computer from a link click or the Ports list. The remote chip shows forwarded ports, and localhost links in a task open through forwarding.
- Reopen the last closed remote window on its host, and peek at your connections by hovering the remote chip.
- An experimental setting loads remote windows' interface from this computer.

#### Dashboard

- Save a set of filters and view settings as a named view.
- A full-width Worktrees view shows each worktree's tasks, agents, pull request and base, and bulk cleanup can clear stale locks.
- The task preview's worktree row is a two-row pill you can step through, and the title shows an unread dot and the task prompt on hover.
- Press Start on an empty box to start a task with its prompt.

#### MCP servers

- Manage MCP servers inside Kepler, from the composer's agent menu or Settings › Agents › MCP servers, including sign-in and sign-out.
- Kepler warns when Claude sessions stop reporting to it, with a Repair action.

#### For your agents

- Agents can set their task's stage, put it on hold, and refresh its pull requests and issues.
- Agents know their related tasks and who started them, can message the sessions they started without asking, and attach the dev servers they start to the task.

#### Smaller additions

- Jira Server and Data Center are supported, Jira images and wiki markup render in descriptions, and you can pick a Linear team when adding issues.
- Swipe with a trackpad or Magic Mouse to go back and forward.
- Right-click a dropdown to open its menu, and walk the branch picker with the arrow keys.
- Save logs as a zip from Settings › Help › Logs, or show them from the Help menu.

### Improvements

#### Performance

- Dashboard navigation is instant with side panels open, and only the parts an update changes re-render.
- Large diffs open fast.
- Pull requests and issues load for what is on screen instead of whole-account lists.
- Busy terminals no longer flood windows that can't keep up, and the app no longer freezes on process, PATH, SSH or Keychain lookups.
- New worktrees check out faster on Windows.

#### Interface

- Tooltips say what a click does, show shortcuts under the title, and open below their trigger.
- Split buttons share one keyboard model with a visible focus outline, and Tab moves from the prompt to Send.
- The agent menu is grouped by agent, and an empty one explains why and offers the fix.
- Headers, toolbars and the composer footer fit the window as it resizes.
- Unsent composer drafts survive a reload.
- Each pull request and issue state has its own icon and colour, and open buttons name the provider.

### Fixes

#### Agents and terminals

- A session no longer loses its conversation or retries forever when its background process dies, and shows a reconnecting overlay while Kepler reattaches.
- An effort or mode changed inside a terminal CLI survives relaunches, and a terminal follows Claude when it continues under a new conversation.
- Terminal pastes and sends no longer wait forever, and the input pause explains itself and waits for Continue.
- Wrapped URLs and file paths stay clickable on every row, and Codex can copy to your clipboard from a remote window.
- Codex API-key and remote ChatGPT sign-in work, a signed-in Cursor CLI shows as signed in, and Codex capacity errors are explained.
- A terminal or external session blocked on a prompt notifies you, for every agent.
- Model lists refresh after an agent is upgraded or signed in.

#### Git and worktrees

- Rebase- and squash-merged branches show as merged, cleanup no longer warns their commits will be lost, and unpushed commits are counted before a worktree is deleted.
- Kepler's fetches no longer break a git pull you run at the same time, and creating a worktree no longer times out.
- Edits to a symlinked file save to its target, and Escape never discards an unsaved inline edit.
- A task reaches Done only once its own branches have landed, including a diverged branch whose pull request merged.

#### Providers

- Linear no longer lists Done and Canceled issues, and canceled issues are no longer shown as completed.
- Azure DevOps and Bitbucket Data Center pull requests you review and Bitbucket Cloud review requests now show up.
- Images in issue and pull request previews load, and merged pull requests keep their details.
- An unreachable provider server shows as unreachable instead of signed out, and GitHub organizations that block Kepler are named.

#### Remote

- A remote window keeps its page when its connection is rebuilt, and the first remote window opens in place.
- A re-verified host key is saved with the host in one step, and a new address on a saved host gets its key checked.

#### Interface

- Escape closes only the top layer, overlays over a dialog scroll, and toasts stay clickable while a dialog is open.
- A sideways scroll or mouse wheel no longer goes Back.
- "3m ago" labels keep updating.
- Dictated text is kept after a segment finishes transcribing.
- Kepler trusts certificates installed in your system's certificate store.

***

<a id="v0-11-0"></a>
## Version 0.11.0

<kbd>Tuesday, September 29th, 2026</kbd>

### Features

#### Agents that keep running

- Agents and terminal sessions now run under a supervisor that keeps them alive through a Kepler restart or update, and recovers them when Kepler comes back. A new switch in Settings turns it on or off.
- Kepler warns before an update only for the agents it would actually interrupt, and Quit & End Sessions ends them on the way out.
- A detached agent that has produced no output for an hour is ended on its own.
- A terminal session resumes after a reboot, keeps its keyboard and paste modes across a restart, and keeps running through a context compaction.

#### The task page and Dashboard previews

- Tabs on the task page are now free-form: drag them into groups and splits, with terminals listed after Changes in the rail.
- Every open Dashboard preview gets its own column, up to 16, with a placeholder until its item loads. Panel widths are remembered across reloads and segment switches.
- Maximize one preview over the others, restore it with a click outside, and reorder panels by dragging their headers or from the panel menu.
- Resize every panel at once with a Shift-drag, and scroll the strip with Shift+wheel or a sideways swipe, even over a terminal.
- Preview headers were rebuilt, and can collapse for a pull request or an issue. The task page header matches.
- The task's prompt is a context item of its own, shown in the rail, the card and the preview, and a new session can start without the task's context.
- Start a session on another branch from the New session menu, start a new session from an existing one, and name a session yourself.
- Tasks moving to Running stay there for 10 seconds after work stops, so the list stops flickering.

#### Todo and filters

- Filter Todo items by iteration and sprint, and sort the Todo and Tasks lists.
- Exclude a filter value instead of only including it, and see search and filter pills inside the search box.
- Issues show their own provider state, and issues included by mention say so.
- Bitbucket and Azure self-managed servers are supported.

#### Deep links

- `kepler://` links open a pre-filled task composer, open a task or a session, start a session, check out a linked pull request's branch, and can carry a prompt that starts immediately.
- A link that only half-resolves offers a clone, a resume or one clear warning.

#### Remote and hosts

- Remote management moved into Settings. Each saved host gets a colour and can be muted, hosts can be added or edited by hand with WSL on par with SSH, and a startup reconnect failure explains why.
- A host already open in another window is recognised and reached through that window.
- New Window opens on the same connection as the window it came from.
- The connection popover was redesigned, and a connected server can be restarted or updated from the host chip, which says what the update will stop.

#### Terminals and links

- File paths in a terminal are links: relative paths, line suffixes and paths wrapped across lines. Open them in an editor at their line, in the default app, in the Changes viewer, or preview a markdown file rendered.
- A terminal session shows its model, effort and mode read-only in chat.
- Terminals answer a TUI's background-colour query and re-theme a running TUI when you change themes.

#### Chat

- Claude artifacts show as cards and stay attached to the task as links, and `/design` and `/slides` work in chat sessions.
- Open a subagent in its own read-only transcript pane.
- Attach files by path, sending only what the session's host can't already read, and open or reveal an uploaded file from its card.
- A transcript remembers where you stopped reading, and a new autoscroll setting never fights you.

#### Updates and windows

- A ready update is one chip in the top bar with a popover on every screen, and downloads show progress, size, speed and time left.
- Kepler reopens the last closed window where it was, and each window remembers its own layout.
- Back and Forward buttons are in the top bar.

#### Keyboard

- Navigate the Dashboard and task page from the keyboard, switch panels with Ctrl+Tab, rename a task with F2, and move tabs with Ctrl+Shift+PageUp/PageDown.
- Cmd/Ctrl+N opens a new task, Cmd/Ctrl+Shift+N a new window, Cmd/Ctrl+, toggles Settings, and Cmd/Ctrl+Shift+M and Cmd/Ctrl+Shift+J maximize a panel or a terminal.
- Shortcuts now show in menu items and button tooltips.

#### For your agents

- Agents can find the workspace's tasks and sessions, send follow-ups to existing ones, choose the harness of a session they start, archive and restore a task, and add files to a task they create.
- Agents can update a branch from its base with a reviewable rebase or merge, and pass guidance to the conflict resolver.

#### Agents and harnesses

- Antigravity is supported through its ACP server, and OpenCode v1 and v2 work side by side.
- Each agent account can have its own colour tinting the agent icon, and accounts appear on the agent card.

#### Smaller additions

- Edit, reorder and add commands in the repository dialog, with a Variables menu that also appears on default folder fields.
- Open on {provider} at the end of every worktree Open in menu, Open in default app in every file menu, and Delete worktree in the worktree pill menu.
- A Wrap lines toggle on every code view.
- Running commands appear on the run button and its menus.
- The English and Spanish interface now covers the remaining hardcoded copy.

### Improvements

#### Performance

- Typing in the composer and streaming updates no longer slow the session view, and transcripts load without unread tool output.
- The Dashboard re-renders only the rows and panels a change touches, loads the Todo feed only on its segment, and opens previews one per frame.
- Terminals stay responsive on busy sessions: closed views resume by delta, output is batched, and windows only receive output for terminals they show.
- Worktree state is no longer re-read when nothing changed, and the Windows agent start is about 2.5 times faster.

#### Look and feel

- Dialogs were redesigned and every confirm reworded, with Enter running a dialog's primary action.
- Popovers, menus, tooltips and dialogs share a 6px radius, and tooltips open after a slightly longer delay.
- Back arrows are now a left chevron, and ghost buttons sit flush against their container's edge.
- What's New is redesigned around a release hero and a grouped version rail.
- The changes panel and overlay chrome were redesigned, with the worktree strip's controls ghosted until hovered.

#### Agents and MCP

- Kepler says why a first prompt is waiting for you, and warns in Settings when an installed agent's version can't be read.
- Terminal agents disclose how their first prompt is delivered and which workspace tools they get.

### Fixes

#### Agents and terminals

- A terminal session ended cleanly by its CLI is no longer reported as a crash, one blocked on a prompt needs attention, and one stopped during startup can resume.
- Terminal sessions keep their conversations when a task is archived or its worktree goes, and sessions stop cleanly when their worktree is removed outside Kepler.
- Hook-tracked sessions keep running while background subagents work, and held permission prompts go back to the CLI instead of being approved.
- A slash command sent as a session's first prompt runs as a real command.
- Agent CLIs resume after Ctrl+Z, a Codex first prompt is sent on its command line, and a prompt that quotes an install path no longer refuses to launch.
- Claude folder trust is read where the CLI records it, and a worktree inherits it.
- Queued prompts survive restarts and show their attachments.
- Codex Sign out actually signs you out, and Kepler follows a CLI sign-in performed outside it.
- Custom agent server environment values are encrypted at rest.
- Terminal typing stays out of crash reports, and typed input, resizes and closes are delivered reliably.

#### Chat

- Agent messages keep their paragraph breaks, and the scroll-to-bottom control shows while a turn streams.
- A resumed subagent's permission prompt is shown, and session-limit errors are clearer.
- Unread sessions are blue again.

#### Dashboard and tasks

- Closing a deleted task's preview panel no longer shows Task not found, and Back returns to the panels a task launch replaced.
- Preview panels keep their widths through closes, swaps and segment switches, and a divider stays under the pointer while you drag it.
- A background preview panel no longer takes focus on its own, and the strip no longer jumps to a session that asks for input.
- Linked issues and pull requests refresh by identity, resolve in the repository their link names, and Azure DevOps work items resolve correctly.
- Repo-less tasks start sessions in place, and a gone worktree or folder is recreated before a new session starts there.
- Closed worktree columns and the terminal drawer stay as you left them.

#### Remote

- A remote window keeps its route through a server restart or a failed reconnect, and SSH windows to one host share a connection.
- Paste-code sign-in works in remote windows, and a remote daemon stays signed in when another machine sharing it quits.
- WSL messages are no longer garbled, and Docker Desktop's own distributions are left out of discovery.
- The outdated-server error is shown in the app's language and says which side to update.

#### Updates and windows

- The update card stays put once an install starts, background update-check failures no longer toast, and Windows no longer silently accepts a downgrade.
- The About dialog opens in the window whose menu asked for it, and restored windows no longer take focus at start-up.
- The screen can turn off on Linux, and Kepler says when a machine can't be kept awake.
- The Windows agent start no longer flashes a console window.

#### Interface

- Enter in a modal's text field no longer closes the modal.
- Pressed splitters no longer take focus or stay lit after a drag.
- Links in a dropdown no longer crash the menu, and an open popover no longer disables the top bar.
- Code scrolls sideways with a trackpad under one horizontal scrollbar.
- Tab strips and the task rail line up evenly.

#### Accounts and providers

- One refusing Azure DevOps organization no longer expires the whole connection.
- "All visible" includes repositories outside your account's organizations, and GitHub issue lists stop at 50 rows per page.

***

<a id="v0-10-0"></a>
## Version 0.10.0

<kbd>Monday, September 21st, 2026</kbd>

### Features

#### Terminal sessions

- Run any agent in a real terminal inside Kepler: Codex, Cursor, Copilot, OpenCode, Auggie, Grok and your own custom agent server, alongside rich chat.
- Choose Terminal or Rich chat per session, set a default per agent, and switch to the other mode from the New session menu.
- A status bar under each terminal session shows the running model, effort and mode, plus a toggle for rich input. It stays current when you change them inside the CLI.
- Answer a terminal agent's permission requests and questions from Kepler, instead of switching to its own interface.
- Terminal agents get Kepler's workspace tools and task context, the same as rich chat, and their transcript survives a restart.
- Paste images into Claude Code and Codex terminals.
- Kepler confirms before closing a busy terminal.
- Pi and Google Antigravity are supported as terminal-only harnesses.

#### Sessions you started outside Kepler

- Kepler now finds agent sessions you started in your own terminal, and past sessions left on disk. Preview the transcript, then continue it, fork it, or adopt it into a task. Kepler binds a conversation to a task without taking it over. On by default.
- External sessions appear on the Dashboard, in the New task picker, the session view and the task rail, with a shared context card.
- Create a task in any plain folder, not just a repository.

#### Reviewing changes

- New Changes overlay for reading a worktree's diffs, over three scopes: the working tree, the whole branch against its base, or a run of commits you pick.
- View file changes in a tree or flat list.
- Toggle between stacked or split diffs.
- Unmodified files can now also be reviewed.

#### Dashboard

- New Inbox grouping sorts tasks into unread, running, needs attention, recent, earlier, done and archived. A session stays marked unseen until you look at it.
- Rebuilt worktree chip: the branch cell shows what the branch adds against its base (commits, files and line delta), and the upstream cell offers only the verb the counts call for, with force-push behind a confirmation. Terminal, Open in and Run sit alongside as split controls.
- The Terminal cell counts the shells running in a checkout and brings the most recent one forward, and the "+" lets you choose between a task's checkouts by branch.
- Tasks spanning several repositories now appear under each of them.
- The header folds its controls one at a time as room runs out.
- A selected row glides to its new position when the list reorders.
- Archived tasks are badged in their preview and detail headers.

#### Tasks and worktrees

- Open a task's worktree, sessions and terminals as tabs or as splits, with a column's tabs mirroring the rail.
- Terminals move into a drawer beneath the columns, sized by a sash. One glyph per tab carries both what the tab is and how it exited, and a finished command run offers Stop or Run again from a result bar.
- Tabs in a task now mean what they show: a session tab archives it, a terminal tab closes it through the busy confirmation, a resource tab just hides it.
- Reorder tabs and dashboard panels from their menus or the keyboard.
- The task context panel can be put away.
- Issues correlated to a task's branch attach on their own, and Related refreshes for real.
- A worktree that's gone stays bound to its task, and Kepler offers to recreate it.
- Kepler remembers which repositories you pick for a tracker project, and preselects them in Jira, Linear and Azure issue flows.

#### Starting a task

- Pick repositories and folders from one ranked list that learns which ones you use most, shared between the repo and folder chips.
- Automatic task branches are named from your task's context and namespaced under kepler/, with the prefix configurable per app and per repository, and your repository's own branch-naming policy applied.
- The New task dialog remembers an unsent draft when you close it.

#### Steering and stopping agents

- Send a follow-up while a turn is running and it steers the agent, instead of waiting for the turn to end.
- Escape stops a running turn, Interrupt & send is a chord from the message composer, and a cancel that's taking too long can escalate to Force stop.
- Stop and Restart are now explicit verbs on a session, with restart progress shown.
- Kepler counts busy terminals when you quit.
- Dormant sessions start on the first prompt, and an archived session can be previewed read-only.

#### Windows, menus and navigation

- Windows and Linux hide the native title bar and gain Kepler's own app menu behind the top-bar menu button, including Settings, Check for Updates, and a Window menu listing every open window.
- New window switcher in the top bar and the tray, showing what each other window's agents are doing. The window title leads with the remote and how many sessions are waiting.
- Back and forward now follow one rule: Back leaves the place or mode you're in, and never retraces a search, a filter or a view-mode change.

#### Appearance

- New middle-dark theme, now the default. The previous dark theme is named Midnight.
- New About dialog, opened from either menu.

#### Repositories, accounts and remote

- One repo dialog for both adding and editing: paste a path or a clone URL and Kepler inspects it into a card.
- Organization switcher in Settings › Account now lets you pick between organizations you belong to.
- Purchase or subscription changes outside Kepler are now picked up without a restart.
- Detected WSL distributions are offered from the Environments page, and voice input works in remote windows.

#### For your agents

- Agents can create tasks and sessions, and detach a task's worktrees.
- Agents can read another session's transcript by a copyable identifier, at the level of detail they ask for.

#### Smaller additions

- Start typing anywhere in a session to focus the message composer.
- Manage commands… in the run menu, deep-linking to that repository's settings.
- Cmd/Ctrl+J opens the task's terminals, Option/Alt-click opens a resource row in the browser, and text context menus offer spellcheck actions.
- Picking an editor or a command no longer silently pins it as your default. Each row carries its own set/unset toggle, reachable from the keyboard.
- Line-wrap toggle on code blocks.

### Improvements

#### Performance

- Issues and pull requests load faster: the provider only broadens its search when you ask, and issues correlate to tasks by lookup instead of a scan.
- The Dashboard reads cheap worktree signals and remembers each branch's base count, so a board of many tasks stays responsive.
- Images in a conversation load their viewer only where one can actually open, so long transcripts stay light.

#### Agents

- Kepler now uses your system Codex CLI rather than a bundled copy.
- Token usage now shows when it was last updated.

#### Writing a prompt

- Prompt controls were tightened throughout, in the New task dialog and in a session alike. The agent pill sits beside Send everywhere, the context gauge is drawn as a usage ring, the agent picker is a list of labelled rows, the agent settings menus are searchable, every control has a real tooltip, and Send shows a sending state from the moment you click.

#### Layout and windows

- The Add and Edit repository dialogs were flattened to match each other, and the path is promoted.
- Every splitter now uses one sash, and a double-click splits it evenly.
- Top bar controls are shed based on the room actually available, rather than fixed width breakpoints.
- The main window now has a 480 by 360 minimum size.

#### Clarity and polish

- Kepler's spinner is used for page and pane loading, and the mark animates on the boot curtain.
- If the app hits an unrecoverable error, you now get a Kepler screen instead of a raw crash page.
- Provider, kind and reference are fused into one source chip on todo rows.
- A task's link subtitle leads with the pull request or issue identifier, and links can be refreshed from the group header.
- The archive and delete dialogs remember your cascade choices.

### Fixes

#### Terminal sessions

- Terminal sessions keep their identity across a restart, survive idle shutdown while busy and come back on reopen, launch in the mode shown when you started them, run under the Claude account you selected, and report the CLI's own error when a launch fails.
- An interrupt is recognised whether it arrives as Escape or Ctrl+C. A turn counts as cancelled once both its hooks and its output go quiet, so a stopped session no longer lingers as though it were still working.
- A Claude terminal session honors its Default model and Manual mode picks.
- A terminal session keeps its row when its worktree is cleaned up.
- Terminal input state is reconstructed after a long-running session scrolls past its startup, so Shift+Enter and pasted newlines keep working.
- Clipboard and link handling improved on Windows and over remote connections, and split-pane resizes no longer arrive as a burst.
- A terminal's close confirmation now names the job you actually launched.

#### Sessions and transcripts

- A session blocked on a permission request or a question now reports as waiting.
- Unknown hook events are read as presence rather than activity, and a replay of the registry no longer marks a live session unread or binds a terminal that was never bound.
- The status dot says what the process is doing and the title says whether it is unread, so a running session no longer reads as two kinds of busy at once.
- Opening a task lands on its own session before an external one.
- Transcript reads that fail or truncate say so, instead of showing an empty conversation.
- Transcripts show a loading state instead of "Start a conversation" while they load, preserve replayed message boundaries, and no longer loop on scroll position.
- Session tabs have context menus, hover cards show full titles, and the session picker offers the alternate run mode.
- An agent that dies unexpectedly is classified the same way on every platform, and the exit hint is kept out of the toast.
- Approving a plan records the mode it selected, and later plans still prompt.

#### Prompts and chat

- The New task dialog confirms before discarding a task you have started writing.
- The message composer stays live after an empty-draft Interrupt & send, holds its shape while a switched agent's options load, and ignores keys an input method is still composing.
- The command menu opens at the caret, not only at the start of the prompt.
- A permission prompt no longer repeats the command already shown on its tool call.
- Slash commands resolve for a session that is disconnected.
- A remembered repository you haven't touched is dropped when an issue or pull request brings its own.

#### Sign-in, plans and accounts

- An expired login is revalidated when terminal auth finishes, a scope-limited credential gets an actionable message, a self-healing token expiry recovers, and an auth error shows a retry screen instead of an endless boot spinner.
- A launch parked waiting for sign-in resumes when that sign-in lands.
- Paid plans are no longer capped where they shouldn't be: agent accounts are unlimited on Pro and above, and the per-plan cap on remote environments is gone.

#### Remote and SSH

- Remote connections reconcile desktop and daemon authentication, recover window history across a reconnect, stay bound to their daemon through a reload, no longer loop restarting on a downgrade, and show a server update as a reconnect rather than a lost session.
- Kepler reuses your own SSH host configuration before offering to edit it, and opens VS Code on SSH environments through that alias.
- Opening a link that carries an access token keeps you on the page it named.

#### Git, worktrees and repositories

- New worktrees fork off the remote tip when the base is a remote branch, record only the push remote, and avoid temporary branch reference collisions.
- Kepler authenticates its own reads against a remote, not just the clone, so a private repository resolves.
- Removing a worktree asks for confirmation before ending the sessions running in it, and a task-owned worktree can be deleted.
- Worktree change counts are measured against the branch's recorded fork point.
- Repository display names are consistent across every surface, each repository gets the shortest label that stays unambiguous, and chips no longer slice it.

#### Issues and pull requests

- Issue and pull request lists carry forward what they already had when part of a fetch fails, tell a provider failure apart from an empty result, stop re-walking a sweep that keeps failing, and no longer duplicate a pull request already in the list when you paste its URL.

#### Dashboard

- A task's status follows its real state: Development reads from the commits ahead of its recorded base, Review needs an open pull request, a dirty tree withholds Done, and a task can be finished from its stored pull-request links.
- Real profile pictures instead of letter initials, preview actions stay visible at narrow widths, groups sort on recency consistently, provider filters combine as a union rather than an intersection, the search box stays in the row until it's genuinely cramped, and external sessions stay listed under filters that can't answer for them.
- Task previews stay open when you reopen the full view.

#### Interface

- Popovers, menus and tooltips stay clear of the top bar, hand-rolled overlays remain usable over an open menu, and passive poppers no longer swallow Escape.
- Sashes have one drag that ends when the operating system takes the pointer, and no longer double the line at a pane boundary.
- A pane keeps the size you dragged it to, and a sized pane comes back at its remembered height.
- Numbered lists stay continuous in rendered markdown.
- The page header keeps its inset at every pointer width.
- The image viewer's close button stays clear of the title bar's drag region.
- The title bar shows the full branch name, with its tooltip on hover.
- Zoom is no longer reapplied on macOS display changes that only moved the work area, or on a native resize elsewhere.

#### Agents and platforms

- The GitKraken tools are installed into command-line agents only. The workspace tools are auto-approved across agents, including Auggie, which used to lose them.
- Trusted Auggie MCP settings are preserved.
- Codex installed through npm, and Cursor's PowerShell entry point, are both found and launched on Windows.

***

<a id="v0-9-3"></a>
## Version 0.9.3

<kbd>Thursday, September 3rd, 2026</kbd>

### Improvements

- Faster loading of correlated issues and pull requests for worktrees, using a single batched request instead of many sequential ones.
- Clicking Stop on a running agent turn now shows a "Stopping…" indicator while it winds down.

### Fixes

- Clicking Stop on a running agent turn no longer shows the composer as idle before the agent has actually stopped.
- Fixed a bug where a stored remote setup-token credential could block the usage chip from updating.
- Fixed repos getting duplicated when batch-selecting multiple issues from the same repo in the Add Resources dialog.

***

<a id="v0-9-2"></a>
## Version 0.9.2

<kbd>Tuesday, September 1st, 2026</kbd>

### Features

- Read a worktree's changes without leaving the Dashboard: "View changes" in the worktree popover opens the full changes view in the side panel.
- Jump around a long conversation from a new bar at the top of the chat. It names the prompt you're currently reading and opens a list of every prompt in the session.
- Copy any code block in a conversation with one press, and open links from the transcript directly.
- Rename a branch from task detail.
- Start and close a session from the keyboard; the standalone task launcher moves to Shift+Alt+N.
- The Add resources dialog can filter by linked work and shows a badge for work already on a task.

### Improvements

- The Agent Graph is much lighter and no longer burns CPU and GPU while sitting open. The picture also holds still while the fleet works: the camera frames what you selected and stays there, roots stop reordering themselves, and node panels answer the node you picked.
- Worktrees an agent creates are now attributed to the session and task that made them.
- The task page's working-changes tree shows added and removed line counts per file and per section.
- Attention toasts opened from the Dashboard now show the task in a side panel instead of navigating away from your list, panels and scroll position.
- Issue and pull request refresh no longer stalls for a minute or more on large organisations.

### Fixes

- Picking an existing branch in the Task Launcher checks it out instead of leaving the repo on a detached HEAD.
- Launching a task no longer fails permanently after a repository's default branch is renamed. It falls back to the repo's current default, and a genuinely missing branch is named along with how to fix it.
- Archive Task and Delete Worktree no longer warn that commits will be lost when those commits are already pushed and part of an open pull request.
- Typing `/` shows your agent's skills in every composer, including the launcher and the dashboard dock, and a slow first probe no longer leaves the menu permanently empty.
- Signing in to an agent account unblocks every session waiting on it, not just one.
- Pasting a pull request or issue URL resolves it directly instead of only matching rows already loaded.
- Merged pull requests stay visible in the Dashboard's Related panel, and a multi-repo task is only finished once all of its pull requests are merged.
- Tasks no longer climb through the progress lifecycle on a cold start.
- A task can attach more than one pull request again.
- Removing a worktree that git only partly removed now cleans up the leftover folder and the stale entry blocking the retry, instead of failing every retry the same way.
- Task folders no longer end up with an unresolved repository placeholder in their path, which made them illegal filenames on Windows.
- Remote windows recover on their own: a disconnect returns the window to local Kepler, and a crashed remote window recovers instead of being stranded.
- The remote tunnel no longer flaps in a reconnect loop, and Remote Access works from inside a Remote Environment.
- Updating while connected to a remote host restarts correctly, and a failed update now tells you what went wrong instead of silently reverting.
- Images returned by tool calls render in the conversation, and structured tool errors are formatted rather than dumped.
- On macOS, traffic lights are placed correctly when a window is created zoomed.
- Copying from the terminal works through Kepler's own clipboard path.
- The default repositories folder is only scanned when asked for.
- Remote access starts on another port when the requested one is refused rather than blocked.

***

<a id="v0-9-1"></a>
## Version 0.9.1

<kbd>Tuesday, August 25th, 2026</kbd>

### Features

- Changed files are now a real file tree, and every file in a diff lives in one continuous scroller. Clicking a file jumps to it instead of reloading the view.
- Large commits paint straight away: a 200-file diff no longer downloads every file before showing the first row, and full contents load per file as you expand them.
- Select several files in the tree with Cmd/Ctrl+click, Shift+Arrow or Cmd+A, and stage, unstage or discard them from a right-click menu.
- New and binary files now render properly in a diff: a new file shows as a whole file, and image changes show a before/after preview.
- Codex sub-agents now show up as their own cards in the conversation.

### Improvements

- Worktree headers show how far a branch has drifted from its base, with distinct behind, diverged and conflict states and a tooltip explaining each.
- Worktree rows in a task's Changes panel now lead with the branch you're on instead of the folder name, with the repo and base on a second line.

### Fixes

- Typing `/` in the launch composer shows your agent's skills again.
- A dormant or disconnected session's conversation is no longer blank. The saved transcript is served back.
- Deleting a git worktree no longer destroys the conversation that ran in it; the session is kept, marked as missing its worktree, and stays readable.
- Connecting an integration now names the account you're signed in to Kepler as, instead of silently using whichever account your browser is logged in to.
- Tasks backed by a folder rather than a git worktree keep their "Start a new session" button.
- "Add repository" in the Add resources dialog is no longer disabled while a repo's default branch is still resolving, or for a repo with no resolvable base.
- Resuming a session that no longer exists closes the tab and tells you why, instead of failing silently.
- A full disk during a save now says so, rather than failing without explanation.
- A sign-in code that was already used now explains what to do next.
- Agent Settings cards show the right agent name in the Accounts section instead of always saying "Claude Code".
- The action button on a Kanban column card no longer overhangs the card's border.
- Kepler's hook server falls back to another port when the remembered one is refused.
- Auto-update no longer offers a version before all of its files are published.

***

<a id="v0-9-0"></a>
## Version 0.9.0

<kbd>Monday, August 24th, 2026</kbd>

### Features

- New task detail view: every task gets its own workspace, with split panes, a rail of its resources, tabbed sessions and integrated terminals.
- New Task Launcher: start a task by writing the prompt first. Repos, issues, pull requests, files and folders attach as resources, and a task no longer needs a repo at all.
- Tasks name themselves from your prompt, and can be renamed or archived from any surface.
- Add resources: browse issues and pull requests with live filters for relationship, repo, state, draft and recency, with search pushed out to every connected provider.
- Actions: write your own prompt actions, pick an agent per action, and fire them from any surface.
- Agent Graph: a live graph of what your agent fleet is doing, with previews, replay and a time scrubber, on the Dashboard and beside a conversation.
- Interactive plan review: read an agent's plan and comment on it inline before the work starts.
- Remote Access is now generally available: a built-in tunnel to reach Kepler from anywhere, with a QR code and controls in the top bar. Your machine stays awake while it's on.
- Find in conversation with Cmd/Ctrl+F.
- Dashboard gains a "Needs my attention" grouping, an archive bucket with bulk cleanup, foldable sections, provider filters, per-worktree controls, terminals in the side panel, several task panels open at once with pinning, and a rows-and-columns list layout.
- Multiple accounts per agent for Codex, Copilot and Auggie.
- Grok Build harness is now supported.
- Bring your own agent: point Kepler at any ACP compatible agent server of your own.
- Agents can manage their own task: list and attach resources, create and discard worktrees, and write task notes.
- Add an existing local repository from Settings or the task dialog, and give repositories a custom display name and description.
- Clones now authenticate with your account's provider token, including enterprise hosts, and adopt an existing folder on disk instead of failing.
- Delete a worktree from the UI, with live guards and an explicit confirmation when something would be lost.
- New "Allow for this session" permission tier, and you can answer a permission request straight from its notification.
- Voice input has a guided, end-to-end setup.
- Dashboard, task view and Settings now work on tablet and phone screens.
- Kepler asks for confirmation before quitting with sessions still running.

### Improvements

- Rebuilt design system: one consistent set of colors, type and spacing, with contrast measured against WCAG AA in both light and dark.
- Much faster startup: cold launch reaches first content sooner, and a freshly launched task is interactive immediately.
- Issue and pull request search runs on the provider instead of locally, so long lists load instantly.
- Conversations read more calmly: consecutive tool calls collapse into clusters, batched edits group together, subagent work folds into a single card, and permission requests render inline in the transcript.
- Markdown files an agent writes render as formatted documents, with a toggle back to the source.
- Quote a selection into the composer as a blockquote, and use a right-click menu in chat, the composer and terminals.
- Rebase and merge move to a new sync engine, with a reliable conflict indicator before you start.
- Token usage is clearer: a redesigned quota gauge, Codex usage-limit resets, Auggie credits and billing cycle, and an account-wide rate-limit indicator across sessions.
- Diff highlighting moved off the main thread, so large diffs no longer stutter the UI.
- Settings split into focused sub-pages, with Remote Access on its own page, and one consistent page header across the app.
- Branch and worktree pickers, and the repo/branch selector in the launcher, were rebuilt for speed and clarity.

### Fixes

- Transcripts no longer go blank, lose their scroll position on tab switches, or restore resumed history out of order.
- Dormant and disconnected sessions recover instead of showing a mute screen, and reconnects correct a stale view.
- Your per-session model, mode and effort picks survive a restart, and a retired model no longer lingers in the picker.
- Zoom survives a macOS Space switch, a window resize and waking from sleep, and windows restore onto the monitor they were on.
- New worktrees fork off the remote default branch instead of whatever HEAD happened to be, and the launcher names the real base branch.
- A revoked or expired provider token is reported for what it is instead of failing every read. An expired Claude login is told apart from being signed out, with a warning before it expires.
- Terminal typing and panel resizing arrive in order, so fast input no longer transposes characters and a drag settles at the final size.
- External agent sessions are discovered across every account and custom home directory, including Codex's current session format.
- Long network Git operations no longer time out at 60 seconds, and an authentication failure surfaces an actionable error instead of hanging on a hidden prompt.
- Notifications are kept for what failed rather than for what worked, and toasts no longer navigate you away when a turn ends.
- Many Dashboard fixes: selection survives tab switches, status colors survive a restart, work starts in the panel it was fired from, and a provider refresh in flight is no longer read as an empty answer.

### Breaking changes

- The List, Kanban and Console views have been removed. The Dashboard is the roster and the task detail view is where work happens.
- The same-network LAN serve mode and the ngrok URL override are gone. Use Remote Access instead.
- Once your data has been migrated by this version, older builds will refuse to open it rather than risk corrupting it.

***

<a id="v0-8-1"></a>
## Version 0.8.1

<kbd>Thursday, July 23rd, 2026</kbd>

### Fixes

- Shift+Enter inserts a newline again in terminal and CLI sessions.
- Assistant messages no longer appear cut off around tool call cards in chat.
- Sessions with outdated or invalid saved model options now load reliably.

***

<a id="v0-8-0"></a>
## Version 0.8.0

<kbd>Wednesday, July 22nd, 2026</kbd>

### Features

- Redesigned remote connection experience: switch between your local and remote environments from a lightweight title-bar popover, with host setup, connection details, and diagnostics moved into a dedicated panel.
- Sign in to Claude Code through your browser without dropping to a terminal, including on remote and SSH connections.
- The repo picker now auto-populates from your Default Repositories Folder.
- Refreshed app icon.

### Improvements

- Remote connections are more secure and more stable, with stronger protection against unauthorized access and smoother recovery from dropped connections and failed sign-ins.
- Agent CLIs now report "Kepler" as the client name, so it shows correctly in places like your Anthropic dashboard.
- Skills and slash commands are now discovered per repository, not just per agent.

### Fixes

- The app now reloads itself after an update instead of failing to load with a stale module.
- Stale saved sessions are closed cleanly instead of getting stuck trying to reconnect.
- Terminal sessions launched with the Default agent no longer reuse a stale model, mode, or effort.
- The model picker is restored for agents preselected with a legacy model.
- Model and mode selection now works for Auggie.
- Terminal environment inherited from VS Code no longer leaks into spawned agents.
- Pull request links on a card now stay scoped to that card's own repository.
- The worktree header now reflects the loaded branch instead of the current git status.
- Long labels in the focused Console column now truncate instead of overflowing.

***

<a id="v0-7-12"></a>
## Version 0.7.12

<kbd>Monday, July 13th, 2026</kbd>

### Features

- Queue up prompts while the agent is busy. They're kept across disconnects, re-authentication, and reconnects.
- Disconnect a provider directly from Settings → Provider Integrations.
- Unified filter and sort menu for the task sidebar.

### Improvements

- Task sidebar keeps a stable, predictable order.
- Tooltips now show the full text on truncated picker labels.
- Updated the bundled Claude and Codex agents.

### Fixes

- More reliable session teardown, cancellation, and recovery when a prompt fails to send.
- Pull request data no longer stays frozen after repeated background refresh warnings.
- Pull request branch matching is now scoped to each card's own repository.
- Removed a spurious "Task completed" notification when resuming a worktree.
- Clicks now pass through correctly when a dialog opens over another dialog.

***

<a id="v0-7-11"></a>
## Version 0.7.11

<kbd>Wednesday, July 8th, 2026</kbd>

### Features

- Paste non-image files directly into the terminal on Windows and Linux.

### Fixes

- Worktrees now show up correctly in the sidebar on remote and production builds.
- Fixed a duplicate agent tab briefly appearing when starting a session.

***

<a id="v0-7-10"></a>
## Version 0.7.10

<kbd>Tuesday, July 7th, 2026</kbd>

### Features

- Augment's Auggie is now available as an AI agent, with in-app browser sign-in for both local and remote/SSH connections.
- Save default agent options that persist per account, so new sessions start with your preferred model and settings.
- Turn off notifications for external terminal tasks with a new opt-out setting.

### Improvements

- Remote connections over SSH and WSL are more reliable: "Open in…" and "Reveal" now work on the host machine, desktop notifications are restored for remote sessions, and failing connections re-provision and retry automatically.
- Windows restore more reliably after a restart, and remote windows are no longer silently downgraded to local when sign-in briefly fails at startup.
- Dismiss all notifications at once with a new pill, and each toast keeps its own close button.

### Fixes

- The app zoom level now persists reliably instead of being reset by per-site zoom state.
- Assistant messages no longer split into fragments when a tool runs mid-response, and streamed text renders as one continuous message.
- The model list in the launcher stays in sync with the session's model picker.
- In-app notification toasts now appear only in the focused window.
- The launcher now surfaces provider errors instead of silently dropping them.
- Clearing the log now closes the confirmation dialog.
- macOS no longer shows a false "malware" warning for bundled command-line tools on launch.

***

<a id="v0-7-9"></a>
## Version 0.7.9

<kbd>Tuesday, June 30th, 2026</kbd>

### Features

- Native desktop notifications on macOS, with an in-app toast fallback.
- Choose which Claude account to use when launching a task.
- Switch between multiple connected integrations of the same provider.
- Browse issues and pull requests from a secondary account without changing your primary one.
- Multi-select questions from the agent are now supported in local sessions.
- Tasks now remember the base branch they were launched from.

### Improvements

- Pull requests are matched to worktrees by their upstream branch, for more accurate correlations.

### Fixes

- Claude agent sessions now start correctly on Windows when Claude is installed via npm.
- Copilot agent sessions no longer fail to start on Windows when Copilot is installed as a global npm package.
- Bundled agent sessions no longer flash console windows on Windows.
- Pull requests where you're a reviewer no longer disappear when filtering by repository.
- Clicking "Chat about this" on an agent prompt now declines it cleanly instead of cancelling the session.
- Bitbucket connection warnings are now handled gracefully.
- Issues now resolve to the correct repository.
- Long edges in the commit graph route around intermediate lanes for a cleaner layout.
- Modals now close only via Escape or the close button, not by clicking outside.
- The context-usage popover renders above the overflow menu instead of behind it.

***

<a id="v0-7-8"></a>
## Version 0.7.8

<kbd>Friday, June 26th, 2026</kbd>

### Features

- Right-click any worktree row in the sidebar for a context menu of actions.
- Kepler is now available as a Flatpak and on the Arch User Repository (AUR).

### Improvements

- The Task Launcher now surfaces transient fetch errors, such as rate limits and timeouts, instead of failing silently.

### Fixes

- Remote connections now recover automatically after a restart or sleep.
- Manually opened terminals receive focus; terminals spawned by a command no longer steal it.
- The Claude Code agent terminal no longer closes immediately when a managed MCP config is present.
- Long commands in the run-command menu now wrap instead of overflowing, and the menu width is capped.
- Picker menus in chat fit their contents, with clearer scrolling when the list overflows.
- Window state is now saved correctly when macOS restarts the app to apply an update.

***

<a id="v0-7-7"></a>
## Version 0.7.7

<kbd>Tuesday, June 23rd, 2026</kbd>

### Fixes

- Fixed a Windows installer issue where some application files were not extracted, which could prevent the app from launching.
- The sign-in screen logo now displays correctly.

***

<a id="v0-7-6"></a>
## Version 0.7.6

<kbd>Tuesday, June 23rd, 2026</kbd>

### Features

- Each window's title bar now reflects the remote connection it's attached to.

### Fixes

- Fixed launching the agent terminal when Kepler is installed through a symlink on Linux.
- The terminal launcher no longer drops the initial prompt when starting a session.

***

<a id="v0-7-5"></a>
## Version 0.7.5

<kbd>Monday, June 22nd, 2026</kbd>

### Features

- Sign in with multiple Claude Code accounts and switch between them.
- Agents can now ask you multiple-choice questions during local sessions.

### Improvements

- Smoother app startup with a unified loading spinner and faster task-list loading.
- Error messages now include the details returned by the server instead of just a status code.

### Fixes

- Agent sessions now recover automatically when an authentication token expires mid-session.
- Claude usage now reads from the correct account when more than one is signed in.
- Manually run commands can now be stopped even after running longer than five minutes.
- Pull request commits stay visible in the review commit graph.
- External CLI session status is now preserved across app restarts.
- Task launch failures are now shown to you instead of failing silently.
- Deleted worktrees no longer trigger repeated status-check errors.

***

<a id="v0-7-4"></a>
## Version 0.7.4

<kbd>Friday, June 19th, 2026</kbd>

### Features

- Manual commands now run in a visible terminal session, so you can watch live output and stop them from the terminal panel.
- The Task Launcher now hides issues and pull requests that already have tasks by default, with a Show tasked toggle when you need them.

### Fixes

- Launcher pickers now open with the selected item already visible and no jumpy scrolling on hover.
- Pull request status is clearer in the sidebar, and worktrees with open pull requests stay in Review instead of moving to Done because of older closed pull requests.
- Task launch now avoids branch-name conflicts with existing nested branch names.

***

<a id="v0-7-3"></a>
## Version 0.7.3

<kbd>Friday, June 19th, 2026</kbd>

### Fixes

- Launching a task from a remote-only branch now retries on transient network failures instead of immediately failing to create worktrees.
- Improved stability for certain unhandled errors.

***

<a id="v0-7-2"></a>
## Version 0.7.2

<kbd>Thursday, June 18th, 2026</kbd>

### Features

- Run a configured command directly from a Kanban card or the chat modal.
- Kanban cards move to the Done column automatically when their pull request merges or closes.
- Press Ctrl+Q to fully quit Kepler on Windows and Linux.

### Improvements

- The Task Launcher keeps a stable size per tab and now floats above fullscreen apps.
- Console layout is remembered as you navigate between views.
- The task setup toast now shows the worktree name and the commands it ran.
- Pull request links now appear on worktrees even when their branch can't be auto-matched.
- Settings feature toggles are realigned into consistent, unified checkbox rows.

### Fixes

- Signing out now fully signs you out of Claude Code.
- Model, mode, effort, and shared context are preserved when you switch a session's strategy.
- Agent sessions now start reliably on Windows.
- Kepler-locked worktrees are removed reliably on Windows.
- Signing in from WSL now opens the Windows browser.
- Terminal sessions open in the correct working directory, and the first agent turn starts faster.
- CLI sessions now start correctly in direct (non-git) worktrees.
- Terminals keep their width and no longer flash when switching views.
- Leftover agent and terminal processes are cleaned up reliably after a crash or when a session ends.
- The Console now sorts reliably, keeps keystrokes isolated to the focused column, and no longer shows duplicate notifications.
- Console input controls collapse cleanly in narrow columns.
- Horizontal trackpad scrolling now works across Console columns.
- Tasks reuse an existing worktree on a branch when its label can't be resolved.
- The onboarding setup button no longer flashes before setup finishes loading.
- The Claude strategy popover now uses a gear icon instead of a warning icon.

***

<a id="v0-7-1"></a>
## Version 0.7.1

<kbd>Tuesday, June 16th, 2026</kbd>

### Features

- Rich chat is now the default mode for Claude Code sessions.
- Remote development now works against Windows machines over SSH.

### Improvements

- Smoother trackpad scrolling in full-screen terminal apps, backed by a faster terminal renderer.
- Pull request lists now load every page, so large sets of PRs show up completely.

### Fixes

- Claude Code sessions started outside Kepler are now detected, scoped to the right repo, and recovered from their transcripts.
- macOS line-editing shortcuts (such as Ctrl+A and Ctrl+E) now reach the shell in the terminal.
- Restoring a session from the picker now selects and resumes it automatically.
- Your open windows are now kept when the app restarts to apply an update.
- Reconnecting to a session that errored now restores its model, mode, and reasoning effort.
- Remote installs are more reliable when a previous install was interrupted or two run at the same time.
- Diffs no longer show spurious changes caused by differing line endings.
- A task's commit list no longer includes unrelated commits when your local main branch is behind the remote.

***

<a id="v0-7-0"></a>
## Version 0.7.0

<kbd>Monday, June 15th, 2026</kbd>

### Features

- The worktree sidebar now draws a lane graph when your branch has diverged from its upstream, so you can see the split at a glance.

### Fixes

- Resuming an agent session that the backend no longer recognizes now starts a fresh session instead of failing.
- A terminal's initial prompt is now reliably delivered when its session starts.
- Terminal contents no longer flash garbled on open. Buffer replay now waits until the terminal is correctly sized.
- Kepler now returns you to the home view when a worktree is deleted outside the app, instead of leaving you on a broken page.
