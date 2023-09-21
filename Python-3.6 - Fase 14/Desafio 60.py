numero = int(input('Digite o número desejado para ver o fatorial:' ))
contador = numero - 1
numerofat = numero
if numero == 0:
    print('O número inserido não tem fatorial.')
while contador >= 1:
    numerofat *= contador
    contador -= 1
print('O número que você inseriu foi {} e o fatorial dele é {}'.format(numero, numerofat))