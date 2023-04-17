mais = homens = mulheres20 = 0
titulo = 'CADASTRE UMA PESSOA'
print(30 * '-')
print(titulo.center(30))
print(30 * '-')
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print(30 * '-')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print(30 * '-')
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    if idade > 18:
        mais += 1
    if continuar == 'N':
        break
fim = 'FIM DO PROGRAMA'
print(f'{fim:=^30}')
print(f'''Foram cadastradas {mais} pessoas com mais de 18 anos;
{homens} homens;
E {mulheres20} mulheres com menos de 20 anos.''')