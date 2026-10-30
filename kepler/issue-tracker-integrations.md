---
title: Issue Tracker Integrations
description: Connect your issue trackers to Kepler, cloud or self-hosted, so the issues you're working on land in one list, with everything an agent needs already attached.
product: Kepler
feature: Issue Tracker Integrations
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [jira, linear, trello, github, github-enterprise, gitlab, gitlab-self-hosted, azure-devops]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [integrations, issue-trackers, jira, jira-data-center, linear, trello, github, gitlab, azure-devops, self-hosted, accounts, settings]
taxonomy:
    category: kepler
---
<kbd>Last updated: October 2026</kbd>

Connect an issue tracker and the issues you're working on show up in [the Kepler interface](/kepler/kepler-interface), alongside your pull requests and the tasks you already have running. Starting work on one becomes picking a row rather than describing the work from scratch.

Manage providers in **Settings → Integrations**, in the **Issues and pull requests** section.

<figure style="text-align:center">
  <a href="/wp-content/uploads/provider-integrations-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/provider-integrations-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Issues and pull requests section of Settings › Integrations. Azure DevOps and GitHub read Connected, each with Disconnect and Reconnect and a visibility line, Everything visible, with Choose what's visible…; Azure DevOps lists two accounts, Alex Lee (primary) and Alex Lee (Contoso). Azure DevOps Server, Bitbucket, Bitbucket Data Center, GitHub Enterprise, GitLab, GitLab Self-Hosted, Jira, Jira Server / Data Center, Linear and Trello each offer Connect.">
  </a>
  <figcaption style="text-align:center; color:#888">Issues and pull requests, in Settings → Integrations.</figcaption>
</figure>

***

## Trackers Kepler can read issues from

Ten of Kepler's twelve providers return issues:

| Provider | Also returns pull requests |
|---|---|
| **GitHub** | Yes |
| **GitHub Enterprise** | Yes |
| **GitLab** | Yes |
| **GitLab Self-Hosted** | Yes |
| **Azure DevOps** | Yes |
| **Azure DevOps Server** | Yes |
| **Jira** | No |
| **Jira Server / Data Center** | No |
| **Linear** | No |
| **Trello** | No |

**Bitbucket** and **Bitbucket Data Center** are the other two. They return pull requests only. See [Pull Request Integrations](/kepler/pull-request-integrations).

Self-hosted instances are first-class: **GitHub Enterprise**, **GitLab Self-Hosted**, **Azure DevOps Server**, and **Jira Server / Data Center** read issues the same way their cloud counterparts do, and two servers of the same kind stay separate even when their issue keys overlap. Which fields come back depends on your server's version, and your machine needs to be able to reach the server. You connect a self-hosted instance inside Kepler with its address and a personal access token. See [Connect a self-hosted tracker](#connect-a-self-hosted-tracker).

Kepler trusts the certificates installed in your operating system's certificate store, so a server signed by your company's own certificate authority, or a network that re-signs HTTPS traffic, works without extra setup.

***

## Connect a tracker

Connecting a cloud tracker (**GitHub**, **GitLab**, **Azure DevOps**, **Jira**, **Linear**, or **Trello**) takes four steps:

1. Open **Settings → Integrations**.
2. Find the provider in **Issues and pull requests** and click **Connect**.
3. Authorize Kepler in the browser window that opens.
4. Return to Kepler, where the provider shows a **Connected** badge in **Issues and pull requests**.

Your GitKraken account holds integrations, not this copy of Kepler, so a provider you connect here also becomes available to the `gk` command-line interface (CLI) and GitKraken Desktop. You need to sign in to a GitKraken account to manage them; Kepler prompts you if you are not signed in.

**Connect** hands the authorization for a cloud tracker to GitKraken's website. Kepler opens `/connect` there in your system browser, names the provider, and includes a redirect back into Kepler. When you return, Kepler refetches your providers instead of reusing its cached list.

While you authorize, Kepler keeps a **Connect {provider} in your browser** dialog open, with the provider's name in place of {provider}. If your browser didn't open, copy the **Connection link** from the dialog and open it in a browser yourself. **Try again** makes a fresh link, since each link works once. The dialog closes by itself as soon as the new connection appears, and Kepler checks for it again whenever you come back to a Kepler window. If Kepler can't start the connection, the dialog reads **Unable to connect {provider}** and says why.

### Connect a self-hosted tracker

