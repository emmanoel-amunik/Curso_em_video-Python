lw = float(input('What is the width of the wall?'))
aw = float(input('What is the height of the wall?'))
a = lw * aw
p = a / 2
print('The area of this wall is {:.3f}m² and to paint it you will need {:.3f} liters of paint'.format(a, p))
