---
title: Voice Input
description: Dictate to an agent instead of typing. Voice input transcribes on your device with Whisper, works push-to-talk or hands-free, and is available in remote windows.
product: Kepler
feature: Voice Input
content_type: how-to
audience: developer
plan_required: all
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex-cli, copilot-cli, cursor, auggie, opencode]
hosted_variant: both
status: GA
last_verified: 2026-08
llms_include: true
tags: [voice-input, dictation, whisper, microphone, settings, agent-sessions]
taxonomy:
  category: kepler
---
<kbd>Last updated: August 2026</kbd>

Voice input puts a microphone in the agent prompt so you can talk instead of typing. **Transcription runs on your device**, using a Whisper model Kepler downloads once. Kepler never uploads your audio.

It is off until you turn it on. Enable it in **Settings → Voice Input** and download a model; the microphone in the prompt goes live when the model is ready.

***

## Two ways to talk

Voice input offers two modes:

| Mode | How it works | Setting |
|---|---|---|
| **Push-to-talk** | Click **Start voice input**, speak, then click **Stop and transcribe**. The text lands in the prompt | The default |
| Hands-free | The microphone stays open and each phrase is transcribed as you pause | **Continuous dictation** |

With push-to-talk you can also have Kepler send for you: **Submit after speaking** sends the prompt when you stop recording instead of inserting the text for you to review.

The two are mutually exclusive. Continuous dictation keeps the microphone open, so no single stop exists to submit on. Kepler disables whichever option you didn't choose, with a hint explaining why.

Kepler treats short, whole utterances as commands rather than dictation: saying "send", "cancel", or "clear" acts on the prompt instead of adding text to it. Kepler dictates anything longer verbatim.

While a transcription is in flight, the microphone shows **Transcribing…**. If a streaming session falls behind, it pauses the microphone rather than dropping audio: *Transcribing too slowly — pausing the mic. Wait, or pick a smaller model.*

***

## Settings → Voice Input

The page reveals one step at a time: each step appears only once it can do something.

| Setting | What it controls | Default |
|---|---|---|
| **Enable voice input** | Adds the microphone to the agent chat prompt. Everything below stays hidden until this is on | Off |
| **Check what this computer can run** | A one-time measurement of how fast this machine transcribes, so Kepler can recommend a quality. **Run the check** starts it | Not run |
| Transcription quality | **Fast**, **Balanced**, **Accurate**, **Most accurate**, with the recommendation badged **Suggested**. **Download and set up** installs it | **Fast** preselected |
| **Submit after speaking** | Sends the prompt when you stop recording, instead of inserting the text | Off |
| **Continuous dictation** | Keeps the microphone open and transcribes each phrase as you pause | Off |

Once a model is installed, the page shows **Voice input is ready** with the model, its size on disk, and when it was added. From there:

- **Change quality** reopens the picker.
- **Remove** deletes the model and turns off the chat microphone.
- **Technical details** shows the model ID, its revision, and the backend and data type it runs on.

Downloads keep going if you leave the page, and Kepler notifies you when the model is ready. For the full walkthrough of the setup sequence, see [Settings](/kepler/settings).

***

## Why the microphone is unavailable

Hover the microphone, and its tooltip explains why:

| Tooltip | What it means |
|---|---|
| *Voice input is off. Open Settings to enable it.* | Not enabled yet. Clicking opens Settings |
| *Voice input needs a one-time setup. Open Settings to finish it.* | Enabled, but no model is downloaded. Clicking opens Settings |
| *Voice input requires a secure (https) connection* | Kepler is being used over plain HTTP, where the browser will not grant microphone access |
| *Voice input is not supported in this environment* | This build or browser cannot run it |
| *Loading voice model…* / *Transcribing…* | Busy. The button is disabled for the moment |

A microphone that is available but idle reads **Start voice input**; while recording, it reads **Stop and transcribe**. You can always stop. If the surrounding prompt goes read-only mid-recording, the transcript still lands in the draft.

***

## Microphone permission on macOS

macOS asks for microphone access the first time you record, and Kepler prompts for it rather than failing silently.

If access is denied or restricted, Kepler explains what to do:

> Kepler can't use the microphone because access is denied or restricted. Turn it on in System Settings → Privacy & Security → Microphone if your device policy allows it. You may need to restart Kepler for the change to take effect.

**Open System Settings** takes you straight to the Microphone pane. The guidance stays on screen if the deep link cannot open, so you keep the instructions.

***

## Remote windows

Voice input works in a window attached to a remote environment. The agent runs on the remote machine; the microphone and the transcription stay local, on the computer in front of you.

Over a plain HTTP connection the microphone is unavailable — *Voice input requires a secure (https) connection*.

<!-- TODO(verify): whether the downloaded Whisper model has to be downloaded again per client. src/ui/voice/constants.ts says the model cache lives in IndexedDB per renderer rather than in Kepler's settings, "because, in HTTP/remote mode, different browser clients can hold different local caches" — confirm what that means in practice for a remote window and for browser-based Remote Access before stating it. -->

See [Remote Environments](/kepler/remote-environments).

---
