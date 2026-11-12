---
title: Dictation and Read Aloud
description: Dictate to an agent instead of typing, and have its replies read aloud. Dictation transcribes on your device with Qwen3-ASR, or with Whisper where WebGPU is unavailable, learns the words you fix, and works push-to-talk or hands-free; read aloud uses your system's voices or Kokoro. Both work in remote windows.
product: Kepler
feature: Voice
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode, grok, pi, antigravity]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [dictation, voice-input, read-aloud, text-to-speech, kokoro, qwen3-asr, whisper, webgpu, microphone, settings, agent-sessions]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Kepler has 2 voice features, both set up in **Settings → Voice**:

- **Dictation** adds a microphone to the agent prompt, so you can talk instead of typing. **Transcription runs on your device**, using a model Kepler downloads once. Kepler never uploads your audio.
- **Read aloud** reads an agent's replies to you. See [Read aloud](#read-aloud).

Dictation has 2 transcription engines:

- **Qwen3-ASR** is the default. It reads what you're writing, so it gets developer terms such as Jira, rebase, or pull request right more often than Whisper. It needs a graphics card with WebGPU.
- **Whisper** works on any machine. Use it where WebGPU is unavailable.

<figure style="text-align:center">
  <a href="/wp-content/uploads/start-voice-input-aug-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/start-voice-input-aug-2026.png" class="help-center-img img-bordered" alt="The composer's microphone icon, with its Start voice input tooltip">
  </a>
  <figcaption style="text-align:center; color:#888">The composer's microphone, with its Dictate tooltip.</figcaption>
</figure>

Dictation turns on once you download a model in **Settings → Voice**. The microphone in the prompt becomes available when the model is ready.

<figure style="text-align:center">
  <a href="/wp-content/uploads/voice-input-settings-aug-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/voice-input-settings-aug-2026-v3@2x.png" class="help-center-img img-bordered" alt="Settings › Voice input with Whisper set up: Use voice input in the chat prompt ticked; Transcription engine with the Whisper card selected and the note that Qwen3-ASR needs a graphics card with WebGPU, which is not available here, then the Fast model, About 42 MB on this machine, with Change quality, Remove Whisper and a collapsed Technical details; and When you stop talking set to Insert the text so you can edit it, with Send the prompt and Keep listening, transcribing each phrase as you pause.">
  </a>
  <figcaption style="text-align:center; color:#888">The Dictation settings on a computer without WebGPU, where Whisper transcribes.</figcaption>
</figure>

***

## Choose what happens when you stop talking

To record, click **Dictate** in the prompt, speak, then click **Stop and transcribe**.

To choose what Kepler does with what you say, go to **Settings → Voice → When you stop talking** and pick one of these options:

| Option | What it does |
|---|---|
| **Insert the text so you can edit it** | Puts the text in the prompt for you to review. This is the default |
| **Send the prompt** | Sends the prompt as soon as you stop recording |
| **Keep listening, transcribing each phrase as you pause** | Keeps the microphone open and transcribes each phrase as you pause |

With Qwen3-ASR, **Keep listening** can correct earlier words in a paragraph as you keep talking. Once you edit that text, Kepler adds only new words and never overwrites what you typed.

Kepler treats short, whole utterances as commands rather than dictation: saying "send", "cancel", or "clear" acts on the prompt instead of adding text to it. Kepler dictates anything longer verbatim.

While a transcription is in progress, the microphone shows **Transcribing…**. If transcription falls behind while you keep talking, Kepler pauses the microphone rather than dropping audio. Wait for it to catch up, or pick a smaller model.

### Teach dictation your words

Qwen3-ASR learns how you spell words it gets wrong. When you fix a single dictated word in the prompt before you send it, Kepler notes the fix. After you make the same fix in 2 sends, a notice suggests the word, and **Review** opens Settings. Dictation uses a suggested word only after you approve it.

**Learned words**, in **Settings → Voice**, lists the words in 2 groups:

