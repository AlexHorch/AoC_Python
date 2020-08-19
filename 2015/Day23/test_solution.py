import unittest
from solution import compute, getState





class TestSolution(unittest.TestCase):
    def test_compute_inc_a(self):
        self.assertEqual([1, {"a": 1, "b": 0}], compute(
            ["inc a"], getState()))

    def test_compute_inc_b(self): self.assertEqual([1, {"a": 0, "b": 1}], compute(
        ["inc b"], getState()))

    def test_compute_hlf_a(self):
        self.assertEqual([1, {"a": 2, "b": 5}], compute(
            ["hlf a"], getState(a=5, b=5)))

    def test_compute_hlf_b(self):
        self.assertEqual([1, {"a": 5, "b": 2}], compute(
            ["hlf b"], getState(a=5, b=5)))

    def test_compute_tpl_a(self):
        self.assertEqual([1, {"a": 15, "b": 5}], compute(
            ["tpl a"], getState(a=5, b=5)))

    def test_compute_tpl_b(self):
        self.assertEqual([1, {"a": 5, "b": 15}], compute(
            ["tpl b"], getState(a=5, b=5)))

    def test_compute_jmp_simple(self):
        self.assertEqual([5, {"a": 0, "b": 0}], compute(["jmp 5"], getState()))

    def test_compute_jio(self):
        self.assertEqual([6, {"a": 0, "b": 1}], compute(
            ["jio a 5", "jio b 5"], getState(b=1)))


if __name__ == "__main__":
    unittest.main()
