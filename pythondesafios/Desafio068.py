from random import randint
print(40 * '=-')
print('VAMOS JOGAR PAR OU ÍMPAR')
print(40 * '=-')
cont = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    paimp = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    soma = jogador + computador
    if paimp == 'P' and soma % 2 == 0:
        cont += 1
        print(20 * '-')
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR.')
        print(20 * '-')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print(20 * '-')
    elif paimp == 'I' and soma % 2 != 0:
        cont += 1
        print(20 * '-')
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        print(20 * '-')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print(20 * '-')
    elif paimp == 'P' and soma % 2 != 0:
        print(20 * '-')
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        print(20 * '-')
        print('Você PERDEU!')
        break
    elif paimp == 'I' and soma % 2 == 0:
        print(20 * '-')
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
        print(20 * '-')
        print('Você PERDEU!')
        break
print(40 * '=-')
print(f'GAME OVER! Você venceu {cont} vez(es).')
