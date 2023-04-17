nota1 = float(input('Digite aqui a nota da primeira avaliação: '))
nota2 = float(input('Digite aqui a nota da segunda avaliação: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('A média das suas notas é de {:.1f} pontos.'.format(media))
    print('Situação: \033[1;31mREPROVADO. ESTUDE MAIS.')
elif 5 <= media <= 6.9:
    print('A média das suas notas é de {:.1f} pontos.'.format(media))
    print('Situação: \033[1;33mRECUPERAÇÃO. ESTUDE MAIS')
elif media >= 7:
    print('A média das suas notas é de {:.1f} pontos.'.format(media))
    print('Situação: \033[1;32mAPROVADO. PARABÉNS!')
