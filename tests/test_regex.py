from unittest import TestCase
from plute.text.features.regex import regex_group_search


class Test(TestCase):
    def test_regex_group_search(self):
        text_input = ["555", "555", "542"]
        test_output = regex_group_search([r"\d+", "aaca+", "a(ab)+"])(text_input)
        self.assertGreater(1, test_output[0])
        self.assertEqual(0, test_output[1])
        self.assertEqual(0, test_output[2])
