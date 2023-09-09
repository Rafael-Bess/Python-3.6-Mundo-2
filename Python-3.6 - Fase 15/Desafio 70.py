nome = str
preco = total = contpreco  = 0
barato = 50000
nomebarato = ''
while True:
    nome = str(input('Digite o nome do Produto: '))
    preco = int(input('Digite o valor do produto: R$'))
    continua = str(input('Deseja continuar? S/N: ')).upper()
    total += preco
    if preco > 1000:
        contpreco += 1
    if preco < barato:
        barato = preco
        nomebarato = nome
    if continua == 'N':
        print(f'Fim do programa. preço total {total} e o produto mais barato comprado foi {nomebarato}')
        break
