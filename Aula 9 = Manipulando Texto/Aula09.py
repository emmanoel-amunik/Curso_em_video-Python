frase = 'Curso em Video Python'
print(frase)
print(frase[3])
print(frase[3:9])
print(frase[:21])
print(frase[19:])
print(frase[1:15:3])
print(frase[1::3])
print(frase[::3])  # jumping letters
print(frase.count('o'))
print(frase.upper().count('O'))  # putting in uppercase n counting 'o'
print(frase.replace('Python', 'Android'))
# the replaced is only in this circumstance
# but, if I assign: "frase = frase.replace..." this command will be saved

print("""Nos exemplos seguintes, pode-se distinguir entrada e saída p
ela presença ou ausência dos prompts (>>> e …): para repetir o exe
mplo, você deve digitar tudo após o prompt, quando o mesmo aparece; linha
s que não começarem com um prompt são na verdade as saídas geradas pelo 
interpretador. Observe que quando aparece uma linha contendo apenas o pro
mpt secundário você deve digitar uma linha em branco; 
é assim que se encerra um comando de múltiplas linhas.""")  # all in the correct line

print('Curso' in frase)  # true or false
print(frase.find('Video'))

frase = 'Curso em Video Python'
divided = frase.split()
print(divided[2])
