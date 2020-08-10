import unittest
import solution

example = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3""".split("\n")


class TestSolution(unittest.TestCase):
    def test_parse_ingredient(self):
        self.assertEqual([-1, -2, 6, 3, 8],
                         solution.parse_ingredient(example[0]))
        self.assertEqual([2, 3, -2, -1, 3],
                         solution.parse_ingredient(example[1]))

    def test_total(self):
        self.assertEqual(62842880, solution.total([[-1, -2, 6, 3, 8], [2, 3, -2, -1, 3]], [44, 56]))

    def test_best_mix(self):
        self.assertEqual(62842880, solution.optimal(example))
    
    def test_best_mix_c(self):
        self.assertEqual(57600000, solution.optimal_c(example, 500))


if __name__ == '__main__':
    unittest.main()
