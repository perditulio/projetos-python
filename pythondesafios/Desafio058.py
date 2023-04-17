from random import randint
from time import sleep
tentativas = 0
print('========= JOGO DE ADIVINHAÇÃO =========')
pc = randint(0, 10)
jogada = int(input('\033[1;33m Pensei em um número! Digite o seu palpite: '))
print('PROCESSANDO...')
sleep(1)
while jogada != pc:
    print('\033[1;31m Você errou!')
    if jogada < pc:
        print('\033[1;33mTente um número mais alto.')
    else:
        print('\033[1;33mTente um número mais baixo.')
    jogada = int(input('\033[1;33mTente outro palpite: '))
    tentativas +=1
    print('\033[1;33mPROCESSANDO...')
    sleep(1)
print('\033[1;32mVocê venceu! Parabéns!! O número que pensei era o {}.'.format(pc))
print('Foram necessárias {} tentivas para acertar.'.format(tentativas + 1))
