cont = numero = 0
while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero >= 1:
        for c in range(1, 11):
            cont += 1
            print(f'{numero} X {cont} = {numero * cont}')
    if numero == 0:
        print('O número digitado foi zero, por favor digite novamente: ')
    if numero < 0:
        print('Fim do programa volte sempre! ')
        break
