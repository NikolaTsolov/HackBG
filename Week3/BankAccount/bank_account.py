class BankAccount:
    def __init__(self, name, money, currency):
        if money < 0:
            raise ValueError("Your have to start with a positive amoun of money")

        self.__name = name
        self.__money = money
        self.__currency = currency
        self.__history = []
        self.__add_to_history("Account was created")

    def __add_to_history(self, event):
        self.__history.append(event)

    def holder(self):
        return self.__name

    def currency(self):
        return self.__currency

    def deposit(self, money):
        if money < 0:
            raise ValueError
        self.__money += money
        self.__add_to_history("Deposited {}{}".format(money, self.__currency))

    def balance(self):
        self.__add_to_history("Balance check -> {}{}".format(self.__money, self.__currency))
        return self.__money

    def withdraw(self, amount):
        if self.__money - amount >= 0:
            self.__money -= amount
            self.__add_to_history("{}$ was withdrawed".format(amount))
            return True
        else:
            self.__add_to_history("Withdraw for {}$ failed.".format(amount))
            return False

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.__name, self.__money, self.__currency)

    def __int__(self):
        self.__add_to_history("__int__ check -> {}$".format(self.__money))
        return self.__money

    def transfer_to(self, account, amount):
        if self.__currency == account.__currency and self.__money - amount >= 0:
            account.__money += amount
            self.__money -= amount
            self.__add_to_history("Transfer to {} for {}{}".format(account.__name, amount, account.__currency))
            account.__add_to_history("Transfer from {} for {}{}".format(self.__name, amount, account.__currency))
            return True
        else:
            raise ValueError

    def history(self):
        return self.__history


if __name__ == '__main__':
    main()
