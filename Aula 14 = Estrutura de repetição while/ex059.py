v1 = float((input('Type the FIRST value: ')))
v2 = float(input('Type the SECOND value: '))
a = 0
while a != 5:
    print("""    [1] sum
    [2] multiply
    [3] major
    [4] new numbers
    [5] exit""")
    a = int(input('>>>>>> What should be done? '))
    if a == 1:
        print('The sum of this values is {}'.format(v1 + v2))
    elif a == 2:
        print('The multiplication of this values is {}'.format(v1 * v2))
    elif a == 3:
        m = 0
        if v1 > v2:
            m = v1
        if v2 > v1:
            m = v2
        print('The major number of this values is {}'.format(m))
    elif a == 4:
        print('Input the numbers again:')
        v1 = float((input('Type the FIRST value: ')))
        v2 = float(input('Type the SECOND value: '))
    elif a == 5:
        print('processing...')
    else:
        print('ERROR')
    print('=-=' * 10)
print('end')
