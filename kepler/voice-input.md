---
title: Voice Input
description: Dictate to an agent instead of typing. Voice input transcribes on your device with Qwen3-ASR, or with Whisper where WebGPU is unavailable, learns the words you fix, works push-to-talk or hands-free, and is available in remote windows.
product: Kepler
feature: Voice Input
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode, grok, pi, antigravity]
hosted_variant: both
status: GA
last_verified: 2026-10
llms_include: true
tags: [voice-input, dictation, qwen3-asr, whisper, webgpu, microphone, settings, agent-sessions]
taxonomy:
  category: kepler
---
<kbd>Last updated: October 2026</kbd>

Voice input puts a microphone in the agent prompt so you can talk instead of typing. **Transcription runs on your device**, using a model Kepler downloads once. Kepler never uploads your audio.

Kepler has two transcription engines:

- **Qwen3-ASR** is the default. It reads what you're writing, so it gets developer terms such as Jira, rebase, or pull request right more often than Whisper. It needs a graphics card with WebGPU.
- **Whisper** works on any machine. Kepler uses it where WebGPU is unavailable, and keeps it for anyone who set up Whisper before Qwen3-ASR was available.

<figure style="text-align:center">
  <a href="/wp-content/uploads/start-voice-input-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/start-voice-input-aug-2026.png" class="help-center-img img-bordered" alt="The composer's microphone icon, with its Start voice input tooltip">
  </a>
  <figcaption style="text-align:center; color:#888">The composer's microphone icon.</figcaption>
</figure>
<!-- TODO(screenshot): Replace — ade-start-voice-input-01: on a machine with a WebGPU graphics card, set up Qwen3-ASR 1.7B in Settings → Voice input, then hover the composer's microphone so the tooltip reads Start voice input · Qwen3-ASR 1.7B. -->

Voice input is off until you set it up in **Settings → Voice input**: Kepler downloads a model, and the microphone in the prompt goes live when the model is ready.

<figure style="text-align:center">
  <a href="/wp-content/uploads/voice-input-settings-aug-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/voice-input-settings-aug-2026-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Voice input with Whisper set up: Use voice input in the chat prompt ticked; Transcription engine with the Whisper card selected and the note that Qwen3-ASR needs a graphics card with WebGPU, which is not available here, then the Fast model, About 42 MB on this machine, with Change quality, Remove Whisper and a collapsed Technical details; and When you stop talking set to Insert the text so you can edit it, with Send the prompt and Keep listening, transcribing each phrase as you pause.">
  </a>
  <figcaption style="text-align:center; color:#888">Settings → Voice input on a computer without WebGPU, where Whisper transcribes.</figcaption>
</figure>

***

## Choose what happens when you stop talking

To record, click **Start voice input** in the prompt, speak, then click **Stop and transcribe**.

To choose what Kepler does with what you say, go to **Settings → Voice input → When you stop talking** and pick one of these options:

| Option | What it does |
|---|---|
| **Insert the text so you can edit it** | Puts the text in the prompt for you to review. This is the default |
| **Send the prompt** | Sends the prompt as soon as you stop recording |
| **Keep listening, transcribing each phrase as you pause** | Keeps the microphone open and transcribes each phrase as you pause |

With Qwen3-ASR, **Keep listening** groups phrases you speak without a long pause into one paragraph. As the paragraph grows, Kepler transcribes it again as a whole and replaces the text it already inserted for it, so earlier words can change as you keep talking. Once you edit past that text, your edit wins: Kepler adds only the new words and never overwrites what you typed.

Kepler treats short, whole utterances as commands rather than dictation: saying "send", "cancel", or "clear" acts on the prompt instead of adding text to it. Kepler dictates anything longer verbatim.

While a transcription is in flight, the microphone shows **Transcribing…**. If a streaming session falls behind, it pauses the microphone rather than dropping audio: *Transcribing too slowly — pausing the mic. Wait, or pick a smaller model.*

### Teach dictation your words

Qwen3-ASR learns how you spell words it gets wrong. When you fix a single dictated word in the prompt before you send it, Kepler notes the fix. Kepler learns from a fix only after the prompt is sent and the agent has finished its turn. After you make the same fix in two sends, Kepler suggests the word, with a notice: *A dictated word fix is ready to review*. **Review** opens Settings. Dictation uses a suggested word only after you approve it.

**Settings → Voice input** lists the words in two groups:

