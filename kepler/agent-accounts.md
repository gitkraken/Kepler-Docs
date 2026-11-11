---
title: Agent Accounts and Usage
description: Run several accounts of one agent, move a session between accounts, sign agents in through your browser, and read the context and plan usage indicators.
product: Kepler
feature: Agent Sessions
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot, auggie, grok]
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [accounts, multiple-accounts, sign-in, usage-limits, context-window, account-colors]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "working-in-kepler"
    nav_label: "Agent Accounts and Usage"
    nav_order: 40
    nav_parent: "working-in-kepler"
    page_type: "content"
    card_icon: "users"
    card_color: "blue"
    card_description: "Several accounts of one agent, browser sign-in, and usage indicators"
---
<kbd>Last updated: November 2026</kbd>

Sign in to your agents, run more than one account of the same agent, and track how much of each account's context window and plan you have used.

## Several accounts for one agent

Claude Code, Codex, GitHub Copilot, Auggie, and Grok Build can each have more than one signed-in account. To manage an agent's accounts, open **Settings → Agents**, expand the agent, and find **Accounts**:

<figure style="text-align:center">
  <a href="/wp-content/uploads/agent-accounts-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-accounts-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Claude Code card in Settings › Agents with two accounts, the default Claude Code CLI (Acme, Default) with the No color mark and Personal with a blue color swatch, each with Check usage and a row menu. Below them sit New sessions start in, Let artifact comments start turns, Artifacts in new sessions, and Program and data folder.">
  </a>
  <figcaption style="text-align:center; color:#888">The Accounts section, in Settings → Agents.</figcaption>
</figure>

Each account keeps its own credentials and history but shares your skills, agents, commands, and settings.

| Control | What it does |
|---|---|
| First row, badged **Default** | The agent's own login, in its normal config directory |
| **Add account** | Adds an isolated account with its own credentials and history |
| **Account name** | Rename a row in place. The name is what you pick from later |
| **Sign in** / **Sign out** | Authenticates or clears that account alone |
| **Check usage** | Reads that account's plan usage. Grayed out only when **Check plan usage with each agent's provider** is turned off in **Settings → Agents → Usage limits**: *To check this account's usage, turn on Check plan usage with each agent's provider in Usage limits.* |
| **Switch account…** | On a signed-in Claude Code account's row menu. Signs that account in with a different Claude login, after a confirmation (**Switch the account for {name}?**) that counts the running sessions using it |
| **Remove account** | Signs the account out and deletes its local data, but leaves your shared skills, agents, and settings alone. Sessions whose conversations are stored only in that account are deleted with it; see below |
| Color swatch | At the left of each added account's row (*Pick a color to tell agents on different accounts apart*): **Rose**, **Amber**, **Lime**, **Cyan**, **Blue**, **Violet**, or **No color**. *The default account stays uncolored*, so its picker shows the ⊘ **No color** mark; the mark does not mean the account is off |

An account's color tints the agent icon on session tabs, in the context panel, and on the terminal status bar. You can tell sessions on different accounts apart by their color.

**Switch account…** opens the same sign-in as **Add account**. If your browser is already signed in, choose a different account on the sign-in page. On the default row, the confirmation adds *This also changes the account the claude command uses in your own terminals.* When the sign-in completes, Kepler confirms *{name} is now signed in as {login}.*

**An added account can stop sharing your configuration.** An added account links to your own configuration instead of copying it. That configuration includes your settings, instructions, skills, agents, commands, plugins, rules, and hooks. If the agent saves a change to one of these while signed in to that account, the account gets its own copy and stops following yours. Kepler then shows **This account stopped sharing your {items}** under the account's row.

Expand the warning to see which file the account copied, with the paths of **This account's copy** and **Your {item}**. Then choose one of the following:

- **Ask Kepler to resolve**: opens a new Ask Kepler chat with a prompt that asks the agent to compare the 2 copies and copy what matters into your shared copy. Nothing is sent until you send it. See [Ask Kepler](/kepler/ask-kepler).
- **Share your {item} again**: links the account back to your file. Kepler first asks **Share your {item} with this account again?**: *Its own copy is saved as a backup next to it, so nothing is lost.*
- **Keep its own {item}**: keeps the account's copy. **Share your {item} again** then moves to the account's row menu.

