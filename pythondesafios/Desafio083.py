expr = str(input('Digite uma expressão: '))
abre = []
fecha = []
for simb in expr:
    if simb == '(':
        abre.append('(')
    elif simb == ')':
        fecha.append(')')
if len(abre) == len(fecha):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está incorreta!')
