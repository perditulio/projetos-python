aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno["Média"] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 5 <= aluno["Média"] < 7:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
print('-=' * 20)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')

