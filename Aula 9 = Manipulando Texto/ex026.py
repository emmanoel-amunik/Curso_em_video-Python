phrase = str(input('Type a phrase: ')).strip().upper()
print('The letter "A" appears {} times in the phrase.'.format(phrase.count('A')))
print('The first letter "A" appears at position {} '.format(phrase.find('A')+1))
print('The last letter "A" appears at position {}'.format(phrase.rfind('A')+1))
