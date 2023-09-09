A1 = float(input('Insira a primeira nota: '))
A2 = float(input('Insira a segunda nota: '))
A3 = float(input('Insira a terceira nota: '))
R = (A1 + A2 + A3) / 3
if R <= 4.9:
    print('Você foi reprovado sua nota foi de {:.1f}'.format(R))
elif 5.0 <= R <= 6.9:
    print('Voce ficou de recuperação. sua nota foi de {:.1f}'.format(R))
else:
    print('Voce foi Aprovado Sua nota foi de {:.1f}'.format(R))
