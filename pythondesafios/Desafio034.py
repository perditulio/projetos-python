salario = float(input('Qual é o seu salário? '))
mai = (salario * 0.1)
men = (salario * 0.15)
if salario > 1250:
    print('Seu salário terá um aumento de R${:.2f} '.format(mai))
    print('Seu novo salário é de R${:.2f}'.format(mai + salario))
else:
    print('Seu salário terá um aumento de R${:.2f} '.format(men))
    print('Seu novo salário será de R${:.2f} '.format(men + salario))
