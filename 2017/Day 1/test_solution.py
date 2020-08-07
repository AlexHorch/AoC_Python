import unittest
import solution


class TestSolution(unittest.TestCase):

    def template(self, fun, txt, exp):
        res = fun(txt)
        self.assertEqual(exp, res)

    def test_consecutiveSum_1(self):
        self.template(solution.consecutiveSum, "1122", 3)

    def test_consecutiveSum_2(self):
        self.template(solution.consecutiveSum, "1111", 4)

    def test_consecutiveSum_3(self):
        self.template(solution.consecutiveSum, "1234", 0)

    def test_consecutiveSum_4(self):
        self.template(solution.consecutiveSum, "91212129", 9)

    def test_halfwaySum_1(self):
        self.template(solution.halfwaySum, "1212", 6)

    def test_halfwaySum_2(self):
        self.template(solution.halfwaySum, "1221", 0)

    def test_halfwaySum_3(self):
        self.template(solution.halfwaySum, "123425", 4)

    def test_halfwaySum_4(self):
        self.template(solution.halfwaySum, "123123", 12)

    def test_halfwaySum_5(self):
        self.template(solution.halfwaySum, "12131415", 4)


if __name__ == '__main__':
    unittest.main()
