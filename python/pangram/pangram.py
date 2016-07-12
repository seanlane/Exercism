def is_pangram(sentence):
	lower = sentence.lower()
	for i in range(26):
		if lower.find(chr(ord('a') + i)) == -1:
			return False
	return True