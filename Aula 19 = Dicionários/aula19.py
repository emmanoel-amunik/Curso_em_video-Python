people = {'name': 'Gus', 'sex': 'M', 'age': 22}
print(people['name'])
print(f'{people["name"]} has {people["age"]} years old.')
print(people.keys())  # name sex age
print(people.values())  # Gus M 22
print(people.items())  # all

for k, v in people.items():
    print(f'{k} = {v}')

# changing
people['name'] = 'John'
# appending
people['weight'] = 98.5

# ---------------------------------------------------------------------------------

united_states = list()
state_1 = {'state': 'Alabama', 'acronym': 'AL'}
state_2 = {'state': 'Texas', 'acronym': 'TX'}
united_states.append(state_1)
united_states.append(state_2)

print(united_states[0]['state'])

# ---------------------------------------------------------------------------------

state = dict()
brazil = list()
for c in range(0, 3):
    state['state'] = str(input('Federative Unit: '))
    state['acronym'] = str(input('State acronym: '))
    brazil.append(state.copy())
for s in brazil:
    for v in s.values():
        print(v, end='-')
    print()  # to skip line
