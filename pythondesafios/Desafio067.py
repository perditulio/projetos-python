n = 0
while True:
    n = int(input('Digite o número que você deseja saber sua tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        resultado = c * n
        print(f'{n} x {c} = {resultado}')
print('Programa interrompido, você digitou um número negativo.')
