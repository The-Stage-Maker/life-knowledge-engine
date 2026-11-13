import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from lke.capture_format import format_capture, make_daily_uri, source_type, url_key, validate_url

URL = 'https://www.youtube.com/watch?v=TEST0000001'
NOW = datetime(2026, 11, 11, 9, 32)


class CaptureFormattingTests(unittest.TestCase):
    def test_exact_format(self):
        self.assertEqual(format_capture(title='Video title', url=URL, captured_at=NOW),
                         '- 09:32 | YouTube | Video title | ' + URL)

    def test_fallback(self):
        for title in (None, '', ' \n '):
            self.assertIn('| YouTube video |', format_capture(title=title, url=URL))
        self.assertIn('| Web | Web link |', format_capture(url='https://example.com/item'))

    def test_injected_timezone_not_converted(self):
        local = NOW.replace(tzinfo=timezone(timedelta(hours=-7)))
        self.assertTrue(format_capture(url=URL, captured_at=local).startswith('- 09:32'))

    def test_default_local_clock(self):
        with patch('lke.capture_format.datetime') as clock:
            clock.now.return_value.astimezone.return_value = NOW
            self.assertTrue(format_capture(url=URL).startswith('- 09:32'))
            clock.now.assert_called_once_with()

    def test_title_cannot_inject_lines_or_columns(self):
        item = format_capture(url=URL, title='A | B\r\n#### heading <x> [link]')
        self.assertNotIn('\n', item)
        self.assertIn(r'A \| B', item)
        self.assertIn(r'\<x\>', item)

    def test_bad_urls(self):
        for url in ('', 'file:///secret', 'javascript:alert(1)', 'https://',
                    'https://example.com/a\nb', 'https://u:p@example.com',
                    'https://example.com:bad', 'https://[broken', 'https://example.com/a|b'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                validate_url(url)

    def test_source_host_boundary(self):
        self.assertEqual(source_type('https://youtube.com.example.com/watch'), 'Web')
        self.assertEqual(source_type('https://M.YOUTUBE.COM/watch?v=TEST0000001'), 'YouTube')

    def test_equivalent_video_keys(self):
        for url in ('https://youtu.be/TEST0000001?si=synthetic',
                    'https://youtube.com/shorts/TEST0000001',
                    'https://m.youtube.com/live/TEST0000001?t=12',
                    URL + '&list=synthetic&t=30'):
            self.assertEqual(url_key(url), url_key(URL))
        self.assertNotEqual(url_key(URL), url_key(URL.replace('0001', '0002')))
        self.assertEqual(url_key('https://youtube.com/playlist?list=synthetic'),
                         'https://youtube.com/playlist?list=synthetic')

    def test_original_url_preserved(self):
        url = 'https://youtu.be/TEST0000001?si=synthetic&t=30'
        self.assertTrue(format_capture(url=url).endswith(url))

    def test_uri_round_trip(self):
        entry = format_capture(title='한국어 & # + %', url=URL + '&t=3', captured_at=NOW)
        uri = make_daily_uri(vault='Synthetic & Test', entry=entry)
        params = parse_qs(urlsplit(uri).query)
        self.assertEqual(params['content'], [entry])
        self.assertEqual(params['vault'], ['Synthetic & Test'])
        self.assertEqual(params['heading'], ['오늘의 인풋'])
        self.assertEqual(params['append'], ['true'])
        self.assertNotIn('overwrite', params)
        self.assertIn('%20', uri)
        self.assertNotIn('+', uri)

    def test_uri_without_heading_and_validation(self):
        self.assertNotIn('heading=', make_daily_uri(vault='Synthetic', entry='x', heading=None))
        for kwargs in ({'vault': '', 'entry': 'x'}, {'vault': 'x', 'entry': ''},
                       {'vault': 'x', 'entry': 'x', 'heading': 'bad\nheading'}):
            with self.assertRaises(ValueError):
                make_daily_uri(**kwargs)


if __name__ == '__main__':
    unittest.main()
