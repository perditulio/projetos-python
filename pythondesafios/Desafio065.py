numero = cont = s = maior = menor = 0
escolha = 'S'
while escolha != 'N':
    numero = int(input('Digite um número: '))
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if escolha != 'S' and escolha != 'N':
        escolha = str(input('Escolha inválida, digite entre [S/N]: ')).strip().upper()[0]
    cont += 1
    s += numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = s / cont
print('Você digitou {} números e a média foi {} .'.format(cont, media))
print('O maior valor foi {} e o menor foi {} .'.format(maior, menor))
