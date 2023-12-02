test = list()
test.append('Gus')
test.append(20)
crowd = list()
crowd.append(test[:])  # copying the list
test[0] = 'Maria'
test[1] = 22
crowd.append(test[:])
print(crowd)
# -----------------------------------------------------

galley = [['John', 19], ['Ana', 33], ['Max', 13], ['Maria', 45]]
print(galley[2][1])
for p in galley:
    print(p)
    print(p[0])  # only the names
    print(f'{p[0]} has {p[1]} years old.')
# ------------------------------------------------------

galley = list()
data = list()
totmai = totmen = 0
for c in range(0, 3):
    data.append(str(input('Name: ')))
    data.append(int(input('Age: ')))
    galley.append(data[:])  # copy
    data.clear()

for p in galley:  # checking the ages
    if p[1] >= 21:
        print(f'{p[0]} is of legal age')
        totmai += 1  # counting
    else:
        print(f'{p[0]} is underage')
        totmen += 1  # counting

print(f' We have {totmai} of legal age and {totmen} underage')
