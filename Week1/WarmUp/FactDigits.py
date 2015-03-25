def factorial(n):
    resault = 1
    for number in range(1, n+1):
        resault *= number
    return resault

def to_digits(n):
    return [int(item) for item in str(n)]

def fact_digits(n):
    n = abs(n)
    return sum(factorial(item) for item in to_digits(n))

def main():
    print (fact_digits(999))
if __name__ == '__main__':
    main()
