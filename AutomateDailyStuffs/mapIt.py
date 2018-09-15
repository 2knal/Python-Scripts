#! /usr/bin/python3

import sys, pyperclip, webbrowser

# If there are command line arguments
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])

# Or else check for address on clipboard
else:
	address = pyperclip.paste()

# Open the web browser using web browser module
webbrowser.open(r'https://www.google.com/maps/place/' + address)

