# Military Enlist
from datetime import date
year = int(input('What is your birth year?'))
current = date.today().year
age = current - year
if age < 18:
    print('It is NOT time for you to enlist in the military service yet.')
    print('There are still {} years left before your enlistment'.format(18 - age))
elif age == 18:
    print('It is time for you enlist in the military service.')
else:
    print('It is about time you singed up for military service.')
    print('It is been {} years since you should have enlisted'.format(age - 18))
