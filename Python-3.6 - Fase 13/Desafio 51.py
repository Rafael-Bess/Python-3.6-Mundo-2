print('{}{}{}'.format(20 *'=', '\n10 termos de uma PA\n', 20 * '='))
ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
décimo = ptermo + (10 - 1) * razao
for c in range(ptermo, décimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Acabou!!')


