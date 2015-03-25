def is_decreasing(seq):
	length = len(seq)
	if end == 1:
		resault = True
	else:
		for index in range(0,length-1):
			if seq[index] > seq[index+1]:
				resault = True
			else:
				resault = False
				break
	return resault
		
print (is_decreasing([1,1,1]))