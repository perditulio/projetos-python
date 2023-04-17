brasileirao = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
               'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
               'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional',
               'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio',
               'Bahia', 'Sport Recife', 'Chapecoense')
print(f'Os 5 primeiros colocados do Brasileirão 2021 são: {brasileirao[0:5]}')
print(f'Foram rebaixados os times: {brasileirao[16:20]}')
print(f'Os times em ordem alfabética: {sorted(brasileirao)}')
print(f'A chapecoense é o {brasileirao.index("Chapecoense") + 1}º colocado.')
