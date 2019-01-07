from random import randint

player1R = randint(1,3)
player2R = randint(1,3)

if(player1R == 1):
    player1 = "piedra"
elif(player1R == 2):
    player1 = "papel"
else:
    player1 = "tijeras"

if (player2R == 1):
    player2 = "piedra"
elif (player2R == 2):
    player2 = "papel"
else:
    player2 = "tijeras"

print("PIEDRA,PAPEL O TIJERA !!!")

print("el jugador 1 a sacado " + player1)
print("el jugador 2 a sacado " + player2)

if(player1R == player2R):
    print("Empate")

if(player1R == 1):

    if(player2R == 2):
        print("gana jugador 2")

    if(player2R == 3):
        print("gana jugador 1")

if (player1R == 2):

    if (player2R == 1):
        print("gana jugador 1")

    if (player2R == 3):
        print("gana jugador 2")


if (player1R == 3):

    if (player2R == 1):
        print("gana jugador 2")

    if (player2R == 2):
        print("gana jugador 1")
