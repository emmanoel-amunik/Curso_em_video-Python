# Average
n1 = float(input('Type the first grade:'))
n2 = float(input('Type the second grade:'))
a = (n1 + n2) / 2
if a < 5:
    print('Your average is {} and you are REPROVED.'.format(a))
elif a < 6.9:
    print('Your average is {} and you are in RECOVERING.'.format(a))
else:
    print('Your average is {} and you are APPROVED.'.format(a))
