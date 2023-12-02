vel = float(input("What was the car's speed?"))
if vel > 80:
    print('The car was over the speed limit and will be fined.')
    print('The traffic ticket will be R${:.2f}'.format((vel - 80) * 7))
else:
    print('The car was within the limit.')
