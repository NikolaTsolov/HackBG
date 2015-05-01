def contains_digit(number,digit):
    resault = False
    string = str(number)
    str_dig = str(digit)
    for index in range(0,len(string)):
        if str_dig == string[index]:
            resault = True
    return resault

def main():
    print(contains_digit(12346789, 5))

if __name__ == '__main__':
    main()
