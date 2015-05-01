def contains_digit(number, digit):
    resault = False
    string = str(number)
    str_dig = str(digit)
    for index in range(0, len(string)):
        if str_dig == string[index]:
            resault = True
    return resault

def contains_digits(number, digits):
    for digit in digits:
        if not contains_digit(number, digit):
            return False
        return True

def main():
    print(contains_digits(40213, [0, 4, 3]))

if __name__ == '__main__':
    main()

