from copy import copy
from pattern import get_pattern_frequencies, get_pattern_from_words
from print import print_dictionary
from math import log2



#
def get_average_information(guess, answers):
	num_answers = len(answers)

	# get the pattern frequencies
	pattern_frequencies = get_pattern_frequencies(guess, answers)

	# get the total amount of information bits
	average_bits = 0
	for index in pattern_frequencies:
		bits = get_bits_of_information(num_answers, pattern_frequencies[index])
		average_bits += (float(pattern_frequencies[index]) / num_answers) * bits

	# calculate average bits
	return average_bits




#
def get_bits_of_information(num_answers_before, num_answers_after):
	ratio = num_answers_before / float(num_answers_after)
	bits = log2(ratio)
	return bits






