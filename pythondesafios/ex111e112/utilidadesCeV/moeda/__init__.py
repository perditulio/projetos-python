def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda (preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, aumenta=0, diminui=0):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'{"Preço analisado:":<20}{moeda(preço):>20}')
    print(f'{"Dobro do preço:":<20}{dobro(preço, True):>20}')
    print(f'{"Metade do preço:":<20}{metade(preço, True):>20}')
    print(f'{f"{aumenta}% de aumento:":<20}{aumentar(preço, aumenta, True):>20}')
    print(f'{f"{diminui}% de redução:":<20} {diminuir(preço, diminui, True):>19}')
    print('-' * 40)
