'''
Draw A Game Board
Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---

This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

'''
def lineas(n):
    lista1 = []
    for i in range(n):
        lista1.append(" ")
        for j in range(3):
            lista1.append("-")
    lista1 = "".join(lista1)
    print(lista1)
def columna(n):
    lista2 = []
    for i in range(n):
        lista2.append("|")
        for j in range(3):
            lista2.append(" ")
        if i + 1 == n:
            lista2.append("|")
    lista2 = "".join(lista2)
    print(lista2)

size=input("What size game board do you want me to draw: ")
size=int(size)

for i in range(size):
    lineas(size)
    columna(size)
    if i+1==size:
        lineas(size)



game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
