from copy import deepcopy
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
def get_words_information(guesses, answers, keys, possible_positions):
	letter_frequencies = get_letter_frequencies(answers, keys)
	words_information = {}

	for word in guesses:
		info = calculate_expected_information(word, answers, possible_positions, letter_frequencies)
		words_information[word] = info
	return words_information



#
def calculate_expected_information(word, answers, possible_positions, letter_frequencies):
	information = 0
	for i in range(0, len(word)):
		letter = word[i]
		if i + 1 in possible_positions[letter]:
			information += letter_frequencies[letter]	
		else:
			information = 0
			break	
	return information



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
def get_next_guess(guesses, answers, keys, possible_solutions):
	words_information = get_words_information(guesses, answers, keys, possible_solutions)
	sorted_words = sort_words_by_information(words_information)
	next_guess = sorted_words[0]
	return next_guess
