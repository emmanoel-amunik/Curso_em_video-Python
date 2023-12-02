words = ('learning', 'program', 'language', 'python', 'course', 'free',
         'study', 'practice', 'work', 'marketplace', 'programmer', 'future')
for w in words:
    print(f'\nIn the word {w.upper()} we have ', end='')
    for letters in w:
        if letters.lower() in 'aeiou':
            print(letters, end=' ')
