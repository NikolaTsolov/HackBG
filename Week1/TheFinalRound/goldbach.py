def is_prime(n):

    if n == 1:
        return False
    if n < 0:
        return False
    if n == 2:
        return True
    else:
        for number in range(2, n):
            if n % number == 0:
                resault = False
                break
            else:
                resault = True
    return resault

def goldbach(n):
    tupl = ()
    arr = []
    for number in range(2, n//2+1):
        if is_prime(number) and is_prime(n-number):
            tupl = (number, n - number)
            arr.append(tupl)
    tupl = ()
    return arr

def main():
    print(goldbach(100))

if __name__ == '__main__':
    main()

