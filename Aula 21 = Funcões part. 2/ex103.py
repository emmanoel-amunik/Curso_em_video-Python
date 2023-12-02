def token(player='<unknown>', goals=0):
    print(f"The player {player} scored {goals} goal(s) in the championship.")


player_name = str(input("Player's name: "))
total_goals = str(input("Goals: "))

if total_goals.isnumeric():
    total_goals = int(total_goals)
else:
    total_goals = 0

if player_name.strip() == '':
    token(goals=total_goals)
else:
    token(player_name, total_goals)
