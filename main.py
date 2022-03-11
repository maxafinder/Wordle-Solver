from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from board import get_board, get_rows, print_rows
from keyboard import get_keyboard



if __name__ == "__main__":
	## open driver (Safari)
	driver = webdriver.Safari()
	driver.get("https://www.nytimes.com/games/wordle/index.html")

	# get the board, rows, and keyboard
	board = get_board(driver)
	rows = get_rows(board)
	keyboard = get_keyboard(driver)
	
	print_rows(rows)

	# close the webdriver
	driver.close()
