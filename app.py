from flask import Flask, render_template, request

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from driver import get_driver
from solve import solve


# Create Flask app
app = Flask(__name__)


@app.route("/")
@app.route("/game")
def game():
	return render_template("game.html")


# Create a route
@app.route("/home")
def home():
	# Rendering template is due to "Jinja".
	# we can pass arguments to the template and access them using {{}}
	return render_template("home.html", name="Max")





@app.route("/solve")
def s():
	# open driver
	op= webdriver.ChromeOptions()
	op.add_argument("headless")
	driver = webdriver.Chrome(options=op)

	if driver == -1:
		print("ERROR: Problem starting driver")
		exit()
	elif driver == -2:
		exit()
	driver.get("https://www.nytimes.com/games/wordle/index.html")

	# Solve
	answer = solve(driver)

	# close the webdriver
	driver.quit()

	# return answer
	if answer != -1:
		return render_template("answer.html", answer=answer[0], guesses=answer[1])
		#return "\nCorrect Answer:", str(answer[0]), "\nSolved in", str(answer[1]), "guesses.\n"
	else:
		return "Couldn't solve"
		#return "\nWasn't able to solve.\n"

