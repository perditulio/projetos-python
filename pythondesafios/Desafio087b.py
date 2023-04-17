matriz = []
linha1 = []
linha2 = []
linha3 = []
spar = scol = 0
for c in range(0,3):
    valores1 = int(input('Digite os valores da primeira linha da matriz: '))
    linha1.append(valores1)
    if valores1 % 2 == 0:
        spar += valores1
matriz.append(linha1[:])
for c in range(0,3):
    valores2 = int(input('Digite os valores da segunda linha da matriz: '))
    linha2.append(valores2)
    if valores2 % 2 == 0:
        spar += valores2
matriz.append(linha2[:])
for c in range(0,3):
    valores3 = int(input('Digite os valores da terceira linha da matriz: '))
    linha3.append(valores3)
    if valores3 % 2 == 0:
        spar += valores3
matriz.append(linha3[:])
print('-=' * 40)
print(f'''[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]''')
print('-=' * 40)
print(f'A soma dos números pares é igual a {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é igual a {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é igual a {mai}')