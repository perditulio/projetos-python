p = float(input('Informe o preço do produto: '))
d = p - (p * 0.05)
print('Na liquidação, este produto terá um desconto de 5%, resultando no valor de R${:.2f}.'.format(d))
