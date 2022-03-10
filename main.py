import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_board(driver):
	# get the game-app root
	game_app = driver.find_element(By.TAG_NAME, "game-app")
	game_app_root = driver.execute_script("return arguments[0].shadowRoot", game_app)

	## find the <div id="board"> element
	board = game_app_root.find_element(By.ID, "board")
	return board




def get_keyboard(driver):
	# get the game-app root
	game_app = driver.find_element(By.TAG_NAME, "game-app")
	game_app_root = driver.execute_script("return arguments[0].shadowRoot", game_app)

	# find the game-keyboard root
	game_keyboard = game_app_root.find_element(By.TAG_NAME, "game-keyboard")
	game_keyboard_root = driver.execute_script("return arguments[0].shadowRoot", game_keyboard)

	# find the <div id="keyboard"> element
	keyboard_div = game_keyboard_root.find_element(By.ID, "keyboard")
	return keyboard_div




if __name__ == "__main__":
	## open driver (Safari)
	driver = webdriver.Safari()
	driver.get("https://www.nytimes.com/games/wordle/index.html")

	board = get_board(driver)
	keyboard = get_keyboard(driver)

	print("board:", board.tag_name)
	print("keyboard:", keyboard.tag_name)
