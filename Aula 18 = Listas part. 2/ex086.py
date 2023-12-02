head_quarters = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for li in range(0, 3):
    for c in range(0, 3):
        # "li" and "c" will direct the position to be filled
        head_quarters[li][c] = int(input(f'Type a value for [{li}, {c}]: '))
print('-' * 30)
for li in range(0, 3):
    for c in range(0, 3):
        # "li" and "c", now, will direct the position to be read
        print(f'[{head_quarters[li][c]:^5}]', end='')
    print()

"""

values = [[], [], []]
for r in range(0, 9):
    v = int(input(f'Type a value to: '))
    if len(values[0]) < 3:
        values[0].append(v)
    elif len(values[1]) < 3:
        values[1].append(v)
    elif len(values[2]) < 3:
        values[2].append(v)
print(f'[ {values[0][0]} ] [ {values[0][1]} ] [ {values[0][2]} ]')
print(f'[ {values[1][0]} ] [ {values[1][1]} ] [ {values[1][2]} ]')
print(f'[ {values[2][0]} ] [ {values[2][1]} ] [ {values[2][2]} ]')

"""