<figure style="text-align:center">
  <a href="/wp-content/uploads/account-config-drift-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/account-config-drift-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Claude Code card in Settings › Agents with two accounts. Under the second account, Personal, an open warning reads This account stopped sharing your settings, names its own copy of settings.json and your /home/alex/.claude/settings.json, and offers Ask Kepler to resolve, Share your settings again and Keep its own settings.">
  </a>
  <figcaption style="text-align:center; color:#888">An added account that stopped sharing your settings.</figcaption>
</figure>

**Removing an account tells you what it will remove.** The **Remove {name}?** dialog works through it in steps:

- Kepler stops the running sessions on the account: *{count} running sessions will be stopped now*.
- Kepler would delete the sessions whose conversations are stored only in this account: *{count} sessions will be permanently deleted*. To keep them, first click **Move to CLI account** under **Keep these conversations**. The sessions stay in their tasks, and removing the account then deletes nothing.
- If you do not move them, **Continue to remove** asks once more: **Permanently delete {count} sessions?** To remove the account, tick *I understand that {count} sessions in {tasks} will be permanently deleted, and that this can't be undone.*

**How many accounts you can add depends on your GitKraken plan.** Pro and higher plans have no limit. If your plan stops covering an account that a running session uses, the session tells you instead of failing silently: *This session runs on a {name} account your plan doesn't cover. Switch it to another account, or upgrade to use this one again.*

### Choosing an account for a session

If 2 or more accounts are signed in, the **Agent** list shows one row per account, labeled with the account name. You pick the agent and the account in one click, in the **New task** composer or in a draft session tab.

<figure style="text-align:center">
  <a href="/wp-content/uploads/account-multiple-selector-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/account-multiple-selector-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Agent list open in the New task composer, grouped by agent. Under a Claude Code heading sit two account rows, CLI (alex.lee@example.com, Acme) with a check mark and Personal, followed by Codex CLI, GitHub Copilot CLI, Cursor, Antigravity, OpenCode and the other agents, then Add another account and Install another agent.">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent list, with one row per account.</figcaption>
</figure>

With one account, the agent keeps a single row, with that account shown beside its name.

A session starts on the account you picked. Later, you can move it to another signed-in account of the same agent and keep the conversation. When more than one account exists, session tabs name the account. If a tab's account has since been removed, the tab reads **(account missing)**.

Kepler reads usage figures from the account the session runs on, not from the first account in the list.

#### Moving a session to another account

To move a session to another account, use any of these:

