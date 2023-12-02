numbers = (int(input('Type a number: ')),
           int(input('Type another number: ')),
           int(input('Type one more number: ')),
           int(input('Type the las number: ')))
print(f'You enter the values {numbers}')
if 9 in numbers:
    print(f'The number 9 appeared {numbers.count(9)} times.')
else:
    print(f'The number 9 is not listed.')
if 3 in numbers:
    print(f'The number 3 is in position {numbers.index(3)}')
else:
    print(f'The number 3 is not listed.')
for n in numbers:
    if n % 2 == 0:
        print(f'The pair values typed are {n}')
