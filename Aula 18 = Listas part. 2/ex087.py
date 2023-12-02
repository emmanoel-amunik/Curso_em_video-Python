head_quarters = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totv = tott = 0
for li in range(0, 3):
    for c in range(0, 3):
        # "li" and "c" will direct the position to be filled
        head_quarters[li][c] = int(input(f'Type a value for [{li}, {c}]: '))
print('-' * 30)
for li in range(0, 3):
    for c in range(0, 3):
        # "li" and "c", now, will direct the position to be read
        print(f'[{head_quarters[li][c]:^5}]', end='')
        if head_quarters[li][c] % 2 == 0:
            totv += head_quarters[li][c]  # to sum, not count, the values
    print()
print('-' * 30)
print(f'The sum of the pair values is {totv}')
for li in range(0, 3):
    # the line is variable, but the column is fixe
    tott += head_quarters[li][2]
print(f'The sum of the values in the third column is {tott}')
print(f'The major values in the second line is {max(head_quarters[1])}')
