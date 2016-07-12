def rna_char(char_in):
	if char_in is 'A':
		return 'U'
	elif char_in is 'C':
		return 'G'
	elif char_in is 'G':
		return 'C'
	elif char_in is 'T':
		return 'A'
	else:
		print "Error, received '%s'" % char_in 

def to_rna(sequence):
	result = ""
	for i in range(len(sequence)):
		result += rna_char(sequence[i])
	return result
