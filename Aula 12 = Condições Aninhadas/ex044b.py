price = float(input('What is the price of the product? R$'))
print('''Payment Methods
[ 1 ] Cash or Check
[ 2 ] Credit Card 
[ 3 ] 2x on Credit
[ 4 ] 3x or more on Credit''')
payment = int(input('What is the option? '))
if payment == 2:
    print('The value with a 5% discount will be R${:.2f} '.format(price - (price * 5 / 100)))
elif payment == 3:
    print('The value will not be discounted and will be R${:.2f}'.format(price))
elif payment == 4:
    print('The value with 20% interest will be {:.2f}'.format(price + (price * 20 / 100)))
elif payment == 1:
    print('The value with 10% discount will be R${:.2f}'.format(price - (price * 10 / 100)))
