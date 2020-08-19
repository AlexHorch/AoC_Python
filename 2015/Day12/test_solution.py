import unittest
from solution import evaluate_list


class TestSolution(unittest.TestCase):
    def test_parse_list(self):
        self.assertEquals(6, evaluate_list([1, 2, 3]))

    def test_parse_nested_list(self):
        self.assertEquals(3, evaluate_list([[[3]]]))

    def test_parse_nested_distionary_in_list(self):
        self.assertEquals(5, evaluate_list([{"a": 5}]))

    def test_parse_list_kokmposite(self):
        self.assertEquals(8, evaluate_list([[[[[[[[1],1]]]]]], {"a": 2}, 2, 2]))


if __name__ == '__main__':
    unittest.main()
