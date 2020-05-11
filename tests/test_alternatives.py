from unittest import TestCase
from plute.text.utils.alternatives import flatten_alternatives, serialize_alternatives


class Test(TestCase):
    def test_flatten_alternatives(self):
        target = [f"text {i}" for i in range(5)]
        test_input = [[{"transcript": f"text {i}"} for i in range(5)]]
        test_output = flatten_alternatives(test_input, text_only=True)
        self.assertEqual(target, test_output, "Test failed: flatten_alternatives happy case failed.")

    def test_serialize_alternatives(self):
        target = "<s> text_1 <s></s> text_2 <s></s> text_3 </s>"
        test_input = [[{"transcript": "text_1"}, {"transcript": "text_2"}, {"transcript": "text_3"}]]
        test_output = serialize_alternatives(test_input)
        self.assertEqual(target, test_output, "Test failed: serialize_alternatives - happy case failed.")
