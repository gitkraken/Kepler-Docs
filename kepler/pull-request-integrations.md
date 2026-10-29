---
title: Pull Request Integrations
description: Connect your Git hosts to Kepler, cloud or self-hosted, so the pull requests you authored and the ones waiting on your review land in one list, already matched to the worktrees they belong to.
product: Kepler
feature: Pull Request Integrations
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
integrations: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, azure-devops]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [integrations, pull-requests, github, gitlab, bitbucket, bitbucket-data-center, azure-devops, self-hosted, worktrees, accounts, settings]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Connect a Git host and the pull requests you authored, plus the ones waiting on your review, show up in [the Kepler interface](/kepler/kepler-interface). Kepler also matches them to the worktrees you already have, so a branch you are working on carries its pull request wherever you see it.

Manage providers in **Settings → Integrations**, in the **Issues and pull requests** section.

<figure style="text-align:center">
  <a href="/wp-content/uploads/provider-integrations-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/provider-integrations-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Issues and pull requests section of Settings › Integrations. Azure DevOps and GitHub read Connected, each with Disconnect and Reconnect and a visibility line, Everything visible, with Choose what's visible…; Azure DevOps lists two accounts, Alex Lee (primary) and Alex Lee (Contoso). Azure DevOps Server, Bitbucket, Bitbucket Data Center, GitHub Enterprise, GitLab, GitLab Self-Hosted, Jira, Jira Server / Data Center, Linear and Trello each offer Connect.">
  </a>
  <figcaption style="text-align:center; color:#888">Issues and pull requests, in Settings → Integrations.</figcaption>
</figure>

