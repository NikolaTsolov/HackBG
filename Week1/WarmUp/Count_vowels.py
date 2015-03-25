def count_vowels(string):
	end = len(string)
	counter = 0

	for number in range(0,end):
		if string[number] == 'A' or string[number] == 'a':
			counter += 1
		if string[number] == 'E' or string[number] == 'e':
			counter += 1
		if string[number] == 'I' or string[number] == 'i':
			counter += 1
		if string[number] == 'O' or string[number] == 'o':
			counter += 1
		if string[number] == 'U' or string[number] == 'u':
			counter += 1
		if string[number] == 'Y' or string[number] == 'y':
			counter += 1

	return counter

print (count_vowels("A nice day to code!"))