"""Integration test of the extraction workflow.
"""
import os
import unittest

import prototag.prototag as pt

from . import INTEGRATION_FILEDIR


class TestYAMLExtraction(unittest.TestCase):
    """Test the complete YAML extraction.
    """

    def test_file_1(self):
        """Valid markdown header
        """
        expected = {
            'author': 'olli',
            'tag': ['python', 'idea']
        }
        path = os.path.join(INTEGRATION_FILEDIR, 'test_file_1_valid.md')
        result = pt.extract_header(path)
        self.assertEqual(result, expected)

    def test_file_2(self):
        """Invalid header start.
        """
        path = os.path.join(INTEGRATION_FILEDIR,
                            'test_file_2_invalid_start_line.md')
        result = pt.extract_header(path)
        self.assertEqual(result, None)

    def test_file_3(self):
        """Invalid yaml content.
        """
        path = os.path.join(INTEGRATION_FILEDIR, 'test_file_3_invalid_yaml.md')
        result = pt.extract_header(path)
        self.assertEqual(result, None)

    def test_read_directory(self):
        """List all .md files.
        """
        testfile = os.path.join(INTEGRATION_FILEDIR, 'test_file_1_valid.md')
        results = pt.read_directory(INTEGRATION_FILEDIR)

        self.assertEqual(results, [
            (testfile, {
                'author': 'olli',
                'tag': ['python', 'idea']
            })
        ])
