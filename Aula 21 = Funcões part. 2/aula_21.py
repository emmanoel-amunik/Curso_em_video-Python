# docstrings and optional parameters


def somar(a=0, b=0, c=0):
    """
    -> Sum three values and displays the result on the screen.
    :param a: first value
    :param b: second value
    :param c: third value
    """
    s = a + b + c
    print(f"The sum will be {s}")


somar(3, 3, 5)
somar(b=4, c=2)


# help

help(input)
# or
print(input.__doc__)
# or on terminal


def test(b):
    global a  # this will change "5" for "8" making this "a" as global.
    a = 8
    b += 4
    c = 2
    print(f"A inside valley {a}")
    print(f"B inside valley {b}")
    print(f"C inside valley {c}")


a = 5
test(a)
print(f"A outside valley {a}")


# return

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f"The results was {r1}, {r2} and {r3}.")
