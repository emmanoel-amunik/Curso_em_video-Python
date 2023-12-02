player_info = dict()
goal = list()
team = list()

while True:
    player_info['name'] = str(input("Player's name: "))
    matches = int(input("Matches played: "))
    goal.clear()
    for c in range(matches):
        goal.append(int(input(f"How many goal in game {c+1}? ")))
    player_info['goals'] = goal[:]
    player_info['t_goals'] = sum(goal)
    team.append(player_info.copy())
    player_info.clear()
    while True:
        choice = str(input("Continue [Y/N]? ")).upper()[0]
        if choice in 'SN':
            break
        print("ERROR! Please typed only Y or N.")
    if choice in 'N':
        break
print('-' * 35)


for k, v in enumerate(team):
    print(f"{k+1:>4} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()


while True:
    search = int(input("Show the data of which player? (999 to stop) "))
    if search == 999:
        break
    if search >= len(team):
        print(f"ERROR! There is no player with code {search}!")
    else:
        print(f" -- PLAYER'S DATA {team[search]['name']}:")
        for i, g in enumerate(team[search]['goals']):
            print(f"    In the game {i+1} got {g} goals.")

print('END')
