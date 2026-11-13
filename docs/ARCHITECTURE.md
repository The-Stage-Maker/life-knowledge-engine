# Architecture — native Media Capture v0.1

## Default path (basic capture reported; edge cases pending)

```text
Share Sheet (URLs/Text)
  → Date (current local time)
  → Format Date (HH:mm)
  → Get Text from Input (Shortcut Input)
  → Text (- time | Media | shared content + newline)
  → Obsidian Capture to Daily Note (Append, selected test vault)
```

No Python runs on the phone. No URI construction, regex, metadata requests,
duplicate check, note read, or pre-open action belongs to this default path.
The input heading must already be the last section. The native action's actual
placement under the heading was observed in the November 12 test note. Other
layouts, spacing edge cases, and missing-note behavior remain untested.
The Daily notes plugin owns note naming and template settings; the Shortcut does
not recreate those settings or add a date to the body.

## Automated reference code

`src/lke/native_capture.py` provides `format_native_capture`: a pure text model
of the default Text action. It preserves raw shared text and adds the time prefix
and trailing newline. Explicit datetimes retain their timezone; the default
clock is local. It neither converts iOS share objects nor stores anything.

`tests/test_native_capture.py` tests synthetic text formatting, local clock use,
raw multiline input, and repeat capture behavior. These are not native action,
append-preservation, or end-to-end tests.

## Optional experimental layer

The retained `capture_format.py` and `daily_note.py` helpers implement validation,
source inference, video identity, URI formatting, and in-memory insertion with
literal templates. They do not access files or run after the native capture.
Their tests validate those separate algorithms only.

The earlier complex Shortcut recipe, patterns, and manual test record live in
`shortcuts/experimental/`. The regex tests target that directory, using Python's
regex engine, not Apple's. This material is not a prerequisite for basic capture.

## Limits

Repeated shares append repeated entries. No queue, retries, dedupe cache, or
processing service exists. Text may contain Markdown or newlines. There is no
URL validation, midnight guard, or guaranteed background success. Native action
errors, first-day creation, template application, and sync must be observed in a
fictional test vault. Inspect before retrying to avoid unintended duplicates.
