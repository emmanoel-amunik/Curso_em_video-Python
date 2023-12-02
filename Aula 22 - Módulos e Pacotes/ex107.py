from useful import currency

price = float(input("Type a price: $ "))

print(f"The half of ${price} is ${currency.half(price):.2f}")
print(f"The double of ${price} is ${currency.double(price):.2f}")
print(f"Increasing 10%, we have ${currency.increase(price, 10):.2f}")
print(f"Decreasing 13%, we have ${currency.decrease(price, 13):.2f}")