**GitHub Enterprise**, **GitLab Self-Hosted**, **Azure DevOps Server**, and **Jira Server / Data Center** connect inside Kepler with a personal access token rather than through the browser:

1. Open **Settings → Integrations**.
2. Find the provider in **Issues and pull requests** and click **Connect**. The **Connect {name}** dialog opens.
3. In **Server URL**, enter the server's address, including the port and installation path when your server uses them.
4. In **Personal access token**, paste a token with access to the issues you need.
5. Click **Save connection**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/self-hosted-connect-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/self-hosted-connect-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Connect Jira Server / Data Center dialog: Register your server using a personal access token. Server URL holds https://jira.acme.example, with the hint to include the port and installation path when your server uses them, and Personal access token holds a masked token, with the hint to use a token with access to the repositories or issues you need. Cancel and Save connection sit at the bottom.">
  </a>
  <figcaption style="text-align:center; color:#888">Connecting a Jira Server / Data Center instance with a personal access token.</figcaption>
</figure>

Kepler checks the token against the server from your machine, keeps it in a protected credential store on this device, and syncs the connection to your GitKraken account. The dialog reports whether the server accepted the token, whether Kepler saved it without being able to reach the server or verify its certificate, or whether the server refused it (*The server refused this token. Check its value and permissions.*). Until the upload to your account lands, the provider's row shows **Cloud sync pending**. **Reconnect** on a self-hosted provider opens the same dialog, so you can replace an expired or rejected token there. See [Pull Request Integrations](/kepler/pull-request-integrations#connect-a-self-hosted-instance) for every message the dialog shows.

Three controls sit on a connected provider's row:

| Control | What it does |
|---|---|
| **Reconnect** | Re-runs authorization. Use it when a sign-in has expired |
| **Disconnect** | Removes the provider's primary connection (see below) |
| **Refresh** | At the top of the section, re-checks every provider |

A provider's row can also carry a warning:

| Warning | What it means | What to do |
|---|---|---|
| **Sign-in expired** | The provider's sign-in has expired | Kepler tries to refresh the token on its own; **Reconnect** is the manual fix |
| **Cannot connect to server** | Kepler couldn't reach the provider's server. The integration is still connected | Nothing to reconnect. Check that the server is up and reachable from your network or VPN; the warning clears once it answers |
| **Unexpected response** | The provider answered with data Kepler couldn't read, so some of its items may be missing. The integration is still connected | Reconnecting won't fix it. If it persists, check for a proxy or gateway between Kepler and the provider |
| An organization named under the row | One organization refuses Kepler's access, so its items are left out while everything else still loads. GitHub organizations that restrict OAuth app access, for example, are named with a **Request access on GitHub** link | Follow the row's own advice, which names who can lift the block |

You don't have to open Settings to find a failing provider. Todo, the **Add resources** lists, and a link preview name it too, with the one fix that applies: **Reconnect**, **Reconnect in settings** for a self-hosted provider, **Open settings**, or **Retry**. See [Pull Request Integrations](/kepler/pull-request-integrations#where-your-pull-requests-turn-up) for each warning.

***

## Choose what Kepler brings in

Each connected integration carries a visibility line under its row in **Settings → Integrations**. The line reads **Everything visible**, or **{count} hidden** with the number of items you've hidden. Trello has no visibility line.

To hide part of an integration:

1. Click **Choose what's visible…** on the provider's row. The **Choose what {name} brings in** dialog opens.
2. Clear the checkbox of each item to hide. Type in **Filter…** to narrow a long list.
3. Click **Save**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/provider-visibility-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/provider-visibility-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Choose what GitHub brings in dialog: hidden items are left out of the dashboard, the launcher and pickers, and tasks and branches already linked to them keep resolving. Under a Filter field, Organizations lists acme ticked and acme-labs unticked, and Repositories lists acme-labs/checkout-experiments unticked and greyed, marked Hidden with its organization, then acme/acme-api, acme/acme-web, acme/design-system and alex-lee/dotfiles ticked. Cancel and Save sit at the bottom.">
  </a>
  <figcaption style="text-align:center; color:#888">Hiding the acme-labs organization also hides its repositories.</figcaption>
</figure>

What the dialog lists depends on the provider:

| Provider | Lists |
|---|---|
| **GitHub**, **GitHub Enterprise**, **GitLab**, **GitLab Self-Hosted**, **Bitbucket**, **Bitbucket Data Center** | **Organizations** and **Repositories** |
| **Azure DevOps**, **Azure DevOps Server** | **Organizations**, **Repositories**, and **Projects** |
| **Jira**, **Jira Server / Data Center**, **Linear** | **Projects** |

