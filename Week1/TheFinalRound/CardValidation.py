def to_digits(n):
    return [int(x) for x in str(n)]

def is_credit_card_valid(number):
    arr = to_digits(number)
    if len(arr) % 2 == 1:
        index = len(arr)
        while index != 0:
            if index % 2 == 0:
                arr[index] *= 2
            index -= 1
        resault = sum(arr)
        return resault % 10 == 0

def main():
    print(is_credit_card_valid(79927398715))

if __name__ == '__main__':
    main()
