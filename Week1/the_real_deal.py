from warmup import to_digits, to_number
import copy

def sum_of_divisors(n):
    resault = 0
    for number in range(1, n+1):
        if n % number == 0:
            resault += number
    return resault

def is_prime(n):
    if n <= 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    else:
        for number in range(2, n):
            if n % number == 0:
                return False
            else:
                resault = True
    return resault

def prime_number_of_divisors(n):
    count = 0
    for number in range(1, n+1):
        if n % number == 0:
            count += 1
    return is_prime(count)

def contains_digit(number, digit):
    return str(digit) in str(number)

def contains_digits(number, digits):
    for digit in digits:
        if not contains_digit(number, digit):
            return False
    return True

def is_number_balanced(n):
    digits = to_digits(n)
    if len(digits) % 2 == 1:
        left_side = sum(digits[0:len(digits) // 2])
        right_side = sum(digits[len(digits) // 2 + 1:len(digits)])
        return left_side == right_side
    else:
        left_side = sum(digits[0:len(digits) // 2])
        right_side = sum(digits[len(digits) // 2:len(digits)])
        return left_side == right_side

def count_substrings(heystack, needle):
    return heystack.count(needle)

def zero_insert(n):
    numbers_list = to_digits(n)
    new_numbers_list = to_digits(n)
    count = 1
    for index in range(0, len(numbers_list)-1):
        if numbers_list[index] == numbers_list[index+1]:
            new_numbers_list.insert(index+count, 0)
            count += 1
        elif (numbers_list[index] + numbers_list[index+1]) % 10 == 0:
            new_numbers_list.insert(index+count, 0)
            count += 1
    return to_number(new_numbers_list)

def sum_matrix(m):
    resault = 0
    for item in m:
        for number in item:
            resault += number
    return resault

NEIGHBORS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def is_within(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False
    if at[1] < 0 or at[1] >= len(m[0]):
        return False
    else:
        return True


def bomb(m, at):
    if not is_within(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if is_within(m, position):
            position_value = m[position[dx]][position[dy]]
            m[position[dx]][position[dy]] -= min(target_value, position_value)
    return m

def matrix_bombing_plan(m):
    dictionary = {}
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            new_matrix = bomb(copy.deepcopy(m), (i, j))
            dictionary[(i, j)] = sum_matrix(new_matrix)

    return dictionary


if __name__ == '__main__':
    main()
