from random import randint

lottery_games = list()
num = list()

games = int(input('How many lottery games? '))

for p in range(games):
    for n in range(1, 7):
        ran = randint(1, 60)
        if ran not in num:
            num.append(ran)
        else:
            num.append(randint(1, 60))

    lottery_games.append(num[:])
    num.clear()

for i, l in enumerate(lottery_games):
    print(f'Game {i+1}: {l}')
