s = 0
cont = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
        cont += 1
print('O somatório de todos os números ímpares, múltiplos de 3, até 500 é: {}.'.format(s))
print('Foram somados {} valores.'.format(cont))
