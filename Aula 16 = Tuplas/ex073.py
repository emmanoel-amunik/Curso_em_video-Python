table = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthias', 'Flamengo',
         'Athletico Paranaense', 'Atlético Mineiro', 'Fortaleza', 'São Paulo',
         'América Mineiro', 'Botagofo', 'Santos', 'Goiás', 'Bragantina',
         'Coritiba', 'Cuiabá', 'Ceará', 'Atlético Goianiense', 'Avaí', 'Juventude')
print('-' * 90)
print(f'The top 5 are {table[:5]}')
print('-' * 90)
print(f'The las 4 are {table[-4:]}')
print('-' * 90)
print(sorted(table))
print('-' * 90)
print(f'The Fortaleza is in position {table.index("Fortaleza")+1} in the table.')
