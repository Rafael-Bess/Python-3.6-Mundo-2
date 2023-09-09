acumulador = 0
contador = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número:'.format(c)))
    if num % 2 == 0:
        acumulador += num
        contador += 1
print('\nVocê informou {} números pares, e a soma é: {}'.format(contador, acumulador))
