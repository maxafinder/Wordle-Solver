import sys
from selenium import webdriver


# Gets the driver for the browser specified from the command line.
# @return -> a selenium webdriver for the specified browser.
#						 -1 if there was an error starting the driver.
#						 -2 if the command line usage was incorrect
def get_driver():
	# Check command line arguments
	if len(sys.argv) == 2: 
		if sys.argv[1] == "chrome":
			print("Running Chrome")
			driver = start_chrome_driver()

		elif sys.argv[1] == "safari":
			if sys.platform != "darwin": # Trying to run Safari on non-Mac
				print("ERROR: Need Mac for Safari, use Chrome instead")
			print("Running Safari")
			driver = start_safari_driver()
			
		else:
			print("ERROR: Usage --> python3 main.py <chrome || safari>")
			return -2
	else:
		print("ERROR: Usage --> python3 main.py <chrome || safari>")
		return -2
	return driver


# Starts the driver for Chrome.
# @return -> a selenium Chrome webdriver.
def start_chrome_driver():
	try:
		op= webdriver.ChromeOptions()
		op.add_argument("headless")
		driver = webdriver.Chrome(options=op)
	except:
		return -1
	return driver


# Starts the driver for Safari.
# @return -> a selenium Safari webdriver.
def start_safari_driver():
	try:
		driver = webdriver.Safari()
	except:
		return -1
	return driver
