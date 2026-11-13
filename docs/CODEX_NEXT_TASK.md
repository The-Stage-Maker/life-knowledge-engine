# Development handoff — simplified native capture

Branch: `feature/media-capture-v01`. No commit or push performed.

## Current default

The beginner guide uses five native actions and Share Sheet configuration:
Date → Format Date → Get Text from Input → Text → Capture to Daily Note.
The visible format is `- HH:mm | Media | shared content`. The input heading must
already be the final section of the template and today's note.

There is no Shortcut-side regex, deduplication, enrichment, or URI building.
The old design, patterns, and test record are retained in `shortcuts/experimental/`.
Advanced Python helpers remain isolated reference code; no processing engine
runs after capture. `native_capture.py` is the minimal default text reference.

## Validation

Run `python3 -m unittest discover -s tests -v` from the repository root.
The default formatting tests use synthetic strings. Advanced tests cover separate
experimental algorithms. Neither suite runs iOS, writes a vault, or proves
native note creation, template application, content preservation, or sync.

Validation rerun on 2026-11-12: **35 automated tests passed** (4 default text-reference
tests and 31 retained experimental tests); `git diff --check` passed.
User-reported November 12 basic capture results and remaining edge cases are
recorded separately in [iPhone tests](IOS_TEST_PLAN.md). Documentation reviewed on
2026-11-11 confirms Capture to Daily Note exists and supports append/prepend;
exact device fields and behavior still need inspection.

## Next task

Basic native URL capture and separately OCR-extracted text capture were reported
successful on November 12. Direct image sharing captured only a filename; long
text reduced scanability. Next, test first-day creation, duplicate shares, offline
use, and cross-device sync with fictional data. Record app versions, verify other
template layouts, and check preservation/newlines. Record failures honestly.
Do not add advanced actions merely to hide a native limitation. Keep duplicate handling and
metadata enrichment deferred unless explicitly requested.

No real vault access, outside-repository device action, publishing, or GitHub
push is authorized by these instructions. Do not fabricate an installable Shortcut.
