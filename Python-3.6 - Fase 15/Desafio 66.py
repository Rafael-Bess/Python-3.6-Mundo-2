'''n = s = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
F string a utilização é assim: print(f'A soma vale {s}')
para fazer a formatação é print(f'O {nome} tem {idade} anos e ganha R${salário:.2f}')'''
'''
Desafio 66:
'''
numero = soma = cont = 0
while True:
    numero = int(input('Digite os números que deseja somar. (999 para sair) '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'A soma dos {cont} números foi {soma}')