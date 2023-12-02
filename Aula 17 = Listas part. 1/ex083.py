expr = str(input('Type an expression: '))
pile = list()
for simb in expr:
    if simb == '(':
        pile.append('(')
    elif simb == ')':
        if len(pile) > 0:
            pile.pop()
        else:
            pile.append(')')  # It's necessary or in this case "(2.(2+3).2(4)))" d be valid
            break
if len(pile) == 0:
    print('Your expression is valid!')
else:
    print('Your expression is wrong!')
