from datetime import date
current = date.today().year
totalup = 0
totaldown = 0
for person in range(1, 8):
    born = int(input('What year was {}° person born in?'.format(person)))
    age = current - born
    if age >= 21:
        totalup += 1
    else:
        totaldown += 1
print('In all, we has {} people of legal age'.format(totalup))
print('In all, we had {} underage people'.format(totaldown))
