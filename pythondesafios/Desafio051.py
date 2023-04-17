a1 = float(input('Digite aqui o primeiro termo para calcularmos uma PA: '))
r = float(input('Digite aqui a razão desejada para a PA: '))
for c in range(1, 11):
    print(a1 + (c - 1) * r)
