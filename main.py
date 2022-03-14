from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from driver import get_driver
from board import get_board, get_rows, get_tiles
from keyboard import get_keyboard, get_keys, click_key, guess_word
from letter import get_letter_state, get_possbile_letter_positions, get_letter_states 
from print import print_dictionary, print_tiles, print_rows, print_keys



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
	guess_word(keys, "steep")
	keys = get_keys(driver)

	# Get keys after guessing word
	keys = get_keys(driver)


	# Guess more words

	#guess_word(keys, "zebra")
	#keys = get_keys(driver)

	#guess_word(keys, "grape")
	#keys = get_keys(driver)

	#guess_word(keys, "alone")
	#keys = get_keys(driver)

	# start typing "new"
	click_key(keys, "n")
	click_key(keys, "e")
	click_key(keys, "w")


	# get the state of each letter
	states = get_letter_states(keys)
	#print_dictionary(states)

	# get the row tiles
	tiles = get_tiles(driver)
	#print_tiles(tiles)

	# get the possible letter positions
	possible_positions = get_possbile_letter_positions(driver, keys)
	print_dictionary(possible_positions)


	# close the webdriver
	driver.quit()

