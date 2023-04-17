peso = float(input('Insira o seu peso (em Kg): '))
altura = float(input('Insira sua altura (em metros): '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
elif imc >= 40:
    print('Você está com obesidade mórbida.')
