---
title: Integration Settings
description: Connect issue trackers and Git hosts to Kepler, choose what each one brings in, and follow agent sessions you start in your own terminal.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-hosted, bitbucket, bitbucket-data-center, azure-devops, azure-devops-server]
integrations: [github, gitlab, bitbucket, azure-devops, jira, jira-data-center, linear, trello]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [settings, integrations, issue-trackers, git-hosts, terminal]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Use **Settings → Integrations** to connect the issue trackers and Git hosts you start tasks from, and to follow agent sessions you run in your own terminal.

## Issues and pull requests

Connect your issue and pull request providers to see their issues and pull requests in the **New task** composer and in [the Kepler interface](/kepler/kepler-interface). Kepler lists every supported provider, connected or not, in this order:

| Provider |
|---|
| Azure DevOps |
| Azure DevOps Server |
| Bitbucket |
| Bitbucket Data Center |
| GitHub |
| GitHub Enterprise |
| GitLab |
| GitLab Self-Hosted |
| Jira |
| Jira Server / Data Center |
| Linear |
| Trello |

Each provider row shows these controls and states:

| Control | What it does |
|---|---|
| **Connect** | Starts the connection flow for a provider you have not connected |
| **Connected** | Shown on a working connection |
| **Reconnect** | Refreshes an expired token. A **Sign-in expired** badge and the hint *Sign-in has expired. Click Reconnect to refresh this provider's token.* mark the rows that need it |
| **Cannot connect to server** | The provider's server did not answer. The integration stays connected and this state clears by itself once the server responds, so you do not need to reconnect |
| **Unexpected response** | The provider answered with data Kepler could not read, so some of its items may be missing. The integration stays connected, and reconnecting does not fix this state |
| **Disconnect** | Disconnects the provider from GitKraken everywhere: every GitKraken product and service that uses this connection loses access too. Other accounts for that provider stay connected, and you can reconnect at any time |
| **Refresh** | Checks every provider's connection status again. It is in the section header |

If a row shows **Cannot connect to server**, check that the server is reachable from your network or VPN. If **Unexpected response** stays, check for a proxy or gateway between Kepler and the provider.

Providers connect through your GitKraken account, so the section asks you to sign in before it shows anything to manage.

A self-hosted provider, such as GitHub Enterprise, Azure DevOps Server, Bitbucket Data Center, or Jira Server / Data Center, connects with a personal access token. **Connect** or **Reconnect** opens **Connect {name}**, with **Server URL** and **Personal access token**. **Save connection** checks the token against your server from this machine, saves the connection here, and syncs it to your GitKraken account. Until the sync finishes, the row shows **Cloud sync pending**. See [Pull Request Integrations](/kepler/pull-request-integrations) and [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

To hide organizations, repositories, or tracker projects you do not want in Kepler, use **Choose what's visible…**. Every connected provider except Trello has it, on a line that reads **Everything visible** or **{count} hidden**. In **Choose what {name} brings in**, untick the items to hide. *Hidden items are left out of the dashboard, the launcher and pickers. Tasks and branches already linked to them keep resolving.* Kepler saves the choice on your GitKraken account. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

When a provider has more than 1 account, an **Accounts** block lists them. **Set as primary** chooses which account Kepler acts as, and **Read from this account** chooses which account Kepler reads issues and pull requests from. These can be different accounts.

When an organization refuses a working connection, because it blocks third-party OAuth apps or has not approved GitKraken, the row names the organization and says that its items are not shown. The row links to a fix, such as **Request access on GitHub**.

Under the list, the line *Agents can use these through the GitKraken MCP server.* links to [MCP servers](/kepler/settings-agents#mcp-servers).

For per-provider setup, see [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

## Your terminal

The following setting lets you follow agent sessions you start outside Kepler:

| Setting | What it controls | Default |
|---|---|---|
| **Show sessions started outside Kepler** | *Lists sessions you start in your own terminal, so you can follow and continue them here.* | On |

To do this, Kepler installs GitKraken hooks. The switch covers every agent that reports through hooks, and its help text names those agents. See [Agent Sessions](/kepler/agent-sessions#sessions-started-outside-kepler).

If Kepler stops receiving hook events from a running agent session, every window shows *Agent sessions aren't reporting to Kepler*, with a **Repair** button. **Repair** installs the reporting configuration again. A running CLI does not reload its hooks, so restart any session that still does not report. A window that only views another computer's sessions shows the warning without **Repair**, and tells you to repair reporting from the computer running those sessions.

***

---
