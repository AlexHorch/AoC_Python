import unittest
from solution import primes


class TestSolution(unittest.TestCase):
    def test_primes_10(self):
        self.assertListEqual([2, 3, 5, 7], primes(10))

    def test_primes_5(self):
        self.assertListEqual([2, 3, 5], primes(5))


if __name__ == '__main__':
    unittest.main()
