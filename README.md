# Life Knowledge Engine

**Capture what matters. Reflect with ease.**

A low-friction personal media journal: share a source into today's Obsidian Daily
Note, then return later to reflect.

## iPhone Media Capture v0.1

**Status: basic iPhone capture confirmed by user-reported tests on November 12,
2026; edge-case verification remains pending.** No installable Shortcut export
is included in this repository.

Default workflow: Share URL or text → local time → Markdown text → Obsidian's
native **Capture to Daily Note**, configured to append to a fictional test vault.

```markdown
#### 오늘의 인풋
- 09:32 | Media | https://youtu.be/TEST0000001
```

The capture adds only `HH:mm`, not a date. Put the input heading in the **final
section** of the daily template and existing note. Observed captures appeared
under that heading; placement with other template layouts remains untested.
There is no heading search, deduplication, title lookup,
regex, or custom URI in the default Shortcut. Repeated shares may create duplicates.

## November 12 iPhone observations

These results were reported by the user, not independently reproduced by the
repository tools. No actual URLs, book text, images, or private notes were collected.

- **Confirmed success:** YouTube URL appended with an `HH:mm` timestamp; Threads,
  Facebook, and Apple Podcasts episode URLs also appended successfully.
- **Confirmed placement:** All observed entries appeared under `오늘의 인풋` in
  the test Daily Note, without repeating the date.
- **Confirmed limitations:** Sharing a book-page image captured only its filename,
  not its contents. Separately OCR-extracted text appended successfully, but long
  text made the Daily Note difficult to scan. The Shortcut does not perform OCR.
- **Still untested:** First-day note creation and template application, duplicate
  shares, offline use, and cross-device synchronization. Other layout, permission,
  and clock edge cases are listed in the [test record](docs/IOS_TEST_PLAN.md).

For now, prefer URLs or short text for a scannable journal. Image capture and a
long-text storage workflow remain future work; no automatic extraction or
summarization is implemented.

## Start here

Follow the [five-action iPhone guide](shortcuts/README.md), using only the
fictional `LKE Capture Test` vault. Record results in the
[manual test plan](docs/IOS_TEST_PLAN.md). Missing-note creation, template
application, permission edge cases, offline behavior, and sync remain pending.

The earlier [advanced design](shortcuts/experimental/README.md) is retained as an
optional experiment. Its features are not part of the beginner setup. A later
processing engine may handle cleanup and deduplication; none is currently wired in.

## Automated validation

Python 3.10+; standard library only. Run from the repository root:

```sh
python3 -m unittest discover -s tests -v
```

`src/lke/native_capture.py` models the default Text action with synthetic strings.
It does not run Shortcuts or write notes. Other helpers and tests retain advanced
formatting, URL validation, deduplication, insertion, and URI experiments.
Passing these tests **does not establish working iPhone capture**.

## Development and privacy

See [Product specification](docs/PRODUCT_SPEC.md), [Architecture](docs/ARCHITECTURE.md),
[Development handoff](docs/CODEX_NEXT_TASK.md), and [Security](docs/SECURITY.md).
All fixtures are fictional. No private vault, workplace data, patient records,
credentials, server, or separate mobile app is required.
