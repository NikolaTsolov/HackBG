def is_increasing(seq):
	end = len(seq)
	if end == 1:
		resault = True
	else:
		for indexin range(0,end-1):
			if seq [index] < seq [index+1]:o
				resault = True
			else:
				resault = False
				break
	return resault

print (is_increasing([1,2,3,4,5,6,7,8]))
