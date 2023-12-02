values = [[], []]
for v in range(0, 7):
    n = int(input(f'Type the {v+1}º value: '))
    if n % 2 == 0:
        values[0].append(n)
    elif n % 2 == 1:
        values[1].append(n)

values[0].sort()
values[1].sort()

print(f'The pair values entered are: {values[0]}')
print(f'The odd values entered are: {values[1]}')
