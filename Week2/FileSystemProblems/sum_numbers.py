import sys
from cat import read_file, has_enaugh_inputs

def sum_numbers(filename):
    reader = read_file(filename)
    content = [int(number) for number in reader.split(" ")]
    print(content)
    return sum(content)

def main():
    if has_enaugh_inputs(1):
        print(sum_numbers(sys.argv[1]))
    else:
        print("Not enaugh inputs")

if __name__ == '__main__':
    main()
