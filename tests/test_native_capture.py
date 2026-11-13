"""Default capture text contract only; no native action or device is executed."""
import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from lke.native_capture import format_native_capture


class NativeCaptureTests(unittest.TestCase):
    def test_local_time_without_date(self):
        stamp = datetime(2026, 11, 11, 9, 32, tzinfo=timezone(timedelta(hours=-7)))
        self.assertEqual(format_native_capture('https://youtu.be/TEST0000001', captured_at=stamp),
                         '- 09:32 | Media | https://youtu.be/TEST0000001\n')

    def test_default_uses_local_clock(self):
        with patch('lke.native_capture.datetime') as clock:
            clock.now.return_value.astimezone.return_value = datetime(2026, 11, 11, 0, 5)
            self.assertTrue(format_native_capture('Synthetic text').startswith('- 00:05 |'))
            clock.now.return_value.astimezone.assert_called_once_with()

    def test_raw_text_is_not_enriched_or_normalized(self):
        for content in ('', 'not a URL', '한국어 | [example]\nsecond line',
                        'https://youtu.be/TEST0000001?si=synthetic'):
            with self.subTest(content=content):
                result = format_native_capture(content, captured_at=datetime(2026, 11, 11, 9, 32))
                self.assertEqual(result.removeprefix('- 09:32 | Media | '), content + '\n')

    def test_repeated_capture_is_not_suppressed(self):
        first = format_native_capture('Synthetic input', captured_at=datetime(2026, 11, 11, 9, 32))
        second = format_native_capture('Synthetic input', captured_at=datetime(2026, 11, 11, 9, 33))
        self.assertIn('Synthetic input', first)
        self.assertIn('Synthetic input', second)


if __name__ == '__main__':
    unittest.main()
