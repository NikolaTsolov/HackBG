class Bill:
    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return int(self.amount)

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

    def __len__(self):
        return 1

class BillBatch:
    def __init__(self, bills):
        self.bills = []
        for item in bills:
            self.bills.append(item)

    def __len__(self):
        return len(self.bills)

    def __int__(self):
        return self.total()

    def total(self):
        resault = []
        for item in self.bills:
            resault.append(int(item))
        return sum(resault)

    def __getitem__(self, index):
        return self.bills[index]

class CashDesk:
    def __init__(self):
        self.vault = []

    def take_money(self, money):
        self.vault.append(money)

    def total(self):
        total_sum = 0
        for item in self.vault:
            total_sum += int(item)
        return total_sum

    def inspect(self):
        bills_list = []
        conteiner = {}
        print("We have a total of {}$ in the desk".format(self.total()))
        print("We have the following count of bills, sorted in ascending order:")
        if slef.total > 0:
            for bills in self.vault:
                if len(bills) == 1:
                    bills_list.append(self.bills)
                else:
                    for bill in bills:
                        bills_list.append(bill)
            for bill in bills_list:
                if


        print("{}$ bills - {}".format(arr[index], count))



if __name__ == '__main__':
    main()
