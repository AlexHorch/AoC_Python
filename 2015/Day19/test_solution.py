import unittest
from solution import add_exchange, parse_exchanges, applications, symbols, steps

lines = """H => HO
H => OH
O => HH"""

subs = parse_exchanges(lines)


class TestSolution(unittest.TestCase):
    def test_add_exchange(self):
        x = {}
        add_exchange(x, "a => b")
        self.assertEqual({"a": ["b"]}, x)

    def test_parse_exchanges_1_line(self):
        self.assertEqual({"a": ["b"]}, parse_exchanges("a => b"))

    def test_parse_exchanges_2_lines(self):
        self.assertEqual({"a": ["b", "c"]}, parse_exchanges("a => b\na => c"))

    def test_applications_HOH(self):
        self.assertEqual(4, len(applications("HOH", subs)))

    def test_applications_HOHOHO(self):
        self.assertEqual(7, len(applications("HOHOHO", subs)))


if __name__ == '__main__':
    unittest.main()
