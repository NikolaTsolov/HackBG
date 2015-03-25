def reverse_list(obj):
	end = len(obj)
	for i in range(0,end//2):
		new_obj = obj[i]
		obj[i] = obj[end-1]
		obj[end-1] = new_obj
		end -= 1
	return obj

def fibonachi(n):
	if n == 1:
		resault = [1]
	elif n == 2:
		resault = [1,1]
	else:
		resault = [1,1]
		for number in range(0,n-2):
			resault.insert(number+2,resault[number]+resault[number+1])
	return resault

def fib_number (n):
	fib = fibonachi(n)
	end = len(fib)
	fib = reverse_list(fib)
	number = 0

	for i in range(0,end):
		number += fib[i] * 10 ** i

	return number

print (fib_number(10))
