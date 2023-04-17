sexo = str(input('Digite aqui o seu sexo [M/F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Incorreto! Digite apenas "M" (masculino) ou "F" (feminino): ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
