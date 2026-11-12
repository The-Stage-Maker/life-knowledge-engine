# Security & Publication Rules

## Public vs. private

The Git repository is **not** the Obsidian vault. Never copy the personal vault into the repository, even temporarily. Do not commit journal entries, private conversations, export ZIPs, real photos, workplace files, patient identifiers, credentials, tokens, or confidential system details.

## Before each commit / publication

- Review every filename and GitHub Desktop's **Changes** diff.
- Confirm examples are invented, not anonymized extracts of actual private/work records.
- Ensure any `.env`, credentials, key files, tokens, backups, and exported conversations are not tracked. Check the existing Python `.gitignore`; extend as needed rather than replacing it without review.
- Test against synthetic files in a temporary directory, not the real vault.
- Do not log the contents of private notes into console logs, CI artifacts, or analytics.
- Avoid pushing any real personal file even into a private Git repository; a later change to public could expose Git history.

## Local automation safeguards

- Read-only discovery first; write only after a backup and the user's explicit choice.
- Limit write scopes to approved note sections; never overwrite a complete file to add one media item.
- Keep API keys locally in secure storage or ignored environment settings, never embedded in the Shortcuts share link or a repo.
- Configure AI processing as opt-in and account for separate API costs.
- Company data cannot be copied to personal services just because a browser can access them.

## Incident response

If a sensitive file is accidentally committed, **do not simply delete the file and assume it is gone**. Stop publication and review Git history, revoke any exposed credentials, and follow appropriate provider/security procedures.
