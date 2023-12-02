salary = float(input("What's the employee's salary?"))
if salary >= 1250.00:
    n = (salary * 10 / 100) + salary
else:
    n = (salary * 15 / 100) + salary
print('After the increase, the salary will be R${:.2f}'.format(n))
