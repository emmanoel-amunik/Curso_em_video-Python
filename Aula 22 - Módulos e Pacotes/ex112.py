from useful import currency
from useful import data

price = data.read_money("Type the price:")
currency.summary(price, 35, 22)
