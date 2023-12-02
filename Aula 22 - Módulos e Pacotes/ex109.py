from useful import currency

price = float(input("Type the price: $ "))

print(f"The half of {currency.c_format(price)} is {currency.half(price, True)}")
print(f"The double of {currency.c_format(price)} is {currency.double(price, True)}")
print(f"Increasing 10%, we have {currency.increase(price, 10, True)}")
print(f"Decreasing 13%, we have {currency.decrease(price, 13, True)}")
