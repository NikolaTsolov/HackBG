import unittest
from cat import read_file, has_enaugh_inputs

class TestCat (unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(read_file("text1.txt"), "We have some text here\n")

    def test_has_enaugh_inputs(self):
        self.assertFalse(has_enaugh_inputs(1))

if __name__ == '__main__':
    unittest.main()
