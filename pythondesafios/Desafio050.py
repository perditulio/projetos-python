s = 0
for c in range(1, 7):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        s += n1
print('A soma dos números pares digitados é igual a: {}'.format(s))
