import unittest
from solution import combinations


class TestSolution(unittest.TestCase):
    def test_combinations_six(self):
        self.assertCountEqual([[2, 2, 2], [3, 3], [6]],
                              combinations([2, 2, 2, 3, 3, 6]))


if __name__ == '__main__':
    unittest.main()
