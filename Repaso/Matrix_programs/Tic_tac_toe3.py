print("Bienvenido al juego de tic tac toe")
tablero_de_juego=[["*","*","*"],["*","*","*"],["*","*","*"]]
for i in tablero_de_juego:
    print(f"\t{i}")
n=0
lista_fila_ocupada=[]
lista_columna_ocupada=[]

while n<=9:
    finjugador1="Continuar"
    finjugador2="Continuar"
    # Jugador 1
    #Validacion de posicion ocupada
    while finjugador1=="Continuar":
        filacorrecta = 0
        columnacorrecta = 0
        print("\n\tEs el turno del jugador 1")
        #Validacion de fila
        while filacorrecta==0:
            fila_jugador1 = int(input("¿En que fila quieres ingresar tu ficha?(1-3): "))
            if fila_jugador1 not in (1,2,3):
                print("Numero de fila invalido, vuelva a intentar")
                filacorrecta=0
            else:
                filacorrecta=1
        #Validacion de columna
        while columnacorrecta==0:
            columna_jugador1 = int(input("¿En que columna quieres ingresar tu ficha?(1-3): "))
            if columna_jugador1 not in (1, 2, 3):
                print("Numero de columna invalido, vuelva a intentar")
                columnacorrecta=0
            else:
                columnacorrecta=1
        if tablero_de_juego[fila_jugador1 - 1][columna_jugador1 - 1]=="X" or tablero_de_juego[fila_jugador1 - 1][columna_jugador1 - 1]=="O":
            print("Esa posicion ya esta ocupada, intenta en otra posicion")
            finjugador1 = "Continuar"
        else:
            lista_fila_ocupada.append(fila_jugador1)
            lista_columna_ocupada.append(columna_jugador1)
            tablero_de_juego[fila_jugador1 - 1][columna_jugador1 - 1] = "X"
            for i in tablero_de_juego:
                print(f"\t{i}")
            n += 1
            finjugador1 = "Fin"

    #Jugador 2
    # Validacion de posicion ocupada
    while finjugador2 =="Continuar":
        filacorrecta = 0
        columnacorrecta = 0
        print("\n\tEs el turno del jugador 2")
        #Validacion fila
        while filacorrecta==0:
            fila_jugador2 = int(input("¿En que fila quieres ingresar tu ficha?(1-3): "))
            if fila_jugador2 not in (1,2,3):
                print("Numero de fila invalido, vuelva a intentar")
                filacorrecta = 0
            else:
                filacorrecta = 1
        #Validacion columna
        while columnacorrecta==0:
            columna_jugador2 = int(input("¿En que columna quieres ingresar tu ficha?(1-3): "))
            if columna_jugador2 not in (1, 2, 3):
                print("Numero de columna invalido, vuelva a intentar")
                columnacorrecta = 0
            else:
                columnacorrecta = 1
        if tablero_de_juego[fila_jugador2 - 1][columna_jugador2 - 1] == "X" or tablero_de_juego[fila_jugador2 - 1][columna_jugador2 - 1] == "O":
            print("Esa posicion ya esta ocupada, intenta en otra posicion")
            finjugador2 = "Continuar"
        else:
            lista_fila_ocupada.append(fila_jugador2)
            lista_columna_ocupada.append(columna_jugador2)
            tablero_de_juego[fila_jugador2 - 1][columna_jugador2 - 1] = "O"
            for i in tablero_de_juego:
                print(f"\t{i}")
            n += 1
            finjugador2 = "Fin"

