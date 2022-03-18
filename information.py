from copy import copy
from platform import java_ver
from next_guess import eliminate_answers
from pattern import get_pattern_from_words
from print import print_dictionary
from math import log2



#
def get_average_information(guess, answers):
	# get the total amount of information bits
	total_information_bits = 0
	for solution in answers:
		information_bits = get_bits_of_information(guess, answers, solution)
		total_information_bits += information_bits

	# calculate average information bits
	average_information_bits = float(total_information_bits) / len(answers)
	return average_information_bits



#
def get_bits_of_information(guess, answers, solution):
	# find how many answers the resulting pattern would eliminate
	answers_before = len(answers)

	pattern = get_pattern_from_words(guess, solution)
	answers = eliminate_answers(guess, pattern, answers)

	answers_after = len(answers)
	ratio = answers_before / float(answers_after)
	bits = log2(ratio)
	return bits






