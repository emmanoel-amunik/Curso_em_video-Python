from random import randint
from time import sleep
items = ('Stone', 'Paper', 'Scissors')
computer = randint(0, 2)
print('''Your options:
[ 0 ] Stone
[ 1 ] Paper
[ 2 ] Scissors''')
player = int(input('What is your move? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-=' * 11)
print('Computer move {}'.format(items[computer]))
print('Player move {}'.format(items[player]))
print('-=' * 11)
if computer == 0:
    if player == 0:
        print('DRAW')
    elif player == 1:
        print('PLAYER WINS')
    elif player == 2:
        print('COMPUTER WINS')
    else:
        print('INVALID MOVE!')
elif computer == 1:
    if player == 0:
        print('COMPUTER WINS')
    elif player == 1:
        print('DRAW')
    elif player == 2:
        print('PLAYER WINS')
    else:
        print('INVALID MOVE!')
elif computer == 2:
    if player == 0:
        print('PLAYER WINS')
    elif player == 1:
        print('COMPUTER WINS')
    elif player == 2:
        print('DRAW')
    else:
        print('INVALID MOVE!')
