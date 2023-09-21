num = int(input('Digite um número inteiro: '))
acumulador = 0
for c in range(1, num + 1):
    if num % c == 0:
        acumulador += 1
        print('\033[91m {}'.format(c), end='')
    else:
        print('\033[34m {}'.format(c), end='')
if acumulador == 2:
    print('\n\033[mO número foi divisvel foi {} vezes e não é primo'.format(acumulador))
else:
    print('\n\033[mO número foi divisvel {} e ele é primo'.format(acumulador))
