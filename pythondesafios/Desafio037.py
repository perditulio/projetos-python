numero = int(input('Digite o número que você deseja converter: ' ))
conversao = int(input('Digite "1" para converter para binário, "2" para octal e "3" para hexadecimal: '))
if conversao == 1:
    print('O número {} convertido para binário é: {}'.format(numero, format(numero, 'b')))
elif conversao == 2:
    print('O número {} convertido para octal é: {}'.format(numero, format(numero, 'o')))
elif conversao == 3:
    print('O número {} convertido para hexadecimal é: {}'.format(numero, format(numero, 'x')))
else:
    print('Opção INVÁLIDA. Você não escolheu nenhuma das três opções para conversão disponíveis.')
