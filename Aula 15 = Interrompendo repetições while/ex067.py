while True:
    n = int(input('Do you want to see the table of what value? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('Negative number entered. Table closed.')
