from random import randint
from time import sleep
lista = list()
mega = list()
print('-' * 40)
print('            JOGO DA MEGA SENA     ')
print('-' * 40)
sorteios = int(input('Quantos jogos você deseja sortear? : '))
for s in range(0, sorteios):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    mega.append(lista[:])
    lista.clear()
print('-=' * 3, f'SORTEANDO {sorteios} JOGOS', '-=' * 3)
for i, f in enumerate(mega):
    print(f'Jogo {i + 1}: {f}')
    sleep(1)
print('-=' * 10, 'BOA SORTE', '-=' * 10)