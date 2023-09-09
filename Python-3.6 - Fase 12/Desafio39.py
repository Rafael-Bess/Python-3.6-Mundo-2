from datetime import date
nome = str(input('Digite seu nome: ')).title()
dtnasci = int(input('Digite o Ano do seu nascimento: '))
dtatual = date.today().year
idade = int(dtatual - dtnasci)
atual = int(dtnasci + 18)
falta = (atual - idade - dtnasci)
if idade <= 15:
    print('Você ainda não pode se alistar, somente no ano de {}\n'
          'faltam {} anos'.format(atual, falta))
elif idade == 16 and idade == 17:
    print('{} Você já tem {} e pode realizar a inscrição para o alistamento obrigatório\n'
          '{} ano(s) para expirar'.format(nome, idade, falta))
elif idade == 18:
    print('{} Você precisa se Comparecer a junta militar para o alistamento obrigatório'.format(nome))
else:
    print('Seu prazo de alistamento expirou\n'
          'data de expiração {} '.format(atual))
