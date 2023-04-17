pessoas = list()
dados = list()
pesadas = list()
leves = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print('=-' * 40)
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso cadastrado foi de {mai}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        pesadas.append(p[0])
        print(pesadas, end='')
    pesadas.clear()
print()
print(f'O menor peso cadastrado foi de {men}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        leves.append(p[0])
        print(leves, end='')
    leves.clear()
