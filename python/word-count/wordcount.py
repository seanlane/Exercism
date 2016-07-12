from collections import defaultdict
import re

def word_count(sentence):
	lower = sentence.lower()
	words = re.split("[\W_]+", lower, flags=re.UNICODE)
	counts = defaultdict(int)
	for word in words:
		if word == '':
			continue
		counts[word] += 1
	return counts