player_info = dict()
goal = list()
player_info['name'] = str(input("Player's name: "))
matches = int(input("Matches played: "))

for c in range(matches):
    goal.append(int(input(f"How many goal in game {c+1}? ")))
player_info['goals'] = goal[:]
player_info['t_goals'] = sum(goal)
print('-' * 35)

print(f"The player's name is {player_info['name']}")
print(f"The player's goals in the season are {player_info['goals']}")
print(f"The player's total of goals are {player_info['t_goals']}")
print('-' * 35)

print(f"The player {player_info['name']} played {matches} matches.")
for i, v in enumerate(player_info['goals']):
    print(f"     => In match {i+1}, he scored {v} goals.")
