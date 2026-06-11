---
title: Agent Integrations
description: Connect Claude Code, Codex CLI, Copilot CLI, Cursor, or OpenCode to Kepler and start running agent sessions inside your Tasks.
product: Kepler
feature: Agent Integrations
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, opencode]
hosted_variant: both
status: GA
last_verified: 2026-06
llms_include: true
tags: [agent-integrations, claude-code, codex-cli, copilot-cli, cursor, opencode, setup]
taxonomy:
    category: kepler
---
<kbd>Last updated: June 2026</kbd>

## Overview

Kepler is GitKraken's **Agentic Development Environment** (ADE), a delivery surface that adds task management and Git worktrees around the coding agent you already use. You do not switch agents to use Kepler; you connect the one you already have.

Each connected agent runs as an **agent session** inside a **Task**. A Task is the core unit of work in Kepler: it holds work across one or more repos, manages a **worktree** (a Git worktree per Task per repo), and tracks all changes produced by the session.

### Supported agents

| Agent | Description | Prerequisites | Status |
|---|---|---|---|
| Claude Code | Anthropic's coding agent | Claude Code installed and configured locally | Supported |
| Codex CLI | OpenAI's coding agent | Codex CLI installed and configured locally | Supported |
| Copilot CLI | GitHub's coding agent | Copilot CLI installed and authorized with a GitHub account | Supported |
| Cursor | AI code editor with built-in agent | Cursor installed <!-- TODO: confirm with engineering: auth or API key requirements --> | Supported |
| OpenCode | Open-source, model-agnostic coding agent | OpenCode installed; API key for your chosen model | Supported |

***

## Claude Code

Claude Code is Anthropic's coding agent. Kepler launches it as an agent session inside a Task and passes Task context and repo state automatically at session start.

### Prerequisites

- Claude Code must be installed on your local machine.
- Claude Code must be authenticated with a valid Anthropic API key or Claude.ai account before connecting to Kepler.

### Connect Claude Code to Kepler

1. Open Kepler and navigate to **Settings**.
2. Select **Agent Integrations** from the sidebar.
3. Under **Claude Code**, click **Connect**.
4. Kepler detects the Claude Code installation path automatically. If detection fails, enter the path manually.
5. Click **Save**.

<!-- TODO: confirm with engineering: exact settings path and field names for Claude Code connection -->

<figure>
  <img src="..." class="help-center-img img-bordered" alt="Claude Code connection settings in Kepler">
  <figcaption style="text-align:center; color:#888">Claude Code connection settings panel in Kepler</figcaption>
</figure>

### How Kepler passes context

When you start a Claude Code agent session inside a Task, Kepler automatically provides:

- The Task description and any attached instructions.
- The repo path and the Task's dedicated worktree.
- Branch context so the agent commits to the correct branch.

You do not need to re-describe your Task to the agent manually.

### Verification and troubleshooting

**Claude Code not detected**
Verify that the `claude` binary is on your `PATH` by running `claude --version` in a terminal. If it is not found, reinstall Claude Code or enter the binary path manually in Kepler settings.

**Authentication errors**
Run `claude auth` in a terminal to confirm your session is active. Re-authenticate if the token has expired, then return to Kepler and reconnect.

**Permission errors**
Ensure the user running Kepler has read and execute access to the Claude Code binary and to the repo directory.

***

## Codex CLI

Codex CLI is OpenAI's coding agent. Kepler connects to it as an agent session inside a Task and passes Task context and repo access automatically.

### Prerequisites

- Codex CLI must be installed on your local machine.
- Codex CLI must be configured with a valid OpenAI API key.

### Connect Codex CLI to Kepler

1. Open Kepler and navigate to **Settings**.
2. Select **Agent Integrations** from the sidebar.
3. Under **Codex CLI**, click **Connect**.
4. Kepler detects the Codex CLI installation path automatically. If detection fails, enter the path manually.
5. Click **Save**.

<!-- TODO: confirm with engineering: exact settings path and field names for Codex CLI connection -->

<figure>
  <img src="..." class="help-center-img img-bordered" alt="Codex CLI connection settings in Kepler">
  <figcaption style="text-align:center; color:#888">Codex CLI connection settings panel in Kepler</figcaption>
</figure>

### How Kepler passes context

When you start a Codex CLI agent session inside a Task, Kepler passes:

- The Task description and instructions.
- The repo path and the Task's dedicated worktree.
- Branch context for the session.

### Verification and troubleshooting

**Codex CLI not detected**
Run `codex --version` in a terminal to confirm the binary is on your `PATH`. If not found, reinstall Codex CLI or enter the binary path manually in Kepler settings.

**Authentication errors**
Confirm your `OPENAI_API_KEY` environment variable is set and valid. Re-export the key if it has changed, then reconnect Codex CLI in Kepler settings.

