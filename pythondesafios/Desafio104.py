def leiaint(msg):
    valor = 0
    ok = False
    while True:
        global n
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Program principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
