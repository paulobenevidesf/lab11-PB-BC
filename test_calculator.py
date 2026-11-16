# https://github.com/paulobenevidesf/lab11-PB-BC
# Partner 1: Paulo Jose Benevides Filho
# Partner 2: Benjamin Cao

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-1, 5), -5)

    def test_divide(self):
        # Based on how your divide function was written (b/a)
        self.assertEqual(calculator.div(2, 10), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -4)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()