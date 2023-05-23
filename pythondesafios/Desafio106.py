from time import sleep
c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;43m',  # 2 - amarelo
     '\033[0;30;44m',  # 3 - azul
     '\033[0;30;45m',  # 4 - roxo
     '\033[0;30;42m',  # 5 - verde
     '\033[7;30m'      # 6 - branco
     )


def ajuda(a):
    título(f'Acessando o manual do comando \'{a}\'', 4)
    print(c[6], end='')
    (help(a))
    print(c[6], end='')
    sleep(2)
    return a


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[cor], end='')
    sleep(1)


# Program principal
título('SISTEMA DE AJUDA PyHELP', 5)
while True:
    opc = input(f'{c[0]}Digite o comando para ver as instruções (FIM para terminar): ')
    if opc.upper() == 'FIM':
        break
    else:
        ajuda(opc)
título('ATÉ LOGO', 1)
