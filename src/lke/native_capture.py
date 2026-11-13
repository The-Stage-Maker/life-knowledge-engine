"""Pure text reference for the default native Shortcut; no iOS or vault access."""
from datetime import datetime


def format_native_capture(shared_content: str, *, captured_at: datetime | None = None) -> str:
    """Prefix supplied text with local time, without parsing or deduplicating it.

    Mirrors the Text action's trailing newline. Does not emulate iOS input
    conversion, Obsidian append spacing, storage, or missing-note creation.
    """
    now = captured_at if captured_at is not None else datetime.now().astimezone()
    return f"- {now:%H:%M} | Media | {shared_content}\n"
