---
title: Issue Tracker Integrations
description: Connect your issue trackers to Kepler so the issues assigned to you land in one list, with everything an agent needs already attached.
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
last_verified: 2026-08
llms_include: true
tags: [integrations, issue-trackers, jira, linear, trello, github, gitlab, azure-devops, accounts, settings]
taxonomy:
    category: kepler
---
<kbd>Last updated: August 2026</kbd>

Connect an issue tracker and every issue assigned to you shows up in [the Kepler interface](/kepler/kepler-interface), alongside your pull requests and the tasks you already have running. Starting work on one becomes picking a row rather than describing the work from scratch.

Manage providers in **Settings → Integrations**, in the **Provider Integrations** section.

<!-- TODO(screenshot): Settings → Integrations → Provider Integrations, with one provider connected and its Accounts list expanded. The existing _images/provider-integrations.png and _images/pr-integrations.png predate the Connected badge, the Disconnect button, and the account switcher. -->

***

## Trackers Kepler can read issues from

Eight of Kepler's nine providers return issues:

| Provider | Name in Settings | Also returns pull requests |
|---|---|---|
| **GitHub** | GitHub | Yes |
| **GitHub Enterprise** | GitHub Enterprise | Yes |
| **GitLab** | GitLab | Yes |
| **GitLab Self-Hosted** | GitLab Self-Hosted | Yes |
| **Azure DevOps** | Azure DevOps | Yes |
| **Jira** | Jira | No |
| **Linear** | Linear | No |
| **Trello** | Trello | No |

Bitbucket is the ninth. It returns pull requests only — see [Pull Request Integrations](/kepler/pull-request-integrations).

Self-hosted instances are first-class: **GitHub Enterprise** and **GitLab Self-Hosted** read issues the same way their cloud counterparts do. Which fields come back depends on your server's version.

***

## Connect a tracker

Connecting a tracker takes four steps:

1. Open **Settings → Integrations**.
2. Find the provider in **Provider Integrations** and click **Connect**.
3. Authorize Kepler in the browser window that opens.
4. Kepler returns to **Provider Integrations** and the provider shows a **Connected** badge.

Your GitKraken account holds integrations, not this copy of Kepler, so a provider you connect here also becomes available to the `gk` command-line interface (CLI) and GitKraken Desktop. You need to sign in to a GitKraken account to manage them; Kepler prompts you if you are not signed in.

**Connect** hands the whole authorization to GitKraken's website. Kepler opens `/connect` there in your system browser, names the provider, and includes a redirect back into Kepler. Kepler has no in-app form for a host URL or a personal access token, so you supply whatever the provider needs directly in the browser. When you return, Kepler refetches your providers instead of reusing its cached list.

<!-- TODO(verify): the redirect and the absence of an in-app form are confirmed against getConnectUrl (src/backend/auth/auth.ts) and useConnectProvider (src/ui/data/auth.ts) at kepler 7c31af83e. The browser-side steps themselves live on GitKraken's website and are not in this repo — confirm with the web team what Jira site selection, Linear workspace selection, and the GitHub Enterprise / GitLab Self-Hosted host-and-token fields actually ask for before documenting them as a numbered flow. -->

Three controls sit on a connected provider's row:

| Control | What it does |
|---|---|
| **Reconnect** | Re-runs authorization. Use it when a sign-in has expired |
| **Disconnect** | Removes the provider — see below |
| **Refresh** | At the top of the section, re-checks every provider |

A warning triangle on a row means that provider's sign-in has expired. Kepler tries to refresh the token on its own; **Reconnect** is the manual fix.

***

## More than one account of the same provider

You can connect several accounts of the same provider — two GitHub accounts, a work Jira site and a personal one. When a provider has two or more, an **Accounts** list appears under its row with one entry per account.

Each entry carries two independent controls:

| Control | What it changes | How far it reaches |
|---|---|---|
| **Read from this account** | Which account Kepler reads this provider's issues and pull requests from | Kepler only, and non-destructive |
| **Set as primary** / **Primary** | The provider's primary account | Everywhere — other Kepler windows, the `gk` CLI, and GitKraken Desktop |

