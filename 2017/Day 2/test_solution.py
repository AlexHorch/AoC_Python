import unittest
import solution


class TestSolution(unittest.TestCase):
    def test_spreadsheet_checksum_1(self):
        result = solution.sscs1("5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8")
        self.assertEqual(18, result)

    def test_row_checksum_1_1(self):
        result = solution.rcs1("5\t1\t9\t5")
        self.assertEqual(8, result)

    def test_row_checksum_1_2(self):
        result = solution.rcs1("7\t5\t3")
        self.assertEqual(4, result)

    def test_row_checksum_1_3(self):
        result = solution.rcs1("2\t4\t6\t8")
        self.assertEqual(6, result)

    def test_row_checksum_2_1(self):
        result = solution.rcs2("5\t9\t2\t8")
        self.assertEqual(4, result)

    def test_row_checksum_2_2(self):
        result = solution.rcs2("9\t4\t7\t3")
        self.assertEqual(3, result)

    def test_row_checksum_2_1(self):
        result = solution.rcs2("3\t8\t6\t5")
        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()
