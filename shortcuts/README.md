# iPhone capture setup (prototype; device testing pending)

## Goal

From YouTube on iPhone: tap **Share**, run the custom shortcut, and add a line with capture time and the original video URL to the current daily note, under `#### 오늘의 인풋`.

## Before testing

1. Confirm Obsidian and iOS are current, and the existing vault is synced.
2. Add `#### 오늘의 인풋` as the **last section** of the Daily Journal template. In an already-created day's note, add it manually once for the initial test. Later automation must solve the first-capture-of-the-day case.
3. Back up your vault before introducing a new automation.

## Supported paths to evaluate

- **Native Obsidian Share Sheet:** select Obsidian → a configured Location with Daily note + Append. This is the simplest proof-of-concept for reliably saving URLs. It does not by itself guarantee a consistently formatted capture timestamp and page title.
- **Apple Shortcuts:** configure the Shortcut to accept shared URLs, format the current local time as `HH:mm`, build a Markdown entry, and send it to Obsidian's `Capture to Daily Note` action. The user chooses a destination vault. Check whether the action supports targeting the input heading; if not, use a correctly encoded `obsidian://daily` URL with `append=true` and `heading=오늘의 인풋`.
- **Fallback:** When title extraction fails, use the label `YouTube video` while preserving the URL. Avoid brittle web scraping or third-party credentials for v0.1.

## Critical edge case

Historically, some background capture flows have failed when the day's Daily Note did **not yet exist**. Test this case explicitly. If necessary, add an automatic safe step to create/open the Daily Note before the append; do not overwrite any existing note.

## Test results

- [ ] iPhone Share Sheet entry can launch shortcut
- [ ] Current local `HH:mm` appears
- [ ] URL is preserved even if title extraction fails
- [ ] Entry appears under `오늘의 인풋`
- [ ] No duplicate visible date
- [ ] First input of a new day works
- [ ] Mac and iPad eventually sync the new entry
- [ ] No existing content gets overwritten

Nothing in this directory is an installable `.shortcut` file yet. Configuration and real-device verification are required.
