import unittest
from cash_desk import Bill, BillBatch, CashDesk

class TestBill(unittest.TestCase):

    def setUp(self):
        self.bill = Bill(10)
        self.bill2 = Bill(15)
        self.bill3 = Bill(10)

    def test_init(self):
        self.assertTrue(isinstance(self.bill, Bill))
        self.assertEqual(self.bill.amount, 10)

    def test_int(self):
        self.assertEqual(int(self.bill), 10)

    def test_str(self):
        self.assertEqual(str(self.bill), "A 10$ bill")

    def test_eq(self):
        self.assertFalse(self.bill == self.bill2)
        self.assertTrue(self.bill == self.bill3)

    def test_hash(self):
        self.assertIsNotNone(hash(self.bill), 10)

    def test_len(self):
        self.assertEqual(len(self.bill), 1)

class TestBatchBill(unittest.TestCase):

    def setUp(self):
        self.values = [10, 20, 50, 100]
        self.bills = [Bill(value) for value in self.values]
        self.batch = BillBatch(self.bills)

    def test_init(self):
        self.assertTrue(isinstance(self.batch, BillBatch))
        self.assertEqual(self.batch.bills, self.bills)

    def test_len(self):
        self.assertEqual(len(self.batch), 4)

    def test_total(self):
        self.assertEqual(self.batch.total(), 180)

    def test_int(self):
        self.assertEqual(int(self.batch), 180)

    def test_get_item(self):
        self.assertEqual(self.batch[0], self.bills[0])


class TestCashDesk(unittest.TestCase):

    def setUp(self):
        self.cash = CashDesk()
        self.values = [10, 20, 50, 100, 100, 100]
        self.bills = [Bill(value) for value in self.values]
        self.batch = BillBatch(self.bills)
        self.cash.take_money(self.batch)
        self.cash.take_money(Bill(10))

    def test_init(self):
        self.assertTrue(isinstance(self.cash, CashDesk))

    def test_take_money(self):
        self.assertEqual(self.cash.vault, [self.batch, Bill(10)])

    def test_total(self):
        self.assertEqual(self.cash.total(), 390)



if __name__ == '__main__':
    unittest.main()
