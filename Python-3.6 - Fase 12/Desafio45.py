'''Mexi nesse código diversas vezes e adorei a forma que ficou. e importante para minha carreira.
acredito que esteja fácil para entender também. aliás se verificar no Po eu coloquei um emoji para dizer a animação que o sistema deveria apresentar. '''

import random
from time import sleep
jogador = int(input('Vamos jogar Jo-ken-pô?\n'
                    '[ 1 ] - Pedra\n'
                    '[ 2 ] - Papel\n'
                    '[ 3 ] - Tesoura\n'
                    '-----------\n'))
jo = 1
ken = 2
po = 3
emoji = {jo: '✊', ken: '🖐️', po: '✌️'}

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po {}'.format(emoji[po]))
sleep(1)

pedra = 1
papel = 2
tesoura = 3
lista = [1, 2, 3]
pc = random.choice(lista)

if jogador == pedra and pc == tesoura:
    print('Você escolheu Pedra e o computador escolheu Tesoura. Você Ganhou!!')
elif jogador == pedra and pc == papel:
    print('Você escolheu Pedra e o computador escolheu Papel. Você Perdeu!!')
elif jogador == papel and pc == pedra:
    print('Você escolheu Papel e o computador escolheu Pedra. Você Ganhou!!')
elif jogador == papel and pc == tesoura:
    print('Você escolheu Papel e o computador escolheu Tesoura. Você Perdeu!!')
elif jogador == tesoura and pc == pedra:
    print('Você escolheu Tesoura e o computador escolheu Pedra. Você Perdeu!!')
elif jogador == tesoura and pc == papel:
    print('Você escolheu Tesoura e o computador escolheu Papel. Você Ganhou!!')
else:
    print('Você escolheu o mesmo que o computador. Empatou!!')
