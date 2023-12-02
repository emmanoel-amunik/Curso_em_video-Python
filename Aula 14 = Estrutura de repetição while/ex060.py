n = int(input('Type a number to calculate its factorial: '))
c = n
f = 1
print('Calculating \033[1;35m{}!\033[m = '.format(c), end='')
while c > 0:
    print('\033[34m{} '.format(c), end='')
    print('\033[30mx ' if c > 1 else '\033[30m= ', end='\033[1;32m')
    f *= c
    c -= 1
print(f)
