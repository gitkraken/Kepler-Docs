---
title: Integration Settings
description: Connect issue trackers and Git hosts to Kepler, choose what each one brings in, and follow agent sessions you start in your own terminal.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, bitbucket-data-center, azure-devops, azure-devops-server]
integrations: [github, gitlab, bitbucket, azure-devops, jira, jira-data-center, linear, trello, asana]
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [settings, integrations, issue-trackers, git-hosts, terminal]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "kepler-configuration"
    nav_label: "Integration Settings"
    nav_order: 40
    nav_parent: "kepler-behavior-and-integration-settings"
    page_type: "content"
    card_icon: "plug-connected"
    card_color: "amber"
    card_description: "Connect issue trackers and Git hosts, and choose what each brings in"
---
<kbd>Last updated: November 2026</kbd>

Use **Settings → Integrations** to connect the issue trackers and Git hosts you start tasks from, and to follow agent sessions you run in your own terminal.

## Issues and pull requests

Connect your issue and pull request providers to see their issues and pull requests in the **New task** composer and in [the Kepler interface](/kepler/kepler-interface). Kepler lists every supported provider, with the connected ones first: Azure DevOps, Azure DevOps Server, Bitbucket, Bitbucket Data Center, GitHub, GitHub Enterprise, GitLab, GitLab Self-Hosted, Jira, Jira Server / Data Center, Linear, Trello, and Asana.

Each provider row shows these controls and states:

| Control | What it does |
|---|---|
| **Connect** | Connects a provider you have not connected |
| **Connected** | Marks a working connection |
| **Reconnect** | Refreshes a token on a row marked **Sign-in expired** |
| **Cannot connect to server** | The server did not answer; the integration stays connected and the state clears on its own |
| **Unexpected response** | Kepler could not read the provider's answer, so some items may be missing; reconnecting does not fix it |
| **Disconnect** | Disconnects the account from every GitKraken product that uses it; other accounts stay connected |
| **Refresh** | Checks every provider's connection again, from the section header |

If a row shows **Cannot connect to server**, check that the server is reachable from your network or VPN. If **Unexpected response** stays, check for a proxy or gateway between Kepler and the provider.

Providers connect through your GitKraken account, so you sign in to GitKraken before you can manage them.

### Self-hosted providers

A self-hosted provider, such as GitHub Enterprise, Azure DevOps Server, Bitbucket Data Center, or Jira Server / Data Center, connects with a personal access token. Click **Connect**, enter the **Server URL** and **Personal access token**, then click **Save connection**. Kepler checks the token against your server and adds the connection to your GitKraken account. Until it finishes, the row shows **Cloud sync pending**.

A connected self-hosted provider lists each server on its own row. Each server keeps its own repositories and issues:

- To connect another server, click **Add connection** on the provider's row. Connecting more than 1 server needs an active GitKraken plan or trial.
- To renew an expired or rejected token, click **Replace token** on that server's row.
- To make a server the provider's default connection, click **Set as primary**.

### Choose what's visible

To hide organizations, repositories, or tracker projects you do not want in Kepler, click **Choose what's visible…** under the provider's row, then untick the items to hide. Every connected provider except Trello and Asana has it. Hidden items leave the dashboard, the launcher, and pickers, and tasks and branches already linked to them keep working. The choice is saved on your GitKraken account.

### Accounts and organizations

When a provider has more than 1 account, an **Accounts** block lists them. **Set as primary** chooses which account Kepler acts as, and **Read from this account** chooses which account Kepler reads issues and pull requests from. These can be different accounts, but agents' GitKraken MCP server always acts as the primary account. See [MCP servers](/kepler/settings-agents#mcp-servers).

When an organization refuses a working connection, because it blocks third-party OAuth apps or has not approved GitKraken, the row names the organization and says that its items are not shown. The row links to a fix, such as **Request access on GitHub**.

For per-provider setup, see [Issue Tracker Integrations](/kepler/issue-tracker-integrations) and [Pull Request Integrations](/kepler/pull-request-integrations).

## Your terminal

To follow agent sessions you start in your own terminal, use this setting:

| Setting | What it controls | Default |
|---|---|---|
| **Show sessions started outside Kepler** | Lists sessions you start in your own terminal, so you can follow and continue them in Kepler | On |

The setting covers every agent Kepler can follow this way. See [Agent Sessions](/kepler/kepler-external-sessions).

If a running agent session stops reporting to Kepler, every window shows *Agent sessions aren't reporting to Kepler*, with a **Repair** button. **Repair** reinstalls the reporting configuration. Restart any session that still does not report. For another computer's sessions, repair from that computer.

***

---
