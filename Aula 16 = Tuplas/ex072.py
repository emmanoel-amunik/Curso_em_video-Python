numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
           'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    num = int(input('Type a number between 0 and 20: '))
    if 0 <= num <= 20:
        break
    print('Tyr again', end='')
print(f'You typed the number {numbers[num]}')

# ---------- simplified -------------

numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
           'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

numb = int(input('Type a number between 0 and 20: '))

while numb not in range(0, 21):
    numb = int(input('Try again. Type a number between 0 and 20: '))
print(f'You typed the number {numbers[numb]}')
