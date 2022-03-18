from copy import copy, deepcopy
from information import get_average_information, get_bits_of_information
from keyboard import get_keys, guess_word
from letter import get_possbile_letter_positions_after_guess, initialize_possible_positions
from print import print_dictionary
from word_bank import get_answer_bank, get_guess_bank
from next_guess import get_next_guess, eliminate_answers
from board import get_pattern_from_row, get_tiles, is_correct

#
def solve(driver):
	# initialize guesses, answers, and keys
	guesses = get_guess_bank()
	answers = get_answer_bank()
	keys = get_keys(driver)

	print("possible answers left:", str(len(answers)), "\n")


	# guess 6 words
	for i in range(0, 6):

		# get next guess and guess it
		guess = get_next_guess(guesses, answers)
		print("guessing:", guess)
		guess_word(keys, guess)

		# get information about the pattern on the last guess
		keys = get_keys(driver)
		tiles = get_tiles(driver)
		pattern = get_pattern_from_row(tiles[i])
		print(guess, "->", str(pattern))
		
		# if answer is correct
		if is_correct(pattern):
			return [guess, i + 1] # number of attempts it took to solve

		# get the answers that are still possible
		answers = eliminate_answers(guess, pattern, answers)
		print("possible answers left:", str(len(answers)), "\n")

	return -1 # didn't solve





