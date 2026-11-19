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
integrations: [claude-code, codex, copilot, auggie, grok, antigravity]
hosted_variant: both
status: preview
last_verified: 2026-11
llms_include: true
tags: [accounts, multiple-accounts, sign-in, usage-limits, context-window, account-colors]
taxonomy:
  category: kepler
custom_fields:
    nav_category: "kepler-working-in-kepler"
    nav_label: "Agent Accounts and Usage"
    nav_order: 40
    nav_parent: "kepler-working-in-kepler"
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
  <a href="/wp-content/uploads/agent-accounts-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/agent-accounts-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Accounts section of the Claude Code card in Settings › Agents, with Add account above its priority-order help text. Two accounts are listed in order, Claude Code CLI and Personal, each with a drag handle and Check usage, and Personal reads New sessions only.">
  </a>
  <figcaption style="text-align:center; color:#888">The Accounts section, in Settings → Agents.</figcaption>
</figure>

Each account keeps its own credentials but shares your skills, agents, commands, and settings. An account keeps its own conversation history unless it shares history with the CLI, which Claude Code, Codex, and GitHub Copilot accounts can do. A Copilot account shares history unless you choose otherwise.

| Control | What it does |
|---|---|
| First row, badged **Default** | The agent's own login, in its normal config directory |
| **Add account** | Adds an account with its own credentials. For Claude Code, Codex, and GitHub Copilot, you choose **Keep separate** or **Share with the CLI** for its history |
| **Account name** | Rename a row in place. The name is what you pick from later |
| **Sign in** / **Sign out** | Authenticates or clears that account alone |
| **Check usage** | Reads that account's plan usage. Grayed out only when **Check plan usage with each agent's provider** is turned off in **Settings → Agents → Usage and recovery** |
| **Switch account…** | On a signed-in Claude Code account's row menu. Signs that account in with a different Claude login, after a confirmation that counts the running sessions using it |
| **Remove account** | Signs the account out and deletes its local data, but leaves your shared skills, agents, and settings alone. Sessions whose conversations are stored only in that account are deleted with it; see below |
| Color swatch | At the left of each added account's row: pick a color, or **No color**. The default account's ⊘ **No color** mark means it stays uncolored, not that it is off |

