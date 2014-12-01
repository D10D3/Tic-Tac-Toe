# Python Tic-Tac-Toe by D10d3
# Goals:
#       play tic tac toe with computer
# Optional future goals
#       ask to play again
#       keep score of games
#       ask player if X or O
#       ask player if they want to go first
#       Better Computer Logic
#**********************************************************************************************
 
# SETUP
import os
os.system('cls') #Clears the screen on windows machines
import random
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
 
#Sub Routines
def ClearScreen():
	os.system('cls') #Clears the screen on windows machines

def ClearBoard(board):# assign board variables using a list numbered 0-8 for the 9 slots, defaulting to ' ' as empty
	board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	return board
 
def PrintExampleBoard (): #Example board to for player move selection
	print """
	-------------
	| 1 | 2 | 3 |
	-------------
	| 4 | 5 | 6 |
	-------------
	| 7 | 8 | 9 |
	-------------\n"""
   
def PrintBoard (): #Prints the current board
	print "Current Board Positions:"
	print "-------------"
	print "|", board[0] , "|" , board[1] , "|" , board[2] , "|"
	print "-------------"
	print "|", board[3] , "|" , board[4] , "|" , board[5] , "|"
	print "-------------"
	print "|", board[6] , "|" , board[7] , "|" , board[8] , "|"
	print "-------------\n"
 
def PlayerTurn(board): #player selects move and it checks if it's valid and applies it to the board
	valid = False
	while not valid:
		print "Select a square to mark (1-9):"
		p_choice = raw_input('>')
		if p_choice in '123456789':
			valid = True
		else:
			#String formatting is cool.
			print('"{}" is not a valid move'.format(p_choice))
			valid = False
		playSquare = int(p_choice) - 1
		if board[playSquare] == ' ':
			board[playSquare] = "X"
		else:
			#String formatting is cool.
			print('"{}" is not a valid move'.format(p_choice))
			valid = False
	return board
 
def ComputerTurn(board): #Computer selects move and it checks if it's valid and applies it to the board
   emptySquares = []
   for square in range(len(board)):
       if board[square] == " ":
           emptySquares.append(square)
   choice = random.choice(emptySquares)
   board[choice] = "O"
   return board
	
def DidPlayerWin(board,Playing):
	# 3 Across Wins
	if board[0] == "X" and board [1] == "X" and board[2] == "X":
			ClearScreen()
			PrintBoard()
			print "You Win!"
			quit()
	elif board[3] == "X" and board [4] == "X" and board[5] == "X":
			ClearScreen()
			PrintBoard()
			print "You Win!"
			quit()
	elif board[6] == "X" and board [7] == "X" and board[8] == "X":
			ClearScreen()
			PrintBoard()
			print "You Win!"
			quit()
	# 3 Down Wins
	elif board[0] == "X" and board [3] == "X" and board[6] == "X":
			ClearScreen()
			PrintBoard()
			print "You Win!"
			quit()
	elif board[1] == "X" and board [4] == "X" and board[7] == "X":
			ClearScreen()
			PrintBoard()
			print "You Win!"
			quit()
	elif board[2] == "X" and board [5] == "X" and board[8] == "X":
			ClearScreen()
			PrintBoard()
			print "You Win!"
			quit()
	# Diagonal Wins
	elif board[0] == "X" and board [4] == "X" and board[8] == "X":
			ClearScreen()
			PrintBoard()
			print "You Win!"
			quit()
	elif board[2] == "X" and board [4] == "X" and board[6] == "X":
			ClearScreen()
			PrintBoard()
			print "You Win!"
			quit()
	# No Win
	else:
			Playing = True
	return Playing

def DidComputerWin(board,Playing):
	# 3 Across Wins
	if board[0] == "O" and board [1] == "O" and board[2] == "O":
			ClearScreen()
			PrintBoard()
			print "The Computer Wins"
			quit()
	elif board[3] == "O" and board [4] == "O" and board[5] == "O":
			ClearScreen()
			PrintBoard()
			print "The Computer Wins"
			quit()
	elif board[6] == "O" and board [7] == "O" and board[8] == "O":
			ClearScreen()
			PrintBoard()
			print "The Computer Wins"
			quit()
	# 3 Down Wins
	elif board[0] == "O" and board [3] == "O" and board[6] == "O":
			ClearScreen()
			PrintBoard()
			print "The Computer Wins"
			quit()
	elif board[1] == "O" and board [4] == "O" and board[7] == "O":
			ClearScreen()
			PrintBoard()
			print "The Computer Wins"
			quit()
	elif board[2] == "O" and board [5] == "O" and board[8] == "O":
			ClearScreen()
			PrintBoard()
			print "The Computer Wins"
			quit()
	# Diagonal Wins
	elif board[0] == "O" and board [4] == "O" and board[8] == "O":
			ClearScreen()
			PrintBoard()
			print "The Computer Wins"
			quit()
	elif board[2] == "O" and board [4] == "O" and board[6] == "O":
			ClearScreen()
			PrintBoard()
			print "The Computer Wins"
			quit()
	# No Win
	else:
			Playing = True
	return Playing

def IsDraw(board,Playing):#Determines if the game ended in a draw
	if ' ' not in board:
		ClearScreen()
		PrintBoard()
		print "The Game Ended in a Draw"
		quit()
	else:
		Playing = True
	return Playing
   
#Introduction
print "lets play Tic-Tac-Toe"
print "You are X's and get to go first\n"
raw_input ("Press Any Key To Begin")
 
#Game Loop     
Playing = True
while Playing:
	ClearScreen()
	PrintBoard()
	PrintExampleBoard()
	board = PlayerTurn(board)
	Playing = DidPlayerWin(board,Playing)
	Playing = IsDraw(board,Playing)
	board = ComputerTurn(board)
	Playing = DidComputerWin(board,Playing)
	Playing = IsDraw(board,Playing)

