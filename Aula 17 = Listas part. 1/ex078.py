values = list()
for v in range(0, 5):
    values.append(int(input(f'Type a value to position {v}: ')))
print('-' * 30)
print(f'You entered the values {values}')
print(f'The major value typed is {max(values)} in positions ', end='')
for i, v in enumerate(values):  # i == index/position  v == value
    if v == max(values):
        print(f'{i}...', end='')
print()
print(f'The minor value typed is {min(values)} in positions ', end='')
for i, v in enumerate(values):
    if v == min(values):
        print(f'{i}...', end='')
print()
