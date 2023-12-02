for c in range(1, 10):
    print(c)
print('end')

c = 1
while c < 10:
    print(c)
    c += 1
print('end')

r = 'S'
while r == 'S':
    n = int(input('Type a value: '))
    r = str(input('Want to continue? [S/N] ')).upper().strip()
print('end')

np = 1
par = impar = 0
while np != 0:
    np = int(input('Type a value:'))
    if np != 0:
        if np % 2 == 0:
            par += 0
        else:
            impar += 0
print('You typed {} pair numbers and {} odd numbers.'.format(par, impar))
print('end')
