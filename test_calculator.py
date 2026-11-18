# https://github.com/paulobenevidesf/lab11-PB-BC
# Partner 1: Paulo Jose Benevides Filho
# Partner 2: Benjamin Cao

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2,3),5)
        self.assertEqual(calculator.add(-7,4),-3)
        self.assertEqual(calculator.add(-7,-3),-10)
    def test_subtract(self):
        self.assertEqual(calculator.sub(1,1),0)
        self.assertEqual(calculator.sub(-1,-2),1)
        self.assertEqual(calculator.sub(5,7),-2)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError,calculator.div,0,0)
        self.assertRaises(ZeroDivisionError,calculator.div,0,-1)
        self.assertRaises(ZeroDivisionError,calculator.div,0,1)

    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(10,100),2)
        self.assertEqual(calculator.logarithm(2,8),3)
        self.assertEqual(calculator.logarithm(3,27),3)

    def test_logarithm_invalid_base(self):
        self.assertRaises(ValueError, calculator.logarithm,1,10)
        self.assertRaises(ValueError, calculator.logarithm,0,12)
        self.assertRaises(ValueError, calculator.logarithm,-1,0)

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