from random import randint
escolhido = 0
numero = randint(1, 10)
cont = 0
while escolhido != numero:
    escolhido = int(input('Insira um número de 1 a 10: '))
    cont += 1
print('O número escolhido pelo computador foi {} você acertou na {}ª tentativa'.format(numero, cont))
if cont == 1:
    print("Parabéns você é o maior adivinhador de todos")