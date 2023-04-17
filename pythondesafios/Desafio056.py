medidade = 0
velho = 0
homemvelho = 0
totmulher = 0
for c in range(1, 5):
    print(5 * '-', '{}ª PESSOA'.format(c), 5 * '-')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (masculino ou feminino): ')).strip().upper()
    medidade += idade
    if c == 1 and sexo == 'MASCULINO':
        velho = idade
        homemvelho = nome
    else:
        if idade > velho and sexo == 'MASCULINO':
            velho = idade
            homemvelho = nome
    if sexo == 'FEMININO' and idade < 20:
        totmulher += 1
médiatot = medidade / 4
print('A média das idades dessas pessoas é de {:.1f} anos.'.format(médiatot))
print('O homem mais velho é {} com {} anos.'.format(homemvelho, velho))
print('Há {} mulher(es) com menos de 20 anos.'.format(totmulher))
