geral = [[], []]
for c in range (1,8):
    valor = int(input(f'Digite o {c}o valor: '))
    if valor % 2 == 0:
        geral[0].append(valor)
    else:
        geral[1].append(valor)
print('-=' * 40)
geral[0].sort()
geral[1].sort()
print(f'Os valores pares são: {geral[0]}')
print(f'Os valores impares são: {geral[1]}')