- **Suggested words**: *Fixes you made in two sends. Dictation uses a word only after you approve it.* Each shows what Qwen3-ASR heard, with **Approve** and **Dismiss**. A dismissed fix is never suggested again.
- **Learned words**: approved words, marked **In use**, and words you added, marked **Added by you**. Each has a remove button. Type in **Add a word** and click **Add** to add one yourself. **Forget learned words** removes every learned, suggested, and added word on this device.

Kepler stores only the words, on this device only, and keeps them after you sign out. Learning runs only while Qwen3-ASR dictates.

<figure style="text-align:center">
  <a href="/wp-content/uploads/voice-learned-words-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/voice-learned-words-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The word sections of Settings › Voice input: Suggested words, Fixes you made in two sends, with Kepler heard as keplar and Approve and Dismiss; then Learned words with its description, Jira (In use · heard as gira) and pnpm (Added by you), each with a remove button, and Forget learned words.">
  </a>
  <figcaption style="text-align:center; color:#888">A suggested word waiting for approval, above the learned words.</figcaption>
</figure>

***

## Set up voice input in Settings

**Settings → Voice input** has four sections: **Voice input**, **Transcription engine**, **When you stop talking**, and **Learned words**.

**Transcription engine** offers three cards. Every engine runs on this computer, and nothing you say leaves it.

| Engine | What it is |
|---|---|
| **Qwen3-ASR 1.7B** | The most accurate, especially with developer terms and mixed languages. Needs a recent graphics card |
| **Qwen3-ASR 0.6B** | Better than Whisper with technical terms, and lighter on memory, for graphics cards with less memory |
| **Whisper** | Works on any machine, including without a compatible graphics card. Less accurate with technical terms |

Kepler checks the graphics card and marks the Qwen3-ASR size it suits as **Recommended**. A device that never chose an engine starts on that size. Without WebGPU, the page says *Qwen3-ASR needs a graphics card with WebGPU, which is not available here. Whisper works on this computer.*, and Whisper is the engine.

To set up Qwen3-ASR, follow these steps:

1. Open **Settings → Voice input**.
2. Under **Transcription engine**, pick a Qwen3-ASR card.
3. Click **Download and set up**, which shows the download size.

To set up Whisper, follow these steps:

1. Under **Transcription engine**, pick **Whisper**.
2. Under **Set up voice input**, click **Get started**. Kepler checks what this machine can run. This check runs once.
3. Under **Choose transcription quality**, pick **Fast**, **Balanced**, **Accurate**, or **Most accurate**. Kepler marks the best fit for this machine as **Suggested**.
4. Click **Download and set up**.

Setting up turns voice input on. Downloads keep going if you leave the page, and Kepler notifies you when the model is ready. Until a newly chosen model is downloaded, dictation keeps using a model that is already ready, and the page says so.

Once a model is installed, the page offers these settings:

