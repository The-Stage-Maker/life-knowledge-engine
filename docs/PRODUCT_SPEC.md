# Product Specification — Media Capture MVP

## Product intent

Create a **low-friction media journal** rather than another general-purpose AI knowledge organizer. The owner's primary goals are (1) effortless daily capture across media formats, (2) a brief evening reflection on selected captures, and (3) simple recurring reflection. This document describes the *planned* first milestone; it does not claim the feature works yet.

## MVP-1: iPhone YouTube capture

**Trigger:** User chooses **Share** in YouTube and runs a configured iOS Shortcut or Obsidian Share Sheet Location.

**Destination:** The existing private Obsidian vault, named `My Life Knowledge Base`, in `01 Daily Journal/YYYY-MM-DD.md` using the daily-note mechanism.

**Target section:** `#### 오늘의 인풋`.

**Canonical visible format:**

```
- HH:mm | YouTube | [Title](https://www.youtube.com/watch?v=...)
```

**Rules:**
- Daily Note filename holds the date. Never add a repeated date on each capture.
- `HH:mm` is the local **capture time**, not viewing time or video publication time.
- Preserve at least the original URL even if title extraction fails. Use `YouTube video` as a fallback title.
- Never overwrite existing Daily Note text or user formatting. Append only under the designated heading when supported.
- Handle the case where today's Daily Note does not exist yet. Research/verify a safe workflow on device before claiming reliable background capture.
- Avoid duplicate entries where feasible, but never silently drop distinct annotations on the same URL.
- A device may be offline; make failures visible and retry safely without losing the original shared URL.
- No paid API or external server is required for this initial capture.

## Acceptance tests

1. Share a public YouTube video in iPhone YouTube → one new item under `오늘의 인풋`.
2. The Daily Note filename is the only visible date; record shows local `HH:mm`.
3. Existing notes and templates remain unchanged.
4. A capture still preserves the URL when title lookup fails.
5. A new day works without manually creating the daily note, or the limitation is documented and clearly addressed.
6. Mac and iPad receive the new item after iCloud synchronization.
7. No data from the vault enters the public Git repository.

## Following milestones

**MVP-2:** Social post / podcast / web link / quick voice transcription / book quote captured with consistent source and time metadata.

**MVP-3:** One-screen evening review displaying the day's captures; user chooses items and speaks or types their own short reflection. The system creates a linked Insight Note only after user confirmation.

**MVP-4:** Weekly review of captured media, user-authored reflections, unresolved questions, and optional goals/next steps. AI interpretation must cite sources and label uncertainty.

## Non-goals for MVP-1

- Passive collection of every viewed YouTube video
- Unattended publishing to social media
- Auto-generating personal opinions
- Importing confidential work or patient data
- Live, complete export of all ChatGPT conversations
