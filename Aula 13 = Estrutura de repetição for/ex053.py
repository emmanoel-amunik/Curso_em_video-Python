phrase = str(input('Type a phrase: ')).strip().upper()
words = phrase.split()
comb = ''.join(words)
reverse = ''

# or we can use "reverse = comb[::-1]" instead of "for"

for letter in range(len(comb) - 1, -1, -1):
    reverse += comb[letter]
print('The reverse of {} is {}'.format(comb, reverse))
if reverse == comb:
    print('We have a palindrome!')
else:
    print('The typed phrase is not a palindrome!')
