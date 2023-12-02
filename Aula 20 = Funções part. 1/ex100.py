from random import randint
from time import sleep


def sort(num_list):
    print("Drawing 5 values form the list: ", end='')
    for cont in range(0, 5):
        num = randint(1, 10)
        num_list.append(num)
        print(f"{num} ", end='')
        sleep(0.3)
    print("DONE!")


def sum_even(num_list):
    soma = 0
    for value in num_list:
        if value % 2 == 0:
            soma += value
    print(f"Adding the even values of {num_list}, we have {soma}")


numbers = list()
sort(numbers)
sum_even(numbers)
