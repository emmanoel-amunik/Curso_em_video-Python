from random import randint
v = 0
while True:
    pl = int(input('Type a value: '))
    com = randint(0, 11)
    total = pl + com
    tipe = ' '
    while tipe not in "EO":
        tipe = str(input('Even or Odd? [E/O] ')).upper().strip()
    print(f'You played {pl} and the computer {com}. The total is {total}', end='')
    print('EVEN!' if total % 2 == 0 else 'ODD!')
    if tipe == 'E':
        if total % 2 == 0:
            print('You win!')
            v += 1
        else:
            print('You lost!')
            break
    elif tipe == 'O':
        if total % 2 == 1:
            print('You win!')
            v += 1
        else:
            print('You lost!')
            break
    print("Let's play again...")
print(f'GAME OVER! You win {v} times.')
