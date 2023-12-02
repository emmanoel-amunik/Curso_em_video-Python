from useful import numbers

num = int(input("Type a value: "))
fat = numbers.factorial(num)
print(f"The factorial of {num} is {fat}.")
print(f"The double of {num} is {numbers.double(num)}")
