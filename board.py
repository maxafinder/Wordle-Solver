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


# Gets the rows of the board in a list of Beautiful Soup objects.
# @param driver -> the selenium webdriver that opens Wordle
# @return -> array of Beautiful Soup objects containing board.
def get_rows(driver):
	# get the html of the gameboard
	board = get_board(driver)
	board_html = board.get_attribute("innerHTML")

	# parse the html of the gameboard
	soup = BeautifulSoup(board_html, 'html.parser')
	rows = soup.contents
	return rows


# Gets the row tiles of the board.
# @param driver -> the selenium webdriver that opens Wordle.
# @return -> a list of rows each containing a list of 5 tiles wich are Beautiful Soup objects.
def get_tiles(driver):
	# get the game-app root
	game_app = driver.find_element(By.TAG_NAME, "game-app")
	game_app_root = driver.execute_script("return arguments[0].shadowRoot", game_app)

	# where we store the rows of tiles	
	row_tiles = []

	# get list of the <game-row> elements 
	board = game_app_root.find_element(By.ID, "board")
	game_rows = game_app_root.find_elements(By.TAG_NAME, "game-row")

	# access shadow DOM in each game-row and get the tiles
	for game_row in game_rows:
		game_row_root = driver.execute_script("return arguments[0].shadowRoot", game_row)
		row = game_row_root.find_element(By.CLASS_NAME, "row")
		row_html = row.get_attribute("innerHTML")
		soup = BeautifulSoup(row_html, 'html.parser')
		tiles = soup.contents
		row_tiles.append(tiles)
	return row_tiles



#
def get_pattern_from_row(row):
	pattern = []
	for tile in row:
		try:
			evaluation = tile["evaluation"]
			pattern.append(evaluation)
		except:
			return -1
	return pattern


#
def get_guess_from_row(row):
	guess = []
	for tile in row:
		try:
			letter = tile["letter"]
			guess.append(letter)
		except:
			return -1
	return guess


#
def is_correct(pattern):
	for evaluation in pattern:
		if evaluation != "correct":
			return False
	return True
