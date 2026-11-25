---
title: Dictation and Read Aloud
description: Dictate to an agent instead of typing, in the prompt or straight into a Terminal session, and have its replies read aloud. Dictation transcribes on your device with Qwen3-ASR, Parakeet, or Whisper, learns the words you fix, and types as you talk or when you stop; read aloud uses your system's voices or Kokoro. Both work in remote windows.
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
tags: [dictation, voice-input, read-aloud, text-to-speech, kokoro, qwen3-asr, parakeet, whisper, webgpu, microphone, settings, agent-sessions]
taxonomy:
  category: kepler
---
<kbd>Last updated: November 2026</kbd>

Kepler has 2 voice features, both set up in **Settings → Voice**:

- **Dictation** adds a microphone to the agent prompt and to a Terminal session's status bar, so you can talk instead of typing. **Transcription runs on your device**, using a model Kepler downloads once. Kepler never uploads your audio.
- **Read aloud** reads an agent's replies to you. See [Read aloud](#read-aloud).

Dictation has 3 transcription engines:

- **Qwen3-ASR** reads what you're writing, so it gets developer terms such as Jira, rebase, or pull request right more often than Whisper. It needs a graphics card with WebGPU.
- **Parakeet** is fast, and understands English and 24 other European languages. It needs a graphics card with WebGPU and 16-bit float shader support.
- **Whisper** works on any machine. Use it where WebGPU is unavailable.

<figure style="text-align:center">
  <a href="/wp-content/uploads/start-voice-input-aug-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/start-voice-input-aug-2026-v3@2x.png" class="help-center-img img-bordered" alt="The New task composer: Add issue, Add PR and Add context above the empty prompt, then the attach button, the microphone button with its Dictate tooltip and the shortcut Ctrl Shift Space below it, and the Chat / Terminal switch; on the right, the agent pill with a warning sign and Start.">
  </a>
  <figcaption style="text-align:center; color:#888">The composer's microphone, with its Dictate tooltip.</figcaption>
</figure>

Dictation turns on once you download a model in **Settings → Voice**. The microphone in the prompt becomes available when the model is ready.

<figure style="text-align:center">
  <a href="/wp-content/uploads/voice-input-settings-aug-2026-v6@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/voice-input-settings-aug-2026-v6@2x.png" class="help-center-img img-bordered" alt="The Dictation section of Settings › Voice: under Speech model, Whisper (80 MB) is picked with Remove…, Licenses and a select at Fast (80 MB), and a Qwen3-ASR 1.7B and 0.6B row says they need a graphics card with WebGPU. Below come Dictation language (Auto-detect), Dictation mode with Type as you talk picked beside Type when you stop and Send when you stop, and Vocabulary (No words yet, Manage, Qwen speech models only).">
  </a>
  <figcaption style="text-align:center; color:#888">The Dictation settings on a computer without WebGPU, where Whisper transcribes.</figcaption>
</figure>

***

## Choose what happens when you stop talking

To record, click **Dictate** in the prompt, or press **Ctrl/⌘ + Shift + Space** (**Toggle dictation**), and speak. Click the microphone again to stop, or press the shortcut again. The shortcut works in whichever message box has focus and a microphone, including the **New task** composer and a Terminal session.

While you dictate, the **Search Kepler** field in the top bar shows **Listening…** and your words. Click it to stop.

To change the **Speech model**, **Dictation mode**, or **Dictation language** without opening Settings, right-click the microphone. **Voice settings…** opens **Settings → Voice**.

To choose what Kepler does with what you say, go to **Settings → Voice → Dictation mode** and pick one of these options:

| Option | What it does |
|---|---|
| **Type as you talk** | Each phrase appears in the prompt when you pause, until you press the mic again. This is the default |
| **Type when you stop** | Everything you said appears in the prompt when you press the mic again, ready to edit |
| **Send when you stop** | The prompt is sent with what you said when you press the mic again |

With Qwen3-ASR or Parakeet, the phrase you are saying shows in the prompt as you speak. With Qwen3-ASR, **Type as you talk** can correct earlier words in a paragraph as you keep talking. Once you edit that text, Kepler adds only new words and never overwrites what you typed.

Kepler treats short, whole utterances as commands rather than dictation: saying "send", "cancel", or "clear" acts on the prompt instead of adding text to it. Kepler dictates anything longer verbatim.

While a transcription is in progress, the microphone shows **Transcribing…**. If transcription falls behind, Kepler pauses the microphone until it catches up. If this happens often, pick a smaller model.

### Dictate in a Terminal session

In a Terminal session, the microphone sits on the status bar while Kepler's message box is hidden. Click it, or press **Ctrl/⌘ + Shift + Space**, and speak. A caption shows **Listening…** and then your words, and Kepler types the text into the agent's own input, following your **Dictation mode**.

Dictation only adds to the agent's input, so saying "clear" does not erase it: clear it in the terminal. If the agent cannot take input yet, Kepler moves the dictated text to the message box.

