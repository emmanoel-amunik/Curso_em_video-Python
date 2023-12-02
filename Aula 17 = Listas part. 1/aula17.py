num = [2, 5, 9, 1]
num[2] = 3  # to change the value of the element
num.append(7)  # to an element (in the end)
num.sort()  # to sort the list kkkk
num.sort(reverse=True)  # to sort the list backwards
num.insert(2, 0)  # in position "2" the value '0' will be added
num.pop()  # delete the las value
num.pop(2)  # delete the value in element "2"
num.remove(2)  # will remove the first value 2 in the list
print(num)
print(f'This list has {len(num)} elements.')  # self-explanatory
# -------------------------------------------------------------------

if 5 in num:
    num.remove(5)
else:
    print('number 5 not found')
# -------------------------------------------------------------------

values = list()
values.append(3)
values.append(4)
values.append(2)

for v in values:  # only to print the values
    print(f'{v}', end='')

for c, v in enumerate(values):  # to enumerate and print the values
    print(f'In position {c} I find the value {v}!')
# --------------------------------------------------------------------

values = list()
for cont in range(0, 5):  # to fill a list with user's inputs
    values.append(int(input('Type a value: ')))

for c, v in enumerate(values):  # to show the list entered by the user
    print(f'In position {c} I find the value {v}')
