from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
dados['idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
carteira = int(input('Carteira de Trabalho (0 caso não tenha): '))
if carteira == 0:
    dados['ctps'] = carteira
    print('-=' * 30)
    for k, v in dados.items():
        print(f'-{k} tem o valor {v}')
else:
    dados['ctps'] = carteira
    dados['contrataçao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrataçao'] + 35) - datetime.now().year)
    print('-=' * 30)
    for k, v in dados.items():
        print(f'-{k} tem o valor {v}')
