def sum_of_divisors(n):
    resault = 0
    for number in range(1,n+1):
        if n%number == 0:
            resault += number
    return resault

print (sum_of_divisors(1000))
