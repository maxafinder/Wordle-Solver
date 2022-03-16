from tkinter import W
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from driver import get_driver
from board import get_board, get_rows, get_tiles
from keyboard import get_keyboard, get_keys, click_key, guess_word
from letter import get_letter_state, get_possbile_letter_positions, get_letter_states 
from print import print_dictionary, print_tiles, print_rows, print_keys
from word_bank import get_answer_bank, get_guess_bank
from next_guess import eliminate_answers


if __name__ == "__main__":

	# open driver
	driver = get_driver()
	if driver == -1:
		print("ERROR: Problem starting driver")
		exit()
	elif driver == -2:
		exit()
	driver.get("https://www.nytimes.com/games/wordle/index.html")


	# Get the keys
	keys = get_keys(driver)

	# guess word
	guess_word(keys, "lease")

	## Get keys after guessing word
	keys = get_keys(driver)


	## Guess more words

	#guess_word(keys, "crane")
	#keys = get_keys(driver)

	#guess_word(keys, "bends")
	#keys = get_keys(driver)

	#guess_word(keys, "which")
	#keys = get_keys(driver)



	# get the state of each letter
	states = get_letter_states(keys)
	#print_dictionary(states)

	# get the row tiles
	tiles = get_tiles(driver)
	print_tiles(tiles)

	# get the possible letter positions
	possible_positions = get_possbile_letter_positions(driver, keys)
	print_dictionary(possible_positions)

	# get list of possible 5 letter words
	answers = get_answer_bank()
	guesses = get_guess_bank()

	answers = eliminate_answers(answers, possible_positions)
	for a in answers:
		print(a)


	# close the webdriver
	driver.quit()

