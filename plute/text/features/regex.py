"""
This module provides functions that work on regular expressions for feature extraction.
"""
from typing import List, Callable
from exegr import GroupRegexMatch


def regex_group_search(patterns: List[str]) -> Callable:
    """
    Compile list of regex-patterns.

    Returns a function that allows pattern matching in a list of strings.
    [[WARN]]: Negative look-(ahead|behind) patterns will fail.

    :param patterns: Regular expression patters.
    :return: Callable
    """
    compiled_patterns = GroupRegexMatch(patterns)

    def search(texts: List[str]) -> List[float]:
        """
        Match a previously compiled list of patterns.

        This function returns a list of the same size as number of patterns compiled.
        A scoring function grades each pattern on the basis of:
        - How frequently was a pattern seen across texts.
        - The span of that pattern for each string in the texts.
        The maximum score possible is 1, minimum 0.
        :param texts:
        :return:
        """
        return compiled_patterns.search(texts)
    return search
