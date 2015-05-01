def count_substrings(heystack, needle):
    return heystack.count(needle)

def is_an_bn(word):
    if len(word) % 2 == 0:
        left_side = count_substrings(word[0:len(word)//2], 'a')
        right_side = count_substrings(word[len(word)//2:len(word)], 'b')
        if left_side == right_side and left_side == len(word)//2 or word == "":
            return True
    return False

def main():
    print (is_an_bn("aaaaabbbbb"))

if __name__ == '__main__':
    main()
