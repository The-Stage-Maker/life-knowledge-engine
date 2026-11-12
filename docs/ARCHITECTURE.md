# Architecture (proposed)

```text
iPhone/iPad -- Apple Shortcuts / Obsidian Share Sheet --> Obsidian Daily Note
                                                  |
                                                  v
                                   Private iCloud-synced Vault
                                                  |
                                                  v
                          Optional Mac-side local processing (later)
                            dedupe, metadata, safe AI enrichment
                                                  |
                                                  v
                               Evening and weekly reflection tools

Public GitHub repository: only code, docs, and fictional examples.
```

## Separation of concerns

- **Private vault:** Actual personal content; must be outside the Git repository.
- **Public repository:** Software, tests, documentation, and synthetic examples.
- **Workplace:** Microsoft 365 tenant remains separate. No PHI or confidential internal data is moved to a personal vault, third-party API, or public repository without organizational authorization.
- **Mobile input:** The first prototype uses iOS-supported native actions, reducing server costs and maintenance.
- **Future Mac processing:** Reads only explicitly designated local vault locations, operates on copies for testing, writes idempotently, logs minimal non-sensitive diagnostics, and includes rollback/backups.

## Design decisions

1. **Daily Note is the log; not every capture becomes a new file.** Long sources may be stored separately later.
2. **No duplicate dates in the rendered journal.** File names encode date; entries show local time.
3. **Source provenance over generated summaries.** Preserve URLs and explicit user quotations; distinguish them from AI-generated metadata.
4. **Human-authored reflection.** AI may suggest connections but cannot overwrite or impersonate personal views.
5. **Graceful failures.** If capture enrichment breaks, save raw URL first and surface failure. Never lose the input.
