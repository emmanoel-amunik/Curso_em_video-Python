s = str(input('What is your sex? [M/F] ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Wrong! Try again: ')).strip().upper()[0]
print('end')
