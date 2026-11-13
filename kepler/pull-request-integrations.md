---
title: Pull Request Integrations
description: Connect your Git hosts to Kepler, cloud or self-hosted, so the pull requests you authored and the ones waiting on your review land in one list, already matched to the worktrees they belong to.
product: Kepler
feature: Pull Request Integrations
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, bitbucket-data-center, azure-devops, azure-devops-server]
integrations: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, bitbucket-data-center, azure-devops, azure-devops-server]
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [integrations, pull-requests, github, gitlab, bitbucket, bitbucket-data-center, azure-devops, self-hosted, worktrees, accounts, settings]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "kepler-integrations"
    nav_label: "Pull Request Integrations"
    nav_order: 40
    nav_parent: "kepler-integrations"
    page_type: "content"
    card_icon: "git-pull-request"
    card_color: "green"
    card_description: "Bring pull requests from your Git hosts, cloud or self-hosted, into one list"
---
<kbd>Last updated: November 2026</kbd>

Connect a Git host to see the pull requests you authored, and the ones waiting on your review, in [the Kepler interface](/kepler/kepler-interface). Kepler also matches each pull request to your existing worktrees, so a branch you are working on shows its pull request wherever the branch appears.

You manage providers in the **Issues and pull requests** section of **Settings → Integrations**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/provider-integrations-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/provider-integrations-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Issues and pull requests section of Settings › Integrations. Azure DevOps and GitHub read Connected, each with Disconnect and Reconnect and a visibility line, Everything visible, with Choose what's visible…; Azure DevOps lists two accounts, Alex Lee (primary) and Alex Lee (Contoso). Azure DevOps Server, Bitbucket, Bitbucket Data Center, GitHub Enterprise, GitLab, GitLab Self-Hosted, Jira, Jira Server / Data Center, Linear and Trello each offer Connect.">
  </a>
  <figcaption style="text-align:center; color:#888">Issues and pull requests, in Settings → Integrations.</figcaption>
</figure>

Each connected Git host has a visibility line under its row. The line reads **Everything visible**, or shows how many items you have hidden. To leave organizations or repositories out of Todo, the lists, and the pickers, click **Choose what's visible…**. See [Choose what Kepler brings in](/kepler/issue-tracker-integrations#choose-what-kepler-brings-in).

***

## Hosts Kepler can read pull requests from

Of Kepler's 13 providers, 8 return pull requests:

| Provider | Also returns issues |
|---|---|
| **GitHub** | Yes |
| **GitHub Enterprise** | Yes |
| **GitLab** | Yes |
| **GitLab Self-Hosted** | Yes |
| **Azure DevOps** | Yes |
| **Azure DevOps Server** | Yes |
| **Bitbucket** | No |
| **Bitbucket Data Center** | No |

Bitbucket and Bitbucket Data Center do not appear in issue filters.

The other 5 providers (Jira, Jira Server / Data Center, Linear, Trello, and Asana) return issues only. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

Kepler supports self-hosted instances. **GitHub Enterprise**, **GitLab Self-Hosted**, **Azure DevOps Server**, and **Bitbucket Data Center** read pull requests and merge requests the same way their cloud counterparts do. Which fields come back depends on your server's version.

