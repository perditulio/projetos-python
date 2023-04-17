from time import sleep
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
print('''O que você deseja fazer?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do Programa''')
opção = int(input('Sua opção: '))
while opção != 5:
    if opção == 1:
        print('A soma entre {} e {} é {}.'.format(n1, n2, n1 + n2))
    elif opção == 2:
        print('O produto de {} e {} é {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            print('O maior número digitado é o {}.'.format(n1))
        elif n2 > n1:
            print('O maior número digitado é o {}.'.format(n2))
        else:
            print('Os números digitados tem o mesmo valor.')
    elif opção == 4:
        n1 = float(input('Digite um novo valor:'))
        n2 = float(input('Digite outro valor:'))
    elif opção > 5:
        print('Opção inválida, tente novamente.')
    sleep(1)
    print(40 * '=')
    print('''O que você deseja fazer?
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do Programa''')
    opção = int(input('Sua opção: '))
print('Você saiu do programa!')