- **Suggested words**: each shows what Qwen3-ASR heard, with **Approve** and **Dismiss**. A dismissed fix is never suggested again.
- **Words**: the words you approved and the words you added. Each has a remove button. Type in **Add a word** and click **Add** to add one yourself. **Forget learned words…** removes every learned, suggested, and added word on this device.

Kepler stores only the words, on this device only, and keeps them after you sign out.

<figure style="text-align:center">
  <a href="/wp-content/uploads/voice-learned-words-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/voice-learned-words-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The word sections of Settings › Voice input: Suggested words, Fixes you made in two sends, with Kepler heard as keplar and Approve and Dismiss; then Learned words with its description, Jira (In use · heard as gira) and pnpm (Added by you), each with a remove button, and Forget learned words.">
  </a>
  <figcaption style="text-align:center; color:#888">A suggested word waiting for approval, above the learned words.</figcaption>
</figure>

***

## Set up dictation in Settings

In **Settings → Voice**, the **Dictation** section's **Model** list offers 3 models. Every model runs on this computer, and nothing you say leaves it.

| Model | What it is |
|---|---|
| **Qwen3-ASR 1.7B** | The most accurate, especially with developer terms and mixed languages. Needs a recent graphics card |
| **Qwen3-ASR 0.6B** | Better than Whisper with technical terms, and lighter on memory, for graphics cards with less memory |
| **Whisper** | Works on any machine, including without a compatible graphics card. Less accurate with technical terms |

Kepler checks the graphics card and marks the Qwen3-ASR size it suits as **Recommended**. Without WebGPU, only Whisper can run.

To set up dictation, follow these steps:

1. Open **Settings → Voice**.
2. For Whisper, pick a **Quality** on its row: **Fast**, **Balanced**, **Accurate**, or **Most accurate**. Kepler marks the best fit for this machine as *suggested*.
3. Click **Download** on the model's row.

Your first download turns dictation on. Downloads keep going if you leave the page, and Kepler notifies you when the model is ready. With more than 1 model downloaded, pick the one dictation uses. Until a newly chosen Whisper quality is downloaded, dictation keeps using the one already installed.

Once a model is downloaded, these settings apply:

