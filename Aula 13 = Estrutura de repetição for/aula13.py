for c in range(0, 6):  # to print 'hi' 6 times
    print('Hi')
print('End.')

for c in range(1, 7):  # to count 1 to 6
    print(c)
print('End')

for c in range(6, 0, -1):  # to count 6 to 0
    print(c)
print('End')

n = int(input('Type a number: '))  # to count from 0 to {}
for c in range(0, n+1):
    print(c)
print('End')

s = int(input('Start: '))  # to count using values inserted by the user
e = int(input('End: '))
st = int(input('Step: '))
for c in range(s, e+1, st):
    print(c)
print('End')

s = 0
for c in range(0, 4):       # to count and add the values
    n = int(input('Type a number: '))
    s += n  # same as "s = n + s"
print('The sum of all values is {}'.format(s))
