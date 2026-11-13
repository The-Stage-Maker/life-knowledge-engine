# Optional experimental capture design

This is the retained advanced recipe, not the default v0.1 setup. Start with
[the five-action native Shortcut](../README.md). Regex, deduplication, and URI
routing below are optional experiments, not requirements for basic capture.

Status: code tested with synthetic strings; **not installed or tested on an iPhone**.
No installable `.shortcut` is included. Python is a reference implementation, not
an iPhone runtime. Use only a new, empty test vault for this procedure.

## What is actually supported

Research checked 2026-11-11:

- Obsidian lists **Open Daily Note**, **Get Daily Note**, and **Capture to Daily Note**.
  The documentation does not describe every action parameter or error result.
- Its native `daily` URI documents `append`, `heading`, and `content`. We use this
  for section targeting; do not assume Capture to Daily Note has a heading field.
- Native Share Sheet Locations support daily-note append, but the documented
  web-content template setup uses **New Note**. It is not evidence of a complete
  timestamped, deduplicated daily-note workflow.

Sources: [Obsidian iOS](https://help.obsidian.md/ios),
[URI](https://help.obsidian.md/Extending+Obsidian/Obsidian+URI).
Apple documents [Share Sheet setup](https://support.apple.com/guide/shortcuts/apd163eb9f95/ios),
[input types](https://support.apple.com/guide/shortcuts/input-types-apd7644168e1/ios),
[custom date formats](https://support.apple.com/guide/shortcuts/custom-date-formats-apd8d9b19184/ios),
and [Match Text](https://support.apple.com/121131).

**Device gate:** In Shortcuts, search Apps → Obsidian for Open Daily Note and Get
Daily Note. If either is missing, update the apps and open Obsidian once. If still
missing, stop: this recipe cannot safely check duplicates. Do not substitute an
unverified action. Action labels can be localized. Record app and iOS versions
in the [manual test record](IOS_TEST_PLAN.md).

## 1. Prepare a fictional test vault

These are instructions for you to perform manually; the repository tools never
open a vault. Do not use personal, workplace, or patient notes.

1. In Obsidian create a new vault called `LKE Capture Test`.
2. Enable Settings → Core plugins → Daily notes.
3. In Daily notes settings set Date format to `YYYY-MM-DD`, New file location to
   `Daily`, and Template file location to a note called `Templates/Daily`.
4. Create that template with the fictional contents below. Keep any custom
   template sections you want to test; the input heading need not be last.

   ```markdown
   # {{date}}

   #### 오늘의 인풋

   #### Reflection
   Synthetic text that must stay unchanged.
   ```

5. Leave today's note absent for the first test. Daily notes is documented to
   [create notes from its configured template](https://help.obsidian.md/plugins/daily-notes).
   Community template scripts are outside this test.

## 2. Create the Shortcut

Open Apple Shortcuts → **+** → name it `LKE Capture`. Open Details and enable
**Show in Share Sheet**. Set accepted types to **URLs** and **Text**. Do not accept
files or images. For no input choose **Stop and Respond** if that setting appears;
the URL count check below is still required.

To add an action, search its bold name in the action search box. A name in
backticks such as `SharedURL` below is a variable you create, not an action.
Use **Set Variable** after an output to give it that name. When a later step
requests it, tap the input field → Select Variable → choose that variable.
Do not type a variable name as ordinary text. If inserts automatically use the
previous action's output, replace that token with the specified variable.

### Input and timestamp

1. Add **Date**, set to **Current Date**, and save as `CapturedAt`. This must be
   first, before opening Obsidian.
2. **Format Date** on `CapturedAt`: Date Format → Custom → `HH:mm`. Save as `Time`.
   Use the device's local timezone; do not select UTC.
3. **Format Date** on `CapturedAt`, Custom `yyyy-MM-dd`. Save as `CaptureDay`.
   This is a guard variable only; it is not included in the entry.
4. **Get URLs from Input**, explicitly using `Shortcut Input`. Save as `URLs`.
5. **Count** items in `URLs`. Add **If** count is not `1`: **Show Alert** with
   `Share exactly one YouTube video URL; nothing saved`, then **Stop This Shortcut**.
   Place subsequent actions after **End If**.
6. **Get Item from List**, First Item of `URLs`. Save as `SharedURL`.
7. **Match Text** on `SharedURL` using the `video_url` pattern below. If Matches
   has no value, Show Alert `Unsupported video URL; nothing saved` and Stop This
   Shortcut. Then **Get Group from Matched Text**, group `1`, on those Matches;
   save as `VideoID`.

Copy the following pattern as one line, exactly (no surrounding backticks):

```regex
^https?://(?:youtu\.be/|(?:(?:www|m|music)\.)?youtube\.com/(?:watch\?v=|shorts/|live/|embed/))([A-Za-z0-9_-]{11})(?:[?&#][^\s<>"\\|]*)?$
```

This deliberately accepts normal YouTube share links and shorts/live/embed links.
It rejects playlists, redirect links, and watch links where `v` is not the first
query parameter. It never expands a link online. The Python helper accepts a
wider set of query orders. Synthetic IDs are syntax fixtures, not playable videos.

### Title and entry

8. **Get Text from Input** on `Shortcut Input`. **Replace Text**: replace
   `SharedURL` with empty text, Regular Expression **off**. Save output as `Title`.
   This uses any accompanying shared text as a title; it does not invent metadata.
9. **Replace Text** on `Title`, Regular Expression **on**, find `\s+`, replace
   with one space. Then Replace Text, regex on, find `^\s+|\s+$`, replace with
   empty text. Set `Title` to this output.
10. **If** `Title` has no value: **Text** `YouTube video` → Set Variable `Title`.
    End If. YouTube may share only a URL: this fallback is normal. No title prompt
    or web request is required. Safari page-title extraction is not assumed for
    a YouTube app share.
11. **Replace Text**, regex **off**, replace `|` with `\|` in `Title`; set `Title`
    to the result. Titles containing other Markdown syntax may render as Markdown
    on iOS; Python additionally escapes it. Newlines have already been removed.
12. Add **Text**, inserting the three variable tokens in this exact layout:

    ```text
    - [Time] | YouTube | [Title] | [SharedURL]
    ```

    Square brackets above only identify tokens: do not type the brackets. Save
    as `Entry`. A date must not appear in this text.

### Create/read, deduplicate, append

13. Add Obsidian **Open Daily Note** and select `LKE Capture Test`. This is the
    deliberate foreground step for the missing-note case; no guessed sleep or
    background creation workaround is used.
14. Add Obsidian **Get Daily Note**, same vault, today's date if a date field is
    offered. Save its text as `DailyText`. Exact field labels and return type
    must be checked on device. If opening the app prevents continuation, return
    to Shortcuts and record that as a failure; do not claim one-tap capture works.
    If reading fails, stop rather than appending blindly.
15. **Match Text** on `DailyText` with the following pattern. Replace the literal
    `VIDEO_ID` inside the pattern with the `VideoID` variable token:

    ```regex
    (?m)^- [0-9]{2}:[0-9]{2} \| YouTube \| [^\r\n]*https?://(?:youtu\.be/|(?:(?:www|m|music)\.)?youtube\.com/(?:watch\?v=|shorts/|live/|embed/))VIDEO_ID(?=[?&#)\s]|$)
    ```

    If Matches has any value: Show Alert `Already captured today`, then Stop This
    Shortcut. This detects generated rows and legacy link rows, including common
    URL variants. It does not update an old title or delete annotations.
16. **Match Text** on `DailyText` using `(?m)^#### 오늘의 인풋[ \t]*\r?$`.
    **Count** Matches. If count is greater than `1`, Show Alert `Duplicate input
    headings; fix the test note first`, then Stop This Shortcut.
17. **If** heading count is `0`: add **Text** with two initial newlines followed by
    `#### 오늘의 인풋`, a newline, and the `Entry` token. Save as `Payload`.
    Add an empty **Text** → Set Variable `HeadingQuery`.
    **Otherwise**: Set Variable `Payload` to `Entry`. Add **Text**
    `&heading=%EC%98%A4%EB%8A%98%EC%9D%98%20%EC%9D%B8%ED%92%8B` → Set Variable
    `HeadingQuery`. End If. The literal heading query is pre-encoded Korean text.
18. **URL Encode** `Payload`, operation Encode; save as `EncodedPayload`.
    Encode the payload once, not the whole URI.
19. **Text** `LKE Capture Test` → **URL Encode**, Encode → save as `EncodedVault`.
20. **Date** Current Date → **Format Date** Custom `yyyy-MM-dd`. If it differs
    from `CaptureDay`, Show Alert `Day changed during capture; share again`, then
    Stop This Shortcut. This reduces midnight misfiling; it cannot eliminate a
    rollover between the check and Obsidian processing the URI.
21. Add **Text** with the following, inserting variable tokens at the bracketed
    positions, with no spaces or line breaks:

    ```text
    obsidian://daily?vault=[EncodedVault]&append=true&spacing=newline[HeadingQuery]&content=[EncodedPayload]
    ```

22. Add **Open URLs** using that text. Do not add `overwrite=true`. Do not add a
    `Saved` notification: dispatching a URI is not confirmation that it saved.
    Inspect the opened Daily Note during testing.

The patterns also live in [patterns.json](patterns.json) for regression tests.
Do not keep sample capture rows or matching heading lines inside code fences or
YAML in the test template: this simple Shortcut regex does not parse Markdown.
Use one exact level-four heading; renamed or decorated headings are not matched.
Python has stronger Markdown handling, but its code does not run in Shortcuts.

## 3. First end-to-end run

1. In a disposable test note in any text-sharing app, type the fictional text:
   `Synthetic video https://youtu.be/TEST0000001?si=synthetic`.
2. Select and share that text → `LKE Capture`. Allow permissions for the test
   vault if prompted. Do not open the synthetic link in a browser.
3. Check today's note: template content remains, and one entry appears under
   the input heading with the local time from when capture started.
4. Share the same text again. Expect `Already captured today` and no new row.
5. Share `https://www.youtube.com/watch?v=TEST0000001&t=12`. Expect the same
   duplicate result. Share `https://youtu.be/TEST0000002` to get a second row
   with the fallback title.
6. Complete [all device cases](IOS_TEST_PLAN.md), including absent notes,
   custom sections, offline capture, and sync. An actual YouTube app share is
   a separate pending manual transport test; synthetic tests cannot establish
   its payload shape or permissions.

## Reliability limits and recovery

- No server, mobile app, community plugin, credentials, clipboard cache, or
  background Mac process is needed. The Shortcut opens Obsidian on each capture.
- Sequential same-device duplicates are checked against the actual note. Two
  simultaneous captures or unsynced devices can still both append. Wait for sync
  before another device captures. This is not an atomic database operation.
- No automatic retry is installed. If an action errors, keep the original share,
  inspect today's test note, and rerun; do not manually append a second copy.
- Offline operation avoids title requests but still depends on locally available
  vault files and Obsidian action behavior. Permissions and sync can interrupt it.
- If first-day creation or Get Daily Note fails, manually open today's test note
  in Obsidian and rerun. Record this as a workaround, not acceptance of automatic
  first-capture creation. Do not remove the dedupe check to hide a failure.
- Daily URI chooses the day when Obsidian handles it. A delayed midnight capture
  may need manual correction in the test vault. No exactly-once guarantee.
- Device setup remains pending. These instructions are a concrete test recipe,
  not a claim that an iOS Shortcut was built or validated by Python tests.
