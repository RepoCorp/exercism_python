#Hamming exercism

def distance(str1, str2):
	dist = 0
	zipped = zip(str1, str2)
	for i, j in zipped:
		if i != j:
			dist += 1
	return dist
