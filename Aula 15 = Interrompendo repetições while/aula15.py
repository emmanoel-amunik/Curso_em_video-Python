"""
cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('end')

# but if I put TRUE, this will happen forever

cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1

n = s = 0
while True:
    n = int(input('Type a number:'))
    if n == 999:
        break
    s += n
print(f'The sun is {s}')
"""
# f strings
name = 'Phill'
age = 33
wage = 987.3
print(f'The {name} has {age} years old.')
print('The {} has {} years old.'.format(name, age))
print(f'The {name:^10} has {age} years old and earn R${wage:.2f}.')
