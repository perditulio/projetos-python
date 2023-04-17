titulo = 'BANCO DO TUGÃO'
print(40 * '=')
print(titulo.center(40))
print(40 * '=')
cinq = vinte = dez = um = 0
while True:
    valor = int(input('Qual o valor que você deseja sacar? R$'))
    while valor >= 1000:
        cinq += 20
        valor -= 1000
    while valor >= 100:
        cinq += 2
        valor -= 100
    while valor >= 50:
        cinq += 1
        valor -= 50
    while valor >= 20:
        vinte += 1
        valor -= 20
    while valor >= 10:
        dez += 1
        valor -= 10
    while valor >= 1:
        um += 1
        valor -= 1
    if valor == 0:
        break
print(f'''Total de {cinq} cédulas de R$50
Total de {vinte} cédulas de R$20
Total de {dez} cédulas de R$10
Total de {um} cédulas de R$1''')
print(40 * '=')
print(f'Vonte sempre ao {titulo}! Tenha um bom dia!')
