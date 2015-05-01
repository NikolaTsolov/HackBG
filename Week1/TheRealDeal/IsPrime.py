def is_prime(n):

    if n == 1:
        return False
    if n < 0:
        return False
    if n == 2:
        return True
    else:
        for number in range(2,n):
            if n % number == 0:
                resault = False
                break
            else:
                resault = True
    return resault

def main():
    print (is_prime(-11))

if __name__ == '__main__':
    main()
