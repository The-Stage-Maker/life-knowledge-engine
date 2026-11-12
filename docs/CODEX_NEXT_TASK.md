# Next Codex task — iPhone share-to-Daily-Note prototype

Open the **local** `life-knowledge-engine` repository. Do **not** access the real Obsidian vault. The current repo has an existing Python `.gitignore`; preserve and inspect it.

Implement a small, testable first milestone:

1. Read README.md, docs/PRODUCT_SPEC.md, docs/ARCHITECTURE.md, docs/SECURITY.md, and shortcuts/README.md.
2. Review the Python `src/lke/capture_format.py` and tests; improve clarity or test coverage if needed.
3. Produce a precise, minimal setup walkthrough for a real iPhone Apple Shortcut that accepts URLs from the iOS Share Sheet and captures to an Obsidian Daily Note; avoid external apps or services if possible.
4. Prefer Obsidian's native **Capture to Daily Note** Shortcut action or a properly URL-encoded `obsidian://daily` action with append and heading, as documented. Do not claim that Apple Shortcut actions can be installed purely by committing code.
5. Verify the challenge of capturing when today's note does not yet exist. The prototype must explicitly test this. Do not say it works until tested on an actual iPhone.
6. The first milestone must save `- HH:mm | YouTube | [Title](URL)` below `#### 오늘의 인풋` without duplicating the date or overwriting other note content. If automatic title retrieval is not supported, store a safe fallback label and original URL.
7. Add an honest test checklist including success, duplicate share, malformed URL, offline behavior, and cross-device sync.
8. Use only fictional/sample data. Do not commit or attempt to inspect personal notes, company files, or API keys.
9. Report exactly what was implemented versus what still requires device setup/testing, and prepare a concise, portfolio-ready commit message.

Official references:
- https://obsidian.md/help/ios
- https://obsidian.md/help/uri
