'''Fibonacci'''
proximo = 1
atual = 1
anterior = 0
contador = 1
n = 0
n2 = 1
mais = int(input('Quantas vezes você quer ver o numero de fibonacci: '))
quant = 0
while mais != 0:
    quant += mais
    while contador <= quant:
        contador += 1
        print(proximo)
        proximo += anterior
        anterior = atual
        atual = proximo
    mais = int(input('Deseja ver mais algum número? 0 para sair. \n'))
print('Fim')