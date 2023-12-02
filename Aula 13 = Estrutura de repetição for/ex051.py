first = int(input('First term: '))
ratio = int(input('Ratio: '))
tenth = first + (10 - 1) * ratio
for c in range(first, tenth + ratio, ratio):
    print('{} '.format(c), end='→ ')
print('end')
