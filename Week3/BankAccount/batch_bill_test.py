from CashDesk import BillBatch
from CashDesk import Bill
import unittest

class TestBillBatch(unittest.TestCase):
    def setUp(self):
        self.values = [10, 20, 50, 100]
        self.bills = [Bill(value) for value in self.values]

        self.my_batch = BillBatch(self.bills)
    def test_init(self):
        self.assertTrue(isinstance(self.my_batch, BillBatch))
        self.assertEqual(self.my_batch.bills, self.bills)

    def test_iteration(self):
            self.assertEqual(self.my_batch[1], self.my_batch[1])

            with self.assertRaises(ValueError):
                my.acount(-50)

if __name__ == '__main__':
    unittest.main()
