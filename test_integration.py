"""Integration test of the extraction workflow.
"""
import os
import unittest

import prototag as pt


class TestYAMLExtraction(unittest.TestCase):
    """Test the complete YAML extraction.
    """

    def test_file_1(self):
        """Valid markdown header
        """
        expected = {
            'author': 'Felix Bernhardt',
            'tags': ['the-new-google', 'idea']
        }
        result = pt.extract_header('./test/test_file_1_valid.md')
        self.assertEqual(result, expected)

    def test_file_2(self):
        """Invalid header start.
        """
        result = pt.extract_header('./test/test_file_2_invalid_start_line.md')
        self.assertEqual(result, None)

    def test_file_3(self):
        """Invalid yaml content.
        """
        result = pt.extract_header('./test/test_file_3_invalid_yaml.md')
        self.assertEqual(result, None)

    def test_read_directory(self):
        """List all .md files.
        """
        testdir = './test'
        testfile = os.path.join(testdir, 'test_file_1_valid.md')
        results = pt.read_directory('./test')

        self.assertEqual(results, [
            (testfile, {
                'author': 'Felix Bernhardt',
                'tags': ['the-new-google', 'idea']
            })
        ])
