def sum_matrix(m):
    resault = 0
    for item in m:
        for somthing in item:
            resault += somthing
    return resault

def main():
    print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))

if __name__ == '__main__':
    main()
