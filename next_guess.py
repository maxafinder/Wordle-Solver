from information import get_average_information
from pattern import get_pattern_from_words, compare_patterns


# Eliminates answers that are not possible from a list of answers
# based on the pattern that was revealed from a guess.
# @param guess -> the word that was guessed.
# @param pattern -> the pattern that was revealed from "guess".
# @param answers -> the list of answers that are still possible.
# @return -> the list of answers after eliminating ones that aren't possible.
def eliminate_answers(guess, pattern, answers):
	new_answers = []

	# check to see if answer gives us the same pattern against "guess"
	for a in answers:
		p = get_pattern_from_words(guess, a)
		if compare_patterns(pattern, p):
			new_answers.append(a)
	return new_answers


# Sorts words by average information gained against the answers left.
# @param words_avg_information -> a dictionary that maps each word to the average bits
# 																of information gained against the answers left.
# @return -> a list of words sorted from greatest to least in terms of average
# 					 information gained.
def sort_words_by_information(words_avg_information):
	sorted_words = []
	for word in words_avg_information:
		insert_index = 0
		for i in range(0, len(sorted_words)):
			insert_index = i
			if words_avg_information[sorted_words[i]] < words_avg_information[word]:
				break
			elif i == len(sorted_words) - 1:
				insert_index += 1
		sorted_words.insert(insert_index, word)
	return sorted_words


# Finds the next best guess based on the possible answers left.
# @param guesses -> the list of guesses that are valid guesses.
# @param answers -> a list of answers that are still possible.
# @return -> the word that has the highest expected bits of information.
def get_next_guess(guesses, answers):
	# if last answer
	if len(answers) == 1:
		print("Guessing answer:")
		return answers[0]

	# this algorithm found that "soare" has the highest amount of expected
	# information as a first guess and this holds true as long as the bank of words
	# for possible guesses and answers doesn't change, so as an optimization it
	# automatically guesses "soare" as the first word without calculating it every time.
	if len(answers) == 2309: # this is the first guess
		print("Top 5 next guesses:")
		print("soare 5.885202744292757")
		print("roate 5.884856313732008")
		print("raise 5.878302956493168")
		print("reast 5.867738020843561")
		print("raile 5.865153829041269")
		return "soare"

	average_info_bits = {}
	for g in guesses:
		avg_info = get_average_information(g, answers)
		average_info_bits[g] = avg_info
	sorted_words = sort_words_by_information(average_info_bits)
	print("Top 5 next guesses:")
	for i in range(0, 5):
		print(sorted_words[i], average_info_bits[sorted_words[i]])
	return sorted_words[0]

