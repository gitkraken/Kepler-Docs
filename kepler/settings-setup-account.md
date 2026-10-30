---
title: Setup and Account Settings
description: Reopen Kepler's first-run setup checklist, see who you are signed in as, switch organizations, check what your plan unlocks, and track your GitKraken AI credits, usage by feature, and trials.
product: Kepler
feature: Settings
content_type: reference
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: []
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [settings, setup, account, organization, plan, ai-credits, trials, gitkraken-dev]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Use **Setup** to get back to Kepler's first-run checklist. Use **Account** to see who you are signed in as, which organization you are acting as, what your plan includes, and how you are using your GitKraken AI credits.

## Setup

To reopen the first-run checklist, click **Setup** at the top of the Settings sidebar, under **Search settings**. Its progress ring shows how much of the checklist is done. For what the checklist asks you to do, and how to hide it from the toolbar, see [Getting Started → Finish the setup checklist](/kepler/kepler-getting-started#finish-the-setup-checklist).

***

## Account

The **Account** page has these controls:

| Control | What it does |
|---|---|
| **Account** | Who you are signed in as, with your name and email |
| Organization | Your active organization and its plan. If your GitKraken account belongs to more than 1 organization, this line is a switcher |
| **Refresh account status** | Reads your plan again. Kepler also picks up a purchase or plan change you make outside the app by itself, without a restart |
| **Manage account** / **Manage subscription** | Opens your GitKraken account or subscription on gitkraken.dev |
| **Unlock more with Kepler** | What this plan includes and what it does not. Shown only while something is left to unlock |
| **GitKraken AI credits** | Your credit balance, with **Buy credits**, and **Your usage by feature**. Shown only when there is a balance to show |

The organization you are acting as decides what a feature costs and whether it is unlocked at all.

**Your usage by feature** shows where your AI credits went. It appears once you have used an AI feature. A stacked bar splits your use between your 3 most-used AI features and everything else, shown as **Other**. Below the bar, each feature has a row with its share of your use as a percentage, such as **Commit Message**, **Conflict Resolution**, **Compose Changes**, or **Task & branch names**. To see what a feature does, hover its help icon.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ai-usage-breakdown-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ai-usage-breakdown-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The GitKraken AI credits section of Settings › Account: Your weekly usage 412,500 / 3.2M (13%, resets Sun, Mar 8), Shared weekly credits 18.4M / 80M, and Your usage by feature, a stacked bar over Commit Message 38.3%, Conflict Resolution 27.2%, Compose Changes 18.5%, Task & branch names 9.9% and Pull Request 6.1%, each with a help icon, above Buy credits.">
  </a>
  <figcaption style="text-align:center; color:#888">GitKraken AI credits, with your usage by feature.</figcaption>
</figure>

### When a feature is locked

If a feature is locked on the organization you are acting as but included on another organization you belong to, Kepler offers to switch instead of showing a paywall: *{organization} ({plan}) already includes this.*, with **Switch to organization**.

If you just changed your plan, use **Check again** under **Already upgraded?** on the paywall. If nothing has changed, the paywall reads *Still on {plan}*. A paywall that covers the whole window also shows an account card with **Signed in as**, your **Current organization**, and a **Switch** button for each other organization whose plan includes the feature.

### Trials

When a trial starts, a dialog reads **You just opened up all of Kepler**, with a pill that shows how many days are free (*{count} days free*). It lists what the trial unlocks: *Every feature below is yours until {date}.*

When the trial ends, a dialog reads **Your trial has ended** and lists **What your trial included**. It offers an upgrade or, if your account can start the trial again, a way to continue where you stopped.

---
