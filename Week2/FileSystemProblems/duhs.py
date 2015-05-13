import os
import sys
from cat import has_enaugh_inputs

class FileNotFoundError(Exception):
    pass

def main():
    if has_enaugh_inputs(1):
        resault = []
        path = sys.argv[1]
        for dirpaths, dirnames, filenames in os.walk(path):
            for file_name in filenames:
                try:
                    full_path = os.path.join(dirpaths, file_name)
                    resault.append(os.path.getsize(full_path))
                except:
                    print("FileNotFoundError")
        print(sum(resault) * (10 ** -9))
    else:
        print("Not enaugh inputs")

if __name__ == '__main__':
    main()
