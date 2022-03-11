from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


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
