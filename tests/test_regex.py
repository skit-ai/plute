import pytest
from plute.text.features.regex import regex_group_search


text_inputs_and_scores = [
    (["555", "555", "542"], 0),
    (["aaca", "aacaaa", "aacaa"], 1),
    (["aab", "aabab", "aababab"], 2),
]


@pytest.mark.parametrize("test_input, matching_index", text_inputs_and_scores)
def test_regex_group_search(test_input, matching_index):
    """
    test function for single pattern match.
    The inputs are such that only one of the pattern matches all the strings.
    """
    test_output = regex_group_search([r"\d+", "aaca+", "a(ab)+"])(test_input)
    for idx, value in enumerate(test_output):
        if idx == matching_index:
            assert value > 0.9
        else:
            assert value == 0