A ticked item is visible. Hiding an organization also hides its repositories, which show *Hidden with its organization* and can't be ticked on their own. A hidden project leaves the issue lists but stays in the project pickers, and a project with no issue returned yet may be missing from the list.

Hidden items are left out of Todo, the issue and pull request lists, and the pickers. Tasks and branches already linked to a hidden item keep resolving. Kepler stores the choice on your GitKraken account, so it follows you to other machines where you sign in.

***

## More than one account of the same provider

You can connect several accounts of the same provider: two GitHub accounts, a work Jira site and a personal one. When a provider has two or more, an **Accounts** list appears under its row with one entry per account.

Each entry carries two independent controls:

| Control | What it changes | How far it reaches |
|---|---|---|
| **Read from this account** | Which account Kepler reads this provider's issues and pull requests from | Kepler only, and non-destructive |
| **Set as primary** / **Primary** | The provider's primary account | Everywhere: other Kepler windows, the `gk` CLI, and GitKraken Desktop |

**Browsing a secondary account does not change your primary.** Selecting **Read from this account** on a second account switches what Kepler shows you and leaves the primary alone. That's why **Read from this account** is a radio control rather than a button. The primary is the default read account, so a provider with no override reads through it.

Switching either one clears that provider's saved filters (an organization or project from the old account need not exist on the new one) and re-fetches the list.

**Reconnect keeps your choices.** When one account's sign-in fails, **Reconnect** renews that account's connection without disconnecting it first. Once the same account comes back, its new connection takes the old one's place, as primary or as the read account if it was either, and Kepler removes the old one. Another account of the provider never becomes primary by accident.

The read account also authenticates git. Starting work on an issue in a repository you have never cloned makes Kepler clone that repository, using the same connection it reads through. See [Pull Request Integrations](/kepler/pull-request-integrations) for which hosts this covers and what happens on the hosts it does not.

**Linear connections stay separate by workspace.** Each Linear account's entry shows *Workspace: {workspace}*, the Linear workspace that connection was granted. Two connections to different workspaces are separate accounts, so Kepler never reads one workspace's issues through another workspace's connection.

***

## Disconnect a provider

Click **Disconnect** on the provider's row in **Settings → Integrations** and confirm.

Disconnecting reaches further than Kepler: it removes the connection from your GitKraken account, so the `gk` CLI and GitKraken Desktop lose it too. What happens to the provider depends on whether you have another account connected:

- **With another account connected**, Kepler promotes it to primary and the provider stays connected under it. Nothing else changes.
- **With no other account connected**, the provider is removed entirely. Kepler drops its saved filters and its rows from your lists, so nothing lingers behind pointing at a provider you no longer have.

You can reconnect at any time.

***

## Jira, Linear, and Trello have no pull requests

Kepler keeps two separate lists of what each provider can return: which providers can list issues, and which can list pull requests. Jira (Cloud, Server, and Data Center), Linear, and Trello are on the first list only.

Two consequences you will notice:

- **Kepler never asks them for pull requests.** Kepler excludes them from the pull-request read instead of querying and ignoring them.
- **The interface hides the dead filters.** A provider filter only offers providers that can return results for what you are looking at, so Jira never appears as a pull-request filter. In the list, Kepler builds facets from the rows actually loaded, so a facet with nothing to offer never appears.

The same rule runs the other way for Bitbucket and Bitbucket Data Center, which have no issues.

***

## What Kepler reads from an issue

When an issue becomes a task, Kepler attaches what it read, so the agent starts with that context instead of asking for it. Kepler pulls these fields from the issue:

| Field | Notes |
|---|---|
| **Identifier** | The issue key or number: `GK-1234` for Jira, `DRE-2` for Linear, a number for GitHub, GitLab, and Azure DevOps |
| **Title** | |
| **Description** | The issue body. When an Azure DevOps work item keeps its content in another field, such as **Repro Steps** on a Bug, Kepler reads that field and labels the description with its name |
| **Issue type** | The provider's own vocabulary: a Jira issue type, an Azure DevOps work item type |
| **Author** | When the provider reports one |
| **Assignees** | |
| **Status** | The issue's current state, in the provider's own words (a Jira *To Verify* rather than a generic *open*), when the provider reports one |
| **Last updated** | When the issue was last updated |
| **Labels** | The provider's own labels, shown as badges in issue previews. Kepler distinguishes "this issue has no labels" from "this provider cannot report labels" |
| **Project or board** | Jira projects, Linear teams, Azure DevOps areas. Git hosts hang issues off a repository instead |
| **Iteration or sprint** | Azure DevOps iterations and Jira sprints. A Jira issue carried across sprints keeps them all |
| **Repository** | Name, owner, and host, for the git hosts |
| **URL** | Used by the open control, which names the provider: **Open on GitHub**, **Open on Jira**, and so on |