Right-click the status-bar microphone for the same dictation menu as in the prompt.

### Teach dictation your words

Qwen3-ASR learns how you spell words it gets wrong. When you fix a single dictated word in the prompt before you send it, Kepler notes the fix. After you make the same fix in 2 sends, a notice suggests the word, and **Review** opens the **Vocabulary** page. Dictation uses a suggested word only after you approve it.

**Vocabulary**, in **Settings → Voice**, shows how many words dictation knows. Click **Manage** to open the **Vocabulary** page. **Manage** works only while a Qwen3-ASR model dictates. On the page:

- **Suggested words** each show what Qwen3-ASR heard, with **Approve** and **Dismiss**. A dismissed fix is never suggested again.
- Below them, the words you approved and the words you added each have a remove button. To add a word yourself, type it in **Add a word** and click **Add**.
- **Forget learned words…** removes every learned, suggested, and added word on this device.

Kepler stores only the words, on this device only, and keeps them after you sign out.

<figure style="text-align:center">
  <a href="/wp-content/uploads/voice-learned-words-oct-2026-v4@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/voice-learned-words-oct-2026-v4@2x.png" class="help-center-img img-bordered" alt="Settings › Voice › Vocabulary: words you fix in dictated text are suggested here and kept on this device, for Qwen speech models only. Suggested words lists Kepler, heard as keplar, with Approve and Dismiss, above the words Jira and pnpm with remove buttons, the Add a word field with Add, and Forget learned words….">
  </a>
  <figcaption style="text-align:center; color:#888">The Vocabulary page, with a suggested word waiting for approval above the learned words.</figcaption>
</figure>

***

## Set up dictation in Settings

**Settings → Voice** opens with **Check your setup**, where you can try dictation and read aloud before you talk to an agent:

- **Microphone** picks the microphone dictation listens to, saved for this window. Click **Try dictation**, the microphone button beside it, and speak to test it. Nothing you say there is sent to an agent.
- **Speaker** picks the speaker Kokoro reads replies on. System voices always play on the system default. Click **Play a reply**, the play button beside it, to hear a sample.

If the microphone or speaker you picked is not connected, Kepler tells you and uses the system default.

<figure style="text-align:center">
  <a href="/wp-content/uploads/voice-check-setup-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/voice-check-setup-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="Check your setup in Settings › Voice: Microphone is set to System default, saved for this window and not synced, beside a Try dictation mic button. Speaker reads System default, greyed because system voices always play on the system default (pick Kokoro to choose a speaker), beside a Play a reply button.">
  </a>
  <figcaption style="text-align:center; color:#888">Check your setup, with the microphone and speaker Kepler uses.</figcaption>
</figure>

Below it, the **Dictation** section's **Speech model** list offers these models. Every model runs on this computer, and nothing you say leaves it.

| Model | What it is |
|---|---|
| **Qwen3-ASR** | Gets developer terms and mixed languages right more often than Whisper. Pick a **Qwen3-ASR size**: **1.7B** is the most accurate, **0.6B** suits graphics cards with less memory |
| **Parakeet TDT 0.6B v3** | A fast model for English and 24 other European languages that detects which one you speak. Listed only when the graphics card supports it |
| **Whisper** | Works on any machine, including without a compatible graphics card. Less accurate with technical terms |

Kepler marks the model that suits this computer and your languages **Recommended**. Without WebGPU, only Whisper can run.

To set up dictation, follow these steps:

1. Open **Settings → Voice**.
2. For Qwen3-ASR, pick a **Qwen3-ASR size**. For Whisper, pick a quality from **Fast** to **Most accurate**. **Automatic** uses the quality Kepler suggests for this machine.
3. Click **Download** on the model's row.

Your first download turns dictation on. Downloads keep going if you leave the page, and Kepler notifies you when the model is ready. With more than 1 model downloaded, pick the one dictation uses.

Once a model is downloaded, these settings apply:

