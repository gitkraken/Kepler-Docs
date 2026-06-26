---
title: Pull Request Integrations
description: Connect your Git hosting platform to Kepler so you can create Tasks directly from pull requests.
product: Kepler
feature: Pull Request Integrations
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, azure-devops]
integrations: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, azure-devops]
hosted_variant: both
status: GA
last_verified: 2026-06
llms_include: true
tags: [integrations, pull-requests, github, gitlab, bitbucket, azure-devops, oauth]
taxonomy:
  category: kepler
---
<kbd>Last updated: June 2026</kbd>



## Overview

Kepler (GitKraken's Agentic Development Environment, or ADE) connects to your Git hosting platform so you can create a **Task** directly from an existing pull request. Connecting a PR lets an agent address review comments or begin a code review without manual setup.

<figure>
  <img src="/wp-content/uploads/pr-integrations.png" class="help-center-img img-bordered" alt="The Provider Integrations settings panel in Kepler showing Azure DevOps and GitHub as connected, and Bitbucket, GitHub Enterprise, GitLab, GitLab Self-Hosted, Jira, Linear, and Trello available to connect">
  <figcaption style="text-align:center; color:#888">The Provider Integrations settings panel. Connected providers show a Connected badge; others show a Connect button.</figcaption>
</figure>

### Supported providers

| Provider | Auth method | Self-hosted support |
|---|---|---|
| GitHub | OAuth | No |
| GitHub Enterprise | Personal Access Token | Yes |
| GitLab | OAuth | No |
| GitLab Self-Managed | Personal Access Token | Yes |
| Bitbucket | OAuth | No |
| Azure DevOps | OAuth | No |

When you connect a PR, Kepler pulls the following from it:

- Diff
- Description
- Open review comments
- Current review state

***

## GitHub

Connect GitHub to create Kepler Tasks from GitHub pull requests.

### Prerequisites

- A GitHub account with at least read access to the repository.

### Connect GitHub

1. In Kepler, open **Settings** and navigate to **Provider Integrations**.
2. Under **GitHub**, click **Connect**.
3. Authorize Kepler in the GitHub OAuth window that opens.
4. Kepler shows GitHub as connected in **Provider Integrations**.


***

## GitHub Enterprise

Connect GitHub Enterprise using a personal access token to create Kepler Tasks from pull requests on your self-hosted instance.

### Prerequisites

- A GitHub Enterprise account with at least read access to the repository.
- A Personal Access Token (classic) with the `repo` scope, or a fine-grained token with **Contents** (read) and **Pull requests** (read) permissions.

### Connect GitHub Enterprise

1. In Kepler, open **Settings** and navigate to **Provider Integrations**.
2. Under **GitHub Enterprise**, click **Connect**.
3. Enter your GitHub Enterprise **Host URL** (for example, `https://github.example.com`).
4. Paste your **Personal Access Token**.
5. Click **Save**.


***

## GitLab

Connect GitLab to create Kepler Tasks from GitLab merge requests.

### Prerequisites

- A GitLab account with at least Reporter access to the project.

### Connect GitLab

1. In Kepler, open **Settings** and navigate to **Provider Integrations**.
2. Under **GitLab**, click **Connect**.
3. Authorize Kepler in the GitLab OAuth window that opens.
4. Kepler shows GitLab as connected in **Provider Integrations**.


***

## GitLab Self-Managed

Connect GitLab Self-Managed using a personal access token to create Kepler Tasks from merge requests on your self-managed instance.

### Prerequisites

- Access to a GitLab Self-Managed instance with at least Reporter access to the project.
- A Personal Access Token with the `read_api` and `read_repository` scopes.

### Connect GitLab Self-Managed

1. In Kepler, open **Settings** and navigate to **Provider Integrations**.
2. Under **GitLab Self-Managed**, click **Connect**.
3. Enter your GitLab Self-Managed **Host URL** (for example, `https://gitlab.example.com`).
4. Paste your **Personal Access Token**.
5. Click **Save**.


***

## Bitbucket

Connect Bitbucket to create Kepler Tasks from Bitbucket pull requests.

### Prerequisites

- A Bitbucket account with at least read access to the repository.

### Connect Bitbucket

1. In Kepler, open **Settings** and navigate to **Provider Integrations**.
2. Under **Bitbucket**, click **Connect**.
3. Authorize Kepler in the Bitbucket OAuth window that opens.
4. Kepler shows Bitbucket as connected in **Provider Integrations**.


***

## Azure DevOps

Connect Azure DevOps to create Kepler Tasks from Azure DevOps pull requests.

### Prerequisites

- An Azure DevOps account with at least Reader access to the project.

### Connect Azure DevOps

1. In Kepler, open **Settings** and navigate to **Provider Integrations**.
2. Under **Azure DevOps**, click **Connect**.
3. Authorize Kepler in the Azure DevOps OAuth window that opens.
4. Kepler shows Azure DevOps as connected in **Provider Integrations**.


---
