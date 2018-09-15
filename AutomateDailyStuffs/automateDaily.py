#! /usr/bin/python3

# Automating my daily learning

import webbrowser, sys

# Opening the website www.automatetheboringstuff.com

if len(sys.argv) < 2:
	print('Please enter the chapter number you want to visit.')
	sys.exit()
else:
	sys.argv.remove('automateDaily.py')
	for i in sys.argv:
		webbrowser.open('https://www.automatetheboringstuff.com/chapter' + i)	# Opening the website www.automatetheboringstuff.com

