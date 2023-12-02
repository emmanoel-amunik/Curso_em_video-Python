print('\033[0;30;41m Helo, World! \033[m')
a = 3
b = 5
print('The values are \033[32m{}\033[m and \033[35m{}\033[m!!!'.format(a, b))

# collection or dictionary

name = 'Joe'
colors = {'clean': '\033[m', 'blue': '\033[33m', 'yellow': '\033[33m', 'bw': '\033[7;30m'}
print('Helo! Nice to meet you, {}{}{}!!'.format(colors['bw'], name, colors['clean']))
