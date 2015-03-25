def next_hack(n):
    count = 0
    while True:
        n += 1
        binary = bin(n)[2:]
        binary = str (binary)
        if binary == binary[::-1]:
            for item in binary:
                if item == '1':
                    count += 1
            if count % 2 == 1:
                return n
        count = 0

def main():
    print(next_hack(7))

if __name__ == '__main__':
    main()
