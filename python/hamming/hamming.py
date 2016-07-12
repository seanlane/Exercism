def distance(stringA, stringB):
	count = 0
	
	for i in range(len(stringA)):
		if stringA[i] is not stringB[i]:
			count += 1
	return count