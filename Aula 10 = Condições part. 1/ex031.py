dist = float(input('What is the travel distance?'))
if dist <= 200:
    price = dist * 0.50
else:
    price = dist * 0.45
# or the simplified mode, but not for everyone
# price = dist * 50 if dist <= 200 else dist * 0.45
print('The ticket price will be R${:.2f}'.format(price))
