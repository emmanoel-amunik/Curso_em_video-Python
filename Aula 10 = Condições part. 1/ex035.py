s1 = float(input('Type the first straight:'))
s2 = float(input('Type the second straight:'))
s3 = float(input('Type the third straight:'))
if s3 < s1 + s2 and s2 < s1 + s3 and s1 < s2 + s3:
    print("It's possible to form a triangle.")
else:
    print("It's not possible.")
 