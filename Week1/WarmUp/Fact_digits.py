def factorial(n):
	resault = 1
	for number in range(1, n+1):
		resault *= number
	return resault
def fact_digits(n):
	resault = 0
	n = abs(n)
	while True:
		resault += factorial(n%10)
		n //= 10
		if n == 0:
			break
	return resault	

print (fact_digits(999))