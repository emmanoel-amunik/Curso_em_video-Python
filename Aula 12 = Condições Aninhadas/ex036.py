# bank loan

house = float(input('What is the price of the house? R$'))
salary = float(input('What is your wage? R$'))
years = int(input('How many years? '))

install = house / (years * 12)

if install <= salary * 30 / 100:
    print('Your loan is approved.')
else:
    print('Your loan was not approved.')
