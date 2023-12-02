a = int(input('Type the first number:'))
b = int(input('Type the second number:'))
c = int(input('Type the third number:'))
# verifying the minor
minor = a
if b < a and b < c:
    minor = b
if c < a and c < b:
    minor = c
# verifying the major
major = a
if b > a and b > c:
    major = b
if c > a and c > b:
    major = c
print('The minor value typed was {}'.format(minor))
print('The major value typed was {}'.format(major))
