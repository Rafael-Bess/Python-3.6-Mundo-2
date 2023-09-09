from time import sleep
frase = str(input('Digite uma Frase para verificar se é um palindromo: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
frase_invertida = frase[::-1]
inverso = ''
print('Você digitou a frase {}, ela ao contrario fica {}'.format(frase, frase_invertida))
print('Verificando se é um palindromo... ')
sleep(1)
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
if inverso == junto:
    print('Ele é um palindromo!')
else:
    print('Ele não é um Palindromo')


    '''da pra fazer apenas com if e else, utilizando o frase_invertida é == junto'''