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
4. After authorization, GitHub is now connected in **Provider Integrations**.

<figure>
  <img src="/wp-content/uploads/github-integration-connected.png" class="help-center-img img-bordered" alt="GitHub shown as connected in Kepler Provider Integrations settings">
  <figcaption style="text-align:center; color:#888">GitHub connected in Kepler Integrations</figcaption>
</figure>

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

<figure>
  <img src="/wp-content/uploads/github-enterprise-integration.png" class="help-center-img img-bordered" alt="GitHub Enterprise connection form in Kepler showing host URL and token fields">
  <figcaption style="text-align:center; color:#888">GitHub Enterprise connection form in Kepler</figcaption>
</figure>

***

## GitLab

Connect GitLab to create Kepler Tasks from GitLab merge requests.

### Prerequisites

- A GitLab account with at least Reporter access to the project.

### Connect GitLab

1. In Kepler, open **Settings** and navigate to **Provider Integrations**.
2. Under **GitLab**, click **Connect**.
3. Authorize Kepler in the GitLab OAuth window that opens.
4. After authorization, GitLab is now connected in **Provider Integrations**.

<figure>
  <img src="/wp-content/uploads/gitlab-integration-connected.png" class="help-center-img img-bordered" alt="GitLab shown as connected in Kepler Provider Integrations settings">
  <figcaption style="text-align:center; color:#888">GitLab connected in Kepler Integrations</figcaption>
</figure>

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

<figure>
  <img src="/wp-content/uploads/gitlab-self-managed-integration.png" class="help-center-img img-bordered" alt="GitLab Self-Managed connection form in Kepler showing host URL and token fields">
  <figcaption style="text-align:center; color:#888">GitLab Self-Managed connection form in Kepler</figcaption>
</figure>

***

## Bitbucket

Connect Bitbucket to create Kepler Tasks from Bitbucket pull requests.

### Prerequisites

- A Bitbucket account with at least read access to the repository.

### Connect Bitbucket

1. In Kepler, open **Settings** and navigate to **Provider Integrations**.
2. Under **Bitbucket**, click **Connect**.
3. Authorize Kepler in the Bitbucket OAuth window that opens.
4. After authorization, Bitbucket is now connected in **Provider Integrations**.

<figure>
  <img src="/wp-content/uploads/bitbucket-integration-connected.png" class="help-center-img img-bordered" alt="Bitbucket shown as connected in Kepler Provider Integrations settings">
  <figcaption style="text-align:center; color:#888">Bitbucket connected in Kepler Integrations</figcaption>
</figure>

***

## Azure DevOps

Connect Azure DevOps to create Kepler Tasks from Azure DevOps pull requests.

### Prerequisites

- An Azure DevOps account with at least Reader access to the project.

### Connect Azure DevOps

1. In Kepler, open **Settings** and navigate to **Provider Integrations**.
2. Under **Azure DevOps**, click **Connect**.
3. Authorize Kepler in the Azure DevOps OAuth window that opens.
4. After authorization, Azure DevOps is now connected in **Provider Integrations**.

<figure>
  <img src="/wp-content/uploads/azure-devops-integration-connected.png" class="help-center-img img-bordered" alt="Azure DevOps shown as connected in Kepler Provider Integrations settings">
  <figcaption style="text-align:center; color:#888">Azure DevOps connected in Kepler Integrations</figcaption>
</figure>

---
