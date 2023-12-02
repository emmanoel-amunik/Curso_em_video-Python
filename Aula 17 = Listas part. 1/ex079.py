values = list()
while True:
    v = (int(input('Type a value: ')))
    if v not in values:
        values.append(v)
        print('Value added successfully...')
    else:
        print('Duplicate value! Not added...')
    ch = input('Continue? [Y/N] ').upper().strip()
    while ch not in 'NY':
        ch = input('Wrong! Continue? [Y/N] ').upper().strip()
    if ch in 'N':
        break
print('-' * 30)
print(f'The values entered in ascending order are {sorted(values)}')
