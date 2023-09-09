'''nome = str(input('Qual é seu Nome?:'))
p = 'PARABÉNS'
if nome == 'rafael'.lower():
    print('Você tem o nome mais foda do mundo'.format(nome.title()))
elif nome == 'Pedro'.lower() or nome == 'Enzo'.lower() or nome == 'Lucas'.lower():
    print('Você é foda')
else:
    print('Seu nome é Comum?'.format(nome))
'''

num = int(input('Digite um numero inteiro: '))
print('o número {} X 1 = {}\n'
      'o número {} X 2 é {}\n'
      'o número {} X 3 é {}\n'
      'o número {} X 4 é {}\n'
      'o número {} X 5 é {}\n'
      'o número {} X 6 é {}\n'
      'o número {} X 7 é {}\n'
      'o número {} X 8 é {}\n'
      'o número {} X 9 é {}\n'
      'o número {} X 10 é {}\n'.format(num, num * 1, num, num * 2, num, num * 3, num, num * 4, num, num * 5,
                                       num, num * 6, num, num * 7, num, num * 8, num, num * 9, num, num * 10))
