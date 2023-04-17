dados = {}
golslist = []
tot = 0
dados['nome'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for p in range(1, dados['partidas'] + 1):
    gols = (int(input(f'Quantos gols na partida {p}? ')))
    golslist.append(gols)
    tot += gols
    dados['gols'] = golslist
    dados['total'] = tot
print('-=' * 20)
print(dados)
print('-=' * 20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas.')
for p, g in enumerate(golslist):
    print(f'  =>Na partida {p+1}, fez {g} gols.')
print(f'Foi um total de {dados["total"]} gols.')
