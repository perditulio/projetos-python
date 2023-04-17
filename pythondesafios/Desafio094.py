dados = list()
mulheres = list()
pessoas = {}
soma = 0
media = 0
while True:
    pessoas['Nome'] = str(input('Nome: '))
    while True:
        pessoas["Sexo"] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoas["Sexo"] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    dados.append(pessoas.copy())
    if pessoas['Sexo'] == 'F':
        mulheres.append(pessoas['Nome'])
    while True:
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if opcao == "N":
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
media = soma/len(dados)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadatradas foram {mulheres}.')
print('D) Lista das pessoas que estão acima da média: ')
for p in dados:
    if p['Idade'] >= media:
        print('      ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
            print()
print('<<ENCERRADO>>')
