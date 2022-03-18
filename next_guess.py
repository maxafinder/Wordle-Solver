from copy import deepcopy
from information import get_average_information
from letter import get_letter_frequencies
from pattern import get_pattern_from_words, compare_patterns
from print import print_dictionary



#
def eliminate_answers(guess, pattern, answers):
	new_answers = []

	# check to see if answer gives us the same pattern against "guess"
	for a in answers:
		p = get_pattern_from_words(guess, a)
		if compare_patterns(pattern, p):
			new_answers.append(a)
	return new_answers



#
def sort_words_by_information(words_information):
	sorted_words = []
	for word in words_information:
		insert_index = 0
		for i in range(0, len(sorted_words)):
			insert_index = i
			if words_information[sorted_words[i]] < words_information[word]:
				break
			elif i == len(sorted_words) - 1:
				insert_index += 1
		sorted_words.insert(insert_index, word)
	return sorted_words



#
def get_next_guess(guesses, answers):
	average_info_bits = {}
	for g in guesses:
		avg_info = get_average_information(g, answers)
		average_info_bits[g] = avg_info
	sorted_words = sort_words_by_information(average_info_bits)
	print("Top 5 next guesses:")
	for i in range(0, 5):
		print(sorted_words[i], average_info_bits[sorted_words[i]])
	return sorted_words[0]
