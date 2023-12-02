from time import sleep


def major(*num):
    print("Analyzing the values...")
    sleep(1)

    for p in num:
        print(p, end=' ')
    print(f"A total of {len(num)} values were reported.")
    print(f"The major value is {max(num)}")
    print("-" * 50)


major(4, 5, 6, 3, 2, 4, 3, 6, 8, 7, 9)
major(4, 1, 2)
major(1, 2)
major(6)
major(1)
