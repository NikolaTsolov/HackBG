def fibonacci(n):
    if n == 1:
        resault = [1]
    elif n == 2:
        resault = [1,1]
    else:
        resault = [1,1]
        for number in range(0,n-2):
            resault.insert(number+2,resault[number]+resault[number+1])
    return resault

def main():
    print (fibonacci(3))

if __name__ == "__main__":
    main()
