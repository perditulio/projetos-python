d = float(input('Digite qual será a distância a percorrer em sua viagem: '))
d1 = 0.5 * d
d2 = 0.45 * d
if d <= 200:
    print('O valor a pagar pela viagem é de R${:.2f} \n Viagem de até 200Km.'.format(d1))
else:
    print('O valor a pagar pela viagem é de R${:.2f} \n Viagem de mais de 200Km.'.format(d2))
