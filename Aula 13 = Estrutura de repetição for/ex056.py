suma = 0
average = 0
olderage = 0
oldername = ''
totwoman20 = 0
for p in range(1, 5):
    print('---- {}° PERSON ----'.format(p))
    name = str(input('Name: ')).strip()
    age = int(input('Age: '))
    sex = str(input('Sex [M/F]: ')).strip()
    suma += age
    if p == 1 and sex in 'Mm':
        olderage = age
        oldername = name
    if sex in 'Mm' and age > olderage:
        olderage = age
        oldername = name
    if sex in 'Ff' and age < 20:
        totwoman20 += 1
average = suma / 4
print("The average age of the group is {} years".format(average))
print("The older man has {} years old and his name is {}.".format(olderage, oldername))
print('In all there are {} women under 20 years old'.format(totwoman20))
