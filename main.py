from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from driver import get_driver
from information import get_average_information
from letter import get_possbile_letter_positions_after_guess, initialize_possible_positions
from next_guess import eliminate_answers , sort_words_by_information
from pattern import get_pattern_from_words, get_pattern_frequencies, get_index_patterns
from solve import solve
from print import print_dictionary
from word_bank import get_answer_bank, get_guess_bank
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


	## get the keys for testing
	#keys = get_keys(driver)


	## Test information calculations
	#answers = get_answer_bank()
	#guesses = get_guess_bank()

	## Test pattern frequencies
	#averages = {}
	#for g in guesses:
		#avg = get_average_information(g, answers)
		#averages[g] = avg
	#sorted_words = sort_words_by_information(averages)
	#for i in range(0, 5):
		#print(sorted_words[i], averages[sorted_words[i]])



	# Solve
	answer = solve(driver)
	if answer != -1:
		print("\nCorrect Answer:", answer[0], "\nSolved in", answer[1], "guesses.\n")
	else:
		print("\nWasn't able to solve.\n")

	# close the webdriver
	driver.quit()

