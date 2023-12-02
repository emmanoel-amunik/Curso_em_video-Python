n1 = int(input('A value:'))
n2 = int(input('Other value:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
print('The sum is {}, the product is {}, the division is {:.3f},'.format(s, m, d), end=' ')
print('integer division {} and potency {}'.format(di, e))

