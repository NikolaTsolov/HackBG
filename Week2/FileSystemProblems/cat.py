import sys

def read_file(filename):
    text_file = open(filename, "r")
    reader = text_file.read()
    text_file.close
    return reader

def has_enaugh_inputs(count):
    return len(sys.argv[1:]) >= count


def  main():
    if has_enaugh_inputs(1):
        contend = []
        for filename in sys.argv[1:]:
            contend.append(read_file(filename))
        print("\n".join(contend))
    else:
        print("Not enaugh input")


if __name__ == '__main__':
    main()