| Setting | What it does |
|---|---|
| **Remove…** | On a downloaded model's row: deletes the model and frees its storage. Removing the model that dictates turns the microphone off until you pick another |
| **Dictation language** | With a Qwen3-ASR model: the language you speak. See [Dictation language](#dictation-language) |
| **When you stop talking** | Chooses what happens to what you say. See [Choose what happens when you stop talking](#choose-what-happens-when-you-stop-talking) |

### Dictation language

With Qwen3-ASR, **Dictation language** is **Auto-detect** by default, or 1 of 30 languages, each listed by its own name. Choose a language to always dictate in it. **Auto-detect** picks among your system's preferred languages, the app language, and the languages you have dictated in before. Whisper ignores this setting.

### Model updates

When a newer version of a Qwen3-ASR model ships, a notice offers **Update**, and the model's row in **Settings → Voice** keeps offering **Update**. Dictation keeps using the installed model until you update.

### Linux graphics cards

On Linux, Kepler turns WebGPU on so Qwen3-ASR can use the graphics card:

- Under Wayland, WebGPU is on by default.
- Under X11, start Kepler with `--enable-linux-webgpu` to turn it on.
- Start Kepler with `--disable-linux-webgpu` to turn it off.

If Kepler's first window hangs or never draws with WebGPU on, Kepler turns WebGPU off for later launches and restarts. Without WebGPU, use Whisper.

For every dictation and read aloud setting, see [Voice settings](/kepler/settings-app#voice).

***

## Why the microphone is unavailable

Hover the microphone, and its tooltip explains why:

| Tooltip | What it means |
|---|---|
| *Dictation needs a model. Open Settings to download one.* | No model is downloaded yet. Clicking opens Settings |
| *Dictation requires a secure (https) connection* | You're using Kepler over plain HTTP, where the browser will not grant microphone access |
| *Dictation is not supported in this environment* | This build or browser cannot run it |
| *The selected voice model needs WebGPU, which is not available here. Open Settings to choose Whisper.* | A Qwen3-ASR model is selected, but this computer or browser has no WebGPU. Clicking opens Settings |
| *The graphics card is not responding, so dictation cannot start. Open Settings to check it again.* | The graphics card did not answer. Clicking opens Settings |
| *Loading voice model…* / *Transcribing…* | Busy. The button is disabled for the moment |

<figure style="text-align:center">
  <a href="/wp-content/uploads/voice-mic-tooltip-oct-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/voice-mic-tooltip-oct-2026-v2@2x.png" class="help-center-img img-bordered" alt="The New task launcher with the microphone button showing a struck-through mic and its tooltip: The selected voice model needs WebGPU, which is not available here. Open Settings to choose Whisper.">
  </a>
  <figcaption style="text-align:center; color:#888">The microphone with a Qwen3-ASR model selected on a computer without WebGPU.</figcaption>
</figure>

With Qwen3-ASR, the microphone's **Dictate** tooltip also names the model, for example **Dictate · Qwen3-ASR 1.7B**.

When dictation fails, Kepler names the cause, with **Open Settings** where Settings can fix it. For example:

- *A voice model is being installed. Try again when it finishes.*
- *The voice model is no longer downloaded on this computer. Download it again in Settings.*
- *The voice engine stopped responding. Try again; the model reloads on its own.*
- *Dictation stopped unexpectedly.*

***

## Microphone permission on macOS

macOS asks for microphone access the first time you record.

If access is denied or restricted, turn it on in **System Settings → Privacy & Security → Microphone**, if your device policy allows it. **Open System Settings**, in Kepler's message, takes you straight to that pane. You may need to restart Kepler for the change to take effect.

***

## Read aloud

Read aloud speaks an agent's replies to you. Kepler reads only the prose: code blocks, diffs, and tables become a short summary. In the chat, the sentence being read is highlighted.

To have a reply read aloud, use one of these controls:

- **Read aloud**, the speaker button under each chat reply. While that reply plays, the button reads **Stop reading**.
- **Read aloud from here**, in the right-click menu of a message or a terminal session. Kepler reads from the sentence under the pointer through the replies after it.
- **Read last reply**, on a terminal session's status bar.

While anything is being read, **Stop reading** appears in the top bar, on every page.

<figure style="text-align:center">
  <a href="/wp-content/uploads/read-aloud-nov-2026.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/read-aloud-nov-2026.png" class="help-center-img img-bordered" alt="An agent reply in the chat being read aloud: its second sentence, The total now takes the discount off before tax, so a discounted order no longer pays tax on money it never spent, is highlighted, and under the reply the Read aloud button has turned into Stop reading, a square icon between Copy and the reply's time.">
  </a>
  <figcaption style="text-align:center; color:#888">A reply being read aloud, with its current sentence highlighted.</figcaption>
</figure>

The read aloud controls appear only on a computer with a voice to read with. Read aloud starts with your system's voices. To change the voice, follow these steps:

1. Open **Settings → Voice**, and go to **Read aloud**.
2. Under **Voice engine**, choose **System voices** or **Kokoro**. Kokoro has natural English voices and needs a graphics card with WebGPU. Click **Download** to get it. Until Kokoro is downloaded, and for text that is not English, the system voice reads.
3. Pick a **Voice**. Choosing one plays a short sample.
4. Set the **Speed**.

***

## Remote windows

Dictation works in a window attached to a remote environment. The agent runs on the remote machine; the microphone and the transcription stay local, on the computer in front of you.

Over a plain HTTP connection the microphone is unavailable. See [Why the microphone is unavailable](#why-the-microphone-is-unavailable).

Voice settings belong to each computer:

- A desktop window, local or connected to a remote, uses this computer's voice settings.
- A Remote Access browser uses the settings of the Kepler it's connected to.
- Neither the settings nor the models sync between devices.

A remote window or a Remote Access browser may need to download the model once. A different browser, device, or private window downloads it again.

Learned words and the languages this device has dictated in stay on the device in front of you, and never go to the remote machine.

See [Remote Environments](/kepler/remote-environments).

---
