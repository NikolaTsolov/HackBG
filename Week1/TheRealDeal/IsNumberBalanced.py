def to_digits(n):
    return [int(x) for x in str(n)]

def is_number_balanced(n):
    digits = to_digits(n)
    if len(digits) % 2 == 1:
        return sum(digits[0:len(digits) // 2]) == sum(digits[len(digits) // 2 + 1:len(digits)])
    else:
        return sum(digits[0:len(digits) // 2]) == sum(digits[len(digits) // 2:len(digits)])

def main():
    print(is_number_balanced(1230))

if __name__ == '__main__':
    main()
