import pytest
from plute.text.utils.alternatives import flatten_alternatives, serialize_alternatives


flatten_alternatives_test_cases = [
    (
        [[{"transcript": f"text_{i}"}] for i in range(5)],
        True,
        [f"text_{i}" for i in range(5)]
    ),
    (
        [[{"transcript": f"text_{i}"}] for i in range(5)],
        False,
        [{"transcript": f"text_{i}"} for i in range(5)]
    )
]


@pytest.mark.parametrize("alternatives, text_only, expected", flatten_alternatives_test_cases)
def test_flatten_alternatives(alternatives, text_only, expected):
    test_output = flatten_alternatives(alternatives, text_only=text_only)
    assert test_output == expected


serialize_alternatives_test_cases = [
    (
        [[{"transcript": f"text_{i}"}] for i in range(1, 4)],
        "<s> text_1 <s></s> text_2 <s></s> text_3 </s>"
    ),
    (
        [[{"transcript": f"<UNK>_{i} <UNK>_{(i + 1)}"}] for i in range(1, 4)],
        "<s> <UNK>_1 <UNK>_2 <s></s> <UNK>_2 <UNK>_3 <s></s> <UNK>_3 <UNK>_4 </s>"
    )
]


@pytest.mark.parametrize("alternatives, expected", serialize_alternatives_test_cases)
def test_serialize_alternatives(alternatives, expected):
    test_output = serialize_alternatives(alternatives)
    assert test_output == expected
