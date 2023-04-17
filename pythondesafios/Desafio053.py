frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
unir = ''.join(palavras)
inverso = ''
for letra in range(len(unir) - 1, -1, -1):
    inverso += unir[letra]
print('A frase que você digitou é {} e seu inverso é {}.'.format(unir, inverso))
if unir == inverso:
    print('Esta frase é um PALÍNDROMO!')
else:
    print('Esta frase NÃO É um PALÍNDROMO!')
