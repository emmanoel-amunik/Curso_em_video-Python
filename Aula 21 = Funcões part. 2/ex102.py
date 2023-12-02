def factorial(n, show=False):
    """
    -> Calculates the factorial of a number.
    :param n: The number to be calculated.
    :param show: (optional) Show or not the count.
    :return: The factorial value of a number.
    """
    f = 1

    for c in range(n, 0, -1):

        if show:
            print(c, end='')
            if c > 1:
                print(" x ", end='')
            else:
                print(' = ', end='')
        f *= c

    return f


print(factorial(5, show=True))
help(factorial)
