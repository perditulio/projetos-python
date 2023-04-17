n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
numeros = (n1, n2, n3, n4)
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primeiro valor 3 digitado está na posição {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for c in numeros:
    if c % 2 == 0:
       print(c, end=', ')
print('FIM')