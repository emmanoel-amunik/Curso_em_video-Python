from random import randint
from time import sleep
num = randint(0, 10)
print('===' * 20)
print('I wll think a number between 0 and 10. Try to guess...')
print('===' * 20)
print('Guess the number between 0 and 10 chosen by the computer: ')
hit = False
while not hit:
    user = int(input('What is your guess? '))
    print('PROCESSING...')
    sleep(0.5)
    if user == num:
        hit = True
    else:
        print('Wrong! Try again', end='. ')
print('You are right! The number was {}'.format(num))
