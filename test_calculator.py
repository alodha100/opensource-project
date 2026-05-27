import unittest

from calculator import calculate


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate("add", 2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculate("subtract", 7, 4), 3)

    def test_multiply(self):
        self.assertEqual(calculate("multiply", 3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculate("divide", 8, 2), 4)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            calculate("divide", 8, 0)


if __name__ == "__main__":
    unittest.main()
