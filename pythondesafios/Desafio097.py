def escreva(txt):
    print('~' * len(txt) + 2 * '~')
    print(txt)
    print('~' * len(txt) + 2 * '~')


escreva(f"{'  Olá, Mundo!': ^5}")
escreva(f"{'  Curso de Python no Youtube': ^5}")
