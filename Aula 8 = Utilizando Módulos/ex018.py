from math import sin, radians, cos, tan

angle = float(input('Type the angle:'))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))
print('The angle of {}° has the sine of {:.2f},'.format(angle, sine), end=' ')
print('the cosine of {:.2f} and the tangent of {:.2f}.'.format(cosine, tangent))
