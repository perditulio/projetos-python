from time import sleep


def lin():
    print('-=' * 20)


def maior(*núm):
    print('Analisando os valores passados...')
    tam = len(núm)
    for valor in núm:
        sleep(0.25)
        print(valor, end=' ')
    print(f' Foram informados {tam} valores ao todo')
    nmaior = max(núm)
    print(f'O maior valor informado foi {nmaior}.')


maior(2, 9, 4, 5, 7, 1)
lin()
maior(4, 7, 0)
lin()
maior(1, 2)
lin()
maior(6)
lin()
maior(0)
lin()
