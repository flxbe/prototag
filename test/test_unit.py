"""Unit tests
"""
import unittest
import prototag.prototag as pt


def create_gen(lines):
    """Create a line generator from an array of lines.
    """
    for line in lines:
        print(line)
        yield line


class TestMarkdownExtractor(unittest.TestCase):
    """Test the extractor utility for `.md`-files.
    """

    def test_valid_header(self):
        """The header extractor should only return the correct header content.
        """
        lines = [
            '<!--\n',
            'test string 1\n',
            'test string 2\n',
            '-->\n',
            '\n',
            '# Header\n',
            'Some content.\n'
        ]
        result = pt.extract_md_header(create_gen(lines))
        self.assertEqual(result, 'test string 1\ntest string 2\n')

    def test_invalid_header_start(self):
        """Invalid header start.
        """
        lines = [
            '<--\n',
            'test string 1\n',
            '-->\n'
        ]
        result = pt.extract_md_header(create_gen(lines))
        self.assertEqual(result, None)

    def test_header_not_at_beginning(self):
        """The header does not start at the first line.
        """
        lines = [
            '\n',
            '<!--\n',
            'test string 1\n',
            '-->\n'
        ]
        result = pt.extract_md_header(create_gen(lines))
        self.assertEqual(result, None)

    def test_no_header_end(self):
        """The header is not properly closed.
        """
        lines = [
            '<!--\n',
            'test string 1\n',
        ]
        result = pt.extract_md_header(create_gen(lines))
        self.assertEqual(result, None)
