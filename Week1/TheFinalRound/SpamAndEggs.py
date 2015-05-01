def prepare_meal(n):
    string = ""
    count = 0
    if n % 3 == 0 or n % 5 == 0:
        while n % 3 == 0:
            string += "spam "
            n = n // 3
            count += 1
        while n % 5 == 0:
            if count > 0:
                string += "and "
                count = 0
            string += "eggs "
            n = n // 3
    return string

def main():
    print(prepare_meal(45))

if __name__ == '__main__':
    main()
