acumulador = 0
contador = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        acumulador += num
        contador += 1
        print('{} '.format(num), end='')
print('\nE o Total entre todos esses numeros somados é: {}'.format(acumulador), end='')


