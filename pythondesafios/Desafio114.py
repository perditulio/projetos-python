from urllib import request

try:
    site = request.urlopen('http://www.pudim.com.br')
except:
    print('Não consegui acessar o site do pudim.')
else:
    print('Consegui acessar o site do pudim com sucesso.')
