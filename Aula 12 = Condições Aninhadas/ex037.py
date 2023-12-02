num = int(input('Type a integer: '))
print('''Choose one of the bases for conversion:
[ 1 ] convert to BINARY
[ 2 ] convert to OCTAL
[ 3 ] convert to HEXADECIMAL''')
choice = int(input('Your choice: '))
if choice == 1:
    print('{} converted to BINARY equals {}'.format(num, bin(num)[2:]))
elif choice == 2:
    print('{} converted to OCTAL equals {}'.format(num, oct(num)[2:]))
elif choice == 3:
    print('{} converted to HEXADECIMAL equals {}'.format(num, hex(num)[2:]))
else:
    print('Invalid option')
