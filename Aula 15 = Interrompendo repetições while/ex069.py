tot18 = totM = totW20 = 0
while True:
    print('-' * 20)
    print('REGISTER A PERSON')
    print('-' * 20)
    age = int(input('Age: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sex: [M/F] ')).strip().upper()
    if age >= 18:
        tot18 += 1
    if sex == 'M':
        totM += 1
    if sex == 'F' and age < 20:
        totW20 += 1
    ch = ' '
    while ch not in 'NY':
        ch = str(input('Want to continue? [Y/N] ')).strip().upper()
    if ch == 'N':
        break
print(f'The total of people with 18 years old or more: {tot18}.')
print(f'The total of men registered is {totM}.')
print(f'The total of women under 20 years old is {totW20}.')
