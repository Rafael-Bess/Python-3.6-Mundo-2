from datetime import date

cont = 0
dtatual = date.today().year
cont2 = 0
for c in range(1, 8):
        dtnasci = int(input('Em que ano a {}º Pessoa nasceu? '.format(c)))
        idade = dtatual - dtnasci
        if idade <= 18:
            cont += 1
        else:
            cont2 += 1
print('Ao todo tivemos {} maiores de idade e {} menores de idade'.format(cont, cont2))


'''
refiz da mesma forma do guanabara


from datetime import date
cont = 0
cont2 = 0
dtatual = date.today().year
for c in range(1, 8):
    nasc = int((input('Em que ano a {}º Pessoa nasceu? '.format(c))))
    idade = dtatual - nasc
    if idade >= 21:
        cont += 1
    else:
        cont2 +=1
print('Ao todo tivemos {} maiores de idade e {} menores de idade'.format(cont, cont2))
'''