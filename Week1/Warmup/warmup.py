def factorial(n):
    resault = 1
    for number in range(1, n + 1):
        resault *= number
    return resault

def fibonacci(n):
    if n == 1:
        resault = [1]
    elif n == 2:
        resault = [1, 1]
    else:
        resault = [1, 1]
        for number in range(0, n-2):
            resault.insert(number+2, resault[number]+resault[number+1])
    return resault

def to_digits(n):
    return [int(item) for item in str(n)]

def sum_of_digits(n):
    n = abs(n)
    return sum(to_digits(n))

def fact_digits(n):
    n = abs(n)
    return sum(factorial(item) for item in to_digits(n))

def palindrome(obj):
    string = str(obj)
    resault = string[::-1] == string
    return resault

def reverse_list(obj):
    end = len(obj)
    for index in range(0, end//2):
        new_obj = obj[index]
        obj[index] = obj[end-1]
        obj[end-1] = new_obj
        end -= 1
    return obj

def to_number(digits):
    resault = 0
    digits = reverse_list(digits)
    end = len(digits)
    for index in range(0, end):
        resault += digits[index] * 10 ** index
    return resault

def fib_number (n):
    string = ""
    fib = fibonacci(n)
    for item in fib:
        string += str(item)
    return int(string)

def count_vowels(string):
    vowels = "aeiouyAEIOUY"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def count_consontants(string):
    consontants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTWXZ"
    count = 0
    for char in string:
        if char in consontants:
            count += 1
    return count

def char_histogram(string):
    dictionary = {}
    for char in string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

def reverse_int(n):
    string = str(n)
    return int(string[::-1])

def p_score(n):
    if palindrome(n):
        return 1
    else:
        return 1 + p_score(n + reverse_int(n))

def is_decreasing(seq):
    if len(seq) == 1:
        resault = True
    else:
        for index in range(0, len(seq)-1):
            if seq[index] > seq[index+1]:
                resault = True
            else:
                resault = False
                break
    return resault

def is_increasing(seq):
    if len(seq) == 1:
        resault = True
    else:
        for index in range(0, len(seq) - 1):
            if seq[index] < seq[index+1]:
                resault = True
            else:
                resault = False
                break
    return resault

def next_hack(n):
    count = 0
    number = n
    while True:
        number += 1
        binary = str(bin(number)[2:])
        if palindrome(binary):
            for char in binary:
                if char == '1':
                    count += 1
            if count % 2 == 1:
                return number
        count = 0



if __name__ == '__main__':
    main()
