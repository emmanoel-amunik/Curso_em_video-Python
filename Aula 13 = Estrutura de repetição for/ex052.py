num = int(input('Type a number: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mThe number {} was divisible {} times'.format(num, tot))
if tot == 2:
    print("And that's why it's PRIME!")
else:
    print("And that's why isn't PRIME!")
