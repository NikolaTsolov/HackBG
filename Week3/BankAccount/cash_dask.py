class Bill:
    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return int(self.amount)

    def __str__(self):
#return "A {}$ bill".format(self.amount)
        return str(self.amount)

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
        index = 0
        arr = []
        count = 1
        print("We have a total of {}$ in the desk".format(self.total()))
        print("We have the following count of bills, sorted in ascending order:")
        for item in self.vault:
            if len(item) == 1:
                arr.append(int(item))
            else:
                for money in item:
                    arr.append(int(money))
        arr = sorted(arr)
        while index < len(arr)-1:
            while index < len(arr)-1 and arr[index] == arr[index+1]:
                count += 1
                index += 1
            print("{}$ bills - {}".format(arr[index], count))
            index += 1
            count = 1




def main():

    a = Bill(10)
    b = Bill(5)
    c = Bill(10)

    int(a) == 10
    str(a) == "A 10$ bill"
    print(a)
    # A 10$ bill

    a == b
    # False
    a == c
    # True

    money_holder = {}

    money_holder[a] = 1
    #    We have one 10% bill

    if c in money_holder:
        money_holder[c] += 1

    print(money_holder)
    # { "A 10$ bill": 2 }

    values = [10, 20, 50, 100]
    bills = [Bill(value) for value in values]

    batch = BillBatch(bills)

    print(batch.total())

    print(len(batch))

    for bill in batch:
        print(bill)

    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BillBatch(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total())
    # 390
    desk.inspect()

if __name__ == '__main__':
    main()
