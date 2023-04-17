casa = float(input('Qual o valor da casa que você pretende comprar? '))
salario = float(input('Informe o seu salário: '))
tempo = float(input('Em quantos anos você pretende pagar a casa?'))
prestaçao = casa / (tempo * 12)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, tempo))
print('A prestação mensal será de R${:.2f}'.format(prestaçao))
if prestaçao >= 0.3 * salario:
    print('NEGADO. Você não poderá realizar o empréstimo.')
else:
    print('EMPRÉSTIMO CONCEDIDO. Você segue nossas condições de emprétimo e poderá realizá-lo.')
