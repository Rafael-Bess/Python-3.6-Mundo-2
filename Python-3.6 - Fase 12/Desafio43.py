peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua Altura: '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('Abaixo do Peso seu IMC é: {:.1f}'.format(imc))

elif 18.5 <= imc <= 24.9:
    print('Peso Ideal seu IMC é: {:.1f}'.format(imc))

elif 25.0 <= imc <= 29.9:
    print('Sobrepeso seu IMC é: {:.1f}'.format(imc))

elif 30.0 <= imc <= 39.9:
    print('Obesidade seu IMC é: {:.1f}'.format(imc))

else:
    if imc >= 40:
        print('Obesidade Mórbida seu IMC é: {:.1f}'.format(imc))
