from random import choice

n1 = str(input('First student:'))
n2 = str(input('Second student:'))
n3 = str(input('Third student:'))
n4 = str(input('Fourth student:'))
lista = [n1, n2, n3, n4]
chosen = choice(lista)
print(f'The chosen student was: {chosen}')
