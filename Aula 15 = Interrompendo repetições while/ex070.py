totp = tot1k = minor = cont = 0
cheap = ''
while True:
    pn = str(input("What's the name of the product? ")).upper().strip()
    pp = float(input("What's the product price? $ "))
    cont += 1
    totp += pp
    if pp > 1000:
        tot1k += 1
    if cont == 1 or pp < minor:
        minor = pp
        cheap = pn
    ch = ' '
    print('-' * 25)
    while ch not in 'NY':
        ch = str(input('Want to continue? [Y/N] ')).strip().upper()[0]
        print('-' * 25)
    if ch in 'N':
        break
print(f'The total purchased is ${totp:.2f}')
print(f'The total of gods costing more than $1000 is {tot1k}')
print(f'The cheaper product is {cheap} and costs ${minor:.2f}')
