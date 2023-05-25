def leiaDinheiro(preço):
    valor = 0
    ok = False
    while True:
        n = str(input(preço)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[0;31mERRO! "{n}" é um preço inválido!\033[m')
        else:
            ok = True
            return float(n)
        if ok:
            break


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
