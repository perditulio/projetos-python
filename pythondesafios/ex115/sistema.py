from lib.interface import *
from lib.dados import *
from time import sleep

nome_arquivo = 'dados.txt'

if not arquivoExiste(nome_arquivo):
    criarArquivo(nome_arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerdados(nome_arquivo)
    elif resposta == 2:
        cabeçalho('Cadastrar Pessoas')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar(nome_arquivo, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)
