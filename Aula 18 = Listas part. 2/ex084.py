people = list()
data = list()
totp = 0
while True:
    people.append(str(input('Name: ')))
    totp += 1
    people.append(float(input('Weight: ')))
    data.append(people[:])
    people.clear()  # without this the data be duplicate.
    ch = str(input('Continue? [Y/N] ')).strip().upper()[0]
    if ch in 'N':
        break
over_weight = list()
under_weight = list()
for p in data:
    if p[1] >= 100:
        over_weight.append(p[0])
    elif p[1] <= 70:
        under_weight.append(p[0])

print(f'The total of people registered was {totp}')
print(f'The heaviest people are: {over_weight}')
print(f'The lightest people are: {under_weight}')