You connect a self-hosted instance inside Kepler with its address and a personal access token. See [Connect a self-hosted instance](#connect-a-self-hosted-instance). Your machine needs to be able to reach the server. Kepler trusts the certificates in your operating system's certificate store, so a server signed by your company's own certificate authority works without extra setup.

Kepler shows GitLab merge requests as pull requests, in the same list.

***

## Connect a Git host

To connect a cloud Git host (**GitHub**, **GitLab**, **Bitbucket**, or **Azure DevOps**), follow these steps:

1. Open **Settings → Integrations**.
2. Find the provider in **Issues and pull requests** and click **Connect**.
3. Authorize Kepler on GitKraken's website, which opens in your browser.
4. Return to Kepler, where the provider shows a **Connected** badge.

Integrations belong to your GitKraken account, not to this copy of Kepler, so a provider you connect here is also available to the `gk` command-line interface (CLI) and GitKraken Desktop. To manage integrations, sign in to a GitKraken account.

If your browser did not open, copy the **Connection link** from the dialog Kepler shows while you authorize, and open it in a browser yourself. Each link works once, so **Try again** makes a new one. The dialog closes by itself once the connection appears. **Reconnect** uses the same dialog.

<!-- TODO(verify): the browser-side steps and the scopes each cloud provider asks for live on GitKraken's website (see help.gitkraken.com/gk-dev/gk-dev-integrations), outside the Kepler repo. Confirm the live browser connect steps and provider scopes for GitHub, GitLab, Bitbucket, and Azure DevOps with the web team. -->

### Connect a self-hosted instance

**GitHub Enterprise**, **GitLab Self-Hosted**, **Azure DevOps Server**, and **Bitbucket Data Center** connect inside Kepler with a personal access token rather than through the browser:

1. Open **Settings → Integrations**.
2. Find the provider in **Issues and pull requests** and click **Connect**. The **Connect *provider*** dialog opens.
3. In **Server URL**, enter the server's address, including the port and installation path when your server uses them.
4. In **Personal access token**, paste a token with access to the repositories you need.
5. Click **Save connection**.

The address must be `http` or `https`, without credentials, a query, or a fragment. Kepler checks the token against the server from your machine, saves it on this device, and adds the connection to your GitKraken account. The dialog reports how the check went:

| Message | What it means |
|---|---|
| *Credentials verified with the server.* | The server accepted the token |
| *Credentials saved. Unable to verify the server certificate. Check its TLS configuration.* | Kepler saved the token but could not verify the server's certificate |
| *Credentials saved without verification. Unable to reach the server.* | Kepler saved the token without checking it |
| *The server refused this token. Check its value and permissions.* | Fix the token and save again |

Until Kepler finishes syncing the connection to your account, the provider's row shows **Cloud sync pending**, and you cannot make that connection the primary. If Kepler cannot reach GitKraken, it retries when you refresh your providers.

Once connected, a self-hosted provider lists each server on its own row, with **Set as primary**, **Replace token**, and **Disconnect**. Each server keeps its own repositories and pull requests:

- To connect another server, click **Add connection** on the provider's row. Connecting more than 1 server needs an active GitKraken plan or trial.
- To renew an expired or rejected token, click **Replace token** on that server's row.
- To make a server the provider's default connection, click **Set as primary**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/self-hosted-installations-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/self-hosted-installations-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="GitHub Enterprise in Settings › Integrations with Add connection beside its name and one row per server below it: github.acme.example and ghe.contoso.example, each signed in as alex-lee and marked Connected, with Replace token and Disconnect, the primary server marked Primary and the other offering Set as primary. Below them, Everything visible with Choose what's visible…, and a notice that agents' GitKraken MCP server acts as alex-lee (https://github.acme.example), the primary connection on your GitKraken account.">
  </a>
  <figcaption style="text-align:center; color:#888">A self-hosted provider with 2 servers connected.</figcaption>
</figure>

Use these controls to manage connected providers:

| Control | What it does |
|---|---|
| **Reconnect** | Runs authorization again. Use it when a sign-in has expired |
| **Disconnect** | Removes the provider. See [Disconnect a provider](#disconnect-a-provider) |
| **Refresh** | At the top of the section, checks every provider again |

A provider's row can show a warning:

- **Sign-in expired**: the token needs refreshing. Kepler tries to refresh it by itself; **Reconnect** refreshes it by hand.
- **Cannot connect to server**: the integration is still connected, but Kepler could not reach the server. Instead of reconnecting, check that the server is up and reachable from your network or VPN.
- An organization named under the row: that organization refuses Kepler's access, such as a GitHub organization that restricts OAuth apps. Kepler leaves out only that organization's items.

See [Issue Tracker Integrations](/kepler/issue-tracker-integrations) for the warnings in full.

***

## Cloning a repository for a pull request

When you start work on a pull request from a repository you have never cloned, Kepler first clones the repository into your **Repositories folder** (**Settings → Repositories**). How the clone signs in depends on the host:

| Host | How the clone authenticates |
|---|---|
| **GitHub**, **GitHub Enterprise** | Your connected account's token |
| **GitLab**, **GitLab Self-Hosted** | Your connected account's token |
| **Bitbucket**, **Bitbucket Data Center**, **Azure DevOps**, **Azure DevOps Server** | Your own Git credentials |

A self-hosted repository clones through the account connected to that server. When a provider has more than one account, the clone uses the account Kepler reads from: **Read from this account** where you set one, otherwise the primary.

Kepler does not write the token into the clone's `.git/config` or the remote's URL.

If Kepler has no usable token for the host, the clone uses your own Git credential helper. Kepler cannot prompt you for Git credentials, so with no credential helper the clone fails. To fix it, sign in with a Git credential helper (for example, `gh auth login`) or use an SSH URL, then try again.

***

## More than one account of the same provider

You can connect several accounts of the same provider. When a provider has two or more, an **Accounts** list appears under its row with one entry per account.

Each entry carries two independent controls:

| Control | What it changes | How far it reaches |
|---|---|---|
| **Read from this account** | Which account Kepler reads this provider's pull requests and issues from | Kepler only, and non-destructive |
| **Set as primary** / **Primary** | The provider's primary account | Everywhere: other Kepler windows, the `gk` CLI, and GitKraken Desktop |

**Browsing a secondary account does not change your primary.** Selecting **Read from this account** on a second account switches what Kepler shows you and leaves the primary alone. The primary is the default read account, so a provider with no override reads through it.

**Agents keep acting as the primary account.** Your agents' GitKraken MCP server always uses the primary connection of your GitKraken account, even when Kepler reads a provider through another account.

Changing either one clears that provider's saved filters.

***

## Disconnect a provider

Click **Disconnect** on the provider's row in **Settings → Integrations** and confirm.

<figure style="text-align:center">
  <a href="/wp-content/uploads/disconnect-provider-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/disconnect-provider-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="GitHub's row in Settings › Integrations, with its Connected badge, Disconnect and Reconnect.">
  </a>
  <figcaption style="text-align:center; color:#888">A connected provider's row.</figcaption>
</figure>

Disconnecting affects more than Kepler: it removes the connection from your GitKraken account, so the `gk` CLI and GitKraken Desktop lose it too. What happens to the provider depends on whether you have another account connected:

- **With another account connected**, Kepler promotes it to primary and the provider stays connected under it. Nothing else changes.
- **With no other account connected**, Kepler removes the provider entirely, with its saved filters and its rows in your lists.

You can reconnect at any time.

***

## How pull requests attach to worktrees

Kepler matches a pull request to a worktree by its branch, so a branch shows its pull request, even after the pull request merges.

### Auto-attaching a matched pull request

When you open a pull request outside Kepler (with `gh` in a terminal, from GitKraken Desktop, or on the web), Kepler attaches it to the task for you. The pull request then behaves like one you attached yourself: it appears in the task's resources, and the agent receives it as context. See [Tasks and Resources](/kepler/tasks-and-resources).

Kepler attaches only an open pull request that is yours, from a branch that matches a worktree's branch on an active task in the same repository. To link a teammate's pull request, attach it yourself.

Kepler never removes or replaces a link. Several active tasks can share one pull request.

***

## What Kepler reads from a pull request

Kepler reads these fields from a pull request:

| Field | Notes |
|---|---|
| **Number and title** | |
| **Description** | The pull request body |
| **State** | **Open**, **Draft**, **Merged**, or **Closed** |
| **Repository** | Name, owner, and host |
| **Author** | When the provider reports one. A row shows **Yours** for a pull request you authored, and **Review** for someone else's |
| **Head and base branch** | When the provider reports them |
| **Fork** | Whether the head branch lives on a fork, and where |
| **Created at** | |
| **Checks and review** | Shown on an open or draft pull request's chip in a task panel: failing, pending, or passing checks, and an approved review |
| **URL** | Used by the open control, which names the provider: **Open on GitHub**, **Open on Bitbucket**, and so on |

<!-- TODO(verify): at v0.16.0 Kepler's pull request data also carries reviewers, assignees, mergeability, and when it was last updated, which the table above does not list (checks and the review decision are answered by v0.19.0). Confirm which of these Kepler shows or hands to the agent before adding them. Also confirm with engineering what supplies review comments and the diff to a Review or Address Feedback run before documenting them. -->

A merged pull request keeps its description and author for as long as a task, archived or not, still links it.

Images embedded in a pull request's description display in Kepler's previews, including on GitHub Enterprise, GitLab Self-Hosted, and Azure DevOps Server.

***

## Where your pull requests turn up

Your pull requests appear in 4 places:

| Surface | What it gives you |
|---|---|
| [The Kepler interface](/kepler/kepler-interface) | A **Todo** view lists the pull requests related to you on each connected host, or every open one in the repositories added to Kepler |
| [Actions](/kepler/actions) | The **Action** button hands the pull request to an agent. **Review** and **Address Feedback** are the 2 built-in Actions for pull requests, and Kepler picks one based on who authored the pull request |
| [Review Changes](/kepler/review-changes) | Reading the diff and the commits behind a pull request |
| [Tasks and Resources](/kepler/tasks-and-resources) | A pull request is a resource on a task, so you can attach one to work that already exists |

**Todo's scope.** A Todo view's **View** menu sets its **Scope**: **Mine**, the work related to you, or **All**, which adds the open pull requests of the repositories added to Kepler on every Git host above. See [Which issues Kepler lists](/kepler/issue-tracker-integrations#which-issues-kepler-lists).

Under **Mine**, each provider reports a different set of pull requests related to you, so Todo lists these from each:

| Host | Pull requests Todo lists |
|---|---|
| **GitHub**, **GitHub Enterprise** | Yours, assigned to you, or ones you review |
| **GitLab**, **GitLab Self-Hosted**, **Azure DevOps**, **Azure DevOps Server**, **Bitbucket Data Center** | Yours or awaiting your review |
| **Bitbucket** | Yours, or awaiting your review in your workspaces and repositories added to Kepler |

The pull request list on a task's **Resources** screen has its own scope menu: **Related to me** or **All in my repos**.

**Review requests come from every host.** Pull requests waiting on your review show up from every Git host above. On a large Bitbucket workspace, review requests can take a while to appear.

**Lists stay current while you look at them.** Pull request and issue lists refresh while they are on screen, and again when you come back to the window. When one provider fails to load, the others keep loading, and the failed provider's last loaded pull requests stay in the list.

**A failing provider is named, with its fix.** When a connected provider's read fails, Todo, the **Resources** screen's lists, and a link preview show a warning that names the provider and the fix, such as *Sign in to GitHub again to load its work.* Each warning offers one fix:

| What went wrong | The fix offered |
|---|---|
| The sign-in needs renewing | **Reconnect**, or **Reconnect in settings** for a self-hosted provider, which needs a new token |
| The provider refused part of the request, so some organizations or repositories are missing | **Open settings** |
| Rate limiting, an unreachable server, an unreadable answer, or a temporary problem | **Retry** |

On Todo, each warning also has **Filter out *provider***, which hides that provider from the Todo view so it stops reporting the failure. To show the provider again, clear it in the view's **Provider** filter.

Rows kept from the last good load show a cloud mark on their provider chip.

<figure style="text-align:center">
  <a href="/wp-content/uploads/todo-provider-failure-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/todo-provider-failure-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="Todo when GitHub refuses its sign-in: Unable to load your work, over a warning that reads Sign in to GitHub again to load its work, with a Reconnect button and, beside it, a crossed-out eye button, Filter out GitHub.">
  </a>
  <figcaption style="text-align:center; color:#888">Todo names a provider whose sign-in failed and offers Reconnect, or Filter out.</figcaption>
</figure>

**The pull request picker says why its list is empty.** When you add a pull request from the **Resources** screen, the picker explains an empty list:

- If the **Linked work** filter hides pull requests, the picker says how many it hides and which filter hides them, and offers **Show all**.
- If no connected provider can list pull requests, the picker reads **Connect your code host** and lists the providers that can fill the tab, each with **Connect**.

The **Linked work** filter defaults to **No active task**, which shows pull requests with no task or with archived tasks only. A task counts as active until you archive it, so Done and on-hold tasks count. To see every pull request, choose **Any**.

A row with task history carries a badge that says how many tasks it belongs to, and whether they are archived.

When nothing you have connected can list issues or pull requests, **Add issue** and **Add PR** in the **New task** composer open on a connect view, **Connect where your work lives**. Connect each provider you use, then click **Continue**. On the **Resources** screen, an empty list offers **Connect your code host** or **Connect your issue tracker** instead.

You can also start work on a pull request from GitLens or GitKraken Desktop. See [Create a task](/kepler/create-task).

---
