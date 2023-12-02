def write(phrase):
    size = len(phrase) + 4
    print("~" * size)
    print(f"  {phrase}")
    print("~" * size)


write('Olá, Mundo!')
write('Gustavo Guanabara')
write('CeV')
