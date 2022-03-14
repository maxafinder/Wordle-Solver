# This file contains all functions that are used for printing information.


# Prints the rows of the board
# @param rows -> list of BeautifulSoup objects of the game rows.
def print_rows(rows):
	print()
	for i in rows:
		print(i)
	print()


# Prints the html of the keys.
# @param keys -> list of selenium WebElements that are the keyboard keys.
def print_keys(keys):
	for key in keys:
		print(key.get_attribute("outerHTML"))


# Prints the tiles of the board
# @param tiles -> a list of rows each containing a list of 5 tiles.
def print_tiles(tiles):
	for row in tiles:
		for tile in row:
			print(tile)
		print()


# Prints the key-value pair for the dictionary.
# @param dictionary -> the dictionary we want to print.
def print_dictionary(dictionary):
	for i in dictionary:
		print(i, "->", dictionary[i])

