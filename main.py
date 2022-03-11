import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


# Gets the div containing the board in a selenium WebElement.
# @param driver -> the selenium webdriver that opens Wordle
# @return -> selenium WebElement containing <div id="board">
def get_board(driver):
	# get the game-app root
	game_app = driver.find_element(By.TAG_NAME, "game-app")
	game_app_root = driver.execute_script("return arguments[0].shadowRoot", game_app)

	# find the <div id="board"> element
	board = game_app_root.find_element(By.ID, "board")
	return board



# Gets the rows of the board in an array of Beautiful Soup objects.
# @param board -> a selenium WebElement containing <div id="board">
# @return -> array of Beautiful Soup objects containing board.
def get_rows(board):
	# get the html of the gameboard
	board_html = board.get_attribute("innerHTML")

	# parse the html of the gameboard
	soup = BeautifulSoup(board_html, 'html.parser')
	rows = soup.contents
	return rows



# Prints the rows of the board
# @param rows -> array of BeautifulSoup objects of the game rows.
def print_rows(rows):
	for i in rows:
		print(i)
	


# Gets the div containing the keyboard in a selenium WebElement.
# @param driver -> the selenium webdriver that opens Wordle
# @return -> selenium WebElement containing <div id="keyboard">
def get_keyboard(driver):
	# get the game-app root
	game_app = driver.find_element(By.TAG_NAME, "game-app")
	game_app_root = driver.execute_script("return arguments[0].shadowRoot", game_app)

	# find the game-keyboard root
	game_keyboard = game_app_root.find_element(By.TAG_NAME, "game-keyboard")
	game_keyboard_root = driver.execute_script("return arguments[0].shadowRoot", game_keyboard)

	# find the <div id="keyboard"> element
	keyboard = game_keyboard_root.find_element(By.ID, "keyboard")
	return keyboard






if __name__ == "__main__":
	## open driver (Safari)
	driver = webdriver.Safari()
	driver.get("https://www.nytimes.com/games/wordle/index.html")

	# get the board, rows, and keyboard
	board = get_board(driver)
	rows = get_rows(board)
	keyboard = get_keyboard(driver)

	print_rows(rows)
	




	driver.close()
