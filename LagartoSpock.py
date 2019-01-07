from random import randint

player1R = randint(1,5)
player2R = randint(1,5)

if(player1R == 1):
    player1 = "piedra"
elif(player1R == 2):
    player1 = "papel"
elif(player1R == 3):
    player1 = "tijera"
elif(player1R == 4):
    player1 = "lagarto"
else:
    player1 = "spock"

if (player2R == 1):
    player2 = "piedra"
elif (player2R == 2):
    player2 = "papel"
elif (player2R == 3):
    player2 = "tijera"
elif (player2R == 4):
    player2 = "lagarto"
else:
    player2 = "spock"

print("PIEDRA,PAPEL,TIJERA, LAGARTO, SPOCK !!!")

print("el jugador 1 a sacado " + player1)
print("el jugador 2 a sacado " + player2)

if(player1R == player2R):
    print("Empate")

if(player1R == 1):

    if(player2R == 2 or player2R == 5):
        print("gana jugador 2")

    if(player2R == 3 or player2R == 4):
        print("gana jugador 1")

if (player1R == 2):

    if (player2R == 1 or player2R == 5):
        print("gana jugador 1")

    if (player2R == 3 or player2R == 4):
        print("gana jugador 2")


if (player1R == 3):

    if (player2R == 1 or player2R == 5):
        print("gana jugador 2")

    if (player2R == 2 or player2R == 4):
        print("gana jugador 1")

if (player1R == 4):

    if (player2R == 3 or player2R == 1):
        print("gana jugador 2")

    if (player2R == 2 or player2R == 5):
        print("gana jugador 1")

if (player1R == 5):

    if (player2R == 1 or player2R == 3):
        print("gana jugador 2")

    if (player2R == 2 or player2R == 4):
        print("gana jugador 1")