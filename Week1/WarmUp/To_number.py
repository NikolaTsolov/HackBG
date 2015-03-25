def reverse_list(obj):
    end = len(obj)
    for i in range(0, end//2):
        new_obj = obj[i]
        obj[i] = obj[end-1]
        obj[end-1] = new_obj
        end -= 1
    return obj

def to_number(digits):

    number = 0

    digits = reverse_list(digits)

    end = len(digits)

    for n in range(0, end):
        number += digits[n] * 10 ** n
    return number

print (to_number([1, 2, 3, 0, 2, 3]))