Kepler does not read an issue's priority field, due date, milestone, Trello checklist, or Linear cycle. An agent can still find these by opening the issue's URL itself, but Kepler does not deliver them as attached context. Todo's **Priority** grouping and filter come from labels instead: a label such as `P1`, `priority: high`, `blocker`, or `critical` sets the level, and the most urgent label wins. Jira and Linear keep priority in a field Kepler doesn't read, so their issues show as **Unprioritised** unless a label says otherwise. See [Arranging Your Work](/kepler/arranging-your-work).

Kepler converts descriptions to Markdown when the provider stores them in another format: Jira's wiki markup and Azure DevOps work items' HTML. Headings, code blocks, and tables then read the same in Kepler's previews and in the agent's context. Images embedded in an issue's description, including Jira and Azure DevOps attachments, display in Kepler's issue previews. On a self-hosted server (GitHub Enterprise, GitLab Self-Hosted, Azure DevOps Server, or Jira Server / Data Center) they stay blocked and don't display, though the server's member avatars do. The agent receives the description as text: Kepler does not pass the attachments or images themselves.

### Comments

When you open an issue in a reader, either the task panel's side pane or the issue's pane on the task page, a **Comments** section under the summary shows its discussion. Kepler reads comments for **GitHub**, **GitHub Enterprise**, **GitLab**, **GitLab Self-Hosted**, **Jira**, and **Jira Server / Data Center**, through the same connection it reads the issue with. For other providers the section says comments for that provider aren't available in Kepler yet.

Kepler reads up to the newest 100 comments, shows the latest ones with the newest at the bottom, and offers **Show earlier comments** for the rest it read. **Refresh comments** reads the discussion again. Each comment shows its author, when it was posted, and its body as Markdown. Comments are for you to read: Kepler shows them in the reader but doesn't attach them to the task or hand them to the agent.

### Which issues Kepler lists

Kepler lists open work. An issue that's finished or cancelled in its tracker (a Linear issue in *Done* or *Canceled*, for example) drops out of **Todo** and the issue pickers. An issue already attached to a task keeps showing on that task with its real state, finished or not.

**Todo** shows the issues related to you on each connected integration, across every organization you belong to. Providers answer different questions about you, so what counts as related differs:

| Provider | Issues Todo lists |
|---|---|
| **GitHub**, **GitHub Enterprise** | Yours, assigned to you, or mentioning you |
| **GitLab**, **GitLab Self-Hosted**, **Azure DevOps**, **Azure DevOps Server** | Yours or assigned to you |
| **Jira**, **Jira Server / Data Center**, **Linear**, **Trello** | Assigned to you |

An issue that's there only because you were mentioned is marked **Mentioned**, so you can tell it apart from work that's yours. Hover the **Related to me** chip in Todo's header to see the rule for each integration you have connected.

<figure style="text-align:center">
  <a href="/wp-content/uploads/todo-scope-tooltip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/todo-scope-tooltip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Related to me chip on Todo with its tooltip: Related to me, Across every organization you belong to, then one block per connected integration. Azure DevOps lists Issues: Yours or assigned to you and Pull requests: Yours or awaiting your review; GitHub lists Issues: Yours, assigned to you or mentioning you and Pull requests: Yours, assigned to you or ones you review. It ends with To browse everything else, use New task → Issues → All visible.">
  </a>
  <figcaption style="text-align:center; color:#888">The Related to me tooltip states Todo's scope for each connected integration.</figcaption>
</figure>

To browse beyond that, use **All visible** in the issue list of **Add resources**. For GitHub and Azure DevOps it reads every issue across your organizations, including repositories you can read outside them, such as ones you're an outside collaborator on, and it loads more slowly. Jira and Linear show only your issues there until you pick a project or a team:

