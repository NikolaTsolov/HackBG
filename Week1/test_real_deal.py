import unittest
from the_real_deal import sum_of_divisors, is_prime, prime_number_of_divisors
from the_real_deal import contains_digit, contains_digits, is_number_balanced
from the_real_deal import count_substrings, zero_insert, sum_matrix
from the_real_deal import is_within, bomb, matrix_bombing_plan

class TestRealDeal(unittest.TestCase):

    def test_sum_of_divisors(self):
        self.assertEqual(sum_of_divisors(8), 15)
        self.assertEqual(sum_of_divisors(7), 8)
        self.assertEqual(sum_of_divisors(1), 1)
        self.assertEqual(sum_of_divisors(1000), 2340)

    def test_is_prime(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(8), False)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(-10), False)
        self.assertEqual(is_prime(113), True)

    def test_prime_number_of_devisors(self):
        self.assertEqual(prime_number_of_divisors(7), True)
        self.assertEqual(prime_number_of_divisors(8), False)
        self.assertEqual(prime_number_of_divisors(9), True)

    def test_contains_digit(self):
        self.assertEqual(contains_digit(123, 4), False)
        self.assertEqual(contains_digit(42, 2), True)
        self.assertEqual(contains_digit(1000, 0), True)
        self.assertEqual(contains_digit(12346789, 5), False)

    def test_contains_digits(self):
        self.assertEqual(contains_digits(402123, [0, 3, 4]), True)
        self.assertEqual(contains_digits(666, [6, 4]), False)
        self.assertEqual(contains_digits(123456789, [1, 2, 3, 0]), False)
        self.assertEqual(contains_digits(456, []), True)

    def test_is_number_balanced(self):
        self.assertEqual(is_number_balanced(9), True)
        self.assertEqual(is_number_balanced(11), True)
        self.assertEqual(is_number_balanced(13), False)
        self.assertEqual(is_number_balanced(121), True)
        self.assertEqual(is_number_balanced(4518), True)
        self.assertEqual(is_number_balanced(28471), False)
        self.assertEqual(is_number_balanced(1238033), True)

    def test_count_substrings(self):
        self.assertEqual(count_substrings("This is a test string", "is"), 2)
        self.assertEqual(count_substrings("babababa", "baba"), 2)
        self.assertEqual(count_substrings("Python is an awesome language to program in!", "o"), 4)
        self.assertEqual(count_substrings("We have nothing in common!", "really?"), 0)
        self.assertEqual(count_substrings("This is this and that is this", "this"), 2)

    def test_zero_insertion(self):
        self.assertEqual(zero_insert(116457), 10160457)
        self.assertEqual(zero_insert(55555555), 505050505050505)
        self.assertEqual(zero_insert(1), 1)
        self.assertEqual(zero_insert(6446), 6040406)

    def test_sum_matrix(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sum_matrix(m), 45)
        m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(sum_matrix(m), 0)
        m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        self.assertEqual(sum_matrix(m), 55)

    def test_is_within(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(is_within(m, (0, 0)), True)
        self.assertEqual(is_within(m, (-1, 1)), False)
        self.assertEqual(is_within(m, (3, 0)), False)
        self.assertEqual(is_within(m, (0, -1)), False)
        self.assertEqual(is_within(m, (0, 3)), False)

    def test_bomb(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m2 = [[1, 1, 3], [3, 4, 6], [7, 8, 9]]
        m3 = [[0, 0, 0], [0, 5, 1], [2, 3, 4]]
        self.assertEqual(bomb(m, (0, 0)), m2)
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(bomb(m, (1, 1)), m3)

    def test_matrix_bombing_plan(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        dictonary = {
            (0, 0): 42,
            (0, 1): 36,
            (0, 2): 37,
            (1, 0): 30,
            (1, 1): 15,
            (1, 2): 23,
            (2, 0): 29,
            (2, 1): 15,
            (2, 2): 26}
        self.assertEqual(matrix_bombing_plan(m), dictonary)


if __name__ == '__main__':
    unittest.main()
