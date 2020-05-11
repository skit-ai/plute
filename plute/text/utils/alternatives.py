"""
This module provides functions that work on ASR alternatives described as:
```
[[{"transcript": "..."}]]
```
We call these alternatives_list.
and
```
[{"transcript": "..."}]
```
as alternatives.
"""
from typing import List, Dict


def flatten_alternatives(alternatives_list: List[List[Dict]], field="transcript", text_only=False) -> List[str]:
    """
    Flatten a list of alternatives.
    :param alternatives_list: Represents ASR transcription output.
    :param field: The field within alternatives that contains text.
    :return:
    """
    return [alternative[field] if text_only else alternative
            for alternatives in alternatives_list for alternative in alternatives]


def serialize_alternatives(alternatives_list: List[List[Dict]], field="transcript") -> str:
    """
    A string representation of a list of strings, useful for feature creation.
    :param alternatives_list: Represents ASR transcription output.
    :param field: The field within alternatives that contains text.
    :return:
    """
    flat_alternatives = flatten_alternatives(alternatives_list, field=field, text_only=True)
    return "<s> " + " <s></s> ".join(flat_alternatives) + " </s>"
