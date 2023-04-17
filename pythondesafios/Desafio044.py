preço = float(input('Insira aqui o preço do produto: '))
pagamento = int(input('Se quiser pagar à vista com dinheiro/cheque digite "1", \nse quiser pagar à vista no cartão digite "2",\npara dividir em 2x digite "3" e para dividir em 3x ou mais digite "4": '))
cash = preço - (preço * 0.1)
acartao = preço - (preço * 0.05)
cartao3x = preço + (preço * 0.2)
if pagamento == 1:
    print('Você escolheu pagar à vista com dinheiro/cheque, portanto terá 10% de desconto.')
    print('O novo preço do produto é R${:.2f}.'.format(cash))
elif pagamento == 2:
    print('Você escolheu pagar à vista no cartão e terá 5% de desconto.')
    print('O novo preço do produto é de R${:.2f}.'.format(acartao))
elif pagamento == 3:
    print('Você escolheu pagar em até 2x no cartão, portanto o preço do produto permanece o mesmo: R${:.2f}'.format(preço))
elif pagamento == 4:
    print('Você escolheu pagar de até 3x ou mais no cartão, portanto terá de pagar 20% de juros.')
    print('Você deverá pagar o valor de R${:.2f}'.format(cartao3x))
