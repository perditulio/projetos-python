import random
print('Vamos jogar Jokenpô??')
jogador = str(input('Escreva "pedra", "papel" ou "tesoura": ')).strip().capitalize()
opçoes = 'Pedra', 'Papel', 'Tesoura'
x = random.choice(opçoes)
if x == 'Pedra' and jogador == 'Pedra':
    print('EMPATE, ambos escolheram Pedra!')
elif x == 'Papel' and jogador == 'Papel':
    print('EMPATE, ambos escolheram Papel!')
elif x == 'Tesoura' and jogador == 'Tesoura':
    print('EMPATE, ambos escolheram Tesoura!')
elif x == 'Pedra' and jogador == 'Tesoura':
    print('VOCÊ PERDEU. O computador escolheu {}.'.format(x))
elif x == 'Tesoura' and jogador == 'Pedra':
    print('VOCÊ VENCEU. O computador escolheu {}.'.format(x))
elif x == 'Pedra' and jogador == 'Papel':
    print('VOCÊ VENCEU. O computador escolheu {}.'.format(x))
elif x == 'Papel' and jogador == 'Pedra':
    print('VOCÊ PERDEU. O computador escolheu {}.'.format(x))
elif x == 'Tesoura' and jogador == 'Papel':
    print('VOCÊ PERDEU. O computador escolheu {}.'.format(x))
elif x == 'Papel' and jogador == 'Tesoura':
    print('VOCÊ VENCEU. O computador escolheu {}.'.format(x))
