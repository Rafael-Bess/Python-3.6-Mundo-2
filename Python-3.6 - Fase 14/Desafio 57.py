v = ''
n = input('Digite o seu sexo [M/F]: ').upper()
while n != 'M' and n != 'F':
    n = input('Digite novamente o seu sexo? [M/F]: ').upper()
if n == 'M':
    v = 'masculino'
else:
    n == 'F'
    v = 'feminino'
print("Seu sexo é {} ".format(v))