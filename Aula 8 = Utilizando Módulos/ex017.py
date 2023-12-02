"""
co = float(input('Opposite side length:'))
ca = float(input('Adjacent side length:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('The hypotenuse will measure {:.2f}'.format(hi))
"""

from math import hypot

co = float(input('Opposite side length:'))
ca = float(input('Adjacent side length:'))
hi = hypot(co, ca)
print('The hypotenuse will measure {:.2f}'.format(hi))
