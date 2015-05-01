def iteration_of_nan_expand(expanded):
    count = 1
    index = 0
    if expanded == "":
        return 0
    elif expanded == "Not a NaN":
        return 1
    elif expanded[len(expanded)-9:len(expanded)] == "Not a NaN":
        expanded = expanded[0:len(expanded)-9]
        while index < len(expanded):
            if expanded[index:index+6] == "Not a ":
                count += 1
            index += 6
    else:
        return False
    return count

def main():
    print(iteration_of_nan_expand("Not a Not a Not a Not a NaN"))

if __name__ == '__main__':
    main()
