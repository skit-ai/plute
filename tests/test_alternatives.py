import pytest
from plute.text.utils.utterances import serialize_utterances, merge_utterances, utterances_to_texts


flatten_utterances_test_cases = [
    (
        [[{"transcript": f"text_{i}_{j}", "confidence": 0} for j in range(3)] for i in range(3)],
        [[
            {'confidence': 0, 'transcript': 'text_0_0 text_1_0 text_2_0'},
            {'confidence': 0, 'transcript': 'text_0_0 text_1_0 text_2_1'},
            {'confidence': 0, 'transcript': 'text_0_0 text_1_1 text_2_0'},
            {'confidence': 0, 'transcript': 'text_0_1 text_1_0 text_2_0'},
            {'confidence': 0, 'transcript': 'text_0_0 text_1_0 text_2_2'},
            {'confidence': 0, 'transcript': 'text_0_0 text_1_1 text_2_1'},
            {'confidence': 0, 'transcript': 'text_0_0 text_1_2 text_2_0'},
            {'confidence': 0, 'transcript': 'text_0_1 text_1_0 text_2_1'},
            {'confidence': 0, 'transcript': 'text_0_1 text_1_1 text_2_0'},
            {'confidence': 0, 'transcript': 'text_0_2 text_1_0 text_2_0'}
        ]]
    )
]


@pytest.mark.parametrize("utterances, expected", flatten_utterances_test_cases)
def test_merge_utterances(utterances, expected):
    test_output = merge_utterances(utterances)
    assert test_output == expected


serialize_utterances_test_cases = [
    (
        [[{"transcript": f"text_{i}", "confidence": 0}] for i in range(1, 4)],
        "<s> text_1 text_2 text_3 </s>"
    ),
    (
        [[{"transcript": f"<UNK>_{i} <UNK>_{(i + 1)}", "confidence": 0} for i in range(1, 4)]],
        "<s> <UNK>_1 <UNK>_2 <s></s> <UNK>_2 <UNK>_3 <s></s> <UNK>_3 <UNK>_4 </s>"
    ),
    ([[]], ""),
    ([], "")
]


@pytest.mark.parametrize("utterances, expected", serialize_utterances_test_cases)
def test_serialize_utterances(utterances, expected):
    test_output = serialize_utterances(utterances)
    assert test_output == expected


invalid_utterance_format = [
    (["text"], [])
]


@pytest.mark.parametrize("utterances, expected", invalid_utterance_format)
def test_utterances_to_texts(utterances, expected):
    test_output = utterances_to_texts(utterances)
    assert test_output == expected
