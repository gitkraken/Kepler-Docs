---
title: Agent Tool Settings
description: Manage the MCP servers your Kepler agents load, and let your agents use Kepler's built-in tools for rebasing, merging, and cleaning up commits.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot, cursor, antigravity, opencode, pi, auggie, grok]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [settings, agent-tools, mcp-servers, built-in-tools]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Use **Settings → Agent tools** to manage the tools your agents can use beyond the ones they come with: [MCP servers](#mcp-servers) and Kepler's [built-in tools](#built-in-tools).

## MCP servers

Use **MCP servers** to give your agents extra tools, for example your issue tracker. The servers here are each agent's own defaults, and every repository inherits them.

To see the servers an agent loads, pick the agent with **Agent**. If that agent has more than 1 account, pick an account too. Kepler lists only the agents that expose their MCP servers to Kepler. In the list:

- Click a server to open its own page. There you can turn the server or a single tool off, sign in to a server that needs it, use **Also add to…** to copy the server to another agent, and **Remove server**.
- Click **Add server** in the section header to add one.

A server or tool you turn off here is off in every repository, unless a repository turns it back on for itself. A repository's own **MCP servers** section is on its [Edit repo](/kepler/settings-repositories#edit-a-repository) page. For some agents, you can also switch a server on or off for one session from the composer. See [MCP Servers](/kepler/mcp-servers).

Below the list, one more setting applies across every agent:

| Setting | What it controls | Default |
|---|---|---|
| **Keep the GitKraken MCP server installed in every agent** | *Gives every command-line agent Git tools and your issues and pull requests through GitKraken. Turn off to manage it yourself.* | On |

Every session Kepler starts also gets Kepler's own workspace tools, which are always on and have no setting. With them, an agent can work with your tasks and their notes, links, files, and worktrees, and with sessions, approvals, and [themes](/kepler/settings-app#theme). With [Built-in tools](#built-in-tools) on, it can also rebase, merge, and compose commits. An agent can name a repository by one of its [aliases](/kepler/settings-repositories#edit-a-repository). For the full list of tools, see [Tasks and Resources](/kepler/tasks-and-resources).

In both Chat and Terminal, workspace tools run without the agent's own permission prompt. Instead, an action that needs your approval, such as deleting a worktree or changing another task, waits for you on an approval card. See [Approval Settings](/kepler/settings-approvals).

## Built-in tools

Use **Built-in tools** to let your agents call Kepler's own tools for rebasing, merging, and cleaning up commits:

| Setting | What it does | Default |
|---|---|---|
| **AI Sync** | *Lets agents rebase or merge your branch and resolve conflicts for you. Every change can be undone.* | Off |
| **AI Compose** | *Lets agents turn messy changes into clean, focused commits. Every change can be undone.* | Off |

A change applies to new agent sessions. Sessions already running keep the tools they started with.

***

---
