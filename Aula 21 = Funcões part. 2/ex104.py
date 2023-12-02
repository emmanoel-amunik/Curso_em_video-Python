def readint(msg):
    ok = False
    value = 0

    while True:
        n = str(input(msg))

        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print("\033[0;31mERROR! Type a valid integer.\033[m")

        if ok:
            break

    return value


number = readint('Type a number: ')
print(f"You entered the number {number}")
