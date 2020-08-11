import unittest
from solution import permutations


class TestSolution(unittest.TestCase):
    def test_permutations(self):
        self.assertEqual([(0,), (1,)], list(permutations(1)))
    def test_permutations_b(self):
        self.assertEqual([(0,0,),(0,1,),(1,0,),(1,1,)], list(permutations(2)))


if __name__ == '__main__':
    unittest.main()
