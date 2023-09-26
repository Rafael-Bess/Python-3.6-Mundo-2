num = int(input('Digite o valor que quer sacar: R$ '))
total = num
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'O total da {totced} cédulas de {ced}')
        if ced == 50:
            ced = 20
            totced = 0
        elif ced == 20:
            ced = 10
            totced = 0
        elif ced == 10:
            ced = 5
            totced = 0
        elif ced == 5:
            ced = 1
            totced = 0
        if total == 0:
            break
print('FIM DO MUNDO 2')
