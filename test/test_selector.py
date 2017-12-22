"""Unit tests
"""
import unittest
import prototag.selector as selector
from prototag.selector import select_results


class TestSelector(unittest.TestCase):
    """Test the complete result selector.
    """

    results = [
        ('file1', {
            'author': ['flxbe'],
            'tag': ['tag1', 'tag2']
        }),
        ('file2', {
            'author': ['flxbe'],
            'tag': ['tag1', 'tag3']
        }),
        ('file3', {
            'tag': ['tag1']
        })
    ]

    def select_results(self, filenames):
        """Select and return a subset of the testresults.
        """
        return [(f, d) for (f, d) in self.results if f in filenames]

    def test_no_selectors(self):
        """This should return everything."""
        selected_results = select_results(self.results, {})
        self.assertEqual(selected_results, self.results)

    def test_unknown_selectors(self):
        """An unknown selector is used."""
        selector_strings = {
            'unknwon': 'value'
        }
        selected_results = select_results(self.results, selector_strings)
        self.assertEqual(selected_results, [])

    def test_unknown_selectors_with_empty_value(self):
        """An unknown selector without any value  is used."""
        selector_strings = {
            'unknwon': ''
        }
        selected_results = select_results(self.results, selector_strings)
        self.assertEqual(selected_results, self.results)

    def test_unknown_selectors_without_value(self):
        """An unknown selector without any value  is used."""
        selector_strings = {
            'unknwon': None
        }
        selected_results = select_results(self.results, selector_strings)
        self.assertEqual(selected_results, self.results)

    def test_all_results_valid(self):
        """All results are valid."""
        selector_strings = {
            'tag': 'tag1'
        }
        selected_results = select_results(self.results, selector_strings)
        self.assertEqual(selected_results, self.results)

    def test_exclude_invalid_results(self):
        """Only one result is valid."""
        selector_strings = {
            'tag': 'tag1,tag2'
        }
        expected_results = self.select_results(['file1'])
        selected_results = select_results(self.results, selector_strings)
        self.assertEqual(len(selected_results), 1)
        self.assertEqual(selected_results, expected_results)

    def test_select_by_multiple_attributes(self):
        """Also select by author name"""
        selector_strings = {
            'author': 'flxbe',
            'tag': 'tag2'
        }
        expected_results = self.select_results(['file1'])
        selected_results = select_results(self.results, selector_strings)
        self.assertEqual(len(selected_results), 1)
        self.assertEqual(selected_results, expected_results)


class TestValidate(unittest.TestCase):
    """Test the validation function.
    """

    def test_valid_or_clause(self):
        result = ('filename', {
            'tag': ['tag1', 'tag2']
        })
        selectors = {
            'tag': [['tag1'], ['tag3']]
        }
        self.assertTrue(selector.validate(result, selectors))

    def test_invalid_or_clause(self):
        result = ('filename', {
            'tag': ['tag1', 'tag2']
        })
        selectors = {
            'tag': [['tag3'], ['tag4']]
        }
        self.assertFalse(selector.validate(result, selectors))

    def test_valid_and_clause(self):
        result = ('filename', {
            'tag': ['tag1', 'tag2']
        })
        selectors = {
            'tag': [['tag1', 'tag2']]
        }
        self.assertTrue(selector.validate(result, selectors))

    def test_invalid_and_clause(self):
        result = ('filename', {
            'tag': ['tag1', 'tag2']
        })
        selectors = {
            'tag': [['tag1', 'tag3']]
        }
        self.assertFalse(selector.validate(result, selectors))


class TestSelectorParser(unittest.TestCase):
    """Test the selector extraction.
    """

    def test_no_selector_string(self):
        """Should return None.
        """
        result = selector.parse()
        self.assertEqual(result, None)

    def test_empty_selector_string(self):
        """Should return None.
        """
        result = selector.parse('')
        self.assertEqual(result, None)

    def test_single_and_selector(self):
        """Should extract a single AND selector.
        """
        result = selector.parse('idea,python')
        self.assertEqual(result, [
            ['idea', 'python']
        ])

    def test_single_or_selector(self):
        """Should extract a single OR selector.
        """
        result = selector.parse('python:programing')
        self.assertEqual(result, [
            ['python'],
            ['programing']
        ])

    def test_selector(self):
        """Should extract OR and AND selectors.
        """
        result = selector.parse('idea,python:programing')
        self.assertEqual(result, [
            ['idea', 'python'],
            ['programing']
        ])
