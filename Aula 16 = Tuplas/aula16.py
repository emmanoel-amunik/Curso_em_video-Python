snack = ('Hamburger', 'Juice', 'Pizza', 'Pudding')
# Tuples
print(snack)  # all
print(snack[1])  # only Juice
print(snack[1:])  # from Juice onwards
print(snack[1:3])  # from Juice to Pizza
print(snack[:2])  # starting in Pizza
print(snack[-2:])  # starting in Pizza and going to the beginning
print(sorted(snack))  # to put the tuple in order

# Tuples are IMMUTABLES!!!!!!! but you can delete it

# snack[1] = 'Soda'
# print(snack[1])

pop = (1, 4, 5)
del pop

# ---------organizing and enumerating tuples-------------

snack = ('Hamburger', 'Juice', 'Pizza', 'Pudding')

for food in snack:  # the basic
    print(f"I'll eat {food}!")

for food, pos in enumerate(snack):  # 1º method
    print(f"I'll eat {food} in position {pos}")  # to enumerate

for cont in range(0, len(snack)):  # 2º method
    print(f"I'll eat {snack[cont]} in position {cont}")  # to enumerate

# ---------adding tuples----------

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # the order changes the result
print(c)
print(len(c))  # the number of elements in this tuple
print(c.count(5))  # how many times "5" appear in this tuple
print(c.index(8))  # what position is the 8 in
print(c.index(5, 1))  # position with displacement (starting from position "1")

# --------letters and numbers--------

person = ('John', 39, 'M', 99.88)
print(person)
