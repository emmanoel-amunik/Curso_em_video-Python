from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10))
print(f'The numbers are {num}')
print(f'The major valor is {max(num)}')
print(f'The minor valor is {min(num)}')
