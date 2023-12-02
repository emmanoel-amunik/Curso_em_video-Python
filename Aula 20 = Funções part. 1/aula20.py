def soma(a, b):
    s = a + b
    print(s)


# Optimized main program
soma(4, 5)
soma(8, 9)
soma(2, 1)


def soma_2(a, b):
    print(f"A = {a} and B = {b}")
    s = a + b
    print(f"The sum A + B = {s}")


# Main program
soma_2(a=4, b=5)
soma_2(b=4, a=5)

"""
# Main program
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s) 
"""


# --------------------------------------------------

def counter_1(*num):  # "*" will create a Tuple with all values
    for value in num:
        print(f"{value} ", end='')
    print("END!")

    size = len(num)
    print(f"The values of {num} were received and in all they are {size} numbers")


counter_1(2, 1, 7)
counter_1(8, 0)
counter_1(4, 4, 7, 5, 2)


# ---------------------------------------------------
def double(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


values = [3, 4, 2, 7, 8, 1, 9, 3]
double(values)
print(values)
