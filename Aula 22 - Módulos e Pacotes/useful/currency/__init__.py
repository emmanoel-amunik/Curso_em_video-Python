def c_format(value):
    return f'${value:.2f}'


def half(value, f=False):

    result = value / 2
    if f is True:
        form = c_format(result)
        return form

    return result


def double(value, f=False):

    result = value * 2

    if f is True:
        form = c_format(result)
        return form

    return result


def decrease(value, percentage, f=False):

    result = value - (value * percentage) / 100

    if f is True:
        form = c_format(result)
        return form

    return result


def increase(value, percentage, f=False):

    result = value + (value * percentage) / 100

    if f is True:
        form = c_format(result)
        return form

    return result


def summary(value, inc, dec):

    print("-" * 30)
    print("VALUE SUMMARY".center(30))
    print("-" * 30)

    print(f"Price analysing: \t{c_format(value)}")
    print(f"Double price: \t{double(value, True)}")
    print(f"{inc}% increasing: \t{increase(value, inc, True)}")
    print(f"{dec}% decreasing: \t{decrease(value, dec, True)}")

    print("-" * 30)
