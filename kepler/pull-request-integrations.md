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

Of Kepler's 12 providers, 8 return pull requests:

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

The other 4 providers (Jira, Jira Server / Data Center, Linear, and Trello) return issues only. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

Kepler supports self-hosted instances. **GitHub Enterprise**, **GitLab Self-Hosted**, **Azure DevOps Server**, and **Bitbucket Data Center** read pull requests and merge requests the same way their cloud counterparts do, and 2 servers of the same kind stay separate. Which fields come back depends on your server's version.

You connect a self-hosted instance inside Kepler with its address and a personal access token, and Kepler checks the token against the server from your machine. See [Connect a self-hosted instance](#connect-a-self-hosted-instance). The instance must be reachable both from your machine and from gitkraken.dev, so you cannot connect a server that is only reachable inside your network or VPN. <!-- TODO(verify): v0.15 checks the personal access token from this machine; confirm with engineering whether syncing it to the account still needs gitkraken.dev to reach the server --> Kepler trusts the certificates in your operating system's certificate store, so a server signed by your company's own certificate authority works without extra setup.

Kepler shows GitLab merge requests as pull requests, in the same list.

***

## Connect a Git host

To connect a cloud Git host (**GitHub**, **GitLab**, **Bitbucket**, or **Azure DevOps**), follow these steps:

1. Open **Settings → Integrations**.
2. Find the provider in **Issues and pull requests** and click **Connect**.
3. Authorize Kepler in the browser window that opens.
4. Return to Kepler, where the provider shows a **Connected** badge in **Issues and pull requests**.

Integrations belong to your GitKraken account, not to this copy of Kepler, so a provider you connect here is also available to the `gk` command-line interface (CLI) and GitKraken Desktop. To manage integrations, sign in to a GitKraken account.

For a cloud host, **Connect** sends you to GitKraken's website to authorize. Kepler opens `/connect` there in your system browser, names the provider, and includes a redirect back into Kepler. When you return, Kepler fetches your providers again instead of reusing its cached list.

While you authorize, Kepler keeps a **Connect {provider} in your browser** dialog open, with the provider's name in place of {provider}. If your browser did not open, copy the **Connection link** from the dialog and open it in a browser yourself. **Try again** makes a new link, because each link works once.

The dialog closes by itself as soon as the new connection appears, and Kepler checks for it again whenever you come back to a Kepler window. If Kepler cannot start the connection, the dialog reads **Unable to connect {provider}** and says why. **Reconnect** uses the same dialog.

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
| *Credentials saved. Unable to verify the server certificate. Check its TLS configuration.* | Kepler saved the token but could not verify the server's certificate |
| *Credentials saved without verification. Unable to reach the server.* | Kepler saved the token without checking it |
| *The server refused this token. Check its value and permissions.* | Fix the token and save again |

Until Kepler finishes syncing the connection to your account, the provider's row shows **Cloud sync pending**, and you cannot make that connection the primary. If Kepler cannot reach GitKraken, it retries when you refresh your providers. **Reconnect** on a self-hosted provider opens the same dialog, so you can replace an expired or rejected token there.

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

When you start work on a pull request from a repository you have never cloned, Kepler first clones the repository into your **Default Repositories Folder**. The clone authenticates with the provider token that your connected GitKraken account already holds, the same connection the pull request came through. As a result, a private repository clones without you having to set up a Git credential helper. How the clone authenticates depends on the host:

| Host | How the clone authenticates |
|---|---|
| **GitHub**, **GitHub Enterprise** | Your connected account's token |
| **GitLab**, **GitLab Self-Hosted** | Your connected account's token |
| **Bitbucket**, **Bitbucket Data Center**, **Azure DevOps**, **Azure DevOps Server** | Your own Git credentials |

For an enterprise or self-managed host, Kepler matches the clone's host against the domain stored on your connection. The repository then clones through the account connected to that instance, not through a cloud account from the same vendor. When a provider has more than one account, the clone uses the account Kepler reads from: **Read from this account** where you set one, otherwise the primary.

Kepler passes the token only to that one Git process. Kepler does not write the token into the clone's `.git/config` or add it to the remote's URL, and never shows it in the interface.

If Kepler has no usable token for the host, the clone uses your own Git credential helper. Kepler never lets Git open an interactive prompt, so when no credential helper is available, the clone fails with a message that names the host and tells you what to do: *git has no saved credentials for this remote and Kepler cannot prompt for them. Sign in with a git credential helper (e.g. `gh auth login`, or the macOS keychain helper) or use an SSH url, then try again.*

***

## More than one account of the same provider

You can connect several accounts of the same provider. When a provider has two or more, an **Accounts** list appears under its row with one entry per account.

Each entry carries two independent controls:

| Control | What it changes | How far it reaches |
|---|---|---|
| **Read from this account** | Which account Kepler reads this provider's pull requests and issues from | Kepler only, and non-destructive |
| **Set as primary** / **Primary** | The provider's primary account | Everywhere: other Kepler windows, the `gk` CLI, and GitKraken Desktop |

**Browsing a secondary account does not change your primary.** Selecting **Read from this account** on a second account switches what Kepler shows you and leaves the primary alone. The primary is the default read account, so a provider with no override reads through it.

Changing either one clears that provider's saved filters, because a repository from the old account might not exist on the new one. Kepler then fetches the list again.

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
- **With no other account connected**, Kepler removes the provider entirely. Kepler drops its saved filters and its rows from your lists, so nothing in Kepler still points to a provider you no longer have.

You can reconnect at any time.

***

## Bitbucket has no issues

Kepler keeps 2 separate lists of what each provider can return: providers that can list issues, and providers that can list pull requests. Bitbucket and Bitbucket Data Center are on the pull-request list only, so Kepler never asks them for issues, and a provider filter for issues never offers them. Kepler also builds the list's facets from the rows actually loaded, so a facet with nothing to match never appears.

The same rule applies the other way to Jira, Linear, and Trello, which have no pull requests.

***

## How pull requests attach to worktrees

Kepler matches a pull request to a worktree by **branch**. It tries the worktree's **upstream branch** as well as its local one.

The upstream pass matters when the 2 names differ. If your local branch is `fix-login` but it tracks `origin/justin/fix-login`, the pull request's head branch is the upstream name, so matching on the local name alone finds nothing. Kepler's second pass compares against the short branch name of the tracking ref and finds the match.

Matching covers open and closed pull requests together, so a merged pull request still shows on the branch it merged from.

### Confirmed and inferred links

Kepler records **how** it made each link, so you can tell a confirmed link from a guess:

| How the link was made | Reads as | What it means |
|---|---|---|
| Recorded on the task | Confirmed | The link is authoritative. Kepler records one when you launch the task from the pull request, when an agent opens a pull request, when you attach one yourself, or through the branch auto-attach below |
| The pull request's head branch matched the worktree's local branch | Confirmed | A direct branch match |
| The head branch matched the worktree branch's **upstream** branch | Confirmed, and marked | Git-native rather than a guess, but the local name differs, so Kepler labels it **Matched from upstream branch** |
| An identifier parsed out of the branch name | Inferred | A heuristic. Issues only: pull requests are never linked this way |

A confirmed link has no extra marking. Kepler draws a dotted underline under any link you should check, and its tooltip says why: **Matched from upstream branch**, or **Matched from branch name** for an inferred issue link.

When Kepler finds the same pull request in more than one way, the most authoritative link wins: the task's own recorded link, then a local branch match, then an upstream branch match.

Kepler matches branches only within each item's own repository, so a pull request in one repository never matches a branch of the same name in another.

### Auto-attaching a matched pull request

When you open a pull request outside Kepler (with `gh` in a terminal, from GitKraken Desktop, or on the web), Kepler records it on the task for you, instead of only matching it each time it reads your pull requests.

Whenever new pull-request data arrives, Kepler checks your active tasks that have no pull request yet, and attaches one whose head branch matches a worktree's branch. The pull request then behaves like one you attached yourself: it appears in the task's resources, and the agent receives it as context. See [Tasks and Resources](/kepler/tasks-and-resources).

Auto-attach is stricter than branch matching, because Kepler saves an attached resource and sends it to an agent, while a match only shows a card. Auto-attach follows 4 rules:

| Rule | Why |
|---|---|
| Exact matches only | The pull request's head branch has to be the worktree's own branch name, and its repository has to match a remote exactly. The upstream-branch pass and the rename-tolerant fallback still show the card; neither attaches |
| Open pull requests only | A merged pull request cannot claim a branch name that gets reused later |
| The head branch has to live in the same repository | Branch matching keys on the head branch name, and the author of a fork picks that name freely. An attached resource reaches your agent, so a stranger's pull request must not claim your branch |
| One pull request per task per pass | A task drops out of the next pass as soon as it holds one |

Auto-attach still attaches a pull request that another active task already holds, because several active tasks can share one pull request. Attaching it to one task leaves it on the other, and restoring an archived task that holds it archives nothing.

Auto-attach never archives or replaces anything. A branch match is a guess, so it never replaces work you started on purpose, and it never removes a link because a pull request was briefly missing from a read.

***

## What Kepler reads from a pull request

Kepler reads these fields from a pull request:

| Field | Notes |
|---|---|
| **Number and title** | |
| **Description** | The pull request body |
| **State** | Kepler derives one of **Open**, **Draft**, **Merged**, or **Closed** |
| **Repository** | Name, owner, and host |
| **Author** | When the provider reports one. Kepler also tracks whether you authored it, which decides whether a row shows **Yours** or **Review** |
| **Head and base branch** | When the provider reports them. These drive branch matching and the branch a task starts from |
| **Fork** | Whether the head branch lives on a fork, and where, so Kepler can fetch it from the fork remote instead of `origin` |
| **Created at** | |
| **URL** | Used by the open control, which names the provider: **Open on GitHub**, **Open on Bitbucket**, and so on |

<!-- TODO(verify): re-checked field by field against the shared PullRequest shape in src/shared/provider/pull-request.ts at kepler 7c31af83e. It's unchanged, and the table above is complete apart from the base-repo clone URLs, which only prefill the Clone form. The June 2026 version of this page also claimed Kepler pulls the diff, open review comments, and the current review state when you attach a pull request; none of those are fields on this shape. Confirm with engineering which path supplies review comments and the diff to a Review or Address Feedback run before documenting them. -->

A merged pull request keeps its description and author for as long as a task, archived or not, still links it.

On a self-hosted server (GitHub Enterprise, GitLab Self-Hosted, Azure DevOps Server, or Bitbucket Data Center), images embedded in a pull request's description are blocked and do not display in Kepler's previews. The server's member avatars still load.

Azure DevOps reports pull requests without a usable number, so Kepler identifies them by URL instead. You do not see a difference, and identifying by URL is why a pull request you look up by link resolves correctly there.

***

## Where your pull requests turn up

Your pull requests appear in 4 places:

| Surface | What it gives you |
|---|---|
| [The Kepler interface](/kepler/kepler-interface) | The **Todo** segment lists the pull requests related to you on each connected host, with your role on each |
| [Actions](/kepler/actions) | The **Action** button hands the pull request to an agent. **Review** and **Address Feedback** are the 2 built-in Actions for pull requests, and Kepler picks one based on who authored the pull request |
| [Review Changes](/kepler/review-changes) | Reading the diff and the commits behind a pull request |
| [Tasks and Resources](/kepler/tasks-and-resources) | A pull request is a resource on a task, so you can attach one to work that already exists |

**Todo's scope differs by host.** Each provider reports a different set of pull requests related to you, so Todo lists these from each:

| Host | Pull requests Todo lists |
|---|---|
| **GitHub**, **GitHub Enterprise** | Yours, assigned to you, or ones you review |
| **GitLab**, **GitLab Self-Hosted**, **Azure DevOps**, **Azure DevOps Server**, **Bitbucket Data Center** | Yours or awaiting your review |
| **Bitbucket** | Yours, or awaiting your review in your workspaces and repositories added to Kepler |

Hover the **Related to me** chip in Todo's header to see the rule for each integration you have connected. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations#which-issues-kepler-lists) for the issue side.

**Review requests come from every host.** Pull requests waiting on your review show up from Azure DevOps, Azure DevOps Server, and Bitbucket Data Center as well as GitHub and GitLab. Bitbucket Cloud has no account-wide way to ask for them, so Kepler reads review requests repository by repository, starting with the repositories you have in Kepler and then the rest of your workspaces at a pace that stays inside Bitbucket's hourly request limits. On a large workspace they can take a while to appear.

**Kepler loads the lists you are looking at.** Pull request and issue lists refresh while they are on screen, and again when you come back to the window, instead of downloading your whole account's lists in the background. A task's own pull requests refresh when an agent ends a turn, a branch is pushed, or a pull request is published. When one provider fails to load, the others keep loading, and the failed provider's last loaded pull requests stay in the list.

**A failing provider is named, with its fix.** When a connected provider's read fails, Todo, the **Add resources** lists, and a link preview show a warning that names the provider and what went wrong, such as *GitHub needs you to sign in again, so its work may be missing.* On Todo the warning sits under **Unable to load your work**. Each warning offers one fix:

| What went wrong | The fix offered |
|---|---|
| The sign-in needs renewing | **Reconnect**, or **Reconnect in settings** for a self-hosted provider, which needs a new token |
| The provider refused part of the request, so some organizations or repositories may be missing | **Open settings** |
| Rate limiting, an unreachable server, an unreadable answer, or a temporary problem | **Retry** |

Rows kept from the last good load show a cloud mark on their provider chip, labeled *Not refreshed: shown from the last successful {provider} load.*

<figure style="text-align:center">
  <a href="/wp-content/uploads/todo-provider-failure-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/todo-provider-failure-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="Todo when GitHub refuses its sign-in: Unable to load your work, over a warning that reads GitHub needs you to sign in again, so its work may be missing, with a Reconnect button.">
  </a>
  <figcaption style="text-align:center; color:#888">Todo names a provider whose sign-in failed and offers Reconnect.</figcaption>
</figure>

**The pull request picker says why its list is empty.** When you attach a pull request from **Add resources**, the picker explains an empty list instead of showing *No matches*:

- If the **Linked work** filter hides pull requests, the picker says how many it hides and which filter hides them, and offers **Show all**.
- If no connected provider can list pull requests, the picker reads **Connect your code host** and lists the providers that can fill the tab, each with **Connect**.

The **Linked work** filter defaults to **No active task**. A task counts as active until you archive it, so Done and on-hold tasks count. The filter has 5 options:

| Option | Shows pull requests |
|---|---|
| **Any** | Whatever their task history |
| **No active task** | With no task, or with archived tasks only. This default keeps earlier work easy to find, so you do not duplicate it |
| **No tasks ever** | Never linked to a task |
| **Has an active task** | Linked to at least one task that is not archived |
| **Archived tasks only** | Linked only to archived tasks |

A row with task history carries a badge: **Task** or **{count} tasks** when one of them is active, **Archived task** or **{count} archived tasks** when all are archived.

When nothing you have connected can list issues or pull requests, **Add resources** opens on a connect view, **Connect where your work lives**, with a tile for each provider. Connect each one you use, then click **Continue**. The provider filter's menu also offers **Connect another provider…**, which opens the same view with a **Back** button.

You can also start work on a pull request from GitLens or GitKraken Desktop. See [Create a task](/kepler/create-task).

---
