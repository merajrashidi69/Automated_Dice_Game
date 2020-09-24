import random
from time import sleep
player1=random.randint(1,6)
player2=random.randint(1,6)

print(f'Player1 has rolled the dice to {player1}.')
sleep(1)
print(f'Player2 has rolled the dice to {player2}.\n')
sleep(1)
if player1 > player2:
    print(f'Player1 wins at a dice roll of {player1}.')
elif player2 > player1:
    print(f'Player2 wins at a dice roll of {player2}.')
elif player1 == player2:
    print('The game was a draw.')

else:
    print('Error.')
