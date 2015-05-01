import unittest
from final_round import count_words, unique_words_count, nan_expend
from final_round import iteration_of_nan_expand, integer_prime_factorization
from final_round import group, same_items, max_consecutive, groupby
from final_round import prepare_meal, reduce_file_path, is_an_bn
from final_round import is_credit_card_valid, goldbach, magic_square
from final_round import friday_years

class TestFinalRound(unittest.TestCase):

    def test_count_words(self):
        l = ["apple", "banana", "apple", "pie"]
        d = {'apple': 2, 'pie': 1, 'banana': 1}
        self.assertEqual(count_words(l), d)
        l = ["python", "python", "python", "ruby"]
        d = {'ruby': 1, 'python': 3}
        self.assertEqual(count_words(l), d)

    def test_unique_words_count(self):
        l = ["apple", "banana", "apple", "pie"]
        self.assertEqual(unique_words_count(l), 3)
        l = ["python", "python", "python", "ruby"]
        self.assertEqual(unique_words_count(l), 2)
        self.assertEqual(unique_words_count(["HELLO!"] * 10), 1)

    def test_nan_expand(self):
        self.assertEqual(nan_expend(0), "")
        self.assertEqual(nan_expend(1), "Not a NaN")
        self.assertEqual(nan_expend(2), "Not a Not a NaN")
        self.assertEqual(nan_expend(3), "Not a Not a Not a NaN")

    def test_iteration_nan_expand(self):
        self.assertEqual(iteration_of_nan_expand(""), 0)
        self.assertEqual(iteration_of_nan_expand("Not a NaN"), 1)
        s = "Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN"
        self.assertEqual(iteration_of_nan_expand(s), 10)
        self.assertEqual(iteration_of_nan_expand("Hello Pappy"), False)
        self.assertEqual(iteration_of_nan_expand("Fizz Not a NaN"), False)

    def test_prime_factorisation(self):
        l = [(2, 1), (5, 1)]
        self.assertEqual(integer_prime_factorization(10), l)
        l = [(2, 1), (7, 1)]
        self.assertEqual(integer_prime_factorization(14), l)
        l = [(2, 2), (89, 1)]
        self.assertEqual(integer_prime_factorization(356), l)
        self.assertEqual(integer_prime_factorization(89), [(89, 1)])
        l = [(2, 3), (5, 3)]
        self.assertEqual(integer_prime_factorization(1000), l)

    def test_same_items(self):
        self.assertEqual(same_items([1, 1, 1, 2, 3, 1, 1]), [1, 1, 1])

    def test_group(self):
        l = [1, 1, 1, 2, 3, 1, 1]
        self.assertEqual(group(l), [[1, 1, 1], [2], [3], [1, 1]])
        l = [1, 2, 1, 2, 3, 3]
        self.assertEqual(group(l), [[1], [2], [1], [2], [3, 3]])

    def test_max_consecutive(self):
        l = [1, 2, 3, 3, 3, 3, 4, 3, 3]
        self.assertEqual(max_consecutive(l), 4)
        l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]
        self.assertEqual(max_consecutive(l), 3)

    def test_groupby(self):
        d = {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}
        l = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(groupby(lambda x: x % 2, l), d)
        d = {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
        l = [1, 2, 3, 5, 8, 9, 10, 12]
        self.assertEqual(groupby(lambda x: 'odd' if x % 2 else 'even', l), d)
        d = {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}
        l = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(groupby(lambda x: x % 3, l), d)

    def test_prepare_meal(self):
        self.assertEqual(prepare_meal(5), "eggs")
        self.assertEqual(prepare_meal(15), 'spam and eggs')
        self.assertEqual(prepare_meal(45), 'spam spam and eggs')
        self.assertEqual(prepare_meal(3), 'spam')

    def test_reduce_file_path(self):
        self.assertEqual(reduce_file_path("/"), "/")
        self.assertEqual(reduce_file_path("/srv/../"), "/")
        s1 = "/srv/www/htdocs/wtf/"
        self.assertEqual(reduce_file_path(s1), "/srv/www/htdocs/wtf")
        s1 = "/srv/www/htdocs/wtf"
        self.assertEqual(reduce_file_path(s1), "/srv/www/htdocs/wtf")
        s1 = "/srv/./././././"
        self.assertEqual(reduce_file_path(s1), "/srv")
        self.assertEqual(reduce_file_path("/etc//wtf/"), "/etc/wtf")
        s1 = "/etc/../etc/../etc/../"
        self.assertEqual(reduce_file_path(s1), "/")

        self.assertEqual(reduce_file_path("//////////////"), "/")
        self.assertEqual(reduce_file_path("/../"), "/")

    def test_is_an_bn(self):
        self.assertTrue(is_an_bn(""))
        self.assertFalse(is_an_bn("Rado"))
        self.assertFalse(is_an_bn("aaabb"))
        self.assertTrue(is_an_bn("aaabbb"))
        self.assertFalse(is_an_bn("aabbaabb"))
        self.assertFalse(is_an_bn("bbbaaa"))
        self.assertTrue(is_an_bn("aaaabbbb"))

    def test_is_credit_card_valid(self):
        self.assertTrue(is_credit_card_valid(79927398713))
        self.assertFalse(is_credit_card_valid(79927398715))

    def test_goldbach(self):
        self.assertEqual(goldbach(4), [(2, 2)])
        self.assertEqual(goldbach(6), [(3, 3)])
        self.assertEqual(goldbach(8), [(3, 5)])
        self.assertEqual(goldbach(10), [(3, 7), (5, 5)])
        self.assertEqual(goldbach(100), [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)])

    def test_magic_square(self):
        self.assertFalse(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertTrue(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
        l = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
        self.assertTrue(magic_square(l))
        l = [[23, 28, 21], [22, 24, 26], [27, 20, 25]]
        self.assertTrue(magic_square(l))
        l = [[16, 23, 17], [78, 32, 21], [17, 16, 15]]
        self.assertFalse(magic_square(l))

    def test_friday_years(self):
        self.assertEqual(friday_years(1000, 2000), 178)
        self.assertEqual(friday_years(1753, 2000), 44)
        self.assertEqual(friday_years(1990, 2015), 4)

if __name__ == '__main__':
    unittest.main()
