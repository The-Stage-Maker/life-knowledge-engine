"""Pure helpers for a synthetic, source-linked Daily Note media entry.

These functions do not access a vault or perform network requests. A future iOS
Shortcut should use the same visible format; this is not a working iOS Shortcut.
"""

from __future__ import annotations

from datetime import datetime
from urllib.parse import urlencode, urlparse


def _safe_text(text: str) -> str:
    """Escape Markdown-link syntax and keep one line per capture."""
    return (
        text.replace("\\", "\\\\")
        .replace("[", "\\[")
        .replace("]", "\\]")
        .replace("|", "\\|")
        .replace("\r", " ")
        .replace("\n", " ")
        .strip()
    )


def format_capture(*, title: str, url: str, medium: str, captured_at: datetime) -> str:
    """Format a human-readable capture; preserve local capture time and URL."""
    parsed = urlparse(url.strip())
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("URL must be an HTTP(S) URL")
    if not title.strip():
        title = f"{medium} item"
    # Encode literal parentheses in link destinations to protect Markdown.
    safe_url = url.strip().replace("(", "%28").replace(")", "%29")
    return f"- {captured_at.strftime('%H:%M')} | {_safe_text(medium)} | [{_safe_text(title)}]({safe_url})"


def make_daily_uri(*, vault: str, entry: str, heading: str = "오늘의 인풋") -> str:
    """Obsidian daily URI; needs real-device integration testing."""
    if not vault.strip() or not entry.strip():
        raise ValueError("vault and entry are required")
    return "obsidian://daily?" + urlencode({
        "vault": vault,
        "append": "true",
        "heading": heading,
        "content": entry,
    })
