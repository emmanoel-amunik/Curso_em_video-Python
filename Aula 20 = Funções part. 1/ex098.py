from time import sleep


def counter(start, end, step):

    if step < 0:
        step *= -1

    if step == 0:
        step = 1

    print('-' * 20)
    print(f"Count from {start} to {end} from {step} to {step}")

    if start < end:
        cont = start

        while cont <= end:
            print(f"{cont}", end=' ')
            sleep(0.3)
            cont += step
        print("END!")

    elif start > end:
        cont = start

        while cont >= end:
            print(f"{cont}", end=' ')
            sleep(0.3)
            cont -= step
        print("END!")


counter(1, 10, 1)
counter(10, 0, 2)
print('-' * 20)

print("Now is your turn to customize the count!")
c_start = int(input("Start: "))
c_end = int(input("End: "))
c_step = int(input("Step: "))
counter(c_start, c_end, c_step)
