#! /usr/bin/python3
# Playing 2048 Number of times you want!

import time, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if len(sys.argv) < 2:
	print("Please, enter number of times you want to play!")
	sys.exit()

browser = webdriver.Firefox()
browser.get("https://gabrielecirulli.github.io/2048/")
repeat = 0

def is_over(browser):
	try:
		game_over = browser.find_element_by_class_name('game-over')
		return game_over
	except:
		pass

grid = browser.find_element_by_tag_name('body')
direction = {0: Keys.UP, 1: Keys.RIGHT, 2: Keys.DOWN, 3: Keys.LEFT}
count = 0
browser.find_element_by_class_name('grid-container').click()

while True:
	grid.send_keys(direction[count%4])
	count += 1

	if is_over(browser) and repeat<int(sys.argv[1]):
		
		print('Game over boys!')
		repeat += 1
		time.sleep(3)
		restartElem = browser.find_element_by_link_text('Try again')
		restartElem.click()
	elif repeat >= int(sys.argv[1]):
		score = browser.find_element_by_class_name('best-container').text
		print("Your highest score in this haul was " + str(score))
		browser.quit()
		sys.exit()
