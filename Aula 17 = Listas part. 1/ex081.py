num = list()
while True:
    num.append(int(input('Type a number: ')))
    ch = str(input('Continue? [Y/N] ')).upper().strip()
    if ch in 'N':
        break
print('-' * 30)
print(f'{len(num)} numbers were entered')
num.sort(reverse=True)
print(f'The values sorted in descending order are {num} ')
if 5 in num:
    print('The value 5 was entered and is in the list')
else:
    print('The value 5 was not entered')
