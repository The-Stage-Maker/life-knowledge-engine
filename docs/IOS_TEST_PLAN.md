# Native five-action capture — manual test record

## Evidence and scope

**Basic capture observed on November 12, 2026; edge cases remain untested.**
Results below were reported by the user. Repository tools did not access the
phone or vault, inspect original captures, or independently reproduce the tests.
No personal URLs, book excerpts, images, filenames, or private records are stored
here. Automated Python tests are separate from these manual observations.

- Test date: 2026-11-12
- iOS / Obsidian versions: not supplied
- Shortcut: native capture workflow; exact installed revision/field labels not supplied
- Destination: user's test Daily Note; actual vault identifier not recorded
- Fictional name for future setup/tests: `LKE Capture Test`

## Confirmed success

| Input / behavior | Reported observation | Status |
| --- | --- | --- |
| YouTube URL | Successfully appended to the Daily Note with an HH:mm timestamp. | Confirmed by user |
| Threads URL | Successfully appended. | Confirmed by user |
| Facebook URL | Successfully appended. | Confirmed by user |
| Apple Podcasts episode URL | Successfully appended. | Confirmed by user |
| Separately OCR-extracted book text | Extracted text successfully appended. OCR occurred before sharing, not inside this Shortcut. | Confirmed by user; usability limitation below |
| Placement and date | All observed entries appeared under 오늘의 인풋 in the test Daily Note without repeating the date. | Confirmed for observed entries |

Synthetic illustration only, not copied from an actual capture:

```text
- 09:32 | Media | https://example.com/synthetic-media
```

The observations do not establish exact input fidelity, preservation of all
pre-existing content, automatic source/title extraction, or behavior with other
template layouts. HH:mm was explicitly reported for the YouTube test; detailed
clock comparisons and timestamps for each other input were not supplied.

## Confirmed limitations

| Input | Observation | Implication |
| --- | --- | --- |
| Book-page image shared directly | Only the image filename was captured, not the image contents. | Direct image sharing is not content capture or OCR. The beginner guide remains URL/Text only; image-input configuration used in the test was not supplied. |
| Long OCR-extracted text | Appended successfully but made the Daily Note difficult to scan. | Prefer URLs or short text for now. Separate storage/linking of long content is future work, not implemented behavior. |

## Still-untested cases

Use the [beginner guide](../shortcuts/README.md) and fictional data in a disposable
test vault. Record versions and brief outcomes without copying private captures.

| Case | Next test / boundary | Status |
| --- | --- | --- |
| First-day note creation | Run when today's test note does not exist. Record creation, error, or partial save. Do not infer creation from successful appends to an existing note. | Untested |
| Template application | On first creation, check fictional properties and sections plus final input heading. | Untested |
| Duplicate shares | Share the same synthetic URL twice. Repeated entries are expected by design, but this has not been tested; no deduplication is implemented. | Untested |
| Offline use | Preload the test vault, enable airplane mode, share synthetic text, inspect local save or error. | Untested |
| Cross-device synchronization | In an authorized disposable synced vault, check entries on another device and record delay/conflicts. | Untested |
| Final-section assumption | Observed placement passed for the tested note. Explicitly compare a final input heading with a layout containing another section after it; verify actual append-at-end behavior. | Other layouts untested |
| Missing heading | Confirm no automatic heading creation; restore the required final heading manually for normal use. | Untested |
| Preservation and spacing | Compare fictional existing content before/after; verify separate rows and trailing-newline handling across repeated captures. | Untested |
| Clock and day rollover | Compare launch time to local clock, test 12-hour display and a later calendar day. No midnight guard is implemented. | Untested beyond observed HH:mm |
| Action fields / permissions | Record app versions, exact field labels, and behavior with denied permissions or Obsidian open/closed. | Not recorded / edge cases untested |
| Input edge cases | Inspect empty input, multiple items, Korean, pipes, Markdown, and multiline rendering using synthetic content. | Untested beyond reported long-text usability |

Inspect the test note before retrying a failed capture: retries may duplicate
entries. If first-day creation fails, manually opening today's note is a workaround,
not a passed automatic-creation test. Keep the five-action default simple while
characterizing native limitations.

## Automated versus manual validation

The Python suite checks synthetic text transformations and retained experimental
algorithms. It does not execute Apple Shortcuts, verify the native append action,
or replace any untested case above. See the development handoff for the latest
recorded automated run.

Advanced deduplication, URI, and regex checks belong to the separate
[experimental record](../shortcuts/experimental/IOS_TEST_PLAN.md); the reported
native tests do not validate that experimental workflow.
