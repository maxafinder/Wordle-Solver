from keyboard import get_keys, guess_word
from word_bank import get_answer_bank, get_guess_bank
from next_guess import get_next_guess, eliminate_answers
from board import get_pattern_from_row, get_tiles, is_correct

# Solves the wordle.
# @param driver -> the selenium webdriver that opens Wordle
# @return -> a list where the first element is the correct answer to
#				     the wordle and the second element is the number of guesses
#						 it took to solve the wordle. It returns -1 if it couldn't
#						 solve the wordle in 6 guesses. 
def solve(driver):
	# initialize guesses, answers, and keys
	guesses = get_guess_bank()
	answers = get_answer_bank()
	keys = get_keys(driver)
	print("possible answers left:", str(len(answers)), "\n")

	# guess 6 words
	for i in range(0, 6):
		# calculate the next best guess
		guess = get_next_guess(guesses, answers)

		# guess the word
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

