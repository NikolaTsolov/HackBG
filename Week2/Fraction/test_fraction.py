import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):

    def setUp(self):
        self.num1 = Fraction(1, 2)
        self.num2 = Fraction(2, 4)
        self.num3 = Fraction(7, 21)
        self.num0 = Fraction(8, 4)

    def test_init(self):
        self.assertTrue(isinstance(self.num1, Fraction))
        self.assertEqual(self.num1.numerator, 1)
        self.assertEqual(self.num1.denominator, 2)

    def test_simplify(self):
        self.num3.simplify()
        self.assertEqual(self.num3, Fraction(1, 3))
        self.num0.simplify()
        self.assertEqual(self.num0, Fraction(2, 1))

    def test_str(self):
        self.assertEqual(str(self.num1), "1 / 2")
        self.assertEqual(str(self.num2), "1 / 2")
        self.assertEqual(str(self.num3), "1 / 3")
        self.assertEqual(str(Fraction(2, 1)), "2")

    def test_add(self):
        num4 = self.num1 + self.num2
        num5 = self.num2 + self.num3
        self.assertEqual(num5, Fraction(5, 6))
        self.assertEqual(num4, Fraction(1, 1))

    def test_sub(self):
        num4 = self.num1 - self.num2
        num5 = self.num3 - self.num1
        num6 = self.num2 - self.num3
        self.assertEqual(num4, Fraction(0, 1))
        self.assertEqual(num5, Fraction(-1, 6))
        self.assertEqual(num6, Fraction(1, 6))

    def test_mul(self):
        num4 = self.num1 * self.num2
        num5 = self.num3 * self.num3
        self.assertEqual(num4, Fraction(1, 4))
        self.assertEqual(num5, Fraction(1, 9))

    def test_eq(self):
        self.assertFalse(self.num1 == self.num3)
        self.assertTrue(self.num1 == self.num2)

if __name__ == '__main__':
    unittest.main()


