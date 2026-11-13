"""Pure media capture helpers: no files, network, or vault access."""
from __future__ import annotations

from datetime import datetime
import re
from urllib.parse import parse_qs, quote, urlencode, urlsplit

HEADING = "오늘의 인풋"
YOUTUBE_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "music.youtube.com", "youtu.be"}


def validate_url(url: str) -> str:
    """Accept a single HTTP(S) URL, never credentials or embedded whitespace."""
    url = url.strip()
    if any(c.isspace() or ord(c) < 32 for c in url) or any(c in url for c in '<>"\\|'):
        raise ValueError("URL contains unsafe characters")
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("URL must be an HTTP(S) URL")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("URLs with credentials are not supported")
    _ = parsed.port  # Validate malformed ports too.
    return url


def source_type(url: str) -> str:
    return "YouTube" if urlsplit(validate_url(url)).hostname in YOUTUBE_HOSTS else "Web"


def url_key(url: str) -> str:
    """Identify a YouTube video across share URLs; preserve other URL identities."""
    url = validate_url(url)
    parsed = urlsplit(url)
    if parsed.hostname in YOUTUBE_HOSTS:
        parts = parsed.path.strip('/').split('/')
        video = None
        if parsed.hostname == "youtu.be" and len(parts) == 1:
            video = parts[0]
        elif parsed.path == "/watch":
            values = parse_qs(parsed.query).get("v", [])
            if len(values) == 1:
                video = values[0]
        elif len(parts) == 2 and parts[0] in {"shorts", "live", "embed"}:
            video = parts[1]
        if video and re.fullmatch(r"[A-Za-z0-9_-]{11}", video):
            return "youtube:" + video
    return url


def _safe_text(text: str) -> str:
    text = " ".join(text.split())
    return re.sub(r"([\\`*_[\]<>|])", r"\\\1", text)


def format_capture(*, url: str, title: str | None = None, medium: str | None = None,
                   captured_at: datetime | None = None) -> str:
    """Default to the current local time; explicit times retain their timezone."""
    url = validate_url(url)
    medium = (medium or source_type(url)).strip() or source_type(url)
    title = (title or "").strip() or ("YouTube video" if medium == "YouTube" else "Web link")
    now = captured_at if captured_at is not None else datetime.now().astimezone()
    return f"- {now:%H:%M} | {_safe_text(medium)} | {_safe_text(title)} | {url}"


def make_daily_uri(*, vault: str, entry: str, heading: str | None = HEADING) -> str:
    """Build a native append request, not a save acknowledgement or dedupe check.

    Pass heading=None when entry itself creates a missing heading at note end.
    """
    if not vault.strip() or not entry.strip():
        raise ValueError("vault and entry are required")
    params = {"vault": vault, "append": "true", "content": entry, "spacing": "newline"}
    if heading is not None:
        if not heading.strip() or '\n' in heading or '\r' in heading:
            raise ValueError("heading must be a nonempty single line")
        params["heading"] = heading
    return "obsidian://daily?" + urlencode(params, quote_via=quote)
