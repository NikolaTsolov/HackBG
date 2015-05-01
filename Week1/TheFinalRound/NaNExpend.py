def nan_expend(times):
    string = ""
    if times >= 1:
        string = "Not a NaN"
        for number in range(1, times):
            string = "Not a " + string
    return string

def main():
    print(nan_expend(0))

if __name__ == '__main__':
    main()
