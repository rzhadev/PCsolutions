def display_board(board):
	print(board[1]+'|'+board[2]+'|'+board[3])
	print(board[4]+'|'+board[5]+'|'+board[6])
	print(board[7]+'|'+board[8]+'|'+board[9])
def check_winner(mark,board):
	return ((board[1] == mark and board[2] == mark and board[3] == mark) or 
	(board[4] == mark and board[5] == mark and board[6] == mark) or 
	(board[7] == mark and board[8] == mark and board[9] == mark) or 
	(board[1] == mark and board[4] == mark and board[7] == mark) or 
	(board[2] == mark and board[5] == mark and board[8] == mark) or
	(board[3] == mark and board[6] == mark and board[9] == mark) or 
	(board[1] == mark and board[5] == mark and board[9] == mark) or 
	(board[3] == mark and board[5] == mark and board[7] == mark))

def player_input():
	marker = ''
	while marker != 'X' and marker != 'O':
		marker = input('Do you want to be X or O? :').upper()
	if marker == 'X':
		return ('X','O')
	else:
		return ('O','X')
def place_marker(marker,myboard,position):
	myboard[position] = marker 
def fill_check(myboard,position):
	return myboard[position] != 'X' and myboard[position] != 'O'
def fullboard_check(myboard):
	total = 0 
	for space in myboard:
		if space == 'X' or space == 'O':
			total = total + 1
	return total == 9
def player_choice(board):
	position = 0
	while position not in [1,2,3,4,5,6,7,8,9] or not fill_check(board,position):
		position = int(input('Choose your next move 1-9: '))
	return position
def replay():
	return input('Do you want to replay the game? :')

print('Tic Tac Toe')
while True:
	myboard = ['#','1','2','3','4','5','6','7','8','9']
	player1_marker, player2_marker = player_input()
	turn = 'X'
	play_game = input('Do you want to start? yes or no :')
	if play_game.lower() == 'yes':
		game_on = True
	else:
		game_on = False
	while game_on:
		if turn == 'X':
			display_board(myboard)
			position = player_choice(myboard)
			place_marker(turn,myboard,position)
			if check_winner(turn,myboard):
				display_board(myboard)
				print('X wins the game')
				break
			else:
				turn = 'O'
		else:
			display_board(myboard)
			position = player_choice(myboard)
			place_marker(turn,myboard,position)
			if check_winner(turn,myboard):
				display_board(myboard)
				print('O wins the game')
				break
			else:
				turn = 'X'
	if replay() != True:
		break

