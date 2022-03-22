from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from driver import get_driver
from solve import solve


if __name__ == "__main__":
	# open driver
	driver = get_driver()
	if driver == -1:
		print("ERROR: Problem starting driver")
		exit()
	elif driver == -2:
		exit()
	
	# Get the nytimes wordle website
	try:
		driver.get("https://www.nytimes.com/games/wordle/index.html")
	except:
		print("ERROR: Couldn't get https://www.nytimes.com/games/wordle/index.html")
		exit()
		

	# Solve
	answer = solve(driver)
	if answer != -1:
		print("\nCorrect Answer:", answer[0], "\nSolved in", answer[1], "guesses.\n")
	else:
		print("\nWasn't able to solve.\n")

	# close the webdriver
	driver.quit()