| Setting | What it does |
|---|---|
| **Use voice input in the chat prompt** | Turns the microphone on or off. Turn it off to pause voice input. The downloaded models stay on this computer |
| **Dictation language** | With a Qwen3-ASR model ready: the language you speak. See [Dictation language](#dictation-language) |
| **Remove Qwen3-ASR models** | Deletes every downloaded Qwen3-ASR model and frees their storage. If Qwen3-ASR is what dictates, the microphone stops using it |
| **Change quality** | With Whisper: reopens the quality picker, so you can switch to another Whisper model |
| **Remove Whisper** | Deletes the Whisper model and frees its storage. If Whisper is what dictates, the chat microphone turns off |
| **Technical details** | With Whisper: shows the model ID, its revision, and the backend and data type it runs on |
| **When you stop talking** | Chooses what happens to what you say. See [Choose what happens when you stop talking](#choose-what-happens-when-you-stop-talking) |

If you use Whisper and never chose an engine, on a computer that can run Qwen3-ASR, the page offers **Try Qwen3-ASR for better results** once, with **Switch to Qwen3-ASR (*size*)** and **Not now**.

### Dictation language

With Qwen3-ASR, **Dictation language** is **Auto-detect** by default, or one of 30 languages, each listed by its own name. Choose one to always dictate in it. **Auto-detect** picks among your system's preferred languages and the app language, or among all languages when those name fewer than two. It also leans on the languages this device has reliably dictated in before. Whisper ignores this setting.

### Model updates

When a newer version of a Qwen3-ASR model ships, a notice on this device says once that a newer version of the voice model is available, with **Update**. **Settings → Voice input** keeps offering **Update (*size*)**, and says *A newer version of this model is available. Dictation keeps using the installed one until you update.*

### Linux graphics cards

On Linux, Kepler turns WebGPU on so Qwen3-ASR can use the graphics card:

- Under Wayland, WebGPU is on by default.
- Under X11, start Kepler with `--enable-linux-webgpu` to turn it on.
- Start Kepler with `--disable-linux-webgpu` to turn it off.

If Kepler's first window hangs or never draws with WebGPU on, Kepler turns WebGPU off for later launches and restarts. Without WebGPU, use Whisper.

For the full walkthrough of the setup sequence, see [Settings](/kepler/settings-app#voice-input).

***

## Why the microphone is unavailable

Hover the microphone, and its tooltip explains why:

| Tooltip | What it means |
|---|---|
| *Voice input is off. Turn it on in Settings.* | Not set up yet, or turned off. Clicking opens Settings |
| *Voice input needs a one-time setup. Open Settings to finish it.* | Enabled, but no model is downloaded. Clicking opens Settings |
| *Voice input requires a secure (https) connection* | Kepler is being used over plain HTTP, where the browser will not grant microphone access |
| *Voice input is not supported in this environment* | This build or browser cannot run it |
| *The selected voice model needs WebGPU, which is not available here. Open Settings to choose Whisper.* | A Qwen3-ASR model is selected, but this computer or browser has no WebGPU. Clicking opens Settings at **Transcription engine** |
| *The graphics card is not responding, so voice input cannot start. Open Settings to check it again.* | The graphics card didn't answer. Clicking opens Settings at **Transcription engine** |
| *Loading voice model…* / *Transcribing…* | Busy. The button is disabled for the moment |

<figure style="text-align:center">
  <a href="/wp-content/uploads/voice-mic-tooltip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/voice-mic-tooltip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The New task launcher with the microphone button showing a struck-through mic and its tooltip: The selected voice model needs WebGPU, which is not available here. Open Settings to choose Whisper.">
  </a>
  <figcaption style="text-align:center; color:#888">The microphone with a Qwen3-ASR model selected on a computer without WebGPU.</figcaption>
</figure>

A microphone that is available but idle reads **Start voice input**; while recording, it reads **Stop and transcribe**. With Qwen3-ASR, the tooltip also names the engine, for example **Start voice input · Qwen3-ASR 1.7B**. You can always stop. If the surrounding prompt goes read-only mid-recording, the transcript still lands in the draft.

When voice input fails, Kepler names the cause, with **Open Settings** where Settings can fix it. For example:

- *A voice model is being installed. Try again when it finishes.*
- *The voice model is no longer downloaded on this computer. Download it again in Settings.*
- *The voice engine stopped responding. Try again; the model reloads on its own.*
- *Voice input stopped unexpectedly.*

***

## Microphone permission on macOS

macOS asks for microphone access the first time you record, and Kepler prompts for it rather than failing silently.

If access is denied or restricted, Kepler explains what to do:

> Kepler can't use the microphone because access is denied or restricted. Turn it on in System Settings → Privacy & Security → Microphone if your device policy allows it. You may need to restart Kepler for the change to take effect.

**Open System Settings** takes you straight to the Microphone pane. The guidance stays on screen if the deep link cannot open, so you keep the instructions.

***

## Remote windows

Voice input works in a window attached to a remote environment. The agent runs on the remote machine; the microphone and the transcription stay local, on the computer in front of you.

Over a plain HTTP connection the microphone is unavailable, and its tooltip reads *Voice input requires a secure (https) connection*.

Voice settings belong to each computer:

- A desktop window, local or connected to a remote, uses this computer's voice settings.
- A Remote Access browser uses the settings of the Kepler it's connected to.
- Neither the settings nor the models sync between devices.

Kepler caches downloaded models per browser storage context:

- **A remote Electron window** reuses its model across reconnects and restarts, as long as you're returning to the same saved remote connection from the same desktop app. A different machine, a different profile, or a connection that falls back to a different port needs its own download. Until a Qwen3-ASR model is verified in that window, dictation there uses an installed Whisper model rather than failing or starting a download on its own.
- **Browser-based Remote Access** caches the model per browser, device, and profile. A different browser, device, or a private window needs its own download. The same browser returning to the same address can reuse what it already has, unless that browser has since cleared its storage.

Learned words and the languages this device has dictated in stay in the same storage, on the device in front of you, and never go to the remote machine.

See [Remote Environments](/kepler/remote-environments).

---
