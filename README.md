Developed by: Max Finder

-------------------------------------------------------------------

--Description of Project--

This program solves Wordle on "https://www.nytimes.com/wordle".

It uses selenium to interact with the site using a webdriver. The program supports Chrome and Safari, however if you want to run the solver using Chrome you need to install a Chrome driver following the instructions below.

-------------------------------------------------------------------

How to use Chrome driver (Mac):

1. Install driver for your machine's version of Chrome:
	 Chrome -> https://chromedriver.storage.googleapis.com/index.html

2. Move the chromedriver file you just downloaded to /usr/local/bin

3. Add this file to your systems path.
	 (in ~/.bash_profile add the line "export $PATH:/usr/local/bin/chromedriver")

4. Try running the command "chromedriver" and see if it executes. You might have to run the command "xattr -d com.apple.quarantine /usr/local/bin/chromedriver" in order to give your machine permission to execute the driver.

-------------------------------------------------------------------

How to use Chrome driver (Windows):

1. Install driver for your machine's version of Chrome:
	 Chrome -> https://chromedriver.storage.googleapis.com/index.html

2. Move the chromedriver file you just downloaded to \Windows\System32

3. Add this file to your systems path.

-------------------------------------------------------------------

How to run:

Navigate to the projects directoy and run the virtual environment by running the command "pipenv shell"
Then run the program with "python3 main.py <chrome || safari>"

-------------------------------------------------------------------

NOTES:
Uses Pipenv Python package managing tool to manage dependencies.