import unittest
import solution


class TestSolution(unittest.TestCase):

    def test_to_reindeer(self):
        self.assertEqual(solution.Reindeer("Vixen", "8", "8", "53"), solution.to_reindeer(
            "Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds."))

    def test_distance(self):
        self.assertEqual(1120, solution.Reindeer(
            "Comet", "14", "10", "127").distance(1000))

    def test_scores(self):
        self.assertEqual({"Comet": 312, "Dancer": 689}, solution.scores(solution.reindeers(
            "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.\nDancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."), 1000))


if __name__ == '__main__':
    unittest.main()
