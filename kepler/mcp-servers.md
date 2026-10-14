---
title: MCP Servers
description: See the MCP servers each agent loads, turn a server or a single tool on or off per repository or for every repository, add and remove servers, and sign in to the ones that need it, from inside Kepler.
product: Kepler
feature: MCP Servers
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, opencode, auggie, grok]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [mcp, mcp-servers, model-context-protocol, tools, agents, claude-code, codex, opencode, copilot, cursor, auggie, grok, settings, composer]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Your coding agents load Model Context Protocol (MCP) servers from their own config files. Kepler reads those files and lists exactly the servers each agent will load, so you can see them, turn a server or one of its tools off where you don't want it, add or remove a server, and sign in to a server that needs it. You don't have to edit the agent's config by hand.

You manage them in three places:

- Per repository, from the composer's **Agent settings** pill
- Per repository, in **Settings → Repositories →** *repository* **→ MCP servers**
- As global defaults, in **Settings → Agents → MCP servers**

**Requirements and limits**

- Works for **Claude Code**, **Codex**, **GitHub Copilot**, **Cursor**, **OpenCode**, **Auggie**, and **Grok Build**. Pi, Antigravity, and custom agents don't expose their MCP servers to Kepler; their manager reads *This agent does not expose its MCP servers to Kepler.*
- The agent must be installed. Settings lists only the agents that answer.
- Kepler shows the servers the agent's config files define. Servers that don't live on disk, such as claude.ai connectors, aren't listed.

***

## Where you manage them

| Where | What a change applies to |
|---|---|
| The composer's **Agent settings** pill → **MCP servers** → **Manage** | This repository, for that agent |
| **Settings → Repositories →** *repository* **→ MCP servers** | This repository, for the agent you pick |
| **Settings → Agents → MCP servers** | Every repository, as the default each one inherits |

The **MCP servers** dialog in the composer includes **Open repo settings**, which opens the same list in **Settings → Repositories**.

Every place shows the same manager. It groups servers by where they're defined:

| Group | Where the server comes from |
|---|---|
| **Added by you** | Your own config for the agent, used in every repository |
| **In this repo, shared with your team** | Checked into this repository |
| **In this repo, just you** | This repository only, not shared |
| **From plugins** | Installed by a plugin |
| **Set by your organization** | Managed by your organization |

Each row is a server. The switch on a row turns the server on or off, and clicking the row opens the server's own page. A row can carry these badges:

- **Sign in needed**: the server needs authentication before the agent can use it.
- **Every repo**: a change to the server reaches every repository.
- **Locked**: *Kepler cannot edit this entry in the agent's config file*, such as a server your organization manages.

<figure style="text-align:center">
  <a href="/wp-content/uploads/mcp-servers-dialog-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/mcp-servers-dialog-oct-2026.png" class="help-center-img img-bordered" alt="The MCP servers dialog for Claude Code on the gitkraken-client repository. The User group holds the GitKraken server and the Project group holds playwright-electron, both turned on, with Add server below.">
  </a>
  <figcaption style="text-align:center; color:#888">The MCP servers dialog for one repository.</figcaption>
</figure>
<!-- TODO(screenshot): Replace — The MCP servers dialog at 0.13.0, with the Added by you and In this repo, shared with your team groups, a switch on each row, the Sign in needed, Every repo, or Locked badges, and Open repo settings. -->

***

## Per repository

In a session or in the New task composer, open the **Agent settings** pill. Its **MCP servers** row reads *{enabled} of {total} enabled*; **Manage** opens the **MCP servers** dialog. Its subtitle reads *{agent} in {repo}*, the agent and the repository it applies to. When you open a server's page, **All servers** takes you back to the list.

<figure style="text-align:center">
  <a href="/wp-content/uploads/mcp-agent-settings-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/mcp-agent-settings-oct-2026.png" class="help-center-img img-bordered" alt="The Agent settings menu from the New task composer, with the MCP servers row at the bottom reading 2 of 2 enabled beside a Manage button.">
  </a>
  <figcaption style="text-align:center; color:#888">The MCP servers row in the Agent settings menu.</figcaption>
</figure>

A change here applies to that repository only. Worktrees of one checkout share the setting, so a server you turn off in a repository stays off in every task's worktree of it.

If a server is off in Settings and you haven't turned it on here, it says *Off for every repo in Settings. Turn it on to use it here.*, with **Open Settings** to go to the global default. Turning it on in the dialog turns it on for this repository only.

### Turn off a single tool

A server's page lists its **Tools** under the **Let {agent} use this server** switch. Kepler connects to the server to ask for its tools, so the list can take a moment (*Asking the server for its tools…*). If the server needs authentication first, the list reads *Sign in to this server to see its tools.*

To turn off one tool, open the server's page and turn off the tool's switch. *Turn a tool off to keep {agent} from calling it.*

<!-- TODO(screenshot): New — An MCP server's page at 0.13.0, with Let {agent} use this server, the Tools list with a switch per tool, and Also add to…. -->

Turning off a single tool works for Claude Code, Codex, and Grok Build. For the other agents, turn the whole server off instead.

***

## Global defaults

**Settings → Agents → MCP servers** is the same manager with no repository. Its description reads *Give your agents extra tools, like a database, a browser or your issue tracker.* Use the **Agent** picker at the top to choose the agent, and the account when that agent has more than one.

