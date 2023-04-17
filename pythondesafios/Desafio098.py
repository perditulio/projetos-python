from time import sleep
def lin():
    print('-=' * 20)


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(0.25)
    print(inicio, end=' ')
    sleep(0.25)
    while True:
        if inicio != fim:
            if inicio > fim:
                if passo > 0:
                    inicio -= passo
                elif passo == 0:
                    passo = 1
                    inicio -= passo
                else:
                    inicio += passo
            elif inicio < fim:
                inicio += passo
            print(inicio, end=' ')
            sleep(0.25)
        elif inicio == fim:
            print('FIM!')
            break


lin()
contador(inicio=1, fim=10, passo=1)
lin()
contador(inicio=10, fim=0, passo=2)
lin()
contador(inicio=int(input('Início: ')), fim=int(input('Fim: ')), passo=int(input('Passo: ')))
lin()
