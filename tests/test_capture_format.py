import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from lke.capture_format import format_capture, make_daily_uri


class CaptureFormattingTests(unittest.TestCase):
    def test_time_and_link_without_repeating_date(self):
        item = format_capture(
            title="Sample talk", url="https://example.com/video",
            medium="YouTube", captured_at=datetime(2026, 11, 11, 9, 32),
        )
        self.assertEqual(item, "- 09:32 | YouTube | [Sample talk](https://example.com/video)")
        self.assertNotIn("2026-11-11", item)

    def test_title_fallback_and_bad_url(self):
        result = format_capture(title="", url="https://example.com/video", medium="YouTube", captured_at=datetime.now(timezone.utc))
        self.assertIn("[YouTube item]", result)
        with self.assertRaises(ValueError):
            format_capture(title="X", url="file:///private/diary", medium="YouTube", captured_at=datetime.now())

    def test_uri_encoding_and_heading(self):
        uri = make_daily_uri(vault="My Life Knowledge Base", entry="- 09:32 | YouTube | [Sample](https://example.com)")
        qs = parse_qs(urlparse(uri).query)
        self.assertEqual(qs["vault"], ["My Life Knowledge Base"])
        self.assertEqual(qs["append"], ["true"])
        self.assertEqual(qs["heading"], ["오늘의 인풋"])
        self.assertIn("09:32", qs["content"][0])


if __name__ == "__main__":
    unittest.main()
