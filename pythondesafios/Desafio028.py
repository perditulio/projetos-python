import random
n = int(random.randint(0, 5))
n1 = int(input('Pensei em um número de 0 a 5, consegue adivinhá-lo?: '))
print('O número que pensei foi o {}.'.format(n))
if n1 == n:
    print('Ótimo chute! Você acertou!')
else:
    print('Você errou! Valeu a tentativa!')
