cont = sun = 0
while True:
    n = int(input('Type a number (999 to stop): '))
    if n == 999:
        break
    cont += 1
    sun += n
print(f'You typed {cont} numbers and sun among them is {sun}')
