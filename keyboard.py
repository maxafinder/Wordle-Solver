from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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


# Gets a list of selenium WebElements that are the keyboard keys.
# @param driver -> the selenium webdriver that opens Wordle
def get_keys(driver):
	keyboard = get_keyboard(driver)
	keys = keyboard.find_elements(By.TAG_NAME, "button")
	return keys


# Clicks the keyboard key with the specified value.
# @param keys -> list of selenium WebElements that are the keyboard keys.
# @param val -> the value of the key we want to click.
def click_key(keys, val):
	# find the key in keys with val
	for key in keys:
		if key.text.lower() == val.lower():
			# click the key
			key.send_keys(Keys.ENTER)


# Guesses the word and waits for board to update.
# @param keys -> list of selenium WebElements that are the keyboard keys.
# @param word -> the 5 letter word we want to guess.
def guess_word(keys, word):
	if len(word) > 5:
		print("Invalid guess")
		return
	for i in word:
		click_key(keys, i)
	click_key(keys, "enter")
	sleep(2)


