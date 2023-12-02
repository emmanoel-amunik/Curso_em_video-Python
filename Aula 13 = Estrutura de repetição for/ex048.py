su = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        su += c
print('The sum of all {} values is {}'.format(cont, su))
