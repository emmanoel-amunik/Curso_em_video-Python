people_info = dict()
data = list()
soma = media = 0
while True:
    people_info['name'] = str(input("Name: "))
    while True:
        people_info['sex'] = str(input("Sex [M/F]: ")).upper()[0]
        if people_info['sex'] in 'MF':
            break
        print("ERROR! Please, type only M or F.")
    people_info['age'] = int(input("Age: "))
    soma += people_info['age']
    data.append(people_info.copy())
    people_info.clear()
    while True:
        choice = str(input("Continue [Y/N]? ")).upper()[0]
        if choice in 'YN':
            break
        print("ERROR! Please, type only Y or N.")
    if choice in 'N':
        break

total_p = len(data)
media = soma / len(data)
print(f"The number of people registered is {total_p}")
print(f"The average of ages is {media:5.2f} years old.")

print("The women registered are ", end='')
for p in data:
    if p['sex'] in 'F':
        print(f"{p['name']} ", end='')
print()

print("List of people who are above the average: ")
for p in data:
    if p['age'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print("<<< END >>>")
