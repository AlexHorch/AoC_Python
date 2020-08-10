import unittest
import solution

example = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""


class TestSolution(unittest.TestCase):
    def test_shortest(self):
        self.assertEqual(605, solution.shortest(example))

    def test_longest(self):
        self.assertEqual(982, solution.longest(example))


if __name__ == '__main__':
    unittest.main()
