# Product specification — native Media Capture v0.1

## Objective

Minimize setup and capture effort: share a URL or text, prefix local `HH:mm`,
and append through Obsidian's documented Capture to Daily Note action.

```text
- 09:32 | Media | https://youtu.be/TEST0000001
```

## Default contract

- Five actions: Date → Format Date → Get Text from Input → Text → Capture to
  Daily Note. Share Sheet input is configured for URLs and Text.
- Use a fictional test vault and select Append. Capture adds no date to the body.
- Keep shared content as supplied. `Media` is a fixed label, not source inference.
  No separate title is required and no web metadata is requested.
- Place `#### 오늘의 인풋` last in the template and existing Daily Note. This is
  a setup requirement, not automatic heading routing. Verify native append
  placement and preservation of earlier content on-device.
- No Shortcut-side validation, deduplication, regex, custom URI, or retry logic.
  Duplicate captures are expected. Multiline text remains multiline.
- Do not promise automatic first-day creation or template application before a
  device test. Manually opening today's test note is an explicit workaround.

## Acceptance

The default must be buildable from the short guide, accept synthetic shared
content, append without damaging existing text, and display local time without
adding a date. User-reported November 12 tests confirm basic URL/text capture
and observed heading placement without repeated dates. Image contents were not captured and
long OCR text reduced scanability. Remaining cases are tracked in
[IOS_TEST_PLAN.md](IOS_TEST_PLAN.md).
Missing-note creation must be characterized, even if a manual-open workaround is
needed. No automated Python test can certify native app behavior.

## Deferred and experimental

Cleanup, deduplication, title enrichment, and source classification may be handled
by a later processing engine. No such engine runs today. The previous
[advanced Shortcut design](../shortcuts/experimental/README.md) and Python helpers
remain optional experiments, not default requirements or mobile guarantees.
