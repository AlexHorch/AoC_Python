import unittest
import solution

example = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""


class TestSolution(unittest.TestCase):
    def test_parse(self):
        self.assertListEqual([[0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 0], [1, 0, 0, 0, 0, 1], [
                             0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 0, 0]], solution.parse_input(example))

    def test_step(self):
        self.assertListEqual([[0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0], [
                             1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0]], solution.step(solution.parse_input(example)))


if __name__ == '__main__':
    unittest.main()
