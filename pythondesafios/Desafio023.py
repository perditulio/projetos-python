n1 = int(input('Digite um número de 0 a 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('Unidade(s): {}'.format(u))
print('Dezena(s): {}'.format(d))
print('Centena(s): {}'.format(c))
print('Milhare(s): {}'.format(m))
