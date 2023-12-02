data = list()

while True:
    name = (str(input('Type the student name: ')))
    n1 = (float(input('Grade 1: ')))
    n2 = (float(input('Grade 2: ')))
    average = (n1 + n2) / 2
    data.append([name, [n1, n2], average])  # the list on append
    ch = str(input('Continue [Y/N]? ')).strip()[0]
    if ch in 'Nn':
        break
print('-' * 30)
print(f'{"Noº":<4}{"NAME":<10}{"AVERAGE":>8}')
print('-' * 26)
for i, s in enumerate(data):
    print(f'{i:<4}{s[0]:<10}{s[2]:>8.1f}')
while True:
    print('-' * 30)
    opt = int(input("Show which student's grades? (999 to stop)? "))
    if opt == 999:
        print('FINISHING...')
        break
    elif opt <= len(data) - 1:
        print(f'Grades of {data[opt][0]} are {data[opt][1]}')
print('<<< COME BACK ANYTIME >>>')
