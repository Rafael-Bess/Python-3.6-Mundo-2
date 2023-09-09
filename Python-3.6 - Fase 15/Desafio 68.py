import random
from random import randint
from time import sleep
num = resultado = cont = 0
print('Vamos jogar par ou impar')
while True:
    num = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar? [P/I]')).upper()
    computador = random.randint(1, 10)
    resultado = num + computador
    if escolha == 'P' and resultado % 2 == 0:
        print(f'Você escolheu {num} e o PC {computador} foi Par {resultado}')
        print('Você Ganhou!!')
        cont += 1
    elif escolha == 'I' and resultado % 2 != 0:
        print(f'Você escolheu {num} e o PC {computador} foi Impar {resultado}')
        print('Você Ganhou!!')
        cont += 1
    else:
        print(f'O computador escolheu {computador} e você {num}')
        print(f'Game Over! Você ganhou {cont} seguidas')
        break
