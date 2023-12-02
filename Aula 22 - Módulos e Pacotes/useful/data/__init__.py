def read_money(msg):

    valid = False

    while not valid:

        t_input = str(input(msg)).replace(',', '.').strip()

        if t_input.isalpha() or t_input == '':
            print(f'ERROR: \"{t_input}\" is an invalid price.')
        else:
            valid = True

            return float(t_input)
