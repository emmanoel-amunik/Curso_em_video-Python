from datetime import date
year = int(input('What is the both year? '))
age = date.today().year - year
if age <= 9:
    print('The age is {} years and he is in the LITTLE category.'.format(age))
elif age <= 14:
    print('The age is {} years and he is in the CHILD category.'.format(age))
elif age <= 19:
    print('The age is {} years and he is in the JUNIOR category.'.format(age))
elif age <= 25:
    print('The age is {} years and he is in the SENIOR category.'.format(age))
else:
    print('The age is {} years and he is in the MASTER category.'.format(age))
