from datetime import date
year = int(input('Type the year or type 0 for the current year:'))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('The year of {} is a leap year.'.format(year))
else:
    print('The year of {} is not a leap year.'.format(year))
