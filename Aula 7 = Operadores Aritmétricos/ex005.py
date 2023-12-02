n = int(input('Type a number:'))
na = n - 1
ns = n + 1
print('The predecessor of {} is {} and the successor of {} is {}.'.format(n, na, n, ns))

# we can do it only putting (n-1) n (n+1) on .format, but the correct is create a variable
# the smaller the number of variables, the smaller the memory expenditure
# ------BUT----- not always. Sometimes we'll need the variables in the future
