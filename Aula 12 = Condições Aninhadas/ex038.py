n1 = int(input('Type the first value:'))
n2 = int(input('Type the second value:'))
if n1 > n2:
    print('The first value is the major.')
elif n2 > n1:
    print('The second value is the major.')
else:
    print('There is no major value. Both are the same.')
