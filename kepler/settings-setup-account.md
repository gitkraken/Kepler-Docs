---
title: Setup and Account Settings
description: The Setup and Account entries at the top of Kepler's Settings, covering the first-run setup checklist, who you're signed in as, your organization and plan, what your plan unlocks, GitKraken AI credits and usage by feature, and trials.
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

The first two entries of the Settings rail are about you rather than the app: **Setup** and **Account**.

## Setup

**Setup** sits at the top of the rail, under **Search settings**. Its progress ring shows how much of the first-run checklist is done, and clicking it reopens the checklist. For what the checklist asks you to do, and how to hide it from the toolbar, see [Getting Started → Finish the setup checklist](/kepler/kepler-getting-started#finish-the-setup-checklist).

***

## Account

The Account page has three sections: **Account**, **Unlock more with Kepler**, and **GitKraken AI credits**. The following table lists its controls:

| Control | What it does |
|---|---|
| **Account** | Who you're signed in as, with your name and email |
| Organization | Your active organization and its plan. When your GitKraken account belongs to more than one organization, this line becomes a switcher. What a feature costs, and whether it's unlocked at all, follows the organization you're acting as |
| **Refresh account status** | Re-reads your plan. Kepler also picks up a purchase or plan change made outside the app on its own, with no restart |
| **Manage account** / **Manage subscription** | Opens your GitKraken account or subscription on gitkraken.dev |
| **Unlock more with Kepler** | What this plan does and doesn't include. Shown only while something is left to unlock |
| **GitKraken AI credits** | Your credit balance, with **Buy credits**, and **Your usage by feature**. Shown only when there's a balance to show |

**Your usage by feature** shows where your AI credits went. A stacked bar splits your use between your three most-used AI features and everything else as **Other**. Below the bar, each feature has a row with its share of your use as a percentage, such as **Commit Message**, **Conflict Resolution**, **Compose Changes**, or **Task & branch names**. Hover a feature's help icon for what it does. The breakdown appears only once you've used an AI feature.

<figure style="text-align:center">
  <a href="/wp-content/uploads/ai-usage-breakdown-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/ai-usage-breakdown-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The GitKraken AI credits section of Settings › Account: Your weekly usage 412,500 / 3.2M (13%, resets Sun, Mar 8), Shared weekly credits 18.4M / 80M, and Your usage by feature, a stacked bar over Commit Message 38.3%, Conflict Resolution 27.2%, Compose Changes 18.5%, Task & branch names 9.9% and Pull Request 6.1%, each with a help icon, above Buy credits.">
  </a>
  <figcaption style="text-align:center; color:#888">GitKraken AI credits, with your usage by feature.</figcaption>
</figure>

When a feature is locked on the organization you're acting as but included on another one you belong to, Kepler says so and offers the switch rather than sending you to a paywall: *{organization} ({plan}) already includes this.*, with **Switch to organization**.

A paywall also asks **Already upgraded?** with **Check again**, for a plan you've just changed. If nothing has changed, it says so briefly: *Still on {plan}*. A paywall that covers the whole window also shows an account card: **Signed in as**, your **Current organization**, and a **Switch** button for each other organization whose plan includes the feature.

### Trials

When a trial starts, a dialog reads **You just opened up all of Kepler**, with a pill showing how many days are free (*{count} days free*). It lists what the trial unlocks: *Every feature below is yours until {date}.* When the trial ends, a dialog reads **Your trial has ended** and lists **What your trial included**. It offers an upgrade or, when your account can start the trial again, a way to pick up where you left off.

---
