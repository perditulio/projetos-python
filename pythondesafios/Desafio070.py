soma = barato = caro = cont = nome = 0
while True:
    produto = str(input('Qual o produto que deseja comprar? '))
    preco = float(input('Digite o valor deste produto: R$'))
    opcao = str(input('Deseja adicionar mais algum produto? [S/N]: ')).strip().upper()
    cont += 1
    soma += preco
    if cont == 1 or preco < barato:
        barato = preco
        nome = produto
    if preco > 1000:
        caro += 1
    if opcao == 'N':
        break
print(40 * '=')
print(f'''O total gasto na sua compra foi de R${soma:.2f};
{caro} produtos custam mais de R$1000.00;
O produto mais barato comprado é o(a) {nome}, que custou R${barato:.2f}.''')