**The order of the accounts decides which one Kepler uses.** With 2 or more accounts, drag a row by its handle, or choose **Move to top**, **Move up**, or **Move down** on its row menu. A new session that you start without picking an account starts on the first account with usage left. When a session hits its usage limit, Kepler also turns to the first account with usage left; see [When you hit a usage limit](#when-you-hit-a-usage-limit).

- To keep an account out of that choice, clear **Use at a usage limit** on its row menu. The row then reads **Skipped at a usage limit**.
- An account that keeps its own history reads **New sessions only**, because a conversation cannot move to it.

An account's color tints the agent icon on session tabs, in the context panel, and on the terminal status bar. You can tell sessions on different accounts apart by their color.

**Switch account…** opens the same sign-in as **Add account**. If your browser is already signed in, choose a different account on the sign-in page. On the default row, the switch also changes the account the `claude` command uses in your own terminals, and the confirmation says so.

**An added account can stop sharing your configuration.** An added account links to your own configuration instead of copying it. That configuration includes your settings, instructions, skills, agents, commands, plugins, rules, and hooks. If the agent saves a change to one of these while signed in to that account, the account gets its own copy and stops following yours. Kepler then shows **This account stopped sharing your {items}** under the account's row.

Expand the warning to see which file the account copied, with the paths of **This account's copy** and **Your {item}**. Then choose one of the following:

- **Ask Kepler to resolve**: opens a new Ask Kepler chat with a prompt that asks the agent to compare the 2 copies and copy what matters into your shared copy. Nothing is sent until you send it. See [Ask Kepler](/kepler/ask-kepler).
- **Share your {item} again**: links the account back to your file, after a confirmation. Kepler saves the account's own copy as a backup next to it, so nothing is lost.
- **Keep its own {item}**: keeps the account's copy. **Share your {item} again** then moves to the account's row menu.

<figure style="text-align:center">
  <a href="/wp-content/uploads/account-config-drift-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/account-config-drift-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Claude Code card in Settings › Agents with two accounts. Under the second account, Personal, an open warning reads This account stopped sharing your settings, names its own copy of settings.json and your /home/alex/.claude/settings.json, and offers Ask Kepler to resolve, Share your settings again and Keep its own settings.">
  </a>
  <figcaption style="text-align:center; color:#888">An added account that stopped sharing your settings.</figcaption>
</figure>

**Removing an account tells you what it will remove.** The **Remove {name}?** dialog counts the running sessions it will stop and the sessions it will permanently delete, because their conversations are stored only in this account. To keep those sessions, first click **Move to CLI account** under **Keep these conversations**. The sessions stay in their tasks, and removing the account then deletes nothing. If you do not move them, **Continue to remove** asks you to confirm the deletion once more.

### Choosing an account for a session

If 2 or more accounts are signed in, the **Agent** list shows one row per account, labeled with the account name. You pick the agent and the account in one click, in the **New task** composer or in a draft session tab.

<figure style="text-align:center">
  <a href="/wp-content/uploads/account-multiple-selector-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/account-multiple-selector-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The Agent list open, with two rows under Claude Code: CLI, checked, with alex.lee@example.com and an Acme badge, and Personal. Other agents follow, then Add another account and Install another agent.">
  </a>
  <figcaption style="text-align:center; color:#888">The Agent list, with one row per account.</figcaption>
</figure>

With one account, the agent keeps a single row, with that account shown beside its name.

A session starts on the account you picked, or, if you did not pick one, on the first account in your order with usage left. Later, you can move it to another signed-in account of the same agent and keep the conversation. When more than one account exists, session tabs name the account. If a tab's account has since been removed, the tab reads **(account missing)**.

#### Moving a session to another account

To move a session to another account, use any of these:

- **Continue as** on the session's row or tab menu.
- The **Account** row in the composer's **Agent settings**: **Restart conversation as** on a live session, or **Resume as** on a dormant one.
- **Continue as** at the foot of the plan usage card on a Terminal session's status bar.
- **Continue on {account}** on the usage-limit bar. See [When you hit a usage limit](#when-you-hit-a-usage-limit).
- The **Resume** or **Restart** split button on a dormant session, when another account could take the conversation.

Each list shows the agent's other accounts with their login, color, and usage, and checks the current one. When you pick an account, Kepler restarts the agent with this conversation as that account and confirms **Continued as {login}**.

Some accounts look different in the list:

- An account that keeps its own history is grayed out as **Separate history**, because it cannot read this conversation. To change that, open **Settings → Agents**.
- A signed-out account offers **Sign in…**.
- An account signed in with an API key or a token has no login name. It reads **Signed in**, and you can pick it like any other.

If the session is busy, with a turn running or work still going in the background, Kepler asks first: **Stop this session and continue as {login}?** **Stop and switch** stops the session and resumes the conversation on the new account.

<!-- TODO(screenshot): Replace — ade-continue-as-01: a live session's Agent settings with the Account row open on Restart conversation as, listing the agent's other signed-in account (needs two signed-in accounts of one agent). -->

***

## Signing in through your browser

Claude Code and Codex both sign in through your browser, without a terminal. To sign in, open **Settings → Agents**, click **Sign in**, and pick a method under **Choose how you want to authenticate.**

| Connection | Claude Code | Codex |
|---|---|---|
| Local | Kepler runs the sign-in, your browser opens, and Kepler shows a status line instead of a terminal | Browser sign-in with your ChatGPT account |
| Remote or SSH | **Sign in with Claude.ai**: sign in in your local browser, then paste the code it returns | **ChatGPT (device code)**: sign in with a one-time code in your browser |

A local sign-in offers these controls:

- **Open sign-in in browser**: opens the sign-in page if the browser did not open on its own.
- **Sign-in link**, with **Copy link**: the same address, so you can open it in another browser or profile.
- **Paste the code from your browser**, with **Paste from clipboard** and **Submit code**: appears if the callback cannot complete. If Kepler rejects the code, copy the full code and try again.

On a remote, the same button and **Sign-in link** field sit above the code. Codex shows a **One-time code** to enter there, and Claude Code shows a field for the code your browser returns. If your ChatGPT workspace turns off device sign-in, use **Import local Codex login** or an API key instead.

Auggie signs in the same way locally. On a remote target, Auggie asks you to paste the JSON it returns. GitHub Copilot uses a device code: click **Sign in with GitHub**, then enter a one-time code at `github.com/login/device`.

On a remote Codex target you can also **Import local Codex login** to copy your local Codex sign-in to that target. See [Remote Environments](/kepler/remote-environments).

Before a login expires, Kepler warns you how many days are left. To renew it, sign in again.

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
| **Plan usage** | Your provider plan's windows (**5h** and **7d**) as **Used** and **Resets** columns, plus whatever else the provider reports about the plan | Claude Code and Codex sessions report their own 5-hour and 7-day limits. The full readout, Auggie, GitHub Copilot, and Google Antigravity need **Check plan usage with each agent's provider**, which is on by default |

While a session is idle, the context ring warns about the prompt cache on its own. It shows an hourglass with the time the cache has left, or **Expiring** or **Expired**. The context card then warns that the next message re-reads most of the context. If there is no context reading, the ring is a dashed circle, and its card still shows the cost when the agent reports one.

**Check plan usage with each agent's provider** fetches the full readout, including per-model limits and extra usage, from each agent's provider. It is on by default, in **Settings → Agents → Usage and recovery**:

<figure style="text-align:center">
  <a href="/wp-content/uploads/show-token-usage-aug-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/show-token-usage-aug-2026-v4@2x.png" class="help-center-img img-bordered" alt="The Usage and recovery section of Settings › Agents: Check plan usage with each agent's provider, ticked, with its help text; When a usage limit is reached, a dropdown set to Wait for the reset (Continues on its own when the limit resets), which applies to every agent in chat and in the terminal; and Retry automatically when the model is overloaded, ticked, with its help text.">
  </a>
  <figcaption style="text-align:center; color:#888">The Usage and recovery section of Settings → Agents.</figcaption>
</figure>

Kepler asks with the agent's own sign-in, which goes nowhere else and is never changed. With the setting off, Kepler makes no request to any provider. A Claude Code or Codex session still reports its own **5h** and **7d** readings as it runs, and Kepler shows those, marked as reported by the agent.

The meter shows the shortest window. If the provider reports a balance that cannot be shown as a percentage, the meter shows the remaining plan balance instead. Hover the meter to open the detail. A spent window reads **Limit reached until {time}**. Every reading says how old it is (**Updated {when}**), with **Refresh** to fetch it again.

Kepler judges a usage bar by pace: the share of the window you have used, compared with the share of the window that has passed. The detail reads **On pace** or **Ahead of pace**. When you are ahead, it estimates when you will use up the window. The bar turns amber, then red, as you get ahead of pace or near the limit.

| Provider | What its popover shows |
|---|---|
| **Claude Code** | The **5h** and **7d** windows, an **Extra usage** pool with credits used against any monthly limit, and **Usage limit resets** |
| **Codex** | The same 2 windows, plus **Usage limit resets**: earned resets that clear an active limit early, each with its expiry |
| **Auggie** | No windows, only the plan's name and the credits left on it |
| **GitHub Copilot** | The plan's monthly **Premium**, **Chat**, and **Completions** quotas, each with when it resets, and the credits used on token-based billing. A spent premium quota reads **Premium quota exhausted** |
| **Google Antigravity** | Every limit on the selected model, including its 5-hour and weekly windows, as a percentage used. Antigravity reports no token counts |

**You can spend an earned usage reset from Kepler.** Claude Code and Codex accounts list their earned resets under **Usage limit resets** in the plan usage popover. A Claude Code reset is named by what it refills, such as **Five-hour reset** or **Weekly reset**. To use one, click **Redeem reset**. Kepler warns you first when redeeming now may waste usage: for Codex, when more than 3% of your 7-day allowance is left, and for Claude Code, when the limit the reset refills is not reached yet (**Limit not reached yet**). The confirmation lists your current usage and the reset's expiry. Redeeming uses up the reset and cannot be undone.

<figure style="text-align:center">
  <a href="/wp-content/uploads/usage-reset-redeem-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/usage-reset-redeem-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="The Plan usage popover open under the Codex usage chip in the New task composer, which reads Limit reached until Mar 5, 02:30 PM. The popover shows the account (alex.lee@example.com, Plus), the 5h window at 41% used and the 7d window at 100% used, each with its reset time, then Usage limit resets: 1 available, Expires Mar 16, 02:30 PM, the hint Earned resets that clear an active limit early, and a Redeem reset button, above Updated just now and a refresh button.">
  </a>
  <figcaption style="text-align:center; color:#888">Redeem reset, in the Codex plan usage popover.</figcaption>
</figure>

An account on a third-party Claude provider shows no usage. If Kepler cannot fetch the figures, the meter says which problem it hit instead of showing an old number, such as an agent you need to sign in to. Kepler shows GitHub Copilot usage only for github.com accounts. If Copilot is signed in somewhere Kepler cannot read, such as the macOS keychain, set `COPILOT_GITHUB_TOKEN` to see its usage.

### When you hit a usage limit

Kepler does not keep sending prompts into a spent limit. As soon as the account's usage reading or the agent's own report shows the limit is spent, Kepler holds the prompts you queue until the limit resets. The queue banner says when the queue will be sent.

The prompts go out on their own shortly after the reset, even with no Kepler window open and across a restart. To release one session's queue early, click **Send now**. A spent limit on one model does not hold prompts for the account's other models. With **Check plan usage with each agent's provider** off, a queued prompt waits only if the agent itself says when its limit resets.

<!-- TODO(screenshot): New: The queue banner holding a prompt until the quota resets (*Sending at {time}, when the quota resets.*) with **Send now**. -->

Kepler holds queued prompts this way for every agent whose plan usage it reads. If a turn hits the limit before the agent produced anything, the turn is not lost: Kepler sends the same prompt again after the reset.

When a usage limit cuts off a turn, a limit bar docks on the composer. In a Terminal session with the composer hidden, the bar sits on the status bar. It names the limit the account reached, such as **{account} reached its weekly limit**, and when it resets. Then it offers what can keep the work going:

- **Continue on {account}**: moves this conversation to another of the agent's accounts, which picks up where it stopped. Kepler suggests the first account in your order with usage left; see [Several accounts for one agent](#several-accounts-for-one-agent).
- **New session as {account}** or **Continue in {agent}**: starts a new session, on an account that keeps its own history or on another agent, that reads this conversation first.
- **Wait**: sends a continue message when the account resets.
- **Manage accounts…**, in the bar's account menu, and **Dismiss**.

<figure style="text-align:center">
  <a href="/wp-content/uploads/usage-limit-bar-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/usage-limit-bar-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="A session whose turn was cut off, with the limit bar docked on the composer reading OpenCode reached its usage limit. The bar offers Continue in Claude Code and Dismiss.">
  </a>
  <figcaption style="text-align:center; color:#888">The limit bar, offering to continue in another agent.</figcaption>
</figure>

To choose what Kepler does on its own when a limit is reached, open **Settings → Agents → Usage and recovery → When a usage limit is reached**. The choice applies to every agent, in Chat and in the terminal.

| Choice | What happens |
|---|---|
| **Manual** | The limit bar offers to wait for the reset or switch accounts |
| **Wait for the reset** (the default) | The session continues on its own when the limit resets |
| **Switch accounts** | The session continues on an account with usage left, or after the reset if none has any |

While a session waits for the reset, the bar reads **Waiting for {account}**, with **Cancel**. When Kepler moves the conversation for you, the bar reads **Switched to {account} automatically**.

A Claude Code account can read 100% while the agent still answers, for example on extra usage. Until a turn is refused, the bar only warns, such as **{account} is at its weekly limit**.

---
