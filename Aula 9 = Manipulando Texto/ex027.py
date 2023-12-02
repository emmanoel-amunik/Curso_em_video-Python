name = str(input('Type the complete name:')).strip()
print('Nice to meet you!')
print('Your first name is {}'.format(name.split()[0]))
print('Your last name is {}'.format((name.split()[-1])))
