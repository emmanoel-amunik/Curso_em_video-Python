print('AP Generator')
print('-=' * 10)
first = int(input('First term: '))
ratio = int(input('AP Ratio: '))
term = first
cont = 1
total = 0
more = 10
while more != 0:
    total += more
    while cont <= total:
        print('{} → '.format(term), end='')
        term += ratio
        cont += 1
    print('BREAK')
    more = int(input('Hoe many terms do you want to show more? '))
print('Finished progression with {} terms shown.'.format(total))
print('end')
