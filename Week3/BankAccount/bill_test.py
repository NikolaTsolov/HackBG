import unittest
from CashDesk import Bill

class BillTest(unittest.TestCase):
    def setUp(self):
        self.my_bill = Bill(5)
    def test_create_new_bill_instance(self):
        self.assertTrue(isinstance(self.my_bill, Bill))

    def test_valid_amount(self):
        self.assertEqual(self.my_bill.amount, 5)

    def test_int_cast(self):
        self.assertEqual(int(self.my_bill), 5)

    def test_str_cast(self):
        my_bill = Bill(5)
        self.assertEqual(str(my_bill), "5")

'''   def test_eq(self):
        other_bill = Bill(5)
        self.assertTrue(self.my_bill == other_bill)'''

if __name__ == '__main__':
    unittest.main()
