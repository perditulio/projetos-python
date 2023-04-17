from datetime import date
ano = int(input('Informe o ano de seu nascimento: '))
hoje = date.today().year
tempo = date.today().year - ano
falta = 18 - tempo
passou = tempo - 18
print('Quem nasceu em {} tem {} anos de idade.'.format(ano, tempo))
if tempo < 18:
    print('Você ainda vai se alistar. Falta {} ano(s) para isso.'.format(falta))
    print('Você deve se alistar no ano de {}.'.format(hoje + falta))
elif tempo > 18:
    print('Já passou da hora de você se alistar. \nJá se passaram {} ano(s) desde que você atingiu a idade para se alistar.'.format(passou))
    print('Você deeveria ter se alistado no ano de {}.'.format(hoje - passou))
else:
    print('Está na hora de você se alistar para o serviço militar orbigatório!')
