# iPhone Media Capture v0.1 — five-action setup

**Basic capture was reported successful on November 12, 2026; edge cases remain
untested.** See the [actual test record](../docs/IOS_TEST_PLAN.md). This guide is
not an installable Shortcut export. Use only a fictional vault named `LKE Capture Test`.

[Obsidian documents **Capture to Daily Note**](https://help.obsidian.md/ios) as
appending or prepending text without opening the app. Its help does not specify
all action fields, missing-note behavior, or heading targeting. The setup below
uses append only; confirm the available fields on your phone.

## Prepare the test note once

1. In Obsidian, create `LKE Capture Test`. Enable **Settings → Core plugins →
   Daily notes**. Use `YYYY-MM-DD` for the filename date format.
2. Create a fictional Daily notes template and select it in **Daily notes →
   Template file location**. Put any other sections **before** the input heading:

   ```markdown
   #### Reflection
   Synthetic text to preserve.

   #### 오늘의 인풋
   ```

3. Open today's Daily Note in this test vault before the first test. Ensure
   `#### 오늘의 인풋` is its **final section** too. Existing notes do not inherit
   later template edits. Do not add a date to the capture text.

The final-section rule assumes the action appends at the end of the note. Test
that placement on-device; this recipe does not search for or create the heading.

## Build the Shortcut

In Apple Shortcuts, tap **+**, name it `LKE Capture`, open **Details**, and turn on
**Show in Share Sheet**. Set accepted input types to **URLs** and **Text**.
Receiving Share Sheet input is configuration, not an extra action.

Add these **five actions**, in this order:

| Action | Set it to |
| --- | --- |
| 1. **Date** | **Current Date**. |
| 2. **Format Date** | Input: the Date action's output. Date Format: **Custom**. Format String: `HH:mm`. Keep the device-local timezone. |
| 3. **Get Text from Input** | Input: **Shortcut Input**, not the formatted date. |
| 4. **Text** | Build the text below using the output tokens from actions 2 and 3. Press Return once after the shared-content token so the entry ends with a newline. |
| 5. **Capture to Daily Note** (Obsidian) | Text: action 4's output. Vault: `LKE Capture Test`. Choose **Append**, not Prepend. Expand the action's options if needed. |

For action 4, type `- `, insert the **Formatted Date** variable, type ` | Media | `,
then insert the text output from action 3. Tap an input field and choose
**Select Variable** to pick an earlier action's output. Do not type the token
names or square brackets literally. The resulting text should look like:

```text
- 09:32 | Media | https://youtu.be/TEST0000001
```

If **Capture to Daily Note** is missing, update/open Obsidian and check again.
If the action does not expose the text, destination vault, or append controls
needed here, stop and record the mismatch. Do not guess fields or substitute a
custom URI. Exact localized field labels and permissions are pending verification.

## Try it with fictional content

1. In a disposable text note, select `https://youtu.be/TEST0000001`, tap **Share**,
   and choose **LKE Capture**. This synthetic URL is not a playable video.
2. Open today's note in `LKE Capture Test`. Check for one row with the local
   `HH:mm`, `Media`, and the shared URL, below the final input heading. Check that
   the reflection text is unchanged and that the row starts on a new line.
3. Share again: **a second entry is expected**. There is no duplicate check.
4. Complete the short [device test record](../docs/IOS_TEST_PLAN.md), especially
   missing-note creation and end-of-note placement. Basic URL/text capture is
   reported successful; the listed edge cases remain untested.

## What this version does not do

No regex, URL validation, deduplication, title lookup, heading routing, custom URI,
or processing engine runs in this Shortcut. Shared text is kept as supplied;
multiline text or Markdown may span lines or affect rendering. Share one item at
a time. No-input behavior is unverified; launch through Share, not the editor.

Missing daily notes and template application are unverified. If capture fails,
open today's test note manually and retry only after checking whether it already
saved—retries can duplicate entries. Offline capture, sync, and midnight routing
also need device tests. Do not infer successful storage from a completed animation.

The [optional advanced design](experimental/README.md) preserves the earlier
regex/URI workflow separately. It is not needed for this beginner setup.

References: Apple [Share Sheet setup](https://support.apple.com/guide/shortcuts/apd163eb9f95/ios),
[input types](https://support.apple.com/guide/shortcuts/input-types-apd7644168e1/ios),
[custom time formatting](https://support.apple.com/guide/shortcuts/custom-date-formats-apd8d9b19184/ios),
Obsidian [Daily notes templates](https://help.obsidian.md/plugins/daily-notes).
These sources were reviewed on 2026-11-11; documentation support is not a device test.
