import unittest
import solution

examples = [""".#.#.#
...##.
#....#
..#...
#.#..#
####..""", """..##..
..##.#
...##.
......
#.....
#.##..""", """..###.
......
..###.
......
.#....
.#....""", """...#..
......
...#..
..##..
......
......""", """......
......
..##..
..##..
......
......"""]


class TestSolution(unittest.TestCase):
    def test_parse(self):
        self.assertListEqual([[0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 0], [1, 0, 0, 0, 0, 1], [
                             0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 0, 0]], solution.parse_input(examples[0]))

    def test_state(self):
        f = solution.parse_input(examples[0])
        self.assertEqual(0, solution.state(f, 0, 0))
        self.assertEqual(0, solution.state(f, -1, 0))
        self.assertEqual(0, solution.state(f, 0, -1))
        self.assertEqual(0, solution.state(f, 6, 0))
        self.assertEqual(0, solution.state(f, 0, 6))
        self.assertEqual(1, solution.state(f, 0, 1))

    def test_step_1(self):
        self.assertListEqual(solution.parse_input(
            examples[1]), solution.step(solution.parse_input(examples[0])))

    def test_step_2(self):
        self.assertListEqual(solution.parse_input(
            examples[2]), solution.step(solution.parse_input(examples[1])))

    def test_step_3(self):
        self.assertListEqual(solution.parse_input(
            examples[3]), solution.step(solution.parse_input(examples[2])))

    def test_step_4(self):
        self.assertListEqual(solution.parse_input(
            examples[4]), solution.step(solution.parse_input(examples[3])))


if __name__ == '__main__':
    unittest.main()
