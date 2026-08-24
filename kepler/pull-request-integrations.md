---
title: Pull Request Integrations
description: Connect your Git hosts to Kepler so the pull requests you authored and the ones waiting on your review land in one list, already matched to the worktrees they belong to.
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
last_verified: 2026-08
llms_include: true
tags: [integrations, pull-requests, github, gitlab, bitbucket, azure-devops, worktrees, accounts, settings]
taxonomy:
  category: kepler
---
<kbd>Last updated: August 2026</kbd>

Connect a Git host and the pull requests you authored, plus the ones waiting on your review, show up in [the Kepler interface](/kepler/kepler-interface). Kepler also matches them to the worktrees you already have, so a branch you are working on carries its pull request wherever you see it.

Manage providers in **Settings → Integrations**, in the **Provider Integrations** section.

<figure>
  <a href="/wp-content/uploads/provider-integrations-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/provider-integrations-aug-2026.png" class="help-center-img img-bordered" alt="Settings → Integrations → Provider Integrations, with GitHub and Jira connected, showing the Connected badge and Disconnect and Reconnect buttons">
  </a>
  <figcaption style="text-align:center; color:#888">Provider Integrations, in Settings → Integrations.</figcaption>
</figure>

***

## Hosts Kepler can read pull requests from

Six of Kepler's nine providers return pull requests:

| Provider | Name in Settings | Also returns issues |
|---|---|---|
| **GitHub** | GitHub | Yes |
| **GitHub Enterprise** | GitHub Enterprise | Yes |
| **GitLab** | GitLab | Yes |
| **GitLab Self-Hosted** | GitLab Self-Hosted | Yes |
| **Azure DevOps** | Azure DevOps | Yes |
| **Bitbucket** | Bitbucket | No |

