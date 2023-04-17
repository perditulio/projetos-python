r1 = float(input('Insira o compriemnto de uma reta: '))
r2 = float(input('Insira o comprimento de outra reta: '))
r3 = float(input('Insira o comprimenta de mais uma reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Essas 3 retas podem formar um triângulo.')
else:
    print('Essas 3 retas são impossíveis de formar um triângulo.')
