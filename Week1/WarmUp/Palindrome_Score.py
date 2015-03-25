def palindroms(obj):
	resault = False
	string = str(obj)
	end = len(string)
	for n in range(0,end):
		if string[n] == string[end-n-1]:
			print 
			resault = True
		else:
			return False
			break
		return resault

def reverse_list(obj):
	end = len(obj)
	for i in range(0,end//2):
		new_obj = obj[i]
		obj[i] = obj[end-1]
		obj[end-1] = new_obj
		end -= 1
	return obj

def to_number(digits):

	number = 0

	digits = reverse_list(digits)

	end = len(digits)

	for n in range(0,end):
		number += digits[n] * 10 ** n

	return number

def to_digits(n):

	digits = []
	n = abs(n)
	number = 0

	while True:
		digits.insert(number,n%10)
		number += 1
		n //= 10
		if n == 0:
			break

	end = len(digits)

	digits = reverse_list(digits)

	return digits

def reverse_int(n):

	dig = to_digits(n)
	dig = reverse_list(dig)
	return to_number(dig)

def p_score(n):
	if palindroms(n):
		return 1
	else:
		return 1 + p_score(n+reverse_int(n))

print (p_score(198))