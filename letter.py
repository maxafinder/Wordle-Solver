from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from board import get_tiles
from print import print_dictionary

# Gets the state of a letter
# @param keys -> list of selenium WebElements that are the keyboard keys.
def get_letter_state(keys, val):
	for key in keys:
		if key.text.lower() == val.lower():
			key_html = key.get_attribute("outerHTML")
			soup = BeautifulSoup(key_html, 'html.parser')
			try:
				state = soup.contents[0]['data-state']
				return state
			except:
				return ""


# Creates a dictionary with the state of each letter a-z
# @param keys -> list of selenium WebElements that are the keyboard keys.
def get_letter_states(keys):
	states = {}
	for key in keys:
		if len(key.text) == 1: # is a letter
			states[key.text.lower()] = get_letter_state(keys, key.text)
	return states


# Gets the correct letters that have been discovered for each position
# @param tiles -> a list of rows each containing a list of 5 tiles.
# @return -> a dictionary that maps position numbers 1-5 to the correct letters that
# 					 have been discovered.
def get_correct_letters(tiles):
	# initialize correct letters dictionary to empty strings
	correct_letters = {}
	for i in range(1, 6):
		correct_letters[i] = ""

	# check each tile for correct letters
	for row in tiles:
		for tile in range(0, 5):
			# try to get the letter and evaluation
			try:
				letter = row[tile]["letter"]
				evaluation = row[tile]["evaluation"] # absent, present, or correct

				if evaluation == "correct":
					correct_letters[tile + 1] = letter
			except: # haven't guessed in this row yet
				break
	return correct_letters


# Determines if the evaluation of a letter is "present" somewhere in the guess.
# @param row -> the row of the guess we are evaluating.
# @param l -> the letter that we are looking for.
# @return -> True if a letter has evaluation "present" somewhere in the guess, otherwise False.
def is_present_in_guess(row, l):
	for tile in range(0, 5):
		try:
			letter = row[tile]["letter"]
			evaluation = row[tile]["evaluation"] # absent, present, or correct

			if letter == l and evaluation == "present":
				return True
		except:
			return False
		return False




# Creates a dictionary with the possible positions for each letter based on the current guesses.
# @param driver -> the selenium webdriver that opens Wordle
# @param keys -> list of selenium WebElements that are the keyboard keys.
# @return -> a dictionary that maps each letter to a list of possible positions in the word (1-5).
def get_possbile_letter_positions(driver, keys):
	# get the tiles and states for each letter
	tiles = get_tiles(driver)
	states = get_letter_states(keys)

	# create dictionary with all letter positions
	# TODO: initialize with possible letter positions from word bank

	possible_positions = {}
	for key in keys:
		if len(key.text) == 1: # is a letter
			possible_positions[key.text.lower()] = [1, 2, 3, 4, 5]

	# go through the tiles and extract information
	for row in tiles:
		for tile in range(0, 5):
			# try to get the letter and evaluation
			try:
				letter = row[tile]["letter"]
				evaluation = row[tile]["evaluation"] # absent, present, or correct


				# if evaluation of letter is absent
				if evaluation == "absent":
					# check to see if the letter could still could be in word
					if states[letter] == "absent": # not in word
						possible_positions[letter].clear()

					elif states[letter] == "correct": # is correct in word
						# gets the correct letters that have been discovered for each position
						correct_letters = get_correct_letters(tiles)

						# if there could still be another instance of the letter besides the correct one
						if is_present_in_guess(row, letter):
							possible_positions[letter].remove(tile + 1)
						else: # remove possible positions besides correct ones for this letter
							for i in range(1, 6):
								if correct_letters[i] != letter:
									possible_positions[letter].remove[i]


				# if evaluation of letter is "correct"
				elif evaluation == "correct":
					print(letter, "is CORRECT at position", tile + 1)

					# remove position from all other letters
					for l in possible_positions:
						if l.lower() != letter.lower():
							try:
								possible_positions[l].remove(tile + 1)
							except:
								continue


				# if evaluation of letter is "present"
				elif evaluation == "present": 
					# remove the position with evaluation "present" from possible positions
					possible_positions[letter].remove(tile + 1)

			except: # haven't guessed in this row yet
				print("here", row, tile)
				break
	return possible_positions




