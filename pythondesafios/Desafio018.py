from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que deseja calcular: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print(' Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f} '.format(seno,cosseno,tangente))
