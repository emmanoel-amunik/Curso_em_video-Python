values = list()
while True:
    values.append(int(input('Type a number: ')))
    ch = str(input('Continue? [Y/N] ')).strip().upper()
    if ch in 'N':
        break
p_num = list()
o_num = list()
for num in values:
    if num % 2 == 0:
        p_num.append(num)
    elif num % 2 == 1:
        o_num.append(num)

print(f'The entered list is {values}')
print(f'The pair numbers in the list are {p_num}')
print(f'The odd numbers in the list are {o_num}')
