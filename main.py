from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from board import get_board, get_rows, print_rows
from keyboard import get_keyboard, get_keys, click_key, guess_word



if __name__ == "__main__":
	## open driver (Safari)
	driver = webdriver.Safari()
	driver.get("https://www.nytimes.com/games/wordle/index.html")

	# get the rows, and keys
	rows = get_rows(driver)
	keys = get_keys(driver)

	# guess "traps"
	guess_word(keys, "traps")

	# start typing "new"
	click_key(keys, "n")
	click_key(keys, "e")
	click_key(keys, "w")

	# print the rows on the board
	rows = get_rows(driver)
	print_rows(rows)


	# close the webdriver
	driver.close()

