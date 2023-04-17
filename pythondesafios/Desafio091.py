from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
for c in range(1,5):
    jogo[f'jogador{c}'] = randint(1, 6)
ranking = {}
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lygar: {v[0]} com {v[1]}.')