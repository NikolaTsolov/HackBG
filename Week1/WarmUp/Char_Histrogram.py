def char_histogram(string):
	end = len(string)
	dictionary = {}
	for number in range(0,end):
		dictionary[string[number]] = 0

	for number in range(0,end):
		dictionary[string[number]] += 1

	return dictionary

print (char_histogram("AAAaaa!!!"))