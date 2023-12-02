def factorial(num=1):
    fac = 1
    for count in range(num, 0, -1):
        fac *= count
    return fac


number_1 = int(input("Type a number: "))
print(f"The factorial of {number_1} is equal to {factorial(number_1)}")

f1 = factorial(5)
f2 = factorial(4)
f3 = factorial(1)
print(f"The results are {f1}, {f2} and {f3}.")


def even(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


number = int(input("Type a number: "))

if even(number):
    print("It's even!")
else:
    print("It's not even!")
