numero = int(input('Digite um número: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[0;33m {}'.format(c), end='')
        tot += 1
    elif numero % c != 0:
        print('\033[0;31m {}'.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(numero, tot))
if tot == 2:
    print('Por isso este número é PRIMO.')
else:
    print('Por isso este número NÃO É PRIMO.')
