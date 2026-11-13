# Optional experimental design — manual test record

These cases apply only to the advanced recipe, not the default native capture.

**All cases pending. No iPhone or private vault was accessed during implementation.**

Use the [setup guide](README.md) first. Create only fictional test
content. Do not copy personal templates or notes into the repository. Device
execution is a separate user-run step, not authorization for an agent to inspect
a vault. Record version numbers and pass/fail descriptions, not personal screenshots.

- Test date: pending
- iOS version: pending
- Obsidian version: pending
- Shortcut revision: manual recipe v0.1
- Test vault: `LKE Capture Test` (fictional)
- Sync method for disposable test vault: pending

| Case | Procedure and expected result | Result |
| --- | --- | --- |
| Action catalog | Find Open Daily Note and Get Daily Note; note available parameters and text output type. | Pending |
| First capture | Today's note absent; share synthetic URL. Daily note created once from test template, one input row, reflection unchanged. | Pending |
| Existing note | Add fictional text above and below input section; share a different video. Only a row and spacing added inside section. | Pending |
| Missing heading | Remove input heading from test note; share another ID. One new level-four section appears at end. | Pending |
| Custom template | Add properties and several sections; put input section in middle. Next missing-note run preserves all template content and expands native date. | Pending |
| Duplicate | Repeat same URL later. Alert appears and entire note remains unchanged. | Pending |
| URL variant | Share same ID as youtu.be and watch?v= with differing tracking/time parameters. Still one row. | Pending |
| Next day | Repeat a video on a different local calendar day. New day's note gets one row. Do not change the device clock just to simulate. | Pending |
| No title | Share raw synthetic URL. Title is YouTube video; URL unchanged. | Pending |
| Shared title | Share fictional title plus URL; title appears on one line. Test Korean, pipes, and newlines. | Pending |
| Bad input | Share text without URL, two URLs, non-YouTube URL, playlist, malformed ID. Alert; no note append. | Pending |
| Duplicate headings | Two exact input headings in test note. Alert; no append. | Pending |
| Clock | Capture time matches local HH:mm at launch; no per-entry date. Test 00:xx and 12/24-hour device settings. | Pending |
| Midnight | Initiate near midnight. If guard triggers, no append; rerun next day. Record any late URI routing. | Pending |
| Offline | Preload test vault, enable airplane mode, share synthetic text. No metadata request; verify local append or visible failure. | Pending |
| Permissions/error | Deny test-vault permission or make test vault unavailable. Shortcut must stop; no false Saved message. Restore access and inspect before retry. | Pending |
| App transition | Run from Share Sheet with Obsidian closed/open. Verify sequence resumes after Open Daily Note and reads newly created note. | Pending |
| Sync | With permission, sync only disposable fictional vault to another device. Verify row and template survive; record sync delay. | Pending |
| YouTube transport | With separate approval to use a public video, share from YouTube app; record whether URL and title arrive, using no account history or personal data. | Pending |
| Concurrency limit | Two simultaneous captures may duplicate; confirm no claim of atomic delivery. Run ordinary acceptance sequentially. | Pending |

For each failure record case name, app versions, observed behavior, and workaround
without personal data. Keep first-capture and app-transition failures as release
blockers. Manual open-and-retry is useful recovery, not a passed automatic test.

Automated test results are tracked in the development handoff/final work report;
they validate string transformations only and cannot replace this table.
