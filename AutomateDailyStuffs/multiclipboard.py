#! /usr/bin/python3

import sys, pyperclip, shelve

shelf_file = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	shelf_file[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv):
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(shelf_file.items())))
	elif sys.argv[1] in list(shelf_file.keys()):
		pyperclip.copy(shelf_file[sys.argv[1]])

shelf_file.close()