Each connected Git host carries a visibility line under its row, which reads **Everything visible** or how many items you've hidden. Click **Choose what's visible…** to leave organizations or repositories out of Todo, the lists, and the pickers. See [Choose what Kepler brings in](/kepler/issue-tracker-integrations#choose-what-kepler-brings-in).

***

## Hosts Kepler can read pull requests from

Eight of Kepler's twelve providers return pull requests:

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

Jira, Jira Server / Data Center, Linear, and Trello are the other four. They return issues only. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

Self-hosted instances are supported. **GitHub Enterprise**, **GitLab Self-Hosted**, **Azure DevOps Server**, and **Bitbucket Data Center** read pull requests and merge requests the same way their cloud counterparts do, and two servers of the same kind stay separate; which fields come back depends on your server's version. You connect a self-hosted instance inside Kepler with its address and a personal access token, and Kepler checks the token against the server from your machine (see [Connect a Git host](#connect-a-git-host)). The instance must be reachable both from your machine and from gitkraken.dev, so a server that's only reachable inside your network or VPN can't be connected. <!-- TODO(verify): v0.15 checks the personal access token from this machine; confirm with engineering whether syncing it to the account still needs gitkraken.dev to reach the server --> Kepler trusts the certificates in your operating system's certificate store, so a server signed by your company's own certificate authority works without extra setup.

GitLab merge requests appear as pull requests throughout Kepler. There is one list, not two.

***

## Connect a Git host

Connecting a cloud Git host (**GitHub**, **GitLab**, **Bitbucket**, or **Azure DevOps**) takes four steps:

1. Open **Settings → Integrations**.
2. Find the provider in **Issues and pull requests** and click **Connect**.
3. Authorize Kepler in the browser window that opens.
4. Return to Kepler, where the provider shows a **Connected** badge in **Issues and pull requests**.

Your GitKraken account holds integrations, not this copy of Kepler, so a provider you connect here also becomes available to the `gk` command-line interface (CLI) and GitKraken Desktop. You need to sign in to a GitKraken account to manage them.

**Connect** hands the authorization for a cloud host to GitKraken's website. Kepler opens `/connect` there in your system browser, names the provider, and includes a redirect back into Kepler. When you return, Kepler refetches your providers instead of reusing its cached list.

While you authorize, Kepler keeps a **Connect {provider} in your browser** dialog open, with the provider's name in place of {provider}. If your browser didn't open, copy the **Connection link** from the dialog and open it in a browser yourself. **Try again** makes a fresh link, since each link works once. The dialog closes by itself as soon as the new connection appears, and Kepler checks for it again whenever you come back to a Kepler window. If Kepler can't start the connection, the dialog reads **Unable to connect {provider}** and says why. **Reconnect** runs through the same dialog.

<!-- TODO(verify): the browser-side steps and the scopes each cloud provider asks for live on GitKraken's website (see help.gitkraken.com/gk-dev/gk-dev-integrations), outside the Kepler repo. Confirm the live /connect steps and provider scopes for GitHub, GitLab, Bitbucket, and Azure DevOps with the web team. Self-hosted providers no longer use this flow at v0.15 (src/ui/components/settings/SelfHostedProviderDialog.tsx). -->

### Connect a self-hosted instance

**GitHub Enterprise**, **GitLab Self-Hosted**, **Azure DevOps Server**, and **Bitbucket Data Center** connect inside Kepler with a personal access token rather than through the browser:

1. Open **Settings → Integrations**.
2. Find the provider in **Issues and pull requests** and click **Connect**. The **Connect {name}** dialog opens.
3. In **Server URL**, enter the server's address, including the port and installation path when your server uses them.
4. In **Personal access token**, paste a token with access to the repositories you need.
5. Click **Save connection**.

Kepler accepts only an `http` or `https` address without credentials, a query, or a fragment. It checks the token against the server from your machine, keeps it in a protected credential store on this device, and syncs the connection to your GitKraken account. The dialog reports how the check went:

| Message | What it means |
|---|---|
| *Credentials verified with the server.* | The server accepted the token |
| *Credentials saved. Unable to verify the server certificate. Check its TLS configuration.* | Kepler saved the token but couldn't verify the server's certificate |
| *Credentials saved without verification. Unable to reach the server.* | Kepler saved the token without checking it |
| *The server refused this token. Check its value and permissions.* | Fix the token and save again |

Until the upload to your account lands, the provider's row shows **Cloud sync pending**, and you can't make that connection the primary. If Kepler can't reach GitKraken, it retries when you refresh your providers. **Reconnect** on a self-hosted provider opens the same dialog, so you can replace an expired or rejected token there.

Three controls sit on a connected provider's row:

| Control | What it does |
|---|---|
| **Reconnect** | Re-runs authorization. Use it when a sign-in has expired |
| **Disconnect** | Removes the provider (see below) |
| **Refresh** | At the top of the section, re-checks every provider |

A row marked **Sign-in expired** needs its token refreshed. Kepler tries to do that itself; **Reconnect** is the manual fix. A row marked **Cannot connect to server** is different: the integration is still connected, but Kepler couldn't reach the server, so check that it's up and reachable from your network or VPN rather than reconnecting. When one organization refuses Kepler's access, such as a GitHub organization that restricts OAuth apps, Kepler names it under the row and leaves only its items out. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations) for the warnings in full.

***

## Cloning a repository you don't have

Starting work on a pull request whose repository you have never cloned makes Kepler clone that repository first, into your **Default Repositories Folder**. That clone authenticates with the provider token your connected GitKraken account already holds, the same connection the pull request itself came through. As a result, a private repository clones without you having to set up a git credential helper. Kepler authenticates the clone differently depending on the host:

| Host | How the clone authenticates |
|---|---|
| **GitHub**, **GitHub Enterprise** | Your connected account's token |
| **GitLab**, **GitLab Self-Hosted** | Your connected account's token |
| **Bitbucket**, **Bitbucket Data Center**, **Azure DevOps**, **Azure DevOps Server** | Falls through to your own git credentials |

For an enterprise or self-managed host, Kepler matches the clone's host against the domain stored on your connection, so the repository clones through the account connected to that instance rather than through a cloud account of the same family. When a provider has more than one account, the clone follows the same choice your reads follow: **Read from this account** where you set one, otherwise the primary.

Kepler hands the token to that one git process and nothing more. Kepler does not write it into the clone's `.git/config`, does not add it to the remote's URL, and never exposes it to the interface.

Where Kepler holds no usable token for the host, the clone falls back to your own git credential helper. Kepler never lets git open an interactive prompt, so when no credential helper is available, the clone fails with a message that names the host and tells you what to do: *git has no saved credentials for this remote and Kepler cannot prompt for them. Sign in with a git credential helper (e.g. `gh auth login`, or the macOS keychain helper) or use an SSH url, then try again.*

***

## More than one account of the same provider

You can connect several accounts of the same provider. When a provider has two or more, an **Accounts** list appears under its row with one entry per account.

Each entry carries two independent controls:

| Control | What it changes | How far it reaches |
|---|---|---|
| **Read from this account** | Which account Kepler reads this provider's pull requests and issues from | Kepler only, and non-destructive |
| **Set as primary** / **Primary** | The provider's primary account | Everywhere: other Kepler windows, the `gk` CLI, and GitKraken Desktop |

**Browsing a secondary account does not change your primary.** Selecting **Read from this account** on a second account switches what Kepler shows you and leaves the primary alone. The primary is the default read account, so a provider with no override reads through it.

Switching either one clears that provider's saved filters (a repository from the old account need not exist on the new one) and re-fetches the list.

***

## Disconnect a provider

Click **Disconnect** on the provider's row in **Settings → Integrations** and confirm.

<figure style="text-align:center">
  <a href="/wp-content/uploads/disconnect-provider-aug-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/disconnect-provider-aug-2026-v2@2x.png" class="help-center-img img-bordered" alt="GitHub's row in Settings › Integrations, with its Connected badge, Disconnect and Reconnect.">
  </a>
  <figcaption style="text-align:center; color:#888">A connected provider's row.</figcaption>
</figure>

Disconnecting reaches further than Kepler: it removes the connection from your GitKraken account, so the `gk` CLI and GitKraken Desktop lose it too. What happens to the provider depends on whether you have another account connected:

- **With another account connected**, Kepler promotes it to primary and the provider stays connected under it. Nothing else changes.
- **With no other account connected**, the provider is removed entirely. Kepler drops its saved filters and its rows from your lists, so nothing lingers behind pointing at a provider you no longer have.

You can reconnect at any time.

***

## Bitbucket has no issues

Kepler keeps two separate lists of what each provider can return. Bitbucket and Bitbucket Data Center are on the pull-request list only, so Kepler never asks them for issues, and a provider filter for issues never offers them. In the list, Kepler builds facets from the rows actually loaded, so a facet with nothing to offer never appears.

The same rule runs the other way for Jira, Linear, and Trello, which have no pull requests.

***

## How pull requests attach to worktrees

Kepler matches a pull request to a worktree by **branch**, and it tries the worktree's **upstream branch** as well as its local one.

That second pass matters when the two names differ. If your local branch is `fix-login` but it tracks `origin/justin/fix-login`, matching on the local name alone finds nothing. The pull request's head branch is the upstream name. Kepler runs a second pass against the short branch of the tracking ref and catches it.

Matching runs against open and closed pull requests together, so a merged pull request still shows on the branch it merged from.

### Confirmed against inferred

Every link Kepler shows records **how** it was made, so you can tell a hard link from a guess:

| How the link was made | Reads as | What it means |
|---|---|---|
| Recorded on the task | Confirmed | The link is authoritative. Kepler records one when you launch the task from the pull request, when an agent opens a pull request, when you attach one yourself, or through the branch auto-attach below |
| The pull request's head branch matched the worktree's local branch | Confirmed | A direct branch match |
| The head branch matched the worktree branch's **upstream** branch | Confirmed, and marked | Git-native rather than a guess, but the local name differs, so Kepler labels it **Matched from upstream branch** |
| An identifier parsed out of the branch name | Inferred | A heuristic. Issues only: pull requests are never linked this way |

A confirmed link carries no extra marking. Kepler underlines with a dotted line any link it wants you to look twice at, and its tooltip says why: **Matched from upstream branch**, or **Matched from branch name** for an inferred issue link.

When Kepler finds one pull request more than one way, the most authoritative wins: the task's own recorded link, then a local branch match, then an upstream branch match.

Kepler scopes branch matching to each item's own repository, so two repositories with a branch of the same name do not borrow each other's pull requests.

### Auto-attaching a matched pull request

A pull request you open outside Kepler (from a terminal `gh`, from GitKraken, from the web) doesn't stay a read-time match. Kepler records it on the task for you.

Whenever fresh pull-request data arrives, Kepler looks over your active tasks that hold no pull request yet and attaches one whose head branch matches a worktree's branch. It then behaves like a pull request you attached yourself: it sits in the task's resources, and it reaches the agent as context. See [Tasks and Resources](/kepler/tasks-and-resources).

Auto-attaching is deliberately stricter than the matching above, because Kepler saves an attached resource and sends it to an agent, where a read-time match only draws a card. Auto-attach follows five rules:

| Rule | Why |
|---|---|
| Exact matches only | The pull request's head branch has to be the worktree's own branch name, and its repository has to match a remote exactly. The upstream-branch pass and the rename-tolerant fallback still draw the card; neither attaches |
| Open pull requests only | A merged pull request cannot claim a branch name that gets reused later |
| The head branch has to live in the same repository | Branch matching keys on the head branch name, and the author of a fork picks that name freely. An attached resource reaches your agent, so a stranger's pull request must not claim your branch |
| One pull request per task per pass | A task drops out of the next pass as soon as it holds one |
| A pull request another active task already holds is left alone | One active task per pull request, without taking it off the task that has it |

Auto-attach never archives anything and never replaces anything. A branch match is a guess, so it never supersedes work you started deliberately, and it never removes a link because a pull request briefly dropped out of a read.

***

## What Kepler reads from a pull request

Kepler pulls these fields from a pull request:

| Field | Notes |
|---|---|
| **Number and title** | |
| **Description** | The pull request body |
| **State** | Kepler derives one of **Open**, **Draft**, **Merged**, or **Closed** |
| **Repository** | Name, owner, and host |
| **Author** | When the provider reports one. Kepler also tracks whether you authored it, which is what splits **Yours** from **Review** on a row |
| **Head and base branch** | When the provider reports them. These drive branch matching and the branch a task starts from |
| **Fork** | Whether the head branch lives on a fork, and where, so Kepler can fetch it from the fork remote instead of `origin` |
| **Created at** | |
| **URL** | Used by the open control, which names the provider: **Open on GitHub**, **Open on Bitbucket**, and so on |

<!-- TODO(verify): re-checked field by field against the shared PullRequest shape in src/shared/provider/pull-request.ts at kepler 7c31af83e. It's unchanged, and the table above is complete apart from the base-repo clone URLs, which only prefill the Clone form. The June 2026 version of this page also claimed Kepler pulls the diff, open review comments, and the current review state when you attach a pull request; none of those are fields on this shape. Confirm with engineering which path supplies review comments and the diff to a Review or Address Feedback run before documenting them. -->

A merged pull request keeps its description and author for as long as a task, archived or not, still links it.

On a self-hosted server (GitHub Enterprise, GitLab Self-Hosted, Azure DevOps Server, or Bitbucket Data Center), images embedded in a pull request's description stay blocked and don't display in Kepler's previews. The server's member avatars still load.

Azure DevOps reports pull requests without a usable number, so Kepler identifies them by URL instead. You should not see a difference; identifying by URL is why a pull request you look up by link resolves correctly there.

***

## Where your pull requests turn up

Your pull requests turn up in four places:

| Surface | What it gives you |
|---|---|
| [The Kepler interface](/kepler/kepler-interface) | The **Todo** segment lists the pull requests related to you on each connected host, with your role on each |
| [Actions](/kepler/actions) | The **Action** button hands the pull request to an agent. **Review** and **Address Feedback** are the two built-in Actions aimed at pull requests, and Kepler picks between them by who authored it |
| [Review Changes](/kepler/review-changes) | Reading the diff and the commits behind a pull request |
| [Tasks and Resources](/kepler/tasks-and-resources) | A pull request is a resource on a task, so you can attach one to work that already exists |

**Todo's scope differs by host.** Each provider answers a different set of questions about you, so Todo lists a different set of pull requests from each:

| Host | Pull requests Todo lists |
|---|---|
| **GitHub**, **GitHub Enterprise** | Yours, assigned to you, or ones you review |
| **GitLab**, **GitLab Self-Hosted**, **Azure DevOps**, **Azure DevOps Server**, **Bitbucket Data Center** | Yours or awaiting your review |
| **Bitbucket** | Yours, or awaiting your review in your workspaces and repositories added to Kepler |

Hover the **Related to me** chip in Todo's header to see the rule for each integration you have connected. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations#which-issues-kepler-lists) for the issue side.

**Review requests come from every host.** Pull requests waiting on your review show up from Azure DevOps, Azure DevOps Server, and Bitbucket Data Center as well as GitHub and GitLab. Bitbucket Cloud has no account-wide way to ask for them, so Kepler reads review requests repository by repository, starting with the repositories you have in Kepler and then the rest of your workspaces at a pace that stays inside Bitbucket's hourly request limits. On a large workspace they can take a while to appear.

**Kepler loads what you're looking at.** Pull request and issue lists refresh while they're on screen, and again when you come back to the window, rather than downloading your whole account's lists in the background. A task's own pull requests refresh when an agent ends a turn, a branch is pushed, or a pull request is published. When one provider fails to load, the others keep loading, and the failed provider's last loaded pull requests stay in the list.

**A failing provider is named, with its fix.** When a connected provider's read fails, Todo, the **Add resources** lists, and a link preview show a warning that names the provider and what went wrong, such as *GitHub needs you to sign in again, so its work may be missing.* On Todo the warning sits under **Unable to load your work**. Each warning offers one fix:

| What went wrong | The fix offered |
|---|---|
| The sign-in needs renewing | **Reconnect**, or **Reconnect in settings** for a self-hosted provider, which needs a new token |
| The provider refused part of the request, so some organizations or repositories may be missing | **Open settings** |
| Rate limiting, an unreachable server, an unreadable answer, or a temporary problem | **Retry** |

Rows kept from the last good load carry a cloud mark on their provider chip, labeled *Not refreshed: shown from the last successful {provider} load.*

<figure style="text-align:center">
  <a href="/wp-content/uploads/todo-provider-failure-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/todo-provider-failure-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Todo when GitHub refuses its sign-in: Unable to load your work, over a warning that reads GitHub needs you to sign in again, so its work may be missing, with a Reconnect button.">
  </a>
  <figcaption style="text-align:center; color:#888">Todo names a provider whose sign-in failed and offers Reconnect.</figcaption>
</figure>

**The pull request picker says why its list is empty.** When you attach a pull request from **Add resources**, the picker explains an empty list instead of showing *No matches*:

- If the **Linked work** filter hides pull requests, the picker says how many it hides and which filter hides them, and offers **Show all**.
- If no connected provider can list pull requests, the picker reads **Connect your code host** and lists the providers that can fill the tab, each with **Connect**.

The **Linked work** filter defaults to **No active task**. A task counts as active until you archive it, so Done and on-hold tasks count. The filter has five options:

| Option | Shows pull requests |
|---|---|
| **Any** | Whatever their task history |
| **No active task** | With no task, or with archived tasks only. This default keeps earlier work findable, so you don't duplicate it |
| **No tasks ever** | Never linked to a task |
| **Has an active task** | Linked to at least one task that isn't archived |
| **Archived tasks only** | Linked only to archived tasks |

A row with task history carries a badge: **Task** or **{count} tasks** when one of them is active, **Archived task** or **{count} archived tasks** when all are archived.

When nothing you have connected can list issues or pull requests, **Add resources** opens on a connect view, **Connect where your work lives**, with a tile for each provider. Connect each one you use, then click **Continue**. The provider filter's menu also offers **Connect another provider…**, which opens the same view with a **Back** button.

You can also start work on a pull request from GitLens or GitKraken Desktop. See [Create a Task](/kepler/create-task).

---
