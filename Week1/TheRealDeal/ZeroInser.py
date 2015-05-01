def to_digits(n):
    return [int(x) for x in str(n)]

def count_digits(n):
    return sum(1 for x in to_digits(n))

def to_number(digits):
    resault = 0
    for digit in digits:
        resault = resault * (10 ** count_digits(digit)) + digit
    return resault

def zero_insert(n):
    arr = to_digits(n)
    new_arr = to_digits(n)
    count = 1
    for index in range(0, len(arr)-1):
        if arr[index] == arr[index+1]:
            new_arr.insert(index+count, 0)
            count += 1
        elif (arr[index] + arr[index+1]) % 10 == 0:
            new_arr.insert(index+count, 0)
            count += 1
    return to_number(new_arr)


def main():
    print(zero_insert(116457))

if __name__ == '__main__':
    main()
