name = str(input('What is tour name?')).strip()
if name == 'Gustavo':
    print('What a cult name!')
elif name == 'Pedro' or 'Maria' or 'Paulo':
    print('Your name is very popular in Brazil.')
elif name in 'Ana Claudia Jessica Juliana':
    print('Beautiful female name.')
else:
    print('Your name is pretty normal.')
print('Have a good day, {}!'.format(name))
