# Life Knowledge Engine

**Capture what matters. Reflect with ease.**

*A low-friction media journal that helps people capture everyday encounters with media, add their own reflections, and revisit meaningful patterns over time.*

> **Status:** Early development (v0.1). This repository documents a prototype and its roadmap—not a finished product.

## Why this project?

The most difficult part of a personal knowledge system is often not analysis. It is capturing something worth remembering *at the moment it happens*, and having a simple way to revisit it at the end of the day.

Life Knowledge Engine focuses on two interactions:

1. **Capture:** Share a video, social post, podcast, article, book quote, or spontaneous idea from a phone with minimal effort.
2. **Reflect:** At night, review today's captured items and attach a few sentences of personal thought to the ones that matter.

Later features will support weekly reflection, goals, and optional AI-assisted writing. The project deliberately prioritizes the everyday experience over a complex second-brain dashboard.

## Planned experience

```text
Phone share / voice / photo
          |
          v
Today's Obsidian Daily Note
    time + type + link/text
          |
          v
Evening review: select + reflect
          |
          v
Source-linked insight (optional)
          |
          v
Weekly review and future writing
```

**Example (synthetic):**

```markdown
#### 오늘의 인풋
- 09:32 | YouTube | [Example talk](https://www.youtube.com/watch?v=example)
- 12:45 | Podcast | [Example episode](https://example.com/episode)
```

The date is represented once by the Daily Note filename, such as `2026-11-11.md`; each captured item displays only the capture time.

## Current progress

- [x] Private Obsidian vault, synced across Mac, iPad, and iPhone
- [x] Daily Journal, Source, Insight, and Topic templates
- [x] Manual Source-to-Insight-to-Topic link test
- [x] Local Git repository created
- [ ] iPhone YouTube share to Daily Note with capture time
- [ ] Generalize capture to social posts, podcasts, voice, and book quotes
- [ ] Evening media review and short reflection
- [ ] Weekly review
- [ ] Optional AI enrichment and content generation

## Technology (planned)

- **Obsidian:** private, Markdown-based record storage
- **iOS Shortcuts / Obsidian Share Sheet:** low-friction mobile capture
- **Python:** local formatting, deduplication, and future processing
- **OpenAI / Gemini APIs (optional):** enrichment and review after opt-in
- **GitHub:** public code, tests, and synthetic demonstrations

## Development approach

The public repository is separate from the private Obsidian vault. We will build in small, testable releases. Each release should show user steps saved, supported media types, traceability, and failure handling. See [Product Specification](docs/PRODUCT_SPEC.md), [Architecture](docs/ARCHITECTURE.md), and [Security](docs/SECURITY.md).

## Privacy

This repository must never contain personal journal entries, exported ChatGPT conversations, private media logs, patient information, confidential workplace information, credentials, or actual vault files. All examples are synthetic. AI outputs must never be presented as the user's thoughts without confirmation.

## Roadmap

- **v0.1 — Capture:** Share one YouTube URL from iPhone and record it under today's input heading with local capture time.
- **v0.2 — Multi-input:** Support social links, podcast links, quick voice text, and book excerpts; retain source attribution.
- **v0.3 — Evening Reflection:** Review today's items and add personal reflections with near-zero note management.
- **v0.4 — Weekly Review:** Compile a source-linked weekly digest and optional next actions.
- **Later:** Opt-in, evidence-grounded AI analysis and writing support.

The initial target is a usable prototype by the end of December 2026; milestones may change after real-device testing.

## Getting started

See the [iPhone Capture Prototype](shortcuts/README.md) for an initial, no-server workflow and the [Development Handoff](docs/CODEX_NEXT_TASK.md) for the next Codex task. This prototype is not yet installed or tested on the owner's devices.
