Desafio 64
soma = 0
contador = 0
numeros = []
while numeros != 999:
    numeros = int(input('Digite 999 para sair ou um número inteiro'))
    soma += numeros
    contador += 1
print('Foram digitados {} números e a soma foi: {}'.format(contador - 1, soma - 999))