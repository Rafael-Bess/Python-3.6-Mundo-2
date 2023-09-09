print('{}{}{}'.format(20 *'=', '\n10 termos de uma PA\n', 20 * '='))
ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
decimo = ptermo + (10 - 1) * razao
a = ptermo
while a <= decimo:
    a += razao
    print(a)