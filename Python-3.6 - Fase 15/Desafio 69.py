idade = 0
sexo = continua = str
cont1 = cont2 = cont3 = 0
print(25 * '=', 'Vamos cadastrar uma Pessoa?', '=' * 25)
while True:
    idade = int(input('Digite a sua Idade: '))
    sexo = (input('Digite o seu SEXO M/F: ')).upper()
    print(25 * '=')
    continua = (input('Deseja continuar? S/N: ')).upper()
    print(25 * '=')
    if idade > 18:
        cont1 += 1
    if sexo == 'M':
        cont2 += 1
    if sexo == 'F' and idade < 20:
        cont3 += 1
    if continua == 'N':
        print('Fim do programa. Resultado: ')
        break
print(f'Existem {cont1} pessoas maiores de 18')
print(f'Existem {cont2} Homens cadastrados')
print(f'Existem {cont3} Mulher com menos de 20 anos')

