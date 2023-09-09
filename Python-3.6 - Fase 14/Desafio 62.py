Desafio 62
print('{}{}{}'.format(20 *'=', '\n10 termos de uma PA\n', 20 * '='))
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end=' -> ')
        termo += razao
        cont += 1
    print('Pausa \n0 - Sair')
    mais = int(input('Gostaria de quantos termos à mais? '))
print('Fim')