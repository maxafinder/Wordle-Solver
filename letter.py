from copy import deepcopy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

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
# @param guess -> the word that we guessed.
# @param pattern -> list of evaluations from the word we guessed ("absent", "present", "correct").
# @param letter -> the letter that we are looking for.
# @return -> True if a letter has evaluation "present" somewhere in the guess, otherwise False.
def is_present_in_guess(guess, pattern, letter):
	for i in range(0, 5):
		if guess[i] == letter  and pattern[i] == "present":
			return True
	return False


#
def initialize_possible_positions(keys):
	possible_positions = {}
	for key in keys:
		if len(key.text) == 1: # is a letter
			possible_positions[key.text.lower()] = [1, 2, 3, 4, 5]
	return possible_positions






# Creates a dictionary with the possible positions for each letter based on the current guesses.
# @param driver -> the selenium webdriver that opens Wordle
# @param keys -> list of selenium WebElements that are the keyboard keys.
# @return -> a dictionary that maps each letter to a list of possible positions in the word (1-5).
def get_possbile_letter_positions_after_guess(guess, pattern, possible_positions):
	new_possible_positions = deepcopy(possible_positions)	

	for i in range(0, 5):
		# get the letter and evaluation
		letter = guess[i]
		evaluation = pattern[i] # absent, present, or correct

		# if evaluation of letter is absent
		if evaluation == "absent":
			# remove this position
			try:
				new_possible_positions[letter].remove(i + 1)
			except:
				pass

			# check to see if the letter could still could be in word
			for l in range(0, 5):
				# if there are multiple instances of the letter (not totally absent)
				if guess[l] == letter and (pattern[l] == "correct" or pattern[l] == "present"):
					# if it is NOT still present somewhere in word, then remove possible
					# positions besides correct ones for this letter
					if not is_present_in_guess(guess, pattern, letter):
						for j in range(0, 5):
							if guess[j] != letter or pattern[j] != "correct":
								try:
									new_possible_positions[letter].remove(j + 1)
								except:
									continue
					break
				

		# if evaluation of letter is "correct"
		elif evaluation == "correct":
			# remove position from all other letters
			for l in new_possible_positions:
				if l.lower() != letter.lower():
					try:
						new_possible_positions[l].remove(i + 1)
					except:
						continue

		# if evaluation of letter is "present"
		elif evaluation == "present": 
			# remove the position with evaluation "present" from possible positions
			new_possible_positions[letter].remove(i + 1)
	return new_possible_positions




#
def get_letter_frequencies(words, keys):
	letter_frequencies = {}
	for key in keys:
		if len(key.text) == 1: # is a letter
			letter_frequencies[key.text.lower()] = 0

	for word in words:
		for letter in word:
			letter_frequencies[letter] = letter_frequencies[letter] + 1
	return letter_frequencies	
