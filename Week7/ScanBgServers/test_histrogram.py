import unittest
from histogram import Histrogram

class TestHistrogram(unittest.TestCase):

    def setUp(self):
        self.h = Histrogram()
        self.h.add("Apache")
        self.h.add("Apache")
        self.h.add("nginx")
        self.h.add("IIS")
        self.h.add("nginx")

    def test_get_dict(self):
        d = {"Apache": 2, "nginx": 2, "IIS": 1}
        self.assertEqual(self.h.get_dict(), d)

    def test_items(self):
        for key, count in self.h.items():
            print("{}: {}".format(key, count))

if __name__ == '__main__':
    unittest.main()
