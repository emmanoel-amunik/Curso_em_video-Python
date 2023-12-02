soma = 0
cont = 0
for c in range(1, 7):
    m = int(input('Type the {}° value: '.format(c)))
    if m % 2 == 0:
        soma += m
        cont += 1
print('You informed {} PAIR values and the sum is {}'.format(cont, soma))
