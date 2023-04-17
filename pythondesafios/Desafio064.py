n = s = cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1
    s += n
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont - 1, s - 999))
