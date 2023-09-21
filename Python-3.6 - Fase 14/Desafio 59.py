valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
while True:
    escolha = int(input('\nEscolha o tipo de operação:'
                        '\n[1] Somar'
                        '\n[2] Multiplicar'
                        '\n[3] Maior'
                        '\n[4] Novos Números'
                        '\n[5] Sair do programa\n'))
    if escolha == 1:
        print('O resultado da soma dos valores é: {}'.format(valor1 + valor2))

    elif escolha == 2:
        print('O resultado da multiplicação é: {}'.format(valor1 * valor2))

    elif escolha == 3:
        if valor1 > valor2:
            print('O valor {} é maior que o {}'.format(valor1,valor2))
        elif valor2 > valor1:
            print('O valor {} é maior que o {}'.format(valor2, valor1))
    elif escolha == 4:
        valor1 = int(input('Digite o valor 1 novamente: '))
        valor2 = int(input('Digite o valor 2 novamente: '))
    elif escolha == 5:
        print('Saindo...')
        break