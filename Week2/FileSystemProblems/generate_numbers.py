import sys
from random import randint
from cat import has_enaugh_inputs

def write_file(filename, contents):
    text_file = open(filename, "w")
    text_file.write(" ".join(contents))
    text_file.close


def generate_numbers(filename, n):
    contents = []
    for index in range(0, int(n)):
        contents.append(str(randint(0, 1000)))
    write_file(filename, contents)

def main():
    if has_enaugh_inputs(2):
        generate_numbers(sys.argv[1], sys.argv[2])
    else:
        print("Not enaugh inputs")

if __name__ == '__main__':
    main()
