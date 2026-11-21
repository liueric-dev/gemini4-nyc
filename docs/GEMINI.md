# Gemini 4 capabilities

From the Gemini API docs (https://aistudio.google.com/docs), checked 2026-11-19 and 2026-11-20. "Not stated" means the docs read didn't say. Fuller notes with quotes: `../../gemini4/api-facts.md`.

## The four Gemini 4 models

Shared by all four:
- Input: text, image, video, audio, PDF; Office/OpenDocument files since Nov 18.
- Output: **text only**. No image or audio generation.
- Context 1,048,576 tokens. Output 65,536 by default, up to 1M with long decode.
- **Live API: not supported.**
- Function calling, structured output, code execution, Google Search and Maps grounding, URL context, file search, computer use, Batch. Implicit caching only.

| Model | ID | Docs' positioning | Thinking levels | Price in/out per 1M |
|---|---|---|---|---|
| Carbon | `gemini-4-carbon` | "most capable reasoning model" | low, medium, high | $2 / $10 through Nov 30 |
| Neon | `gemini-4-neon` | "fast end-to-end task completion" | low, medium, high, xhigh | $3 / $15, paid tier only |
| Hydrogen | `gemini-4-hydrogen` | "speed and efficiency for everyday" coding and agents | low, medium, high, xhigh | $1.50 / $7.50, free tier too |
| Argon | `gemini-4-argon` | "efficient" frontier reasoning, faster and cheaper than Carbon | low, medium, high | not stated |

No quality or benchmark comparison between them in the docs.

## Decisions API (`gemini-decision-1`)
- Not described as a Gemini 4 model.
- Input: text, image, audio, video or PDF. Up to 100 MB inline (50 MB PDF), 15 MB per external URL, 262,144-token context shared across input and questions.
- 1 to 1,000 questions per request. Types: `noul` (yes/no probability), `choice` (2 to 255 options), `score` (2 to 255 levels).
- Each answer returns probabilities and a `confidence`. Zero output tokens; billed on input only (price not found).
- Not supported: conversation history, tool calls, YouTube or `gs://` URLs, caching, Batch. v1beta only, SDK 3.2+.
- No latency or accuracy figures published. Docs say to set thresholds from your own labelled examples.
- Rate limits: free 200 RPM; tier 1 1,500 RPM.

## Other models (not Gemini 4)
| Job | Model |
|---|---|
| Live voice / video in | `gemini-3.8-live` (sub-second latency; images up to 1 FPS; function calling) |
| Speech out | `gemini-3.8-flash-tts` (voice design from a description, cloning with consent audio) |
| Transcription | `gemini-3.5-transcribe`, `-live` (voice-driven editing since Nov 17) |
| Images | `gemini-nano-banana-2.1` |
| Video | `gemini-omni-1.2-flash` (15 s clips) |
| Interactive worlds | `genie-4`: GA Nov 19, real-time 24 fps video + audio, Interactions API, paid only |
| Music | `lyria-3.5` |
| Robotics | `gemini-robotics-er-2-preview` (preview) |

## Features released Nov 10 to 19
- Nov 10 Carbon GA · Nov 11 Decisions API · Nov 12 Hydrogen GA · Nov 17 Transcribe voice editing
- Nov 18 Neon GA; Office file input; slicing by page, sheet, cell range or time interval in prompts and function responses
- Nov 19 Genie 4 GA; tool retrieval (preview): load tool schemas on demand

Video details: about 100 tokens/s at default resolution, 1 FPS default (custom up to 24), max 10 videos per request, clip with `start_offset`/`end_offset`. Slicing with the Decisions API is not documented; clip client-side.

## Managed Agents (public preview)
- Hosted Ubuntu sandbox (Python 3.12, Node 22); agents Antigravity (default model Hydrogen, selectable) and Deep Research.
- Custom agents via `AGENTS.md` and `SKILL.md`; remote MCP; custom functions; hooks; network allowlist; credentials injected at egress.
- Scheduled triggers (cron), default 600 s timeout per run. Computer use not supported in Antigravity.
- About 100k to 3M tokens per interaction; sandbox compute free during preview.

## Unknown
- Argon price; free-tier status of Carbon, Neon, Argon
- Decisions API price and latency
- Live API session limits
- Whether Google DeepMind provides credits on the day ("coming soon" in the guide)
