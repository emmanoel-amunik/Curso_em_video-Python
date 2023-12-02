num = cont = soma = 0
num = int(input('Type a number [999 to stop]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Type a number [999 to stop]: '))
print('You entered {} numbers and the sum among them was {}'.format(cont, soma))
