def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 16 <= idade < 18 or idade > 60:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif 18 <= idade < 60:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'


# Programa principal
print(50 * '-')
nasc = (int(input('Informe o ano de nascimento: ')))
print(voto(nasc))
