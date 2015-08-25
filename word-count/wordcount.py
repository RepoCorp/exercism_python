#Word count exercism 


def word_count(phrase):
	word_list = phrase.split()
	dict = {}
	for element in word_list:
		dict[element] = dict.get(element, 0) + 1
	return dict