- **Continue as** on the session's row or tab menu.
- The **Account** row in the composer's **Agent settings**: **Restart conversation as** on a live session, or **Resume as** on a dormant one.
- The agent and account part of a Terminal session's status bar.
- **Continue as {login}** on the usage-limit banner. See [When you hit a usage limit](#when-you-hit-a-usage-limit).
- The **Resume** or **Restart** split button on a dormant session, when another account could take the conversation.

Each list shows the agent's other accounts with their login, color, and usage, and checks the current one. When you pick an account, Kepler restarts the agent with this conversation as that account (*Restarts {name} with this conversation as {login}.*) and confirms **Continued as {login}**.

Some accounts look different in the list:

- An account that keeps its own history is grayed out as **Separate history**: *This account keeps its own history, so it can't read this conversation. Change that in Settings > Agents.*
- A signed-out account offers **Sign in…**.
- An account signed in with an API key or a token has no login name. It reads **Signed in**, and you can pick it like any other.

If the session is busy, with a turn running or work still going in the background, Kepler asks first: **Stop this session and continue as {login}?** **Stop and switch** stops the session and resumes the conversation on the new account. If the session is still restarting, Kepler asks you to try again in a moment.

<!-- TODO(screenshot): Replace — ade-continue-as-01: a live session's Agent settings with the Account row open on Restart conversation as, listing the agent's other signed-in account (needs two signed-in accounts of one agent). -->

***

## Signing in through your browser

Claude Code and Codex both sign in through your browser, without a terminal. To sign in, open **Settings → Agents**, click **Sign in**, and pick a method under **Choose how you want to authenticate.**

| Connection | Claude Code | Codex |
|---|---|---|
| Local | Kepler runs the sign-in, your browser opens, and Kepler shows a status line instead of a terminal | Browser sign-in with your ChatGPT account |
| Remote or SSH | **Sign in with browser**: *Open Claude sign-in in your local browser, then paste the code it returns. Signs in the remote target directly.* | **ChatGPT (device code)**: *Sign in with a one-time code in your browser. Works on any remote.* |

A local sign-in offers these controls:

- **Open sign-in in browser**: opens the sign-in page if the browser did not open on its own.
- **Sign-in link**, with **Copy link**: the same address, so you can open it in another browser or profile. The field stays after the browser opens, because a browser can open where you cannot see it.
- **Paste the code from your browser**, with **Paste from clipboard** and **Submit code**: appears if the callback cannot complete. A rejected code shows *That code was rejected. Copy the full code and try again.*

On a remote, the same button and **Sign-in link** field sit above the code. Codex shows a **One-time code** to enter there, and Claude Code shows a field for the code your browser returns. If your ChatGPT workspace turns off device sign-in, use **Import local Codex login** or an API key instead.

Auggie signs in the same way locally. On a remote target, Auggie asks you to paste the JSON it returns. GitHub Copilot uses a device code: click **Sign in with GitHub**, then enter a one-time code at `github.com/login/device`.

On a remote Codex target you can also **Import local Codex login** to copy your local Codex sign-in to that target. See [Remote Environments](/kepler/remote-environments).

Kepler warns you before a login lapses: *{N} days left before your {agent} login expires. Sign in again to renew it.*

***

## Usage indicators

Kepler shows 2 usage readouts, and they measure different things.

<figure style="text-align:center">
  <a href="/wp-content/uploads/usage-indicators-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/usage-indicators-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Context window card open above the composer's context ring, which sits between the Agent settings pill (Docs Model, Build) and Send: 68%, with 136K tokens Used, 64K Available and 200K Total, and the Estimated cost at API rates, $0.42.">
  </a>
  <figcaption style="text-align:center; color:#888">The Context window card, from the context ring.</figcaption>
</figure>

| Readout | What it shows | Availability |
|---|---|---|
| **Context window** | How much of *this session's* context window is used, as a ring. Hover to see tokens used, available, and total, the **Estimated cost at API rates**, and the **Prompt cache**: when it expires, and how much of the session's input came from it (*{percent}% cached*) | Whenever the agent reports it |
| **Plan usage** | Your provider plan's windows (**5h** and **7d**) as **Used** and **Resets** columns, plus whatever else the provider reports about the plan | Claude Code and Codex sessions report their own 5-hour and 7-day limits. The full readout, Auggie, and GitHub Copilot need **Check plan usage with each agent's provider**, which is on by default |

While a session is idle, the context ring warns about the prompt cache on its own. It shows an hourglass with the time the cache has left, or **Expiring** or **Expired**. The context card then shows the cache first and warns *The next message re-reads most of the context.* If there is no context reading, the ring is a dashed circle, and its card still shows the cost when the agent reports one.

**Check plan usage with each agent's provider** fetches the full readout, including per-model limits and extra usage, from each agent's provider. It is on by default, in **Settings → Agents → Usage limits**:

<figure style="text-align:center">
  <a href="/wp-content/uploads/show-token-usage-aug-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/show-token-usage-aug-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Usage limits section of Settings › Agents: Check plan usage with each agent's provider, ticked, with its help text on what Kepler asks the provider for and what it shows when off, and Resume after the usage limit resets, unticked.">
  </a>
  <figcaption style="text-align:center; color:#888">Check plan usage with each agent's provider, in Settings → Agents → Usage limits.</figcaption>
</figure>

> Kepler asks each agent's provider for your plan usage, per-model limits and extra usage, using the agent's own sign-in. The sign-in goes nowhere else and is never changed. When off, Kepler shows only what agents report, and a message queued at a usage limit is sent automatically only if the agent says when the limit resets.

With the setting off, Kepler makes no request to any provider. A Claude Code or Codex session still reports its own **5h** and **7d** readings as it runs, and Kepler shows those. A card based only on those readings says so: *Reported by the agent. Turn on {setting} in {section} to also see per-model limits and extra usage.*

The meter shows the shortest window. If the provider reports a balance that cannot be shown as a percentage, the meter shows the remaining plan balance instead. Hover the meter to open the detail. A spent window reads **Limit reached until {time}**. Every reading says how old it is (**Updated {when}**), with **Refresh** to fetch it again.

Kepler judges a usage bar by pace: the share of the window you have used, compared with the share of the window that has passed. The detail reads **On pace** or **Ahead of pace**. When you are ahead, it estimates when you will use up the window, for example *Runs out in ~{duration} at this rate*. The bar turns amber, then red, as you get ahead of pace or near the limit.

| Provider | What its popover shows |
|---|---|
| **Claude Code** | The **5h** and **7d** windows, and an **Extra usage** pool with credits used against any monthly limit |
| **Codex** | The same 2 windows, plus **Usage limit resets**: earned resets that clear an active limit early, each with its expiry |
| **Auggie** | No windows, only the plan's credit balance: a plan line naming the plan with what is left of it, *{remaining} / {included} credits left*, or *{remaining} credits left* on an unmetered plan |
| **GitHub Copilot** | The plan's monthly **Premium**, **Chat**, and **Completions** quotas, each with when it resets (an unlimited one is left out), and **{count} credits used** on token-based billing. A spent premium quota reads **Premium quota exhausted** with a warning mark and when it resets, or **Premium quota status unknown** once that reset has passed |

An account on a third-party Claude provider shows no usage. If Kepler cannot fetch the figures, the meter says which problem it hit instead of showing an old number. For example: *Sign in to {agent} to see usage data.*, *Sign in to Copilot through Kepler to see usage data.*, or *This agent doesn't expose usage data.* Where it applies, the meter adds *Your sessions aren't affected.*

### When you hit a usage limit

Kepler does not keep sending prompts into a spent limit. As soon as the account's usage reading or the agent's own report shows the limit is spent, Kepler holds the prompts you queue until the limit resets. It does not wait for a turn to fail first. The queue banner reads *Sending at {time}, when the quota resets.*

The prompts go out on their own shortly after the reset, even with no Kepler window open and across a restart. To release one session's queue early, click **Send now**. A spent limit on one model does not hold prompts for the account's other models. With **Check plan usage with each agent's provider** off, a queued prompt waits only if the agent itself says when its limit resets.

<!-- TODO(screenshot): New: The queue banner holding a prompt until the quota resets (*Sending at {time}, when the quota resets.*) with **Send now**. -->

If a turn hits the limit before the agent produced anything, the turn is not lost: Kepler sends the same prompt again after the reset. If the limit cuts off a turn after the agent started replying, and nothing is queued, the session waits for you. To have Kepler continue on its own, turn on **Settings → Agents → Usage limits → Resume after the usage limit resets**: *When a turn is cut off by your account usage limit and nothing is queued, Kepler queues a "continue" message that is sent shortly after the limit resets.* This setting is off by default. You can send the queued message early or remove it, like any other queued message.

When a session's account reaches its limit, a banner shows **{login} reached its usage limit**, with *Available again at {time}.* To keep working now, click **Continue as {login}**, which moves the conversation to the account with the most usage left. The button's menu lists your other accounts. See [Moving a session to another account](#moving-a-session-to-another-account). If no other account can take the conversation, the banner suggests *Add another account to keep going.*

A Claude Code account can read 100% while the agent still answers, for example on extra usage. Until a turn is refused, the banner only warns that **{login} is at or near its usage limit**.

Kepler handles usage limits this way for the agents it can read usage for: Claude Code, Codex, and Auggie.

---
