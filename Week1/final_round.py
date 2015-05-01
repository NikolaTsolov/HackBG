from the_real_deal import count_substrings
from warmup import to_digits
from the_real_deal import is_prime
import calendar

def count_words(words):
    return {key: words.count(key) for key in words}

def unique_words_count(words):
    return len(set(words))

def nan_expend(times):
    string = ""
    if times >= 1:
        string = "Not a NaN"
        for number in range(1, times):
            string = "Not a " + string
    return string

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
            else:
                return False
            index += 6
    else:
        return False
    return count

def integer_prime_factorization(n):
    tupl = ()
    count = 0
    number = 2
    resauld = []
    while n != 1:
        if n % number == 0:
            while n % number == 0:
                count += 1
                n = n // number
            tupl = (number, count)
        count = 0
        if tupl != ():
            resauld.append(tupl)
            tupl = ()
        number += 1
    return resauld

def same_items(items):
    first = items[0]
    index = 1
    resauld = [first]
    while index < len(items) and items[index] == first:
        resauld.append(items[index])
        index += 1
    return resauld

def group(items):
    resauld = []
    new_group = []
    while len(items) != 0:
        new_group = same_items(items)
        items = items[len(new_group):]
        resauld.append(new_group)
    return resauld

def max_consecutive(items):
    max_count = 0
    while len(items) != 0:
        new_group = same_items(items)
        items = items[len(new_group):]
        if max_count < len(new_group):
            max_count = len(new_group)
    return max_count

def groupby(func, seq):
    diction = {}
    for item in seq:
        if func(item) in diction:
            diction[func(item)].append(item)
        else:
            diction[func(item)] = [item]
    return diction

def prepare_meal(n):
    string = ""
    count = 0
    if n % 3 == 0 or n % 5 == 0:
        while n % 3 == 0:
            n = n // 3
            count += 1
        string += " ".join(["spam" for i in range(0, count)])
        if n % 5 == 0:
            string += " ".join(["eggs" if count == 0 else " and eggs"])
    return string

def reduce_file_path(path):
    reduced_path = []
    parts = [part for part in path.split("/") if part != "" and part != "."]
    while len(parts) != 0:
        part = parts.pop()
        if part == "..":
            if len(parts) != 0:
                parts.pop()
        else:
            reduced_path.insert(0, part)
    return "/" + "/".join(reduced_path)

def is_an_bn(word):
    if len(word) % 2 == 0:
        left_side = count_substrings(word[0:len(word)//2], 'a')
        right_side = count_substrings(word[len(word)//2:len(word)], 'b')
        if left_side == right_side and left_side == len(word)//2 or word == "":
            return True
    return False

def is_credit_card_valid(number):
    arr = to_digits(number)
    if len(arr) % 2 == 1:
        index = len(arr)
        while index != 0:
            if index % 2 == 0:
                arr[index] *= 2
            index -= 1
        resault = sum(arr)
        return resault % 10 == 0
    return False

def goldbach(n):
    tupl = ()
    arr = []
    for number in range(2, n//2+1):
        if is_prime(number) and is_prime(n-number):
            tupl = (number, n - number)
            arr.append(tupl)
    tupl = ()
    return arr

def magic_square(matrix):
    row_sum = 0
    colum_sum = 0
    f_diagonal = 0
    b_diagonal = 0
    for i in range(0, len(matrix) - 1):
        if sum(matrix[i]) != sum(matrix[i+1]):
            return False
        row_sum = sum(matrix[i])
    for i in range(0, len(matrix) - 1):
        if sum([row[i] for row in matrix]) != sum([row[i+1] for row in matrix]):
            return False
        colum_sum = sum([row[i] for row in matrix])
    if row_sum != colum_sum:
        return False
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i == j:
                f_diagonal += matrix[i][j]
            if (i + j) == len(matrix[i]) - 1:
                b_diagonal += matrix[i][j]
    if row_sum != f_diagonal or row_sum != b_diagonal:
        return False
    return True

def friday_years(start, end):
    friday_index = 4
    count_friday_years = 0
    for year in range(start, end):
        friday_in_this_year = 0
        for month in range(1, 13):
            this_month = calendar.monthcalendar(year, month)
            for week in this_month:
                if week[friday_index] != 0:
                    friday_in_this_year += 1
        if friday_in_this_year == 53:
            count_friday_years += 1
    return count_friday_years




if __name__ == '__main__':
    main()
