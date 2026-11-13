"""In-memory reference implementation. Never reads or writes an Obsidian vault."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import re

from .capture_format import HEADING, format_capture, url_key


@dataclass(frozen=True)
class CaptureResult:
    content: str
    added: bool
    entry: str


def _visible_lines(text: str):
    """Yield offsets outside initial YAML frontmatter and fenced code blocks.

    Deliberately a small Markdown subset, not a general Markdown parser.
    """
    offset = 0
    frontmatter = text.startswith(('---\n', '---\r\n'))
    fence = None
    for index, line in enumerate(text.splitlines(keepends=True)):
        stripped = line.rstrip('\r\n')
        if frontmatter:
            if index and stripped in {'---', '...'}:
                frontmatter = False
        elif fence:
            if re.fullmatch(r' {0,3}' + re.escape(fence[0]) + '{' + str(len(fence)) + r',}\s*', stripped):
                fence = None
        else:
            match = re.match(r' {0,3}(`{3,}|~{3,})', stripped)
            if match:
                fence = match[1]
            else:
                yield offset, line
        offset += len(line)
    if frontmatter or fence:
        raise ValueError("Unclosed frontmatter or code fence; repair note before capture")


def append_capture(note: str | None, *, url: str, title: str | None = None,
                   captured_at: datetime | None = None, template: str = "") -> CaptureResult:
    """Insert once per video per supplied day; return all existing text intact.

    None means a missing note; an existing empty note never reapplies a template.
    Templates are literal text: no Templater code or date placeholders executed.
    Dedupe covers capture rows only, including legacy Markdown-link rows.
    Ambiguous duplicate headings fail without changing text.
    """
    entry = format_capture(url=url, title=title, captured_at=captured_at)
    key = url_key(url)
    content = template if note is None else note
    lines = list(_visible_lines(content))
    for _, line in lines:
        if not re.match(r'^- \d{2}:\d{2} \| [^|]+ \| ', line):
            continue
        # New format ends in a raw URL; legacy format ends in [title](URL).
        candidate = line.rstrip().rsplit(' | ', 1)[-1]
        if not candidate.startswith(('http://', 'https://')):
            match = re.search(r'\]\((https?://.*)\)$', candidate)
            candidate = match[1] if match else ''
        try:
            if url_key(candidate) == key:
                return CaptureResult(content, False, entry)
        except ValueError:
            continue

    headings = []
    for offset, line in lines:
        match = re.match(r'^ {0,3}(#{1,6})[ \t]+(.+?)\s*$', line)
        if match:
            label = re.sub(r'\s+#+$', '', match[2]).strip()
            headings.append((offset, len(match[1]), label))
    targets = [h for h in headings if h[1:] == (4, HEADING)]
    if len(targets) > 1:
        raise ValueError("Multiple input headings; choose one before capture")
    newline = '\r\n' if '\r\n' in content else '\n'
    if targets:
        start, level, _ = targets[0]
        end = next((pos for pos, depth, _ in headings if pos > start and depth <= level), len(content))
        prefix, suffix = content[:end], content[end:]
        separator = '' if prefix.endswith(('\n', '\r')) else newline
        content = prefix + separator + entry + newline + (newline if suffix else '') + suffix
    else:
        separator = '' if not content or content.endswith(newline * 2) else (newline if content.endswith(newline) else newline * 2)
        content += separator + '#### ' + HEADING + newline + entry + newline
    return CaptureResult(content, True, entry)
