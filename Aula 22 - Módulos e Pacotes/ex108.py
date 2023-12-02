from useful import currency

price = float(input("Type the price: $ "))

print(f"The half of {currency.c_format(price)} is {currency.c_format(currency.half(price))}")
print(f"The double of {currency.c_format(price)} is {currency.c_format(currency.double(price))}")
print(f"Increasing 10%, we have {currency.c_format(currency.increase(price, 10))}")
