"""
This module provides functions that work on ASR utterances (refer to plute.types) described as:
```
[[{"transcript": "..."}]]
```
"""
import itertools
from functools import reduce
from operator import mul
from typing import List, Any
from plute.types import Utterance, Transcript


def merge_utterances(utterances: List[Utterance]) -> List[Utterance]:
    """
    Merge utterances into a single utterance.

    At times when the user is speaking with gaps, we get more than one utterance from
    the ASR.

    To make sure that the rest of the systems work fine, we merge those
    results using a cross join and re-rank them using the following two attributes:
    1. Sum of index for each utterance
    2. Product of confidence values

    NOTE: We are still returning items as if the ASR returned a single utterance.
          Also the confidence values here will be very low so care must be taken
          in interpretation.
    """
    merged = []

    def join_transcripts(transcripts):
        return " ".join(text.strip() for text in transcripts)

    indexed_utterances = [enumerate(utterance) for utterance in utterances]

    for utterance_product in itertools.product(*indexed_utterances):
        # utterance_product represents each combination of alternatives across utterances.
        # looks like:
        # ...
        # ((i, k::Alternative), (i, l::Alternative))
        # ((i, k::Alternative), (i + 1, l::Alternative)
        # ...
        # Where i -> index of alternative within the utterance.
        # and k, l denote different utterances.
        if utterance_product:
            index_sum = sum(idx for idx, _ in utterance_product)
            alternative = {
                "transcript": join_transcripts([alternative["transcript"] for _, alternative in utterance_product]),
                "confidence": reduce(mul, [alternative["confidence"] or 0 for _, alternative in utterance_product])
            }
            merged.append((index_sum, alternative))
    merged = sorted(merged, key=lambda utterance: (utterance[0], -utterance[1]["confidence"] or 0))[:10]
    return [[utterance for _, utterance in merged]]


def are_utterances_null(utterances: List[Any]) -> bool:
    return (not utterances) or (utterances == [[]])


def utterances_to_texts(utterances: List[Utterance]) -> List[Transcript]:
    """
    Return list of texts from single utterance alternatives. If there are more
    than one utterances, we only pick the first one.
    """
    if are_utterances_null(utterances):
        return []

    if isinstance(utterances[0], list):
        return [alternative["transcript"] for alternative in utterances[0]]

    return []
