resp = 'S'
soma = quant = average = major = smaller = 0
while resp in 'S':
    num = int(input('Type a number: '))
    soma += num
    quant += 1
    if quant == 1:
        major = smaller = num
    else:
        if num > major:
            major = num
        if num < major:
            smaller = num
    resp = str(input('Do you want to continue [S/N]? ')).upper().strip()[0]
average = soma / quant
print('You typed {} numbers and the average is {}'.format(quant, average))
print('The major value was {} and the smaller value was {}'.format(major, smaller))
print('end')

