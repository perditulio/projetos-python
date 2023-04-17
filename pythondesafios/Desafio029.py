v = float(input('A que velocidade você passou com o seu carro?: '))
multa = (v - 80) * 7
if v > 80:
    print('Você excedeu o limite de velocidade permitido e deverá pagar uma multa de R${:.2f}'.format(multa))
print('Dirija com segurança! ')
