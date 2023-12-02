print('AP Generator')
print('-=' * 10)
first = int(input('First term: '))
ratio = int(input('AP Ratio: '))
term = first
cont = 1
while cont <= 10:
    print('{} → '.format(term), end='')
    term += ratio
    cont += 1
print('end')
