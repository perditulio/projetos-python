from datetime import datetime
totmaior = 0
totmenor = 0
for c in range(1, 8):
    data = int(input('Digite aqui o ano de nascimento de alguém: '))
    idade = datetime.today().year - data
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))