| Setting | What it does |
|---|---|
| **Remove…** | On a downloaded model's row: deletes the model and frees its storage. Removing the model that dictates turns the microphone off until you pick another |
| **Dictation language** | With a Qwen3-ASR model: the language you speak. See [Dictation language](#dictation-language) |
| **Dictation mode** | Chooses what happens to what you say. See [Choose what happens when you stop talking](#choose-what-happens-when-you-stop-talking) |
| **Vocabulary** | With a Qwen3-ASR model: the words dictation learned from your fixes. See [Teach dictation your words](#teach-dictation-your-words) |

### Dictation language

With Qwen3-ASR, **Dictation language** is **Auto-detect** by default, or 1 of 30 languages, each listed by its own name. Choose a language to always dictate in it. Parakeet and Whisper detect the language you speak, so the setting is unavailable with them.

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

Hover the microphone, and its tooltip explains why. When the model cannot dictate, clicking the microphone opens the dictation menu, where you can download or choose another model.

| Tooltip | What it means |
|---|---|
| *Download a model first* | No model is downloaded yet |
| *Dictation requires a secure (https) connection* | You're using Kepler over plain HTTP, where the browser will not grant microphone access |
| *Dictation is not supported in this environment* | This build or browser cannot run it |
| *Choose Whisper here. The selected model needs WebGPU, which is not available.* | A Qwen3-ASR or Parakeet model is selected, but this computer or browser has no WebGPU |
| *The graphics card is not responding, so dictation cannot start. Open Settings to check it again.* | The graphics card did not answer |
| *Loading voice model…* / *Transcribing…* | Busy. The button is disabled for the moment |

<figure style="text-align:center">
  <a href="/wp-content/uploads/voice-mic-tooltip-oct-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/voice-mic-tooltip-oct-2026-v3@2x.png" class="help-center-img img-bordered" alt="The New task launcher with the microphone button showing a struck-through mic and its tooltip: Dictate, with the shortcut Ctrl Shift Space, over Choose Whisper here. The selected model needs WebGPU, which is not available.">
  </a>
  <figcaption style="text-align:center; color:#888">The microphone with a Qwen3-ASR model selected on a computer without WebGPU.</figcaption>
</figure>

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

- **Read aloud**, the speaker button under each chat reply. While that reply plays, the button pauses and resumes it, and **Stop reading** appears beside it.
- **Continuous reading**, the headphones button in the composer and on a Terminal session's status bar. It reads the latest reply, then each new one as it arrives, until you stop. Right-click it to change the **Speech model**, **Voice**, or **Speed**, or to open **Voice settings…**.
- **Read aloud from here**, in the right-click menu of a message or a terminal session. Kepler reads from the sentence under the pointer through the replies after it.
- **Read the last reply aloud, or pause and resume it**, a shortcut for the focused session, with no default key. Assign one in **Settings → Keyboard shortcuts**.

During continuous reading, the **Read aloud** bar above the composer shows the sentence being read, with buttons to pause, skip to the next reply, or stop, and a **Continuous reading** toggle.

<figure style="text-align:center">
  <a href="/wp-content/uploads/read-aloud-bar-nov-2026-v2@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/read-aloud-bar-nov-2026-v2@2x.png" class="help-center-img img-bordered" alt="Above a session's composer, the Read aloud bar shows Pause reading, Skip to the next reply and Stop reading, the status Reading aloud, the sentence being read and Continuous reading turned on; in the composer footer the Continuous reading button (headphones) is pressed.">
  </a>
  <figcaption style="text-align:center; color:#888">The Read aloud bar during continuous reading.</figcaption>
</figure>

While anything is being read, the **Search Kepler** field in the top bar shows **Reading aloud** and the sentence. Click it to stop reading.

<figure style="text-align:center">
  <a href="/wp-content/uploads/read-aloud-nov-2026-v3@2x.png" target="_blank" rel="noopener noreferrer">
    <img src="/wp-content/uploads/read-aloud-nov-2026-v3@2x.png" class="help-center-img img-bordered" alt="An agent reply in the chat being read aloud: its second sentence, The total now takes the discount off before tax, so a discounted order no longer pays tax on money it never spent, is highlighted, and under the reply the Read aloud button has turned into Pause reading, with Stop reading beside it, between Copy and the reply's time.">
  </a>
  <figcaption style="text-align:center; color:#888">A reply being read aloud, with its current sentence highlighted.</figcaption>
</figure>

The read aloud controls appear only on a computer with a voice to read with. Read aloud starts with your system's voices. To change the voice, follow these steps:

1. Open **Settings → Voice**, and go to **Read aloud**.
2. Under **Speech model**, choose **System** or **Kokoro**. Kokoro has natural English voices and needs a graphics card with WebGPU. Click **Download** to get it. Until Kokoro is downloaded, and for text that is not English, the system voice reads. To pick the speaker Kokoro plays on, use **Speaker** in [Check your setup](#set-up-dictation-in-settings).
3. Pick a **Voice**. Choosing one plays a short sample.
4. Set the **Speed**.

***

## Remote windows

Dictation works in a window attached to a remote environment. The agent runs on the remote machine; the microphone and the transcription stay local, on the computer in front of you.

Over a plain HTTP connection the microphone is unavailable. See [Why the microphone is unavailable](#why-the-microphone-is-unavailable).

Voice settings belong to each computer:

- Every desktop window uses this computer's voice settings, including a window connected to a remote.
- A Remote Access browser uses the settings of the Kepler it's connected to.
- Neither the settings nor the models sync between devices.

A remote window or a Remote Access browser may need to download the model once. A different browser, device, or private window downloads it again.

Vocabulary words and the languages this device has dictated in stay on the device in front of you, and never go to the remote machine.

See [Remote Environments](/kepler/remote-environments).

---
