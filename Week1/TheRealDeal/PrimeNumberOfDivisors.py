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

def prime_number_of_divisors(n):
    count = 0
    for number in range(1, n+1):
        if n % number == 0:
            count += 1
    resault = is_prime(count)
    return resault

def main():
    print (prime_number_of_divisors(9))

if __name__ == '__main__':
    main()
