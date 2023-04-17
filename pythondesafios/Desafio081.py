lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    cont += 1
    lista.append(n)
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if opcao == 'N':
        break
print(40 * '-=')
lista.sort(reverse=True)
print(f'Foram digitados {cont} valores.')
print(f'Valores em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('Não encontrei o valor 5 na lista.')
