palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'FUTEBOL', 'GLOBO', 'PREMIERE', 'GALO', 'VINGADOR',
            'BATMAN', 'AMERICA', 'BRASIL', 'NEYMAR')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end='; ')
