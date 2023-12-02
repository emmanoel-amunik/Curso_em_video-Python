days = int(input('For how many days was the car rented?'))
km = float(input('How many kilometers were travelled?'))
p = (days * 60) + km * 0.15
print('The car rental price is U${:.2f}'.format(p))
