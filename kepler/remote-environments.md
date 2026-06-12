---
title: Remote Environments
description: Run Kepler Tasks on a remote machine via SSH or inside a Windows Subsystem for Linux (WSL) environment, or expose Kepler for remote access using the built-in server.
product: Kepler
feature: Remote Environments
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: []
hosted_variant: both
status: GA
last_verified: 2026-06
llms_include: true
tags: [remote-environments, ssh, wsl, remote-access, ngrok, networking]
taxonomy:
   category: kepler
---
<kbd>Last updated: June 2026</kbd>

Kepler (GitKraken's Agentic Development Environment, or ADE) covers two remote scenarios. First, you can run Tasks on a remote machine or WSL environment when you need more compute or a Linux runtime. Second, you can expose Kepler over the network to access it from another device.

***

## SSH: Run Tasks on a Remote Machine

Use SSH when your local machine doesn't have enough compute for the work, or when builds are too slow. When a Task runs via SSH, Kepler runs the worktrees and agent sessions on the remote machine. Kepler's UI remains local.

### Prerequisites

- SSH access to the remote machine (key-based or password authentication).
- Kepler installed locally.
<!-- TODO: confirm with engineering — does the remote machine need any Kepler agent software installed, or does Kepler push it automatically? -->

### Connect a Remote Machine

1. Open Kepler and navigate to **Settings → Remote Environments**.
2. Click **Add Remote Machine**.
3. Enter the SSH connection details:
   - **Host**: hostname or IP address of the remote machine.
   - **Port**: SSH port. Default: `22`.
   - **Username**: the SSH user on the remote machine.
   - **Authentication**: select key-based or password authentication.
4. Click **Test Connection** to verify Kepler can reach the machine.
5. Click **Save**.

After you save, the remote machine is available as a target when you create or configure a Task.

### What Runs Remotely vs. Locally

| Component | Runs on |
|---|---|
| Tasks | Remote machine |
| Worktrees | Remote machine |
| Agent sessions | Remote machine |
| Kepler UI | Local machine |

### Troubleshooting SSH Connections

**Connection refused** — Confirm the SSH daemon is running on the remote machine and the port is open in the firewall.

**Authentication failed** — Verify the username and credentials. For key-based auth, confirm the public key is in `~/.ssh/authorized_keys` on the remote machine.

**Timeout** — Check that the remote machine is reachable from your network. If connecting over a VPN, confirm the VPN is active.

<!-- TODO: confirm with engineering — are there any Kepler-specific logs to check when an SSH connection fails? -->

***

## WSL: Run Tasks in Windows Subsystem for Linux

Use WSL when you are on Windows and need a Linux environment for agent sessions or builds. Kepler connects to a WSL environment the same way it connects to a remote machine via SSH.

### Prerequisites

- WSL installed on the local Windows machine.
- WSL version 2 recommended. <!-- TODO: confirm with engineering — is WSL 2 required, or is WSL 1 supported? -->

### Connect a WSL Environment

1. Open Kepler and navigate to **Settings → Remote Environments**.
2. Click **Add Remote Machine**.
3. For **Host**, enter `localhost` (or the WSL instance address).
4. Configure SSH credentials for the WSL environment as you would for any remote machine.
5. Click **Test Connection**, then **Save**.

The WSL environment is available as a Task target alongside any other remote machines.

### Troubleshooting WSL Connections

**WSL not detected** — Confirm WSL is installed and at least one distribution is running. Run `wsl --list --running` in PowerShell to check.

**Version conflict** — If you experience unexpected behavior, run `wsl --set-default-version 2` in PowerShell to ensure WSL 2 is the default. <!-- TODO: confirm with engineering — specific version requirements for Kepler. -->

**SSH connection refused in WSL** — The SSH daemon may not be running inside WSL. Start it with `sudo service ssh start` inside the WSL terminal.

***

## Remote Access: Access Kepler from Another Device

Remote Access is a separate feature from SSH and WSL. Remote Access starts a local server inside Kepler so you can reach the Kepler UI from another device on your network, or from outside your network via a tunnel.

### Configure Remote Access

Navigate to **Settings → Remote Access** to configure the server before starting it.

| Setting | What it controls | Default | Notes |
|---|---|---|---|
| **Port** | The port Kepler's server listens on | `3000` | Change if port 3000 is in use |
| **Host** | The address the server binds to | `0.0.0.0` | `0.0.0.0` listens on all network interfaces |
| **URL Override** | The URL used in the QR code instead of the auto-detected address | _(none)_ | Use this when connecting through a tunnel, e.g., `https://my-tunnel.ngrok.io` |

### Start Remote Access

1. Open **Settings → Remote Access**.
2. Review the port, host, and URL Override settings.
3. Click **Start**.

Kepler displays a QR code. Scan it with a mobile device or secondary machine to open the Kepler UI in a browser.

### Connect via QR Code

The QR code encodes the access URL based on the auto-detected address, or the **URL Override** if one is set. Scan the code from any device on the same network to open Kepler in a browser.

<figure>
  <img src="..." class="help-center-img img-bordered" alt="Kepler Remote Access settings panel showing port, host, URL Override fields, and a QR code">
  <figcaption style="text-align:center; color:#888">Remote Access settings with QR code displayed after clicking Start.</figcaption>
</figure>

### Expose Kepler Outside the Local Network with ngrok

To access Kepler from outside your local network, use a tunneling tool such as ngrok.

1. Install ngrok and authenticate it with your ngrok account.
2. Start Kepler's Remote Access server (see above).
3. In a terminal, run:
   ```
   ngrok http 3000
   ```
   Replace `3000` with your configured port if you changed the default.
4. Copy the public URL ngrok generates (for example, `https://abc123.ngrok.io`).
5. In **Settings → Remote Access**, paste the ngrok URL into the **URL Override** field.
6. Click **Start** (or **Restart** if the server is already running).

The QR code now encodes the ngrok URL, and Kepler is accessible from any device with internet access.

### Security Considerations

By default, Kepler's Remote Access server does not require authentication. Anyone who can reach the server URL can access your Kepler instance.

<!-- TODO: confirm with engineering — is any authentication or token-based access available for Remote Access? -->

To limit who can connect:

- Use Remote Access only on trusted networks, or behind a tunnel that enforces authentication (such as ngrok's OAuth/IP restriction options).
- Stop the Remote Access server when you are not using it by clicking **Stop** in **Settings → Remote Access**.
- If using ngrok or a similar tunnel, use the URL Override field so the QR code reflects the secured tunnel URL rather than the local address.

---
