from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from driver import get_driver
from information import get_average_information
from letter import get_possbile_letter_positions_after_guess, initialize_possible_positions
from next_guess import eliminate_answers 
from pattern import get_pattern_from_words, get_pattern_frequencies, get_index_patterns
from solve import solve
from print import print_dictionary
from word_bank import get_answer_bank
from keyboard import get_keys


if __name__ == "__main__":

	# open driver
	driver = get_driver()
	if driver == -1:
		print("ERROR: Problem starting driver")
		exit()
	elif driver == -2:
		exit()
	driver.get("https://www.nytimes.com/games/wordle/index.html")


	# get the keys for testing
	keys = get_keys(driver)


	# Test information calculations
	answers = get_answer_bank()

	# Do patterns determine which answers to eliminate
	#guess = "crane"
	#for i in range(0, 1):
		#a = answers[i]	
		#print(guess)
		#print(a)
		#possible_positions = initialize_possible_positions(keys)
		#pattern = get_pattern_from_words(guess, a)
		#print(pattern)
		#print("---------------")
		#possible_positions = get_possbile_letter_positions_after_guess(guess, pattern, possible_positions)
		#new_answers = eliminate_answers(guess, pattern, answers, possible_positions)
		#new_answers = new_eliminate_answers(guess, pattern, answers)
		#for ans in new_answers:
			#ans_pattern = get_pattern_from_words(guess, ans)
			#print(ans, "===", ans_pattern)
	#print("\n\n")


	# Test pattern frequencies
	#f = get_pattern_frequencies("hello", answers)
	#print_dictionary(f)


	# Solve
	answer = solve(driver)
	if answer != -1:
		print("\nCorrect Answer:", answer[0], "\nSolved in", answer[1], "guesses.\n")
	else:
		print("\nWasn't able to solve.\n")

	# close the webdriver
	driver.quit()

