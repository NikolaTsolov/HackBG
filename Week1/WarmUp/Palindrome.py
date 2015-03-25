def palindroms(obj):
    string = str(obj)
    resault = string[::-1] == string
    return resault

def main():
    print (palindroms(121))

if __name__ == '__main__':
    main()
