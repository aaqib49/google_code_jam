''' This script prints the alien number after converting from source language to target language

Usage:
	solution.py <n> <s> <t>
'''

from docopt import docopt


def run(num, source, target):
	value = get_source_val(num, source)
	result = get_target_num(value, target)


def get_source_val(num, source):
	embeddings = {}
	for c, character in enumerate(source):
		embeddings[character] = c

	value = 0
	for c, character in enumerate(num[::-1]):
		value += embeddings[character] * (len(source) ** c)
	print ("value:",  value)
	return value


def get_target_num(value, target):
	target_embeddings = {}
	for c, character in enumerate(target):
		target_embeddings[str(c)] = character
	n_digits = 0
	len_t = len(target)
	while value >= len_t**(n_digits):
		n_digits += 1

	target_num = {}
	for i in range(n_digits):
		for j in range(len_t):
			remaining_value = j * (len_t ** (n_digits - i - 1))
			if value > remaining_value:
				target_num[i] = j
			elif value == remaining_value:
				target_num[i] = j
				value -= remaining_value
				break
			elif value < remaining_value:
				value -= (j-1) * (len_t ** (n_digits - i - 1))
				break
			if j == (len_t - 1):
				value -= remaining_value
	
	target_str = ""
	for i in range(len(target_num)):
		target_str += target_embeddings[str(target_num[i])]
	print("target_str: ", target_str)
	return target_str


if __name__ == '__main__':
	arguments = docopt(__doc__)
	print(arguments)

	if arguments['<n>']:
		num = arguments['<n>']
	if arguments['<s>']:
		source = arguments['<s>']
	if arguments['<t>']:
		target = arguments['<t>']
	run(str(num), str(source), str(target))
