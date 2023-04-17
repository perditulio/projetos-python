listagem = ('Mouse', 249.99,
            'Teclado', 349.99,
            'Monitor', 500,
            'Computador', 5549.9,
            'Mousepad', 150.47,
            'Headphone', 400.9,
            'Web Cam', 200,
            'Cadeira Gamer', 2339.99)
print(40 * '-')
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(40 * '-')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>8.2f}')
print(40 * '-')
