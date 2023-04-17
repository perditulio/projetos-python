def area(largura, comprimento):
    totarea = largura * comprimento
    print(f'A área de um terreno {largura} X {comprimento} é de {totarea}m².')


area(largura=float(input('LARGURA (m): ')), comprimento=float(input('COMPRIMENTO (m): ')))
