from random import randint

num1Player1 = randint(1,10)
num2Player1 = randint(1,10)
num3Player1 = randint(1,10)

num1Player2 = randint(1,10)
num2Player2 = randint(1,10)
num3Player2 = randint(1,10)

totalPlayer1 = num1Player1 + num2Player1 + num3Player1
totalPlayer2 = num1Player2 + num2Player2 + num3Player2

print("El jugador 1 a sacado un "+ str(num1Player1) + " un "+ str(num2Player1)+ " y un "+ str(num3Player1))
print("La suma total es de " + str(totalPlayer1))
print("El jugador 1 a sacado un "+ str(num1Player2) + " un "+ str(num2Player2)+ " y un "+ str(num3Player2))
print("La suma total es de " + str(totalPlayer2))

if(totalPlayer1>15):
    if(totalPlayer2>15):
        print("empate")
    else:
        print("gana jugador 2")
elif(totalPlayer2>15):
    print("gana jugador 1")
else:
    if(totalPlayer1>totalPlayer2):
        print("gana jugador 1")
    else:
        print("gana jugador 2")
