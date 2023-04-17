titulo = ('MÉDIA DE UM ALUNO')
print(' {:=^50} '.format(titulo))
nome = str(input('Digite o seu nome: '))
print('Olá, {}! Seja bem vindo(a)! Vamos calcular a média de suas notas?'.format(nome))
n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
m = (n1 + n2) / 2
print('A média de suas notas é: {:.1f} '.format(m))
