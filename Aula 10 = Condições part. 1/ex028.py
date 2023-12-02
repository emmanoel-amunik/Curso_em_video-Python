from random import randint
from time import sleep
num = randint(0, 5)
print('===' * 20)
print('I wll think a number between 0 and 5. Try to guess...')
print('===' * 20)
user = int(input('Guess the number between 1 and 5 chosen by the computer: '))
print('PROCESSING...')
sleep(1)
if num == user:
    print('You are right! The number was {}'.format(num))
else:
    print('You are wrong! The number was {}. Try again.'.format(num))