**Permission errors**
Ensure the user running Kepler has read and execute access to the Codex binary and to the repo directory.

***

## Copilot CLI

Copilot CLI is GitHub's coding agent. Kepler connects to it as an agent session and passes Task context and repo access at session start.

### Prerequisites

- Copilot CLI must be installed on your local machine.
- Copilot CLI must be authorized with a GitHub account that has an active Copilot subscription.

### Connect Copilot CLI to Kepler

1. Open Kepler and navigate to **Settings**.
2. Select **Agent Integrations** from the sidebar.
3. Under **Copilot CLI**, click **Connect**.
4. Kepler detects the Copilot CLI installation path automatically. If detection fails, enter the path manually.
5. Click **Save**.

<!-- TODO: confirm with engineering: exact settings path and field names for Copilot CLI connection -->

<figure>
  <img src="..." class="help-center-img img-bordered" alt="Copilot CLI connection settings in Kepler">
  <figcaption style="text-align:center; color:#888">Copilot CLI connection settings panel in Kepler</figcaption>
</figure>

### Verification and troubleshooting

**Copilot CLI not detected**
Run `gh copilot --version` in a terminal to confirm the extension is installed. If not found, install it with `gh extension install github/gh-copilot`.

**Authorization errors**
Run `gh auth status` to confirm your GitHub session is active. Re-authenticate with `gh auth login` if needed, then reconnect in Kepler settings.

**Permission errors**
Ensure the user running Kepler has read and execute access to the `gh` binary and to the repo directory.

***

## Cursor

Cursor is an AI code editor with a built-in coding agent. Kepler connects to Cursor's agent and runs it as an agent session inside a Task.

### Prerequisites

- Cursor must be installed on your local machine.
<!-- TODO: confirm with engineering: whether an API key or Cursor account login is required, and how Kepler authenticates with Cursor -->

### Connect Cursor to Kepler

1. Open Kepler and navigate to **Settings**.
2. Select **Agent Integrations** from the sidebar.
3. Under **Cursor**, click **Connect**.
4. <!-- TODO: confirm with engineering: step-by-step connection flow for Cursor -->
5. Click **Save**.

<figure>
  <img src="..." class="help-center-img img-bordered" alt="Cursor connection settings in Kepler">
  <figcaption style="text-align:center; color:#888">Cursor connection settings panel in Kepler</figcaption>
</figure>

### Verification and troubleshooting

<!-- TODO: confirm with engineering: Cursor-specific detection, auth, and permission troubleshooting steps -->

**Cursor not detected**
Confirm Cursor is installed and that the `cursor` binary is accessible. Enter the binary path manually in Kepler settings if auto-detection fails.

**Authentication or API key errors**
<!-- TODO: confirm with engineering: how Cursor auth errors surface in Kepler and what the resolution is -->

***

## OpenCode

OpenCode is an open-source, model-agnostic coding agent. It runs any model through a unified interface. Use it when you need a model that Claude Code, Codex CLI, or Copilot CLI do not offer.

### Prerequisites

- OpenCode must be installed on your local machine.
- You must have a valid API key for the model you intend to use (for example, Anthropic, OpenAI, or another supported provider).
- <!-- TODO: confirm with engineering: full list of supported models and providers -->

### When to use OpenCode vs. a proprietary agent

Use OpenCode when:

- You want to switch between models without switching agents.
- You are using a model not offered by Claude Code, Codex CLI, or Copilot CLI.
- You want to run a self-hosted or open-weight model.

Use a proprietary agent (Claude Code, Codex CLI, Copilot CLI) when the agent's fixed model meets your needs and you want first-party support.

### Connect OpenCode to Kepler

1. Open Kepler and navigate to **Settings**.
2. Select **Agent Integrations** from the sidebar.
3. Under **OpenCode**, click **Connect**.
4. Kepler detects the OpenCode installation path automatically. If detection fails, enter the path manually.
5. Select or enter the model you want OpenCode to use.
6. Click **Save**.

<!-- TODO: confirm with engineering: exact settings path, field names, and model selector behavior for OpenCode -->

<figure>
  <img src="..." class="help-center-img img-bordered" alt="OpenCode connection settings in Kepler">
  <figcaption style="text-align:center; color:#888">OpenCode connection settings panel in Kepler</figcaption>
</figure>

### Verification and troubleshooting

**OpenCode not detected**
Run `opencode --version` in a terminal to confirm the binary is on your `PATH`. If not found, reinstall OpenCode or enter the binary path manually in Kepler settings.

**API key errors**
Confirm the API key for your chosen model is set correctly. OpenCode reads API keys from environment variables. Verify that the relevant variable (for example, `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`) is exported in your shell environment, then reconnect in Kepler settings.

**Permission errors**
Ensure the user running Kepler has read and execute access to the OpenCode binary and to the repo directory.

---
