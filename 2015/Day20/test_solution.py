import math
import unittest
from solution import primes, prime_factorization, presents, permutations

ps = primes(int(math.sqrt(36000000))+1)


class TestSolution(unittest.TestCase):
    def test_primes_10(self):
        self.assertListEqual([2, 3, 5, 7], primes(10))

    def test_primes_5(self):
        self.assertListEqual([2, 3, 5], primes(5))

    def test_prime_factorization_primes(self):
        self.assertListEqual([], prime_factorization(1, ps))
        self.assertListEqual([2], prime_factorization(2, ps))
        self.assertListEqual([5], prime_factorization(5, ps))
        self.assertListEqual([11], prime_factorization(11, ps))

    def test_prime_factorization_komposites(self):
        self.assertListEqual([2, 3], prime_factorization(6, ps))
        self.assertListEqual([3, 5], prime_factorization(15, ps))
        self.assertListEqual([5, 5, 5], prime_factorization(125, ps))
        self.assertListEqual([2, 2, 3, 3, 5], prime_factorization(180, ps))

    def test_permutations(self):
        self.assertCountEqual([(0,),(1,) ],permutations(1))
        self.assertCountEqual([], permutations(0))

    def test_presents(self):
        self.assertEqual(10, presents(1, ps))
        self.assertEqual(30, presents(2, ps))
        self.assertEqual(40, presents(3, ps))
        self.assertEqual(70, presents(4, ps))


if __name__ == '__main__':
    unittest.main()
