import unittest
from bank_account import BankAccount

class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.my_account = BankAccount("Rado", 0, "$")

    def test_new_bank_account_consturctor(self):
        self.assertTrue(isinstance(self.my_account, BankAccount))
        self.assertEqual(self.my_account.name, "Rado")
        self.assertEqual(self.my_account.money, 0)
        self.assertEqual(self.my_account.currency, "$")

    def test_balance_chek(self):
        self.assertEqual(self.my_account.balance(), self.my_account.money)

    def test_deposit(self):
        self.my_account.deposit(1000)
        self.assertEqual(self.my_account.money, 1000)
        with self.assertRaises(ValueError):
            self.my_account.deposit(-1000)

    def test_withdraw(self):
        self.my_account.money = 50
        self.assertTrue(self.my_account.withdraw(50) == True)
        self.assertTrue(self.my_account.withdraw(50) == False)

    def test_int_cast(self):
        self.assertEqual(int(self.my_account), 0)

    def test_str_cast(self):
        self.assertEqual(str(self.my_account), "Bank account for Rado with balance of 0$")

    def test_transfer_to(self):
        other_account = BankAccount("Ivo", 0, "$")
        self.my_account.money = 500
        self.assertEqual(self.my_account.currency, other_account.currency)
        self.my_account.transfer_to(other_account, 500)
        self.assertEqual(other_account.money, 500)
        self.assertEqual(self.my_account.money, 0)
        with self.assertRaises(ValueError):
            self.my_account.transfer_to(other_account, 500)
        other_account.currency = "BGR"
        self.my_account.money = 500
        with self.assertRaises(ValueError):
            self.my_account.transfer_to(other_account, 500)

    def test_history(self):
        arr = []
        other_arr = []
        arr.append("Account was created")
        self.my_account.deposit(1000)
        arr.append("Deposited 1000$")
        arr.append("Balance check -> 1000$")
        self.my_account.balance()
        int(self.my_account)
        arr.append("__int__ check -> 1000$")
        self.my_account.withdraw(500)
        arr.append("500$ was withdrawed")
        self.my_account.balance()
        arr.append("Balance check -> 500$")
        self.my_account.withdraw(1000)
        arr.append("Withdraw for 1000$ failed.")
        other_account = BankAccount("Ivo", 0, "$")
        other_arr.append("Account was created")
        self.my_account.money = 1000
        self.my_account.transfer_to(other_account, 500)
        arr.append("Transfer to Ivo for 500$")
        other_arr.append("Transfer from Rado for 500$")
        self.assertEqual(self.my_account.history(), arr)
        self.assertEqual(other_account.history(), other_arr)







if __name__ == '__main__':
    unittest.main()
