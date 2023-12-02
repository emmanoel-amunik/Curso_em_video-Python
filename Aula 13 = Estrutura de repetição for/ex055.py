larger = 0
smaller = 0
for w in range(1, 6):
    weight = float(input('Weight of the {}° person: ').format(w))
    if w == 1:
        larger = weight
        smaller = weight
    else:
        if weight > larger:
            larger = weight
        if weight < smaller:
            smaller = weight
print('The larger weight read was {}Kg'.format(larger))
print('The smaller weight read was {}Kg'.format(smaller))
