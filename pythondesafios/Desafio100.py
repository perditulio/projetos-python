from random import randint
from time import sleep

valores = list()
pares = list()
par = soma = sorteion = 0


def sorteio(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for valor in lst:
        sleep(0.25)
        print(valor, end=' ')
    print('PRONTO!')


def somaPar(list):
    print(f'Somando os valores pares de {list}, temos {soma}')



for c in range(0, 5):
    sorteion = randint(0, 10)
    valores.append(sorteion)
    if sorteion % 2 == 0:
        par = sorteion
        soma += sorteion
        pares.append(par)
sorteio(valores)
somaPar(pares)