**Browsing a secondary account does not change your primary.** Selecting **Read from this account** on a second account switches what Kepler shows you and leaves the primary alone. That's why **Read from this account** is a radio control rather than a button. The primary is the default read account, so a provider with no override reads through it.

Switching either one clears that provider's saved filters — an organization or project from the old account need not exist on the new one — and re-fetches the list.

The read account also authenticates git. Starting work on an issue in a repository you have never cloned makes Kepler clone that repository, using the same connection it reads through. See [Pull Request Integrations](/kepler/pull-request-integrations) for which hosts this covers and what happens on the hosts it does not.

***

## Disconnect a provider

Click **Disconnect** on the provider's row in **Settings → Integrations** and confirm.

Disconnecting reaches further than Kepler. It removes the provider from GitKraken entirely, so the `gk` CLI and GitKraken Desktop lose access too, along with **any additional accounts of that provider**. You can reconnect at any time.

Kepler also drops that provider's saved filters and its rows from your lists, so nothing lingers behind pointing at a provider you no longer have.

<!-- TODO(verify): the confirmation dialog's claim about additional accounts may be wrong. settings.providers.disconnectDescription (src/shared/i18n/locales/en.ts) says "along with any additional {name} accounts", but the only provider backend left after kepler#1956 removes the provider's PRIMARY connection and lets the platform promote a secondary, so a multi-account provider stays connected — see the disconnect docblock in src/backend/provider/core-gitlens-adapter.ts at 7c31af83e. This page currently follows the dialog. Settle which is right with engineering; if the backend is right, both the dialog copy and this paragraph need changing. -->

***

## Jira, Linear, and Trello have no pull requests

Kepler keeps two separate lists of what each provider can return: which providers can list issues, and which can list pull requests. Jira, Linear, and Trello are on the first list only.

Two consequences you will notice:

- **Kepler never asks them for pull requests.** Kepler excludes them from the pull-request read instead of querying and ignoring them.
- **The interface hides the dead filters.** A provider filter only offers providers that can return results for what you are looking at, so Jira never appears as a pull-request filter. In the list, Kepler builds facets from the rows actually loaded, so a facet with nothing to offer never appears.

The same rule runs the other way for Bitbucket, which has no issues.

***

## What Kepler reads from an issue

When an issue becomes a task, Kepler attaches what it read, so the agent starts with that context instead of asking for it. Kepler pulls these fields from the issue:

| Field | Notes |
|---|---|
| **Identifier** | The issue key or number — `GK-1234` for Jira, `DRE-2` for Linear, a number for GitHub, GitLab, and Azure DevOps |
| **Title** | |
| **Description** | The issue body |
| **Issue type** | The provider's own vocabulary — a Jira issue type, an Azure DevOps work item type |
| **Author** | When the provider reports one |
| **Assignees** | |
| **Labels** | The provider's own labels. Kepler distinguishes "this issue has no labels" from "this provider cannot report labels" |
| **Project or board** | Jira projects, Linear teams, Azure DevOps areas. Git hosts hang issues off a repository instead |
| **Repository** | Name, owner, and host, for the git hosts |
| **URL** | Used by **Open in browser** |

<!-- TODO(verify): re-checked field by field against the shared Issue shape in src/shared/provider/issue.ts at kepler 7c31af83e — unchanged, and the table above is complete. It still carries no priority, due date, milestone, Trello checklist, Linear cycle, or Azure DevOps area/iteration path, all of which the June 2026 version of this page claimed. Confirm with engineering whether any of those reach the agent by another path before re-adding them. -->

Kepler does not pass issue attachments or embedded images to the agent.

***

## Where your issues turn up

Your issues turn up in three places:

| Surface | What it gives you |
|---|---|
| [The Kepler interface](/kepler/kepler-interface) | The **Todo** segment lists every issue assigned to you across every connected tracker, grouped and filtered how you like |
| [Actions](/kepler/actions) | The **Action** button on a row hands the issue to an agent with its context attached. Firing an Action on an untracked issue is also how it becomes a task |
| [Tasks and Resources](/kepler/tasks-and-resources) | An issue is a resource on a task, so you can attach one to work that already exists |

The **Issue type**, **Label**, and **Project** filters carry your provider's own vocabulary rather than a Kepler translation of it.

---
