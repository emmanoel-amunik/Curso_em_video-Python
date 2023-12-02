price = float(input('What is the price of the product? '))
payment = str(input('What is the payment method? ')).strip().upper()
if payment == "CREDIT CARD":
    install = int(input('How many installments are you going to pay? '))
    if payment == 'CREDIT CARD' and install == 1:
        print('The value with a 5% discount will be R${:.2f} '.format(price - (price * 5 / 100)))
    elif payment == 'CREDIT CARD' and install == 2:
        print('The value will not be discounted and will be R${:.2f}'.format(price))
    elif payment == 'CREDIT CARD' and install > 2:
        print('The value with 20% interest will be {:.2f}'.format(price + (price * 20 / 100)))
elif payment == 'CASH' or 'CHECK':
    print('The value with 10% discount will be R${:.2f}'.format(price - (price * 10 / 100)))
