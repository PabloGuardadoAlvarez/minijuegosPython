from random import randint

num1Player1 = randint(1,6)
num2Player1 = randint(1,6)


num1Player2 = randint(1,6)
num2Player2 = randint(1,6)

print("El jugador 1 a sacado un "+ str(num1Player1) + " y un "+ str(num2Player1))
print("El jugador 2 a sacado un "+ str(num1Player2) + " y un "+ str(num2Player2))

player1Total = num1Player1 + num2Player1
player2Total = num1Player2 + num2Player2

player1Big =0
player2Big =0

if(player1Total>player2Total):
    print("El jugador 1 ha ganado")
elif(player2Total > player1Total):
    print("El jugador 2 ha ganado")
else:
    if(num1Player1 > num2Player1):
        player1Big = num1Player1
    else:
        player1Big = num2Player1
    if(player1Big>num1Player2 and player1Big>num2Player2):
        print("El jugador 1 ha ganado")
    elif(num1Player2>player1Big or num2Player2>player1Big):
        print("El jugador 2 ha ganado")
    else:
        print("Empate")