Jira, Linear, and Trello are the other three. They return issues only — see [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

Self-hosted instances are supported. **GitHub Enterprise** and **GitLab Self-Hosted** read pull requests and merge requests the same way their cloud counterparts do; which fields come back depends on your server's version. Your machine needs to be able to reach the instance.

GitLab merge requests appear as pull requests throughout Kepler. There is one list, not two.

***

## Connect a Git host

Connecting a Git host takes four steps:

1. Open **Settings → Integrations**.
2. Find the provider in **Provider Integrations** and click **Connect**.
3. Authorize Kepler in the browser window that opens.
4. Kepler returns to **Provider Integrations** and the provider shows a **Connected** badge.

Your GitKraken account holds integrations, not this copy of Kepler, so a provider you connect here also becomes available to the `gk` command-line interface (CLI) and GitKraken Desktop. You need to sign in to a GitKraken account to manage them.

**Connect** hands the whole authorization to GitKraken's website. Kepler opens `/connect` there in your system browser, names the provider, and includes a redirect back into Kepler. Kepler has no in-app form for a host URL or a personal access token, so you supply a self-hosted instance's address and whatever credential it needs directly in the browser. When you return, Kepler refetches your providers instead of reusing its cached list.

<!-- TODO(verify): re-confirmed at kepler 7c31af83e and on the current checkout — the redirect-only flow and the absence of an in-app form are settled (src/backend/auth/auth.ts:227 builds only websiteUrl + /connect with product, optional provider, and redirect_uri; src/ui/data/auth.ts:68 hands that off to openExternalUrl; Settings and onboarding provider buttons only call connect.mutate({ providerId }), with no host/token/scope fields anywhere in-app). No per-provider token scopes are declared in this repo either. What's still open: the browser-side steps and the scopes each provider asks for live on GitKraken's website (see help.gitkraken.com/kepler/pull-request-integrations and help.gitkraken.com/gk-dev/gk-dev-integrations), which is website-owned content outside this repo. Remains unresolved until the web team confirms the live /connect steps and provider scopes for GitHub Enterprise, GitLab Self-Hosted, Bitbucket, and Azure DevOps. -->

Three controls sit on a connected provider's row:

| Control | What it does |
|---|---|
| **Reconnect** | Re-runs authorization. Use it when a sign-in has expired |
| **Disconnect** | Removes the provider — see below |
| **Refresh** | At the top of the section, re-checks every provider |

A warning triangle on a row means that provider's sign-in has expired. Kepler tries to refresh the token itself; **Reconnect** is the manual fix.

***

## Cloning a repository you don't have

Starting work on a pull request whose repository you have never cloned makes Kepler clone that repository first, into your **Default Repositories Folder**. That clone authenticates with the provider token your connected GitKraken account already holds, the same connection the pull request itself came through. As a result, a private repository clones without you having to set up a git credential helper. Kepler authenticates the clone differently depending on the host:

| Host | How the clone authenticates |
|---|---|
| **GitHub**, **GitHub Enterprise** | Your connected account's token |
| **GitLab**, **GitLab Self-Hosted** | Your connected account's token |
| **Bitbucket**, **Azure DevOps** | Falls through to your own git credentials |

For an enterprise or self-managed host, Kepler matches the clone's host against the domain stored on your connection, so the repository clones through the account connected to that instance rather than through a cloud account of the same family. When a provider has more than one account, the clone follows the same choice your reads follow: **Read from this account** where you set one, otherwise the primary.

Kepler hands the token to that one git process and nothing more. Kepler does not write it into the clone's `.git/config`, does not add it to the remote's URL, and never exposes it to the interface.

Where Kepler holds no usable token for the host, the clone falls back to your own git credential helper. Kepler never lets git open an interactive prompt, so when no credential helper is available, the clone fails with a message that names the host and tells you what to do — *git has no saved credentials for this remote and Kepler cannot prompt for them. Sign in with a git credential helper (e.g. `gh auth login`, or the macOS keychain helper) or use an SSH url, then try again.*

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

<figure>
  <a href="/wp-content/uploads/disconnect-provider-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/disconnect-provider-aug-2026.png" class="help-center-img img-bordered" alt="A connected provider's row, with Connected badge, Disconnect, and Reconnect">
  </a>
  <figcaption style="text-align:center; color:#888">A connected provider's row.</figcaption>
</figure>

Disconnecting reaches further than Kepler: it removes the connection from your GitKraken account, so the `gk` CLI and GitKraken Desktop lose it too. What happens to the provider depends on whether you have another account connected:

- **With another account connected**, Kepler promotes it to primary and the provider stays connected under it. Nothing else changes.
- **With no other account connected**, the provider is removed entirely. Kepler drops its saved filters and its rows from your lists, so nothing lingers behind pointing at a provider you no longer have.

You can reconnect at any time.

***

## Bitbucket has no issues

Kepler keeps two separate lists of what each provider can return. Bitbucket is on the pull-request list only, so Kepler never asks it for issues, and a provider filter for issues never offers it. In the list, Kepler builds facets from the rows actually loaded, so a facet with nothing to offer never appears.

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

A pull request you open outside Kepler (from a terminal `gh`, from GitKraken, from the web) used to stay a read-time match and never become a resource. Kepler now records it for you.

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
| **URL** | Used by **Open in browser** |

<!-- TODO(verify): re-checked field by field against the shared PullRequest shape in src/shared/provider/pull-request.ts at kepler 7c31af83e — unchanged, and the table above is complete apart from the base-repo clone URLs, which only prefill the Clone form. The June 2026 version of this page also claimed Kepler pulls the diff, open review comments, and the current review state when you attach a pull request; none of those are fields on this shape. Confirm with engineering which path supplies review comments and the diff to a Review or Address Feedback run before documenting them. -->

Azure DevOps reports pull requests without a usable number, so Kepler identifies them by URL instead. You should not see a difference; identifying by URL is why a pull request you look up by link resolves correctly there.

***

## Where your pull requests turn up

Your pull requests turn up in four places:

| Surface | What it gives you |
|---|---|
| [The Kepler interface](/kepler/kepler-interface) | The **Todo** segment lists every pull request you authored and every one you are a reviewer on, with your role on each |
| [Actions](/kepler/actions) | The **Action** button hands the pull request to an agent. **Review** and **Address Feedback** are the two built-in Actions aimed at pull requests, and Kepler picks between them by who authored it |
| [Review Changes](/kepler/review-changes) | Reading the diff and the commits behind a pull request |
| [Tasks and Resources](/kepler/tasks-and-resources) | A pull request is a resource on a task, so you can attach one to work that already exists |

---
