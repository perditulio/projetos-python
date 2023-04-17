s = float(input('Digite aqui o seu salário: '))
a = (s * 0.15)+ s
d = a - s
print('Caso haja um aumento de 15% do seu salário, você receberá R${:.2f} '.format(a))
print('A diferença do valor antigo para o valor com o aumento é de R${:.2f}'.format(d))
