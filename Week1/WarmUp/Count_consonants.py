def count_consonants(string):
	end = len(string)
	counter = 0

	for number in range(0,end):
		if string[number] == 'B' or string[number] == 'b' or string[number] == 'C' or string[number] == 'c':
			counter += 1
		if string[number] == 'D' or string[number] == 'd' or string[number] == 'F' or string[number] == 'f':
			counter += 1
		if string[number] == 'G' or string[number] == 'g' or string[number] == 'H' or string[number] == 'h':
			counter += 1
		if string[number] == 'J' or string[number] == 'j' or string[number] == 'K' or string[number] == 'k':
			counter += 1
		if string[number] == 'L' or string[number] == 'l' or string[number] == 'M' or string[number] == 'm':
			counter += 1
		if string[number] == 'N' or string[number] == 'n' or string[number] == 'P' or string[number] == 'p':
			counter += 1
		if string[number] == 'Q' or string[number] == 'q' or string[number] == 'R' or string[number] == 'r':
			counter += 1
		if string[number] == 'S' or string[number] == 's' or string[number] == 'T' or string[number] == 't':
			counter += 1
		if string[number] == 'V' or string[number] == 'v' or string[number] == 'W' or string[number] == 'w':
			counter += 1
		if string[number] == 'X' or string[number] == 'x' or string[number] == 'Z' or string[number] == 'z':
			counter += 1

	return counter

print (count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
