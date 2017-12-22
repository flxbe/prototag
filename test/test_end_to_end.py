"""Test the complete tool by using the CLI.
"""
import unittest
import subprocess

import prototag

from . import ENDTOEND_FILEDIR

VERSION = prototag.__version__


class TestEndToEnd(unittest.TestCase):
    """Test the CLI.
    """

    def stdout_result(self, filenames):
        """return the stdout result based on the expected filenames.
        """
        filestring = '\n'.join(filenames)
        return '{}\n'.format(filestring).encode()

    def test_cli(self):
        """Should work
        """
        stdout = subprocess.check_output('ptag')
        self.assertEqual(stdout, b'')

    def test_version(self):
        """Should print the version using `--version`
        """
        expected = '{}\n'.format(VERSION).encode()
        stdout = subprocess.check_output(['ptag', '--version'])
        self.assertEqual(stdout, expected)

    def test_short_version(self):
        """Should print the version using `-v`
        """
        expected = '{}\n'.format(VERSION).encode()
        stdout = subprocess.check_output(['ptag', '-v'])
        self.assertEqual(stdout, expected)

    def test_print_all_valid_files(self):
        """Should return the filenames of all valid files.
        """
        expected = self.stdout_result([
            'file_1.md',
            'file_2.md'
        ])
        stdout = subprocess.check_output(['ptag', ENDTOEND_FILEDIR])
        self.assertEqual(stdout, expected)

    def test_filter_by_tag(self):
        """Should filter the files by tag.
        """
        tag_selector = 'python'
        expected = self.stdout_result([
            'file_2.md'
        ])
        stdout = subprocess.check_output(
            ['ptag', '-t', tag_selector, ENDTOEND_FILEDIR])
        self.assertEqual(stdout, expected)

    def test_filter_by_tag_using_long_option(self):
        """Should filter the files by tag.
        """
        tag_selector = 'python'
        expected = self.stdout_result([
            'file_2.md'
        ])
        stdout = subprocess.check_output(
            ['ptag', '--tag', tag_selector, ENDTOEND_FILEDIR])
        self.assertEqual(stdout, expected)

    def test_filter_by_tag_or_condition(self):
        """Should filter the files by tag.
        """
        tag_selector = 'python:js'
        expected = self.stdout_result([
            'file_1.md',
            'file_2.md'
        ])
        stdout = subprocess.check_output(
            ['ptag', '-t', tag_selector, ENDTOEND_FILEDIR])
        self.assertEqual(stdout, expected)

    def test_filter_by_author(self):
        """Should filter the files by author.
        """
        author_selector = 'jan'
        expected = self.stdout_result([
            'file_2.md'
        ])
        stdout = subprocess.check_output(
            ['ptag', '-a', author_selector, ENDTOEND_FILEDIR])
        self.assertEqual(stdout, expected)

    def test_filter_by_author_using_long_option(self):
        """Should filter the files by author.
        """
        author_selector = 'jan'
        expected = self.stdout_result([
            'file_2.md'
        ])
        stdout = subprocess.check_output(
            ['ptag', '--author', author_selector, ENDTOEND_FILEDIR])
        self.assertEqual(stdout, expected)

    def test_filter_by_multiple_author(self):
        """Should filter the files by author.
        """
        author_selector = 'jan,olli'
        expected = self.stdout_result([
            'file_2.md'
        ])
        stdout = subprocess.check_output(
            ['ptag', '-a', author_selector, ENDTOEND_FILEDIR])
        self.assertEqual(stdout, expected)

    def test_filter_by_author_and_tag(self):
        """Should filter the files by author.
        """
        author_selector = 'olli'
        tag_selector = 'js'
        expected = self.stdout_result([
            'file_1.md'
        ])
        stdout = subprocess.check_output(
            ['ptag', '-a', author_selector, '-t', tag_selector, ENDTOEND_FILEDIR])
        self.assertEqual(stdout, expected)
