import math
num = int(input('Type a number:'))
root = math.sqrt(num)
print('The square root of {} equals to {}.'.format(num, math.ceil(root)))

from math import sqrt
num = int(input('Type a number:'))
root = sqrt(num)
print('The square root of {} equals to {:.2f}.'.format(num, root))

from math import sqrt, floor
num = int(input('Type a number:'))
root = sqrt(num)
print('The square root of {} equals to {:.2f}.'.format(num, floor(root)))

import random
num = random.randint(1, 100)
print(num)

import emoji
print(emoji.emojize('Hello, world! :globe_showing_Americas:', language='alias'))
