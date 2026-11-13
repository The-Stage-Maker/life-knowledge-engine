"""Optional experimental regex contract tests; these do not run iOS or Apple's regex engine."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = json.loads((ROOT / 'shortcuts/experimental/patterns.json').read_text())


class ShortcutPatternTests(unittest.TestCase):
    def test_accepted_urls_and_id(self):
        for url in ('https://youtu.be/TEST0000001?si=synthetic',
                    'https://www.youtube.com/watch?v=TEST0000001&t=12',
                    'https://m.youtube.com/shorts/TEST0000001',
                    'https://music.youtube.com/live/TEST0000001'):
            with self.subTest(url=url):
                match = re.fullmatch(PATTERNS['video_url'], url)
                self.assertIsNotNone(match)
                self.assertEqual(match[1], 'TEST0000001')

    def test_rejected_urls(self):
        for url in ('https://youtube.com.example.com/watch?v=TEST0000001',
                    'https://user@youtube.com/watch?v=TEST0000001',
                    'file:///example', 'https://youtube.com/playlist?list=example',
                    'https://youtu.be/short', 'https://youtu.be/TEST0000001extra',
                    'https://youtu.be/TEST0000001\ninjection',
                    'https://youtube.com/watch?list=example&v=TEST0000001'):
            with self.subTest(url=url):
                self.assertIsNone(re.fullmatch(PATTERNS['video_url'], url))

    def test_capture_identity_boundaries(self):
        pattern = PATTERNS['capture_row'].replace('VIDEO_ID', 'TEST0000001')
        for row in ('- 09:32 | YouTube | Title | https://youtu.be/TEST0000001?si=example',
                    '- 10:15 | YouTube | [Title](https://www.youtube.com/watch?v=TEST0000001)',
                    '- 11:00 | YouTube | Title | https://youtube.com/shorts/TEST0000001'):
            self.assertIsNotNone(re.search(pattern, row))
        for row in ('A mention https://youtu.be/TEST0000001',
                    '- 09:32 | YouTube | Title | https://youtu.be/TEST0000002',
                    '- 09:32 | YouTube | Title | https://youtu.be/TEST0000001extra'):
            self.assertIsNone(re.search(pattern, row))

    def test_heading(self):
        text = '# Test\r\n#### 오늘의 인풋\r\n#### Reflection\r\n'
        self.assertEqual(len(re.findall(PATTERNS['input_heading'], text)), 1)
        self.assertEqual(len(re.findall(PATTERNS['input_heading'], '##### 오늘의 인풋\n')), 0)

    def test_guide_contains_exact_patterns(self):
        guide = (ROOT / 'shortcuts/experimental/README.md').read_text()
        for pattern in PATTERNS.values():
            self.assertIn(pattern, guide)


if __name__ == '__main__':
    unittest.main()
