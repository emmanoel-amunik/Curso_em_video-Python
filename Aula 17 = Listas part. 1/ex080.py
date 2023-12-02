values = list()
for v in range(0, 5):
    n = int(input('Type a number: '))
    if v == 0 or n > values[-1]:  # if the element is 0 or "n" is max than the last in values
        values.append(n)
        print('Added at the end of the list...')
    else:
        pos = 0
        while pos < len(values):
            if n <= values[pos]:
                values.insert(pos, n)
                print(f'Added at position {pos} of the list')
                break
            pos += 1
print('-' * 30)
print(f'The values entered in order are {values}')
print(f'{len(values)}')
