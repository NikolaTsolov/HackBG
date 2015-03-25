def to_digits(n):
    return [int(item) for item in str(n)]
def sum_of_digits(n):
    n = abs(n)
    return sum(to_digits(n))

def main():
    print (sum_of_digits(-10))

if __name__ == '__main__':
    main()
