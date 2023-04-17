print(20 * '-', 'GERADOR DE PA', 20 * '-')
p1 = int(input('Primeiro termo:'))
r = int(input('Razão da PA: '))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
