name = str(input("What's your name? "))
if name == 'Gustavo':
    print('What a beautiful name you have!')
else:
    print('Your name is so normal!')
print('God Day, {}!'.format(name))

n1 = float(input('Type the first grade: '))
n2 = float(input('Type the second grade: '))
m = (n1 + n2)/2
print('Your average was {:.1f}'.format(m))
if m >= 6.0:
    print('Your average was good! Congrats!')
else:
    print('Your average was bad! Study more!')
