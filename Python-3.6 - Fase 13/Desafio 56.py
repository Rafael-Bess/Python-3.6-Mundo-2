maior_idade_homem = 0
nomevelho = 0
calculo = 0
media = 0
contador_mulher = 0
for c in range(1, 5):
    print('------ {}a Pessoa ------'.format(c))
    nome = str(input('\nNome: ')).strip().title()
    idade = int(input('\nIdade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().title()
    calculo += idade
    media = calculo / 4
    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <= 19:
        contador_mulher += 1
print('A média de idade do grupo é {} '.format(media))
print('O nome do Homem mais velho é {} e possui {} anos'.format(nomevelho.title(), maior_idade_homem))
print('A quantidade de mulheres com menos de 20 é: {}'.format(contador_mulher))


