soma = 0
contador = 0
maior_num = float('-inf')
menor_num = float('inf')
num = 1  # Inicializar num com um valor diferente de zero Inicializar num com um valor diferente de zero
while num != 0:
    while num != 0:
        num = int(input('Digite um número: '))
        if num != 0:
            soma += num
            contador += 1
        if num > maior_num:
            maior_num = num
        if num > 0:
            num < menor_num
            menor_num = num
if contador > 0:
    media = soma / contador
    print('A média dos números digitados (desconsiderando o zero) é: {:.2f}'.format(media))
    print('O maior número digitado foi: {}'.format(maior_num))
    print('O menor número digitado foi: {}'.format(menor_num))
else:
    print('Nenhum número válido foi digitado (exceto zero).')