- **Jira**: when the issue list shows Jira alone, a project picker appears, starting with **All projects**. Pick a project to see every open issue in it. Kepler remembers the pick for each Jira connection.
- **Linear**: when the issue list shows Linear alone, a team picker and a **Project** picker appear. Pick a team, a Linear project, or both, to see every open issue in them, whoever it's assigned to. The **Project** picker starts at **All projects** and lists your Linear workspace's projects by name with their state (**Backlog**, **Planned**, **Started**, **Paused**, **Completed**, or **Canceled**), closed ones included. A Linear project can span teams, so the two pickers narrow together. Changing the team clears the project pick.

<!-- TODO(screenshot): New — ade-linear-project-picker-01: the Add to this task dialog on its Issues tab with Linear selected and the Project picker open on All projects and the workspace's projects, each with its state. -->

**A Linear issue synced with GitHub shows once.** When Linear's GitHub Issues sync keeps a two-way copy of a Linear issue on GitHub, Kepler pairs the two and lists them as one row, the Linear issue, with the filter counts to match. Open the GitHub copy's own panel and it lists on its own again. The pair shares one task history, so a task started from either copy is the issue's task, whichever copy you look at. Starting work from the Linear issue uses the repository of its GitHub copy, when exactly one repository you have in Kepler matches it; otherwise the Linear issue's own repository choice applies. Kepler pairs a copy only on GitHub or GitHub Enterprise Cloud that you're connected to, never GitHub Enterprise Server, and only one-to-one: a Linear issue synced with several GitHub issues, or two Linear issues claiming one copy, isn't paired.

***

## Where your issues turn up

Your issues turn up in three places:

| Surface | What it gives you |
|---|---|
| [The Kepler interface](/kepler/kepler-interface) | The **Todo** segment lists your issues across every connected tracker, grouped and filtered how you like |
| [Actions](/kepler/actions) | The **Action** button on a row hands the issue to an agent with its context attached. Firing an Action on an untracked issue is also how it becomes a task |
| [Tasks and Resources](/kepler/tasks-and-resources) | An issue is a resource on a task, so you can attach one to work that already exists |

The **Issue type**, **Label**, **Project**, and **Status** filters carry your provider's own vocabulary rather than a Kepler translation of it. Azure DevOps and Jira issues also filter by **Iteration** and **Sprint**, each named the way its tracker names it.

Kepler recognizes an issue from its URL when you paste or attach one, including these work item URLs:

- **GitLab** work items, at `/-/work_items/<number>` in a project. Kepler stores them as issues of that project. A group-level work item belongs to no repository, so it stays a plain URL.
- **Azure DevOps** work items, at `/<organization>/<project>/_workitems/edit/<number>` or at the organization level, `/<organization>/_workitems/edit/<number>`.

**Search by key or link.** In the issue list of **Add resources**, type a Jira or Linear issue key, such as `OPS-42`, or paste a Jira Cloud, Jira Server / Data Center, Linear, or Azure DevOps work item link. Kepler looks that issue up directly from its tracker, whatever its state, rather than only filtering the rows already loaded. A Jira Server / Data Center link resolves when it points at an installation you have connected.

**Jira keys in commits and branches.** With Jira or Jira Server / Data Center connected, Kepler matches issue keys in commit messages and branch names against your Jira sites' own key patterns, so `OPS-42` in a commit message links to that issue. Right-click a commit in a worktree's commit list for **Open issue {issue}** and **Copy issue URL for {issue}** (see [Review Changes](/kepler/review-changes#the-changes-panel)), and the **Worktrees and branches** page shows the keys as chips on branch and worktree rows (see [Settings](/kepler/settings-repositories#worktrees-and-branches)). When two connected sites share a key, the label adds the site's address. Only Jira keys are linked this way; other trackers' issue references in a commit aren't.

**Pick from the list with the keyboard.** The issue list in **Add resources** has a preview pane and keyboard picking: arrows move between rows, **Space** selects, and **Enter** or a double-click adds. See [Picking issues and pull requests](/kepler/tasks-and-resources#picking-issues-and-pull-requests).

**Paste a link on the Links tab.** An issue URL pasted on the **Links** tab of **Add resources** is looked up and added as that issue, with **Add as plain link** to keep it a plain link. See [Pasting an issue link](/kepler/tasks-and-resources#pasting-an-issue-link).

**Paste a link into a prompt.** Paste an issue or pull request URL into a session's or a new task's composer and it becomes a link chip, which Kepler attaches to the task when you send. See [Sending a prompt](/kepler/agent-sessions#sending-a-prompt).

---
