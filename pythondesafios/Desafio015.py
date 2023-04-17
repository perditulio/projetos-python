t = int(input('Informe por quantos dias voê alugou o veículo: '))
d = float(input('Informe quantos quilômetros foram percorridos com o veículo: '))
f = 60 * t + 0.15 * d
print('Alugando o veículo por {} dias e percorrendo {}km, o valor a pagar será de R${:.2f}.'.format(t,d,f))
