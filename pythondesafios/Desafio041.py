from datetime import datetime
ano = int(input('Digite o ano do seu nascimento: '))
idade = datetime.today().year - ano
print('Você tem {} anos de idade.'.format(idade))
if idade <= 9:
    print('De acordo com sua idade, você pertence à categoria \033[1;36mMIRIM.')
elif 9 < idade <= 14:
    print('De acordo com sua idade, você pertence à categoria \033[1;36mINFANTIL.')
elif 14 < idade <= 19:
    print('De acordo com sua idade, você pertence à categoria \033[1;36mJUNIOR.')
elif 19 < idade <= 20:
    print('De acordo com sua idade, você pertence à categoria \033[1;36mSÊNIOR.')
else:
    print('De acordo com sua idade, você pertence à categoria \033[1;36mMASTER.')
