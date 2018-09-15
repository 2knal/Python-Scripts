#! /usr/bin/python

# Program for Tic-Tac-Toe Game

# Initializing board
board = {'Top-left': ' ', 'Top-mid': ' ', 'Top-right':' ', 
	     'Mid-left': ' ', 'Mid-mid': ' ', 'Mid-right': ' ', 
	     'Bot-left': ' ', 'Bot-mid': ' ', 'Bot-right':' '}

print()
print('Note the initial postions of the board: (2 Player Game)', end = '\n\n')

# Displaying board positions
print('Top-left', '|', 'Top-mid', '|', 'Top-right')
print('---------+---------+---------')
print('Mid-left', '|', 'Mid-mid', '|', 'Mid-right')
print('---------+---------+---------')
print('Bot-left', '|', 'Bot-mid', '|', 'Bot-right','\n')

def print_board():
	print(board['Top-left'] + '|' + board['Top-mid'] + '|' + board['Top-right'])
	print('-+-+-')
	print(board['Mid-left'] + '|' + board['Mid-mid'] + '|' + board['Mid-right'])
	print('-+-+-')
	print(board['Bot-left'] + '|' + board['Bot-mid'] + '|' + board['Bot-right'])

def check_rows():
	if board['Top-left'] == board['Top-mid'] == board['Top-right'] == 'X' or board['Top-left'] == board['Top-mid'] == board['Top-right'] == '0':
		print(turn + ', is the Winner!')
		
	elif board['Mid-left'] == board['Mid-mid'] == board['Mid-right'] == 'X' or board['Mid-left'] == board['Mid-mid'] == board['Mid-right'] == '0':
		print(turn + ', is the Winner!')
		return True
	elif board['Bot-left'] == board['Bot-mid'] == board['Bot-right'] == 'X' or board['Bot-left'] == board['Bot-mid'] == board['Bot-right'] == '0':
		print(turn + ', is the Winner!')
		return True
	else:
		return False

def check_columns():
	if board['Top-left'] == board['Mid-left'] == board['Bot-left'] == 'X' or board['Top-left'] == board['Mid-left'] == board['Bot-left'] == '0':
		print(turn + ', is the Winner!')
		return True
	elif board['Top-mid'] == board['Mid-mid'] == board['Bot-mid'] == 'X' or board['Top-mid'] == board['Mid-mid'] == board['Bot-mid'] == '0':
		print(turn + ', is the Winner!')
		return True
	elif board['Top-right'] == board['Mid-right'] == board['Bot-right'] == 'X' or board['Top-right'] == board['Mid-right'] == board['Bot-right'] == '0':
		print(turn + ', is the Winner!')
		return True
	else:
		return False

def check_diagonals():
	if board['Top-left'] == board['Mid-mid'] == board['Bot-right'] == 'X' or board['Top-left'] == board['Mid-mid'] == board['Bot-right'] == 'O':
		print(turn + ', is the Winner!')
		return True
	elif board['Top-right'] == board['Mid-mid'] == board['Bot-left'] == 'X' or board['Top-right'] == board['Mid-mid'] == board['Bot-left'] == 'O':
		print(turn + ', is the Winner!')
		return True
	else:
		return False

# Asking user for initiating the game...
print('Who wants to play first? (X/O): ', end = '')
turn = input()
print('Let`s Begin...')

# Playing the game...
for i in range(9):
	print()
	print_board()
	print()
	print('Which position you want to tuck in ' + turn + '?')
	postion = input()
	board[postion] = turn
	if check_rows() == True or check_columns() == True or check_diagonals() == True:
		print()
		print_board()
		break
	elif (i == 8) and (check_rows() == False or check_columns() == False or check_diagonals() == False):
		print()
		print_board()
		print('Oops, it`s a Draw!')
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'


