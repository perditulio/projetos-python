from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for c in numeros:
    print(f'{c} ', end='')
print(f'\nO maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')
