---
title: Integration Settings
description: The Integrations page of Kepler's Settings, covering issue tracker and Git host connections, and sessions started in your own terminal.
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

*Bring your work into Kepler: start tasks from your issues and pull requests, and follow agent sessions you run in your own terminal.* The Integrations page has two sections: **Issues and pull requests** and **Your terminal**.

## Issues and pull requests

Connect your issue and pull request providers to see them in the Task Composer and in [the Kepler interface](/kepler/kepler-interface). Kepler lists every supported provider whether or not it is connected, in this order:

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

Each provider row carries these controls and states:

| Control | What it does |
|---|---|
| **Connect** | Starts the connection flow for a provider you have not connected |
| **Connected** | Shown on a working connection |
| **Reconnect** | Refreshes an expired token. A **Sign-in expired** badge and the hint *Sign-in has expired. Click Reconnect to refresh this provider's token.* mark the rows that need it |
| **Cannot connect to server** | The provider's server didn't answer. The integration is still connected, and this clears on its own once the server responds. Check that it's reachable from your network or VPN. No reconnect needed |
| **Unexpected response** | The provider answered with data Kepler was unable to read, so some of its items may be missing. The integration is still connected and reconnecting won't fix it, so if it persists, check for a proxy or gateway between Kepler and the provider |
| **Disconnect** | Disconnects the provider from GitKraken everywhere: every GitKraken product and service that uses this connection loses access too. Other accounts for that provider stay connected, and you can reconnect at any time |
| **Refresh** | Re-checks every provider's connection status. It's in the section header |

Providers connect through your GitKraken account, so the section asks you to sign in before it shows anything to manage.

A self-hosted provider, such as GitHub Enterprise, Azure DevOps Server, Bitbucket Data Center, or Jira Server / Data Center, connects with a personal access token. **Connect** or **Reconnect** opens **Connect {name}**, with **Server URL** and **Personal access token**. **Save connection** checks the token against your server from this machine, saves the connection here, and syncs it to your GitKraken account. Until the sync finishes, the row shows **Cloud sync pending**. See [Pull Request Integrations](/kepler/pull-request-integrations) and [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

Every connected provider except Trello also has a line that reads **Everything visible** or **{count} hidden**, with **Choose what's visible…**. It opens **Choose what {name} brings in**, where you untick the organizations, repositories, or tracker projects you don't want. *Hidden items are left out of the dashboard, the launcher and pickers. Tasks and branches already linked to them keep resolving.* The choice is saved on your GitKraken account. See [Issue Tracker Integrations](/kepler/issue-tracker-integrations).

When a provider has more than one account, an **Accounts** block lists them. **Set as primary** chooses which account Kepler acts as, and **Read from this account** chooses which one Kepler reads issues and pull requests from. They can be different accounts.

When an organization refuses a working connection (it blocks third-party OAuth apps, or hasn't approved GitKraken), the row names the organization and says its items aren't shown, with a link to fix it, such as **Request access on GitHub**.

Under the list, *Agents can use these through the GitKraken MCP server.* links to [MCP servers](/kepler/settings-agents#mcp-servers).

For per-provider setup, see [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

## Your terminal

The following setting covers agent sessions you start outside Kepler:

| Setting | What it controls | Default |
|---|---|---|
| **Show sessions started outside Kepler** | *Lists sessions you start in your own terminal, so you can follow and continue them here.* Kepler installs GitKraken hooks to do this. One switch covers every agent that reports through hooks, and the help text names them. See [Agent Sessions](/kepler/agent-sessions#sessions-started-outside-kepler) | On |

If Kepler stops receiving hook events from a running agent session, every window shows *Agent sessions aren't reporting to Kepler*, with a **Repair** button. **Repair** reinstalls the reporting configuration. Restart any session that still doesn't report, since a running CLI doesn't reload its hooks. A window that only views another computer's sessions gets the warning without **Repair**, and is told to repair reporting from the computer running those sessions.

***

---
