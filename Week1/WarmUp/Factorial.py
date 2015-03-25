def factorial(n):
    resault = 1
    for number in range(1, n + 1):
        resault *= number
    return resault

def main():
    print (factorial(4))

if __name__ == '__main__':
    main()
