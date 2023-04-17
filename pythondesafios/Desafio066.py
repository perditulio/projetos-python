n = cont = s =0
while True:
    n = int(input('Digite um número [999 para finalizar]: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram digitados {cont} números e soma entre eles é {s} .')
