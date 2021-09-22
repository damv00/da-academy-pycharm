'''
0 means an empty square,
a 1 means that player 1 put their token in that space,
and a 2 means that player 2 put their token in that space.

Given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
tell me whether anyone has won, and tell me which player won, if any.
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
'''
def tic_tac_toe(game):
	for i in game:
		print("\t",i)
	columna1=[game[0][0],game[1][0],game[2][0]]
	columna2=[game[0][1],game[1][1],game[2][1]]
	columna3=[game[0][2],game[1][2],game[2][2]]

	#Validacion de columna
	if columna1==[1,1,1] or columna2==[1,1,1] or columna3==[1,1,1]:
		print("Player one is the winner")
	elif columna1==[2,2,2] or columna2==[2,2,2] or columna3==[2,2,2]:
		print("Player two is the winner")

	#Validacion diagonal
	elif game[0][0]==game[1][1]==game[2][2]==1:
		print("Player one is the winner")
	elif game[0][0]==game[1][1]==game[2][2]==2:
		print("Player two is the winner")
	elif game[0][2]==game[1][1]==game[2][0]==1:
		print("Player one is the winner")
	elif game[0][2]==game[1][1]==game[2][0]==2:
		print("Player two is the winner")
	#Validacion de fila
	elif game[0]==[1,1,1] or game[1]==[1,1,1] or game[2]==[1,1,1]:
		print("Player one is the winner")
	elif game[0]==[2,2,2] or game[1]==[2,2,2] or game[2]==[2,2,2]:
		print("Player two is the winner")
	else:
		print("There was no winner")

first_play=[[1, 2, 0],
			[2, 1, 0],
			[2, 1, 2]]
tic_tac_toe(first_play)