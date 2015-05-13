class BankAccount:
    def __init__(self, name, money, currency):
        self.name = name
        self.money = money
        self.currency = currency
        self.history_list = ["Account was created"]

    def deposit(self, money):
        if money < 0:
            raise ValueError
        self.money += money
        self.history_list.append("Deposited {}$".format(self.money))

    def balance(self):
        self.history_list.append("Balance check -> {}$".format(self.money))
        return self.money

    def withdraw(self, amount):
        if self.money - amount >= 0:
            self.money -= amount
            self.history_list.append("{}$ was withdrawed".format(amount))
            return True
        else:
            self.history_list.append("Withdraw for {}$ failed.".format(amount))
            return False

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.money, self.currency)

    def __int__(self):
        self.history_list.append("__int__ check -> {}$".format(self.money))
        return self.money

    def transfer_to(self, account, amount):
        if self.currency == account.currency and self.money - amount >= 0:
            account.money += amount
            self.money -= amount
            self.history_list.append("Transfer to {} for {}{}".format(account.name, amount, account.currency))
            account.history_list.append("Transfer from {} for {}{}".format(self.name, amount, account.currency))
            return True
        else:
            raise ValueError

    def history(self):
        return self.history_list


if __name__ == '__main__':
    main()