**Keep the GitKraken MCP server installed in every agent** is on by default. *Gives every command-line agent Git tools and your issues and pull requests through GitKraken. Turn off to manage it yourself.*

<figure style="text-align:center">
  <a href="/wp-content/uploads/mcp-global-defaults-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/mcp-global-defaults-oct-2026.png" class="help-center-img img-bordered" alt="The MCP servers section of Settings → Agents, with a tab for each agent and Claude Code selected. Under User, a GitKraken server is turned on, with Add server below it.">
  </a>
  <figcaption style="text-align:center; color:#888">Global MCP server defaults, in Settings → Agents.</figcaption>
</figure>
<!-- TODO(screenshot): Replace — Settings → Agents → MCP servers at 0.13.0, with the Agent picker, the server list, and Keep the GitKraken MCP server installed in every agent. -->

The two levels combine like this:

- A repository uses the global value until you change that server in its own dialog.
- A repository's choice wins over the global one, in either direction: a repository can turn off a server that's on globally, or turn on a server that's off globally.
- Kepler stores a choice only while it differs from the level beneath it, so switching a server back to match the global default hands control back to the default.

Plugin servers show in Settings but can't be changed there.

***

## Adding and removing servers

To add a server, click **Add server** at the foot of the manager. The **Add MCP server ({agent})** page opens with these fields:

| Field | What it takes |
|---|---|
| **Name** | Letters, numbers, `.`, `_`, or `-`, up to 64 characters, unique where it's saved |
| **Applies to** | **Every repo**, **This repo only**, or **This repo, shared with your team**. The choices depend on the agent and on whether you're in a repository |
| **Runs as** | **Command** for a local server, or **URL** or **URL (SSE)** for a remote one |
| **Command** and **Arguments** | For a command server, for example `npx -y @some/server` |
| **URL** | For a remote server, an `http://` or `https://` address |
| **Environment variables** / **Headers** | Key and value pairs. Values stay hidden until you choose **Show value** |

<figure style="text-align:center">
  <a href="/wp-content/uploads/mcp-add-server-oct-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/mcp-add-server-oct-2026.png" class="help-center-img img-bordered" alt="The Add server form in Settings → Agents → MCP servers for Claude Code, with Name, Transport set to Command, Command, Arguments, and Environment variables fields, and Cancel and Add server buttons.">
  </a>
  <figcaption style="text-align:center; color:#888">Adding a command server.</figcaption>
</figure>
<!-- TODO(screenshot): Replace — The Add MCP server ({agent}) page at 0.13.0, with Name, Applies to, Runs as set to Command, Command, Arguments, and Environment variables. -->

Kepler writes the new server into the agent's own config file, in the format that agent uses, so the agent's CLI sees it too.

To remove a server, open the server's page and click **Remove server**. Kepler deletes the server from the agent's config. You can't undo this. Plugin and managed servers can't be removed from Kepler.

***

## Copy a server to other agents

To use a server you already set up with another agent or account, copy it instead of adding it again. Kepler copies the server's full definition, including its environment variables and headers.

1. Open the server's page.
2. Click **Also add to…**.
3. Select each agent, or each account of an agent, that should get the server.
4. Click **Add to *N* destinations**.

Kepler adds the server to each destination in turn. If one copy fails, the others still go ahead, and the failed destination stays selected with its error.

Servers from plugins can't be copied, so their page doesn't show **Also add to…**.

***

## Signing in

For a server that needs authentication, its page has a **Sign-in** section. It offers **Sign in**, or **Re-authenticate** once you're signed in, and **Clear authentication** to sign it out. Kepler runs the agent's own CLI to do it, under the same account the session uses, so the credentials end up where the agent looks for them. Sign-in is available for Claude Code, Codex, OpenCode, and Cursor servers.

In a local window, **Open sign-in page** opens your browser and Kepler finishes when you're done (*Finish signing in in your browser*). In a window connected to a remote environment, sign in on that page, then paste the URL you land on into **Redirect URL**.

***

## When changes apply

| Where the change lands | When it takes effect |
|---|---|
| A Claude Code **Chat** session | Straight away. Kepler reconnects the session with the new servers and keeps the conversation and your model and mode picks |
| A terminal session, or any other agent's session | On restart. The **Agent settings** pill and the dialog show *{count} MCP changes apply when the agent restarts.* with **Restart agent** |
| The New task composer | The session you start comes up with that state |

Turning a server or tool off doesn't edit the agent's config for Claude Code, Codex, OpenCode, or GitHub Copilot: Kepler keeps the choice itself and passes it to the agent when it launches, so the same agent run from your own terminal is unaffected. The one exception is turning on a Claude Code server that Claude's own config lists as disabled, which Kepler can only do by editing that list. For Auggie, Cursor, and Grok Build, Kepler writes the change into the agent's config file, which their CLIs also read. Adding and removing a server always edits the config file.

Each agent account keeps its own MCP setup. When Kepler launches a Claude Code account other than the default one, it first copies in the default account's servers.

***

## Related

- [Settings](/kepler/settings): **Settings → Agents**, including the **MCP servers** section.
- [Agent Integrations](/kepler/agent-integrations): the agents Kepler runs and how to set them up.
- [Agent Sessions](/kepler/agent-sessions): the composer's **Agent settings** pill, and restarting a session.

---
