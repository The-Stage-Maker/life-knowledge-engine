import sys
import unittest
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from lke.daily_note import append_capture

URL = 'https://www.youtube.com/watch?v=TEST0000001'
NOW = datetime(2026, 11, 11, 9, 32)


def capture(note, **kwargs):
    return append_capture(note, url=URL, captured_at=NOW, **kwargs)


class DailyNoteTests(unittest.TestCase):
    def test_missing_note(self):
        self.assertEqual(capture(None).content,
                         '#### 오늘의 인풋\n- 09:32 | YouTube | YouTube video | ' + URL + '\n')

    def test_template_is_preserved_and_literal(self):
        template = '---\ntags: [synthetic]\n---\n# {{date}}\n\n#### 오늘의 인풋\n\n#### Reflection\nKeep this.\n'
        result = capture(None, template=template)
        self.assertTrue(result.added)
        self.assertIn('# {{date}}', result.content)
        self.assertTrue(result.content.endswith('#### Reflection\nKeep this.\n'))
        self.assertEqual(result.content.replace(result.entry + '\n\n', ''), template)

    def test_existing_empty_note_does_not_apply_template(self):
        self.assertNotIn('Template', capture('', template='Template').content)

    def test_missing_heading_appended(self):
        note = '# Synthetic day\n\nKeep every character.'
        self.assertTrue(capture(note).content.startswith(note + '\n\n#### 오늘의 인풋'))

    def test_duplicate_and_url_variant_preserve_exact_text(self):
        first = capture(None).content
        again = append_capture(first, url='https://youtu.be/TEST0000001?si=test',
                               title='Changed metadata', captured_at=NOW.replace(hour=12))
        self.assertFalse(again.added)
        self.assertEqual(first, again.content)

    def test_distinct_video_and_new_day(self):
        first = capture(None).content
        self.assertTrue(append_capture(first, url=URL.replace('0001', '0002')).added)
        self.assertTrue(capture(None).added)

    def test_legacy_row_duplicate(self):
        note = '- 08:01 | YouTube | [Old title](' + URL + ')\n'
        self.assertFalse(capture(note).added)

    def test_mention_is_not_capture(self):
        self.assertTrue(capture('A reflection mentions ' + URL).added)

    def test_nested_heading_belongs_to_section(self):
        note = '#### 오늘의 인풋\n##### Detail\nKeep\n#### Next\nUnchanged'
        result = capture(note)
        self.assertLess(result.content.index('Keep'), result.content.index(result.entry))
        self.assertLess(result.content.index(result.entry), result.content.index('#### Next'))

    def test_fenced_heading_and_capture_ignored(self):
        for fence in ('```', '~~~~'):
            note = fence + '\n#### 오늘의 인풋\n- 09:32 | YouTube | Demo | ' + URL + '\n' + fence + '\n'
            result = capture(note)
            self.assertTrue(result.added)
            self.assertTrue(result.content.startswith(note))
            self.assertEqual(result.content.count('#### 오늘의 인풋'), 2)

    def test_frontmatter_heading_ignored(self):
        note = '---\n#### 오늘의 인풋\n---\n# Day\n'
        self.assertEqual(capture(note).content.count('#### 오늘의 인풋'), 2)

    def test_ambiguous_heading_fails(self):
        with self.assertRaises(ValueError):
            capture('#### 오늘의 인풋\n#### 오늘의 인풋\n')

    def test_crlf_preserved(self):
        result = capture('# Day\r\n#### 오늘의 인풋\r\n#### Next\r\n')
        self.assertNotIn('\n', result.content.replace('\r\n', ''))

    def test_unclosed_markdown_fails_without_inserting_into_code(self):
        for note in ('---\ntags: synthetic\n', '```\nexample', '~~~~\nexample'):
            with self.subTest(note=note), self.assertRaises(ValueError):
                capture(note)

    def test_no_trailing_newline(self):
        self.assertIn('#### 오늘의 인풋\n- 09:32', capture('#### 오늘의 인풋').content)


if __name__ == '__main__':
    unittest.main()
