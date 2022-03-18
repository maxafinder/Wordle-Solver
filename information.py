from pattern import get_pattern_frequencies 
from math import log2


# Gets the expected amount of information in the form of "bits of information"
# that we would expect to gain from a guess given a set of answers.
# @param guess -> the word that we want to find the expected amount of information for.
# @param answers -> a list of words that can still be answers.
# @return -> the average information gained for the guess against all answers.
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


# Converts the number of answers before and after into the unit of "bits of information" gained.
# Ex. if we divide the answer space by a facter of 4, then that is 2 bits of information.
# @param num_answers_before -> the number of answers before the guess.
# @param num_answers_after -> the number of answers after the guess.
# @return -> the information gained in units of bits.
def get_bits_of_information(num_answers_before, num_answers_after):
	ratio = num_answers_before / float(num_answers_after)
	bits = log2(ratio)
	return bits

