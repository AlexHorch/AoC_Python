import unittest
import solution

examples = r"""
""
"abc"
"aaa\"aaa"
"\x27"
""".split("\n")[1:-1]

lit = [2, 5, 10, 6]
act = [0, 3, 7, 1]


class TestSolution(unittest.TestCase):
    def test_first_example_code(self):
        self.assertEqual(2, solution.code_len(examples[0]))

    def test_second_example_code(self):
        self.assertEqual(5, solution.code_len(examples[1]))

    def test_third_example_code(self):
        self.assertEqual(10, solution.code_len(examples[2]))

    def test_fourth_example_code(self):
        self.assertEqual(6, solution.code_len(examples[3]))

    def test_first_example_mem(self):
        self.assertEqual(0, solution.mem_len(examples[0]))

    def test_second_example_mem(self):
        self.assertEqual(3, solution.mem_len(examples[1]))

    def test_third_example_mem(self):
        self.assertEqual(7, solution.mem_len(examples[2]))

    def test_fourth_example_mem(self):
        self.assertEqual(1, solution.mem_len(examples[3]))

    def test_first_example_rep(self):
        self.assertEqual(6, solution.rep_len(examples[0]))

    def test_second_example_rep(self):
        self.assertEqual(9, solution.rep_len(examples[1]))

    def test_third_example_rep(self):
        self.assertEqual(16, solution.rep_len(examples[2]))

    def test_fourth_example_rep(self):
        self.assertEqual(11, solution.rep_len(examples[3]))

    def test_diff1_example(self):
        self.assertEqual(12, solution.diff1(examples))

    def test_diff2_example(self):
        self.assertEqual(19, solution.diff2(examples))


if __name__ == '__main__':
    unittest.main()
